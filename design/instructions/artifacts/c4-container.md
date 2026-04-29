# C4 Artifact: containers/<container>/container.md

## Purpose

Describe one runtime container or data-store container as a black box.

## Canonical structure

- Use `design/templates/c4/container.template.md`.

## Authoring rules

- State container type explicitly (service, application, relational store, file/object store, broker).
- Keep responsibilities, boundaries, and contracts explicit.
- For service containers, document owned schemas/namespaces and integration boundaries.
- For data-store containers, prefer internal storage structure over application-style decomposition.
- Record container-specific architecture decisions and split triggers when deviations exist.

## Quality checklist

- Container scope is coherent and non-overlapping.
- Inbound/outbound contracts are clear.
- Persistence ownership is explicit.
