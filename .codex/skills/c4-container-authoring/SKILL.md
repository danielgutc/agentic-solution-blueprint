# C4 Container Authoring Skill

Use this skill when creating or revising container-level C4 artifacts.

## Trigger conditions

- The task targets `design/c4/containers/system-containers.md` or `container.md` files.
- The task defines container boundaries, contracts, or service decomposition.

## Prechecks

- Apply shared prechecks from `design/instructions/process/c4-authoring-playbook.md`.
- Confirm the task is at container level, not system or component level.

## Workflow

1. Apply:
   - `design/instructions/artifacts/c4-system-containers.md`
   - `design/instructions/artifacts/c4-container.md`
2. Use:
   - `design/templates/c4/system-containers.template.md`
   - `design/templates/c4/container.template.md`
3. Decompose by bounded contexts and explicit contracts.
4. Record protocol/payload style for container interactions when known.
5. Keep decomposition tree current and navigable.

## Failure handling

- Apply shared escalation rules from `design/instructions/process/c4-authoring-playbook.md`.

## Validation checklist

- Apply shared validation baseline from `design/instructions/process/c4-authoring-playbook.md`.
- Container boundaries are coherent.
- Schema/namespace/folder ownership is explicit.
- Data stores are modeled as data-store containers.
