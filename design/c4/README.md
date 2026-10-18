# C4 Architecture

This folder contains the canonical architecture description for the project created from this blueprint.

## Layout

- `system/` contains the software system view.
- `containers/system-containers.md` contains the authoritative container landscape.
- `containers/` contains one folder per approved container in the system.
- Each container owns its components under `components/`.
- Container-specific technical documents live beside their owning `container.md`; component-specific documents live beside their owning `component.md`. Scope and ownership determine placement; see the [C4 artifact conventions](../../.blueprint/instructions/artifacts/c4.md).

## Documentation model

- Human-authored Markdown and Draw.io diagrams with sibling SVG exports describe system, container, and component intent.
- Source interfaces, API comments, and executable tests define code contracts.
- The documentation toolchain uses Doxygen by default after language capability fixtures pass, then renders committed component guides, per-symbol Markdown API pages, and code-diagram sources from Doxygen XML and native source documentation.
- Optional aggregate API sites are CI artifacts; navigable generated Markdown and human-authored SVG diagrams remain available from a fresh clone.
- Each implemented `component.md` links its generated `code.md`; generated guides and API pages link back to the owning component and source declarations. Components without repository-owned implementation do not link placeholders.

## Folder shape

```text
c4/
  README.md
  system/
    system.md
    _diagrams/
  containers/
    README.md
    system-containers.md
    _diagrams/
    <container>/
      container.md
      <document>.md     # optional container-owned technical detail
      _diagrams/
      components/
        <component>/
          component.md
          <document>.md # optional component-owned technical detail
          _diagrams/
          code.md          # generated
          api/             # generated committed Markdown by scope and stable symbol ID
          _code-diagrams/  # generated sources
```
