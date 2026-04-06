# Structure

## Repository Layout

- `.codex/` contains Codex-specific memory, skills, and agent guidance.
- `.design/steering/` contains stable project guidance.
- `.design/instructions/` contains focused authoring and implementation guidance by artifact type.
- `.design/specs/` contains per-feature requirements, design, tasks, and diagrams.
- `tools/` contains repository-local scripts and developer automation.
- `tests/` contains cross-cutting integration and end-to-end validation.
- Additional solution components can be added at the repo root as the architecture becomes clearer.

## Workflow

Feature specs support two valid flows:

1. Requirements-first: define requirements, create the design, break work into tasks, then implement.
2. Design-first: define the design first, derive requirements from it, break work into tasks, then implement.

Use requirements-first for product-driven work with flexible implementation.
Use design-first when technical constraints or architectural feasibility lead the change.

## Diagrams

- Use PlantUML for architecture and design diagrams.
- Keep feature-specific diagrams in the relevant spec folder.
