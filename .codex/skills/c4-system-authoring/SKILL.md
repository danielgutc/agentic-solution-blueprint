---
name: c4-system-authoring
description: Author or revise software-system-level C4 artifacts, including actors, external systems, system boundary, responsibilities, and context diagrams. Use when working at the C4 system level.
---

# C4 System Authoring Skill

Use this skill when creating or revising software-system-level C4 artifacts.

## Trigger conditions

- The task targets `design/c4/system/system.md`.
- The task concerns actors, external systems, boundaries, or responsibilities.

## Prechecks

- Apply shared prechecks from `design/instructions/process/c4-authoring-playbook.md`.
- Confirm the task is at system level, not container or component level.

## Workflow

1. Apply `design/instructions/artifacts/c4-system.md`.
2. Use `design/templates/c4/system.template.md` for section structure.
3. Update system narrative and system context diagram.
4. Ensure clear `Next level` path to system containers.

## Failure handling

- Apply shared escalation rules from `design/instructions/process/c4-authoring-playbook.md`.
- If the request requires system-level container decomposition, hand off to `c4-system-containers-authoring`.

## Validation checklist

- Apply shared validation baseline from `design/instructions/process/c4-authoring-playbook.md`.
- System boundary is explicit.
- Actors/external systems are complete.
- Diagram and narrative align.
