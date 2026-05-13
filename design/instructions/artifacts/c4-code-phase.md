# C4 Artifact: component code-design phase

## Purpose

Control code-level C4 design through explicit two-phase approvals per container using Design by Contract.

## Phases

- Phase 1: Design by Contract
  - define provided/consumed interfaces
  - define method signatures
  - define required request/response objects
  - define preconditions, postconditions, invariants, and failure semantics
  - keep class internals abstract
- Phase 2: internal implementation
  - define architecture-level classes/modules that realize approved contracts
  - define internal flows and extension points at architecture level
  - add domain model and persistence structure views where relevant
  - do not implement runtime internals in this phase

## Authoring rules

- Do not start Phase 2 before Phase 1 approval.
- Treat C4 code phases as architecture track artifacts independent from runtime implementation.
- Runtime implementation starts only after C4 code phase 2 is explicitly approved.
- If implementation design changes contracts or architecture boundaries, update C4 artifacts first and re-approve before continuing.
- Follow `design/instructions/standards/design-by-contract.md`.
- For relational persistence, model owned schema with ER-style diagrams.
- For file/object storage, model folder/namespace structures and access paths.

## Quality checklist

- Phase boundaries are explicit.
- Contract and implementation artifacts remain aligned.
- Contracts can be consumed from the artifact without hidden operation names or undocumented payload shapes.
- Contract obligations are explicit enough to drive tests.
- Persistence structures reflect ownership boundaries.
