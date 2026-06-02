param(
    [string]$Path = "design/c4",
    [string]$DrawioExe = "C:\Program Files\draw.io\draw.io.exe",
    [switch]$ValidateOnly
)

$ErrorActionPreference = "Stop"

function Get-LinkedCells {
    param([string]$DrawioPath)

    [xml]$xml = Get-Content -Raw -LiteralPath $DrawioPath
    $cells = @{}
    foreach ($cell in $xml.SelectNodes("//mxCell")) {
        if ($cell.id) {
            $cells[$cell.id] = $cell
        }
    }

    function Get-Geometry {
        param($Cell)

        $geometry = $Cell.mxGeometry
        if ($null -eq $geometry) {
            return $null
        }

        $x = if ($geometry.x) { [double]$geometry.x } else { 0.0 }
        $y = if ($geometry.y) { [double]$geometry.y } else { 0.0 }
        $width = if ($geometry.width) { [double]$geometry.width } else { 0.0 }
        $height = if ($geometry.height) { [double]$geometry.height } else { 0.0 }

        $parentId = $Cell.parent
        while ($parentId -and $cells.ContainsKey($parentId)) {
            $parent = $cells[$parentId]
            $parentGeometry = $parent.mxGeometry
            if ($null -ne $parentGeometry) {
                $x += if ($parentGeometry.x) { [double]$parentGeometry.x } else { 0.0 }
                $y += if ($parentGeometry.y) { [double]$parentGeometry.y } else { 0.0 }
            }
            $parentId = $parent.parent
        }

        [pscustomobject]@{
            X = $x
            Y = $y
            Width = $width
            Height = $height
        }
    }

    $vertexCells = @()
    foreach ($cell in $cells.Values) {
        if ($cell.vertex -eq "1") {
            $geometry = Get-Geometry -Cell $cell
            if ($null -ne $geometry -and $geometry.Width -gt 0 -and $geometry.Height -gt 0) {
                $vertexCells += [pscustomobject]@{
                    Id = $cell.id
                    Geometry = $geometry
                    Link = $cell.link
                }
            }
        }
    }

    if ($vertexCells.Count -eq 0) {
        return @()
    }

    $minX = $vertexCells[0].Geometry.X
    $minY = $vertexCells[0].Geometry.Y
    foreach ($vertex in $vertexCells) {
        if ($vertex.Geometry.X -lt $minX) {
            $minX = $vertex.Geometry.X
        }
        if ($vertex.Geometry.Y -lt $minY) {
            $minY = $vertex.Geometry.Y
        }
    }

    $linkedCells = foreach ($vertex in $vertexCells) {
        if ($vertex.Link) {
            [pscustomobject]@{
                Id = $vertex.Id
                Link = $vertex.Link
                X = $vertex.Geometry.X - $minX
                Y = $vertex.Geometry.Y - $minY
                Width = $vertex.Geometry.Width
                Height = $vertex.Geometry.Height
            }
        }
    }

    @($linkedCells)
}

function Set-ContentWithRetry {
    param(
        [string]$Path,
        [string]$Value
    )

    for ($attempt = 1; $attempt -le 10; $attempt++) {
        try {
            Set-Content -LiteralPath $Path -Value $Value -NoNewline
            return
        } catch [System.IO.IOException] {
            if ($attempt -eq 10) {
                throw
            }
            Start-Sleep -Milliseconds 500
        }
    }
}

function Add-LinkOverlays {
    param(
        [string]$SvgPath,
        [array]$LinkedCells
    )

    $svg = Get-Content -Raw -LiteralPath $SvgPath
    $svg = [regex]::Replace(
        $svg,
        '(?s)\s*<g id="diagram-navigation-links" data-generated-by="tools/diagrams/export-drawio-svg\.ps1">.*?</g>\s*(?=</svg>)',
        ''
    )

    if ($LinkedCells.Count -eq 0) {
        Set-ContentWithRetry -Path $SvgPath -Value $svg
        return
    }

    $overlay = New-Object System.Text.StringBuilder
    [void]$overlay.AppendLine('<g id="diagram-navigation-links" data-generated-by="tools/diagrams/export-drawio-svg.ps1">')
    foreach ($cell in $LinkedCells) {
        $href = [System.Security.SecurityElement]::Escape($cell.Link)
        $id = [System.Security.SecurityElement]::Escape($cell.Id)
        $x = $cell.X.ToString("0.###", [System.Globalization.CultureInfo]::InvariantCulture)
        $y = $cell.Y.ToString("0.###", [System.Globalization.CultureInfo]::InvariantCulture)
        $width = $cell.Width.ToString("0.###", [System.Globalization.CultureInfo]::InvariantCulture)
        $height = $cell.Height.ToString("0.###", [System.Globalization.CultureInfo]::InvariantCulture)
        [void]$overlay.AppendLine("  <a data-cell-id=`"$id`" xlink:href=`"$href`" href=`"$href`" target=`"_self`"><rect x=`"$x`" y=`"$y`" width=`"$width`" height=`"$height`" fill=`"#ffffff`" fill-opacity=`"0`" stroke=`"none`" pointer-events=`"all`"/></a>")
    }
    [void]$overlay.Append('</g>')

    $updated = $svg -replace '</svg>\s*$', "$($overlay.ToString())</svg>"
    Set-ContentWithRetry -Path $SvgPath -Value $updated
}

function Test-LinkOverlays {
    param(
        [string]$SvgPath,
        [array]$LinkedCells
    )

    $svg = Get-Content -Raw -LiteralPath $SvgPath
    $missing = @()
    foreach ($cell in $LinkedCells) {
        if (-not $svg.Contains("data-cell-id=`"$($cell.Id)`"") -or -not $svg.Contains("href=`"$($cell.Link)`"")) {
            $missing += $cell
        }
    }

    $missing
}

if (-not (Test-Path -LiteralPath $Path)) {
    throw "Path not found: $Path"
}

if (-not $ValidateOnly -and -not (Test-Path -LiteralPath $DrawioExe)) {
    throw "Draw.io executable not found: $DrawioExe"
}

$drawioFiles = if ((Get-Item -LiteralPath $Path).PSIsContainer) {
    Get-ChildItem -Path $Path -Recurse -Filter "*.drawio"
} else {
    Get-Item -LiteralPath $Path
}

$failed = @()
foreach ($drawioFile in $drawioFiles) {
    $svgPath = [System.IO.Path]::ChangeExtension($drawioFile.FullName, ".svg")
    $linkedCells = @(Get-LinkedCells -DrawioPath $drawioFile.FullName)

    if (-not $ValidateOnly) {
        & $DrawioExe --export --format svg --svg-links-target same-win --output $svgPath $drawioFile.FullName | Out-Null
        Add-LinkOverlays -SvgPath $svgPath -LinkedCells $linkedCells
    }

    if (-not (Test-Path -LiteralPath $svgPath)) {
        $failed += "$($drawioFile.FullName): missing SVG export"
        continue
    }

    $missing = @(Test-LinkOverlays -SvgPath $svgPath -LinkedCells $linkedCells)
    if ($missing.Count -gt 0) {
        $failed += "$($drawioFile.FullName): missing link overlays for cells $((($missing | ForEach-Object { $_.Id }) -join ', '))"
    }

    Write-Output "$($drawioFile.FullName): links=$($linkedCells.Count), svg=$svgPath"
}

if ($failed.Count -gt 0) {
    $failed | ForEach-Object { Write-Error $_ }
    exit 1
}
