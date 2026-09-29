# Task Tracker Artifact

## Purpose

Use `design/foundation/task.md` as a glanceable lifecycle, architecture-maturity, MVP, and handoff dashboard. Keep requirement definitions and detailed evidence in their owning artifacts.

## Canonical shape

Use `.blueprint/templates/foundation/task.template.md`.

## Required shape

Keep these sections in order: `Snapshot`, `Architecture progress (system to containers to components)`, `Maturity guide`, `MVP slices and priorities`, `Active TODO`, `Pending approvals`, `Re-review triggers`, `Parking lot`, and `Done recently`. Include a README breadcrumb, related foundation links, and a table of contents.

- `Snapshot` uses `Area | Status | Coverage | Notes | Next action`; name the current scope and link its evidence.
- `Architecture progress` links the system and container overview, then uses the container maturity and component depth matrices in the canonical template. The maturity matrix includes interface-diagram evidence. Add container rows only after the design gate approves those boundaries.
- `Maturity guide` explains the matrix columns using this blueprint's technical-design, walking-skeleton, delivery, readiness, development, and verification phases. Do not introduce the war game's separate code-phase model by copying its tracker verbatim.
- `MVP slices and priorities` uses `Slice ID | Slice name | Priority | Status | Requirements | Key tasks | Feedback / evidence | Notes`. Keep the hypothesis and scope in `mvp.md` and requirement-level priority, target, and status in `requirements.md`.
- `Active TODO` uses stable `TASK-*` IDs with status in parentheses, owner, bounded scope, expected evidence, and next owner or decision. Add priority and MVP slice in those parentheses when applicable.
- `Pending approvals` records scope, requested decision, linked evidence, decision owner, and status. Keep explicit approvals and re-review triggers durable.

Link evidence rather than copying long artifact content. Keep completed detail brief, and move speculative or unapproved ideas to the parking lot. Update the tracker at handoff boundaries.

## Quality checks

- Status agrees with `.blueprint/instructions/standards/status-taxonomy.md` and prerequisite gates; `N/A` is for an inapplicable matrix capability, not an approval status.
- A container cannot show later work as approved when its design, contracts, or readiness gate is weaker for the same scope.
- Active work is bounded and owned.
- Evidence and blockers are actionable.
- The next decision and owner are obvious.
