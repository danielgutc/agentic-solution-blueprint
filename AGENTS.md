# Agent Instructions

## Purpose

- Treat this repository as a reusable blueprint for starting new projects.
- Use this file as the primary source of behavioral instructions.
- Treat README files as descriptive references unless this file explicitly tells you to follow them operationally.

## Source of truth

- Use `design/foundation/product.md` for business and product direction.
- Use `design/foundation/requirements.md` for enduring requirements.
- Use `design/foundation/tech.md` for technical direction and constraints.
- Use `design/foundation/design.md` for enduring design decisions.
- Use `design/foundation/traceability-matrix.md` as the requirements-to-components traceability matrix.
- Use `design/c4/` as the canonical architecture area.
- Use `implementation/` for real built components only after the workflow reaches implementation.
- Keep Codex-only support files under `.codex/`.

## Repository layout

- Expect the top-level repository layout to be:

```text
.codex/
design/
implementation/
tools/
tests/
```

- Expect the design layout to be:

```text
design/
  foundation/
    product.md
    requirements.md
    tech.md
    design.md
    traceability-matrix.md
  c4/
    README.md
    system/
      system.md
      diagrams/
    containers/
      README.md
      <container>/
        container.md
        diagrams/
        components/
          <component>/
            component.md
            diagrams/
            code.md
            code-diagrams/
  instructions/
```

- Keep C4 components nested under their owning container.
- Keep one system description under `design/c4/system/`.
- Add container folders under `design/c4/containers/` only when the project architecture defines them.
- Add component folders only under an existing container.
- Keep real runtime components under `implementation/<component>/`.
- Do not create concrete implementation components, C4 containers, or C4 components preemptively in the blueprint.

## What to read

- Read `design/foundation/product.md`, `design/foundation/requirements.md`, and `design/foundation/tech.md` before proposing feature direction.
- Read `design/foundation/design.md` and `design/c4/` when architectural views or enduring boundaries matter.
- Read `design/foundation/traceability-matrix.md` when tracing requirements to architecture or implementation.
- Read `design/instructions/<type>.md` when editing the corresponding artifact type.

## Foundation templates

### `design/foundation/product.md`

- Keep this file in the following structure:

```text
# Product

## Summary
## Users or actors
## Problem to solve
## Core outcomes
## Goals
## Non-goals
## Assumptions
```

- Keep the content business-facing rather than implementation-facing.

### `design/foundation/requirements.md`

- Keep this file in the following structure:

```text
# Requirements

## Functional requirements
### FR-001

## Non-functional requirements
### NFR-001

## Constraints
### CON-001

## Assumptions
### ASM-001
```

- Use stable requirement IDs.
- Prefer structured, testable statements.
- Use EARS where practical for functional requirements.

### `design/foundation/tech.md`

- Keep this file in the following structure:

```text
# Tech

## Languages and runtimes
## Frameworks and platforms
## Build and package tools
## Testing approach
## Deployment model
## Constraints
## Key technical decisions
```

- Use this file for technical direction and constraints, not detailed implementation steps.

### `design/foundation/design.md`

- Keep this file in the following structure:

```text
# Design

## System overview
## Architecture decisions
## C4 references
## Data and integration design
## Operational considerations
## Open questions
```

- Use this file for enduring design decisions and architecture explanation.
- Keep C4 references aligned with `design/c4/`.

### `design/foundation/traceability-matrix.md`

- Keep this file in the following structure:

```text
# Traceability Matrix

## Traceability matrix

| Requirement ID | Requirement summary | C4 element(s) | Implementation component(s) | Notes |
| --- | --- | --- | --- | --- |
```

- Use this file to map requirement IDs to C4 elements and implementation components.
- Keep the requirement IDs synchronized with `design/foundation/requirements.md`.

## C4 templates

### `design/c4/system/system.md`

- Keep this file as the whole-system narrative entry point.
- Use it to describe the system scope, actors, external systems, responsibilities, and boundaries.

### `design/c4/containers/<container>/container.md`

- Use this file to describe the container purpose, responsibilities, interfaces, dependencies, and contained components.

### `design/c4/containers/<container>/components/<component>/component.md`

- Use this file to describe the component purpose, responsibilities, interfaces, dependencies, and constraints.

### `design/c4/containers/<container>/components/<component>/code.md`

- Use this file to describe the internal code structure of the component.
- Focus on modules, key types, important flows, extension points, and testing notes.

## File-type instructions

- Follow `design/instructions/csharp.md` when creating or modifying C# code.
- Follow `design/instructions/docker.md` when creating or modifying Docker files.
- Follow `design/instructions/plantuml.md` when creating or modifying PlantUML files.
- Follow `design/instructions/markdown.md` when creating or modifying Markdown files.

## Workflow

- Drive the project through enduring requirements and design artifacts in `design/foundation/`.
- Clarify whether the next conversation step should focus on product, requirements, technical direction, design, traceability, C4 architecture, or implementation readiness.
- If the correct next step is not explicit, ask the user which one to tackle and give a short recommendation.
- Recommend requirements-first when desired behavior is clearer than the implementation approach.
- Recommend design-first when technical constraints, architecture, feasibility, or existing design direction lead the work.
- Do not jump ahead to implementation before the relevant requirements and design are sufficiently defined.
- When writing `design/foundation/requirements.md`, prefer structured, testable statements and use EARS where practical.
- Use `design/foundation/design.md` for enduring design decisions, tradeoffs, and architecture explanation.
- Use `design/foundation/traceability-matrix.md` to map requirements to C4 elements and implementation components.

## C4 usage

- Treat `design/c4/` as enduring architecture, not temporary planning.
- Keep `design/foundation/design.md` and `design/c4/` aligned.
- Keep long-lived architecture diagrams under `design/c4/`.
- Use PlantUML for architecture and design diagrams.
- Allow multiple diagrams at the same abstraction level when they communicate different concerns clearly.

## Boundaries

- Keep planning and architecture in `design/`.
- Keep built application components in `implementation/`.
- Keep repo-local scripts and developer automation in `tools/`.
- Keep cross-component validation in `tests/`.

## Maintenance

- Keep project design artifacts in `design/`.
- Keep Codex-specific memory and skills in `.codex/`.
- Update relevant foundation, architecture, or instruction files when structural conventions change.
- Avoid duplicating behavioral instructions in business-facing files when `AGENTS.md` can express them more clearly.
