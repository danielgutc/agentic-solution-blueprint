# Blueprint 2.0 Migration

## Baseline

`main_v2` starts from the clean `blueprint-1.6` baseline. The later `origin/main` history was reviewed as a source of reusable governance ideas, not used as the branch base, because it combines blueprint evolution with a concrete application and its deployment assets.

## Retrofitted

- Modular instructions under `.blueprint/instructions/` so agents load only phase-relevant detail.
- Canonical artifact shapes under `.blueprint/templates/`.
- A compact lifecycle and multi-agent dashboard at `design/foundation/task.md`.
- Delivery stage, evidence, trust, artifact, exception, and recovery decisions at `design/foundation/delivery.md`.
- An explicit C4 system-container landscape before per-container decomposition.
- Design by Contract for service, component, persistence, and handoff boundaries.
- Native unit/component tests plus framework-agnostic integration, acceptance, smoke, and end-to-end guidance.
- Maintained-library and selected-platform capabilities before custom plumbing.
- Gate-status consistency, scoped approvals, re-review triggers, and expiring exceptions.

## V2 direction

- Reusable roles and skills remain in `agentic-engineering-toolkit`; only project-specific skills belong in `.agents/skills/`.
- Human-authored C4 ends at component intent. Source interfaces, API comments, and executable tests generate compact code projections and full API references.
- Minimum viable CI/CD must build, test, analyze, document, package, and exercise non-production delivery before full development.
- Provider, cloud, deployment platform, framework, and diagram-rendering choices remain project decisions unless explicitly selected.

## Breaking path changes

- `design/instructions/*.md` moved to `.blueprint/instructions/file-types/*.md`.
- `AGENTS.md` is now a concise always-on contract and router rather than the full handbook.
- Consuming projects add `delivery.md`, `task.md`, and `c4/containers/system-containers.md`.
- `.blueprint/blueprint.toml` declares version `2.0`, modular paths, coordination metadata, and twelve implementation-readiness capabilities.

## Intentionally excluded

- Solution-to-blueprint remote and pull-request synchronization rules.
- Repository-local copies of reusable skills under `.codex/skills/`.
- ASP.NET-specific scaffolding and output-routing policy.
- Kubernetes as a default deployment model.
- Draw.io as a mandatory diagram source.
- Concrete Petshop, game, frontend, backend, CI, and deployment implementation.
