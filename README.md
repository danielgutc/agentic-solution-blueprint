# Project Blueprint

This repository is a reusable blueprint for starting new software projects with:

- shared project guidance under `.design/foundation/`
- enduring architecture under `.design/c4/`
- implementation instructions under `.design/instructions/`
- change planning under `.design/specs/`

## Workflow

1. Define or update the enduring project context in `.design/foundation/` and `.design/c4/`.
2. Create or update a feature spec in `.design/specs/<feature>/`.
3. Move from `requirements.md` to `design.md` to `tasks.md`, or use design-first when architecture leads the work.
4. Start implementation only after the task list is clear enough to execute.

## Top-level layout

- `.codex/` contains Codex-specific context only.
- `.design/` contains the blueprint.
- `tools/` contains repo-local utilities and automation scripts.
- `tests/` contains cross-component integration and end-to-end tests.
