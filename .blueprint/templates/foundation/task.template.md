# Task Tracker

## Table of contents

- [Snapshot](#snapshot)
- [Architecture progress (system to containers to components)](#architecture-progress-system-to-containers-to-components)
- [Maturity guide](#maturity-guide)
- [Active TODO](#active-todo)
- [Parking lot](#parking-lot)
- [Done recently](#done-recently)

## Snapshot

Status legend: `Not started`, `In progress`, `Designed`, `Approved`, `Implemented`.

| Area | Status | Coverage | Notes | Next action |
| --- | --- | --- | --- | --- |
| Product | Not started | | | |
| Requirements | Not started | | | |
| Tech | Not started | | | |
| Design | Not started | | | |
| C4 System | Not started | | | |
| C4 Containers | Not started | | | |
| C4 Components | Not started | | | |
| Code phase 1 (contracts) | Not started | | | |
| Code phase 2 (internal design) | Not started | | | |
| Executable implementation phase 1 (interfaces) | Not started | | | |
| Executable implementation phase 2 (tests) | Not started | | | |
| Executable implementation phase 3 (internals) | Not started | | | |
| Infrastructure phase 1 (deployment baseline) | Not started | | | |
| Infrastructure phase 2 (verification) | Not started | | | |
| Infrastructure phase 3 (operational readiness) | Not started | | | |

## Architecture progress (system to containers to components)

- System: <link> - `Not started`
- Container overview: <link> - `Not started`

### Container maturity matrix

| Container | Container design | Components design | Interfaces diagram | Code phase 1 (contracts) | Code phase 2 (class or domain design) | Implementation track | Implementation phase 1 | Implementation phase 2 | Implementation phase 3 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <container> | Not started | Not started | Not started | Not started | Not started | <Executable / Infrastructure / Mixed / N/A> | Not started | Not started | Not started | <details><summary>Notes</summary>Container status notes.</details> |

### Component depth matrix

| Container | Components total | Components with phase 1 contract detail | Components with phase 2 code design section | Components with phase 2 class diagrams | Component docs |
| --- | --- | --- | --- | --- | --- |
| <container> | 0 | 0 | 0 | 0 | <link> |

## Maturity guide

### Design columns

- `Container design`: container responsibility, boundary, dependencies, contracts, and track are documented.
- `Components design`: component decomposition exists for executable/application containers; use `N/A` for pure data-store or infrastructure containers without project-built components.
- `Interfaces diagram`: relevant diagrams exist and are exported with required navigation links.
- `Code phase 1 (contracts)`: Design by Contract obligations, ports, payloads, and boundary contracts are documented and approved.
- `Code phase 2 (class or domain design)`: internal class, domain, persistence, and collaboration design is documented and approved before runtime implementation.

### Implementation tracks

- `Executable`: project-built service/application code; phase 1 interfaces, phase 2 tests, phase 3 internals.
- `Infrastructure`: deployable data store, file/object store, broker, cache, or support dependency; phase 1 deployment baseline, phase 2 verification, phase 3 operational readiness.
- `Mixed`: both executable code and infrastructure surfaces exist; clarify covered surfaces in notes or split TODO items by track.
- `N/A`: no implementation/deployment surface exists in the current scope.

### Implementation phases

- `Executable phase 1`: interface-driven implementation skeletons and dependency-boundary wiring.
- `Executable phase 2`: tests-first executable contract specifications.
- `Executable phase 3`: internal runtime implementation that satisfies approved tests and contracts, including the approved core business/runtime behavior.
- `Infrastructure phase 1`: deployment baseline assets.
- `Infrastructure phase 2`: infrastructure verification.
- `Infrastructure phase 3`: operational readiness, including runbooks, backup/restore, observability, or cleanup tasks when relevant.

For partial executable implementation slices, name completed capabilities and missing core capabilities explicitly in the Snapshot, Container maturity matrix notes, and Active TODOs. Do not mark phase 3 `Approved` when core behavior is still deferred behind scaffolding, persistence wiring, deterministic placeholders, or adapter stubs.

## Active TODO

- `TASK-001` (`Todo`) <description>.
- `TASK-002` (`Todo`) Code phase 1: <description>.
- `TASK-003` (`Todo`) Code phase 2: <description>.
- `TASK-004` (`Todo`) Executable implementation phase 1: <description>.
- `TASK-005` (`Todo`) Infrastructure phase 1: <description>.

## Parking lot

- <deferred item>

## Done recently

- <recently completed item>
