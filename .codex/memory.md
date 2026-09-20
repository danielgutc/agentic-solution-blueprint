# Working Memory

Use this file only for short-lived notes that help Codex stay consistent across sessions. Promote durable rules into `AGENTS.md` or `.blueprint/instructions/`.

Current stable notes:

- This repository is a reusable, business-agnostic project blueprint.
- `.blueprint/blueprint.toml` declares version `2.0` and records structural, coordination, documentation, and gate policy.
- `AGENTS.md` is the concise always-on entry point; detailed rules load from `.blueprint/instructions/` only when relevant.
- Canonical artifact shapes live in `.blueprint/templates/`; seeded project artifacts live in `design/`.
- `design/foundation/` includes product, requirements, technology, design, delivery, coordination, traceability, and implementation-readiness artifacts.
- In the C4 structure, components live under their owning container.
- Project-specific skills live in `.agents/skills/`; reusable agents and skills come from the external engineering toolkit.
- Real built components belong under `implementation/`.
- Human-authored C4 ends at component intent; `code.md` and code-diagram sources are generated from source, API comments, and tests.
- Full development starts only after the implementation-readiness gate proves the walking skeleton and minimum delivery pipeline.
- The latest released reusable baseline is tagged `blueprint-1.6`.
- Version 2 work is developed on `main_v2`.
