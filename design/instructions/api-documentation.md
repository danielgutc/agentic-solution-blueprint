# API Documentation Instructions

## Purpose

Generate code-level documentation from implementation source, public API comments, and executable contracts instead of maintaining a duplicate manual interface inventory.

## Sources of Truth

- Keep architectural intent, responsibilities, and cross-boundary semantics in human-authored C4 and decision artifacts.
- Keep signatures, types, errors, compatibility behavior, and implementation-facing contracts in source interfaces and API comments.
- Keep observable contract behavior in automated tests.
- Do not manually edit generated code summaries or generated code-diagram sources.

## Generated Outputs

The project documentation command must produce:

- A compact `code.md` under the owning C4 component.
- Deterministic diagram sources under the component's `code-diagrams/` directory.
- A complete API reference under `artifacts/api-docs/` for publication as a CI artifact or documentation site.

Commit compact Markdown and diagram sources when they are deterministic and reviewable. Do not commit the full API site or rendered diagram output by default.

## Compact Code Summary

Generate only information that helps reviewers and agents navigate the implementation:

- A generated-file warning.
- Source scope, generator, and generation command.
- Modules or packages and their responsibilities.
- Public interfaces and important types.
- Dependencies and extension points.
- Links or identifiers for relevant contract tests.

Exclude exhaustive private members, repeated signatures, and prose already available in the full API reference.

## API Comments

- Document contracts, invariants, side effects, errors, compatibility, deprecation, concurrency, and security expectations when they are not evident from the signature.
- Avoid comments that merely restate names, types, or straightforward control flow.
- Use the ecosystem-native format selected in `design/foundation/tech.md`, such as Javadoc, XML documentation, DocFX, TypeDoc, Dokka, or Sphinx-compatible docstrings.

## Diagram Generation

- Generate stable source diagrams for module, package, dependency, and selected key-type structure.
- Prefer one useful abstraction over exhaustive class graphs.
- Keep dynamic behavior human-authored unless it is generated from an explicit executable scenario or trace.

## CI Requirements

- Generate documentation from a clean checkout.
- Fail when generation reports invalid public documentation or broken references.
- Regenerate committed projections and fail when the working tree would change.
- Publish the full API reference without adding it to source control.
