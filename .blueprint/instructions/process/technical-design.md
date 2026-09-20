# Technical Design

## Purpose

Refine approved containers into implementation-ready components and prove architecture-significant assumptions without beginning broad feature development.

## Required work

1. Confirm requirement IDs, owning container, design decisions, constraints, and risks.
2. Partition components by cohesive responsibility, domain ownership, change pattern, and dependency direction rather than framework layers alone.
3. Define provided and consumed contracts using `../standards/design-by-contract.md`.
4. Model important flows, state transitions, transactions, concurrency, external calls, and failure recovery.
5. Prefer established, actively maintained libraries and selected platform capabilities when they satisfy the approved needs; justify custom plumbing.
6. Define unit, component, contract, and integration test seams plus the first architecture-significant TDD slices.
7. Create the minimal source interfaces, executable skeleton, and representative tests needed to prove the design.
8. Configure ecosystem-native API documentation and deterministic compact code projections.
9. Escalate any required system, domain, or container-boundary change to the solutions architect.

## Boundaries

- Keep component narratives and architecture diagrams human-authored.
- Keep exhaustive signatures and implementation inventories out of component documents.
- Do not implement routine feature bodies merely to make the skeleton appear complete.
- Do not add speculative layers, interfaces, patterns, or extension points.
- Record implementation-only discoveries without letting them silently redefine approved architecture.
