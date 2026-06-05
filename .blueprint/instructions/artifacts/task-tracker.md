# Task Tracker Artifact

Use this instruction for `design/foundation/task.md`.

If `tasks.md` exists at repository root, treat it as a lightweight local queue; do not replace this canonical tracker with `tasks.md`.

## Purpose

Provide a glanceable dashboard of:
- abstraction-level maturity
- container and component progress
- executable implementation and deployable infrastructure gate progress
- delivery-governance design and rollout progress
- active work queue
- deferred backlog

## Required sections

```text
# Task Tracker

## Table of contents
## Snapshot
## Architecture progress (system to containers to components)
## Maturity guide
## Active TODO
## Parking lot
## Done recently
```

## Required `Snapshot` schema

Status legend must include:
- `Not started`
- `In progress`
- `Designed`
- `Approved`
- `Implemented`

Table schema:

```text
| Area | Status | Coverage | Notes | Next action |
| --- | --- | --- | --- | --- |
```

## Required architecture matrices

### Container maturity matrix

```text
| Container | Container design | Components design | Interfaces diagram | Code phase 1 (contracts) | Code phase 2 (class or domain design) | Implementation track | Implementation phase 1 | Implementation phase 2 | Implementation phase 3 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

Keep `Notes` cells in the Container maturity matrix collapsed with:

```html
<details><summary>Notes</summary>...</details>
```

This keeps the matrix glanceable when notes contain approval conditions, implementation details, or operational context.

## Required `Maturity guide` content

Add a concise `Maturity guide` section before `Active TODO`.

The guide must explain the design-side columns:
- `Container design`: container responsibility, boundary, dependencies, contracts, and track are documented.
- `Components design`: component decomposition exists for executable/application containers; use `N/A` for pure data-store or infrastructure containers without project-built components.
- `Interfaces diagram`: relevant diagrams exist and are exported with required navigation links.
- `Code phase 1 (contracts)`: Design by Contract obligations, ports, payloads, and boundary contracts are documented and approved.
- `Code phase 2 (class or domain design)`: internal class, domain, persistence, and collaboration design is documented and approved before runtime implementation.

The guide must explain implementation tracks:
- `Executable`: project-built service/application code; phase 1 interfaces, phase 2 tests, phase 3 internals.
- `Infrastructure`: deployable data store, file/object store, broker, cache, or support dependency; phase 1 deployment baseline, phase 2 verification, phase 3 operational readiness.
- `Mixed`: both executable code and infrastructure surfaces exist; clarify covered surfaces in notes or split TODO items by track.
- `N/A`: no implementation/deployment surface exists in the current scope.

The guide must explain implementation phase meanings:
- `Executable phase 1`: interface-driven implementation skeletons and dependency-boundary wiring.
- `Executable phase 2`: tests-first executable contract specifications.
- `Executable phase 3`: internal runtime implementation that satisfies approved tests and contracts, including the approved core business/runtime behavior.
- `Infrastructure phase 1`: deployment baseline assets.
- `Infrastructure phase 2`: infrastructure verification.
- `Infrastructure phase 3`: operational readiness, including runbooks, backup/restore, observability, or cleanup tasks when relevant.

### Component depth matrix

```text
| Container | Components total | Components with phase 1 contract detail | Components with phase 2 code design section | Components with phase 2 class diagrams | Component docs |
| --- | --- | --- | --- | --- | --- |
```

## Two-phase rule

- Code phase 1 tracks contracts and interfaces.
- Code phase 2 tracks internal class and domain design.
- For storage-only containers, use `N/A` for component-specific code-phase columns.

## Implementation track rule

- Select one or more implementation tracks per target scope after C4 approval.
- Executable service/application scopes use `.blueprint/instructions/process/implementation-interface-test-first.md`.
- Pure deployable infrastructure/data-store/supporting dependency scopes use `.blueprint/instructions/process/implementation-deployable-infrastructure.md`.
- Mixed scopes may use both tracks, but the task tracker must identify which status applies to which surface.
- For pure infrastructure/data-store containers, record component-specific code phase 2 and executable implementation phases as `N/A` when there are no project-built runtime internals.
- Executable implementation phase 1 tracks interface-driven implementation skeletons and dependency-boundary wiring.
- Executable implementation phase 2 tracks tests-first executable contract specifications.
- Executable implementation phase 3 tracks internal runtime implementation that satisfies approved tests and contracts, including approved core behavior.
- Do not mark executable implementation phase 3 `Approved` when only scaffolding, orchestration, persistence wiring, deterministic placeholders, or adapter stubs are complete and core behavior is still deferred.
- For partial implementation slices, name the completed capability and the missing core capability explicitly in `Notes`, `Next action`, and relevant TODOs. Prefer concrete slice names such as `pipeline/state/publication groundwork`, `normalized-source terrain semantics bake`, or `raw provider ingestion pending` over vague labels like `internals implemented`.
- Infrastructure phase 1 tracks deployment baseline assets.
- Infrastructure phase 2 tracks infrastructure verification.
- Infrastructure phase 3 tracks operational readiness.
- If runtime implementation changes contracts, boundaries, persistence ownership, or output authority, update the relevant C4 artifacts and re-approve before continuing.

## Gate status authority

- `design/foundation/task.md` is the authoritative source for recorded gate status.
- Conversation approvals become durable gate status only when reflected in this tracker.
- If another artifact suggests a different status, resolve the mismatch in this tracker before proceeding deeper.

## Matrix consistency rule

- Container maturity status must respect the approval gate sequence from left to right.
- A later phase must not be marked `Approved` unless prerequisite phases for the same container are also marked `Approved`.
- Invalid example: `Designed | Designed | Designed | Approved`.
- Valid corrections:
  - mark prerequisite phases `Approved` when they were explicitly approved
  - or keep the later phase `Designed` until prerequisite approval is recorded
- Approved phases may be revised later, but revisions that affect downstream contracts or design should mark downstream phases for re-review.
- Implementation phase statuses must not be stronger than prerequisite C4 approval statuses for the same scope and track.

## `Active TODO` convention

- Use IDs in `TASK-xxx` format.
- Include status in parentheses.
- Keep ordering phase-first when both phases exist:
  - close phase 1 items before phase 2 expansion.
- For executable implementation work, keep ordering interface skeletons, then tests, then internals.
- For deployable infrastructure work, keep ordering deployment baseline, then verification, then operational readiness.

Examples:

```text
- `TASK-001` (`In progress`) <description>.
- `TASK-002` (`Todo`) Code phase 1: <description>.
- `TASK-003` (`Todo`) Code phase 2: <description>.
- `TASK-004` (`Todo`) Executable implementation phase 1: <description>.
- `TASK-005` (`Todo`) Infrastructure phase 1: <description>.
```
