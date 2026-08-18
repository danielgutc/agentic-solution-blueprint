# Users

## Purpose

Manage user accounts, profiles, and role assignments. Handles user registration, profile updates, and role-based data access.

## Layer role

Bounded context — user data management.

## Ownership

project-built

## Responsibilities

- User profile management (read/update).
- Role assignment (Customer, Admin).
- User data validation and persistence.
- Cross-context user lookup (e.g., Orders context validates CustomerId).

## Contracts

### Inbound Contracts (API)

| Endpoint | Method | Auth | Description |
| --- | --- | --- | --- |
| `/api/users/profile` | GET | Customer | Get current user's profile |
| `/api/users/profile` | PUT | Customer | Update current user's profile |

#### GET /api/users/profile — Precondition

- Customer or Admin role required (valid JWT).
- User identity extracted from JWT claims (sub claim).

#### GET /api/users/profile — Postcondition

- 200 OK with `UserProfileResponse` (Id, Email, FirstName, LastName, Phone, Address, Role).
- 401 Unauthorized if JWT is invalid or expired.

#### PUT /api/users/profile — Precondition

- Customer role required.
- Request body must conform to `UpdateProfileRequest` schema.
- Email must be unique (if changed).

#### PUT /api/users/profile — Postcondition

- 200 OK with updated `UserProfileResponse`.
- 400 Bad Request if validation fails (e.g., email already taken).
- 401 Unauthorized if JWT is invalid.

### Outbound Contracts

| Contract | Target | Protocol | Description |
| --- | --- | --- | --- |
| User Lookup | petshop-db | Npgsql | Find user by ID or email |

## Dependencies

| Dependency | Type | Direction |
| --- | --- | --- |
| petshop-db | Data Store | Users → petshop-db |

## Constraints

- Email addresses are unique and case-insensitive for lookup.
- Phone number must match E.164 format (+C[1-3]XXXXXXXXXX).
- Password changes require current password verification.
- Users cannot change their own role.

## Code design

### Modules

| Module | Responsibility |
| --- | --- |
| `Users.Api` | HTTP endpoints, request/response models, validation |
| `Users.Domain` | User entity and value objects |
| `Users.Application` | Commands (UpdateProfile), Queries (GetProfile) |
| `Users.Infrastructure` | EF Core DbContext, repository implementations |

### Key types

```
Users.Domain
├── Entities
│   └── User (Id, Email, PasswordHash, FirstName, LastName, Phone, Address, Role, CreatedAt, UpdatedAt)
├── ValueObjects
│   ├── Email (string, valid email format)
│   ├── Phone (string, E.164 format)
│   └── Address (Street, City, State, PostalCode, Country)
└── Enums
    └── UserRole (Customer, Admin)

Users.Application
├── Commands
│   └── UpdateProfileCommand (Handler: validates, updates user profile)
├── Queries
│   └── GetProfileQuery (Handler: returns user profile from JWT sub claim)
└── DTOs
    ├── UserProfileResponse (Id, Email, FirstName, LastName, Phone, Address, Role)
    └── UpdateProfileRequest (FirstName?, LastName?, Phone?, Address?)

Users.Infrastructure
├── Data
│   ├── UsersDbContext (EF Core DbContext, DbSet<User>)
│   └── Migrations/ (EF Core migration scripts)
└── Repositories
    └── UserRepository (GetByIdAsync, GetByEmailAsync, UpdateAsync)
```

### Flow

#### Get Profile Flow
```
1. GET /api/users/profile
2. Extract user ID from JWT "sub" claim
3. Users.Application → GetProfileQuery
4. UserRepository.GetByIdAsync(userId)
5. UserRepository → petshop-db (SELECT WHERE id = @userId)
6. Return UserProfileResponse
```

#### Update Profile Flow
```
1. PUT /api/users/profile { firstName?, lastName?, phone?, address? }
2. Extract user ID from JWT "sub" claim
3. Users.Application → UpdateProfileCommand
4. Validate: phone format (E.164), email uniqueness (if changed)
5. UserRepository.UpdateAsync(userId, updates)
6. UserRepository → petshop-db (UPDATE WHERE id = @userId)
7. Return 200 OK with updated UserProfileResponse
```

### Extension points

- **Password change**: Add ChangePassword command with current password verification.
- **Two-factor auth**: Add TOTP/2FA support.
- **Social login**: Add OAuth2 providers (Google, Facebook).

### Testing notes

- Unit tests for domain entities (email validation, phone format).
- Unit tests for commands (validation failures, uniqueness checks).
- Unit tests for queries (user not found, JWT extraction).
- Integration tests for repository layer with Testcontainers PostgreSQL.
- Contract tests for API endpoints against OpenAPI schema.

## Diagrams

### Component Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Users Bounded Context                        │
│                                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌───────────────────────┐  │
│  │  Users.Api  │    │  Users      │    │  Users                │  │
│  │             │    │  .Domain    │    │  .Application         │  │
│  │ Controllers │    │             │    │                       │  │
│  │ • GET       │    │ User        │    │ Commands              │  │
│  │ • PUT       │    │ ValueObjs   │    │ • UpdateProfileCmd    │  │
│  │             │    │ Enums       │    │ Queries               │  │
│  │ Validators  │    │ UserRole    │    │ • GetProfileQry       │  │
│  │             │    │             │    └───────────────────────┘  │
│  └─────────────┘    └─────────────┘    ┌───────────────────────┐  │
│         │                              │  Users                │  │
│         │                              │  .Infrastructure      │  │
│         │                              │                       │  │
│         │                              │ UsersDbContext        │  │
│         │                              │ UserRepository        │  │
│         │                              └───────────────────────┘  │
│         │                              │                          │
│    ┌────┴────┐                    ┌───▼──┐                       │
│    │petshop- │                    │ pet- │                       │
│    │  db     │                    │ shop-│                       │
│    │ (Post-  │                    │  PG  │                       │
│    │ greSQL) │                    └──────┘                       │
│    └─────────┘                                                  │
└─────────────────────────────────────────────────────────────────────┘
```
