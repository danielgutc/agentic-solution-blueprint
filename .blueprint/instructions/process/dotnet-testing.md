# .NET Testing Instructions

## Purpose

Define testing guidance for runtime implementation using a test-driven, interface-driven style.

## Authoritative references

- Unit testing best practices (.NET):
  - https://learn.microsoft.com/en-us/dotnet/core/testing/unit-testing-best-practices
- ASP.NET Core integration testing:
  - https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests?view=aspnetcore-9.0

## Core rules

- Write tests before internal implementation for new behavior.
- Derive tests from approved contract obligations before private implementation details.
- Keep unit tests isolated, fast, repeatable, and self-checking.
- Avoid infrastructure dependencies in unit tests.
- Use component tests for cross-component behavior with external systems mocked.
- Keep test names explicit about method, scenario, and expected behavior.
- Test contract behavior, not private implementation details.
- For executable ASP.NET Core APIs, integration-test `/health` and Development-only OpenAPI/Swagger UI endpoints when those development surfaces are part of the scaffold convention.
- For .NET implementation components, fail validation if generated `bin/` or `obj/` directories exist under `src/` or `tests/`; generated build output is allowed only at the implementation component root.
- Avoid control-flow-heavy logic inside tests; keep test logic simple and explicit.
- Prefer Arrange/Act/Assert structure for readability and consistency.
- Keep unit and component tests in separate projects or folders when practical to preserve test intent.

## Mocking boundaries

- Mock external services, network calls, storage engines, and process boundaries in component tests unless a dedicated integration environment is explicitly required.
- Keep deterministic test doubles and avoid hidden shared state.
- Prefer explicit dependency injection seams to enable stable mocks and fakes.

## Test naming convention

- Default pattern:
  - `<MethodOrBehavior>_<Scenario>_<ExpectedOutcome>`
- Use names that communicate behavior intent without requiring test-body inspection.

## Enforcement guidance

- Enforce test execution in CI with deterministic ordering assumptions removed.
- Keep flaky-test budget at zero for unit and component test suites.
- Use coverage as a signal, not as a sole quality gate.

## Implementation gate alignment

- Follow implementation gates from:
  - `.blueprint/instructions/process/approval-gates.md`
  - `.blueprint/instructions/process/implementation-interface-test-first.md`
