# C4 Artifact: component code-design phase

## Purpose

Control code-level C4 design through explicit two-phase approvals per container.

## Phases

- Phase 1: contracts first
  - define provided/consumed interfaces
  - define method signatures
  - define required request/response objects
  - keep class internals abstract
- Phase 2: internal implementation
  - define classes/modules implementing approved contracts
  - define internal flows and extension points
  - add domain model and persistence structure views where relevant

## Authoring rules

- Do not start Phase 2 before Phase 1 approval.
- If implementation design changes contracts, return to Phase 1 and re-approve.
- For relational persistence, model owned schema with ER-style diagrams.
- For file/object storage, model folder/namespace structures and access paths.

## Quality checklist

- Phase boundaries are explicit.
- Contract and implementation artifacts remain aligned.
- Persistence structures reflect ownership boundaries.
