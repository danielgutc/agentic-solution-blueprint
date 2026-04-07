# Feature Specs

This folder contains feature specs as change-focused work packages.

Each feature spec should live in its own folder:

- `.design/specs/<feature>/requirements.md`
- `.design/specs/<feature>/design.md`
- `.design/specs/<feature>/tasks.md`
- `.design/specs/<feature>/diagrams/`

## Supported workflows

### Requirements-first

Use this when the desired system behavior is known and the implementation can adapt.

Flow:

1. `requirements.md`
2. `design.md`
3. `tasks.md`
4. implementation

### Design-first

Use this when architecture, feasibility, or technical constraints lead the work.

Flow:

1. `design.md`
2. `requirements.md`
3. `tasks.md`
4. implementation

## Requirements format

Prefer EARS-style requirements where practical:

`WHEN <condition> THE SYSTEM SHALL <behavior>`

Keep requirements specific enough to be testable.
Split separate behaviors into separate requirement statements.

## File roles

- `requirements.md` describes what must be true.
- `design.md` explains how the requirements will be satisfied, including architecture, interactions, and tradeoffs.
- `tasks.md` breaks the work into concrete implementation steps that can be executed and verified.

## Scope guidance

- A feature spec is a change unit, not a service or component.
- A spec may affect one component, many components, or only project structure.
- Use feature specs for non-trivial work with multiple tasks and meaningful design decisions.
- For trivial fixes or very small changes, skip feature spec creation unless structured planning is clearly useful.
- Reference `.design/c4/` when a spec changes the enduring system, container, component, or code-level architecture.
