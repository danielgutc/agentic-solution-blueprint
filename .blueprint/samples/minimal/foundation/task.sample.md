# Task Tracker

## Snapshot

Status legend: `Not started`, `In progress`, `Designed`, `Approved`, `Implemented`.

| Area | Status | Coverage | Notes | Next action |
| --- | --- | --- | --- | --- |
| Product | Approved | `design/foundation/product.md` | Problem and goals documented. | Keep assumptions current. |
| Requirements | In progress | `design/foundation/requirements.md` | FR set started. | Add NFR and constraints. |
| Design | Approved | `design/foundation/design.md` | High-level decisions accepted. | Keep open questions visible. |
| C4 System | Designed | `design/c4/system/system.md` | Context exists. | Request approval for system level. |
| C4 Containers | Not started | | Awaiting system approval. | Draft container boundaries. |
| Code phase 1 (contracts) | Not started | | Blocked by C4 approvals. | Start after container approval. |
| Code phase 2 (internal design) | Not started | | Blocked by phase 1. | Start after phase 1 approval. |
| Executable implementation phase 1 (interfaces) | Not started | `implementation/` | No interface-driven runtime skeletons yet. | Scaffold after C4 code phase 2 approval. |
| Executable implementation phase 2 (tests) | Not started | `implementation/` | No executable contract tests yet. | Start after implementation interfaces are approved. |
| Executable implementation phase 3 (internals) | Not started | `implementation/` | No internal runtime behavior yet. | Start after implementation tests are approved. |
| Infrastructure phase 1 (deployment baseline) | Not started | `deployment/` | No deployable infrastructure baseline yet. | Start after infrastructure container contracts are approved. |
| Infrastructure phase 2 (verification) | Not started | `deployment/` | No infrastructure verification yet. | Start after deployment baseline approval. |
| Infrastructure phase 3 (operational readiness) | Not started | `deployment/` | No operational readiness notes yet. | Start after infrastructure verification approval. |

## Architecture progress (system to containers to components)

- System: `Designed`
- Container overview: `Not started`

### Container maturity matrix

| Container | Container design | Components design | Interfaces diagram | Code phase 1 (contracts) | Code phase 2 (class or domain design) | Implementation track | Implementation phase 1 | Implementation phase 2 | Implementation phase 3 | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `example-service` | Not started | Not started | Not started | Not started | Not started | Executable | Not started | Not started | Not started | <details><summary>Notes</summary>Pending system approval.</details> |
| `example-data-storage` | Not started | N/A (data store) | Not started | Not started | N/A (data store) | Infrastructure | Not started | Not started | Not started | <details><summary>Notes</summary>Infrastructure container.</details> |

### Component depth matrix

| Container | Components total | Components with phase 1 contract detail | Components with phase 2 code design section | Components with phase 2 class diagrams | Component docs |
| --- | --- | --- | --- | --- | --- |
| `example-service` | 0 | 0 | 0 | 0 | N/A |
| `example-data-storage` | N/A | N/A | N/A | N/A | N/A |

## Maturity guide

### Design columns

- `Container design`: the container boundary and responsibilities are documented.
- `Components design`: executable containers have component decomposition; data-store containers use `N/A` when they have no project-built internals.
- `Interfaces diagram`: diagram exports exist and preserve navigation links.
- `Code phase 1 (contracts)`: boundary contracts are defined using Design by Contract.
- `Code phase 2 (class or domain design)`: internal design is approved before runtime implementation.

### Implementation tracks

- `Executable`: project-built service/application code.
- `Infrastructure`: deployable support containers such as data stores.
- `Mixed`: both executable and infrastructure surfaces apply.
- `N/A`: no implementation/deployment surface is in scope.

### Implementation phases

- `Executable phase 1`: interface skeletons.
- `Executable phase 2`: tests-first contract specifications.
- `Executable phase 3`: internals, including approved core runtime behavior.
- `Infrastructure phase 1`: deployment baseline.
- `Infrastructure phase 2`: verification.
- `Infrastructure phase 3`: operational readiness.

## Active TODO

- `TASK-001` (`In progress`) Complete FR baseline and IDs.
- `TASK-002` (`Todo`) Code phase 1: define service interface contracts for `example-service`.
- `TASK-003` (`Todo`) Code phase 2: add class and domain design for approved components.
- `TASK-004` (`Todo`) Executable implementation phase 1: scaffold approved service interfaces after C4 code phase 2 approval.
- `TASK-005` (`Todo`) Infrastructure phase 1: create deployment baseline for `example-data-storage` after infrastructure container contracts are approved.

## Parking lot

- Decide whether replay support belongs in first release.

## Done recently

- Approved product scope and core outcomes.
