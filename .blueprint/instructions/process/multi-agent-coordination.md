# Multi-Agent Coordination

## Ownership

Use the role boundaries in `AGENTS.md`. Delegate a bounded outcome, not an open-ended phase, and keep one owner for each enduring decision.

## Repository handoff record

Use the fields declared in `.blueprint/blueprint.toml` under `coordination.handoff_fields` for a compact handoff. Link approved inputs and evidence rather than copying entire artifacts or repeating repository discovery.

Before handing off, update `design/foundation/task.md` with the bounded scope, owning and next roles, current gate status, blockers, and any downstream re-review trigger. The role-specific agent instructions govern the detailed handoff content; this file only defines the durable repository record.

## Parallel work

- Parallelize only when boundaries, inputs, and merge points are stable.
- Product and solution decisions remain serialized when one changes the other's assumptions.
- Technical architecture and delivery foundation may proceed in parallel after container boundaries and toolchain choices stabilize, using the same walking skeleton.
- Software implementation and independent integrated-test design may proceed in parallel after contracts and acceptance intent stabilize.
- Reconcile conflicting evidence at the owning abstraction before continuing downstream.
