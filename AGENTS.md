# Agent Instructions

## Use project context

- Use `.design/foundation/product.md` for product direction.
- Use `.design/foundation/tech.md` for technology choices and constraints.
- Use `.design/foundation/structure.md` for repository layout and C4 structure rules.
- Use `.design/c4/` as the canonical architecture area.
- Keep C4 components nested under their owning container.
- Treat `.design/c4/containers/` as a template area until a real project defines its containers.
- Do not create concrete container or component folders preemptively in the blueprint.
- Treat feature specs as change units, not as services or components.

## Follow file-type instructions

- Follow `.design/instructions/csharp.md` when creating or modifying C# code.
- Follow `.design/instructions/docker.md` when creating or modifying Docker files.
- Follow `.design/instructions/plantuml.md` when creating or modifying PlantUML files.
- Follow `.design/instructions/markdown.md` when creating or modifying Markdown files.

## Use specs appropriately

- For non-trivial changes, use `.design/specs/<feature>/requirements.md`, `design.md`, and `tasks.md`.
- Before creating a new feature spec, decide which workflow applies: Requirements-first or Design-first.
- If the correct workflow is not explicit, ask the user which one to use and give a short recommendation.
- Recommend Requirements-first when desired behavior is clearer than the implementation approach.
- Recommend Design-first when technical constraints, architecture, feasibility, or existing design direction lead the work.
- Once the workflow is chosen, guide the conversation in that order and do not jump ahead to later spec phases prematurely.
- Do not create concrete containers or components until the chosen spec workflow reaches the phase that justifies them.
- For Requirements-first, follow: `requirements -> design -> tasks -> implementation`.
- For Design-first, follow: `design -> requirements -> tasks -> implementation`.
- Use C4 as the architecture format inside the design phase when architectural views are needed.
- When you write `requirements.md`, prefer structured, testable requirements and use EARS where practical.
- For trivial fixes or very small changes, skip feature spec creation unless structured planning is clearly useful.
- Keep feature specs under `.design/specs/<feature>/`.

## Maintain the workspace

- Keep project design artifacts in `.design/`.
- Keep real runtime components under `implementation/` once implementation starts.
- Keep Codex-specific memory and skills in `.codex/`.
- Update relevant foundation, architecture, spec, or instruction files when structural conventions change.
