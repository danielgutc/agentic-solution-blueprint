# CI/CD Files

## Rules

- Express pipeline stages through stable repository-owned commands recorded in `design/foundation/tech.md`.
- Keep provider-specific workflow files focused on orchestration, permissions, caching, artifact transfer, and environment integration.
- Pin or constrain external actions and tools according to the project's supply-chain policy.
- Separate untrusted pull-request validation from trusted packaging and deployment.
- Grant each job the minimum permissions it needs.
- Never place credentials in definitions, generated documentation, logs, or committed configuration.
- Preserve actionable test, analysis, documentation, package, deployment, and provenance evidence.
- Apply concurrency, retry, timeout, and cancellation behavior deliberately.
- Validate syntax and safe non-deployment paths before activating external mutations.

Follow `../process/delivery-foundation.md` for readiness capability and `../artifacts/delivery.md` for project-specific stage contracts.
