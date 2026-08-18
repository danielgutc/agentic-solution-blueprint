# Auth

## Purpose

Handle user authentication, authorization, and token management. Provides JWT token issuance, validation, and refresh functionality.

## Layer role

Bounded context — security and identity.

## Ownership

project-built

## Responsibilities

- User registration with email/password.
- User login with email/password (returns JWT access + refresh tokens).
- Token refresh with rotation.
- Token logout (blacklist/revocation).
- Role-based access control (RBAC) via JWT claims.
- Password hashing with bcrypt.

## Contracts

### Inbound Contracts (API)

| Endpoint | Method | Auth | Description |
| --- | --- | --- | --- |
| `/api/auth/register` | POST | None | Register a new user |
| `/api/auth/login` | POST | None | Login and get JWT tokens |
| `/api/auth/refresh` | POST | None | Refresh access token |
| `/api/auth/logout` | POST | Customer | Logout and invalidate tokens |

#### POST /api/auth/register — Precondition

- Request body must conform to `RegisterRequest` schema.
- Email must not already be registered.
- Password must meet complexity requirements (min 8 chars, uppercase, lowercase, digit).

#### POST /api/auth/register — Postcondition

- 201 Created with `AuthResponse` (accessToken, refreshToken, expiresIn).
- 400 Bad Request if email already exists or validation fails.

#### POST /api/auth/login — Precondition

- Request body must conform to `LoginRequest` schema.
- User must exist with matching credentials.

#### POST /api/auth/login — Postcondition

- 200 OK with `AuthResponse` (accessToken, refreshToken, expiresIn).
- 401 Unauthorized if credentials are invalid.

#### POST /api/auth/refresh — Precondition

- Request body must conform to `RefreshRequest` schema.
- Refresh token must be valid and not revoked.

#### POST /api/auth/refresh — Postcondition

- 200 OK with new `AuthResponse` (new accessToken, new refreshToken, expiresIn).
- 401 Unauthorized if refresh token is invalid or expired.

#### POST /api/auth/logout — Precondition

- Customer role required (valid JWT).
- Access token must be valid.

#### POST /api/auth/logout — Postcondition

- 204 No Content on success.
- 401 Unauthorized if token is invalid.

### Outbound Contracts

| Contract | Target | Protocol | Description |
| --- | --- | --- | --- |
| User Lookup | petshop-db | Npgsql | Validate user credentials |
| Token Blacklist | petshop-cache | Redis | Track revoked refresh tokens |

## Dependencies

| Dependency | Type | Direction |
| --- | --- | --- |
| petshop-db | Data Store | Auth → petshop-db |
| petshop-cache | Data Store | Auth → petshop-cache |

## Constraints

- JWT access token: 15-minute expiry, HS256 signing.
- JWT refresh token: 7-day expiry, stored in Redis with rotation.
- Password hashing: bcrypt with cost factor 12.
- Token blacklist in Redis with TTL matching refresh token expiry.
- JWT contains claims: sub (user ID), email, role (Customer/Admin).

## Code design

### Modules

| Module | Responsibility |
| --- | --- |
| `Auth.Api` | HTTP endpoints, request/response models, validation |
| `Auth.Domain` | UserCredentials entity and value objects |
| `Auth.Application` | Commands (RegisterUser, LoginUser, RefreshToken, Logout), Queries (ValidateToken) |
| `Auth.Infrastructure` | JWT token service, bcrypt password hasher, token blacklist service |

### Key types

```
Auth.Domain
├── Entities
│   └── UserCredentials (UserId, Email, PasswordHash, RefreshToken, RefreshTokenExpiry, CreatedAt)
├── ValueObjects
│   ├── Email (string, valid email format)
│   ├── PasswordHash (string, bcrypt hash)
│   └── RefreshToken (string, cryptographically random)
└── DTOs
    ├── AuthResponse (AccessToken, RefreshToken, ExpiresIn)
    ├── RegisterRequest (Email, Password, FirstName, LastName)
    ├── LoginRequest (Email, Password)
    ├── RefreshRequest (RefreshToken)
    └── LogoutRequest (AccessToken)

Auth.Application
├── Commands
│   ├── RegisterUserCommand (Handler: validates, hashes password, creates user, returns tokens)
│   ├── LoginUserCommand (Handler: validates credentials, issues tokens, returns tokens)
│   ├── RefreshTokenCommand (Handler: validates refresh token, rotates, returns new tokens)
│   └── LogoutCommand (Handler: blacklists refresh token, returns 204)
├── Queries
│   └── ValidateTokenQuery (Handler: validates JWT signature and expiry)
└── DTOs
    ├── AuthResponse (AccessToken, RefreshToken, ExpiresIn)
    └── TokenValidationResult (IsValid, Claims, Expiry)

Auth.Infrastructure
├── Services
│   ├── JwtTokenService (GenerateAccessToken, GenerateRefreshToken, ValidateToken)
│   ├── PasswordHasher (HashPassword, VerifyPassword)
│   └── TokenBlacklistService (AddToBlacklist, IsBlacklisted)
└── Data
    └── AuthDbContext (EF Core DbContext, DbSet<UserCredentials>)
```

### Flow

#### Registration Flow
```
1. POST /api/auth/register { email, password, firstName, lastName }
2. Auth.Api → RegisterUserCommand
3. Validate: email format, password complexity, email uniqueness
4. Hash password with bcrypt (cost 12)
5. Create User entity in petshop-db (schema: users)
6. Create UserCredentials entity in petshop-db (schema: auth)
7. Generate JWT access token (15 min) and refresh token (7 days)
8. Store refresh token in Redis (petshop-cache) with TTL
9. Return 201 Created with AuthResponse
```

#### Login Flow
```
1. POST /api/auth/login { email, password }
2. Auth.Api → LoginUserCommand
3. Look up user in petshop-db by email
4. Verify password with bcrypt
5. If invalid → return 401 Unauthorized
6. Generate JWT access token (15 min) and new refresh token (7 days)
7. Rotate refresh token: revoke old, store new in Redis
8. Return 200 OK with AuthResponse
```

#### Token Refresh Flow
```
1. POST /api/auth/refresh { refreshToken }
2. Auth.Api → RefreshTokenCommand
3. Check refresh token in Redis (petshop-cache)
4. If not found or expired → return 401 Unauthorized
5. Verify refresh token matches user's stored token (rotation check)
6. Generate new access token and new refresh token
7. Update Redis with new refresh token
8. Return 200 OK with new AuthResponse
```

#### Logout Flow
```
1. POST /api/auth/logout { accessToken }
2. Auth.Api → LogoutCommand
3. Validate JWT access token
4. Extract refresh token from token claims
5. Add refresh token to Redis blacklist (TTL = remaining expiry)
6. Return 204 No Content
```

### Extension points

- **Social login**: Add OAuth2 providers (Google, Facebook, Apple).
- **Two-factor auth**: Add TOTP/2FA challenge flow.
- **Password reset**: Add forgot-password with email verification token.
- **Rate limiting**: Add login attempt rate limiting via Redis.

### Testing notes

- Unit tests for password hashing (bcrypt cost factor verification).
- Unit tests for JWT token generation and validation.
- Unit tests for commands (registration validation, login validation, refresh rotation, logout blacklisting).
- Unit tests for token blacklist (Redis operations).
- Integration tests for auth flow with Testcontainers PostgreSQL.
- Contract tests for API endpoints against OpenAPI schema.

## Diagrams

### Component Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Auth Bounded Context                         │
│                                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌───────────────────────┐  │
│  │   Auth.Api  │    │   Auth      │    │   Auth                │  │
│  │             │    │   .Domain   │    │   .Application        │  │
│  │ Controllers │    │             │    │                       │  │
│  │ • POST      │    │ UserCred.   │    │ Commands              │  │
│  │ • POST      │    │ ValueObjs   │    │ • RegisterUserCmd     │  │
│  │ • POST      │    │ DTOs        │    │ • LoginUserCmd        │  │
│  │ • POST      │    │             │    │ • RefreshTokenCmd     │  │
│  │ • POST      │    └─────────────┘    │ • LogoutCmd           │  │
│  │             │                        │ Queries               │  │
│  │ Validators  │                        │ • ValidateTokenQry    │  │
│  │             │                        └───────────────────────┘  │
│  └─────────────┘                        ┌───────────────────────┐  │
│         │                                │   Auth               │  │
│         │                                │   .Infrastructure    │  │
│         │                                │                       │  │
│         │                                │ JwtTokenService      │  │
│         │                                │ PasswordHasher       │  │
│         │                                │ TokenBlacklistSvc    │  │
│         │                                └───────────────────────┘  │
│         │                                │          │               │
│    ┌────┴────┐                    ┌─────▼──┐  ┌───▼──────┐       │
│    │petshop- │                    │ petshop│  │ petshop  │       │
│    │  db     │                    │  -db   │  │  -cache  │       │
│    │ (PG:    │                    │(auth   │  │ (Redis:  │       │
│    │  auth   │                    │ schema)│  │ blacklist│       │
│    │  schema)│                    └────────┘  └──────────┘       │
│    └─────────┘                                                  │
└─────────────────────────────────────────────────────────────────────┘
```
