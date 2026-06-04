# Foundation Artifact: tech.md

## Purpose

Record enduring technical direction, constraints, and key platform choices.

## Canonical structure

- Use `.blueprint/templates/foundation/tech.template.md`.

## Authoring rules

- Focus on lasting technical choices, not sprint-level tasks.
- Capture rationale for major technology decisions.
- Keep constraints explicit when they shape architecture boundaries.
- Record selected framework facilities that should shape code-level design, such as dependency injection, request handling, validation, configuration/options, background work, persistence, messaging, integration clients, observability, and testing conventions.
- In testing guidance, record the functional testing levels, native test frameworks, Robot Framework usage for framework-agnostic black-box suites, real-dependency strategy, and functional coverage expectations.
- Keep framework-facility guidance business-case agnostic; describe the selected stack capabilities and architectural implications, not project-domain behavior.
- In persistence guidance, record whether physical data stores are dedicated or shared, who owns schemas/namespaces/folders/buckets/prefixes, where migrations/provisioning live, how access is enforced, how local/prototype stores emulate production boundaries, and which target engine/runtime capabilities are required.
- Record the default packaging and deployment/orchestration model in the deployment section.
- Default executable backend services to container images orchestrated by Kubernetes unless a project records a different approved choice and rationale.

## Quality checklist

- Chosen runtime/platform stack is explicit.
- Selected framework facilities and code-design implications are explicit enough to guide C4 code phases.
- Functional testing strategy identifies native framework tests, Robot Framework black-box suites, and coverage expectations.
- Persistence access model identifies physical store sharing, schema/namespace/folder/bucket/prefix ownership, migration/provisioning ownership, and enforcement strategy.
- Default deployment/orchestration platform and local development approach are explicit.
- Technical constraints are actionable.
- Key decisions are traceable to business or architecture needs.
