# Markdown Files

## Rules

- Keep each file focused on one artifact or concern.
- Prefer short, scannable sections and explicit decisions.
- Use relative paths for repository links.
- Follow [navigation](../standards/navigation.md) for foundation and C4 breadcrumbs, related links, contents lists, and drill-down links.
- Keep examples next to the rule or decision they clarify.
- Avoid repeating policy that belongs in `.blueprint/instructions/`.
- Never edit generated `code.md`, component `api/` pages, or code-diagram sources manually.
- Begin generated Markdown with a warning, owning architecture scope, source scope, generator identity and pinned version, provenance, and reproduction command.
- Give generated component guides and API pages backlinks to their owning `component.md`; link API pages to their source declarations and parent `code.md`.
- Keep tables narrow enough to review in source; use linked detail when a cell becomes a document.
- Validate links and generated-file freshness in CI.
