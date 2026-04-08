# C4 Architecture

This folder contains the canonical architecture description for the project created from this blueprint.

## Layout

- `system/` contains the software system view.
- `containers/` contains one folder per container in the system.
- Each container owns its components under `components/`.

## Documentation model

- Markdown files provide the narrative description for each C4 level.
- PlantUML diagrams provide the diagrammatic views that support those narratives.

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
          code.md
          code-diagrams/
```
