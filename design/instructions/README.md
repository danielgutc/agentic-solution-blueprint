# Instructions

Use this folder as the modular authoring guide for enduring documentation work.

## Precedence

1. `AGENTS.md` is the behavioral source of truth.
2. `process/*.md` defines workflow sequence and approval gates.
3. `artifacts/*.md` defines canonical section schemas and artifact formats.
4. `standards/*.md` defines reusable cross-artifact conventions.
5. `templates/` and `samples/` provide canonical artifact shapes and examples.

If two instructions conflict, prefer the higher item in this precedence list and update lower-level files to remove drift.

## Structure

- `process/`
  - workflow progression models
  - abstraction and approval gates
  - shared C4 authoring playbook
  - blueprint sync process
  - pre-merge refinement workflow
  - AGENTS cleanup candidates
- `artifacts/`
  - artifact-specific rules and quality checklists
  - canonical section-shape routing to templates
- `standards/`
  - status taxonomy
  - naming and navigation conventions
  - diagram tooling conventions

## Authoring rule

Keep `AGENTS.md` concise. Put detailed, repeatable schemas and checklists in modular instruction files and templates.
For C4 architecture work, use the level-specific C4 skills under `.codex/skills/`.
Keep governance policy and normative rules in `design/instructions/`; skills should reference those rules and focus on execution playbooks.
