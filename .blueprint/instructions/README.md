# Blueprint Instructions

Use this directory for reusable project policy that agents load only when it applies to the current phase or artifact.

## Precedence

1. `AGENTS.md` defines always-on behavior and routing.
2. `process/` defines lifecycle sequence, gates, handoffs, implementation flow, and verification.
3. `artifacts/` defines artifact purpose, ownership, and quality criteria.
4. `standards/` defines cross-cutting conventions.
5. `file-types/` defines language and file-specific rules.
6. `.blueprint/templates/` defines canonical document shapes.

When instructions conflict, follow the higher-precedence source and remove the lower-level drift.

## Progressive loading

- Product, MVP, or requirements work: read `process/lifecycle.md`, `artifacts/foundation.md`, and `standards/navigation.md`.
- Architecture work: also read `process/approval-gates.md`, `artifacts/c4.md`, `standards/design-by-contract.md`, `standards/navigation.md`, `standards/diagram-tooling.md`, and `file-types/drawio.md` when drawing diagrams.
- Multi-agent delegation or handoff: read `process/multi-agent-coordination.md` and `artifacts/task-tracker.md`.
- Technical design or walking-skeleton work: read `process/technical-design.md` and the relevant file-type rules.
- Delivery work: read `process/delivery-foundation.md`, `artifacts/delivery.md`, and `file-types/ci-cd.md`.
- Full implementation: read `process/full-development.md`, `standards/design-by-contract.md`, and the relevant language rules.
- Integration, acceptance, or end-to-end work: read `process/integrated-verification.md`.
- Read templates only when creating or repairing the corresponding artifact.

## Authoring rule

Keep policy in instructions, reusable shapes in templates, project decisions in `design/`, and executable behavior in `implementation/`, `tests/`, or `tools/`. Do not duplicate a detailed rule in `AGENTS.md`.

The reusable engineering toolkit supplies role-specific methods through agents and skills when installed. Blueprint instructions remain usable without that toolkit and state only this repository's additional paths, approval gates, and evidence obligations.
