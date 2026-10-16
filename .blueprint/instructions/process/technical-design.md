# Technical Design

## Purpose

Refine approved containers into implementation-ready components and prove architecture-significant assumptions without beginning broad feature development.

## Blueprint obligations

- Confirm the owning container and design approval before adding component artifacts under `design/c4/containers/`.
- Select or create the owning implementation unit according to `../standards/implementation-layout.md`, then record its mapping to the approved container in `design/foundation/tech.md`. This mapping does not create or alter a C4 boundary.
- Keep `component.md` and component architecture diagrams human-authored; use them for intent, boundaries, and test seams rather than a manual API inventory.
- Place each enduring human-authored technical document with its primary architectural owner: container-owned material at `design/c4/containers/<container>/<document>.md` and component-owned material at `design/c4/containers/<container>/components/<component>/<document>.md`. Examples include walking skeletons, focused assessments, recovery notes, contract designs, and test designs. A document spanning components within one container stays at that container's level.
- For a technical document with shared ownership across containers and no single container owner, select the explicit shared scope at their common C4 level and link it from each participating container; do not duplicate it under one component or use `design/foundation/` as a general technical-document folder. Foundation task, traceability, and implementation-readiness artifacts link the owned detail and record status or evidence.
- Determine ownership from the document's primary decision scope, not its filename or incidental mentions. Keep implementation-local documentation with its implementation unit and keep source interfaces, API comments, executable tests, generated projections, and full API reports in their registered source/output locations.
- Create only the source interfaces, walking skeleton, and representative tests needed to prove architecture-significant decisions before the readiness gate.
- Select and configure the documentation generator. Generate `code.md` and code-diagram sources from source, API comments, and tests; never author those projections manually.
- Record the resulting implementation-unit path and evidence in `design/foundation/traceability-matrix.md` and `design/foundation/task.md` for the scoped readiness review.
- Return changes to system, domain, or container boundaries to the solutions architect and the affected approval gate.

Use the toolkit's `technical-design` skill when available for the general component-design method. The obligations above apply even when that skill is not installed.
