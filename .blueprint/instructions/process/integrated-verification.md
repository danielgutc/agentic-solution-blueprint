# Integrated Verification

## Test levels

- Unit: isolated domain behavior, validation, mapping, and deterministic algorithms using the stack's native framework.
- Component: one component through its public port with external systems substituted.
- Contract/API: public requests, responses, validation, authorization, idempotency, compatibility, and failure semantics.
- Service integration: one service with real owned dependencies where practical, preferably disposable or isolated.
- Cross-service: public-contract workflows across running services.
- End-to-end: complete user or system workflows through the real entry point.
- Deployment smoke: health, readiness, API discovery, a minimal functional operation, and mandatory dependency checks.

## Framework split

- Keep developer-close unit and component tests in the stack's native framework.
- Use Robot Framework or an approved equivalent for framework-agnostic black-box acceptance, cross-service, smoke, and end-to-end suites.
- Use Playwright, Robot Browser, Selenium, or an approved equivalent for browser flows.
- Do not replace fast native tests with slower black-box suites.

## Coverage model

- Every approved functional requirement maps to automated evidence or an explicit owned gap.
- Every public contract covers success, validation failure, and important failure modes.
- Every important persistence, messaging, file, process, and external-service boundary has verification at the appropriate level.
- Every primary workflow has a happy path and representative negative paths.
- Treat numeric code coverage as a signal, not a substitute for requirement, contract, boundary, and workflow coverage.

## Delivery alignment

Record where each applicable level runs in `design/foundation/delivery.md`: local feedback, pull request, trusted main, deployed development, promotion, or scheduled assurance. Missing applicable coverage blocks the corresponding gate unless an approved, expiring exception names compensating verification.
