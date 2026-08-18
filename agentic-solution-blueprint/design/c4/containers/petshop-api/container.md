# petshop-api

## Purpose

.NET 8 ASP.NET Core Web API that provides RESTful services for all PetShop bounded contexts (Catalog, Orders, Users, Auth, Cart).

## Technology

- **Runtime**: .NET 8 (ASP.NET Core 8)
- **ORM**: Entity Framework Core 8
- **CQRS**: MediatR
- **Validation**: FluentValidation
- **API Docs**: Swashbuckle (OpenAPI/Swagger)
- **Logging**: Serilog
- **Database**: Npgsql (PostgreSQL)
- **Cache**: StackExchange.Redis
- **Messaging**: RabbitMQ.Client
- **Auth**: ASP.NET Core Identity + JWT Bearer

## Responsibilities

- Expose RESTful HTTP APIs for all bounded contexts.
- Handle authentication and authorization (JWT).
- Manage database access via EF Core.
- Handle caching via Redis.
- Publish and consume messages via RabbitMQ.
- Validate input and enforce business rules.
- Return standardized error responses.

## Layered component model

```
petshop-api
├── PetShop.Api (web host / entry point)
│   ├── Controllers (HTTP endpoints)
│   ├── Middleware (auth, error handling, logging)
│   └── Program.cs (DI, configuration)
├── PetShop.Catalog (bounded context)
│   ├── Catalog.Api (catalog endpoints)
│   ├── Catalog.Domain (entities, value objects)
│   ├── Catalog.Application (commands, queries)
│   └── Catalog.Infrastructure (EF Core, Redis cache)
├── PetShop.Orders (bounded context)
│   ├── Orders.Api (order endpoints)
│   ├── Orders.Domain (entities, value objects)
│   ├── Orders.Application (commands, queries)
│   └── Orders.Infrastructure (EF Core, RabbitMQ)
├── PetShop.Users (bounded context)
│   ├── Users.Api (user endpoints)
│   ├── Users.Domain (entities, value objects)
│   ├── Users.Application (commands, queries)
│   └── Users.Infrastructure (EF Core)
├── PetShop.Auth (bounded context)
│   ├── Auth.Api (auth endpoints)
│   ├── Auth.Domain (entities, value objects)
│   ├── Auth.Application (commands, queries)
│   └── Auth.Infrastructure (JWT, password hashing)
└── PetShop.Shared (cross-cutting)
    ├── Domain (shared entities, base types)
    ├── Application (shared services, intermediaries)
    └── Infrastructure (shared utilities)
```

## Contracts

### Inbound Contracts (API endpoints)

| Endpoint | Method | Auth | Description |
| --- | --- | --- | --- |
| `/api/catalog/products` | GET | None | Browse/search products |
| `/api/catalog/products/{id}` | GET | None | Get product detail |
| `/api/catalog/categories` | GET | None | List categories |
| `/api/catalog/products` | POST | Admin | Create product |
| `/api/catalog/products/{id}` | PUT | Admin | Update product |
| `/api/catalog/products/{id}` | DELETE | Admin | Delete product |
| `/api/cart` | GET | Customer | Get current cart |
| `/api/cart/items` | POST | Customer | Add item to cart |
| `/api/cart/items/{itemId}` | PUT | Customer | Update cart item |
| `/api/cart/items/{itemId}` | DELETE | Customer | Remove cart item |
| `/api/cart/clear` | DELETE | Customer | Clear cart |
| `/api/orders` | POST | Customer | Place order |
| `/api/orders` | GET | Customer | List user orders |
| `/api/orders/{id}` | GET | Customer/Admin | Get order detail |
| `/api/orders/{id}` | PUT | Admin | Update order status |
| `/api/auth/register` | POST | None | Register user |
| `/api/auth/login` | POST | None | Login (get JWT) |
| `/api/auth/refresh` | POST | None | Refresh JWT |
| `/api/auth/logout` | POST | Customer | Logout |
| `/api/users/profile` | GET | Customer | Get user profile |
| `/api/users/profile` | PUT | Customer | Update user profile |
| `/health` | GET | None | Health check |
| `/swagger` | GET | None | Swagger UI (Dev only) |

### Outbound Contracts

| Contract | Target | Protocol | Description |
| --- | --- | --- | --- |
| Catalog Cache | petshop-cache | Redis | Product catalog caching |
| Order Events | petshop-queue | AMQP | Publish order events |
| Payment Intent | Payment Processor | HTTPS | Create payment intent |
| Email Delivery | Email Service | HTTPS | Send confirmation email |

## Dependencies

| Dependency | Type | Direction |
| --- | --- | --- |
| petshop-db | Data Store | petshop-api → petshop-db |
| petshop-cache | Data Store | petshop-api → petshop-cache |
| petshop-queue | Broker | petshop-api → petshop-queue |
| Payment Processor | External | petshop-api → external |
| Email Service | External | petshop-api → external |

## Boundaries

- Each bounded context owns its database schema.
- Cross-context communication via messages (RabbitMQ), not direct database access.
- API surface is the only external entry point; no direct database access from frontend.
- Authentication is centralized in Auth context; other contexts validate JWT claims.

## Contained components

### Catalog
- **Catalog.Api** — REST endpoints for product/category CRUD and search.
- **Catalog.Domain** — Product, Category, Inventory entities and value objects.
- **Catalog.Application** — Commands (CreateProduct, UpdateProduct), Queries (GetProducts, GetProductById).
- **Catalog.Infrastructure** — EF Core DbContext, repository implementations, Redis cache service.

### Orders
- **Orders.Api** — REST endpoints for order placement and management.
- **Orders.Domain** — Order, OrderItem, Payment entities and value objects.
- **Orders.Application** — Commands (PlaceOrder, UpdateOrderStatus), Queries (GetOrders, GetOrderById).
- **Orders.Infrastructure** — EF Core DbContext, repository implementations, RabbitMQ publisher.

### Users
- **Users.Api** — REST endpoints for user profile management.
- **Users.Domain** — User entity.
- **Users.Application** — Commands (UpdateProfile), Queries (GetProfile).
- **Users.Infrastructure** — EF Core DbContext, repository implementations.

### Auth
- **Auth.Api** — REST endpoints for register, login, refresh, logout.
- **Auth.Domain** — UserCredentials entity.
- **Auth.Application** — Commands (RegisterUser, LoginUser, RefreshToken), Queries (ValidateToken).
- **Auth.Infrastructure** — JWT token service, bcrypt password hasher.

### Shared
- **Shared.Domain** — Base entity types, value objects, domain exceptions.
- **Shared.Application** — Shared services (email, logging, validation).
- **Shared.Infrastructure** — Shared utilities (error handling middleware, Serilog configuration).

## Approval gate

- Container design: **Approved** (this document).
- Components design: **Approved** (above decomposition).
- Interfaces diagram: See contract tables above.
- Code phase 1 (contracts): **Pending**.
- Code phase 2 (class or domain design): **Pending**.

## Diagrams

### Component Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                          petshop-api                                │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    PetShop.Api (Web Host)                   │   │
│  │  Program.cs │ DI │ Middleware │ Health Check               │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│         ┌────────────────────┼────────────────────┐                │
│         │                    │                    │                │
│  ┌──────▼──────┐   ┌────────▼────────┐   ┌───────▼───────┐       │
│  │  Catalog    │   │    Orders       │   │     Auth      │       │
│  │  Context    │   │    Context      │   │    Context    │       │
│  │ ┌─────────┐ │   │ ┌───────────┐   │   │ ┌───────────┐ │       │
│  │ │ .Api    │ │   │ │ .Api      │   │   │ │ .Api      │ │       │
│  │ │ .Domain │ │   │ │ .Domain   │   │   │ │ .Domain   │ │       │
│  │ │ .App    │ │   │ │ .App      │   │   │ │ .App      │ │       │
│  │ │ .Infra  │ │   │ │ .Infra    │   │   │ │ .Infra    │ │       │
│  │ └─────────┘ │   │ └───────────┘   │   │ └───────────┘ │       │
│  └─────────────┘   └─────────────────┘   └───────────────┘       │
│         │                    │                    │                │
│         └────────────────────┼────────────────────┘                │
│                              │                                      │
│                   ┌──────────▼──────────┐                          │
│                   │     Users           │                          │
│                   │     Context         │                          │
│                   │ ┌─────────────────┐ │                          │
│                   │ │ .Api │ .Domain  │ │                          │
│                   │ │ .App │ .Infra   │ │                          │
│                   │ └─────────────────┘ │                          │
│                   └──────────┬──────────┘                          │
│                              │                                      │
│                   ┌──────────▼──────────┐                          │
│                   │      Cart           │                          │
│                   │     Context         │                          │
│                   │ ┌─────────────────┐ │                          │
│                   │ │ .Api │ .Domain  │ │                          │
│                   │ │ .App │ .Infra   │ │                          │
│                   │ └─────────────────┘ │                          │
│                   └──────────┬──────────┘                          │
│                              │                                      │
│              ┌───────────────┼───────────────┐                     │
│              │               │               │                     │
│     ┌────────▼──┐   ┌───────▼──────┐   ┌───▼────────┐           │
│     │ petshop-  │   │ petshop-     │   │ petshop-   │           │
│     │ db        │   │ cache        │   │ queue      │           │
│     │ (PG)      │   │ (Redis)      │   │ (RabbitMQ) │           │
│     └───────────┘   └──────────────┘   └────────────┘           │
└─────────────────────────────────────────────────────────────────────┘
```
