# Diagram Tooling Standard

## Source and export

- Use editable `.drawio` files as the default source for human-authored foundation and C4 diagrams.
- Commit a sibling `.svg` export for every diagram referenced by Markdown. Embed the SVG in the owning document and link its Draw.io source nearby.
- Keep diagram pairs in the owning artifact's `_diagrams/` directory. Do not add an empty or speculative diagram merely to fill a template.
- When a project explicitly approves a different source format in `design/foundation/tech.md`, record its export and navigation rules there before authoring diagrams.

## Update and verification

- Regenerate the SVG from the `.drawio` source after every source change; do not edit the SVG as the primary source.
- A project may use the Draw.io CLI, for example `drawio --export --format svg --svg-links-target same-win --output view.svg view.drawio`, or a documented editor export. Use the command selected in `tech.md` so another contributor can reproduce the result.
- Check that the SVG represents the current source and that Markdown references resolve to both files.
- When source cells contain drill-down links, verify those links survive export and resolve to existing diagrams. A visually correct SVG with missing required links is not a valid export.
- Record the project-selected Draw.io export command and validation command in `design/foundation/tech.md` and run them in the documentation quality gate.

## Navigation

- Link diagram nodes to the next diagram level only when the target exists.
- Keep textual breadcrumbs and section links in Markdown; diagram links serve visual drill-down.
