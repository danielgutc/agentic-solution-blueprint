# petshop-web

## Purpose

React 18 SPA with TypeScript that provides the customer-facing storefront and admin interface for the PetShop Web application.

## Technology

- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite
- **Routing**: React Router v6
- **State Management**: Zustand
- **HTTP Client**: Axios
- **Form Handling**: React Hook Form + Zod
- **Styling**: CSS Modules (or Tailwind CSS)
- **Testing**: Playwright (E2E), Vitest (unit)
- **Accessibility**: axe-core for WCAG 2.1 AA compliance

## Responsibilities

- Render product catalog browsing and search UI.
- Manage shopping cart state (local + server-synced).
- Handle user authentication flow (login, register, logout).
- Render order history and order detail views.
- Provide admin interface for product and order management.
- Navigate between pages via React Router.
- Communicate with petshop-api via REST/HTTPS.

## Layered component model

```
petshop-web
├── public/
│   └── index.html
├── src/
│   ├── main.tsx (entry point)
│   ├── App.tsx (root component, routing)
│   ├── api/
│   │   ├── client.ts (Axios instance with auth interceptor)
│   │   ├── catalog.ts (catalog API calls)
│   │   ├── cart.ts (cart API calls)
│   │   ├── orders.ts (order API calls)
│   │   └── auth.ts (auth API calls)
│   ├── components/
│   │   ├── common/ (Button, Input, Modal, etc.)
│   │   ├── catalog/ (ProductCard, ProductList, SearchBar, CategoryNav)
│   │   ├── cart/ (CartSummary, CartItem, CheckoutForm)
│   │   ├── orders/ (OrderList, OrderDetail, OrderStatusBadge)
│   │   └── layout/ (Header, Footer, Sidebar)
│   ├── pages/
│   │   ├── Home.tsx
│   │   ├── Catalog.tsx
│   │   ├── ProductDetail.tsx
│   │   ├── Cart.tsx
│   │   ├── Checkout.tsx
│   │   ├── Orders.tsx
│   │   ├── OrderDetail.tsx
│   │   ├── Login.tsx
│   │   ├── Register.tsx
│   │   ├── Profile.tsx
│   │   └── admin/ (AdminLayout, AdminProducts, AdminOrders)
│   ├── stores/
│   │   ├── authStore.ts (auth state)
│   │   ├── cartStore.ts (cart state)
│   │   └── catalogStore.ts (catalog state)
│   ├── hooks/
│   │   ├── useAuth.ts
│   │   ├── useCart.ts
│   │   └── useCatalog.ts
│   ├── types/
│   │   ├── catalog.ts (Product, Category types)
│   │   ├── cart.ts (CartItem, Cart types)
│   │   ├── orders.ts (Order, OrderItem types)
│   │   └── auth.ts (User, AuthResponse types)
│   └── utils/
│       ├── validators.ts (Zod schemas)
│       └── formatters.ts (date, currency)
├── tests/
│   ├── e2e/ (Playwright tests)
│   └── unit/ (Vitest tests)
├── vite.config.ts
├── tsconfig.json
└── package.json
```

## Contracts

### Inbound Contracts (user interactions)

| UI Element | Action | Navigation |
| --- | --- | --- |
| Home page | Browse featured products | `/` |
| Catalog page | Search/filter products | `/catalog?search=&category=&priceRange=` |
| Product detail | View product info | `/products/{id}` |
| Category nav | Filter by category | `/catalog?category={id}` |
| Cart icon | View cart | `/cart` |
| Checkout button | Proceed to checkout | `/checkout` |
| Login link | Show login form | `/login` |
| Register link | Show registration form | `/register` |
| Profile link | View user profile | `/profile` |
| Orders link | View order history | `/orders` |
| Admin panel | Access admin features | `/admin/*` |

### Outbound Contracts (API calls)

| Contract | Target | Protocol | Description |
| --- | --- | --- | --- |
| Catalog API | petshop-api | HTTPS/JSON | Browse/search products |
| Cart API | petshop-api | HTTPS/JSON | Manage shopping cart |
| Order API | petshop-api | HTTPS/JSON | Place and view orders |
| Auth API | petshop-api | HTTPS/JSON | Login/register/logout |
| User API | petshop-api | HTTPS/JSON | Manage user profile |

## Dependencies

| Dependency | Type | Direction |
| --- | --- | --- |
| petshop-api | Service | petshop-web → petshop-api (HTTPS) |
| Payment Processor | External | petshop-web → external (via petshop-api) |
| Image CDN | External CDN | petshop-web → external (product images) |

## Boundaries

- All API communication goes through petshop-api; no direct database access.
- Authentication state managed client-side (JWT in memory/cookie) and server-side validated.
- Cart state synced between client (Zustand) and server (petshop-api).
- Admin routes protected by role-based route guards.

## Contained components

### API Layer
- **api/client.ts** — Axios instance with base URL, auth interceptor, error handling.
- **api/catalog.ts** — Functions for catalog API calls (getProducts, getProduct, search, etc.).
- **api/cart.ts** — Functions for cart API calls (getCart, addItem, updateItem, removeItem, clear).
- **api/orders.ts** — Functions for order API calls (placeOrder, getOrders, getOrder, updateStatus).
- **api/auth.ts** — Functions for auth API calls (register, login, refresh, logout).

### State Management
- **stores/authStore.ts** — Auth state (user, token, isAuthenticated) via Zustand.
- **stores/cartStore.ts** — Cart state (items, total) via Zustand.
- **stores/catalogStore.ts** — Catalog state (products, categories, filters) via Zustand.

### Components
- **components/common/** — Reusable UI components (Button, Input, Modal, Spinner, ErrorBoundary).
- **components/catalog/** — Catalog-specific components (ProductCard, ProductList, SearchBar, CategoryNav, PriceFilter).
- **components/cart/** — Cart-specific components (CartSummary, CartItem, CheckoutForm, EmptyCart).
- **components/orders/** — Order-specific components (OrderList, OrderDetail, OrderStatusBadge, OrderTimeline).
- **components/layout/** — Layout components (Header with nav, Footer, Sidebar for admin).

### Pages
- **pages/Home.tsx** — Landing page with featured products.
- **pages/Catalog.tsx** — Product listing with search and filters.
- **pages/ProductDetail.tsx** — Individual product view.
- **pages/Cart.tsx** — Shopping cart view.
- **pages/Checkout.tsx** — Checkout form with payment info.
- **pages/Orders.tsx** — Order history list.
- **pages/OrderDetail.tsx** — Individual order detail.
- **pages/Login.tsx** — Login form.
- **pages/Register.tsx** — Registration form.
- **pages/Profile.tsx** — User profile management.
- **pages/admin/AdminLayout.tsx** — Admin panel layout.
- **pages/admin/AdminProducts.tsx** — Product management CRUD.
- **pages/admin/AdminOrders.tsx** — Order management CRUD.

### Hooks
- **hooks/useAuth.ts** — Auth state and actions (login, logout, checkAuth).
- **hooks/useCart.ts** — Cart operations (addItem, removeItem, updateQuantity).
- **hooks/useCatalog.ts** — Catalog data fetching and filtering.

### Types
- **types/catalog.ts** — Product, Category, ProductFilter TypeScript interfaces.
- **types/cart.ts** — CartItem, Cart TypeScript interfaces.
- **types/orders.ts** — Order, OrderItem, OrderStatus TypeScript interfaces.
- **types/auth.ts** — User, AuthResponse, LoginRequest TypeScript interfaces.

### Utilities
- **utils/validators.ts** — Zod validation schemas for forms.
- **utils/formatters.ts** — Date formatting, currency formatting.

### Tests
- **tests/unit/** — Vitest unit tests for hooks, stores, utilities.
- **tests/e2e/** — Playwright E2E tests for critical user journeys.

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
│                         petshop-web                                 │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    petshop-web (React SPA)                  │   │
│  │  main.tsx │ App.tsx │ Router │ Auth Provider               │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│         ┌────────────────────┼────────────────────┐                │
│         │                    │                    │                │
│  ┌──────▼──────┐   ┌────────▼────────┐   ┌───────▼───────┐       │
│  │  Catalog    │   │    Cart         │   │     Auth      │       │
│  │  Pages      │   │    Pages        │   │    Pages      │       │
│  │ ┌─────────┐ │   │ ┌───────────┐   │   │ ┌───────────┐ │       │
│  │ │Catalog  │ │   │ │Cart      │   │   │ │Login     │ │       │
│  │ │Product  │ │   │ │Checkout  │   │   │ │Register  │ │       │
│  │ │Detail   │ │   │ │         │   │   │ │Profile   │ │       │
│  │ └─────────┘ │   │ └───────────┘   │   │ └───────────┘ │       │
│  └─────────────┘   └─────────────────┘   └───────────────┘       │
│         │                    │                    │                │
│  ┌──────▼──────┐   ┌────────▼────────┐   ┌───────▼───────┐       │
│  │  Orders     │   │    Admin        │   │    Common     │       │
│  │  Pages      │   │    Pages        │   │   Components  │       │
│  │ ┌─────────┐ │   │ ┌───────────┐   │   │ ┌───────────┐ │       │
│  │ │Order    │ │   │ │Admin     │   │   │ │Button    │ │       │
│  │ │History  │ │   │ │Products  │   │   │ │Input     │ │       │
│  │ │Detail   │ │   │ │Orders    │   │   │ │Modal     │ │       │
│  │ └─────────┘ │   │ └───────────┘   │   │ │Spinner   │ │       │
│  └─────────────┘   └─────────────────┘   │ └───────────┘ │       │
│                                           └───────────────┘       │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    State Management                         │   │
│  │  authStore │ cartStore │ catalogStore                       │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    API Layer                                │   │
│  │  api/client │ api/catalog │ api/cart │ api/orders │ api/auth│   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              │ HTTPS/JSON                          │
│                              ▼                                      │
│                    ┌──────────────────┐                            │
│                    │   petshop-api    │                            │
│                    │   (.NET 8 API)   │                            │
│                    └──────────────────┘                            │
└─────────────────────────────────────────────────────────────────────┘
```
