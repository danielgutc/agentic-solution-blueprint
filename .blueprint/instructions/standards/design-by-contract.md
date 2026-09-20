# Design by Contract

Use Design by Contract for service, component, persistence, and agent handoff boundaries.

## Contract definition

- Signature: operation, request, response, and direction.
- Preconditions: input obligations, identity or context, idempotency, and caller responsibilities.
- Postconditions: outcome guarantees, state changes, emitted events, and returned projections.
- Invariants: lifecycle, ownership, authorization, consistency, and persistence rules.
- Failure semantics: validation, absence, conflicts, retryability, timeout, fallback, and cancellation behavior.
- Evolution: compatibility, versioning, deprecation, and migration expectations.

## Rules

- Define contracts before internal implementation details.
- Keep provider and consumer obligations visible in the same artifact or linked siblings.
- Prefer typed domain-oriented operations over stringly typed envelopes.
- Use generic envelopes only with a closed operation registry and schemas.
- Verify contract obligations through executable tests rather than private implementation assertions.
- Treat changed obligations as architecture changes and revisit the nearest affected gate.

A consumer should be able to call or implement the boundary without hidden knowledge.
