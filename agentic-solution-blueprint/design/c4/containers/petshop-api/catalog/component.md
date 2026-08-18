# Catalog

## Purpose

Manage product catalog data including products, categories, and inventory. Provides read-optimized access with Redis caching and admin CRUD operations.

## Layer role

Bounded context — read-heavy, caching-optimized.

## Ownership

project-built

## Responsibilities

- Product CRUD (admin only for write).
- Category management (admin only for write).
- Product search by name, category, price range.
- Redis caching for product listings and individual product details.
- Inventory tracking per product.

## Contracts

### Inbound Contracts (API)

| Endpoint | Method | Auth | Description |
| --- | --- | --- | --- |
| `/api/catalog/products` | GET | None | List/search products (paginated) |
| `/api/catalog/products/{id}` | GET | None | Get product detail |
| `/api/catalog/categories` | GET | None | List all categories |
| `/api/catalog/products` | POST | Admin | Create a new product |
| `/api/catalog/products/{id}` | PUT | Admin | Update an existing product |
| `/api/catalog/products/{id}` | DELETE | Admin | Delete a product (soft delete) |

#### GET /api/catalog/products — Precondition

- No authentication required for browse mode.
- Optional query params: `search` (string), `categoryId` (int), `minPrice` (decimal), `maxPrice` (decimal), `page` (int, default 1), `pageSize` (int, default 20).

#### GET /api/catalog/products — Postcondition

- 200 OK with paginated `ProductListResponse` containing `items`, `totalCount`, `page`, `pageSize`, `hasNextPage`.
- Cache hit: response served from Redis.
- Cache miss: response served from DB, then cached for 5 minutes.

#### GET /api/catalog/products/{id} — Precondition

- Product ID must be a valid GUID or integer.

#### GET /api/catalog/products/{id} — Postcondition

- 200 OK with `ProductResponse` if found.
- 404 Not Found if product does not exist or is deleted.

#### POST /api/catalog/products — Precondition

- Admin role required.
- Request body must conform to `CreateProductRequest` schema.
- Category must exist.

#### POST /api/catalog/products — Postcondition

- 201 Created with `ProductResponse`.
- 400 Bad Request if validation fails.
- 409 Conflict if category does not exist.

#### PUT /api/catalog/products/{id} — Precondition

- Admin role required.
- Request body must conform to `UpdateProductRequest` schema.
- Product must exist.

#### PUT /api/catalog/products/{id} — Postcondition

- 200 OK with updated `ProductResponse`.
- 404 Not Found if product does not exist.
- 400 Bad Request if validation fails.

#### DELETE /api/catalog/products/{id} — Precondition

- Admin role required.
- Product must exist.

#### DELETE /api/catalog/products/{id} — Postcondition

- 204 No Content on success.
- 404 Not Found if product does not exist.

### Outbound Contracts

| Contract | Target | Protocol | Description |
| --- | --- | --- | --- |
| Catalog Cache | petshop-cache | Redis | Cache product listings (TTL 5 min) and individual products (TTL 15 min) |
| Inventory Check | petshop-db | Npgsql | Check inventory levels for order validation |

## Dependencies

| Dependency | Type | Direction |
| --- | --- | --- |
| petshop-db | Data Store | Catalog → petshop-db |
| petshop-cache | Data Store | Catalog → petshop-cache |

## Constraints

- Products are soft-deleted (deleted_at timestamp), not hard-deleted.
- Price must be positive and formatted to 2 decimal places.
- Search is case-insensitive and supports partial matching on product name.
- Categories must have a unique name within the catalog.

## Code design

### Modules

| Module | Responsibility |
| --- | --- |
| `Catalog.Api` | HTTP endpoints, request/response models, validation |
| `Catalog.Domain` | Product, Category, Inventory entities and value objects |
| `Catalog.Application` | Commands (CreateProduct, UpdateProduct, DeleteProduct), Queries (GetProducts, GetProductById, GetCategories) |
| `Catalog.Infrastructure` | EF Core DbContext, repository implementations, Redis cache service |

### Key types

```
Catalog.Domain
├── Entities
│   ├── Product (Id, Name, Description, Price, CategoryId, InventoryCount, ImageUrl, CreatedAt, UpdatedAt, DeletedAt)
│   ├── Category (Id, Name, Description, ParentCategoryId, CreatedAt)
│   └── Inventory (ProductId, Quantity, ReservedQuantity)
├── ValueObjects
│   ├── ProductName (string, min 1, max 200 chars)
│   ├── ProductDescription (string, max 5000 chars)
│   ├── Price (decimal, > 0, 2 decimal places)
│   └── CategoryName (string, min 1, max 100 chars)
└── Enums
    └── ProductStatus (Active, Inactive, OutOfStock)

Catalog.Application
├── Commands
│   ├── CreateProductCommand (Handler: validates, calls repository, returns ProductResponse)
│   ├── UpdateProductCommand (Handler: validates, calls repository, returns ProductResponse)
│   └── DeleteProductCommand (Handler: soft deletes, returns 204)
├── Queries
│   ├── GetProductsQuery (Handler: checks cache, falls back to DB, returns paginated ProductListResponse)
│   ├── GetProductByIdQuery (Handler: checks cache, falls back to DB, returns ProductResponse)
│   └── GetCategoriesQuery (Handler: returns list of CategoryResponse)
└── DTOs
    ├── CreateProductRequest (Name, Description, Price, CategoryId, ImageUrl)
    ├── UpdateProductRequest (Name?, Description?, Price?, CategoryId?, ImageUrl?)
    ├── ProductResponse (Id, Name, Description, Price, Category, ImageUrl, Status, InventoryCount)
    ├── ProductListResponse (Items[], TotalCount, Page, PageSize, HasNextPage)
    └── CategoryResponse (Id, Name, Description, ParentCategoryId?)

Catalog.Infrastructure
├── Data
│   ├── CatalogDbContext (EF Core DbContext, DbSet<Product>, DbSet<Category>)
│   └── Migrations/ (EF Core migration scripts)
├── Repositories
│   ├── ProductRepository (GetProductsAsync, GetProductByIdAsync, CreateAsync, UpdateAsync, DeleteAsync)
│   └── CategoryRepository (GetCategoriesAsync, GetCategoryByIdAsync, CreateAsync)
└── Caching
    └── CatalogCacheService (GetProductsCacheAsync, SetProductsCacheAsync, GetProductCacheAsync, SetProductCacheAsync)
```

### Flow

#### Product Browse Flow
```
1. GET /api/catalog/products?search=dog&category=food&page=1
2. Catalog.Api → GetProductsQuery
3. CatalogCacheService → GetProductsCacheAsync("products:search=dog:category=food:p1")
4. If cache hit → return cached response (Redis)
5. If cache miss → ProductRepository.GetProductsAsync(search, categoryId, page, pageSize)
6. ProductRepository → petshop-db (SELECT with pagination)
7. CatalogCacheService → SetProductsCacheAsync(result, TTL=5min)
8. Return paginated ProductListResponse
```

#### Product Detail Flow
```
1. GET /api/catalog/products/{id}
2. Catalog.Api → GetProductByIdQuery
3. CatalogCacheService → GetProductCacheAsync("product:{id}")
4. If cache hit → return cached response (Redis)
5. If cache miss → ProductRepository.GetProductByIdAsync(id)
6. ProductRepository → petshop-db (SELECT WHERE id = @id)
7. CatalogCacheService → SetProductCacheAsync(result, TTL=15min)
8. Return ProductResponse
```

#### Product Create Flow
```
1. POST /api/catalog/products { name, description, price, categoryId, imageUrl }
2. Catalog.Api → CreateProductCommand
3. Validate: admin role, name unique, price > 0, category exists
4. ProductRepository.CreateAsync(product)
5. ProductRepository → petshop-db (INSERT)
6. CatalogCacheService → ClearProductsCacheAsync() (invalidate product list cache)
7. Return 201 Created with ProductResponse
```

### Extension points

- **Search provider**: Swap full-text search from EF Core to Elasticsearch for large catalogs (>10K products).
- **Cache strategy**: Implement cache-aside with versioned keys for write-through consistency.
- **Image storage**: Add cloud object storage (AWS S3) integration for product images.

### Testing notes

- Unit tests for domain entities (price validation, inventory constraints).
- Unit tests for commands (validation failures, category existence).
- Unit tests for queries (cache hit/miss scenarios).
- Integration tests for repository layer with Testcontainers PostgreSQL.
- Contract tests for API endpoints against OpenAPI schema.

## Diagrams

### Component Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Catalog Bounded Context                      │
│                                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌───────────────────────┐  │
│  │ Catalog.Api │    │  Catalog    │    │  Catalog              │  │
│  │             │    │  .Domain    │    │  .Application         │  │
│  │ Controllers │    │             │    │                       │  │
│  │ • GET       │    │ Product     │    │ Commands              │  │
│  │ • POST      │    │ Category    │    │ • CreateProductCmd    │  │
│  │ • PUT       │    │ Inventory   │    │ • UpdateProductCmd    │  │
│  │ • DELETE    │    │ ValueObjs   │    │ • DeleteProductCmd    │  │
│  │             │    │ Enums       │    │ Queries               │  │
│  │ Validators  │    │             │    │ • GetProductsQry      │  │
│  │             │    └─────────────┘    │ • GetProductByIdQry   │  │
│  └─────────────┘                       │ • GetCategoriesQry    │  │
│         │                              └───────────────────────┘  │
│         │                           ┌───────────────────────┐     │
│         │                           │  Catalog              │     │
│         │                           │  .Infrastructure      │     │
│         │                           │                       │     │
│         │                           │ CatalogDbContext      │     │
│         │                           │ ProductRepository     │     │
│         │                           │ CategoryRepository    │     │
│         │                           │ CatalogCacheService   │     │
│         │                           └───────────────────────┘     │
│         │                              │          │                │
│    ┌────┴────┐                    ┌───▼──┐  ┌───▼───┐           │
│    │petshop- │                    │ pet- │  │petshop│           │
│    │  db     │                    │ shop-│  │-cache │           │
│    │ (Post-  │                    │  PG  │  │(Redis)│           │
│    │ greSQL) │                    └──────┘  └───────┘           │
│    └─────────┘                                                  │
└─────────────────────────────────────────────────────────────────────┘
```
