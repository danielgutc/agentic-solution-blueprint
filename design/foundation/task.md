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

Use stable `TASK-*` IDs. Include status, owner, bounded scope, linked evidence, and the next owner or decision. Add priority and MVP slice for work that contributes to a prioritized slice.

Format each item as `TASK-001` (`Not started`, priority, MVP slice) followed by an action, owning role, evidence link, and next decision. Omit priority or slice only when genuinely inapplicable.

- **TASK-001** (`Verified`, reusable blueprint maintenance) — The developer approved [API documentation model Option C](api-documentation-model-review.md) on 2026-10-26. Policy, templates, registry, tooling, tests, and portable fixtures implement canonical implementation-unit/profile API pages plus container, optional component, and source-bound interface views. The full portable suite passed 22 tests; independent review also passed the 17 renderer/navigation tests and provider-scope probe. Navigation and whitespace checks pass. `selected_workflow` remains unset and seeded lifecycle rows remain unchanged. Changes are prepared for pull request review on `codex/canonical-docs-mvp-v1`; publication and consuming-project adoption evidence are recorded separately. No runtime-container change is approved.

- **TASK-002** (`Verified`, reusable MVP version 1.0 policy) — On 2026-10-28 the developer required MVPs to use their final intended technical architecture, represent the first production-quality version 1.0, support later approved capabilities without a prerequisite corrective rewrite, and remain distinct from shortcut-tolerant PoCs. The [canonical policy](../../.blueprint/instructions/standards/mvp-quality.md) is routed through foundation/lifecycle/design/implementation/approval instructions and MVP/readiness templates; the seeded MVP artifact is aligned. Routine maintenance refactoring and reviewed evolution for new evidence remain valid; future features are not prebuilt. This is reusable governance maintenance, not a new product lifecycle approval. Independent documentation review passed. Navigation/contents checks passed for all 18 seeded design documents and nine changed policy/template files; policy synchronization and whitespace checks passed. The engineering toolkit now applies the same baseline in both coordinator files, all six canonical roles and generated Copilot profiles, and seven lifecycle skills. Its complete validation suite and seven standalone skill checks pass. Independent semantic review passed four explicitly synthetic reasoning cases: temporary authoritative storage, normal TDD refactoring, extension without future-feature overbuild, and shared-solution ownership. Blueprint navigation and all eleven touched reusable instruction/template pages pass; the consuming solution has refreshed its 42-file policy overlay and 28-file portable-bundle digest. Changes are prepared for pull request review on `codex/canonical-docs-mvp-v1`; the consuming solution records the exact source revision and its version 1.0 compliance-review need.

## Pending approvals

| Gate or phase | Scope | Requested decision | Evidence | Decision owner | Status |
| --- | --- | --- | --- | --- | --- |
| Documentation model maintenance | Canonical source API reference and C4 navigation | Option C approved for reusable blueprint policy, templates, registry, and tooling; consuming-project migration remains separately gated | [Model review](api-documentation-model-review.md) | Developer, advised by technical architect | Approved 2026-10-26 |

## Re-review triggers

## Parking lot

## Done recently

- 2026-10-26 — Approved Option C for the reusable API documentation publication model. The approval preserves existing C4/runtime boundaries and leaves repository-intelligence APP boundary review open.
