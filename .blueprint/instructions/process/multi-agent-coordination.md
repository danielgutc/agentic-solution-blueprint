# Multi-Agent Coordination

## Ownership

Use the role boundaries in `AGENTS.md`. Delegate a bounded outcome, not an open-ended phase, and keep one owner for each enduring decision.

## Delegation packet

Provide only the context needed for the task:

- scope and stable identifiers
- owning role and expected next owner
- approved inputs and constraints
- exact output or evidence expected
- decisions that are fixed versus open
- relevant files and commands
- stopping condition and escalation boundary

Do not ask another agent to rediscover the whole repository when the task tracker or a focused handoff can provide the answer.

## Handoff packet

Record:

- completed scope and changed identifiers
- decisions and evidence
- commands or checks run
- unresolved risks or accepted exceptions
- downstream artifacts that may need re-review
- next owner and requested decision

Update `design/foundation/task.md` before handing off. Keep transient reasoning out of enduring artifacts.

## Parallel work

- Parallelize only when boundaries, inputs, and merge points are stable.
- Product and solution decisions remain serialized when one changes the other's assumptions.
- Technical architecture and delivery foundation may proceed in parallel after container boundaries and toolchain choices stabilize, using the same walking skeleton.
- Software implementation and independent integrated-test design may proceed in parallel after contracts and acceptance intent stabilize.
- Reconcile conflicting evidence at the owning abstraction before continuing downstream.
