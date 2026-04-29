# Implementation Artifact: interface-driven, test-first flow

## Purpose

Define the runtime implementation flow after C4 code phase 2 approval using a test-first, interface-driven style.

## Prerequisite

- C4 code phase 2 must be explicitly approved for the target container/component scope.

## Implementation phases

- Phase 1: Interface-driven implementation skeletons
  - apply approved C4 contracts/interfaces in runtime code
  - create component and class skeletons
  - wire dependency boundaries from approved APIs/dependencies
  - document implementation extensions needed because C4 abstraction was higher
- Phase 2: Tests first
  - define and implement unit tests against behavior contracts
  - define and implement component tests with external systems mocked
  - keep tests as executable behavior specifications before internals
- Phase 3: Internal implementation
  - implement internals to satisfy approved tests and contracts
  - preserve dependency boundaries and explicit contracts

## Approval gates

- Gate 1: implementation interfaces approved
- Gate 2: implementation tests approved
- Gate 3: implementation internals approved

## Change-control rule

- If runtime implementation introduces architecture drift, update relevant C4 artifacts and re-approve before continuing implementation.
