# Navigation Standard

The supplied `python tools/docs/check_navigation.py` command validates repository Markdown links, contents lists, and the registered [documentation ownership policy](verification-evidence.md#automated-ownership-check). Explicit input options narrow navigation checks but always enforce ownership across the governed roots. Use its root option for another checkout; see the [tools guide](../../../tools/README.md). Its tests and portable dependencies are listed in the [portable manifest](../../tooling.toml).

## Foundation pages

- Start with a breadcrumb back to the repository README, followed by `Related foundation documents` links to existing sibling artifacts.
- Use a table of contents only when it helps navigation, following the proportionate contents rule below.
- Link from Design to the C4 system view once that approved view exists.

## C4 pages

- Start with a README and Design breadcrumb, then link the containing C4 level where one exists.
- Apply the proportionate contents rule below and add a next-level link only when the next artifact exists.
- Use `Contained containers` for the system-container landscape and `Contained components` for a container page. Link each row or item to its owned detail page when created.
- Use `Owned technical documents` only to navigate existing enduring specifications, contracts, test strategy, or recovery procedures owned at this scope. Choose the canonical container/component artifact before authoring and update it in place. Additional enduring documents require the `documentation.additional_authored_documents` exception with `path`, `owner`, `reason`, and `review_trigger` under [documentation and verification evidence](verification-evidence.md); adding a navigation link does not authorize a document. Do not retain intermediate assessments or execution reports, add placeholder links, or list another C4 scope's documents as local artifacts.
- Use `Code documentation` on an implemented container page to link its generated `code.md`. Add a component `code.md` link only when the optional filtered component view exists; components without a configured view state that no component-specific projection exists instead of linking a placeholder. No component decomposition is required for a container code view.
- Generated container, component, and interface views link to canonical unit/profile API pages. Each canonical page links back to every configured architecture view and to its source declaration. Validate reciprocal links and approved C4 binding IDs with the repository documentation command.
- During migration, old component-local API paths may contain generated moved-notice stubs only. Link new navigation directly to canonical pages; record the stub window in Tech and remove stubs only after the window and clean inbound-link/orphan checks pass.
- Keep the Markdown navigation usable without opening the diagram.

## Proportionate contents

- A table of contents is optional for short pages. Require it on Foundation/C4 detail pages only when they exceed 80 nonblank lines outside fenced examples and contain at least two second-level content sections. README and diagram-support pages remain exempt from the requirement.
- Whenever a contents list is present, link every second-level content section and keep anchors valid. Link and anchor checks apply even when the contents list is omitted.
- Templates provide starting sections and navigation, not a minimum document size. Remove empty/inapplicable sections, redundant related links, and an unnecessary contents list when materializing a small artifact. Keep useful owner/parent breadcrumbs and existing drill-down links.

## Diagram navigation

- Prefer diagram-to-diagram links for visual drill-down. Add a target only after its sibling SVG exists.
- Check the exported SVG links against the Draw.io source and resolve every relative destination.
