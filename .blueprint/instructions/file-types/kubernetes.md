# Kubernetes Manifest Instructions

## Purpose

Use Kubernetes manifests as the default orchestration artifacts for executable backend services and supporting deployable dependencies.

## Rules

- Keep local-development manifests under `deployment/k8s/local/` unless a project documents a different layout.
- Define a `Deployment` and `Service` for each executable HTTP service introduced into implementation.
- Configure HTTP liveness and readiness probes through the service health endpoint, defaulting to `/health`.
- Set explicit container and service ports. Keep desktop port-forward examples in deployment documentation and runbooks, not in Kubernetes manifest annotations or labels.
- Reference service-specific Docker/OCI image tags that can be built locally and resolved by the selected Kubernetes runtime.
- For remote development clusters, image references must resolve to a registry or explicit image-import path reachable by the cluster runtime.
- Keep local manifests development-oriented; introduce production ingress, secret management, persistence, scaling, and security policy only when their design is approved.

## Conventions

- Prefer a namespace manifest and a `kustomization.yaml` for a coherent local stack.
- Keep one service deployment manifest per runtime component unless a shared manifest remains clearer.
- Prefer `imagePullPolicy: IfNotPresent` for development manifests that pull from a cluster-reachable registry.
- Use `imagePullPolicy: Never` only for an explicitly documented local-cluster workflow where the selected Kubernetes context consumes host-built images from the same image cache.
- Do not use `kubectl port-forward` as an image delivery mechanism. Port-forwarding is only for desktop access to already-running services.

## Validation

- Run `kubectl kustomize deployment/k8s/local` to validate renderability.
- Run `kubectl apply --dry-run=client -k deployment/k8s/local` when client-side validation is supported in the current environment.
- Build each referenced image definition when Docker is available.
