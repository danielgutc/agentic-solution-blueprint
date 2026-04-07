# War Game

This repository uses a spec-driven workflow:

1. Update shared guidance in `.design/foundation/` and `.design/c4/` when project-wide rules change.
2. Create or update a feature spec in `.design/specs/<feature>/`.
3. Move from `requirements.md` to `design.md` to `tasks.md`.
4. Start implementation only after the task list is clear enough to execute.

Repository layout:

- `.codex/` contains Codex-specific context only.
- `.design/` contains the reusable project blueprint: foundation, C4 architecture, instructions, and specs.
- `tools/` contains repo-local utilities and automation scripts.
- `tests/` contains cross-component integration and end-to-end tests.
