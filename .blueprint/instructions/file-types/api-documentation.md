# API Documentation

## Purpose

Generate readable code guides, API reference, and code-structure navigation from implementation source, ecosystem-native API comments, and executable contracts. Do not maintain a second manual signature or interface inventory.

## Default toolchain

The blueprint ships the configurable Doxygen XML renderer at [generate_doxygen_docs.py](../../../tools/docs/generate_doxygen_docs.py) and the [Markdown link checker](../../../tools/docs/check_navigation.py). Follow the [tooling guide](../../../tools/docs/doxygen-tooling.md) for configuration and tested scope. Adopt these tools and their tests/fixtures using the [portable manifest](../../tooling.toml); keep language-specific compiler adapters and component ownership configuration project-owned. The shipped renderer is a starting implementation, not proof that a consuming project's language or strict documentation gates pass.

- Use Doxygen as the default source parser and documented structural-relationship engine when it supports the selected implementation language and the constructs present in the repository.
- Pin the accepted Doxygen version and configuration in repository-owned tooling after capability fixtures pass. The blueprint does not prescribe one global Doxygen version.
- Generate Doxygen XML as the normalized intermediate input. Render committed Markdown through a deterministic, repository-owned adapter; Doxygen does not provide the selected Markdown output directly.
- Treat one documentation profile as a coherent source/build context. A profile may include several language projects when its language, target/runtime, compile symbols, native documentation evidence, and parser configuration are coherent; do not require one Doxyfile or profile per project, component, or container.
- Keep the language compiler, build, and ecosystem-native documentation validation authoritative for compilability and exact exported signatures. Doxygen output is documentation evidence, not a substitute compiler.
- Add a focused compiler-model adapter only for a concrete construct that a failing Doxygen capability fixture proves cannot be represented safely. Do not run two competing default documentation models.
- If Doxygen does not support the implementation language or required semantics, record an exception in `design/foundation/tech.md` with the alternative ecosystem generator, scope, owner, capability evidence, compensating validation, and revisit trigger.

## Sources of truth

- Keep architecture intent, component ownership, and cross-boundary rationale in human-authored C4 and decision artifacts.
- Keep exported signatures, types, compatibility, errors, side effects, and implementation-facing contracts in source declarations and ecosystem-native API comments.
- Keep observable contract behavior and examples that claim execution in automated tests.
- Treat generated Markdown, relationship diagrams, and aggregate sites as projections. Change source comments, source declarations, tests, or generator configuration and regenerate them.
- Keep language visibility and architecture visibility separate. A public declaration is not automatically a container interface, and an architecturally significant in-process port need not be public outside its assembly or module.
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
- Record included and excluded languages and source scopes, private-member coverage, native/compiler inventory evidence, and parser limitations for every profile. Do not describe a profile as complete container or repository coverage unless independent evidence establishes that claim.
- Validate supported and dropped comment tags. Preserve semantically required content through a compiler or native sidecar when Doxygen XML omits a supported source-comment construct; fail unsupported or ambiguous content rather than dropping it silently.
- Pin Graphviz separately when the project selects Graphviz-rendered output. A code-relationship renderer may instead generate Mermaid or another approved deterministic source from Doxygen XML.

## Configuration contract

- Use the portable generator's configuration schema version 2 for new and migrated profiles. Its schema version 1 remains accepted only as a deprecated compatibility input during migration; it does not define the new publication model. A capability-qualified project adapter may retain its own explicitly identified and validated configuration schema while implementing the same canonical publication, coverage, provenance, and navigation contract. Record its scope and revisit trigger in Tech.
- Register approved architecture in `architecture.containers[]` and optional `architecture.components[]` using stable C4 IDs, output directories, and existing architecture pages. A stale ID, missing page, or component path outside its registered container fails validation.
- Register one or more `profiles[]`. Each profile declares its stable `id`, `implementation_unit`, Doxygen identity and inputs, native `inventory_evidence`, included and excluded `source_coverage`, canonical `symbols[]`, and architecture `bindings[]`.
- Give each symbol one path-safe stable `key`, qualified name, API scope, and deterministic inventory selector. The configured inventory must match the supported extracted compounds exactly; selectors that match zero or several symbols fail.
- Bind symbols with `owned-implementation`, `provided-interface`, `consumed-interface`, or `supporting-code`. A provided/consumed binding must also declare `interface_scope` as `external-runtime` or `internal-component`; component presence alone does not establish that distinction. At most one `owned-implementation` source owner is allowed for a symbol. Provided, consumed, and supporting bindings may appear in several views: implementing or exposing an interface does not transfer ownership of its declaration. A shared container/unit owner is valid, and components are optional.
- Source paths, namespaces, projects, packages, and access modifiers may support a selector, but they do not create C4 ownership. Binding IDs come from approved C4 artifacts.

## Generated outputs

For each validated implementation-unit/documentation-profile context, the repository documentation command must produce one canonical committed reference:

- `design/code/<implementation-unit>/<documentation-profile>/index.md`
- `design/code/<implementation-unit>/<documentation-profile>/api/<scope>/<stable-symbol-id>.md`
- deterministic code-relationship sources below the profile root when configured

For each configured repository-owned architecture binding, generate link views rather than copies of the symbol content:

- `design/c4/containers/<container>/code.md` as the container-first entry
- `design/c4/containers/<container>/_code-views/interfaces.md` only when provided/consumed source bindings justify it
- `design/c4/containers/<container>/components/<component>/code.md` only when that approved component has bound symbols

A container with no approved component decomposition may still have a container entry view. Do not create empty API folders, component views, or interface-view placeholders. The command may also publish a complete aggregate site or reference under `documentation.api_reference_output` as a CI artifact. HTML is optional aggregate output; committed Markdown remains the default navigable repository format.

## Navigation and provenance

- Once a container `code.md` exists, link it directly from `container.md` under `Code documentation`. Link an optional component view from `component.md` only after that generated view exists.
- Begin every generated page with a generated-file warning, implementation unit, documentation profile, included and excluded source/language/visibility coverage, parser limitations, generator and pinned version, configuration identity, reproduction command, and source-versus-authored provenance.
- Link every architecture view to canonical API pages. Link each canonical page back to its profile index, every configured container/component/interface view, and its source declaration using a stable repository path and line or source-control link when available.
- Use namespace- or module-qualified stable symbol identifiers that distinguish overloads and generic arity; do not key pages by simple type name alone.
- Label dependency and relationship edges with their evidence, such as inheritance, interface implementation, constructor or signature type, documented reference, or project dependency. Do not present structural evidence as a complete runtime call graph.
- Link tests only as identified evidence sources. A test file or method name is not a passing-test claim without recorded execution evidence.

## Architecture-view content

- Container `code.md` is the reader entry point for all configured profiles participating in the container. It distinguishes owned code, shared/supporting code, provided interfaces, and consumed interfaces and links to canonical pages without claiming a complete runtime call graph.
- Optional component `code.md` explains implemented call sequence, lifecycle or state flow, failure and retry behavior, trust boundary, extension points, and important dependencies for its bound symbols. It is not the component definition or a flat inner-class/type inventory.
- `_code-views/interfaces.md` is a source-bound view of provided and consumed architectural ports, generated only when those bindings exist. It groups external runtime ports separately from internal component ports using the explicit binding scope. Do not hand-copy exact signatures into architecture prose.
- Human-authored `container.md` retains external runtime contracts and distinguishes its component overview from internal interfaces. Human-authored `component.md` retains responsibilities and provided/required ports.

## Compatibility migration

- Migration is additive: generate the canonical unit/profile reference and new C4 views before replacing existing links.
- Preserve each legacy component-local API path as a generated moved-notice link stub when configured. A stub contains no copied API content and is never hand-edited.
- Keep stubs through the next blueprint major adoption by default. A consuming project records its exact start/end window in Tech and may remove stubs only after that window and clean inbound-link, orphan, and regeneration checks pass.
- Migrate consuming projects independently after reviewing their unit/profile inventory, coverage, and approved C4 bindings. Do not change source namespaces, projects, packages, visibility, runtime boundaries, or container ownership as part of documentation publication migration.

## CI checks

- Build and validate ecosystem-native source documentation before Doxygen generation.
- Run Doxygen with warnings treated according to the recorded project policy and retain actionable diagnostics.
- Run language capability fixtures and symbol-coverage checks for the pinned version and configuration.
- Validate stable symbol IDs, exact configured inventory, owner/consumer bindings, approved C4 IDs, source links, reciprocal architecture backlinks, API links, relationship provenance, and declared coverage.
- Generate unit-local intermediate output within the owning implementation unit, then assemble committed canonical pages and architecture views at registered paths.
- Regenerate canonical API pages, configured C4 views, compatibility stubs, and code-diagram sources from a clean checkout; fail when the working tree would change.
- Validate Markdown links and fail when an architecture page links missing code documentation, a canonical page loses a configured architecture backlink, or a generated compatibility stub outlives its declared window.
- Publish optional aggregate output without adding ignored build artifacts to source control.
