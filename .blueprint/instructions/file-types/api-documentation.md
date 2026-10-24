# API Documentation

## Purpose

Generate readable code guides, API reference, and code-structure navigation from implementation source, ecosystem-native API comments, and executable contracts. Do not maintain a second manual signature or interface inventory.

## Default toolchain

The blueprint ships the configurable Doxygen XML renderer at [generate_doxygen_docs.py](../../../tools/docs/generate_doxygen_docs.py) and the [Markdown link checker](../../../tools/docs/check_navigation.py). Follow the [tooling guide](../../../tools/docs/doxygen-tooling.md) for configuration and tested scope. Adopt these tools and their tests/fixtures using the [portable manifest](../../tooling.toml); keep language-specific compiler adapters and component ownership configuration project-owned. The shipped renderer is a starting implementation, not proof that a consuming project's language or strict documentation gates pass.

- Use Doxygen as the default source parser and documented structural-relationship engine when it supports the selected implementation language and the constructs present in the repository.
- Pin the accepted Doxygen version and configuration in repository-owned tooling after capability fixtures pass. The blueprint does not prescribe one global Doxygen version.
- Generate Doxygen XML as the normalized intermediate input. Render committed Markdown through a deterministic, repository-owned adapter; Doxygen does not provide the selected Markdown output directly.
- Keep the language compiler, build, and ecosystem-native documentation validation authoritative for compilability and exact exported signatures. Doxygen output is documentation evidence, not a substitute compiler.
- Add a focused compiler-model adapter only for a concrete construct that a failing Doxygen capability fixture proves cannot be represented safely. Do not run two competing default documentation models.
- If Doxygen does not support the implementation language or required semantics, record an exception in `design/foundation/tech.md` with the alternative ecosystem generator, scope, owner, capability evidence, compensating validation, and revisit trigger.

## Sources of truth

- Keep architecture intent, component ownership, and cross-boundary rationale in human-authored C4 and decision artifacts.
- Keep exported signatures, types, compatibility, errors, side effects, and implementation-facing contracts in source declarations and ecosystem-native API comments.
- Keep observable contract behavior and examples that claim execution in automated tests.
- Treat generated Markdown, relationship diagrams, and aggregate sites as projections. Change source comments, source declarations, tests, or generator configuration and regenerate them.
- Follow `../standards/design-by-contract.md` for non-obvious obligations.

## Source-comment contract

Document public or architecturally significant boundaries with the native comment syntax for the selected language. For example, use Microsoft C# XML documentation, Javadoc, or Doxygen-compatible doc comments. Include applicable:

- purpose and responsibility rather than a restatement of the symbol name
- parameter, type-parameter, return-value, property-value, and enum-state meaning
- preconditions, postconditions, invariants, side effects, idempotency, retry and recovery behavior
- cancellation, concurrency, ordering, ownership, trust, authorization, and compatibility constraints
- caller-relevant exceptions or error outcomes
- links to related symbols and concise examples that compile or point to executable evidence

Keep source comments true to implemented behavior. Do not infer product promises, support claims, runtime call graphs, or successful verification from a signature, comment, or test path alone.

## Capability qualification

- Exercise the exact language constructs present in the repository before accepting a Doxygen version or configuration. Cover relevant namespaces or modules, overloads, generics, inheritance and interface implementation, nullable or optional types, records or data classes, primary constructors, partial declarations, enums, and inherited documentation.
- Compare exported symbol identity and signatures with compiler or ecosystem-native build evidence. Fail on missing, duplicated, ambiguous, or silently reclassified public symbols.
- Record known parser limitations and the deterministic normalization rule. Compiler-synthesized equality, clone, accessor, and backing members are omitted unless the project intentionally exposes them.
- Validate supported and dropped comment tags. Preserve semantically required content through a compiler or native sidecar when Doxygen XML omits a supported source-comment construct; fail unsupported or ambiguous content rather than dropping it silently.
- Pin Graphviz separately when the project selects Graphviz-rendered output. A code-relationship renderer may instead generate Mermaid or another approved deterministic source from Doxygen XML.

## Generated outputs

For each implemented C4 component, the repository documentation command must produce:

- `code.md` as a committed developer guide and API entry point
- committed Markdown API pages under `api/<scope>/<stable-symbol-id>.md`
- deterministic code-relationship diagram sources under `_code-diagrams/`

The command may also publish a complete aggregate site or reference under `documentation.api_reference_output` as a CI artifact. HTML is optional aggregate output; committed Markdown remains the default navigable repository format.

Do not generate or link code documentation for a component with no repository-owned implementation. Do not create empty API folders or placeholder pages.

## Navigation and provenance

- Once `code.md` exists, link it directly from the owning `component.md` under `Code documentation`.
- Begin every generated page with a generated-file warning, owning component, source scope, generator and pinned version, configuration identity, reproduction command, and source-versus-authored provenance.
- Link `code.md` back to `component.md`, then link its API entries to committed per-symbol pages.
- Link each API page back to `code.md` and `component.md`, and to its source declaration using a stable repository path and line or source-control link when available.
- Use namespace- or module-qualified stable symbol identifiers that distinguish overloads and generic arity; do not key pages by simple type name alone.
- Label dependency and relationship edges with their evidence, such as inheritance, interface implementation, constructor or signature type, documented reference, or project dependency. Do not present structural evidence as a complete runtime call graph.
- Link tests only as identified evidence sources. A test file or method name is not a passing-test claim without recorded execution evidence.

## Developer guide content

`code.md` should explain the component's implemented purpose, safe call sequence, lifecycle or state flow, failure and retry behavior, trust boundary, extension points, and important dependencies. Link detailed signatures to API pages rather than repeating a flat type inventory. Keep human-authored architectural intent in `component.md` and link it instead of manufacturing it from source structure.

## CI checks

- Build and validate ecosystem-native source documentation before Doxygen generation.
- Run Doxygen with warnings treated according to the recorded project policy and retain actionable diagnostics.
- Run language capability fixtures and symbol-coverage checks for the pinned version and configuration.
- Validate stable symbol IDs, ownership mapping, source links, architecture backlinks, API links, and relationship provenance.
- Generate unit-local intermediate output within the owning implementation unit, then assemble committed component Markdown and publishable aggregate output at registered paths.
- Regenerate committed `code.md`, `api/` pages, and code-diagram sources from a clean checkout; fail when the working tree would change.
- Validate Markdown links and fail when a component links missing code documentation or a generated page loses its owning architecture link.
- Publish optional aggregate output without adding ignored build artifacts to source control.
