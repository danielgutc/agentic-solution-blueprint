# Kubernetes Manifest Instructions

## Purpose

Use Kubernetes manifests as the default orchestration artifacts for executable backend services and supporting deployable dependencies.

## Rules

- Keep local-development manifests under `deployment/k8s/local/` unless a project documents a different layout.
- Define a `Deployment` and `Service` for each executable HTTP service introduced into implementation.
- Configure HTTP liveness and readiness probes through the service health endpoint, defaulting to `/health`.
- Set explicit container ports and keep port-forward examples aligned with `deployment/local-development.md`.
- Reference service-specific Docker/OCI image tags that can be built locally.
- Keep local manifests development-oriented; introduce production ingress, secret management, persistence, scaling, and security policy only when their design is approved.

## Conventions

- Prefer a namespace manifest and a `kustomization.yaml` for a coherent local stack.
- Keep one service deployment manifest per runtime component unless a shared manifest remains clearer.
- Use `imagePullPolicy: Never` for local-only images when the selected local cluster consumes host-built images.

## Validation

- Run `kubectl kustomize deployment/k8s/local` to validate renderability.
- Run `kubectl apply --dry-run=client -k deployment/k8s/local` when client-side validation is supported in the current environment.
- Build each referenced image definition when Docker is available.
