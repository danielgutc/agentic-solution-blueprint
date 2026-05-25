# Task Tracker Artifact

Use this instruction for `design/foundation/task.md`.

If `tasks.md` exists at repository root, treat it as a lightweight local queue; do not replace this canonical tracker with `tasks.md`.

## Purpose

Provide a glanceable dashboard of:
- abstraction-level maturity
- container and component progress
- runtime implementation gate progress
- active work queue
- deferred backlog

## Required sections

```text
# Task Tracker

## Table of contents
## Snapshot
## Architecture progress (system to containers to components)
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
| Container | Container design | Components design | Interfaces diagram | Code phase 1 (contracts) | Code phase 2 (class or domain design) | Implementation phase 1 (interfaces) | Implementation phase 2 (tests) | Implementation phase 3 (internals) | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
```

### Component depth matrix

```text
| Container | Components total | Components with phase 1 contract detail | Components with phase 2 code design section | Components with phase 2 class diagrams | Component docs |
| --- | --- | --- | --- | --- | --- |
```

## Two-phase rule

- Code phase 1 tracks contracts and interfaces.
- Code phase 2 tracks internal class and domain design.
- For storage-only containers, use `N/A` for component-specific code-phase columns.

## Runtime implementation phase rule

- Runtime implementation starts only after C4 code phase 2 is approved for the target container/component scope.
- Implementation phase 1 tracks interface-driven implementation skeletons and dependency-boundary wiring.
- Implementation phase 2 tracks tests-first executable contract specifications.
- Implementation phase 3 tracks internal runtime implementation that satisfies approved tests and contracts.
- Implementation phase statuses correspond to approval gates from `.blueprint/instructions/process/implementation-interface-test-first.md`.
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
- Implementation phase statuses must not be stronger than prerequisite C4 approval statuses for the same scope.

## `Active TODO` convention

- Use IDs in `TASK-xxx` format.
- Include status in parentheses.
- Keep ordering phase-first when both phases exist:
  - close phase 1 items before phase 2 expansion.
- For implementation work, keep ordering interface skeletons, then tests, then internals.

Examples:

```text
- `TASK-001` (`In progress`) <description>.
- `TASK-002` (`Todo`) Code phase 1: <description>.
- `TASK-003` (`Todo`) Code phase 2: <description>.
- `TASK-004` (`Todo`) Implementation phase 1: <description>.
```
