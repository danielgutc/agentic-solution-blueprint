# Container

[README](../../../README.md) / Foundation / [Design](../../../design/foundation/design.md) / C4 / [System](../../../design/c4/system/system.md) / [System containers](../../../design/c4/containers/system-containers.md) / Container

When materializing this template, adjust the breadcrumb for the destination and name the approved owning container.

## Table of contents

- [Purpose](#purpose)
- [Type and technology](#type-and-technology)
- [Responsibilities](#responsibilities)
- [Boundaries and data ownership](#boundaries-and-data-ownership)
- [Provided contracts](#provided-contracts)
- [Consumed contracts](#consumed-contracts)
- [Dependencies](#dependencies)
- [Contained components](#contained-components)
- [Internal interfaces](#internal-interfaces)
- [Owned technical documents](#owned-technical-documents)
- [Code documentation](#code-documentation)
- [Architecture decisions and split triggers](#architecture-decisions-and-split-triggers)
- [Open questions](#open-questions)
- [Diagrams](#diagrams)

## Purpose

## Type and technology

## Responsibilities

## Boundaries and data ownership

## Provided contracts

Describe externally provided runtime contracts at the container boundary. Keep exact source signatures in generated source-bound documentation.

## Consumed contracts

Describe externally consumed runtime contracts at the container boundary. Keep internal component ports in the distinct section below.

## Dependencies

## Contained components

List only approved components with existing detail pages. A container may have no component decomposition; do not invent components to organize source types.

## Internal interfaces

Describe approved component-to-component ports and responsibilities without copying source signatures. When source bindings exist, link the generated `_code-views/interfaces.md` view; otherwise do not create a placeholder.

## Owned technical documents

Link existing container-owned or same-container cross-component documents here, such as a walking skeleton, focused assessment, recovery note, contract design, or test design. Do not add placeholder links. Keep component-owned documents with their component, and keep exact source signatures in implementation source, API comments, executable tests, and canonical generated pages.

## Code documentation

After repository-owned implementation and a generated container entry exist, add a direct `[Code documentation](./code.md)` link. Until then, state that no code projection exists; do not create or link a placeholder. The generated entry links to canonical pages under `design/code/<implementation-unit>/<documentation-profile>/`.

## Architecture decisions and split triggers

For MVP scope, the technical architect records how the approved product and solution direction is realized by this scope's responsibilities, contracts, dependencies, data structures, and test seams. Explain known next-capability extension paths, delayed decisions, assumptions, and PoC-to-product gaps with owners. Link representative walking-skeleton or contract evidence and existing owned technical documents; do not copy source signatures or create future-feature placeholders.

## Open questions

## Diagrams

Embed approved `_diagrams/*.svg` exports and link their sibling `.drawio` sources. Link components to existing detail pages and diagrams only.
