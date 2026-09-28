# Agent Instructions

## Purpose

- Treat this repository as a reusable blueprint for software projects that need explicit product, architecture, delivery, and verification governance.
- Keep this file limited to always-on behavior and routing. Load detailed rules from `.blueprint/instructions/` only when the current task needs them.
- Treat README files as descriptive navigation unless this file or a routed instruction makes them normative.

## Operating model

- Read `.blueprint/blueprint.toml` before selecting a workflow or lifecycle phase.
- Work from the highest relevant abstraction downward and delay lower-level decisions until their inputs and boundaries are stable.
- Keep durable project state in `design/foundation/`, architecture in `design/c4/`, runtime code in `implementation/`, and cross-system verification in `tests/`.
- Use `design/foundation/task.md` as the compact multi-agent status and handoff dashboard. Do not rely on conversation history as the only record of progress or approval.
- Keep project-specific skills in `.agents/skills/`. Use reusable roles and engineering skills from the user-level engineering toolkit rather than copying them into this repository.
- Do not create containers, components, extension points, or infrastructure before approved requirements and architecture justify them.

## Role ownership

- The `product_owner` owns product intent, design-thinking evidence, MVP boundaries, requirements, and acceptance intent.
- The `solutions_architect` owns technical direction, system scope, domain boundaries, C4 context, and authoritative container boundaries.
- The `technical_architect` owns components, contracts, internal structure, test seams, walking skeletons, and documentation-generation tooling inside approved containers; code-level projections are generated, not authored by hand.
- The `software_engineer` implements approved skeleton bodies through TDD after implementation readiness is approved.
- The `infrastructure_engineer` owns the delivery foundation, CI/CD, environments, infrastructure as code, and documentation execution in CI.
- The `test_engineer` owns independent integration, contract, end-to-end, acceptance, smoke, and regression verification.
- Keep each role at its assigned abstraction. Return boundary changes to the owning role instead of silently changing them downstream.

## Repository model

- Keep reusable policy and canonical shapes in `.blueprint/`.
- Keep enduring project decisions and evidence in `design/`.
- Keep runtime code in `implementation/`, cross-system tests in `tests/`, and repository-owned automation in `tools/`.
- Keep Codex working memory in `.codex/` and project-specific skills in `.agents/skills/`.
- Use the path registry in `.blueprint/blueprint.toml` rather than duplicating the full tree here.

## Lifecycle

### Workflow selection

- Leave `selected_workflow` as `unset` only while maintaining the reusable template; a consuming project must set it to `requirements-first` or `design-first` before advancing enduring project artifacts.
- Select `requirements-first` when desired behavior is clearer than the solution approach.
- Select `design-first` when constraints, integrations, feasibility, or architecture risk lead.
- Follow `.blueprint/instructions/process/lifecycle.md` for phase sequence, outcomes, and re-entry rules.
- Seek explicit approval before advancing to the next lifecycle phase.
- Never pass the design-approval or implementation-readiness gate implicitly.

### Approval gates

- Design approval is required before enduring C4 system or container work.
- Scoped implementation-readiness approval is required before full feature development.
- Record approvals and re-review triggers in `design/foundation/task.md`.
- Follow `.blueprint/instructions/process/approval-gates.md` for evidence and consistency rules.

### Instruction routing

- Lifecycle, gates, role handoffs, implementation flow, and verification: `.blueprint/instructions/process/`.
- Foundation, C4, delivery, task, and readiness artifacts: `.blueprint/instructions/artifacts/`.
- Cross-cutting conventions: `.blueprint/instructions/standards/`.
- Language and file-specific rules: `.blueprint/instructions/file-types/`.
- Canonical document shapes: `.blueprint/templates/`.
- Read only the files relevant to the active role, phase, artifact, and file type.

## Enduring artifacts

- Keep product, MVP and prioritization, requirements, technology, design, delivery, traceability, task status, and readiness evidence in `design/foundation/`.
- Keep human-authored C4 content focused on system, container, and component intent.
- Treat source interfaces, ecosystem-native API comments, and executable tests as the implementation contract source.
- Generate deterministic `code.md` and code-diagram sources from code and tests. Do not edit them manually.
- Publish full API references and rendered outputs as CI artifacts by default rather than committing them.
- During technical design, create only the walking skeleton needed to prove architecture-significant contracts, tests, documentation, packaging, and delivery.
- Begin full feature implementation only after scoped implementation readiness is approved.

## C4

- Use `design/c4/` for approved, enduring architecture rather than temporary plans.
- Model one abstraction level at a time and keep components nested under their owning container.
- Add containers only after design approval and components only during technical design.
- Follow `.blueprint/instructions/artifacts/c4.md`, `.blueprint/instructions/standards/design-by-contract.md`, and the relevant templates.

## Implementation

- Keep implementation aligned with approved requirements, C4 boundaries, contracts, and traceability.
- Before readiness approval, create only the walking skeleton needed to prove contracts and delivery assumptions.
- After readiness approval, follow `.blueprint/instructions/process/full-development.md` and implement small TDD slices.
- Return architecture drift to the owning role and gate before continuing.

## File-type instructions

- Read `.blueprint/instructions/file-types/<type>.md` when editing a covered file type.
- API documentation and CI/CD rules also route to their related process and artifact instructions.

## Precedence

Use this order when instructions conflict:

1. `AGENTS.md`
2. `.blueprint/instructions/process/`
3. `.blueprint/instructions/artifacts/`
4. `.blueprint/instructions/standards/`
5. `.blueprint/instructions/file-types/`
6. `.blueprint/templates/`

Resolve drift in the lower-precedence source instead of carrying contradictory rules.

## Maintenance

- Keep project design artifacts in `design/`.
- Keep repo-local scripts and developer automation in `tools/`.
- Keep cross-component validation in `tests/`.
- Keep Codex-specific memory in `.codex/` and project-specific skills in `.agents/skills/`.
- Keep reusable agents and skills in the external engineering toolkit and install them through user-level symbolic links.
- Keep `.blueprint/blueprint.toml`, instructions, templates, and seeded artifacts aligned in the same change.
- Keep reusable policy technology-neutral unless the blueprint explicitly selects a default.
- Prefer established, actively maintained libraries and platform capabilities over custom plumbing when they satisfy approved constraints.
- Record exceptions, owners, expiry conditions, and compensating evidence rather than weakening a gate silently.
