# Delivery Governance

## Purpose

## Reusable pattern and solution ownership

| Boundary | Owns | Does not own |
| --- | --- | --- |
| Blueprint | Reusable stage, gate, evidence, coverage, adapter-capability, exception, rollout, and extraction contracts. | Selected orchestration, adapters, workflow files, credentials, tests, or environment state. |
| Solution | Selected orchestration, executable delivery automation, adapters and versions, tests, repository rules, environment configuration, and approved exceptions. | Reusable policy changes that should be upstreamed to the blueprint. |

## Project delivery decisions

- Selected orchestration:
- Selected artifact registry:
- Selected deployment/promotion approach:
- Local developer entry point:
- Branch and repository governance:
- Approved deviations and rationale:

## Pipeline stage contracts

| Stage | Trigger | Portable automation | Required result | Evidence | Trust level | Blocking behavior |
| --- | --- | --- | --- | --- | --- | --- |
| IDE or save | | | | | Developer workstation | Advisory |
| Pre-commit | | | | | Developer workstation | |
| Pre-push | | | | | Developer workstation | |
| Pull request | | | | | Untrusted proposed change | |
| Merge queue, if used | | | | | Untrusted combined change | |
| Trusted main build | | | | | Trusted source state | |
| Deployed development | | | | | Deployment environment | |
| Environment promotion | | | | | Protected environment | |
| Scheduled assurance | | | | | Declared per job | |

## Functional test execution matrix

`Required` means the applicable affected scope blocks the stage unless an approved, expiring exception exists.

| Test level | Pre-commit | Pre-push | Pull request | Merge queue | Trusted main | Deployed development | Promotion | Scheduled assurance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Unit functional | Fast affected subset | All affected | Required | Required or same-commit evidence | Optional rerun | No | No | Full regression |
| Component functional | No | Affected | Required | Required | Optional rerun | No | No | Full regression |
| API functional through native host | No | Affected APIs | Required | Required | Packaged API verification | Critical paths | Critical paths | Full regression |
| Service integration with real dependencies | No | Optional when practical | Required for affected services | Required | Verify built artifact | Required | Relevant integrations | Full regression |
| Framework-agnostic API acceptance | No | Optional targeted suite | Required when affected | Critical suite | Packaged artifact acceptance | Required | Required | Full regression |
| Framework-agnostic cross-service functional | No | Optional targeted suite | Required when an ephemeral affected stack is practical | Critical suite | No | Required | Required | Full regression |
| End-to-end functional | No | No | Critical affected workflows only | Critical workflows when practical | No | Critical workflows | Required before sensitive promotion | Full suite |
| Deployment smoke | No | No | Manifest and policy simulation only | No | Image startup smoke | Required | Required | Scheduled drift and readiness checks |

### Coverage timing

- Native code and branch coverage during pull-request validation:
- Requirement, contract, and boundary coverage during pull-request validation:
- Workflow and deployment coverage after deployment:
- Approved coverage exceptions:

## Quality gates and evidence

### Gate families

### Evidence formats and retention

### Stable gate identifiers and ownership

## Adapter capability model

| Capability | Required contract | Selected solution adapter and version |
| --- | --- | --- |
| Native build and developer-close tests | | |
| Framework-agnostic functional tests | | |
| Policy checks | | |
| Packaging and supply chain evidence | | |
| Deployment and smoke verification | | |
| Blueprint and documentation checks | | |

Framework-agnostic candidates may include Robot Framework, OPA/Conftest, JUnit, SARIF, portable coverage formats, CycloneDX/SPDX, and OCI-compatible provenance or attestations. Record actual project selections in `design/foundation/tech.md`.

## Branching and repository governance

## Artifact and promotion model

## Trust and security boundaries

## Skills and automation

## Exceptions and failure handling

## Incremental rollout

## Shared automation extraction triggers

- Meaningful duplication proven across multiple solutions:
- Stable capability and command contracts:
- Independent versioning and compatibility need:
- Ownership and support model:

## Open decisions
