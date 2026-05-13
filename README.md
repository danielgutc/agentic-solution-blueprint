# Project Blueprint

This repository is a reusable blueprint for starting new software projects.

## Purpose

Use this blueprint to structure work from product intent to implementation with explicit abstraction gates and durable documentation artifacts.

## Start here

- [Foundation product](./design/foundation/product.md)
- [Foundation task tracker](./design/foundation/task.md)
- [Foundation agent topology (optional)](./design/foundation/agent-topology.md)
- [Foundation design](./design/foundation/design.md)
- [C4 system](./design/c4/system/system.md)
- [C4 system containers](./design/c4/containers/system-containers.md)
- [Instruction index](./.blueprint/instructions/README.md)

## Repository structure

- `.blueprint/` contains reusable governance, instructions, templates, and samples.
- `.codex/` contains Codex-specific skills and memory.
- `design/` contains enduring foundation and architecture artifacts.
- `implementation/` contains real application components.
- `tools/` contains repo-local utilities and automation scripts.
- `tests/` contains cross-component integration and end-to-end tests.

## Documentation structure

### Foundation

Use [design/foundation/](./design/foundation/) for enduring project definitions:

- product
- requirements
- tech
- design
- task tracker
- traceability matrix
- optional agent topology

### C4 architecture

Use [design/c4/](./design/c4/) for enduring architecture artifacts:

- system
- system containers
- per-container documentation and components

### Instructions

Use [.blueprint/instructions/](./.blueprint/instructions/) for modular authoring rules:

- process workflows and gates
- artifact schemas
- shared standards

### Templates

Use [.blueprint/templates/](./.blueprint/templates/) for solution-agnostic target structures.

### Samples

Use [.blueprint/samples/](./.blueprint/samples/) for reference-quality examples.

### Skills

Use [.codex/skills/](./.codex/skills/) for on-demand, task-specific reusable workflows.

## Top-level layout

```text
.blueprint/
.codex/
design/
implementation/
tools/
tests/
```