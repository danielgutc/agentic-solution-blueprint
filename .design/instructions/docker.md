# Docker Files Instructions

## Purpose

Use Docker files to provide reproducible local development and automation environments.

## Rules

- Keep Docker files focused on one responsibility per image.
- Prefer explicit version tags for base images.
- Minimize image size by avoiding unnecessary packages and build steps.
- Use multi-stage builds when compile-time tooling is not needed at runtime.
- Keep secrets and machine-specific values out of Docker files.

## Conventions

- Name files according to purpose, such as `Dockerfile`, `Dockerfile.dev`, or `docker-compose.yml` when we introduce them.
- Group related environment setup commands to keep layer caching effective.
- Add brief comments only when a step is non-obvious or has an important tradeoff.

## Validation

- Build definitions should be easy to run locally.
- Changes to Docker files should be reflected in the relevant spec or task when they affect developer workflow.
