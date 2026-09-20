# Working Memory

Use this file for short-lived notes that help Codex stay consistent across sessions.

Current stable notes:

- This repository is a reusable, business-agnostic project blueprint.
- `.blueprint/blueprint.toml` activates the heavyweight workflow and records structural, documentation, and gate policy.
- The canonical design layout is `design/foundation/`, `design/c4/`, and `design/instructions/`.
- `design/foundation/` is centered on product, requirements, technology, design, traceability, and implementation-readiness artifacts.
- In the C4 structure, components live under their owning container.
- `AGENTS.md` is the single instruction entry point for Codex in this repository.
- Project-specific skills live in `.agents/skills/`; reusable agents and skills come from the external engineering toolkit.
- `design/instructions/markdown.md` is markdown-focused only.
- Real built components belong under `implementation/`.
- Human-authored C4 ends at component intent; `code.md` and code-diagram sources are generated from source, API comments, and tests.
- Full development starts only after the implementation-readiness gate proves the walking skeleton and minimum delivery pipeline.
- The latest released reusable baseline is tagged `blueprint-1.6`.
