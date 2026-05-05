---
name: diagram-export-verify
description: Regenerate and validate diagram exports and navigation links for Draw.io sources. Use when .drawio files change or diagram export, SVG, or navigation issues are reported.
---

# Diagram Export Verify Skill

Use this skill when diagram source files are changed and exports/navigation must be validated.

## Trigger conditions

- A `.drawio` file changed.
- A diagram-link or navigation issue is reported.

## Prechecks

- Identify changed diagram sources and expected sibling `.svg` outputs.
- Confirm target links expected inside exported SVG.

## Workflow

1. Regenerate `.svg` for each changed `.drawio`.
2. Verify export changed (timestamp/hash/content).
3. Verify required links exist in exported SVG when navigation is needed.
4. Verify embedded Markdown references point to current SVG paths.

## Failure handling

- If exported SVG misses links present in source, treat export as failed and regenerate/fix.
- If rendering tooling is unavailable, report exact missing dependency and stop before merge.

## Validation checklist

- Source and export pairs are aligned.
- Link targets resolve to intended diagram destinations.
- No stale absolute-path links remain.
