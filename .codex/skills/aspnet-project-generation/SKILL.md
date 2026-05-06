---
name: aspnet-project-generation
description: Scaffold ASP.NET Core implementation projects with repository-aligned solution layout, source boundaries, generated output routing, and validation. Use when creating a new ASP.NET Core service or application under implementation/.
---

# ASP.NET Project Generation Skill

Use this skill when creating a new ASP.NET Core runtime project in `implementation/`.

## Goals

- Keep source code under the implementation component `src/` folder.
- Keep generated build outputs outside `src/`.
- Preserve repository workflow gates before runtime implementation starts.
- Produce a buildable skeleton before adding behavior.

## Prechecks

1. Confirm the target implementation gate is approved.
2. Confirm the target implementation component root, for example `implementation/<component>/`.
3. Confirm the app model: controller-based Web API, Minimal API, gRPC, worker, or another ASP.NET Core template.
4. Confirm the target framework from repository context; default to the latest stable .NET only when not pinned.

## Required layout

```text
implementation/<component>/
  Directory.Build.props
  <Component>.slnx
  src/
    <Component>.<App>/
      <Component>.<App>.csproj
```

## Generated output routing

Add `Directory.Build.props` at the implementation component root before build or restore:

```xml
<Project>
  <PropertyGroup>
    <BaseOutputPath>$(MSBuildThisFileDirectory)bin\$(MSBuildProjectName)\</BaseOutputPath>
    <BaseIntermediateOutputPath>$(MSBuildThisFileDirectory)obj\$(MSBuildProjectName)\</BaseIntermediateOutputPath>
    <MSBuildProjectExtensionsPath>$(BaseIntermediateOutputPath)</MSBuildProjectExtensionsPath>
  </PropertyGroup>
</Project>
```

This keeps generated `bin/` and `obj/` folders at:

- `implementation/<component>/bin/`
- `implementation/<component>/obj/`

Never leave generated `bin/` or `obj/` folders under `implementation/<component>/src/`.

## Workflow

1. Create the implementation component root.
2. Add `Directory.Build.props`.
3. Generate the solution and project under `src/`.
4. Remove template sample code that does not map to approved design contracts.
5. Add only the skeleton allowed by the current implementation gate.
6. Run format/build validation.
7. Verify no generated `bin/` or `obj/` directory exists under `src/`.

## Validation checklist

- `dotnet build` succeeds.
- `dotnet format --verify-no-changes` succeeds when formatting is configured.
- `bin/` and `obj/` exist only at the implementation component root.
- User-specific files such as `*.csproj.user` are not tracked.
- `.gitignore` covers generated outputs and user-specific files.
