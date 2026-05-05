# C4 System Containers Authoring Skill

Use this skill when creating or revising the system-containers C4 artifact.

## Trigger conditions

- The task targets `design/c4/containers/system-containers.md`.
- The task defines container inventory, boundaries, contracts, or top-level interactions.

## Prechecks

- Apply shared prechecks from `design/instructions/process/c4-authoring-playbook.md`.
- Confirm the task is at system-containers level, not single-container or component level.

## Workflow

1. Apply `design/instructions/artifacts/c4-system-containers.md`.
2. Use `design/templates/c4/system-containers.template.md`.
3. Decompose by bounded contexts and explicit contracts.
4. Record protocol/payload style for container interactions when known.
5. Keep decomposition tree current and navigable.

## Failure handling

- Apply shared escalation rules from `design/instructions/process/c4-authoring-playbook.md`.
- If the request drills into one container internals, hand off to `c4-container-authoring`.

## Validation checklist

- Apply shared validation baseline from `design/instructions/process/c4-authoring-playbook.md`.
- Container inventory and boundaries are coherent.
- System-level container contracts are explicit.
- Persistence ownership is represented at container boundary level.
