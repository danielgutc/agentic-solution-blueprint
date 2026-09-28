# Lifecycle

## Workflow selection

Set `selected_workflow` in `.blueprint/blueprint.toml` before advancing a consuming project.

Use requirements-first when desired behavior and user outcomes are clearer than the implementation approach:

```text
product -> MVP and prioritization -> requirements -> tech -> design -> design approval
-> C4 solution -> traceability -> technical design -> delivery foundation
-> implementation readiness approval -> full development -> integrated verification
```

Use design-first when constraints, integrations, feasibility, or architecture risk lead:

```text
product -> MVP and prioritization -> tech -> design -> design approval -> requirements
-> C4 solution -> traceability -> technical design -> delivery foundation
-> implementation readiness approval -> full development -> integrated verification
```

## Phase outcomes

- Product: problem, actors, outcomes, non-goals, and assumptions are explicit.
- MVP and prioritization: the first feedbackable slice, priority model, scope, learning loop, and later candidates are explicit.
- Requirements: stable IDs express verifiable functional behavior, quality attributes, constraints, and assumptions; priority and target connect requirements to MVP slices.
- Tech: enduring stack, platform, tooling, documentation, test, delivery, and deployment choices are recorded.
- Design: system direction, domain boundaries, tradeoffs, integrations, and operational decisions are reviewable.
- C4 solution: system context and authoritative container boundaries reflect the approved design.
- Traceability: requirements map to architecture, implementation scope, and verification evidence.
- Technical design: approved containers are refined into components, contracts, test seams, and a minimal walking skeleton.
- Delivery foundation: repository commands and CI prove clean build, tests, analysis, documentation, packaging, and non-production delivery.
- Full development: approved slices are implemented through TDD without crossing architecture boundaries silently.
- Integrated verification: assembled behavior is proven through real boundaries and user-observable workflows.

## Pyramidal decomposition

- Complete the highest relevant abstraction before drilling down.
- Keep decisions in the artifact matching their abstraction level.
- Use domain-driven boundaries when decomposing the system.
- Use Design by Contract for boundaries and TDD to prove contracts.
- Re-enter the nearest affected phase and approval gate when implementation evidence changes an enduring decision.

## Approval behavior

- Seek explicit approval before moving to the next phase.
- Record phase status, evidence, and the next owner in `design/foundation/task.md`.
- Follow `approval-gates.md` for durable gate evidence and re-review rules.
