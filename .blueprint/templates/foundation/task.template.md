# Task Tracker

[README](../../../README.md) / Foundation / Task tracker

Related foundation documents:
- [Product](./product.template.md)
- [MVP and prioritization](./mvp.template.md)
- [Requirements](./requirements.template.md)
- [Tech](./tech.template.md)
- [Design](./design.template.md)
- [Delivery governance](./delivery.template.md)
- [Traceability matrix](./traceability-matrix.template.md)
- [Implementation readiness](./implementation-readiness.template.md)

## Table of contents

- [Snapshot](#snapshot)
- [Architecture progress (system to containers to components)](#architecture-progress-system-to-containers-to-components)
- [Maturity guide](#maturity-guide)
- [MVP slices and priorities](#mvp-slices-and-priorities)
- [Active TODO](#active-todo)
- [Pending approvals](#pending-approvals)
- [Re-review triggers](#re-review-triggers)
- [Parking lot](#parking-lot)
- [Done recently](#done-recently)

## Snapshot

Use the lifecycle and task statuses in `.blueprint/instructions/standards/status-taxonomy.md`.

| Area | Status | Coverage | Notes | Next action |
| --- | --- | --- | --- | --- |
| Product | Not started | | | |
| MVP and prioritization | Not started | | | |
| Requirements | Not started | | | |
| Tech | Not started | | | |
| Design | Not started | | | |
| Delivery governance | Not started | | | |
| C4 system | Not started | | | |
| C4 containers | Not started | | | |
| C4 components | Not started | | | |
| Traceability | Not started | | | |
| Technical design and walking skeleton | Not started | | | |
| Delivery foundation | Not started | | | |
| Implementation readiness | Not started | | | |
| Full development | Not started | | | |
| Integrated verification | Not started | | | |

## Architecture progress (system to containers to components)

- System: [System](../../../design/c4/system/system.md) — `Not started`
- Container overview: [System containers](../../../design/c4/containers/system-containers.md) — `Not started`

### Container maturity matrix

Add one row per approved container after design approval. Use `N/A` only for capabilities outside that container's scope.

| Container | Container design | Components design | Interfaces diagram | Contracts and test seams | Walking skeleton | Delivery path | Readiness | Full development | Integrated verification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### Component depth matrix

| Container | Components total | Components with contracts | Components with test seams | Walking skeleton evidence | Component docs |
| --- | --- | --- | --- | --- | --- |

## Maturity guide

- `Container design` and `Components design` reflect approved C4 boundaries and scoped technical design.
- `Interfaces diagram` records an approved Draw.io source and sibling SVG for boundary relationships when the container has relevant interfaces.
- `Contracts and test seams` records executable interfaces and initial tests inside the approved container.
- `Walking skeleton` and `Delivery path` record the minimal build, packaging, and non-production evidence needed for readiness.
- `Readiness` records the scoped approval decision; `Full development` and `Integrated verification` follow that gate.
- Keep each row no stronger than its prerequisite gate. Put compact evidence or a linked detail in `Notes`.

## MVP slices and priorities

Keep hypothesis, scope, and rationale in [MVP and prioritization](./mvp.template.md). Summarize only current execution and feedback here.

| Slice ID | Slice name | Priority | Status | Requirements | Key tasks | Feedback / evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Active TODO

Use stable `TASK-*` IDs. Include status, owner, bounded scope, linked evidence, and the next owner or decision. Add priority and MVP slice for work that contributes to a prioritized slice.

Format each item as `TASK-001` (`Not started`, priority, MVP slice) followed by an action, owning role, evidence link, and next decision. Omit priority or slice only when genuinely inapplicable.

## Pending approvals

| Gate or phase | Scope | Requested decision | Evidence | Decision owner | Status |
| --- | --- | --- | --- | --- | --- |

## Re-review triggers

## Parking lot

## Done recently
