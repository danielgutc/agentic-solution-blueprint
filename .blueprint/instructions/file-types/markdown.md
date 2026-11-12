# Markdown Files

## Rules

- Keep each file focused on one artifact or concern.
- Prefer short, scannable sections and explicit decisions.
- Apply the pre-authoring decision in [documentation and verification evidence](../standards/verification-evidence.md): choose the canonical existing owner and update it in place. Do not create a page per task, phase, or handoff, or standalone acceptance/assessment/evidence documents by default. Additional enduring pages require a `documentation.additional_authored_documents` registry entry with `path`, `owner`, `reason`, and `review_trigger`; a named user report request applies only to that scope.
- Use relative paths for repository links.
- Follow [navigation](../standards/navigation.md) for foundation and C4 breadcrumbs, related links, contents lists, and drill-down links.
- Omit unnecessary contents lists and empty template sections on short pages under that standard; keep existing links and any supplied contents list valid.
- Keep examples next to the rule or decision they clarify.
- Avoid repeating policy that belongs in `.blueprint/instructions/`.
- Never edit generated canonical API pages, C4 code views, compatibility stubs, or code-diagram sources manually.
- Begin generated Markdown with a warning, implementation unit and documentation profile, relevant architecture bindings, included and excluded source/language/visibility scope, generator identity and pinned version, parser limits, provenance, and reproduction command.
- Give canonical API pages backlinks to every configured container, component, and interface view; link them to their source declarations and parent unit/profile index. Architecture views link to canonical pages rather than copying symbol content.
- Keep tables narrow enough to review in source; move long detail into a section of the canonical owner, or link existing detail. A large cell does not justify an additional document without the registry exception.
- Validate links and generated-file freshness in CI.
