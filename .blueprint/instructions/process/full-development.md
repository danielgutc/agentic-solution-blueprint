# Full Development

## Prerequisite

The relevant scope in `design/foundation/implementation-readiness.md` must be explicitly approved.

## Blueprint obligations

- Work within the approved component contracts and requirement IDs for the readiness scope.
- Implement behavior through TDD and run the repository's required quality commands.
- Regenerate API documentation and compact code projections when public structure changes; verify committed projections are current.
- Update `design/foundation/traceability-matrix.md` and `design/foundation/task.md` with implementation and test evidence.
- Do not mark a slice implemented when only scaffolding, adapters, persistence wiring, or placeholders exist.
- If behavior requires an architecture change, return to the owning role and affected approval gate before continuing.

Use the toolkit's `test-driven-development` skill when available for the red-green-refactor method. This file governs the repository's gate and artifacts, not a second TDD procedure.
