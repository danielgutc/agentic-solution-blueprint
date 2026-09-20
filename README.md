# Project Blueprint

This repository is a reusable blueprint for starting new software projects.

The repository is organized around:

- `.blueprint/blueprint.toml` for blueprint activation, paths, documentation policy, and lifecycle gates
- `design/foundation/` for enduring product, requirements, technical, design, and traceability documents
- `design/c4/` for enduring architecture documentation
- `design/instructions/` for artifact-specific guidance
- `implementation/` for real application components

## Top-level layout

- `.agents/skills/` contains project-specific skills only; reusable skills come from the user-level engineering toolkit.
- `.blueprint/` marks projects that use the heavyweight blueprint workflow.
- `.codex/` contains Codex-specific working context only.
- `design/` contains the blueprint.
- `implementation/` contains the real application components.
- `tools/` contains repo-local utilities and automation scripts.
- `tests/` contains cross-component integration and end-to-end tests.

The reusable template leaves `selected_workflow` unset. Each consuming project must choose `requirements-first` or `design-first` before advancing its enduring project artifacts.

## Design layout

```text
design/
  foundation/
    product.md
    requirements.md
    tech.md
    design.md
    traceability-matrix.md
    implementation-readiness.md
  c4/
    README.md
    system/
      system.md
      diagrams/
    containers/
      <container>/
        container.md
        diagrams/
        components/
          <component>/
            component.md
            diagrams/
            code.md              # generated from source and tests
            code-diagrams/       # generated diagram sources
  instructions/
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

## Documentation model

- Keep system, container, and component intent human-authored.
- Treat source interfaces, API comments, and executable tests as the code-contract source.
- Generate compact `code.md` files and code-diagram sources and commit them when deterministic.
- Publish full Javadoc, DocFX, TypeDoc, or equivalent output as a CI artifact rather than committing it by default.
