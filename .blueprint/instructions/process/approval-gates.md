# Approval Gates

## Design approval

Design approval is required before enduring C4 system or container artifacts are created or changed for the scope.

Evidence must show:

- product and selected workflow are explicit
- relevant requirements or technical constraints are understood
- domain and system boundaries are explained
- important tradeoffs, integrations, data ownership, and operational risks are recorded
- unresolved questions are either closed or accepted with an owner

Record the decision in `design/foundation/design.md` and the lifecycle dashboard.

## Implementation readiness

Implementation readiness is required before full feature development for the scoped containers, components, or slice.

The gate must prove every applicable capability listed in `.blueprint/blueprint.toml` and use `design/foundation/implementation-readiness.md` as evidence. A criterion may be excluded only with an explicit owner, rationale, expiry or trigger, and compensating evidence.

## Consistency rules

- A downstream phase cannot be `Approved`, `Implemented`, or `Verified` when a prerequisite is weaker for the same scope.
- Conversation approval is not durable until the relevant artifact and task dashboard record it.
- When an approved upstream artifact changes, mark affected downstream approvals for re-review.
- Scope gates narrowly enough that one approval does not silently cover future components or capabilities.
- Do not use a passing pipeline to substitute for an architecture decision, or a reviewed document to substitute for executable evidence.
