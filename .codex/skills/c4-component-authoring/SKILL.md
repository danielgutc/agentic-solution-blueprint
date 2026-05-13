---
name: c4-component-authoring
description: Author or revise component-level C4 artifacts for a container, including component responsibilities, interfaces, collaboration, and code-phase gates. Use when working on container component decomposition.
---

# C4 Component Authoring Skill

Use this skill when creating or revising component-level C4 artifacts in a container.

## Trigger conditions

- The task targets `design/c4/containers/<container>/components/<component>/component.md`.
- The task defines provided/required interfaces or internal component collaboration.

## Prechecks

- Apply shared prechecks from `.blueprint/instructions/process/c4-authoring-playbook.md`.
- Confirm targeted container contracts are stable enough for decomposition.

## Workflow

1. Apply `.blueprint/instructions/artifacts/c4-component.md`.
2. Apply `.blueprint/instructions/standards/design-by-contract.md` to component APIs and handoffs.
3. Use `.blueprint/templates/c4/component.template.md`.
4. Model one external facade boundary per microservice by default.
5. Model internal APIs among orchestration, integration, and persistence components.
6. Use code-phase gating from `.blueprint/instructions/artifacts/c4-code-phase.md`.

## Failure handling

- Apply shared escalation rules from `.blueprint/instructions/process/c4-authoring-playbook.md`.
- If component changes require container contract changes, return to container level first.
- If storage/API notation is inconsistent with siblings, align diagrams in the same pass.

## Validation checklist

- Apply shared validation baseline from `.blueprint/instructions/process/c4-authoring-playbook.md`.
- Provider/consumer dependency direction is correct.
- Component API obligations are explicit and testable.
- Storage access is modeled directly to data-store nodes.
- Project-built vs third-party ownership is explicit.
