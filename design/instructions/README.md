# Instructions

Use this folder as the modular authoring guide for enduring documentation work.

## Precedence

1. `AGENTS.md` is the behavioral source of truth.
2. `process/*.md` defines workflow sequence and approval gates.
3. `artifacts/*.md` defines canonical section schemas and artifact formats.
4. `standards/*.md` defines reusable cross-artifact conventions.
5. `templates/` and `samples/` provide expected output shapes.

If two instructions conflict, prefer the higher item in this precedence list and update lower-level files to remove drift.

## Structure

- `process/`
  - workflow progression models
  - abstraction and approval gates
  - blueprint sync process
  - pre-merge refinement workflow
  - AGENTS cleanup candidates
- `artifacts/`
  - foundation and C4 artifact format rules
  - task tracker schema
- `standards/`
  - status taxonomy
  - naming and navigation conventions
  - diagram tooling conventions

## Authoring rule

Keep `AGENTS.md` concise. Put detailed, repeatable schemas and checklists in modular instruction files and templates.
