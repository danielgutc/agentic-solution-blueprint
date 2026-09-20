# C# Code

## Rules

- Prefer clear, readable code and cohesive responsibilities over clever abstractions.
- Follow standard .NET naming conventions and enable nullable reference types when supported.
- Keep public APIs intentional, minimal, typed, and aligned with approved contracts.
- Use XML documentation when behavior, errors, compatibility, side effects, security, or invariants are not evident from the signature.
- Generate API reference and compact code projections through the repository documentation command.
- Separate domain logic from transport, persistence, UI, and infrastructure concerns.
- Prefer dependency injection at boundaries rather than hard-coded infrastructure.
- Favor composition over inheritance unless the substitutability requirement is explicit.
- Use the selected framework's native capabilities before adding custom plumbing.
- Write tests for behavior and contract obligations rather than private implementation details.
