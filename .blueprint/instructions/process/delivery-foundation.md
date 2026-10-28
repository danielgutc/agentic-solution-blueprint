# Delivery Foundation

## Purpose

Establish minimum viable CI/CD before full development so the walking skeleton receives executable feedback for build, contracts, documentation, packaging, and delivery assumptions.

## Blueprint obligations

- Implement the capabilities under `gates.implementation_readiness.requires` in `.blueprint/blueprint.toml` from a clean checkout, using the same repository-owned commands locally and in CI.
- Record each command, selected tool, implementation-unit or aggregate scope, and working directory in `design/foundation/tech.md`; record stage triggers, trust boundaries, evidence, and blocking behavior in `design/foundation/delivery.md`.
- Record the pipeline run, generated-document freshness, versioned artifact, and non-production delivery evidence in `design/foundation/implementation-readiness.md`.
- Make the repository documentation command build native source documentation, run the pinned Doxygen capability and expected-symbol coverage checks, generate committed canonical unit/profile pages plus configured C4 link views and relationship sources, validate their links, bindings, coverage disclosure, and provenance, and fail when regeneration changes the working tree.
- Publish optional aggregate API output as a CI artifact. Do not let ignored Doxygen XML, HTML, compiler output, or tool caches become the only copy of committed canonical pages or architecture navigation.
- Do not grant untrusted validation jobs deployment authority. Production promotion automation is not required for readiness, but its owner and future trigger must be explicit.

Use the toolkit's `ci-cd-design` skill when available for general pipeline design and validation. This file specifies the minimum evidence required before full development.

Follow `../standards/implementation-layout.md` when composing unit-local commands into repository-level checks and packages.
Follow `../file-types/api-documentation.md` for the default Doxygen pipeline, language exceptions, output paths, and documentation quality checks.

## Evolution

Add integrated tests, deployment health, promotion, observability, and rollback controls as assembled behavior and operational risk grow. Do not defer proving the initial build, documentation, package, or non-production delivery path until full development.

## MVP delivery baseline

Apply [MVP version 1.0 quality](../standards/mvp-quality.md) to the supported release scope. An experimental package or non-production walking-skeleton path proves only its named delivery seams; it does not establish complete release acceptance. Qualify or replace PoC-only mechanisms before release, while keeping operational complexity proportional to approved requirements.
