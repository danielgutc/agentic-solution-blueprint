# Project Blueprint

This repository is a reusable blueprint for starting new software projects.

The repository is organized around:

- `design/foundation/` for enduring product, requirements, technical, design, and traceability documents
- `design/c4/` for enduring architecture documentation
- `design/instructions/` for artifact-specific guidance
- `implementation/` for real application components

## Top-level layout

- `.codex/` contains Codex-specific context only.
- `design/` contains the blueprint.
- `implementation/` contains the real application components.
- `tools/` contains repo-local utilities and automation scripts.
- `tests/` contains cross-component integration and end-to-end tests.

## Design layout

```text
design/
  foundation/
    product.md
    requirements.md
    tech.md
    design.md
    traceability-matrix.md
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
            code.md
            code-diagrams/
  instructions/
implementation/
  <component>/
```
