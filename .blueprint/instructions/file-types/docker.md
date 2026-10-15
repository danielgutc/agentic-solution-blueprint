# Docker Files

## Rules

- Keep one clear runtime responsibility per image.
- Use explicit, supportable base-image versions and follow the project's update policy.
- Use multi-stage builds when build tooling is unnecessary at runtime.
- Keep images minimal, non-root where practical, and free of secrets or machine-specific values.
- Preserve layer caching without obscuring dependency or build behavior.
- Add health behavior only when it reflects the application's real readiness semantics.
- Keep service-local image build assets with the owning implementation unit. Keep multi-service composition and environment topology under the registered deployment path.
- Treat an image workspace and a C4 container as separate decisions: record their mapping, and do not create a source directory for an unchanged stock or managed image.
- Validate builds locally through a repository-owned command and in CI.

Reflect changes that affect developer workflow, runtime boundaries, packaging, or deployment in the relevant foundation and C4 artifacts.
