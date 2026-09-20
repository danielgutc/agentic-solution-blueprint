# API Documentation

## Purpose

Generate code-level documentation from implementation source, public API comments, and executable contracts instead of maintaining a duplicate manual interface inventory.

## Sources of truth

- Keep architecture intent and cross-boundary semantics in human-authored C4 and decision artifacts.
- Keep signatures, types, errors, compatibility, side effects, and implementation-facing contracts in source interfaces and ecosystem-native API comments.
- Keep observable contract behavior in automated tests.
- Follow `../standards/design-by-contract.md` for non-obvious obligations.

## Generated outputs

The repository documentation command must produce:

- compact `code.md` under each owning C4 component
- deterministic code-diagram sources under each component's `code-diagrams/`
- a complete API reference under `artifacts/api-docs/`

Commit compact Markdown and diagram sources when deterministic and reviewable. Publish the full API site and rendered diagrams as CI artifacts by default.

## Compact projection

Include only:

- a generated-file warning
- source scope, generator, and reproduction command
- modules or packages and responsibilities
- public interfaces and important types
- dependencies and extension points
- relevant contract-test identifiers

Exclude exhaustive private members, repeated signatures, and prose already present in the full API reference.

## API comments

- Document contracts, invariants, side effects, errors, compatibility, deprecation, concurrency, and security expectations when not evident from the signature.
- Do not restate names, types, or straightforward control flow.
- Use the format selected in `design/foundation/tech.md`, such as Javadoc, XML documentation/DocFX, TypeDoc, Dokka, or Sphinx-compatible docstrings.

## CI checks

- Generate from a clean checkout.
- Fail on invalid public documentation or broken references.
- Regenerate committed projections and fail when the working tree would change.
- Publish the full reference without adding it to source control.
