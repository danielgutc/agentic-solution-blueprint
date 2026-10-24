# Containers

This folder contains the container-level subtree of the C4 architecture.

Use `system-containers.md` and `_diagrams/` for the authoritative system-wide container view. Add one folder per approved container only after that landscape is reviewed.

## Container subtree

- `container.md`
- `<document>.md`: optional container-owned technical detail, such as a walking-skeleton contract, assessment, or recovery design
- `_diagrams/`
- `components/`

## Component subtree

- `component.md`: human-authored component responsibilities, boundaries, and design intent
- `<document>.md`: optional component-owned technical detail, such as a contract assessment or test-seam design
- `_diagrams/`: human-authored Draw.io sources and sibling SVG exports
- `code.md`: generated developer guide and API entry point, linked directly from `component.md`
- `api/`: generated committed per-symbol Markdown reference with architecture, guide, and source backlinks
- `_code-diagrams/`: generated code-structure diagram sources

Create the generated entries only for components with repository-owned implementation. Doxygen is the default parser when the component's implementation language and constructs pass the recorded capability fixtures; project-specific exceptions belong in Foundation Tech.

## Folder shape

```text
containers/
  system-containers.md
  _diagrams/
  <container>/
    container.md
    <document>.md       # optional container-owned detail
    _diagrams/
    components/
      <component>/
        component.md
        <document>.md   # optional component-owned detail
        _diagrams/
        code.md          # generated
        api/             # generated committed Markdown
        _code-diagrams/  # generated sources
```

Documents about several components within one container belong at that container's level. Shared documents spanning containers use an explicitly identified common scope and links from the participating owners. Foundation pages link scoped technical detail from their project-wide decisions, status, traceability, and readiness records.
