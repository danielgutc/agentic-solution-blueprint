# Task Tracker

[README](../../README.md) / Foundation / Task tracker

Related foundation documents:
- [Product](./product.md)
- [MVP and prioritization](./mvp.md)
- [Requirements](./requirements.md)
- [Tech](./tech.md)
- [Design](./design.md)
- [Delivery governance](./delivery.md)
- [Traceability matrix](./traceability-matrix.md)
- [Implementation readiness](./implementation-readiness.md)

## Table of contents

- [Snapshot](#snapshot)
- [Architecture progress (system to containers to components)](#architecture-progress-system-to-containers-to-components)
- [Maturity guide](#maturity-guide)
- [MVP slices and priorities](#mvp-slices-and-priorities)
- [Active TODO](#active-todo)
- [Current approvals](#current-approvals)
- [Re-review triggers](#re-review-triggers)

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

- System: [System](../c4/system/system.md) — `Not started`
- Container overview: [System containers](../c4/containers/system-containers.md) — `Not started`

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

Keep hypothesis, scope, and rationale in [MVP and prioritization](./mvp.md). Summarize only current execution and feedback here.

| Slice ID | Slice name | Priority | Status | Requirements | Key tasks | Feedback / evidence | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Active TODO

No active implementation work is assigned in this reusable blueprint. Consuming projects populate their own scoped tasks and approvals.

## Current approvals

| Decision | Scope and authority | Conditions |
| --- | --- | --- |
| API publication model Option C | Developer approved reusable policy, templates, registry, and tooling on 2026-10-26; see [API documentation policy](../../.blueprint/instructions/file-types/api-documentation.md). | Consuming-project migration remains separately gated. This approval does not approve runtime boundary changes. |
| MVP rationale ownership | Developer authorized refactoring on 2026-10-28; see [MVP quality policy](../../.blueprint/instructions/standards/mvp-quality.md). Product owns outcomes, scope, and acceptance rationale; solution architecture owns boundaries and roadmap tradeoffs; technical architecture owns internal realization. | No product or runtime-boundary change is authorized by this maintenance decision. |

## Re-review triggers

Reassess a relied-on maintenance decision when its scope or governing policy changes. Consuming projects must establish their own lifecycle approvals before advancing project work.
