# Full Development

## Prerequisite

The relevant scope in `design/foundation/implementation-readiness.md` must be explicitly approved.

## Blueprint obligations

- Work within the approved component contracts and requirement IDs for the readiness scope.
- Implement the MVP scope, quality obligations, and PoC-to-product gap resolutions recorded in the approved product, solution, and technical artifacts. Return missing or contradictory rationale to its owner before changing the contracts.
- Work within the implementation units and command working directories approved for that scope; do not broaden a unit's toolchain settings to unrelated workspaces.
- Implement behavior through TDD and run the repository's required quality commands.
- Update source-owned API comments with contract changes. Regenerate canonical unit/profile API pages and configured container/component/interface projections; verify committed outputs, reciprocal architecture links, coverage disclosure, and source links are current.
- Update `design/foundation/traceability-matrix.md` and `design/foundation/task.md` with implementation and test evidence.
- Do not mark a slice implemented when only scaffolding, adapters, persistence wiring, or placeholders exist.
- If behavior requires an architecture change, return to the owning role and affected approval gate before continuing.

Use the toolkit's `test-driven-development` skill when available for the red-green-refactor method. This file governs the repository's gate and artifacts, not a second TDD procedure.

Follow `../standards/implementation-layout.md` when adding projects, packages, tests, or generated outputs.
