# C4 Artifact: containers/<container>/components/<component>/component.md

## Purpose

Describe component-level decomposition and contracts inside one container.

## Canonical structure

- Use `design/templates/c4/component.template.md`.

## Authoring rules

- Keep one externally consumed facade boundary per microservice by default.
- Model internal collaboration through explicit component APIs.
- Apply `design/instructions/standards/design-by-contract.md` to component APIs and handoffs.
- For service contracts, use provider/consumer interface directionality.
- For storage, draw direct component-to-data-store relations; do not model schema/file access as interfaces.
- Mark component ownership (`project-built` vs selected third-party stack).
- Keep component names, technology line, and short responsibility summary readable in diagrams.

## Quality checklist

- Facade boundary is explicit.
- `requires` dependencies originate from consumers.
- Component API obligations are explicit enough to test.
- Storage notation is consistent across sibling component diagrams.
