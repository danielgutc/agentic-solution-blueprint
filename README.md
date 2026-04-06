# War Game

This repository uses a spec-driven workflow:

1. Update shared guidance in `.codex/steering/` when project-wide rules change.
2. Create or update a feature spec in `.codex/specs/<feature>/`.
3. Move from `requirements.md` to `design.md` to `tasks.md`.
4. Start implementation only after the task list is clear enough to execute.

Repository layout:

- `.codex/` contains Codex-specific context plus the steering and specs that guide the project.
- `client/`, `server/`, `simulation/`, and `shared/` are the main solution components.
- `tools/` contains repo-local utilities and automation scripts.
- `tests/` contains cross-component integration and end-to-end tests.
