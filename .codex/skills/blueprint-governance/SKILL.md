---
name: blueprint-governance
description: Refactor and maintain reusable blueprint governance artifacts, including AGENTS.md, design instructions, templates, samples, and project skills. Use when evolving blueprint-level rules or keeping governance artifacts aligned.
---

# Blueprint Governance Skill

Use this skill when the task is to evolve the reusable blueprint rather than only solve a solution-specific design problem.

## Goals

- Keep `AGENTS.md` concise and stable.
- Move detailed schemas into modular instruction files.
- Keep templates and samples solution-agnostic.
- Preserve approval-gated workflow and C4 abstraction discipline.

## Workflow

1. Identify whether the requested change is inside blueprint-governance scope using `design/instructions/process/blueprint-sync.md`.
2. Apply changes in the smallest coherent package.
3. Validate consistency:
   - instruction precedence is clear
   - template and sample structure matches artifact rules
   - no contradictory duplicate rule across files
4. For C4-specific behavior changes, update level-specific C4 skills.
5. For upstreamable changes, run blueprint sync via `.codex/skills/blueprint-sync-pr/SKILL.md`.

## Output checklist

- Updated modular instruction files when rules change.
- Updated template files when target structure changes.
- Updated sample files when expected quality level changes.
- Brief reviewer notes explaining what moved out of `AGENTS.md`.
