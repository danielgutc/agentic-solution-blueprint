# C4 Architecture

This folder contains the canonical architecture description for the project created from this blueprint.

## Layout

- `system/` contains the software system view.
- `containers/` contains one folder per container in the system.
- Each container owns its components under `components/`.

## Documentation model

- Human-authored Markdown and PlantUML describe system, container, and component intent.
- Source interfaces, API comments, and executable tests define code contracts.
- The documentation toolchain generates compact code-level Markdown and code-diagram sources.
- Full API reference and rendered diagrams are CI artifacts by default.

## Folder shape

```text
c4/
  README.md
  system/
    system.md
    diagrams/
  containers/
    README.md
    <container>/
      container.md
      diagrams/
      components/
        <component>/
          component.md
          diagrams/
          code.md          # generated
          code-diagrams/   # generated sources
```
