# Containers

`AGENTS.md` is the authoritative source for operational instructions. This file is a descriptive reference for the container subtree.

Create one folder per real container when the project architecture defines it.

Each container folder should contain:

- `container.md`
- `diagrams/`
- `components/`

Each component folder should contain:

- `component.md`
- `diagrams/`
- `code.md`
- `code-diagrams/`

Use:

- `container.md` for container purpose, responsibilities, interfaces, dependencies, and contained components
- `component.md` for component purpose, responsibilities, interfaces, dependencies, and constraints
- `code.md` for the internal code structure of the component

Example shape:

```text
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
```
