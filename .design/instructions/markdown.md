# Markdown Files Instructions

## Purpose

Use Markdown for steering, specs, and lightweight project documentation.

## Rules

- Keep files focused on a single topic or artifact.
- Prefer short sections with clear headings.
- Write for fast scanning and future maintenance.
- Keep examples close to the rule or decision they explain.

## Conventions

- Use sentence case or simple title case consistently within a file.
- Prefer bullet lists for decisions, constraints, and tasks.
- Keep task lists actionable and easy to verify.
- Use relative paths when referencing repository files from Markdown.

## Spec Guidance

- `requirements.md` should describe what must be true and should use EARS-style requirements where practical.
- `design.md` should explain how the requirements will be satisfied, including architecture, interactions, and tradeoffs.
- `tasks.md` should break work into concrete implementation steps that can be executed and verified.

## Feature Spec Guidance

- Use a feature spec for complex features with multiple implementation tasks.
- Do not force small bug fixes or exploratory spikes into a feature spec unless the work needs structured planning.
- Support both valid flows:
  - Requirements-first: start with behavior, then design, then tasks.
  - Design-first: start with technical design, then derive feasible requirements, then tasks.
- Keep all three files present in each feature spec even when the work starts from design.

## EARS Guidance

- Prefer requirement statements in the form `WHEN <condition> THE SYSTEM SHALL <behavior>`.
- Keep requirements specific enough to be testable.
- Split separate behaviors into separate requirement statements.
