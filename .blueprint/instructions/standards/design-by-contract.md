# Design By Contract Standard

Use Design by Contract as the default way to define service, component, persistence, and agent handoff boundaries.

## Contract definition

A contract is more than a name or transport shape. It must make the boundary consumable without hidden knowledge.

- Signature: operation name, request type, response type, and direction.
- Preconditions: input obligations, required identity/context, idempotency expectations, and caller responsibilities.
- Postconditions: successful outcome guarantees, state changes, emitted events, and returned projections.
- Invariants: lifecycle, ownership, authorization, consistency, and persistence rules that must always hold.
- Failure semantics: validation errors, not-found cases, conflict handling, retryability, and fallback behavior.

## Authoring rules

- Define contracts before internal implementation details.
- Keep contracts explicit, typed, and consumer-readable.
- Prefer named command/query methods and typed request/response objects over stringly typed operation names or untyped payload envelopes.
- Use generic envelopes only when the artifact defines a closed operation registry and schema for each operation.
- Keep provider and consumer obligations visible in the same artifact or linked sibling artifacts.
- Treat changed contract obligations as architecture changes that require the nearest approval gate to be revisited.

## Quality checklist

- A consumer can call or implement the contract from the artifact alone.
- Preconditions, postconditions, invariants, and failure semantics are explicit enough to test.
- Runtime tests verify the contract obligations, not private implementation details.
- Contract names reflect domain intent instead of transport mechanics.
