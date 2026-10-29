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

- **TASK-003** (`Implemented`, reusable MVP rationale ownership refactoring) - On 2026-10-28 the developer corrected TASK-002's placement and explicitly authorized this refactoring. Product owns the MVP outcome, scope, quality, and acceptance rationale; solution architecture owns boundary justification and known-roadmap tradeoffs; technical architecture owns internal realization and supporting evidence. The [quality guidance](../../.blueprint/instructions/standards/mvp-quality.md), foundation/C4 instructions, lifecycle handoffs, templates, and seeded artifacts now place rationale at those owners. The toolkit removes the blanket MVP baseline from global Codex/Copilot instructions and downstream roles/skills; the three owning roles and their skills require project-artifact rationale. Copilot profiles were regenerated. TASK-002 remains historical evidence of the earlier implementation; its cross-role global policy placement is superseded by this correction. No consuming-project migration or new product/architecture lifecycle approval is claimed. Validation: seeded navigation and changed Markdown checks, template/seed alignment, policy placement checks, and whitespace checks pass. Eight toolkit validation checks pass; aggregate validation stops on pre-existing software/test model and reasoning assertions (committed Qwen/high versus validator Terra/Luna/medium). Specialist consultation was unavailable because its configured model could not be loaded; no independent review pass is claimed. Installed global coordinators already omit the blanket policy; their unrelated differences and older installed role/skill copies are preserved. Next owner: developer reviews the maintenance diff; toolkit configuration validation and any installation refresh remain separate follow-through.

## Pending approvals

| Gate or phase | Scope | Requested decision | Evidence | Decision owner | Status |
| --- | --- | --- | --- | --- | --- |
| Documentation model maintenance | Canonical source API reference and C4 navigation | Option C approved for reusable blueprint policy, templates, registry, and tooling; consuming-project migration remains separately gated | [Model review](api-documentation-model-review.md) | Developer, advised by technical architect | Approved 2026-10-26 |
| MVP rationale ownership maintenance | Product, solution architecture, and technical architecture artifacts plus toolkit instruction cleanup | Refactoring authorized in this chat; no product or runtime-boundary change | TASK-003 and linked guidance | Developer | Approved 2026-10-28 |

## Re-review triggers

## Parking lot

## Done recently

- 2026-10-26 — Approved Option C for the reusable API documentation publication model. The approval preserves existing C4/runtime boundaries and leaves repository-intelligence APP boundary review open.

## 2026-10-29 native diagram freshness maintenance

A consuming project exposed a check-only defect: native Draw.io exports with styles outside the portable subset were rendered before their embedded model could be validated. The reusable checker now verifies canonical source and link anchors independently of portable rendering. Export still rejects unsupported styles, stale and missing-link exports fail, and check mode never rewrites drawings. Two regression cases first reproduced the failure; seven portable tests and seven project-specific tests pass in the consuming repository, including all six real diagram pairs. The checker, portable tests and usage guide are mirrored here from that authorized reusable-tool maintenance. Local changes await review/commit; no upstream publication or pin advancement is claimed.
