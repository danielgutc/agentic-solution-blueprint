# Structure

## Repository Layout

- `.codex/` contains Codex-specific memory and skills.
- `.design/foundation/` contains stable project guidance.
- `.design/c4/` contains the canonical C4 architecture description.
- `.design/instructions/` contains authoring and implementation guidance by artifact type.
- `.design/specs/` contains per-change requirements, design, tasks, and spec-local diagrams.
- `tools/` contains repository-local scripts and developer automation.
- `tests/` contains cross-cutting integration and end-to-end validation.

## Blueprint intent

- Keep this repository business-agnostic so it can seed different kinds of projects.
- Treat the current C4 files as examples of the structure, not as constraints on the final system.
- Add, rename, or remove containers and components as the actual project architecture becomes clear.

## C4 Layout

- Keep one system description under `.design/c4/system/`.
- Keep each container under `.design/c4/containers/<container>/`.
- Keep components as subfolders of their owning container under `.design/c4/containers/<container>/components/<component>/`.
- Allow multiple diagrams for the same system, container, or component when they tell different stories at the same abstraction level.
- Keep one `code.md` per component and one or more code diagrams when useful.

## Workflow

Feature specs support two valid flows:

1. Requirements-first: define requirements, create the design, break work into tasks, then implement.
2. Design-first: define the design first, derive requirements from it, break work into tasks, then implement.

Use requirements-first for product-driven work with flexible implementation.
Use design-first when technical constraints or architectural feasibility lead the change.

## Diagrams

- Use PlantUML for architecture and design diagrams.
- Keep long-lived C4 diagrams under `.design/c4/`.
- Keep feature-specific diagrams in the relevant spec folder.
