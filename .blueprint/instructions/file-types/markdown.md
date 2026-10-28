# Markdown Files

## Rules

- Keep each file focused on one artifact or concern.
- Prefer short, scannable sections and explicit decisions.
- Use relative paths for repository links.
- Follow [navigation](../standards/navigation.md) for foundation and C4 breadcrumbs, related links, contents lists, and drill-down links.
- Keep examples next to the rule or decision they clarify.
- Avoid repeating policy that belongs in `.blueprint/instructions/`.
- Never edit generated canonical API pages, C4 code views, compatibility stubs, or code-diagram sources manually.
- Begin generated Markdown with a warning, implementation unit and documentation profile, relevant architecture bindings, included and excluded source/language/visibility scope, generator identity and pinned version, parser limits, provenance, and reproduction command.
- Give canonical API pages backlinks to every configured container, component, and interface view; link them to their source declarations and parent unit/profile index. Architecture views link to canonical pages rather than copying symbol content.
- Keep tables narrow enough to review in source; use linked detail when a cell becomes a document.
- Validate links and generated-file freshness in CI.
