# Agent Instructions

## Purpose

- Treat this repository as a reusable blueprint for starting new projects.
- Use this file as the primary source of behavioral instructions.
- Treat README files as descriptive references unless this file explicitly tells you to follow them operationally.

## Operating model

- Read `.blueprint/blueprint.toml` before selecting a workflow or lifecycle phase.
- Drive the project through enduring artifacts in `design/foundation/` and `design/c4/`.
- Keep implementation artifacts in `implementation/`.
- Keep Codex-only support files in `.codex/`.
- Keep project-specific skills in `.agents/skills/`; consume reusable agents and skills from the user-level engineering toolkit instead of copying them into this repository.
- Do not create concrete implementation components or C4 containers/components until the project architecture justifies them.
- Allow only the minimal walking skeleton needed to prove technical design and delivery readiness before full development.

## Role ownership

- The `product_owner` owns product direction, MVP boundaries, requirements, and acceptance intent.
- The `solutions_architect` owns technical direction, system scope, domain boundaries, C4 context, and authoritative container boundaries.
- The `technical_architect` owns component design, internal contracts, test seams, the walking skeleton, and the documentation-generation toolset within approved containers.
- The `software_engineer` implements approved skeleton bodies through TDD after implementation readiness is approved.
- The `infrastructure_engineer` owns the delivery foundation, CI/CD, environments, infrastructure as code, and documentation execution in CI.
- The `test_engineer` owns independent integration, contract, end-to-end, acceptance, and regression verification.
- Keep each role at its assigned abstraction level and return boundary changes to the owning role.
- Use compact handoffs with identifiers, evidence, unresolved risks, and the next owner so agents do not repeat repository discovery.

## Repository model

### Top-level layout

```text
.agents/
  skills/
.blueprint/
  blueprint.toml
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
    implementation-readiness.md
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
            code.md              # generated
            code-diagrams/       # generated sources
  instructions/
```

## Workflow

### Rules

- Leave `selected_workflow` as `unset` only while maintaining the reusable template; a consuming project must set it to `requirements-first` or `design-first` before advancing enduring project artifacts.
- Clarify whether the next conversation step should focus on product, requirements, technical direction, design, solution C4, traceability, technical design, delivery foundation, implementation readiness, full development, or integrated verification.
- If the correct next step is not explicit, ask the user which one to tackle and give a short recommendation.
- Do not jump ahead to technical design before requirements, technical direction, and solution architecture are sufficiently defined.
- Do not make or update enduring C4 system or container artifacts until `design/foundation/design.md` has been reviewed and approved for the relevant change.
- Do not begin full development until `design/foundation/implementation-readiness.md` records approval for the relevant scope.
- Seek approval before advancing through either the design-approval or implementation-readiness gate.
- In design-first work, return to design approval when derived requirements materially change the approved solution.

### Model 1: Requirements-first

- Recommend this model when desired behavior is clearer than the implementation approach.
- Follow this progression:

```text
product -> requirements -> tech -> design -> design approval -> c4 solution -> traceability -> technical design -> delivery foundation -> implementation readiness approval -> full development -> integrated verification
```

- Use this model when the project direction is driven primarily by business behavior, user outcomes, or functional expectations.

### Model 2: Design-first

- Recommend this model when technical constraints, architecture, feasibility, or existing design direction lead the work.
- Follow this progression:

```text
product -> tech -> design -> design approval -> requirements -> c4 solution -> traceability -> technical design -> delivery foundation -> implementation readiness approval -> full development -> integrated verification
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
- Select the build, test, documentation, static-analysis, packaging, CI/CD, and non-production delivery toolchain before the delivery-foundation step.
- Record stable repository commands once they are implemented.
- In the requirements-first model, use approved product direction and current requirements as primary inputs.
- In the design-first model, this step normally comes before design and helps frame the design constraints and choices.

#### Design

- Use `design/foundation/design.md` to document enduring design decisions, tradeoffs, and architecture explanation.
- Keep this file aligned with the technical direction and the chosen workflow model.
- In the requirements-first model, use `product.md`, `requirements.md`, and `tech.md` as primary inputs.
- In the design-first model, use `product.md` and `tech.md` as primary inputs, then refine requirements after design approval.

#### Design Approval

- Use this step to review and approve the current `design/foundation/design.md` before creating or updating enduring C4 architecture artifacts.
- Do not move to C4 system or container modeling until this approval gate is satisfied.

#### C4 Solution

- Use `design/c4/` to document the system context and authoritative container architecture after the relevant design direction is approved.
- Keep the C4 artifacts aligned with `design/foundation/design.md`.
- Use the approved `design.md` as the primary input for this step.
- Keep component and code-level design out of this step.

#### Traceability

- Use `design/foundation/traceability-matrix.md` to map requirement IDs to C4 elements and implementation components.
- Update this artifact after requirements and architecture are sufficiently stable to trace meaningfully.
- Use `requirements.md`, `design.md`, and the current C4 artifacts as the primary inputs for this step.
- Add implementation and verification references incrementally as technical design and tests become available.

#### Technical Design

- Refine approved containers into C4 components, internal contracts, dependency direction, test seams, and implementation slices.
- Keep `component.md` and component diagrams human-authored because they explain responsibilities, boundaries, and design intent.
- Create only the minimal source interfaces, executable skeleton, and representative tests needed to prove architecture-significant behavior.
- Configure the ecosystem-native API documentation generator and compact code-projection generator.
- Do not implement broad feature bodies during this step.

#### Delivery Foundation

- Establish repository-owned commands for clean build, initial tests, formatting, static analysis, documentation generation and verification, packaging, and non-production delivery.
- Allow the technical architect and infrastructure engineer to work in parallel only after container boundaries and toolchain decisions are stable; synchronize through the same walking skeleton.
- Implement CI so those commands run from a clean checkout and preserve actionable evidence.
- Generate `code.md` and code-diagram sources from the walking skeleton; never author those projections manually.
- Produce one immutable, versioned artifact and exercise the appropriate non-production delivery path.
- Production deployment automation is not required at this stage.

#### Implementation Readiness Approval

- Use `design/foundation/implementation-readiness.md` to record evidence for the scope entering full development.
- Require every applicable criterion from `.blueprint/blueprint.toml` to pass or be explicitly rejected as out of scope by the decision owner.
- Do not approve readiness when the walking skeleton cannot build, test, document, package, or follow its intended delivery path in CI.

#### Full Development

- Use `implementation/` for approved application components after implementation readiness is approved.
- Implement behavior in small TDD slices aligned with requirements, technical design, and the traceability matrix.
- Keep source interfaces, API comments, tests, generated `code.md`, and generated code diagrams synchronized through repository tooling.
- Update human-authored architecture only when implementation evidence changes an enduring decision or boundary.

#### Integrated Verification

- Use `tests/integration/` and `tests/e2e/` for cross-component and user-observable verification.
- Derive verification from requirement IDs, acceptance intent, contracts, and operational risks.
- Add integrated test gates, deployment health checks, and release controls to CI/CD as assembled behavior becomes available.
- Keep production promotion and rollback readiness as explicit release concerns rather than assumptions.

## Foundation

### Purpose and model

- Use `design/foundation/` for enduring business, requirements, technical, design, traceability, and implementation-readiness artifacts.
- Treat these files as the main source of truth for what the project is, what it must do, how it is designed, how requirements map to delivery, and whether full development may begin.

### General conventions

- Read `design/foundation/product.md`, `design/foundation/requirements.md`, and `design/foundation/tech.md` before proposing feature direction.
- Read `design/foundation/design.md` when enduring design direction or tradeoffs matter.
- Read `design/foundation/traceability-matrix.md` when tracing requirements to architecture or implementation.
- Read `design/foundation/implementation-readiness.md` before beginning or delegating full development.
- Keep foundation artifacts aligned with each other as the project evolves.

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
## Developer feedback and delivery commands
## API documentation and code projections
## CI/CD platform and quality gates
## Deployment model
## Constraints
## Key technical decisions
```

#### `design/foundation/design.md`

- Use this file for enduring design decisions, tradeoffs, and architecture explanation.
- Keep C4 references aligned with `design/c4/`.
- Keep this file in the following structure:

```text
# Design

## System overview
## Architecture decisions
## C4 references
## Data and integration design
## Operational considerations
## Delivery and documentation strategy
## Open questions
```

#### `design/foundation/traceability-matrix.md`

- Use this file to map requirement IDs to C4 elements and implementation components.
- Keep the requirement IDs synchronized with `design/foundation/requirements.md`.
- Keep this file in the following structure:

```text
# Traceability Matrix

## Traceability matrix

| Requirement ID | Requirement summary | C4 element(s) | Implementation component(s) | Verification evidence | Notes |
| --- | --- | --- | --- | --- | --- |
```

#### `design/foundation/implementation-readiness.md`

- Use this file as the auditable gate before full development.
- Record commands, artifacts, pipeline runs, generated-document checks, non-production delivery evidence, accepted risks, and approval.
- Scope readiness to the relevant containers, components, or implementation slice rather than assuming one approval covers all future work.
- Keep this file in the following structure:

```text
# Implementation Readiness

## Scope
## Status
## Required Evidence
## Deferred Items
## Approval
```

## C4

### Purpose and model

- Use `design/c4/` as the canonical architecture area.
- Treat `design/c4/` as enduring architecture, not temporary planning.
- Keep `design/foundation/design.md` and `design/c4/` aligned.

### General conventions

- Use human-authored Markdown as the narrative entry point for system, container, and component levels.
- Treat code-level Markdown and code-diagram sources as generated projections of implementation source, API comments, and tests.
- Store one or more PlantUML diagrams beside the related human-authored Markdown file when a diagram clarifies architecture.
- Keep long-lived architecture diagrams under `design/c4/`.
- Allow multiple diagrams at the same abstraction level when they communicate different concerns clearly.
- Keep one system description under `design/c4/system/`.
- Keep C4 components nested under their owning container.
- Add container folders under `design/c4/containers/` only when the project architecture defines them.
- Add component folders only under an existing approved container during technical design.
- Commit deterministic generated `code.md` and code-diagram sources; publish full API documentation and rendered outputs as CI artifacts by default.

### Artifacts

#### `design/c4/system/system.md`

- Keep this file as the whole-system narrative entry point.
- Use it to describe the system scope, actors, external systems, responsibilities, and boundaries.
- Keep system-level diagrams in `design/c4/system/diagrams/`.
- Start with a system context diagram.
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

- Use this file to describe the container purpose, responsibilities, interfaces, dependencies, and contained components.
- Keep each container folder shaped as:

```text
<container>/
  container.md
  diagrams/
  components/
```

#### `design/c4/containers/<container>/components/<component>/component.md`

- Keep this file human-authored.
- Use it to describe component purpose, responsibilities, architectural interfaces, dependencies, constraints, invariants, and design rationale.
- Do not duplicate source signatures or generated API reference content.

#### `design/c4/containers/<container>/components/<component>/code.md`

- Generate this file from implementation source, ecosystem-native API comments, and contract-test metadata.
- Include a generated-file warning, source scope, generator command, modules, public interfaces, important types, dependencies, extension points, and relevant test identifiers.
- Keep the projection compact and omit exhaustive private-member inventories.
- Never edit this file manually; change source, comments, tests, or generator configuration instead.
- Generate deterministic diagram sources under `code-diagrams/` and keep rendered outputs outside source control by default.
- Keep each component folder shaped as:

```text
<component>/
  component.md          # human-authored architecture
  diagrams/             # human-authored architecture sources
  code.md               # generated compact projection
  code-diagrams/        # generated diagram sources
```

## Implementation

### Purpose and model

- Use `implementation/` for real built application components.
- Treat `implementation/` as a flat top-level area of real application components unless the project design justifies a different structure.

### General conventions

- Keep implementation components aligned with the enduring requirements, design, and C4 architecture.
- During technical design, create only the walking skeleton required to prove contracts and delivery assumptions.
- Do not begin full feature implementation before the relevant implementation-readiness approval.
- Treat source interfaces, API comments, and executable tests as the code-contract source for generated documentation.

## File-type instructions

- Read `design/instructions/<type>.md` when editing the corresponding artifact type.
- Follow `design/instructions/csharp.md` when creating or modifying C# code.
- Follow `design/instructions/api-documentation.md` when creating public interfaces, API comments, documentation generators, or code projections.
- Follow `design/instructions/ci-cd.md` when creating or modifying build, validation, documentation, packaging, deployment, or release pipelines.
- Follow `design/instructions/docker.md` when creating or modifying Docker files.
- Follow `design/instructions/plantuml.md` when creating or modifying PlantUML files.
- Follow `design/instructions/markdown.md` when creating or modifying Markdown files.

## Maintenance

- Keep project design artifacts in `design/`.
- Keep repo-local scripts and developer automation in `tools/`.
- Keep cross-component validation in `tests/`.
- Keep Codex-specific memory in `.codex/` and project-specific skills in `.agents/skills/`.
- Keep reusable agents and skills in the external engineering toolkit and install them through user-level symbolic links.
- Keep `.blueprint/blueprint.toml` aligned with structural and gate conventions.
- Update relevant foundation, architecture, or instruction files when structural conventions change.
- Avoid duplicating behavioral instructions in business-facing files when `AGENTS.md` can express them more clearly.
