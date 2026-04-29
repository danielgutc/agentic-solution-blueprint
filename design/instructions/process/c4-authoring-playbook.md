# C4 Authoring Playbook

Use this playbook as the shared execution baseline for C4 authoring skills.

## Shared prechecks

- Confirm current abstraction gate from `approval-gates.md` is satisfied.
- Confirm the requested change targets one C4 level only (system, containers, or components).
- Confirm supporting foundation design context is aligned for the requested change.

## Shared escalation rules

- If the current gate is not approved, stop and request approval before proceeding.
- If the request crosses multiple abstraction levels, complete and approve the current level first.
- If unresolved design decisions block decomposition, capture them as explicit open questions.

## Shared validation baseline

- Narrative and diagrams are aligned at the target abstraction level.
- Links and references resolve to expected artifacts.
- No lower-level decomposition is added before required approvals.
