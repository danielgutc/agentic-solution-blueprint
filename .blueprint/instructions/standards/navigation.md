# Navigation Standard

The supplied `python tools/docs/check_navigation.py` command validates repository Markdown links and contents lists. Use its explicit root or input options for another checkout or aggregate reference; see the [tools guide](../../../tools/README.md). Its tests and portable dependencies are listed in the [portable manifest](../../tooling.toml).

## Foundation pages

- Start with a breadcrumb back to the repository README, followed by `Related foundation documents` links to existing sibling artifacts.
- Provide a table of contents linking every second-level section. Keep headings and anchors in sync.
- Link from Design to the C4 system view once that approved view exists.

## C4 pages

- Start with a README and Design breadcrumb, then link the containing C4 level where one exists.
- Provide a table of contents for second-level sections and a next-level link only when the next artifact exists.
- Use `Contained containers` for the system-container landscape and `Contained components` for a container page. Link each row or item to its owned detail page when created.
- Use `Owned technical documents` on container and component pages to link existing scope-owned specifications, assessments, recovery notes, contract designs, test designs, and similar enduring detail. Do not add placeholder links or list documents owned by another C4 scope as local artifacts.
- Use `Code documentation` on an implemented container page to link its generated `code.md`. Add a component `code.md` link only when the optional filtered component view exists; components without a configured view state that no component-specific projection exists instead of linking a placeholder. No component decomposition is required for a container code view.
- Generated container, component, and interface views link to canonical unit/profile API pages. Each canonical page links back to every configured architecture view and to its source declaration. Validate reciprocal links and approved C4 binding IDs with the repository documentation command.
- During migration, old component-local API paths may contain generated moved-notice stubs only. Link new navigation directly to canonical pages; record the stub window in Tech and remove stubs only after the window and clean inbound-link/orphan checks pass.
- Keep the Markdown navigation usable without opening the diagram.

## Diagram navigation

- Prefer diagram-to-diagram links for visual drill-down. Add a target only after its sibling SVG exists.
- Check the exported SVG links against the Draw.io source and resolve every relative destination.
