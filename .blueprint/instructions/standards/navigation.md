# Navigation Standard

## Foundation pages

- Start with a breadcrumb back to the repository README, followed by `Related foundation documents` links to existing sibling artifacts.
- Provide a table of contents linking every second-level section. Keep headings and anchors in sync.
- Link from Design to the C4 system view once that approved view exists.

## C4 pages

- Start with a README and Design breadcrumb, then link the containing C4 level where one exists.
- Provide a table of contents for second-level sections and a next-level link only when the next artifact exists.
- Use `Contained containers` for the system-container landscape and `Contained components` for a container page. Link each row or item to its owned detail page when created.
- Use `Owned technical documents` on container and component pages to link existing scope-owned specifications, assessments, recovery notes, contract designs, test designs, and similar enduring detail. Do not add placeholder links or list documents owned by another C4 scope as local artifacts.
- Keep the Markdown navigation usable without opening the diagram.

## Diagram navigation

- Prefer diagram-to-diagram links for visual drill-down. Add a target only after its sibling SVG exists.
- Check the exported SVG links against the Draw.io source and resolve every relative destination.
