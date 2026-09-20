# Containers

This folder contains the container-level subtree of the C4 architecture.

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
