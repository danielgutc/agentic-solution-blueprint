---
name: c4-container-authoring
description: Author or revise a single-container C4 artifact, including responsibilities, boundaries, contracts, dependencies, and persistence ownership. Use when working on one container's architecture.
---

# C4 Container Authoring Skill

Use this skill when creating or revising a single container C4 artifact.

## Trigger conditions

- The task targets `design/c4/containers/<container>/container.md`.
- The task defines one container's responsibilities, boundaries, contracts, and dependencies.

## Prechecks

- Apply shared prechecks from `.blueprint/instructions/process/c4-authoring-playbook.md`.
- Confirm the task is at single-container level, not system-containers or component level.

## Workflow

1. Apply `.blueprint/instructions/artifacts/c4-container.md`.
2. Apply `.blueprint/instructions/standards/design-by-contract.md` to inbound/outbound contracts.
3. Use `.blueprint/templates/c4/container.template.md`.
4. Decompose by bounded contexts and explicit contracts.
5. Record protocol/payload style for container interactions when known.

## Failure handling

- Apply shared escalation rules from `.blueprint/instructions/process/c4-authoring-playbook.md`.
- If the request is container inventory/overview for the whole system, hand off to `c4-system-containers-authoring`.

## Validation checklist

- Apply shared validation baseline from `.blueprint/instructions/process/c4-authoring-playbook.md`.
- Single-container boundaries are coherent.
- Inbound/outbound contract obligations are explicit.
- Schema/namespace/folder ownership is explicit.
- Data stores are modeled as data-store containers.
