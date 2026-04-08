# Structure

## Repository layout

- `.codex/` contains Codex-specific memory and skills.
- `.design/foundation/` contains stable project guidance.
- `.design/c4/` contains the canonical C4 architecture description.
- `.design/instructions/` contains authoring and implementation guidance by artifact type.
- `.design/specs/` contains per-change requirements, design, tasks, and spec-local diagrams.
- `implementation/` contains real application components created during the implementation phase.
- `tools/` contains repository-local scripts and developer automation.
- `tests/` contains cross-cutting integration and end-to-end validation.

## C4 layout

- Keep one system description under `.design/c4/system/`.
- Keep each container under `.design/c4/containers/<container>/`.
- Keep components as subfolders of their owning container under `.design/c4/containers/<container>/components/<component>/`.
- Allow multiple diagrams for the same system, container, or component when they tell different stories at the same abstraction level.
- Keep one `code.md` per component and one or more code diagrams when useful.

## Diagrams

- Use PlantUML for architecture and design diagrams.
- Keep long-lived C4 diagrams under `.design/c4/`.
- Keep feature-specific diagrams in the relevant spec folder.
