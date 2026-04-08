# C4 Architecture

This folder contains the canonical architecture description for the project created from this blueprint.

`AGENTS.md` is the authoritative source for operational instructions. This file is a descriptive reference for the C4 folder structure.

## Layout

- `system/` contains the software system view.
- `containers/` contains one folder per container in the system.
- Each container owns its components under `components/`.

## Conventions

- Use Markdown files as the narrative entry point for each level.
- Store one or more PlantUML diagrams beside the related Markdown file.
- Keep components nested under their owning container.
- Keep `system/system.md` as the whole-system narrative entry point.
- Add container folders under `containers/` only when the project architecture defines them.
- Add component folders only under an existing container.

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
