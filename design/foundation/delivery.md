# Delivery

[README](../../README.md) / Foundation / Delivery governance

Related foundation documents:
- [Product](./product.md)
- [MVP and prioritization](./mvp.md)
- [Requirements](./requirements.md)
- [Tech](./tech.md)
- [Design](./design.md)
- [Traceability matrix](./traceability-matrix.md)
- [Task tracker](./task.md)
- [Implementation readiness](./implementation-readiness.md)

## Table of contents

- [Purpose and scope](#purpose-and-scope)
- [Delivery flow](#delivery-flow)
- [Project delivery decisions](#project-delivery-decisions)
- [Pipeline stage contracts](#pipeline-stage-contracts)
- [Test execution matrix](#test-execution-matrix)
- [Artifact and promotion model](#artifact-and-promotion-model)
- [Documentation and generated artifacts](#documentation-and-generated-artifacts)
- [Trust and security boundaries](#trust-and-security-boundaries)
- [Evidence and retention](#evidence-and-retention)
- [Failure handling, rollback, and recovery](#failure-handling-rollback-and-recovery)
- [Exceptions](#exceptions)
- [Open decisions](#open-decisions)

## Purpose and scope

## Delivery flow

Describe the approved path from local feedback through validation, packaging, non-production delivery, and promotion. When the flow is approved, store its `.drawio` source and sibling `.svg` export in [_diagrams](./_diagrams/README.md), then embed the SVG and link the source here.

## Project delivery decisions

- Selected orchestration:
- Artifact registry:
- Deployment and promotion approach:
- Local developer entry point:
- Branch and repository governance:

## Pipeline stage contracts

| Stage | Trigger | Repository command(s) | Required result | Evidence | Trust level | Blocking behavior |
| --- | --- | --- | --- | --- | --- | --- |
| Local feedback | | | | | Developer workstation | Advisory |
| Pull request | | | | | Untrusted proposed change | |
| Trusted main | | | | | Trusted source state | |
| Non-production delivery | | | | | Deployment environment | |
| Promotion | | | | | Protected environment | |
| Scheduled assurance | | | | | Declared per job | |

## Test execution matrix

| Test level | Local | Pull request | Trusted main | Non-production | Promotion | Scheduled |
| --- | --- | --- | --- | --- | --- | --- |
| Unit | | | | | | |
| Component | | | | | | |
| Contract/API | | | | | | |
| Service integration | | | | | | |
| Cross-service | | | | | | |
| End-to-end | | | | | | |
| Deployment smoke | | | | | | |

## Artifact and promotion model

## Documentation and generated artifacts

## Trust and security boundaries

## Evidence and retention

## Failure handling, rollback, and recovery

## Exceptions

| ID | Scope | Rationale | Owner | Compensating evidence | Expiry or trigger | Status |
| --- | --- | --- | --- | --- | --- | --- |

## Open decisions
