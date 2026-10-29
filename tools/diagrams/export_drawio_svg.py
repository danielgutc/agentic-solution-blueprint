"""Export simple Draw.io views to linked SVGs.

This intentionally supports a small, deterministic subset of Draw.io XML.
Unsupported features fail instead of producing a partial SVG.
"""

from __future__ import annotations

import argparse
from collections import Counter
import sys
from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree as ET


ROOT = Path(__file__).resolve().parents[2]
SVG_NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG_NS)


def discover(root: Path) -> tuple[Path, ...]:
    design = root / "design"
    return tuple(sorted(design.rglob("*.drawio"))) if design.is_dir() else ()


# Kept as a module value for callers that select a fixed project inventory.
SOURCES = discover(ROOT)


@dataclass
class Vertex:
    ident: str
    label: str
    x: float
    y: float
    width: float
    height: float
    style: dict[str, str]
    link: str | None


@dataclass
class Edge:
    ident: str
    label: str
    source: str
    target: str
    style: dict[str, str]
    points: list[tuple[float, float]]


def svg(tag: str, attributes: dict[str, str] | None = None, parent: ET.Element | None = None) -> ET.Element:
    full_tag = f"{{{SVG_NS}}}{tag}"
    return ET.SubElement(parent, full_tag, attributes or {}) if parent is not None else ET.Element(full_tag, attributes or {})


def num(value: float) -> str:
    return f"{value:.2f}".rstrip("0").rstrip(".")


def parse_style(value: str) -> dict[str, str]:
    result = {}
    for part in value.split(";"):
        if part and "=" in part:
            key, item = part.split("=", 1)
            result[key] = item
        elif part:
            result[part] = "1"
    allowed = {
        "rounded", "whiteSpace", "html", "fillColor", "strokeColor", "fontColor",
        "fontSize", "fontFamily", "align", "verticalAlign", "spacing",
        "spacingLeft", "spacingTop", "text", "edgeStyle", "strokeWidth",
        "endArrow", "endFill", "labelBackgroundColor", "exitY", "exitX",
        "entryY", "entryX", "exitDx", "exitDy", "entryDx", "entryDy",
    }
    unknown = set(result) - allowed
    if unknown:
        raise ValueError(f"unsupported Draw.io styles: {sorted(unknown)}")
    for key in ("exitDx", "exitDy", "entryDx", "entryDy"):
        if key in result and float(result[key]) != 0:
            raise ValueError(f"unsupported Draw.io endpoint offset: {key}={result[key]}")
    return result


def read_source(path: Path) -> tuple[float, float, list[Vertex], list[Edge]]:
    tree = ET.parse(path)
    model = tree.find("./diagram/mxGraphModel")
    if model is None:
        raise ValueError(f"{path}: expected an uncompressed mxGraphModel")
    root = model.find("root")
    if root is None:
        raise ValueError(f"{path}: missing graph root")
    vertices = []
    edges = []
    for child in root:
        wrapper = child if child.tag == "UserObject" else None
        cell = child.find("mxCell") if wrapper is not None else child
        if cell is None or cell.tag != "mxCell":
            continue
        if cell.get("vertex") == "1":
            geometry = cell.find("mxGeometry")
            if geometry is None:
                raise ValueError(f"{path}: vertex without geometry")
            vertices.append(
                Vertex(
                    ident=(wrapper.get("id") if wrapper is not None else cell.get("id")) or "",
                    label=(wrapper.get("label") if wrapper is not None else cell.get("value")) or "",
                    x=float(geometry.get("x", "0")),
                    y=float(geometry.get("y", "0")),
                    width=float(geometry.get("width", "0")),
                    height=float(geometry.get("height", "0")),
                    style=parse_style(cell.get("style", "")),
                    link=wrapper.get("link") if wrapper is not None else cell.get("link"),
                )
            )
        elif cell.get("edge") == "1":
            geometry = cell.find("mxGeometry")
            points = []
            if geometry is not None:
                for point in geometry.findall("./Array[@as='points']/mxPoint"):
                    points.append((float(point.get("x", "0")), float(point.get("y", "0"))))
            edges.append(
                Edge(
                    ident=cell.get("id", ""),
                    label=cell.get("value", ""),
                    source=cell.get("source", ""),
                    target=cell.get("target", ""),
                    style=parse_style(cell.get("style", "")),
                    points=points,
                )
            )
    ids = [vertex.ident for vertex in vertices]
    if len(ids) != len(set(ids)):
        raise ValueError(f"{path}: duplicate vertex IDs")
    if any(edge.source not in ids or edge.target not in ids for edge in edges):
        raise ValueError(f"{path}: edge points to an unknown vertex")
    return float(model.get("pageWidth", "1280")), float(model.get("pageHeight", "720")), vertices, edges


def add_text(parent: ET.Element, vertex: Vertex) -> None:
    lines = vertex.label.splitlines() or [""]
    font_size = float(vertex.style.get("fontSize", "16"))
    line_height = font_size * 1.28
    left = vertex.style.get("align") == "left"
    top = vertex.style.get("verticalAlign") == "top"
    x = vertex.x + float(vertex.style.get("spacingLeft", "12")) if left else vertex.x + vertex.width / 2
    y = vertex.y + float(vertex.style.get("spacingTop", "12")) + font_size if top else vertex.y + vertex.height / 2 - (len(lines) - 1) * line_height / 2
    text = svg(
        "text",
        {
            "x": num(x), "y": num(y), "text-anchor": "start" if left else "middle",
            "dominant-baseline": "middle", "font-family": vertex.style.get("fontFamily", "Arial"),
            "font-size": num(font_size), "fill": vertex.style.get("fontColor", "#172B4D"),
        },
        parent,
    )
    for index, line in enumerate(lines):
        span = svg("tspan", {"x": num(x), "dy": "0" if index == 0 else num(line_height)}, text)
        span.text = line


def add_vertex(parent: ET.Element, vertex: Vertex, *, include_text: bool = True) -> None:
    group = svg("a", {"href": vertex.link, "target": "_self"}, parent) if vertex.link else parent
    if vertex.style.get("text") != "1":
        svg(
            "rect",
            {
                "x": num(vertex.x), "y": num(vertex.y), "width": num(vertex.width),
                "height": num(vertex.height),
                "rx": "12" if vertex.style.get("rounded") == "1" else "0",
                "fill": vertex.style.get("fillColor", "#FFFFFF").replace("none", "transparent"),
                "stroke": vertex.style.get("strokeColor", "#315B8A").replace("none", "transparent"),
                "stroke-width": "2",
            },
            group,
        )
    if include_text:
        add_text(group, vertex)


def endpoint(source: Vertex, target: Vertex, style: dict[str, str], prefix: str) -> tuple[float, float]:
    x_key, y_key = f"{prefix}X", f"{prefix}Y"
    if x_key in style and y_key in style:
        return source.x + float(style[x_key]) * source.width, source.y + float(style[y_key]) * source.height
    sx, sy = source.x + source.width / 2, source.y + source.height / 2
    tx, ty = target.x + target.width / 2, target.y + target.height / 2
    if abs(tx - sx) >= abs(ty - sy):
        return (source.x + source.width if tx > sx else source.x), sy
    return sx, (source.y + source.height if ty > sy else source.y)


def add_edge(parent: ET.Element, edge: Edge, vertices: dict[str, Vertex]) -> None:
    source, target = vertices[edge.source], vertices[edge.target]
    start = endpoint(source, target, edge.style, "exit")
    end = endpoint(target, source, edge.style, "entry")
    path_points = [start, *edge.points, end]
    command = "M " + " L ".join(f"{num(x)} {num(y)}" for x, y in path_points)
    svg("path", {"d": command, "fill": "none", "stroke": edge.style.get("strokeColor", "#315B8A"), "stroke-width": edge.style.get("strokeWidth", "2"), "marker-end": "url(#arrow)"}, parent)
    if edge.label:
        a, b = (path_points[0], path_points[-1]) if len(path_points) == 2 else (path_points[len(path_points) // 2 - 1], path_points[len(path_points) // 2])
        x, y = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2 - 9
        width = max(70, len(edge.label) * 6.8)
        svg("rect", {"x": num(x - width / 2), "y": num(y - 12), "width": num(width), "height": "22", "fill": "#FFFFFF", "opacity": "0.95"}, parent)
        label = svg("text", {"x": num(x), "y": num(y), "text-anchor": "middle", "font-family": "Arial", "font-size": "12", "fill": "#172B4D"}, parent)
        label.text = edge.label


def render(source: Path) -> bytes:
    width, height, vertices, edges = read_source(source)
    document = svg("svg", {"width": num(width), "height": num(height), "viewBox": f"0 0 {num(width)} {num(height)}", "role": "img", "aria-label": source.stem.replace("-", " ")})
    svg("rect", {"width": num(width), "height": num(height), "fill": "#FFFFFF"}, document)
    defs = svg("defs", parent=document)
    marker = svg("marker", {"id": "arrow", "viewBox": "0 0 10 10", "refX": "9", "refY": "5", "markerWidth": "8", "markerHeight": "8", "orient": "auto-start-reverse"}, defs)
    svg("path", {"d": "M 0 0 L 10 5 L 0 10 z", "fill": "#315B8A"}, marker)
    vertex_map = {vertex.ident: vertex for vertex in vertices}
    background_ids = {
        vertex.ident for vertex in vertices
        if any(other.ident != vertex.ident and vertex.x <= other.x and vertex.y <= other.y and
               vertex.x + vertex.width >= other.x + other.width and
               vertex.y + vertex.height >= other.y + other.height for other in vertices)
    }
    for vertex in vertices:
        if vertex.ident in background_ids:
            add_vertex(document, vertex, include_text=False)
    for edge in edges:
        add_edge(document, edge, vertex_map)
    for vertex in vertices:
        if vertex.ident not in background_ids:
            add_vertex(document, vertex)
    for vertex in vertices:
        if vertex.ident in background_ids:
            add_text(document, vertex)
    ET.indent(document, space="  ")
    return ET.tostring(document, encoding="utf-8", xml_declaration=True) + b"\n"


def source_links(source: Path) -> tuple[str, ...]:
    """Read drill-down links without applying the portable renderer's style limits."""
    root = ET.parse(source).find("./diagram/mxGraphModel/root")
    if root is None:
        raise ValueError(f"{source}: missing uncompressed graph root")
    links = []
    for child in root:
        cell = child.find("mxCell") if child.tag == "UserObject" else child
        if cell is not None and cell.get("vertex") == "1":
            link = child.get("link")
            if link:
                links.append(link)
    return tuple(links)


def validate_links(source: Path) -> None:
    for link in source_links(source):
        if not (source.with_suffix(".svg").parent / link).resolve().is_file():
            raise ValueError(f"{source}: broken diagram link {link}")


def canonical_model(document: ET.Element) -> str:
    model = document.find("./diagram/mxGraphModel")
    if model is None:
        raise ValueError("expected an uncompressed mxGraphModel")
    normalized = ET.fromstring(ET.tostring(model, encoding="utf-8"))
    for attribute in ("dx", "dy"):
        normalized.attrib.pop(attribute, None)
    return ET.canonicalize(ET.tostring(normalized, encoding="unicode"), strip_text=True)


def has_source_links(source: Path, document: ET.Element) -> bool:
    required = Counter(source_links(source))
    actual = Counter(
        anchor.get("href") or anchor.get("{http://www.w3.org/1999/xlink}href")
        for anchor in document.iter(f"{{{SVG_NS}}}a")
    )
    return all(actual[link] >= count for link, count in required.items())


def is_current_svg(source: Path, output: Path, expected: bytes | None = None) -> bool:
    if not output.is_file():
        return False
    content = output.read_bytes()
    if content == expected:
        return True
    try:
        document = ET.fromstring(content)
        if document.tag != f"{{{SVG_NS}}}svg":
            return False
        embedded = document.get("content")
        if not embedded:
            return False
        return (canonical_model(ET.parse(source).getroot()) ==
                canonical_model(ET.fromstring(embedded)) and
                has_source_links(source, document))
    except (ET.ParseError, ValueError):
        return False


def selected_sources(root: Path, values: list[str]) -> tuple[Path, ...]:
    if values:
        return tuple((Path(value) if Path(value).is_absolute() else root / value) for value in values)
    return SOURCES if root == ROOT else discover(root)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail when an SVG is missing or stale")
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root (default: this tool's repository)")
    parser.add_argument("sources", nargs="*", help="optional .drawio files relative to --root")
    args = parser.parse_args()
    root = args.root.resolve()
    sources = selected_sources(root, args.sources)
    missing = [source for source in sources if not source.is_file()]
    if missing:
        for source in missing:
            print(f"missing Draw.io source: {source}", file=sys.stderr)
        return 1
    stale = []
    for source in sources:
        output = source.with_suffix(".svg")
        if args.check:
            if is_current_svg(source, output):
                continue
            try:
                result = render(source)
            except ValueError:
                # Native-only features require a matching native export.
                stale.append(output)
                continue
            if not is_current_svg(source, output, result):
                stale.append(output)
        else:
            output.write_bytes(render(source))
    for source in sources:
        validate_links(source)
    if stale:
        for output in stale:
            try:
                name = output.relative_to(root)
            except ValueError:
                name = output
            print(f"stale or missing SVG: {name}", file=sys.stderr)
        return 1
    print(f"{'Validated' if args.check else 'Exported'} {len(sources)} Draw.io/SVG pairs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
