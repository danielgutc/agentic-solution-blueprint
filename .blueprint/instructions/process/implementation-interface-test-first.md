# Implementation process: interface-driven, test-first flow

## Purpose

Define the runtime implementation flow after C4 code phase 2 approval using a test-first, interface-driven, Design by Contract style.

## Prerequisite

- C4 code phase 2 must be explicitly approved for the target container/component scope.

## Implementation phases

- Phase 1: Interface-driven implementation skeletons
  - apply approved C4 contracts/interfaces in runtime code
  - create component and class skeletons
  - wire dependency boundaries from approved APIs/dependencies
  - document implementation extensions needed because C4 abstraction was higher
  - for executable HTTP APIs, allocate a stable local development URL and record it in `deployment/local-development.md`
  - for executable HTTP APIs, expose the generated OpenAPI document and interactive Swagger UI in the `Development` environment only
  - for executable backend services, add Docker/OCI image build assets and Kubernetes local-development manifests unless an approved technical decision records another deployment model
  - follow `.blueprint/instructions/standards/design-by-contract.md`
- Phase 2: Tests first
  - define and implement unit tests against contract preconditions, postconditions, invariants, and failure semantics
  - define and implement component tests with external systems mocked
  - for executable HTTP APIs, verify health and Development-only OpenAPI/Swagger UI availability through integration tests
  - keep tests as executable contract specifications before internals
- Phase 3: Internal implementation
  - implement internals to satisfy approved tests and contracts
  - preserve dependency boundaries and explicit contracts

## Approval gates

- Gate 1: implementation interfaces approved
- Gate 2: implementation tests approved
- Gate 3: implementation internals approved

## Change-control rule

- If runtime implementation introduces architecture drift, update relevant C4 artifacts and re-approve before continuing implementation.
