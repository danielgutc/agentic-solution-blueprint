# Markdown Files

## Rules

- Keep each file focused on one artifact or concern.
- Prefer short, scannable sections and explicit decisions.
- Use relative paths for repository links.
- In foundation artifacts, include a README breadcrumb, links to related foundation files, and a table of contents for second-level sections.
- Keep examples next to the rule or decision they clarify.
- Avoid repeating policy that belongs in `.blueprint/instructions/`.
- Never edit generated `code.md` manually.
- Begin generated Markdown with a warning, source scope, generator identity, and reproduction command.
- Keep tables narrow enough to review in source; use linked detail when a cell becomes a document.
- Validate links and generated-file freshness in CI.
