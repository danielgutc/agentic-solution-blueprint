# Blueprint Governance Skill

Use this skill when the task is to evolve the reusable blueprint rather than only solve a solution-specific design problem.

## Goals

- Keep `AGENTS.md` concise and stable.
- Move detailed schemas into modular instruction files.
- Keep templates and samples solution-agnostic.
- Preserve approval-gated workflow and C4 abstraction discipline.

## Workflow

1. Identify whether the requested change is behavioral (`AGENTS.md`) or format/schema (`design/instructions`, `design/templates`, `design/samples`).
2. Apply changes in the smallest coherent package.
3. Validate consistency:
   - instruction precedence is clear
   - template and sample structure matches artifact rules
   - no contradictory duplicate rule across files
4. For upstreamable changes, sync through a branch based on `blueprint/main`.

## Output checklist

- Updated modular instruction files when rules change.
- Updated template files when target structure changes.
- Updated sample files when expected quality level changes.
- Brief reviewer notes explaining what moved out of `AGENTS.md`.
