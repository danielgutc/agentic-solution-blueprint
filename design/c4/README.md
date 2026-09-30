# C4 Architecture

This folder contains the canonical architecture description for the project created from this blueprint.

## Layout

- `system/` contains the software system view.
- `containers/system-containers.md` contains the authoritative container landscape.
- `containers/` contains one folder per approved container in the system.
- Each container owns its components under `components/`.

## Documentation model

- Human-authored Markdown and Draw.io diagrams with sibling SVG exports describe system, container, and component intent.
- Source interfaces, API comments, and executable tests define code contracts.
- The documentation toolchain generates compact code-level Markdown and code-diagram sources.
- Full API references are CI artifacts by default; navigable human-authored SVG diagrams are committed beside their Draw.io sources.

## Folder shape

```text
c4/
  README.md
  system/
    system.md
    _diagrams/
  containers/
    README.md
    system-containers.md
    _diagrams/
    <container>/
      container.md
      _diagrams/
      components/
        <component>/
          component.md
          _diagrams/
          code.md          # generated
          _code-diagrams/  # generated sources
```
