# PlantUML Files

## Rules

- Use PlantUML only when `design/foundation/tech.md` explicitly records it as an approved exception to the blueprint's Draw.io default.
- Record the committed source, rendered export, and link-validation policy for that exception before authoring diagrams.
- Keep source beside the enduring artifact it supports.
- Use one concern per diagram and split views before readability degrades.
- Keep titles, identifiers, names, and domain vocabulary aligned with narrative artifacts.
- Make direction and boundary semantics explicit.
- Keep human-authored architecture diagrams separate from generated code-structure diagrams.
- Never edit generated code-diagram sources manually; update source metadata or generator configuration and regenerate.
- Validate syntax, links, and rendering in CI.
