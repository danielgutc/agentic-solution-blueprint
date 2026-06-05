# C# Code Instructions

## Purpose

Use these rules when writing or reviewing C# code in this repository.

## Rules

- Prefer clear, readable code over clever abstractions.
- Keep classes and methods small enough to have a single clear responsibility.
- Use meaningful names for types, methods, fields, and variables.
- Favor composition over inheritance unless inheritance is clearly justified.
- Keep shared contracts and reusable models stable and explicit.

## Conventions

- Follow standard .NET/C# coding conventions:
  - https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions
  - https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/identifier-names
- Naming defaults:
  - Use `PascalCase` for types, namespaces, and public members.
  - Use `camelCase` for parameters and local variables.
  - Prefix interfaces with `I`.
  - Use a leading underscore for private instance fields.
  - Avoid unclear abbreviations unless they are widely accepted.
- Prefer clarity over brevity in public and domain-facing APIs.
- Keep one primary type per file unless tight cohesion clearly justifies grouping.
- Prefer nullable reference types when the selected stack supports them.
- Keep public APIs intentional and minimal.
- Add comments only when the intent, boundary, invariant, or non-obvious runtime behavior is not clear from the code itself.
- Write tests for behavior, not implementation details.

## Documentation

- Document public contracts, interfaces, records, enums, and controller actions when they define a service, component, persistence, integration, or user-facing boundary.
- XML documentation should explain the contract purpose, caller expectations, ownership boundary, and important failure or lifecycle semantics when those are not obvious from the member name.
- Document implementation classes when they enforce boundary decisions, invariants, ordering rules, idempotency rules, retry semantics, persistence ownership, or adapter responsibilities.
- For in-memory, simulated, fake, or provisional implementations, explicitly document what behavior is intentionally executable and what real integration is deferred.
- Do not mention workflow phases, approval status, task IDs, maturity labels, or temporary planning language in source XML documentation or code comments.
- When an implementation is partial, describe the concrete runtime behavior and deferred capability in business- or technology-facing terms, not process labels such as "phase 3" or "approved".
- Keep documentation business-case agnostic in reusable instructions and shared templates; describe the engineering rule, not a specific project domain.
- Avoid noisy comments that restate syntax, repeat member names, or narrate obvious assignments.
## Enforcement guidance

- Prefer enforcing conventions via `.editorconfig`, Roslyn analyzers, and `dotnet format` in CI or local validation.
- Keep style automation aligned with the conventions above to reduce subjective review churn.

## Design Guidance

- Separate domain logic from transport, persistence, or UI concerns.
- Keep deterministic logic isolated when it affects gameplay or simulation behavior.
- Prefer dependency injection at boundaries rather than hard-coded infrastructure dependencies.
