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
- Add comments only when the intent is not obvious from the code itself.
- Write tests for behavior, not implementation details.

## Enforcement guidance

- Prefer enforcing conventions via `.editorconfig`, Roslyn analyzers, and `dotnet format` in CI or local validation.
- Keep style automation aligned with the conventions above to reduce subjective review churn.

## Design Guidance

- Separate domain logic from transport, persistence, or UI concerns.
- Keep deterministic logic isolated when it affects gameplay or simulation behavior.
- Prefer dependency injection at boundaries rather than hard-coded infrastructure dependencies.
