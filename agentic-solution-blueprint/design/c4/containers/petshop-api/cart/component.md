# Cart

## Purpose

Manage the shopping cart for authenticated and anonymous users. Provides cart CRUD operations and total calculation.

## Layer role

Bounded context — session/state management.

## Ownership

project-built

## Responsibilities

- Cart CRUD (add, update, remove items).
- Cart total calculation (subtotal, tax, shipping).
- Cart persistence (server-side for authenticated users, Redis for anonymous).
- Cart merge (anonymous → authenticated on login).

## Contracts

### Inbound Contracts (API)

| Endpoint | Method | Auth | Description |
| --- | --- | --- | --- |
| `/api/cart` | GET | Customer | Get current cart |
| `/api/cart/items` | POST | Customer | Add item to cart |
| `/api/cart/items/{itemId}` | PUT | Customer | Update cart item quantity |
| `/api/cart/items/{itemId}` | DELETE | Customer | Remove cart item |
| `/api/cart/clear` | DELETE | Customer | Clear cart |

#### GET /api/cart — Precondition

- Customer role required (valid JWT).
- Cart ID derived from user ID.

#### GET /api/cart — Postcondition

- 200 OK with `CartResponse` (items, subtotal, tax, total, itemCount).
- If no cart exists → return empty cart with 200 OK.

#### POST /api/cart/items — Precondition

- Customer role required.
- Request body must conform to `AddCartItemRequest` schema.
- Product must exist and have inventory > 0.

#### POST /api/cart/items — Postcondition

- 201 Created with updated `CartResponse`.
- 400 Bad Request if product unavailable or quantity exceeds max.

#### PUT /api/cart/items/{itemId} — Precondition

- Customer role required.
- Item must belong to the user's cart.
- Quantity must be > 0 and ≤ available inventory.

#### PUT /api/cart/items/{itemId} — Postcondition

- 200 OK with updated `CartResponse`.
- 404 Not Found if item not in cart.
- 400 Bad Request if quantity invalid.

#### DELETE /api/cart/items/{itemId} — Precondition

- Customer role required.
- Item must belong to the user's cart.

#### DELETE /api/cart/items/{itemId} — Postcondition

- 204 No Content on success.
- 404 Not Found if item not in cart.

#### DELETE /api/cart/clear — Precondition

- Customer role required.

#### DELETE /api/cart/clear — Postcondition

- 204 No Content on success.

### Outbound Contracts

| Contract | Target | Protocol | Description |
| --- | --- | --- | --- |
| Product Lookup | petshop-db | Npgsql | Verify product exists and has inventory |
| Cart Store | petshop-cache | Redis | Persist cart data (key: cart:{userId}) |

## Dependencies

| Dependency | Type | Direction |
| --- | --- | --- |
| petshop-db | Data Store | Cart → petshop-db |
| petshop-cache | Data Store | Cart → petshop-cache |

## Constraints

- Cart items expire after 30 days of inactivity.
- Maximum quantity per item: 99.
- Cart stored in Redis as JSON document (key: cart:{userId}).
- Cart merge on login: anonymous cart items → user's server cart.

## Code design

### Modules

| Module | Responsibility |
| --- | --- |
| `Cart.Api` | HTTP endpoints, request/response models, validation |
| `Cart.Domain` | Cart, CartItem entities and value objects |
| `Cart.Application` | Commands (AddItem, UpdateItem, RemoveItem, ClearCart), Queries (GetCart) |
| `Cart.Infrastructure` | Redis cart store, product validation service |

### Key types

```
Cart.Domain
├── Entities
│   ├── Cart (Id, UserId, Items[], Subtotal, Tax, Total, CreatedAt, UpdatedAt)
│   └── CartItem (Id, CartId, ProductId, ProductName, UnitPrice, Quantity, LineTotal)
├── ValueObjects
│   ├── CartItemQuantity (int, > 0, ≤ 99)
│   ├── CartSubtotal (decimal, ≥ 0)
│   └── CartTotal (decimal, ≥ 0)
└── DTOs
    ├── CartResponse (Items[], Subtotal, Tax, Total, ItemCount)
    ├── AddCartItemRequest (ProductId, Quantity)
    ├── UpdateCartItemRequest (Quantity)
    └── CartItemResponse (Id, ProductId, ProductName, UnitPrice, Quantity, LineTotal)

Cart.Application
├── Commands
│   ├── AddCartItemCommand (Handler: validates product, adds/merges item, returns CartResponse)
│   ├── UpdateCartItemCommand (Handler: validates quantity, updates item, returns CartResponse)
│   ├── RemoveCartItemCommand (Handler: removes item, returns 204)
│   └── ClearCartCommand (Handler: clears all items, returns 204)
├── Queries
│   └── GetCartQuery (Handler: returns cart from Redis or empty cart)
└── DTOs
    └── (see Cart.Domain DTOs above)

Cart.Infrastructure
├── Storage
│   └── RedisCartStore (GetCartAsync, SetCartAsync, RemoveItemAsync, ClearAsync)
└── Validation
    └── ProductAvailabilityService (CheckProductAsync, GetProductPriceAsync)
```

### Flow

#### Add to Cart Flow
```
1. POST /api/cart/items { productId, quantity }
2. Cart.Api → AddCartItemCommand
3. Validate: customer role, product exists, product has inventory
4. GetCartQuery → RedisCartStore.GetCartAsync(userId)
5. If item exists for product → update quantity (merge)
6. If item doesn't exist → add new CartItem
7. Recalculate totals (subtotal, tax, total)
8. RedisCartStore.SetCartAsync(cart, TTL=30days)
9. Return 201 Created with updated CartResponse
```

#### Get Cart Flow
```
1. GET /api/cart
2. Cart.Api → GetCartQuery
3. RedisCartStore.GetCartAsync(userId)
4. If cart exists → return CartResponse
5. If cart doesn't exist → return empty CartResponse (200 OK)
```

### Extension points

- **Guest cart**: Store anonymous cart in Redis with session-based key.
- **Cart merge**: On login, merge anonymous cart into authenticated user's cart.
- **Wishlist**: Add wishlist functionality as a separate bounded context.

### Testing notes

- Unit tests for cart total calculations (subtotal, tax, total).
- Unit tests for commands (add item validation, quantity limits, product availability).
- Unit tests for queries (cart not found, empty cart).
- Integration tests for Redis cart store operations.
- Integration tests for product availability validation.
- Contract tests for API endpoints against OpenAPI schema.

## Diagrams

### Component Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Cart Bounded Context                        │
│                                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌───────────────────────┐  │
│  │   Cart.Api  │    │   Cart      │    │   Cart                │  │
│  │             │    │   .Domain   │    │   .Application        │  │
│  │ Controllers │    │             │    │                       │  │
│  │ • GET       │    │ Cart        │    │ Commands              │  │
│  │ • POST      │    │ CartItem    │    │ • AddItemCmd          │  │
│  │ • PUT       │    │ ValueObjs   │    │ • UpdateItemCmd       │  │
│  │ • DELETE    │    │ DTOs        │    │ • RemoveItemCmd       │  │
│  │             │    │             │    │ • ClearCartCmd        │  │
│  │ Validators  │    └─────────────┘    │ Queries               │  │
│  │             │                        │ • GetCartQry          │  │
│  └─────────────┘                        └───────────────────────┘  │
│         │                              ┌───────────────────────┐  │
│         │                              │   Cart               │  │
│         │                              │   .Infrastructure    │  │
│         │                              │                       │  │
│         │                              │ RedisCartStore       │  │
│         │                              │ ProductAvailability  │  │
│         │                              └───────────────────────┘  │
│         │                              │          │               │
│    ┌────┴────┐                    ┌───▼──┐  ┌───▼──────┐       │
│    │petshop- │                    │ pet- │  │ petshop  │       │
│    │  db     │                    │ shop-│  │  -cache  │       │
│    │ (PG:    │                    │  PG  │  │ (Redis:  │       │
│    │ catalog │                    └──────┘  │ cart:    │       │
│    │ schema) │                             │ {userId} │       │
│    └─────────┘                             └──────────┘       │
└─────────────────────────────────────────────────────────────────────┘
```
