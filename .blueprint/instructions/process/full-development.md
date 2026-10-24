# Full Development

## Prerequisite

The relevant scope in `design/foundation/implementation-readiness.md` must be explicitly approved.

## Blueprint obligations

- Work within the approved component contracts and requirement IDs for the readiness scope.
- Work within the implementation units and command working directories approved for that scope; do not broaden a unit's toolchain settings to unrelated workspaces.
- Implement behavior through TDD and run the repository's required quality commands.
- Update source-owned API comments with public contract changes. Regenerate component guides, per-symbol Markdown API pages, and code projections; verify committed outputs and source links are current.
- Update `design/foundation/traceability-matrix.md` and `design/foundation/task.md` with implementation and test evidence.
- Do not mark a slice implemented when only scaffolding, adapters, persistence wiring, or placeholders exist.
- If behavior requires an architecture change, return to the owning role and affected approval gate before continuing.

Use the toolkit's `test-driven-development` skill when available for the red-green-refactor method. This file governs the repository's gate and artifacts, not a second TDD procedure.

Follow `../standards/implementation-layout.md` when adding projects, packages, tests, or generated outputs.
