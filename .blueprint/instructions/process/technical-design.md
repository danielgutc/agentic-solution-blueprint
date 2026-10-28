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
- Select and configure the code-documentation pipeline under `../file-types/api-documentation.md`. Use Doxygen by default after the selected version and language constructs pass capability fixtures; record an evidenced, scoped alternative in `design/foundation/tech.md` when Doxygen cannot represent the implementation safely.
- Author rich ecosystem-native API comments as part of the source contract. Define coherent documentation profiles that may span several projects when language, target/runtime, compile symbols, native documentation evidence, and parser configuration are compatible.
- Generate one canonical committed page per stable symbol identity within an implementation-unit/documentation-profile context. Generate container entry views, architectural-interface views, optional filtered component guides, and code-diagram sources as link projections; never author those projections manually.
- Bind generated views only to stable IDs from approved C4 artifacts. Separate one explicit owner (component or shared container/unit) from zero or more consumer roles; do not invent a component for shared code or infer architecture visibility from language visibility.
- Add architecture-to-code links only after the generated view exists. Keep every canonical page linked to its source declaration and every relevant configured architecture view.
- Record the resulting implementation-unit path and evidence in `design/foundation/traceability-matrix.md` and `design/foundation/task.md` for the scoped readiness review.
- Return changes to system, domain, or container boundaries to the solutions architect and the affected approval gate.

Use the toolkit's `technical-design` skill when available for the general component-design method. The obligations above apply even when that skill is not installed.

## MVP architecture baseline

For MVP work, apply [MVP version 1.0 quality](../standards/mvp-quality.md). The technical design and walking skeleton use the intended production architecture for their scope. Identify PoC-only mechanisms and required qualification or replacement before release; do not schedule a mandatory structural rewrite merely to add the known approved roadmap. Shared solutions or binaries require justified dependency and runtime boundaries, not a blanket MVP exception.
