# Task Tracker Artifact

## Purpose

Use `design/foundation/task.md` as a glanceable lifecycle, architecture-maturity, MVP, and handoff dashboard. Keep requirement definitions in their owning artifacts and record compact evidence according to [verification evidence](../standards/verification-evidence.md).

## Canonical shape

Use `.blueprint/templates/foundation/task.template.md`.

## Required shape

Use these sections in order where applicable: `Snapshot`, `Architecture progress (system to containers to components)`, `Maturity guide`, `MVP slices and priorities`, `Active TODO`, `Approvals`, `Re-review triggers`, and `Parking lot`. Omit empty sections and unnecessary explanatory boilerplate. Include a README breadcrumb, relevant existing foundation links, and proportionate navigation under [navigation](../standards/navigation.md).

- `Snapshot` uses `Area | Status | Coverage | Notes | Next action`; name the current scope and summarize or link its evidence.
- `Architecture progress` links the system and container overview, then uses the container maturity and component depth matrices in the canonical template. The maturity matrix includes interface-diagram evidence. Add container rows only after the design gate approves those boundaries.
- `Maturity guide` explains the matrix columns using this blueprint's technical-design, walking-skeleton, delivery, readiness, development, and verification phases. Do not introduce the war game's separate code-phase model by copying its tracker verbatim.
- `MVP slices and priorities` uses `Slice ID | Slice name | Priority | Status | Requirements | Key tasks | Feedback / evidence | Notes`. Keep the hypothesis and scope in `mvp.md` and requirement-level priority, target, and status in `requirements.md`.
- `Active TODO` uses stable `TASK-*` IDs with status in parentheses, owner, bounded scope, expected evidence, and next owner or decision. Add priority and MVP slice in those parentheses when applicable.
- `Approvals` records pending decisions and approvals still relied on: scope, requested or granted decision, evidence references, decision owner, decision date or source, conditions, and status. Keep explicit approvals and re-review triggers durable.

Update current entries rather than copying long artifact content or creating separate reports. Remove completed work from Active TODO once its enduring result and any relied-on approval are recorded in their owning artifacts; do not keep a Done recently section or completed-task diary. Keep only relevant unresolved ideas in the parking lot. Update the tracker when scope, blockers, ownership, or gate decisions change; a handoff does not require a new document or history entry.

## Quality checks

- Status agrees with `.blueprint/instructions/standards/status-taxonomy.md` and prerequisite gates; `N/A` is for an inapplicable matrix capability, not an approval status.
- A container cannot show later work as approved when its design, contracts, or readiness gate is weaker for the same scope.
- Active work is bounded and owned.
- Evidence and blockers are actionable.
- The next decision and owner are obvious.
