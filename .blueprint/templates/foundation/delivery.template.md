# Delivery

## Purpose and scope

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
