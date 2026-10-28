# C# Code

## Rules

- Prefer clear, readable code and cohesive responsibilities over clever abstractions.
- Follow standard .NET naming conventions and enable nullable reference types when supported.
- Keep public APIs intentional, minimal, typed, and aligned with approved contracts.
- Use Microsoft C# XML documentation for exported and architecturally significant contracts. Add applicable `summary`, `remarks`, `param`, `typeparam`, `returns`, `value`, `exception`, `example`, `see`, `seealso`, and `inheritdoc` content without promising behavior the implementation does not provide.
- Document preconditions, postconditions, invariants, side effects, idempotency, retry and recovery behavior, cancellation, concurrency, compatibility, and trust constraints when they matter to callers.
- Generate canonical unit/profile API pages and configured container/component/interface projections through the repository documentation command.
- Separate domain logic from transport, persistence, UI, and infrastructure concerns.
- Prefer dependency injection at boundaries rather than hard-coded infrastructure.
- Favor composition over inheritance unless the substitutability requirement is explicit.
- Use the selected framework's native capabilities before adding custom plumbing.
- Write tests for behavior and contract obligations rather than private implementation details.
- Keep each solution, `global.json`, central build or package file, source tree, developer tests, documentation configuration, and generated output inside the implementation unit or registered integration or end-to-end test workspace it intentionally governs.
- Place .NET generated output under the owning workspace's ignored `artifacts/` directory when the selected SDK supports centralized artifacts output. Use the repository artifacts path only for assembled packages, reports, and API documentation.
- Put a setting at repository scope only when every affected .NET workspace intentionally shares it; otherwise keep it at the owning workspace's toolchain root.
