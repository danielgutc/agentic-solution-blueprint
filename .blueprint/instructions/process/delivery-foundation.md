# Delivery Foundation

## Purpose

Establish minimum viable CI/CD before full development so the walking skeleton receives executable feedback for build, contracts, documentation, packaging, and delivery assumptions.

## Required capabilities

- Repository-owned commands work from a clean checkout.
- The walking skeleton builds reproducibly.
- Initial unit, component, and contract tests pass.
- Formatting and static analysis pass.
- API reference and compact code projections generate and validate.
- Committed generated projections are proven current.
- One immutable, versioned artifact is packaged.
- An appropriate non-production delivery path is exercised.
- CI preserves actionable evidence for every required gate.

## Delivery design

- Define triggers, commands, required results, evidence, trust level, and blocking behavior in `design/foundation/delivery.md`.
- Keep provider workflow files thin; reusable logic belongs in repository scripts or build tooling.
- Validate untrusted proposed changes without granting deployment authority.
- Build once and promote the same artifact when the selected platform supports it.
- Production promotion automation is not required for implementation readiness, but its ownership and trigger must be explicit.

## Evolution

Add integration, end-to-end, deployment health, promotion, observability, and rollback controls as assembled behavior and operational risk grow. Do not defer discovering that the project cannot build, document, package, or follow its intended delivery path until full development.
