# Technical Design

## Purpose

Refine approved containers into implementation-ready components and prove architecture-significant assumptions without beginning broad feature development.

## Blueprint obligations

- Confirm the owning container and design approval before adding component artifacts under `design/c4/containers/`.
- Keep `component.md` and component architecture diagrams human-authored; use them for intent, boundaries, and test seams rather than a manual API inventory.
- Create only the source interfaces, walking skeleton, and representative tests needed to prove architecture-significant decisions before the readiness gate.
- Select and configure the documentation generator. Generate `code.md` and code-diagram sources from source, API comments, and tests; never author those projections manually.
- Record the resulting evidence in `design/foundation/traceability-matrix.md` and `design/foundation/task.md` for the scoped readiness review.
- Return changes to system, domain, or container boundaries to the solutions architect and the affected approval gate.

Use the toolkit's `technical-design` skill when available for the general component-design method. The obligations above apply even when that skill is not installed.
