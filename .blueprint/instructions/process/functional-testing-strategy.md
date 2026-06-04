# Functional Testing Strategy

## Purpose

Define the blueprint-level functional testing model across implementation stacks, service boundaries, deployed systems, and user/system workflows.

This strategy focuses on functional correctness. Performance, security, chaos, accessibility, and usability testing may be added by project-specific technical decisions, but they are not part of this default functional testing model.

## Testing levels

- Unit functional tests:
  - verify business rules, pure domain behavior, validators, mappers, and deterministic algorithms in isolation
  - use the selected stack's native test framework
  - avoid infrastructure, network, file-system, clock, and process dependencies unless those are the behavior under test
- Component functional tests:
  - verify one component/module through its public port or approved interface
  - keep external services, storage engines, brokers, and process boundaries mocked, faked, or substituted unless the test is explicitly promoted to integration
  - use the selected stack's native test framework
- API functional tests:
  - verify HTTP/gRPC/API contracts, request validation, authorization assumptions, status codes, response payloads, idempotency, and error semantics
  - use native API host tests for developer-close feedback, and/or Robot Framework for black-box acceptance
- Service integration functional tests:
  - verify one service with real owned dependencies where practical, such as relational databases, object stores, queues, or file stores
  - prefer disposable dependencies through Testcontainers, a test namespace, or equivalent isolated infrastructure
- Cross-service functional tests:
  - verify approved service-to-service workflows across running services using public contracts only
  - default to Robot Framework when the test should remain framework-agnostic and black-box
- End-to-end functional tests:
  - verify full user/system workflows through the real entry point, including UI, API, or external actor flows as applicable
  - default to Robot Framework for workflow orchestration; use Robot Browser/Playwright or equivalent libraries for browser UI flows
- Deployment smoke tests:
  - verify deployed functional readiness after rollout
  - cover health/readiness, API discovery, one minimal happy-path command/query, and any mandatory owned dependency check
  - default to Robot Framework for portable smoke suites; lightweight `kubectl` or shell checks may support cluster diagnostics

## Framework split

- Use native framework tests for developer-close feedback:
  - .NET: xUnit, NUnit, or MSTest plus ASP.NET Core test hosting where applicable
  - Unity: Unity Test Framework for edit-mode and play-mode functional behavior
  - other stacks: the selected stack's idiomatic unit/component test framework
- Use Robot Framework as the default framework-agnostic layer for:
  - black-box API functional acceptance
  - cross-service functional workflows
  - deployed smoke tests
  - end-to-end functional regression suites
  - browser/UI flows when paired with Robot Browser, Playwright, Selenium, or an approved equivalent
- Do not replace native unit/component suites with Robot Framework. Robot tests should answer whether the running system behaves correctly from the outside.

## Functional coverage model

- Requirement coverage:
  - every approved functional requirement maps to automated tests or an explicitly recorded manual verification gap
- Contract coverage:
  - every approved API, service port, component port, or handoff has tests for success, validation failure, and important failure modes
- Boundary coverage:
  - persistence, file/object storage, external service, process, and messaging boundaries have at least one functional test or deployed smoke check at the appropriate level
- Workflow coverage:
  - primary business workflows have at least one happy-path test and representative negative-path tests
- Deployment coverage:
  - each deployed executable service has smoke coverage for health/readiness and one minimal functional operation when the operation exists
- Code/branch coverage:
  - use code and branch coverage as engineering signals for native unit/component tests, not as the sole quality gate
  - set numeric thresholds only when the project can keep them meaningful without encouraging low-value assertions

## Gate alignment

- Implementation phase 2 must define the native unit/component/API tests needed to prove approved contracts before internals.
- Robot Framework suites may be added during phase 2 when black-box acceptance criteria or deployed smoke behavior is already stable.
- Implementation phase 3 must satisfy the approved native tests and preserve or add Robot tests for externally visible behavior that becomes executable.
- A phase cannot be considered complete when the relevant functional coverage is missing, unless the gap is explicitly tracked in `design/foundation/task.md`.

## Artifact guidance

- Record project-specific framework choices in `design/foundation/tech.md`.
- Record deferred functional coverage gaps in `design/foundation/task.md`.
- Keep test cases close to the implementation or deployment surface they validate:
  - native tests under the relevant implementation test project/folder
  - Robot suites under a deployment, tests, or system-level acceptance test folder chosen by the project
