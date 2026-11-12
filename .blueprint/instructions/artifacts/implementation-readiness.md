# Implementation Readiness Artifact

## Purpose

Use `design/foundation/implementation-readiness.md` as the current scoped decision summary allowing an implementation slice to enter full development. Keep applicable approvals and their conditions explicit; do not append assessment rounds, execution logs, or handoff histories.

## Canonical shape

Use `.blueprint/templates/foundation/implementation-readiness.template.md`.

## Rules

- Evaluate every capability declared under `gates.implementation_readiness.requires` in `.blueprint/blueprint.toml`.
- Link reproducible commands/test definitions, artifacts, pipeline runs, generated-document checks, package identifiers, and non-production delivery evidence. Keep only current criterion status, blockers, evidence references, and material limits here; report execution detail in chat or generated outputs under [verification evidence](../standards/verification-evidence.md).
- Use the criterion statuses from `../standards/status-taxonomy.md`.
- Scope the record to named containers, components, implementation units, requirements, or slices, and identify the relevant toolchain roots and command working directories.
- Treat exclusions as accepted exceptions with rationale, owner, expiry or trigger, and compensating evidence.
- Do not approve readiness when CI has not reproduced the walking skeleton from a clean checkout.
- Reassess the affected criteria when an implementation-unit boundary, toolchain root, command working directory, architecture, package model, or delivery path changes.
