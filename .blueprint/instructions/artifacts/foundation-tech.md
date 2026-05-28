# Foundation Artifact: tech.md

## Purpose

Record enduring technical direction, constraints, and key platform choices.

## Canonical structure

- Use `.blueprint/templates/foundation/tech.template.md`.

## Authoring rules

- Focus on lasting technical choices, not sprint-level tasks.
- Capture rationale for major technology decisions.
- Keep constraints explicit when they shape architecture boundaries.
- Record the default packaging and deployment/orchestration model in the deployment section.
- Default executable backend services to container images orchestrated by Kubernetes unless a project records a different approved choice and rationale.

## Quality checklist

- Chosen runtime/platform stack is explicit.
- Default deployment/orchestration platform and local development approach are explicit.
- Technical constraints are actionable.
- Key decisions are traceable to business or architecture needs.
