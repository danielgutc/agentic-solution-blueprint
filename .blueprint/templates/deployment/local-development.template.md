# Local Development Endpoints

This document is the registry for stable local service bindings used during development and integration testing. Update it when a runtime service gains or changes a local endpoint.

Port-forwarding is only for desktop/client access to already-running service endpoints. Project-built service images must be delivered through a registry or explicit image import path reachable by the selected Kubernetes cluster runtime.

## Service endpoints

| Service | Development URL | Kubernetes access | Health | API exploration | Notes |
| --- | --- | --- | --- | --- | --- |
| `<service-name>` | `http://localhost:<port>` | `kubectl -n <namespace> port-forward service/<service-name> <port>:80` | `GET /health` | `GET /swagger`; `GET /openapi/v1.json` in Development only. | `<operational note>` |

## Conventions

- Allocate a stable, non-conflicting local URL for each executable service and record it in this registry.
- Keep health endpoints available at `/health` unless a documented operational constraint requires otherwise.
- For HTTP APIs, expose interactive Swagger UI and the OpenAPI document in `Development` only.
- Keep runtime service URLs in `Properties/launchSettings.json` aligned with this registry.
- Keep local Kubernetes `Service` port-forward mappings aligned with this registry and operational runbooks.
- Do not use port-forwarding as an image registry path. Remote Kubernetes clusters pull images from registries or cluster-runtime image imports, not from desktop service port-forwards.
