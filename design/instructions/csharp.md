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

- Follow standard .NET naming conventions.
- Prefer nullable reference types when the selected stack supports them.
- Keep public APIs intentional and minimal.
- Use XML documentation for public contracts when behavior, errors, compatibility, side effects, or invariants are not evident from the signature.
- Generate the selected API reference and compact code projections through the repository documentation command.
- Add comments only when the intent is not obvious from the code itself.
- Write tests for behavior, not implementation details.

## Design Guidance

- Separate domain logic from transport, persistence, or UI concerns.
- Keep deterministic logic isolated when it affects gameplay or simulation behavior.
- Prefer dependency injection at boundaries rather than hard-coded infrastructure dependencies.
