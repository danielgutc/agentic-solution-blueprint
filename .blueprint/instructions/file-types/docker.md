# Docker Files Instructions

## Purpose

Use Docker files to build reproducible OCI-compatible images consumed by Kubernetes-based local development and deployment environments.

## Rules

- Keep Docker files focused on one responsibility per image.
- Prefer explicit version tags for base images.
- Minimize image size by avoiding unnecessary packages and build steps.
- Use multi-stage builds when compile-time tooling is not needed at runtime.
- Keep secrets and machine-specific values out of Docker files.
- Keep container ports, health endpoints, and runtime environment expectations aligned with the Kubernetes manifests and `implementation/local-development.md`.

## Conventions

- Name image build files according to purpose, such as `Dockerfile` or `Dockerfile.dev`.
- Treat Kubernetes manifests as the default service orchestration artifacts; introduce Docker Compose only as an explicitly documented deviation or auxiliary workflow.
- Group related environment setup commands to keep layer caching effective.
- Add brief comments only when a step is non-obvious or has an important tradeoff.

## Validation

- Build definitions should be easy to run locally.
- Changes to Docker files should be reflected in the relevant foundation, design, or implementation artifacts when they affect developer workflow.
- Validate images against the matching Kubernetes deployment manifest when a service is deployable.
