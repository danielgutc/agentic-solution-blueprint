# Diagram Tooling Standard

## Source of truth

- Keep editable diagram source files as `.drawio`.
- Keep rendered `.svg` files beside source.

## Update rule

- When a `.drawio` file changes, regenerate the sibling `.svg`.
- Do not treat manual SVG edits as the primary update path.
- Use `.blueprint/tools/diagrams/export-drawio-svg.ps1` when available so generated `.svg` files preserve clickable navigation links from source cells.
- If a project keeps a local wrapper or copy under `tools/diagrams/`, it must preserve the blueprint tool behavior and validation semantics.

## Verification checklist

- Confirm SVG changed (timestamp/hash/content).
- Confirm every source cell link is present in the exported SVG when navigation is required.
- Treat missing exported links as an export failure, even when the diagram renders visually.
