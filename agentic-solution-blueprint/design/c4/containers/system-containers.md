# System Containers

## Purpose

Define container boundaries and contracts at the next abstraction level below system.

## Summary

The PetShop Web system consists of 5 containers:
- **petshop-api**: .NET 8 ASP.NET Core Web API (executable service)
- **petshop-web**: React 18 SPA with TypeScript (executable application)
- **petshop-db**: PostgreSQL 16 database (data store)
- **petshop-cache**: Redis 7 cache (data store)
- **petshop-queue**: RabbitMQ 3.13 message broker (broker)

## Architecture decisions

### AD-C001: API as Single Entry Point

**Decision**: All frontend-to-backend communication goes through petshop-api. No direct database access from the frontend.

**Rationale**: Security, centralized authentication, and consistent API contracts.

### AD-C002: Database per System

**Decision**: All bounded contexts share a single PostgreSQL database with schema-per-context separation.

**Rationale**: Simplifies v1 deployment; schemas provide logical separation. Split to separate databases only if bounded contexts require independent scaling or deployment.

### AD-C003: Redis for Caching Layer

**Decision**: Redis serves as the caching layer for catalog data and session storage.

**Rationale**: Reduces database load for read-heavy catalog queries; provides fast session storage.

### AD-C004: RabbitMQ for Async Processing

**Decision**: RabbitMQ handles async order processing (email delivery, inventory updates).

**Rationale**: Decouples order placement from side effects; enables retry and dead-letter handling.

## Contained containers

| Container | Type | Technology | Responsibility |
| --- | --- | --- | --- |
| petshop-api | Service | .NET 8 ASP.NET Core | REST API for all bounded contexts |
| petshop-web | Application | React 18 + TypeScript | Customer-facing web application |
| petshop-db | Data Store | PostgreSQL 16 | Persistent data storage |
| petshop-cache | Data Store | Redis 7 | Caching and session storage |
| petshop-queue | Broker | RabbitMQ 3.13 | Async message processing |

## Interactions

| From | To | Protocol | Direction | Description |
| --- | --- | --- | --- | --- |
| petshop-web | petshop-api | HTTPS/JSON + JWT | Request/Response | REST API calls for all operations |
| petshop-api | petshop-db | TCP/Npgsql | Request/Response | EF Core database access |
| petshop-api | petshop-cache | TCP/Redis Protocol | Request/Response | Cache reads/writes, session storage |
| petshop-api | petshop-queue | AMQP 0-9-1 | Publish/Subscribe | Async order events |
| petshop-api | Payment Processor | HTTPS/JSON | Request/Response | Payment intent creation |
| petshop-queue | Email Service | HTTPS/JSON | Request/Response | Email delivery (via consumer) |

## Diagrams

### Container Diagram

```
┌──────────────────────────────────────────────────────────────────────┐
│                        PetShop Web System                            │
│                                                                      │
│  ┌──────────────┐                    ┌──────────────────────────┐   │
│  │              │    HTTPS/JSON      │                          │   │
│  │  petshop-    │ ──────────────────▶│     petshop-api          │   │
│  │  web         │    JWT Bearer      │  (.NET 8 ASP.NET Core)   │   │
│  │  (React 18)  │                    │                          │   │
│  │              │                    │ ┌──────────────────────┐ │   │
│  └──────────────┘                    │ │ Bounded Contexts:    │ │   │
│                                      │ │ • Catalog            │ │   │
│                                      │ │ • Orders             │ │   │
│                                      │ │ • Users              │ │   │
│                                      │ │ • Auth               │ │   │
│                                      │ │ • Cart               │ │   │
│                                      │ └──────────────────────┘ │   │
│                                      └──────────┬───────────────┘   │
│                                                 │                    │
│                    ┌────────────────────────────┼────────────┐      │
│                    │                            │            │      │
│           ┌────────▼────────┐   ┌──────────────▼──────┐  ┌───▼────┐ │
│           │  petshop-db     │   │   petshop-cache     │  │petshop │ │
│           │  (PostgreSQL 16)│   │   (Redis 7)         │  │-queue  │ │
│           │                 │   │                     │  │(Rabbit │ │
│           │  Schema: catalog│   │  Catalog cache      │  │ MQ 3.13)│ │
│           │  Schema: orders │   │  Session store      │  │        │ │
│           │  Schema: users  │   │                     │  │ Exch:  │ │
│           │  Schema: auth   │   └─────────────────────┘  │ order. │ │
│           └─────────────────┘                              │ events│ │
│                                                            └────────┘ │
└──────────────────────────────────────────────────────────────────────┘
```

### Contract: petshop-web ↔ petshop-api

| Contract | Type | Protocol | Payload | Direction |
| --- | --- | --- | --- | --- |
| Catalog API | REST | HTTPS/JSON | Product query/response | bidirectional |
| Cart API | REST | HTTPS/JSON | Cart item query/response | bidirectional |
| Order API | REST | HTTPS/JSON | Order command/response | bidirectional |
| Auth API | REST | HTTPS/JSON | Auth token request/response | bidirectional |
| User API | REST | HTTPS/JSON | User profile query/response | bidirectional |

### Contract: petshop-api ↔ petshop-db

| Contract | Type | Protocol | Payload | Direction |
| --- | --- | --- | --- | --- |
| Data Access | EF Core | Npgsql | Entity queries/results | bidirectional |
| Migrations | EF Core CLI | Command | Migration scripts | unidirectional (dev) |

### Contract: petshop-api ↔ petshop-cache

| Contract | Type | Protocol | Payload | Direction |
| --- | --- | --- | --- | --- |
| Catalog Cache | Redis | TCP/RESP | Product list cache (JSON) | bidirectional |
| Session Store | Redis | TCP/RESP | Session data (JSON) | bidirectional |
| Rate Limiter | Redis | TCP/RESP | Counter keys | bidirectional |

### Contract: petshop-api ↔ petshop-queue

| Contract | Type | Protocol | Payload | Direction |
| --- | --- | --- | --- | --- |
| Order Events | AMQP | RabbitMQ | OrderPlaced, OrderConfirmed | petshop-api → queue |
| Email Jobs | AMQP | RabbitMQ | EmailRequest | queue → email consumer |
| Inventory Updates | AMQP | RabbitMQ | InventoryAdjustment | queue → inventory consumer |

## Domain and microservice decomposition (tree view)

```
PetShop Web
├── petshop-api (service)
│   ├── Catalog (bounded context)
│   ├── Orders (bounded context)
│   ├── Users (bounded context)
│   ├── Auth (bounded context)
│   └── Cart (bounded context)
├── petshop-web (application)
│   ├── Catalog Pages
│   ├── Cart Pages
│   ├── Order Pages
│   └── Auth Pages
├── petshop-db (data-store)
│   ├── schema: catalog
│   ├── schema: orders
│   ├── schema: users
│   └── schema: auth
├── petshop-cache (data-store)
│   ├── catalog:product-lists
│   ├── catalog:products:{id}
│   └── session:{token}
└── petshop-queue (broker)
    ├── exchange: order.events
    │   ├── queue: order.confirmation.email
    │   └── queue: order.inventory.update
    └── exchange: email.events
        └── queue: email.delivery
```

## Next level

See individual container documents for component decomposition:
- [petshop-api container](containers/petshop-api/container.md)
- [petshop-web container](containers/petshop-web/container.md)
