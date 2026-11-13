# Multi-Agent Coordination

## Ownership

Use the role boundaries in `AGENTS.md`. Delegate a bounded outcome, not an open-ended phase, and keep one owner for each enduring decision.

## Repository handoff record

Use the fields declared in `.blueprint/blueprint.toml` under `coordination.handoff_fields` for a compact handoff. Link approved inputs and evidence rather than copying entire artifacts or repeating repository discovery.

Before handing off, update the current `design/foundation/task.md` summary if bounded scope, owning or next roles, gate status, blockers, or downstream re-review triggers changed. Return conclusions, evidence, limits, and owner actions in the reply; do not create a per-handoff assessment, report, or chronological task entry. The role-specific agent instructions govern detailed handoff content within [documentation and evidence policy](../standards/verification-evidence.md); this file defines only the durable current-state summary.

## Parallel work

- Parallelize only when boundaries, inputs, and merge points are stable.
- Product and solution decisions remain serialized when one changes the other's assumptions.
- Technical architecture and delivery foundation may proceed in parallel after container boundaries and toolchain choices stabilize, using the same walking skeleton.
- Software implementation and independent integrated-test design may proceed in parallel after contracts and acceptance intent stabilize.
- Reconcile conflicting evidence at the owning abstraction before continuing downstream.
