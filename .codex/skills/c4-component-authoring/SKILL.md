# C4 Component Authoring Skill

Use this skill when creating or revising component-level C4 artifacts in a container.

## Trigger conditions

- The task targets `design/c4/containers/<container>/components/<component>/component.md`.
- The task defines provided/required interfaces or internal component collaboration.

## Prechecks

- Apply shared prechecks from `design/instructions/process/c4-authoring-playbook.md`.
- Confirm targeted container contracts are stable enough for decomposition.

## Workflow

1. Apply `design/instructions/artifacts/c4-component.md`.
2. Use `design/templates/c4/component.template.md`.
3. Model one external facade boundary per microservice by default.
4. Model internal APIs among orchestration, integration, and persistence components.
5. Use code-phase gating from `design/instructions/artifacts/c4-code-phase.md`.

## Failure handling

- Apply shared escalation rules from `design/instructions/process/c4-authoring-playbook.md`.
- If component changes require container contract changes, return to container level first.
- If storage/API notation is inconsistent with siblings, align diagrams in the same pass.

## Validation checklist

- Apply shared validation baseline from `design/instructions/process/c4-authoring-playbook.md`.
- Provider/consumer dependency direction is correct.
- Storage access is modeled directly to data-store nodes.
- Project-built vs third-party ownership is explicit.
