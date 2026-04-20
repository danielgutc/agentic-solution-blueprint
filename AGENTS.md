# Agent Instructions

## Purpose

- Treat this repository as a reusable blueprint for starting new projects.
- Use this file as the primary source of behavioral instructions.
- Treat README files as descriptive references unless this file explicitly tells you to follow them operationally.

## Operating model

- Drive the project through enduring artifacts in `design/foundation/` and `design/c4/`.
- Keep implementation artifacts in `implementation/`.
- Keep Codex-only support files in `.codex/`.

## Repository model

### Top-level layout

```text
.codex/
design/
implementation/
tools/
tests/
```

### Design layout

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
      _diagrams/
    containers/
      README.md
      system-containers.md
      _diagrams/
      <container>/
        container.md
        _diagrams/
        components/
          <component>/
            component.md
            _diagrams/
            code.md
            _code-diagrams/
  instructions/
```

### Contribution model

- Keep `origin` as the solution repository.
- Use `agentic-solution-blueprint` as the secondary repository with the remote name `blueprint`.
- If the `blueprint` remote is missing, add it with `git remote add blueprint https://github.com/danielgutc/agentic-solution-blueprint.git`.
- Fetch the blueprint reference with `git fetch blueprint stable`.
- Fetch `blueprint main` before syncing an upstreamable `AGENTS.md` change.
- Treat `AGENTS.md` as the only file that should be contributed back to `agentic-solution-blueprint` from this repository unless the user explicitly says otherwise.
- For every `AGENTS.md` change, make an explicit upstreamability decision before committing:
  - `upstreamable` (default)
  - `solution-specific` (only when the user explicitly says not to upstream)
- If the user does not explicitly mark the change as `solution-specific`, treat it as `upstreamable` and sync it to `agentic-solution-blueprint`.
- Commit every `AGENTS.md` change in its own dedicated commit, separate from all other file changes, so the same change can be reused cleanly in both repositories.
- Treat all other files in this repository as solution-specific by default.
- Use the pull request title `Sync AGENTS.md from {solution repo name}` for blueprint updates coming from this repository.
- When an `AGENTS.md` change is explicitly identified as blueprint-safe and intended to be upstreamed, commit and push that `AGENTS.md` change to the solution repository as usual, then immediately sync it to `agentic-solution-blueprint` against the `main` branch unless the user explicitly says not to.
- Perform blueprint sync from the main repository using a dedicated local branch for the blueprint PR; do not require or keep a persistent local sync worktree folder for this purpose.
- For an upstreamable `AGENTS.md` change, the work is not complete until the corresponding blueprint pull request has been created or updated.
- If a blueprint pull request titled `Sync AGENTS.md from {solution repo name}` is already open, push the new upstreamable `AGENTS.md` commit to that existing pull request branch instead of creating a new pull request.
- If no blueprint pull request titled `Sync AGENTS.md from {solution repo name}` is open, create the corresponding branch in `agentic-solution-blueprint` and open a new pull request against `main`.
- After syncing an upstreamable `AGENTS.md` change, verify whether the blueprint pull request was created or updated and report the resulting branch and pull request URL.
- Do not stop after pushing only to `origin` when the `AGENTS.md` change is meant to be upstreamed to the blueprint repository.
- Do not create blueprint pull requests against `stable`; use `main` as the target branch for blueprint collaboration.

## Workflow

### Rules

- Clarify whether the next conversation step should focus on product, requirements, technical direction, design, traceability, C4 architecture, or implementation readiness.
- If the correct next step is not explicit, ask the user which one to tackle and give a short recommendation.
- Think and document in a pyramidal way: choose the highest appropriate level of abstraction first, and place details in the artifact type that matches the level of decision being made.
- Use domain-driven design during each step in the pyramid.
- Prefer bounded contexts as the basis for service boundaries when defining C4 containers for backend runtime concerns.
- Think in inputs, outputs, and contracts such as APIs when decomposing the problem and creating the relations and dependencies between them.
- Keep runtime authority explicit at every abstraction level and avoid accidental authority splits across peer containers.
- Prefer service contracts between runtime and backend concerns instead of direct runtime coupling to persistence internals.
- Prefer containerized services and separated storage boundaries when responsibilities differ and the split improves clarity, evolution, or operability.
- In microservice-oriented designs, keep persistence ownership per service boundary; shared database engines are allowed, shared schema ownership is not.
- Keep cross-service integration on service contracts (APIs/events) rather than direct cross-schema reads or writes.
- Do not jump ahead to implementation before the relevant requirements and design are sufficiently defined.
- Treat abstraction level as an explicit decision. Confirm and complete the current abstraction level before moving to a more detailed one.
- Do not make or update enduring C4 architecture artifacts until `design/foundation/design.md` has been reviewed and approved for the relevant change.
- Do not create or update C4 container artifacts until the relevant system-level C4 artifacts have been reviewed and approved for the change.
- Do not create or update C4 component or code-level artifacts until the relevant container-level C4 artifacts have been reviewed and approved for the change.

### Model 1: Requirements-first

- Recommend this model when desired behavior is clearer than the implementation approach.
- Follow this progression:

```text
product -> requirements -> tech -> design -> approval -> c4 -> traceability -> implementation
```

- Use this model when the project direction is driven primarily by business behavior, user outcomes, or functional expectations.

### Model 2: Design-first

- Recommend this model when technical constraints, architecture, feasibility, or existing design direction lead the work.
- Follow this progression:

```text
product -> tech -> design -> approval -> requirements -> c4 -> traceability -> implementation
```

- Use this model when the project direction is driven primarily by runtime constraints, technical risk, integration boundaries, or architectural feasibility.

### Steps

#### Product

- Use `design/foundation/product.md` to capture business context, target users or actors, goals, non-goals, and assumptions.
- Establish the project problem and intended outcomes before defining enduring requirements or architecture.
- Output from this step should provide enough context for the next selected workflow step.

#### Requirements

- Use `design/foundation/requirements.md` to define enduring functional and non-functional requirements, constraints, and assumptions.
- Prefer structured, testable statements.
- Use EARS where practical for functional requirements.
- Use stable requirement IDs that can be referenced from the traceability matrix.
- In the requirements-first model, derive requirements primarily from `product.md`.
- In the design-first model, derive requirements from `product.md` and the approved `design.md`.

#### Tech

- Use `design/foundation/tech.md` to document technical direction, chosen platforms, runtime constraints, and key technical decisions.
- Keep this artifact focused on enduring technical direction rather than task-level implementation detail.
- In the requirements-first model, use approved product direction and current requirements as primary inputs.
- In the design-first model, this step normally comes before design and helps frame the design constraints and choices.

#### Design

- Use `design/foundation/design.md` to document enduring design decisions, tradeoffs, and architecture explanation.
- Keep this file aligned with the technical direction and the chosen workflow model.
- In the requirements-first model, use `product.md`, `requirements.md`, and `tech.md` as primary inputs.
- In the design-first model, use `product.md` and `tech.md` as primary inputs, then refine requirements after design approval.

#### Approval

- Use this step to review and approve the current `design/foundation/design.md` before creating or updating enduring C4 architecture artifacts.
- Do not move to the C4 step until this approval gate is satisfied.

#### C4

- Use `design/c4/` to document enduring architecture after the relevant design direction is approved.
- Keep the C4 artifacts aligned with `design/foundation/design.md`.
- Use the approved `design.md` as the primary input for this step.
- Progress through C4 pyramidally by abstraction level:

```text
system -> approval -> containers -> approval -> components -> approval -> code-level docs
```

#### Traceability

- Use `design/foundation/traceability-matrix.md` to map requirement IDs to C4 elements and implementation components.
- Update this artifact after requirements and architecture are sufficiently stable to trace meaningfully.
- Use `requirements.md`, `design.md`, and the current C4 artifacts as the primary inputs for this step.

#### Implementation

- Use `implementation/` for real application components only after the relevant foundation and architecture artifacts justify implementation work.
- Keep implementation aligned with the approved design and the traceability matrix.
- Use the approved foundation artifacts, current C4 artifacts, and the traceability matrix as the primary inputs for this step.

## Foundation

### Purpose and model

- Use `design/foundation/` for enduring business, requirements, technical, design, and traceability artifacts.
- Treat these files as the main source of truth for what the project is, what it must do, how it is designed, and how requirements map to architecture and implementation.

### General conventions

- Read `design/foundation/product.md`, `design/foundation/requirements.md`, and `design/foundation/tech.md` before proposing feature direction.
- Read `design/foundation/design.md` when enduring design direction or tradeoffs matter.
- Read `design/foundation/traceability-matrix.md` when tracing requirements to architecture or implementation.
- Keep foundation artifacts aligned with each other as the project evolves.
- Do not put C4-style runtime topology, container boundaries, or lower-level interaction mechanics in foundation artifacts unless that detail is necessary to explain an enduring high-level design decision.
- Use `In this section` only for sibling navigation at the same hierarchy level.
- Add a `## Table of contents` section to foundation Markdown entry pages.

### Artifacts

#### `design/foundation/product.md`

- Use this file for business-facing product direction.
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

#### `design/foundation/requirements.md`

- Use this file for enduring requirements.
- Prefer structured, testable statements.
- Use EARS where practical for functional requirements.
- Use stable requirement IDs.
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

#### `design/foundation/tech.md`

- Use this file for technical direction and constraints, not detailed implementation steps.
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

#### `design/foundation/design.md`

- Use this file for enduring design decisions, tradeoffs, and architecture explanation.
- Use this file to describe the high-level software-system context and responsibilities that the next approved C4 system level will elaborate.
- Keep this file design-facing and architecture-facing rather than process-facing.
- Keep this file above container decomposition; do not enumerate runtime containers, data stores, or component groupings here unless that detail is necessary to explain an enduring design decision.
- Keep this file in the following structure:

```text
# Design

## System overview
## Architecture decisions
## System architecture focus
## Data and integration design
## Operational considerations
## Open questions
```

#### `design/foundation/traceability-matrix.md`

- Use this file to map requirement IDs to C4 elements and implementation components.
- Keep the requirement IDs synchronized with `design/foundation/requirements.md`.
- Keep this file in the following structure:

```text
# Traceability Matrix

## Traceability matrix

| Requirement ID | Requirement summary | C4 element(s) | Implementation component(s) | Notes |
| --- | --- | --- | --- | --- |
```

## C4

### Purpose and model

- Use `design/c4/` as the canonical architecture area.
- Treat `design/c4/` as enduring architecture, not temporary planning.
- Keep `design/foundation/design.md` and `design/c4/` aligned.
- Respect the C4 abstraction levels and do not mix them:
  - software system: the highest-level system boundary, users, external systems, and major responsibilities
  - container: an application or data store that must be running or available for the software system to work
  - component: a grouping of related functionality behind a well-defined interface inside a container

### General conventions

- Treat C4 container as a runtime boundary (application, service, data store, file/object store, broker), not as a Docker artifact.
- Use Markdown files as the narrative entry point for each C4 level.
- Store one or more PlantUML diagrams beside the related Markdown file.
- Keep long-lived architecture diagrams under `design/c4/`.
- Allow multiple diagrams at the same abstraction level when they communicate different concerns clearly.
- Give PlantUML elements and boundaries explicit names or aliases; avoid anonymous diagram nodes and boundaries that trigger warnings.
- Keep `.puml` files as the authoritative diagram source, and when a diagram is part of the main reading flow, render it to `.svg` beside the source and embed that `.svg` in the corresponding Markdown entry point.
- When PlantUML rendering is needed, expect a local renderer jar to be placed under `tools/plantuml/`; treat that jar as a local tool dependency rather than repository content.
- Keep one system description under `design/c4/system/`.
- Keep C4 components nested under their owning container.
- Use `_diagrams/` as the diagram folder name for enduring C4 views.
- Add container folders under `design/c4/containers/` only when the project architecture defines them.
- Add component folders only under an existing container.
- Use `design/c4/` for enduring runtime topology, boundaries, responsibilities, major interaction mechanisms, and other architecture detail that is too specific for foundation artifacts but not yet code-level design.
- For backend services, prefer a near 1:1 relationship between C4 service containers and deployable microservices when ownership and operability boundaries are clear.
- Decompose containers by enduring responsibility boundaries (for example API, domain workflow, integration, and storage) rather than by implementation convenience.
- When a shared relational engine is used, model it as infrastructure support rather than shared domain authority, and keep schema ownership under the owning service containers.
- Model relational databases and file/object stores as C4 data-store containers (for example cylinder notation), not as service containers.
- In component-level diagrams, represent databases and file/object stores with data-store notation (for example `database`), and represent schemas or namespaces as storage structure elements rather than regular service/component rectangles.
- For component-level storage interactions, prefer direct arrows from consuming components to data-store nodes (for example `Component --> DataStore`) with protocol/payload labels; do not introduce interface elements for schemas or file/object storage endpoints unless the storage API is modeled as a separate service.
- Do not model schema access or file/object store access as interface contracts inside component diagrams; model those relations directly to data-store nodes.
- For service/API contracts (non-storage), use a strict provider/consumer interface pattern:
  - provider exposes interface with association style (for example `Provider - IContract`)
  - consumer depends on interface with explicit `requires` dependency (for example `Consumer ..> IContract : requires`)
- If an API boundary is needed in front of a data store, model that API as a separate service container rather than as an internal pseudo-component of the data store.
- For container relationships, record the protocol or transport family and the payload or data style when known.
- Keep deployment-topology details (replication, node placement, orchestrator topology) in deployment architecture artifacts rather than container-level C4 decomposition.
- Use `In this section` only for sibling navigation at the same hierarchy level.
- Use explicit child-navigation sections:
  - `Contained containers` in `system-containers.md`
  - `Contained components` in `container.md`
- End `system-containers.md` with a tree-style decomposition section that maps `system -> containers -> designed children` at the current approved abstraction level.
- In that system-containers tree section, include links to already-designed child artifacts and show persistence ownership per service boundary (for example owned schema names), while keeping shared database engines represented as infrastructure support.
- For data-store containers in that tree, prefer schema/namespace/folder structure entries rather than service-style component lists.
- Add a `## Table of contents` section to C4 Markdown entry pages.

### Artifacts

#### `design/c4/system/system.md`

- Keep this file as the whole-system narrative entry point.
- Use it to describe the system scope, actors, external systems, responsibilities, and boundaries.
- Include a `Next level` link to `design/c4/containers/system-containers.md`.
- Keep this file at software-system level; it should not enumerate container internals beyond what is needed to explain the overall system boundary and responsibilities.
- Keep system-level diagrams in `design/c4/system/_diagrams/`.
- Start with a system context diagram.
- Make the system context diagram focus on one software system in scope, the people who use it, the external software systems around it, and concise relationship labels between them.
- Do not use the system context diagram to show containers, internal runtime boundaries, or component decomposition.
- Keep this file in the following structure:

```text
# System

## Purpose
## Recommended sections
- Summary
- Actors
- External systems
- Responsibilities
- Boundaries
- Open questions

## Diagrams
```

#### `design/c4/containers/<container>/container.md`

- Use `design/c4/containers/system-containers.md` as the container-level entry point and overview.
- Use each `container.md` file to describe one runtime container or data store as a black box, focusing on purpose, responsibilities, boundaries, contracts, dependencies, and contained components.
- State each container type explicitly (for example application, service, relational data store, or file/object store) and keep the black-box boundary clear.
- At container level, include the container technology and make contracts concrete enough to name the main protocol or transport and the broad payload or data style where that is already known.
- Document architecture decisions at the nearest effective level of abstraction (for example, keep service-split or consolidation decisions in the affected container doc when they are container-specific).
- When persistence is relational and service-oriented, state schema ownership explicitly in the owning service container and avoid defining shared cross-service schema contracts.
- For data-store containers, describe internal structure through schema/namespace/folder boundaries; avoid forcing application-style component decomposition unless there is a strong architectural reason.
- Keep each container folder shaped as:

```text
containers/
  system-containers.md
  _diagrams/
  <container>/
    container.md
    _diagrams/
    components/
```

#### `design/c4/containers/<container>/components/<component>/component.md`

- Use this file to describe the component purpose, responsibilities, ownership, interfaces, ports, dependencies, and constraints.
- At component level, be explicit about whether the component is project-built or provided by a selected third-party stack.
- Describe provided and required interfaces with the main protocol or transport family where known.
- Prefer UML 2.0 component-diagram notation rather than generic rectangles when the richer notation helps communicate the architecture.
- Component-level diagrams should make the following explicit when relevant:
  - project-built versus third-party components
  - provided and required interfaces
  - protocols or transport families
  - ports and component boundaries
  - grouping boundaries such as packages, nodes, or runtime groupings
- In component-level interaction lines, orient dependencies from consumers to required interfaces (for example `..> : requires`), and model providers as exposing interfaces directly (for example `component - interface`) so storage or external systems are not shown as invoking service logic.
- Before finalizing a component diagram, run this validation checklist:
  - each `requires` relation starts at the consumer component or caller service
  - storage interactions are drawn directly to data-store nodes (no storage/schema interfaces unless modeled as a separate API service)
  - service/API providers expose interfaces rather than invoking them
  - databases, file/object stores, schemas, and namespaces are not drawn as regular service/component rectangles
  - when this storage-notation rule changes, align sibling component diagrams in the same repository pass to keep notation consistent across containers
- When helpful for readability, place the component name, technology or third-party software name, and a short responsibility summary directly inside each component box.
- Prefer this in-box text style:
  - bold component name
  - italic technology or third-party software line
  - responsibility summary capped at 8 words
- Wrap long component text intentionally with line breaks to control diagram width and keep the rendered view readable.
- Use groups such as packages, nodes, or runtime boundaries only when they clarify a real subdomain, deployment boundary, or ownership split; do not add them only for decoration.
- Use `skinparam componentStyle uml2` for UML 2.0 component diagrams unless there is a strong reason not to.

#### `design/c4/containers/<container>/components/<component>/code.md`

- Use this file to describe the internal code structure of the component.
- Focus on modules, key types, important flows, extension points, and testing notes.
- Keep each component folder shaped as:

```text
<component>/
  component.md
  _diagrams/
  code.md
  _code-diagrams/
```

## Implementation

### Purpose and model

- Use `implementation/` for real built application components.
- Treat `implementation/` as a flat top-level area of real application components unless the project design justifies a different structure.

### General conventions

- Keep implementation components aligned with the enduring requirements, design, and C4 architecture.
- Do not create implementation components before the project is ready for implementation.

## File-type instructions

- Read `design/instructions/<type>.md` when editing the corresponding artifact type.
- Follow `design/instructions/csharp.md` when creating or modifying C# code.
- Follow `design/instructions/docker.md` when creating or modifying Docker files.
- Follow `design/instructions/plantuml.md` when creating or modifying PlantUML files.
- Follow `design/instructions/markdown.md` when creating or modifying Markdown files.

## Maintenance

- Keep project design artifacts in `design/`.
- Keep repo-local scripts and developer automation in `tools/`.
- Keep cross-component validation in `tests/`.
- Keep Codex-specific memory and skills in `.codex/`.
- Update relevant foundation, architecture, or instruction files when structural conventions change.
- Avoid duplicating behavioral instructions in business-facing files when `AGENTS.md` can express them more clearly.
