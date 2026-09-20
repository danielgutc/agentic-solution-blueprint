# Containers

This folder contains the container-level subtree of the C4 architecture.

Use `system-containers.md` and `diagrams/` for the authoritative system-wide container view. Add one folder per approved container only after that landscape is reviewed.

## Container subtree

- `container.md`
- `diagrams/`
- `components/`

## Component subtree

- `component.md`: human-authored component responsibilities, boundaries, and design intent
- `diagrams/`: human-authored architecture diagram sources
- `code.md`: generated compact projection of source interfaces and important types
- `code-diagrams/`: generated code-structure diagram sources

## Folder shape

```text
containers/
  system-containers.md
  diagrams/
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
