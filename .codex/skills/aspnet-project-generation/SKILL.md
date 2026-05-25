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
- Make executable HTTP APIs discoverable in local development without exposing API documentation surfaces in production by default.
- Default executable backend service deployments to Docker/OCI images and Kubernetes local-development manifests.

## Prechecks

1. Confirm the target implementation gate is approved.
2. Confirm the target implementation component root, for example `implementation/<component>/`.
3. Confirm the app model: controller-based Web API, Minimal API, gRPC, worker, or another ASP.NET Core template.
4. Confirm the target framework from repository context; default to the latest stable .NET only when not pinned.
5. For executable HTTP APIs, select an unused stable local development URL and check `implementation/local-development.md` for conflicts.
6. For deployable executable services, confirm the Kubernetes local-development manifest location and image tag convention.

## Required layout

```text
implementation/<component>/
  Directory.Build.props
  <Component>.slnx
  src/
    <Component>.<App>/
      <Component>.<App>.csproj
```

For executable local services, maintain the shared endpoint registry at:

```text
implementation/local-development.md
```

Use `.blueprint/templates/implementation/local-development.template.md` when the registry does not exist yet.

## HTTP API development defaults

For ASP.NET Core HTTP APIs:

- add health checks with `/health`
- expose an OpenAPI document in `Development` only
- expose interactive Swagger UI in `Development` only, referencing the OpenAPI document
- configure the development launch profile to open the Swagger UI when launched interactively
- record local URLs, health endpoints, and API exploration routes in `implementation/local-development.md`
- add a service image `Dockerfile` and Kubernetes `Deployment`/`Service` manifest under `implementation/deploy/k8s/local/`
- start from `.blueprint/templates/implementation/Dockerfile.template`, `.blueprint/templates/implementation/.dockerignore.template`, and `.blueprint/templates/implementation/k8s/local/service.template.yaml` where applicable

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
6. For executable HTTP APIs, add the development API documentation surface and update the local endpoint registry.
7. For deployable executable services, add container image and Kubernetes local-development assets.
8. Run format/build and deployment-manifest validation.
9. Verify no generated `bin/` or `obj/` directory exists under `src/`.

## Validation checklist

- `dotnet build` succeeds.
- `dotnet format --verify-no-changes` succeeds when formatting is configured.
- `bin/` and `obj/` exist only at the implementation component root.
- User-specific files such as `*.csproj.user` are not tracked.
- `.gitignore` covers generated outputs and user-specific files.
- Executable HTTP APIs have Development-only OpenAPI and Swagger UI endpoints plus an entry in `implementation/local-development.md`.
- Deployable executable services have a Docker/OCI image definition and Kubernetes local-development manifest with health probes.
