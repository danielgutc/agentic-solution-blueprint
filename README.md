# Project Blueprint

This repository is a reusable, heavyweight blueprint for software projects that need explicit product discovery, requirements, architecture, delivery, implementation, and verification governance.

## Start here

- [Blueprint configuration](./.blueprint/blueprint.toml)
- [Instruction index](./.blueprint/instructions/README.md)
- [Task and handoff dashboard](./design/foundation/task.md)
- [Product](./design/foundation/product.md)
- [MVP and prioritization](./design/foundation/mvp.md)
- [Requirements](./design/foundation/requirements.md)
- [Technical direction](./design/foundation/tech.md)
- [Design](./design/foundation/design.md)
- [Delivery governance](./design/foundation/delivery.md)
- [Implementation readiness](./design/foundation/implementation-readiness.md)
- [Traceability matrix](./design/foundation/traceability-matrix.md)
- [C4 system](./design/c4/system/system.md)
- [C4 container landscape](./design/c4/containers/system-containers.md)

## Repository model

- `.agents/skills/` contains project-specific skills only. Reusable roles and skills come from the user-level engineering toolkit.
- `.blueprint/` contains lifecycle policy, modular instructions, and canonical templates.
- `.codex/` contains short-lived Codex working context only.
- `design/foundation/` contains enduring project decisions, coordination state, traceability, and gate evidence.
- `design/c4/` contains enduring system, container, and component architecture.
- `implementation/` contains real application components.
- `tools/` contains repo-local utilities and automation scripts.
- `tests/` contains cross-component integration and end-to-end tests.

The reusable template leaves `selected_workflow` unset. Each consuming project must choose `requirements-first` or `design-first` before advancing its enduring project artifacts.

## Recommended reading order

1. [Product](./design/foundation/product.md) and [MVP and prioritization](./design/foundation/mvp.md)
2. [Task tracker](./design/foundation/task.md) and [lifecycle](./.blueprint/instructions/process/lifecycle.md) to see the selected workflow and current gate
3. [Requirements](./design/foundation/requirements.md), [Tech](./design/foundation/tech.md), and [Design](./design/foundation/design.md) in the selected workflow sequence
4. [C4 system](./design/c4/system/system.md) and [C4 container landscape](./design/c4/containers/system-containers.md), after design approval
5. [Traceability matrix](./design/foundation/traceability-matrix.md), [Delivery governance](./design/foundation/delivery.md), and [Implementation readiness](./design/foundation/implementation-readiness.md)

## Design layout

```text
design/
  foundation/
    product.md
    mvp.md
    requirements.md
    tech.md
    design.md
    delivery.md
    task.md
    traceability-matrix.md
    implementation-readiness.md
    _diagrams/               # optional foundation diagram sources and exports
  c4/
    README.md
    system/
      system.md
      diagrams/
    containers/
      system-containers.md
      <container>/
        container.md
        diagrams/
        components/
          <component>/
            component.md
            diagrams/
            code.md              # generated from source and tests
            code-diagrams/       # generated diagram sources
implementation/
  <component>/
```

## Delivery model

The blueprint separates architecture, a walking skeleton, and full development:

```text
approved design
  -> C4 system and containers
  -> component technical design and walking skeleton
  -> minimum viable CI/CD pipeline
  -> implementation-readiness approval
  -> full development
  -> integrated verification
```

Before full development, CI must build, test, analyze, document, package, and exercise a non-production delivery path from a clean checkout.

See the [lifecycle instructions](./.blueprint/instructions/process/lifecycle.md) for the requirements-first and design-first ordering models.

## Documentation model

- Keep system, container, and component intent human-authored.
- Treat source interfaces, API comments, and executable tests as the code-contract source.
- Generate compact `code.md` files and code-diagram sources and commit them when deterministic.
- Publish full Javadoc, DocFX, TypeDoc, or equivalent output as a CI artifact rather than committing it by default.

## Top-level layout

```text
.agents/
.blueprint/
.codex/
design/
implementation/
tests/
tools/
```
