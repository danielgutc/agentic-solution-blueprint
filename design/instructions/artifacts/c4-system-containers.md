# C4 Artifact: containers/system-containers.md

## Purpose

Define container boundaries and contracts at the next abstraction level below system.

## Canonical structure

- Use `design/templates/c4/system-containers.template.md`.

## Authoring rules

- Keep each container as a black box with explicit responsibilities and boundaries.
- Record key protocols/transports and payload styles for container interactions when known.
- Keep a tree-style decomposition section at the end:
  - `system -> containers -> designed children`
- Show persistence ownership per service boundary in the decomposition view.
- Keep data-store entries structural (schema/namespace/folder), not service-style component lists.

## Quality checklist

- Container boundaries align with bounded contexts.
- Contracts are concrete enough for component decomposition.
- Decomposition tree is navigable and current.
