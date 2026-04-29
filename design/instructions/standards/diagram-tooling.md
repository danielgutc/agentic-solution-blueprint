# Diagram Tooling Standard

## Source of truth

- Keep editable diagram source files as `.drawio`.
- Keep rendered `.svg` files beside source.

## Update rule

- When a `.drawio` file changes, regenerate the sibling `.svg`.
- Do not treat manual SVG edits as the primary update path.

## Verification checklist

- Confirm SVG changed (timestamp/hash/content).
- Confirm expected links are present in exported SVG when navigation is required.
