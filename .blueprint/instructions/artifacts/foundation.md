# Foundation Artifacts

## Purpose

Use `design/foundation/` as the durable source of truth for product intent, MVP and prioritization, requirements, technical direction, design, delivery governance, coordination, traceability, and implementation readiness.

## Canonical shapes

Use the corresponding files under `.blueprint/templates/foundation/`.

## Authoring rules

- Product captures actors, problem, outcomes, user journeys, UX hypotheses, design-thinking evidence, goals, non-goals, and assumptions.
- MVP and prioritization owns the production-quality version 1.0 outcome, smallest useful scope, priority model, feedback loop, and sequencing rationale under [MVP quality](../standards/mvp-quality.md). Link requirement targets to stable MVP slice IDs. Keep PoC experiments and pilot evidence distinct from version 1.0 acceptance.
- Requirements use stable IDs: `FR-*`, `NFR-*`, `CON-*`, and `ASM-*`.
- Record each functional and non-functional requirement's acceptance or verification intent, priority, target slice or later horizon, and status in requirements. Define project-specific target values there; do not duplicate those fields in traceability.
- Prefer EARS for functional requirements when it makes behavior clearer.
- Keep functional behavior, quality attributes, mandated constraints, and uncertain assumptions distinct.
- Do not hide architecture choices inside functional requirements or process rules inside non-functional requirements.
- Tech records enduring stack, framework, tooling, testing, documentation, delivery, persistence, and deployment choices with rationale.
- Tech maps each implementation unit to its path, C4 container or non-runtime owner and purpose, toolchain root, commands, and produced artifacts. Record command working directories explicitly.
- Tech records the code-documentation generator and pinned version, configuration path, native source-comment format, capability-fixture scope, known parser limitations, generated-output paths, freshness command, and any evidenced language-specific exception to the Doxygen default.
- Design explains system direction, domain boundaries, decisions, tradeoffs, integrations, data ownership, operations, and open questions.
- Traceability maps each requirement to architecture, implementation scope, and verification evidence without duplicating those artifacts.
- Container- and component-owned technical documents live with their owning C4 scope under `design/c4/containers/`. Foundation retains system-wide product intent, requirements, technical direction, decisions, governance, coordination, traceability, and readiness records; those artifacts link to owned technical detail and record its status or evidence instead of duplicating it.
- Technical detail with shared ownership across containers and no single container owner belongs at an explicit shared/common C4 scope with links from participating containers. Keep a system-wide decision in Foundation only when its primary purpose is the foundation-level decision or governance record, not merely because it mentions several containers.
- Keep task status and approval evidence aligned with the underlying artifacts.
- Follow `../standards/navigation.md` for breadcrumbs, related foundation links, and contents lists. Keep links relative and point only to files that exist.

## Technical direction defaults

- Prefer established, actively maintained libraries and selected framework capabilities over custom plumbing when they satisfy approved constraints.
- Record the platform facilities that shape component design, including dependency injection, validation, configuration, background work, persistence, messaging, observability, and testing.
- Keep physical data-store ownership, schema or namespace ownership, migration ownership, and access enforcement explicit.
- Treat deployment technology as a project decision. The blueprint does not mandate Kubernetes, a cloud, or a CI provider.
- Apply `../standards/implementation-layout.md` when recording implementation units and repository command scopes.

## Quality checks

- Decisions are placed at the correct abstraction.
- IDs are stable and unique.
- Requirements are verifiable.
- Constraints are actionable.
- Important choices include rationale and revisit triggers.
- Open questions have owners or are explicitly accepted.
