# System

## Purpose

Define the software system boundary, actors, external systems, and major responsibilities for the PetShop Web application.

## Summary

PetShop Web is a two-tier web application (React SPA + .NET 8 API) for browsing, searching, and purchasing pet supplies and pets. The system provides a customer-facing storefront with product catalog, shopping cart, order management, and user accounts, plus an admin interface for inventory and order management.

## Actors

| Actor | Description |
| --- | --- |
| Customer | Registered user who browses products, manages a shopping cart, places orders, and tracks deliveries. |
| Guest | Unauthenticated visitor who can browse the catalog and view product details. |
| Admin | Authorized user who manages product inventory, categories, pricing, and order fulfillment. |

## External systems

| System | Type | Interaction | Direction |
| --- | --- | --- | --- |
| Payment Processor (e.g., Stripe) | External API | Payment intent creation and confirmation | petshop-api → external |
| Email Service (e.g., SendGrid) | External API | Order confirmation email delivery | petshop-api → external |
| Image CDN (e.g., Cloudflare) | External CDN | Product image delivery | petshop-web → external |

## Responsibilities

| Responsibility | Owning Container |
| --- | --- |
| Product catalog management (CRUD) | petshop-api (Catalog context) |
| Product search and filtering | petshop-api (Catalog context) |
| Shopping cart management | petshop-api (Cart context) |
| Order placement and management | petshop-api (Orders context) |
| User registration and profile | petshop-api (Users context) |
| Authentication (JWT) | petshop-api (Auth context) |
| Frontend UI and routing | petshop-web |
| Product browsing and search UI | petshop-web |
| Checkout flow UI | petshop-web |

## Boundaries

- The system boundary includes petshop-web (frontend) and petshop-api (backend).
- External systems (payment, email, CDN) are outside the system boundary.
- petshop-db (PostgreSQL), petshop-cache (Redis), and petshop-queue (RabbitMQ) are supporting infrastructure, not bounded contexts.

## Open questions

- **OQ-001**: Should the frontend use SSR for SEO? See design.md.
- **OQ-002**: What is the maximum expected product catalog size? Assumed: 10,000 SKUs.
- **OQ-003**: Should image storage use cloud object storage or the database/file system?

## Diagrams

### System Context Diagram

```
┌─────────────┐         ┌──────────────────┐         ┌──────────────┐
│   Customer   │────────▶│                  │────────▶│ Payment      │
│   / Guest    │         │   PetShop Web    │         │ Processor    │
│              │────────▶│                  │         │ (Stripe)     │
│   Admin      │────────▶│                  │         └──────────────┘
└─────────────┘         │                  │
                         │                  │         ┌──────────────┐
                         │  petshop-api     │────────▶│ Email        │
                         │                  │         │ Service      │
                         │                  │         │ (SendGrid)   │
                         └────────┬─────────┘         └──────────────┘
                                  │
                    ┌─────────────▼──────────────┐
                    │                            │
              ┌─────▼─────┐  ┌───────┐  ┌───────▼─────┐
              │ petshop-db │  │Redis  │  │ petshop-queue│
              │ (PostgreSQL)│  │Cache  │  │ (RabbitMQ)  │
              └────────────┘  └───────┘  └─────────────┘
```

### Container Diagram

```
┌─────────────┐         ┌──────────────────┐
│   Customer   │────────▶│                  │
│              │         │   petshop-web    │
│   Admin      │────────▶│   (React SPA)    │
└─────────────┘         │                  │
                         │                  │
                         │                  │
                         └────────┬─────────┘
                                  │ HTTPS/JSON
                                  │ JWT Bearer
                                  ▼
                         ┌──────────────────┐
                         │                  │
                         │   petshop-api    │
                         │   (.NET 8 API)   │
                         │                  │
                         │ ┌──────┬──────┬──┴───────┐
                         │ │Cat-  │Ordr│Users│ Auth  │
                         │ │alog  │ers │    │       │
                         │ └──────┴──────┴──────────┘
                         └────────┬─────────┘
                                  │
                    ┌─────────────▼──────────────┐
                    │                            │
              ┌─────▼─────┐  ┌───────┐  ┌───────▼─────┐
              │ petshop-db │  │Redis  │  │ petshop-queue│
              │ (PostgreSQL)│  │Cache  │  │ (RabbitMQ)  │
              └────────────┘  └───────┘  └─────────────┘
```

### Sequence: Place Order

```
Customer → petshop-web: 1. Browse catalog, add to cart
petshop-web → petshop-api: 2. GET /api/catalog/products
petshop-web → petshop-api: 3. POST /api/cart (add items)
Customer → petshop-web: 4. Proceed to checkout
petshop-web → petshop-api: 5. POST /api/orders (with cart ID)
petshop-api → petshop-db: 6. Create order, reserve inventory
petshop-api → petshop-queue: 7. Publish OrderPlaced event
petshop-api → petshop-web: 8. Return order confirmation
petshop-web → Customer: 9. Show order confirmation page
petshop-queue → Email Service: 10. Send confirmation email
petshop-api → Payment Processor: 11. Create payment intent
```

## Next level

See [System Containers](../containers/system-containers.md) for container decomposition.
