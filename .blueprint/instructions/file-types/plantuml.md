# PlantUML Files

## Rules

- Use PlantUML as the committed source format for architecture and design diagrams unless `design/foundation/tech.md` records another approved choice.
- Commit `.puml` source and publish rendered output as a CI artifact by default.
- Keep source beside the enduring artifact it supports.
- Use one concern per diagram and split views before readability degrades.
- Keep titles, identifiers, names, and domain vocabulary aligned with narrative artifacts.
- Make direction and boundary semantics explicit.
- Keep human-authored architecture diagrams separate from generated code-structure diagrams.
- Never edit generated code-diagram sources manually; update source metadata or generator configuration and regenerate.
- Validate syntax, links, and rendering in CI.
