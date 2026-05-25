# Local Development Endpoints

This document is the registry for stable local service bindings used during development and integration testing. Update it when a runtime service gains or changes a local endpoint.

## Service endpoints

| Service | Development URL | Health | API exploration | Notes |
| --- | --- | --- | --- | --- |
| `<service-name>` | `http://localhost:<port>` | `GET /health` | `GET /swagger`; `GET /openapi/v1.json` in Development only. | `<operational note>` |

## Conventions

- Allocate a stable, non-conflicting local URL for each executable service and record it in this registry.
- Keep health endpoints available at `/health` unless a documented operational constraint requires otherwise.
- For HTTP APIs, expose interactive Swagger UI and the OpenAPI document in `Development` only.
- Keep runtime service URLs in `Properties/launchSettings.json` aligned with this registry.
