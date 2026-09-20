# Full Development

## Prerequisite

The relevant scope in `design/foundation/implementation-readiness.md` must be explicitly approved.

## TDD slice

1. Select one traced requirement or behavior slice and its approved component contract.
2. Add or refine the smallest failing test that expresses observable behavior or a contract obligation.
3. Implement the minimum behavior needed to pass.
4. Refactor while preserving contracts, dependency direction, and test evidence.
5. Run the affected fast suite, then the required repository quality commands.
6. Regenerate API documentation and compact code projections when public structure changes.
7. Update traceability and task evidence.

## Rules

- Test preconditions, postconditions, invariants, and failure semantics, not private implementation shape.
- Prefer selected framework facilities and maintained libraries over custom infrastructure.
- Keep external systems replaceable at component-test seams; verify real boundaries at integration level.
- Do not mark a slice implemented when only scaffolding, adapters, persistence wiring, or placeholders exist.
- If implementation requires an architecture change, stop the slice, update the owning artifact, and re-enter the nearest affected approval gate.
