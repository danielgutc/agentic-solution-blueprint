# Orders

## Purpose

Manage the order lifecycle from placement through fulfillment. Ensures idempotent order creation, transactional integrity, and async processing of side effects (email, inventory updates).

## Layer role

Bounded context — transactional, event-driven.

## Ownership

project-built

## Responsibilities

- Idempotent order placement (prevent duplicate orders).
- Order creation with inventory reservation.
- Order status lifecycle management (pending → processing → shipped → delivered).
- Async email notification on order confirmation.
- Order history retrieval for customers and admins.
- Inventory adjustment via RabbitMQ events.

## Contracts

### Inbound Contracts (API)

| Endpoint | Method | Auth | Description |
| --- | --- | --- | --- |
| `/api/orders` | POST | Customer | Place a new order |
| `/api/orders` | GET | Customer | List user's orders |
| `/api/orders/{id}` | GET | Customer/Admin | Get order detail |
| `/api/orders/{id}/status` | PUT | Admin | Update order status |

#### POST /api/orders — Precondition

- Customer role required.
- Request body must conform to `PlaceOrderRequest` schema.
- Cart must exist and have items.
- All items must have sufficient inventory.

#### POST /api/orders — Postcondition

- 201 Created with `OrderResponse` if successful.
- 400 Bad Request if cart is empty or items are unavailable.
- 409 Conflict if duplicate order detected (same cart, same customer, within 5 min window).
- 500 Internal Server Error if inventory reservation fails.

#### GET /api/orders — Precondition

- Customer role required: returns only own orders.
- Admin role required: returns all orders.
- Optional query params: `status`, `page`, `pageSize`.

#### GET /api/orders — Postcondition

- 200 OK with paginated `OrderListResponse`.

#### GET /api/orders/{id} — Precondition

- Customer role: can only access own orders.
- Admin role: can access any order.
- Order ID must be valid.

#### GET /api/orders/{id} — Postcondition

- 200 OK with `OrderResponse` if found.
- 404 Not Found if order does not exist.
- 403 Forbidden if customer tries to access another customer's order.

#### PUT /api/orders/{id}/status — Precondition

- Admin role required.
- Request body must conform to `UpdateOrderStatusRequest` schema.
- Order must exist and be in a valid transition state.

#### PUT /api/orders/{id}/status — Postcondition

- 200 OK with updated `OrderResponse`.
- 400 Bad Request if status transition is invalid.
- 404 Not Found if order does not exist.

### Outbound Contracts

| Contract | Target | Protocol | Description |
| --- | --- | --- | --- |
| Order Events | petshop-queue | AMQP | Publish OrderPlaced event |
| Inventory Check | petshop-db | Npgsql | Reserve inventory for order items |
| Payment Intent | Payment Processor | HTTPS | Create payment intent for order |

## Dependencies

| Dependency | Type | Direction |
| --- | --- | --- |
| petshop-db | Data Store | Orders → petshop-db |
| petshop-queue | Broker | Orders → petshop-queue |
| Payment Processor | External | Orders → external |

## Constraints

- Order IDs are GUIDs.
- Order numbers are sequential (ORD-YYYYMMDD-NNNN format) for customer-facing use.
- Idempotency key: customer ID + cart ID + timestamp (5-min window).
- Inventory reservation is released if order is cancelled or payment fails.
- Valid status transitions: pending → processing → shipped → delivered; any → cancelled.

## Code design

### Modules

| Module | Responsibility |
| --- | --- |
| `Orders.Api` | HTTP endpoints, request/response models, validation |
| `Orders.Domain` | Order, OrderItem, Payment entities and value objects |
| `Orders.Application` | Commands (PlaceOrder, UpdateOrderStatus), Queries (GetOrders, GetOrderById) |
| `Orders.Infrastructure` | EF Core DbContext, repository implementations, RabbitMQ publisher |

### Key types

```
Orders.Domain
├── Entities
│   ├── Order (Id, OrderNumber, CustomerId, Status, TotalAmount, Currency, CreatedAt, UpdatedAt)
│   ├── OrderItem (Id, OrderId, ProductId, ProductName, Quantity, UnitPrice, TotalPrice)
│   └── Payment (Id, OrderId, PaymentIntentId, Status, Amount, Currency, CreatedAt)
├── ValueObjects
│   ├── OrderNumber (string, format ORD-YYYYMMDD-NNNN)
│   ├── OrderTotal (decimal, > 0)
│   └── OrderStatus (Pending, Processing, Shipped, Delivered, Cancelled)
└── Domain Events
    └── OrderPlacedEvent (OrderId, OrderNumber, CustomerId, TotalAmount, Items[])

Orders.Application
├── Commands
│   ├── PlaceOrderCommand (Handler: validates cart, reserves inventory, creates order, publishes event)
│   └── UpdateOrderStatusCommand (Handler: validates transition, updates status)
├── Queries
│   ├── GetOrdersQuery (Handler: returns paginated orders for user)
│   └── GetOrderByIdQuery (Handler: returns order detail with items)
└── DTOs
    ├── PlaceOrderRequest (CartId)
    ├── UpdateOrderStatusRequest (Status)
    ├── OrderResponse (Id, OrderNumber, CustomerId, Status, TotalAmount, Currency, Items[], CreatedAt)
    └── OrderListResponse (Items[], TotalCount, Page, PageSize, HasNextPage)

Orders.Infrastructure
├── Data
│   ├── OrdersDbContext (EF Core DbContext, DbSet<Order>, DbSet<OrderItem>, DbSet<Payment>)
│   └── Migrations/ (EF Core migration scripts)
├── Repositories
│   ├── OrderRepository (GetOrderByIdAsync, GetOrdersByCustomerIdAsync, GetOrdersByAdminAsync, CreateAsync, UpdateStatusAsync)
│   └── OrderItemRepository (GetOrderItemsByOrderIdAsync, CreateAsync)
└── Messaging
    └── OrderEventPublisher (PublishOrderPlacedAsync, PublishOrderConfirmedAsync)
```

### Flow

#### Order Placement Flow
```
1. POST /api/orders { cartId }
2. Orders.Api → PlaceOrderCommand
3. Validate: customer role, cart exists, cart has items
4. Check idempotency: customer ID + cart ID + 5-min window
5. If duplicate → return 409 Conflict with existing order ID
6. Inventory check: for each cart item, verify stock > 0
7. If insufficient stock → return 400 Bad Request
8. Create order in transaction:
   a. Generate order number (ORD-YYYYMMDD-NNNN)
   b. Create Order entity
   c. Create OrderItem entities for each cart item
   d. Reserve inventory (decrease available, increase reserved)
   e. Create Payment entity (status: pending)
9. Commit transaction
10. Publish OrderPlacedEvent to RabbitMQ (order.events exchange)
11. Create payment intent via Payment Processor
12. Return 201 Created with OrderResponse
```

#### Order Status Update Flow
```
1. PUT /api/orders/{id}/status { status }
2. Orders.Api → UpdateOrderStatusCommand
3. Validate: admin role, order exists, status transition valid
4. Update order status in petshop-db
5. If status → shipped: publish OrderShippedEvent
6. If status → delivered: publish OrderDeliveredEvent
7. Return 200 OK with updated OrderResponse
```

### Extension points

- **Payment integration**: Add Stripe/PayPal adapter for real payment processing.
- **Shipping integration**: Add shipping carrier integration (UPS, FedEx) for label generation.
- **Order cancellation**: Add customer-initiated cancellation before shipment.

### Testing notes

- Unit tests for domain entities (order total calculation, status transitions).
- Unit tests for commands (idempotency, inventory reservation, validation failures).
- Unit tests for queries (pagination, filtering by status).
- Integration tests for repository layer with Testcontainers PostgreSQL.
- Integration tests for RabbitMQ message publishing with Testcontainers RabbitMQ.
- Contract tests for API endpoints against OpenAPI schema.
- E2E tests for order placement flow (cart → order → confirmation).

## Diagrams

### Component Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Orders Bounded Context                      │
│                                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌───────────────────────┐  │
│  │  Orders.Api │    │  Orders     │    │  Orders               │  │
│  │             │    │  .Domain    │    │  .Application         │  │
│  │ Controllers │    │             │    │                       │  │
│  │ • POST      │    │ Order       │    │ Commands              │  │
│  │ • GET       │    │ OrderItem   │    │ • PlaceOrderCmd       │  │
│  │ • PUT       │    │ Payment     │    │ • UpdateStatusCmd     │  │
│  │             │    │ ValueObjs   │    │ Queries               │  │
│  │ Validators  │    │ Enums       │    │ • GetOrdersQry        │  │
│  │             │    │ DomainEvts  │    │ • GetOrderByIdQry     │  │
│  └─────────────┘    └─────────────┘    └───────────────────────┘  │
│         │                              ┌───────────────────────┐  │
│         │                              │  Orders               │  │
│         │                              │  .Infrastructure      │  │
│         │                              │                       │  │
│         │                              │ OrdersDbContext       │  │
│         │                              │ OrderRepository       │  │
│         │                              │ OrderItemRepository   │  │
│         │                              │ OrderEventPublisher   │  │
│         │                              └───────────────────────┘  │
│         │                              │          │                │
│    ┌────┴────┐                    ┌───▼──┐  ┌───▼──────┐        │
│    │petshop- │                    │ pet- │  │ petshop- │        │
│    │  db     │                    │ shop-│  │  queue   │        │
│    │ (Post-  │                    │  PG  │  │(RabbitMQ)│        │
│    │ greSQL) │                    └──────┘  └──────────┘        │
│    └─────────┘                    ┌──────────┐                   │
│                                    │ Payment  │                   │
│                                    │Processor │                   │
│                                    └──────────┘                   │
└─────────────────────────────────────────────────────────────────────┘
```
