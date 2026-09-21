# Delivery Foundation

## Purpose

Establish minimum viable CI/CD before full development so the walking skeleton receives executable feedback for build, contracts, documentation, packaging, and delivery assumptions.

## Blueprint obligations

- Implement the capabilities under `gates.implementation_readiness.requires` in `.blueprint/blueprint.toml` from a clean checkout, using the same repository-owned commands locally and in CI.
- Record the commands and selected tools in `design/foundation/tech.md`; record stage triggers, trust boundaries, evidence, and blocking behavior in `design/foundation/delivery.md`.
- Record the pipeline run, generated-document freshness, versioned artifact, and non-production delivery evidence in `design/foundation/implementation-readiness.md`.
- Do not grant untrusted validation jobs deployment authority. Production promotion automation is not required for readiness, but its owner and future trigger must be explicit.

Use the toolkit's `ci-cd-design` skill when available for general pipeline design and validation. This file specifies the minimum evidence required before full development.

## Evolution

Add integrated tests, deployment health, promotion, observability, and rollback controls as assembled behavior and operational risk grow. Do not defer proving the initial build, documentation, package, or non-production delivery path until full development.
