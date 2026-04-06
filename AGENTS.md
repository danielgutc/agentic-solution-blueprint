# Agent Instructions

## Use project context

- Use `.design/steering/product.md` for product direction.
- Use `.design/steering/tech.md` for technology choices and constraints.
- Use `.design/steering/structure.md` for repository layout and workflow rules.
- Treat feature specs as change units, not as services or components.

## Follow file-type instructions

- Follow `.design/instructions/csharp.md` when creating or modifying C# code.
- Follow `.design/instructions/docker.md` when creating or modifying Docker files.
- Follow `.design/instructions/plantuml.md` when creating or modifying PlantUML files.
- Follow `.design/instructions/markdown.md` when creating or modifying Markdown files.

## Use specs appropriately

- For non-trivial changes, use `.design/specs/<feature>/requirements.md`, `design.md`, and `tasks.md`.
- Support both feature-spec workflows:
  - Requirements-first: `requirements -> design -> tasks -> implementation`
  - Design-first: `design -> requirements -> tasks -> implementation`
- Use requirements-first when behavior is known and the design can adapt.
- Use design-first when technical constraints, architecture, or feasibility drive the work.
- When you write `requirements.md`, prefer structured, testable requirements and use EARS where practical.
- For trivial fixes or very small changes, skip feature spec creation unless structured planning is clearly useful.

## Maintain the workspace

- Keep project design artifacts in `.design/`.
- Keep Codex-specific memory and skills in `.codex/`.
- Update relevant steering, spec, or instruction files when structural conventions change.
