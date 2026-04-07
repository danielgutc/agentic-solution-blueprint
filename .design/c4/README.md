# C4 Architecture

This folder contains the canonical architecture description for the project created from this blueprint.

## Layout

- `system/` contains the software system view.
- `containers/` contains one folder per container in the system.
- Each container owns its components under `components/`.
- `dynamic/` and `deployment/` can be added when those views add value.

## Conventions

- Use Markdown files as the narrative entry point for each level.
- Store one or more PlantUML diagrams beside the related Markdown file.
- Keep components nested under their owning container.

## Example structure

- `client/` and `server/` are example containers only.
- Replace them, rename them, or add more containers to fit the real project.
- Use the sample component folders as formatting examples for future components.
