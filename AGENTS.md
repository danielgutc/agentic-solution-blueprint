# Agent Instructions

## Purpose

- Treat this repository as a reusable blueprint for starting new projects.
- Keep `AGENTS.md` concise: always-on behavior, governance, and routing only.
- Keep detailed authoring rules in `design/instructions/`, not in this file.

## Operating model

- Drive work through enduring artifacts in `design/foundation/` and `design/c4/`.
- Keep implementation assets in `implementation/`.
- Keep Codex-only helpers in `.codex/`.
- Use `design/templates/` as canonical artifact structures and `design/samples/` as quality references.

## Repository model

### Top-level layout

```text
.codex/
design/
implementation/
tools/
tests/
```

### Design layout

```text
design/
  foundation/
    product.md
    requirements.md
    tech.md
    design.md
    traceability-matrix.md
    task.md
    agent-topology.md (optional)
  c4/
    system/
    containers/
  instructions/
    process/
    artifacts/
    standards/
    file-types/
  templates/
    foundation/
    c4/
  samples/
```

## Blueprint governance sync

- Keep `origin` as the solution repository.
- Use `blueprint` remote for `agentic-solution-blueprint`.
- Treat `design/instructions/process/blueprint-sync.md` as the single source of truth for:
  - upstreamable governance scope
  - commit isolation requirements
  - sync branch policy
  - PR title convention
- Work is not complete until blueprint PR is created or updated and reported.

## Workflow model

- Select the next step explicitly: product, requirements, tech, design, C4, traceability, or implementation readiness.
- For structural or process changes, propose intended edits first and proceed only after explicit user approval.
- Think pyramidal: complete the current abstraction level before drilling down.
- Use domain-driven design across all decomposition steps.
- Use the workflow models in `design/instructions/process/workflow-models.md`.
- Enforce approval gates in `design/instructions/process/approval-gates.md`.
- Keep C4 code phases and runtime implementation as separate tracks:
  - C4 code phase 1 and 2 are architecture artifacts.
  - runtime implementation starts only after C4 code phase 2 approval.
  - runtime implementation flow follows `design/instructions/process/implementation-interface-test-first.md`.

## Architecture defaults

- Use microservice architecture by default when responsibilities justify independent ownership and deployability.
- Prefer bounded contexts for service boundaries.
- Keep runtime authority explicit; avoid accidental authority splits.
- Integrate services through contracts (APIs/events), not cross-schema reads.
- Keep persistence ownership per service boundary (shared engine allowed, shared schema ownership disallowed).
- Keep data stores modeled as data-store containers, not service containers.
- For service decomposition, default to facade API + orchestration/handler + persistence/integration adapters.
- If intentionally deviating from defaults, record rationale and split triggers at the nearest container-level decision.

## Diagrams and navigation defaults

- Use Draw.io (`.drawio`) as the authoritative diagram source.
- Keep sibling `.svg` exports for embedded documentation.
- Validate exports and required links after diagram changes.
- Keep diagram navigation focused on diagram-to-diagram drill-down.
- Follow shared rules in `design/instructions/standards/diagram-tooling.md` and `design/instructions/standards/navigation.md`.

## Artifact routing

- For workflow sequencing and approvals: `design/instructions/process/*.md`.
- For artifact-specific rules and section requirements: `design/instructions/artifacts/*.md`.
- For cross-cutting conventions (naming, status, navigation, diagrams): `design/instructions/standards/*.md`.
- For file-specific coding/writing rules: `design/instructions/file-types/*.md`.
- For concrete artifact shapes: `design/templates/foundation/*.template.md` and `design/templates/c4/*.template.md`.
- For task dashboard format: `design/instructions/artifacts/task-tracker.md`.
- For runtime testing process and boundaries: `design/instructions/process/dotnet-testing.md`.

## Skills model

- Use skills for repeatable, on-demand complex tasks.
- Use `blueprint-governance` for instruction/template/sample refactors.
- Use C4 skills for level-specific architecture authoring:
  - `c4-system-authoring`
  - `c4-system-containers-authoring`
  - `c4-container-authoring`
  - `c4-component-authoring`
  - `diagram-export-verify`
  - `blueprint-sync-pr`

## Maintenance

- Keep this file short and stable.
- When a rule becomes detailed or procedural, move it to `design/instructions/` or a skill.
- Keep templates, instructions, and samples aligned in the same change set.
