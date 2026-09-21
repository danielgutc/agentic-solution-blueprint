# Integrated Verification

## Timing and ownership

The test engineer may design integrated scenarios once contracts and acceptance intent are stable, in parallel with authorized implementation. The integrated-verification phase closes only when assembled behavior has executable evidence. Native unit, component, and initial contract tests already run before implementation readiness.

## Blueprint obligations

- Map approved functional requirements and public contracts to test evidence in `design/foundation/traceability-matrix.md`, or record an owned gap.
- Verify important cross-component and external boundaries, primary workflows, and deployment health at the lowest level that exercises the real risk.
- Record where each applicable test level runs in `design/foundation/delivery.md`: local feedback, pull request, trusted main, deployed development, promotion, or scheduled assurance.
- Keep developer-close unit and component tests in the selected stack's native framework; do not replace them with slower black-box suites.
- Choose Robot Framework, browser tooling, or an equivalent only when project-approved and useful for the relevant black-box or UI scenarios. No framework is mandated by this blueprint.
- Missing applicable coverage blocks the corresponding gate unless an approved, expiring exception names compensating verification.

Use the toolkit's `integration-e2e-testing` skill when available for scenario design, execution, diagnosis, and reporting. This file records the repository's timing and evidence obligations.
