# Foundation Artifact: delivery.md

## Purpose

Define reusable delivery-governance contracts and record solution-specific delivery selections before repository enforcement, artifact publication, or automated promotion is implemented.

## Canonical structure

- Use `.blueprint/templates/foundation/delivery.template.md`.

## Ownership boundary

- The blueprint owns reusable delivery semantics:
  - pipeline stage and quality-gate contracts
  - functional-test execution timing defaults
  - evidence and coverage expectations
  - adapter capability contracts
  - framework-agnostic tool guidance
  - exception, rollout, and extraction rules
- The solution owns executable delivery implementation:
  - selected orchestration and workflow files
  - selected adapters, tools, and versions
  - local developer entry points and automation tests
  - product and system tests
  - repository rules, ownership, credentials, and environment configuration
  - registry, deployment, and promotion configuration
- A separate shared automation implementation is optional. Extract it only after multiple solutions demonstrate meaningful duplication, contracts are stable, and independent versioning is justified.

## Authoring rules

- Keep reusable stage, gate, evidence, and adapter semantics technology-neutral.
- Record solution-specific technology selections and rationale in `design/foundation/tech.md` and reference them from `design/foundation/delivery.md`.
- Define which checks are advisory, locally blocking, merge blocking, deployment blocking, or promotion blocking.
- Define trust boundaries explicitly. Validation of untrusted proposed changes must not receive deployment authority.
- Build trusted artifacts once and promote the same immutable artifact when the selected stack supports it.
- Keep substantial deterministic logic in solution-owned portable automation rather than embedding it only in orchestration YAML or agent skills.
- Treat local checks as developer feedback and authoritative remote checks as enforcement.
- Record rollout steps so enforcement can be introduced and reverted incrementally.

## Functional test timing rule

- Map every applicable functional test level to its execution moments:
  - pre-commit
  - pre-push
  - pull request
  - merge queue, when used
  - trusted main build
  - deployed development
  - environment promotion
  - scheduled assurance
- Start from the defaults in `.blueprint/instructions/process/functional-testing-strategy.md`.
- Record justified deviations and any missing applicable coverage as explicit, owned, expiring exceptions.
- Collect native code and branch coverage during pull-request validation.
- Collect requirement, contract, and boundary coverage during pull-request validation.
- Collect workflow and deployment coverage from framework-agnostic and deployed functional tests after deployment.

## Framework-agnostic guidance

The blueprint may advise portable tools and formats without making them mandatory technology selections:

- Robot Framework for black-box API acceptance, cross-service workflows, deployment smoke, and end-to-end functional tests
- OPA/Conftest for policy-as-code evaluation
- JUnit-compatible test evidence
- SARIF static-analysis and security findings
- portable coverage formats
- CycloneDX or SPDX software bills of materials
- OCI-compatible provenance and attestation standards

Projects may select equivalent tools when they preserve the approved capability contract and evidence semantics.

## Quality checklist

- Blueprint and solution ownership are explicit.
- Pipeline stages declare triggers, required results, evidence, trust level, and blocking behavior.
- Functional test timing and coverage collection moments are explicit.
- Selected orchestration and adapters remain solution-owned and replaceable.
- Framework-agnostic guidance does not silently become a mandatory project selection.
- Branch, artifact, promotion, trust, exception, and rollback rules are explicit.
- Shared automation extraction has measurable triggers and is not treated as a prerequisite.
