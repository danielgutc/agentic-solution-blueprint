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
| Implementation | Not started | `implementation/` | No runtime code yet. | Scaffold after design gates. |

## Architecture progress (system to containers to components)

- System: `Designed`
- Container overview: `Not started`

### Container maturity matrix

| Container | Container design | Components design | Interfaces diagram | Code phase 1 (contracts) | Code phase 2 (class or domain design) | Implementation | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `example-service` | Not started | Not started | Not started | Not started | Not started | Not started | Pending system approval. |
| `example-data-storage` | Not started | N/A (data store) | Not started | Not started | N/A (data store) | Not started | Infrastructure container. |

### Component depth matrix

| Container | Components total | Components with phase 1 contract detail | Components with phase 2 code design section | Components with phase 2 class diagrams | Component docs |
| --- | --- | --- | --- | --- | --- |
| `example-service` | 0 | 0 | 0 | 0 | N/A |
| `example-data-storage` | N/A | N/A | N/A | N/A | N/A |

## Active TODO

- `TASK-001` (`In progress`) Complete FR baseline and IDs.
- `TASK-002` (`Todo`) Code phase 1: define service interface contracts for `example-service`.
- `TASK-003` (`Todo`) Code phase 2: add class and domain design for approved components.

## Parking lot

- Decide whether replay support belongs in first release.

## Done recently

- Approved product scope and core outcomes.
