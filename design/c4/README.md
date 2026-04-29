# C4 Architecture

This folder contains the canonical architecture description for the project created from this blueprint.

## Layout

- `system/` contains the software system view.
- `containers/` contains one folder per container in the system.
- Each container owns its components under `components/`.

## Documentation model

- Markdown files provide the narrative description for each C4 level.
- Draw.io source diagrams (`.drawio`) provide the editable diagrammatic views.
- Rendered `.svg` files provide embeddable views for Markdown pages.

## Folder shape

```text
c4/
  README.md
  system/
    system.md
    _diagrams/
  containers/
    system-containers.md
    _diagrams/
    README.md
    <container>/
      container.md
      _diagrams/
      components/
        <component>/
          component.md
          _diagrams/
          _code-diagrams/
```
