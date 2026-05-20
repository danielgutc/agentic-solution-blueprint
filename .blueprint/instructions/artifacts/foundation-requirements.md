# Foundation Artifact: requirements.md

## Purpose

Capture enduring functional and non-functional requirements, constraints, and assumptions.

## Canonical structure

- Use `.blueprint/templates/foundation/requirements.template.md`.

## Authoring rules

- Prefer structured, testable statements.
- Use stable IDs (`FR-*`, `NFR-*`, `CON-*`, `ASM-*`).
- Use EARS where practical for functional requirements.
- Classify requirements by intent:
  - functional requirements (`FR-*`) describe observable system behavior, capabilities, operations, or interactions.
  - non-functional requirements (`NFR-*`) describe quality attributes such as performance, reliability, usability, scalability, security, maintainability, observability, portability, or testability.
  - constraints (`CON-*`) describe mandated technology, architecture, authority, integration, persistence, process, regulatory, or scope decisions that limit the solution space.
  - assumptions (`ASM-*`) describe conditions believed true but not guaranteed by the system.
- Keep functional and non-functional requirements implementation-agnostic unless the technology choice is part of the externally required behavior.
- Do not hide architecture decisions inside functional requirements. Move design-shaping rules such as runtime authority, storage ownership, cross-service integration style, deployment topology, or framework choices to constraints or to the design/tech/C4 artifacts.
- Do not hide process standards inside non-functional requirements. Move workflow rules such as Design by Contract gates, approval gates, or test-first implementation process to the relevant process or standard instruction unless the product itself must expose measurable behavior.
- When a statement mixes behavior and design, split it into a functional requirement plus a constraint or design decision.

## Quality checklist

- Every requirement is unambiguous and verifiable.
- IDs are unique and stable.
- Constraints and assumptions are separated from requirements.
- Functional requirements can be validated through externally observable behavior or system outputs.
- Non-functional requirements have a measurable or reviewable quality criterion.
- Architecture and process constraints are explicit and not disguised as product behavior.
