# Project Blueprint

This repository is a reusable blueprint for software projects that need explicit product, requirements, architecture, delivery, implementation, and verification governance. It provides the same path from foundation documents to C4 architecture as a consuming project, while leaving project-specific decisions to that project.

## Start here

- [Task tracker](./design/foundation/task.md)
- [Foundation overview](./design/foundation/product.md)
- [MVP and prioritization](./design/foundation/mvp.md)
- [MVP version 1.0 quality rules](./.blueprint/instructions/standards/mvp-quality.md)
- [Technical direction](./design/foundation/tech.md)
- [Design decisions](./design/foundation/design.md)
- [Delivery governance](./design/foundation/delivery.md)
- [System](./design/c4/system/system.md)
- [System containers](./design/c4/containers/system-containers.md)

## Recommended reading order

1. [Product](./design/foundation/product.md)
2. [MVP and prioritization](./design/foundation/mvp.md)
3. [Task tracker](./design/foundation/task.md)
4. Follow the selected workflow: [Requirements](./design/foundation/requirements.md), [Tech](./design/foundation/tech.md), then [Design](./design/foundation/design.md) for requirements-first; Tech, Design, then Requirements for design-first.
5. [System](./design/c4/system/system.md) and [System containers](./design/c4/containers/system-containers.md), after design approval
6. [Traceability matrix](./design/foundation/traceability-matrix.md)
7. [Delivery governance](./design/foundation/delivery.md)
8. [Implementation readiness](./design/foundation/implementation-readiness.md)

The [lifecycle](./.blueprint/instructions/process/lifecycle.md) defines phase order and approval gates for each workflow.

## Repository structure

- `.blueprint/` contains lifecycle instructions, configuration, and reusable templates.
- `.agents/skills/` contains project-specific skills; reusable roles and skills come from the user-level engineering toolkit.
- `.codex/` contains Codex working context.
- `design/` contains enduring product, technical, design, and architecture documentation.
- `design/code/` contains canonical generated API pages grouped by implementation unit and documentation profile; generated C4 code views link to these pages.
- `implementation/` contains repository-owned implementation units once implementation is approved.
- `deployment/` contains repository-owned deployment topology, environment composition, and infrastructure assets.
- `tools/` contains repository utilities and developer automation.
- `tests/` contains assembled cross-unit integration and end-to-end checks.
- `artifacts/` is the ignored aggregate output location for packages, reports, and generated API documentation.

An implementation unit is a build, test, or packaging workspace. It is related to, but does not mechanically mirror, the C4 container model: a managed service might need no repository implementation, while an application and its embedded store can share one unit. Follow the [implementation workspace standard](./.blueprint/instructions/standards/implementation-layout.md) and record the project-specific mapping in [Tech](./design/foundation/tech.md).

## Documentation structure

### Foundation

Use [design/foundation/](./design/foundation/) for the enduring project definition:

- [Product](./design/foundation/product.md)
- [MVP and prioritization](./design/foundation/mvp.md)
- [Task tracker](./design/foundation/task.md)
- [Requirements](./design/foundation/requirements.md)
- [Tech](./design/foundation/tech.md)
- [Design](./design/foundation/design.md)
- [Delivery governance](./design/foundation/delivery.md)
- [Traceability matrix](./design/foundation/traceability-matrix.md)
- [Implementation readiness](./design/foundation/implementation-readiness.md)
- [API documentation model review](./design/foundation/api-documentation-model-review.md)

### C4 architecture

Use [design/c4/](./design/c4/) for the enduring architecture:

- [System](./design/c4/system/system.md)
- [System containers](./design/c4/containers/system-containers.md)

Add links to container and component pages as approved architecture creates them. The [C4 index](./design/c4/README.md) provides the next navigation level.

## Blueprint use

- Set `selected_workflow` in the [blueprint configuration](./.blueprint/blueprint.toml) to `requirements-first` or `design-first` when starting a consuming project. It remains `unset` in this reusable template.
- Use the [instruction index](./.blueprint/instructions/README.md) and [canonical templates](./.blueprint/templates/README.md) when creating project artifacts.
- Record phase status and approvals in the [task tracker](./design/foundation/task.md). Design approval precedes enduring C4 work; implementation readiness approval precedes full feature development.
- Keep human-authored diagrams in Draw.io with sibling SVG exports. Generate canonical API references and C4 code views from source, tests, and approved architecture bindings according to the [documentation rules](./.blueprint/instructions/file-types/api-documentation.md).

## Top-level layout

```text
.agents/
.blueprint/
.codex/
design/
  code/                   # generated unit/profile API reference when implementation exists
implementation/
deployment/
tools/
tests/
artifacts/                 # generated and ignored
```

Multiple independently owned workspaces normally live at `implementation/<unit>/`. A documented single-unit project can place its workspace directly in `implementation/`. Unit-local `src/`, `tests/`, `docs/`, and `artifacts/` directories are optional; use the structure native to the selected ecosystem and create directories only when they contain owned files.
