# Blueprint Templates

These files define canonical starting shapes for enduring project artifacts.

- Instructions explain why and how to author an artifact.
- Templates define its reusable structure.
- Files under `design/` contain project decisions and evidence.

When a structural convention changes, update the instruction, template, seeded artifact, and `.blueprint/blueprint.toml` path or gate declaration together.

Foundation templates link to sibling `.template.md` files so they are navigable in this repository. When materializing one in `design/foundation/`, change those links to the artifact `.md` names and adjust the README, C4, and diagram links for the destination directory. The seeded foundation files already have project-relative links.
