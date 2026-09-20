# CI/CD Instructions

## Purpose

Establish a minimum viable delivery pipeline before full development so architecture, tests, documentation, packaging, and deployment assumptions receive early executable feedback.

## Implementation Readiness Pipeline

Before the implementation-readiness gate can pass, CI must run from a clean checkout and:

1. Restore dependencies and build the walking skeleton reproducibly.
2. Run the initial unit, component, and contract tests.
3. Run formatting checks and static analysis.
4. Generate the API reference, `code.md`, and code-diagram sources.
5. Verify that committed generated projections are current.
6. Package one immutable, versioned artifact.
7. Exercise a non-production delivery path appropriate to the product.
8. Preserve enough evidence to diagnose a failed gate.

Use repository-owned commands for these stages so local and CI behavior remain aligned. Record the selected commands and platforms in `design/foundation/tech.md`.

## Progressive Delivery

- The readiness pipeline does not need final production deployment automation.
- Add integration and end-to-end gates as assembled behavior becomes available.
- Add production promotion, approvals, observability checks, and rollback automation before the first production release.
- Evolve pipeline controls in proportion to operational and compliance risk.

## Boundaries

- Never place credentials in pipeline definitions, generated documentation, logs, or committed configuration.
- Do not make full development responsible for discovering that the project cannot build, package, document, or follow its intended delivery path.
- Do not duplicate build logic in provider-specific workflow files when it can live in repository-owned commands.
