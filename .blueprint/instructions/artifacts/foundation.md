# Foundation Artifacts

## Purpose

Use `design/foundation/` as the durable source of truth for product intent, MVP and prioritization, requirements, technical direction, design, delivery governance, coordination, traceability, and implementation readiness.

## Canonical shapes

Use the corresponding files under `.blueprint/templates/foundation/`.

## Authoring rules

- Product captures actors, problem, outcomes, user journeys, UX hypotheses, design-thinking evidence, goals, non-goals, and assumptions.
- MVP and prioritization owns the first feedbackable slice, priority model, scope, feedback loop, and sequencing rationale. Link requirement targets to stable MVP slice IDs.
- Requirements use stable IDs: `FR-*`, `NFR-*`, `CON-*`, and `ASM-*`.
- Record each functional and non-functional requirement's acceptance or verification intent, priority, target slice or later horizon, and status in requirements. Define project-specific target values there; do not duplicate those fields in traceability.
- Prefer EARS for functional requirements when it makes behavior clearer.
- Keep functional behavior, quality attributes, mandated constraints, and uncertain assumptions distinct.
- Do not hide architecture choices inside functional requirements or process rules inside non-functional requirements.
- Tech records enduring stack, framework, tooling, testing, documentation, delivery, persistence, and deployment choices with rationale.
- Design explains system direction, domain boundaries, decisions, tradeoffs, integrations, data ownership, operations, and open questions.
- Traceability maps each requirement to architecture, implementation scope, and verification evidence without duplicating those artifacts.
- Keep task status and approval evidence aligned with the underlying artifacts.
- Use a README breadcrumb, related foundation links, and a section table of contents in each foundation artifact. Keep links relative and point only to files that exist.

## Technical direction defaults

- Prefer established, actively maintained libraries and selected framework capabilities over custom plumbing when they satisfy approved constraints.
- Record the platform facilities that shape component design, including dependency injection, validation, configuration, background work, persistence, messaging, observability, and testing.
- Keep physical data-store ownership, schema or namespace ownership, migration ownership, and access enforcement explicit.
- Treat deployment technology as a project decision. The blueprint does not mandate Kubernetes, a cloud, or a CI provider.

## Quality checks

- Decisions are placed at the correct abstraction.
- IDs are stable and unique.
- Requirements are verifiable.
- Constraints are actionable.
- Important choices include rationale and revisit triggers.
- Open questions have owners or are explicitly accepted.
