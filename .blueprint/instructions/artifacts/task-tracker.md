# Task Tracker Artifact

## Purpose

Use `design/foundation/task.md` as a compact lifecycle dashboard and multi-agent handoff surface, not as a second requirements system.

## Canonical shape

Use `.blueprint/templates/foundation/task.template.md`.

## Rules

- Track phase status by explicit scope.
- Summarize MVP slices by ID, priority, status, linked requirements, and next feedback decision; keep the hypothesis and scope in `mvp.md`.
- Link evidence rather than copying artifact content.
- Give each active slice a stable ID, one owning role, expected output, next owner, and stopping condition.
- Record approvals and re-review needs durably.
- Keep completed detail brief; Git history remains the full change log.
- Move speculative or unapproved ideas to the parking lot.
- Update the tracker at handoff boundaries so the next agent does not repeat repository discovery.

## Quality checks

- Status agrees with prerequisite gates.
- Active work is bounded and owned.
- Evidence and blockers are actionable.
- The next decision and owner are obvious.
