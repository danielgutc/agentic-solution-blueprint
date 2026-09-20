# Implementation Readiness Artifact

## Purpose

Use `design/foundation/implementation-readiness.md` as the auditable decision record for allowing a scoped implementation slice to enter full development.

## Canonical shape

Use `.blueprint/templates/foundation/implementation-readiness.template.md`.

## Rules

- Evaluate every capability declared under `gates.implementation_readiness.requires` in `.blueprint/blueprint.toml`.
- Link commands, artifacts, pipeline runs, generated-document checks, package identifiers, and non-production delivery evidence.
- Use the criterion statuses from `../standards/status-taxonomy.md`.
- Scope the record to named containers, components, requirements, or slices.
- Treat exclusions as accepted exceptions with rationale, owner, expiry or trigger, and compensating evidence.
- Do not approve readiness when CI has not reproduced the walking skeleton from a clean checkout.
- Reassess the affected criteria when the toolchain, architecture, package model, or delivery path changes.
