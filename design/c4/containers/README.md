# Containers

This folder contains the container-level subtree of the C4 architecture.

Use `system-containers.md` and `_diagrams/` for the authoritative system-wide container view. Add one folder per approved container only after that landscape is reviewed.

## Container subtree

- `container.md`
- `_diagrams/`
- `components/`

## Component subtree

- `component.md`: human-authored component responsibilities, boundaries, and design intent
- `_diagrams/`: human-authored Draw.io sources and sibling SVG exports
- `code.md`: generated compact projection of source interfaces and important types
- `_code-diagrams/`: generated code-structure diagram sources

## Folder shape

```text
containers/
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
