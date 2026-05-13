# Task Tracker Artifact

Use this instruction for `design/foundation/task.md`.

If `tasks.md` exists at repository root, treat it as a lightweight local queue; do not replace this canonical tracker with `tasks.md`.

## Purpose

Provide a glanceable dashboard of:
- abstraction-level maturity
- container and component progress
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
| Container | Container design | Components design | Interfaces diagram | Code phase 1 (contracts) | Code phase 2 (class or domain design) | Implementation | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
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

## `Active TODO` convention

- Use IDs in `TASK-xxx` format.
- Include status in parentheses.
- Keep ordering phase-first when both phases exist:
  - close phase 1 items before phase 2 expansion.

Examples:

```text
- `TASK-001` (`In progress`) <description>.
- `TASK-002` (`Todo`) Code phase 1: <description>.
- `TASK-003` (`Todo`) Code phase 2: <description>.
```
