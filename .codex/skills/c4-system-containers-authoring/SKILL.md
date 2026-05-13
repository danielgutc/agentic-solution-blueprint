# C4 System Containers Authoring Skill

Use this skill when creating or revising the system-containers C4 artifact.

## Trigger conditions

- The task targets `design/c4/containers/system-containers.md`.
- The task defines container inventory, boundaries, contracts, or top-level interactions.

## Prechecks

- Apply shared prechecks from `.blueprint/instructions/process/c4-authoring-playbook.md`.
- Confirm the task is at system-containers level, not single-container or component level.

## Workflow

1. Apply `.blueprint/instructions/artifacts/c4-system-containers.md`.
2. Apply `.blueprint/instructions/standards/design-by-contract.md` to container interactions.
3. Use `.blueprint/templates/c4/system-containers.template.md`.
4. Decompose by bounded contexts and explicit contracts.
5. Record protocol/payload style for container interactions when known.
6. Keep decomposition tree current and navigable.

## Failure handling

- Apply shared escalation rules from `.blueprint/instructions/process/c4-authoring-playbook.md`.
- If the request drills into one container internals, hand off to `c4-container-authoring`.

## Validation checklist

- Apply shared validation baseline from `.blueprint/instructions/process/c4-authoring-playbook.md`.
- Container inventory and boundaries are coherent.
- System-level container contracts expose provider/consumer obligations.
- Persistence ownership is represented at container boundary level.
