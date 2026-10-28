# API documentation model review

[README](../../README.md) / Foundation / API documentation model review

Related foundation documents:

- [Tech](./tech.md)
- [Design](./design.md)
- [Delivery governance](./delivery.md)
- [Task tracker](./task.md)
- [Implementation readiness](./implementation-readiness.md)

## Table of contents

- [Status](#status)
- [Owner and level](#owner-and-level)
- [Context and evidence](#context-and-evidence)
- [Terms and scope](#terms-and-scope)
- [Decision criteria](#decision-criteria)
- [Options considered](#options-considered)
- [Decision](#decision)
- [Approved publication model](#approved-publication-model)
- [Ownership and membership model](#ownership-and-membership-model)
- [Migration and affected blueprint assets](#migration-and-affected-blueprint-assets)
- [Consequences](#consequences)
- [Validation and evolution](#validation-and-evolution)
- [Deferred decisions and open questions](#deferred-decisions-and-open-questions)

## Status

**Approved on 2026-10-26.** The developer accepted Option C and authorized the reusable blueprint policy, templates, registry, and documentation tooling migration. Consuming-project migration requires its own recorded execution evidence; approval alone does not establish completed migration or change source namespaces, projects, packages, visibility, public APIs, or approved runtime/container boundaries. The repository-intelligence APP cross-process boundary review remains open; no new container is approved by this decision.

## Owner and level

- **Decision owner:** technical architect for C4-to-code projections and documentation-generation tooling
- **Required consultation:** solutions architect when a proposed selector would alter or expose uncertain container/runtime ownership
- **Abstraction level:** reusable blueprint policy for code-documentation extraction, canonical API publication, and C4 navigation
- **Related IDs:** none; `selected_workflow` is intentionally `unset` in this reusable template

## Context and evidence

The current blueprint makes each implemented C4 component the physical home of generated `code.md`, per-symbol API pages, and code-diagram sources. Its portable renderer requires every discovered public/protected compound to match exactly one configured component. This works for a simple one-container, one-component fixture, but it combines four different questions:

1. Which source and compile configuration should Doxygen extract?
2. Where should one symbol's canonical API page live?
3. Which container/component views should include that symbol?
4. Which architectural interface does the symbol implement or consume?

Those questions are not always answered by the same path. The C4 model defines a component as related functionality behind a well-defined interface and describes classes/interfaces as code elements inside a component. Packaging as a JAR, assembly, namespace, or folder is orthogonal and may be one-to-one, one-to-many, or many-to-one. It also treats a code diagram as an optional view scoped to one component, not as the definition of the component itself. See the official C4 descriptions of [components](https://c4model.com/abstractions/component) and [code diagrams](https://c4model.com/diagrams/code).

Doxygen likewise separates extraction from grouping. `INPUT` accepts files and directories, so one extraction can cover several projects when they share a coherent documentation/compile profile. Doxygen topics can group namespaces, classes, files, and other entities, and a compound can belong to multiple groups. These capabilities do not by themselves establish C4 ownership. See the official Doxygen documentation for [`INPUT`](https://www.doxygen.nl/manual/config.html#cfg_input) and [grouping](https://www.doxygen.nl/manual/grouping.html).

The repository-intelligence APP provides bounded evidence, not a universal model: one Doxyfile currently extracts `implementation/app/src`, covering five production C# projects, and one project adapter partitions the XML into six component guides. Its `FILE_PATTERNS=*.cs` and `EXTRACT_PRIVATE=NO` settings exclude Python and Java language assets under the same source root as well as private C# declarations. The current output is therefore a configured C# profile, not a catalogue of every implementation type or proof of whole-APP coverage.

A read-only comparison with the war-strategy-game Wargame Scenario Service provides a second information-architecture example. Its container-owned `code-contracts-phase1.md` aggregates exact component interface operations, while the `scenario-service-query-api` and `scenario-workflow-engine` component pages describe purposes, responsibilities, provided/required interfaces, and ports rather than treating implementation classes as components. The sibling Draw.io interface diagram repeats exact operation signatures. The Markdown and Draw.io inventories already disagree on facade return names: `ScenarioCommandResult` versus `ScenarioCommandResponse`, and `ScenarioRecordResult` versus `ScenarioDetailsResponse`. No inspected source evidence establishes which version is correct. This is evidence that handwritten signature projections can drift and that component narratives remain valuable architectural views; it is not evidence that every consuming project has the same implementation layout or can use one universal extraction profile.

## Terms and scope

- **Extraction scope:** the files/directories parsed into one Doxygen XML result. It may cover one or several language projects.
- **Documentation profile:** a reproducible source/build context that fixes implementation unit, language, target/runtime, compile symbols, native documentation source, Doxygen configuration, compiler/native sidecar, and expected exported-symbol inventory.
- **Canonical symbol page:** the one generated API page for a stable symbol identity within one validated documentation profile.
- **Container entry view:** a generated reader-oriented index for configured repository-owned implementation profiles participating in one C4 container. It states its included and excluded source scopes and does not claim complete coverage of the container runtime.
- **Component view:** a generated filtered guide for code owned or used by one approved C4 component.
- **Architectural interface view:** a generated filtered view of source contracts bound to provided or consumed C4 ports. It is not a manually copied signature list.
- **Implementation type:** a source-level class, interface, record, function, or equivalent. The phrase “inner classes” in the motivating question is treated as implementation types generally, not as a claim about the C# nested-type keyword.

This decision concerns generated navigation and API reference. Human-authored `container.md` continues to own the container's external responsibilities, provided/consumed runtime contracts, data ownership, and contained-component relationships. Human-authored `component.md` continues to own a component's purpose, responsibility, ports, constraints, dependencies, and test seams. Exact signatures and behavior remain authoritative in source declarations, ecosystem-native comments, and executable contracts.

Source visibility and architectural visibility are different. A public type is not automatically an external container interface, and an architecturally significant in-process port need not be public outside its assembly. The model must not turn on private extraction indiscriminately or infer a C4 interface from a language access modifier.

## Decision criteria

Weights are fixed before comparing options. Scores use `1` (poor) through `5` (strong).

| Criterion | Weight | Why it matters |
| --- | ---: | --- |
| One canonical symbol identity without duplicated content | 25 | Shared libraries and shared interfaces must not produce contradictory API pages. |
| Container-first reader navigation and interface clarity | 20 | A reader should enter through the approved runtime boundary and then drill into components and source contracts. |
| Accurate many-to-many architecture membership | 20 | One type may support several components; one library may participate in several containers; ownership and consumption must remain distinct. |
| Profile distinction and authoritative coverage | 15 | Different targets, compile symbols, or language adapters can expose different APIs from the same source; compiler/native evidence, not Doxygen alone, establishes the expected inventory. |
| Migration and backlink stability | 10 | Existing component links and committed documentation need a reviewable transition. |
| Portability and tooling simplicity | 10 | The default must remain usable across languages and implementation layouts without a project-specific rewrite. |

## Options considered

| Option | Canonical identity 25 | Reader navigation 20 | Membership 20 | Profile/coverage 15 | Migration 10 | Simplicity 10 | Weighted result |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| A. Retain component-canonical pages; enrich navigation | 5 | 4 | 2 | 3 | 5 | 4 | 76/100 |
| B. Make each container canonical, with component subviews | 4 | 5 | 3 | 3 | 3 | 3 | 73/100 |
| C. Canonicalize by implementation unit and documentation profile; publish container/component/interface link views | 5 | 5 | 5 | 5 | 2 | 2 | 88/100 |

### Option A: retain component-canonical output and enrich navigation

Keep the current `components/<component>/code.md` and `components/<component>/api/...` structure and require exactly one component match per exported type. Add container indexes and explicit provided/consumed links without moving canonical pages.

The exact-one rule already guarantees one canonical page, and several consumers can link to it without duplicated content. This is a viable, cheaper option when each symbol has an honest component home and richer cross-links are sufficient. Its limitation is that every canonical page must still have one component home and symbol identity remains coupled to that architectural placement. The model has no first-class architecture-independent identity or generated many-to-many owner/consumer views. A shared contract or library can therefore require an artificial component owner, while consumer membership and reciprocal backlinks need additional conventions. Namespace-based selection does not repair this: namespace, package, assembly, and folder can help locate code but are not necessarily C4 components.

### Option B: container-canonical output with component subviews

Generate one symbol reference below each container and let component pages filter that container reference.

This fits the desired container-first reading experience and avoids duplication among components of the same container. Across containers it must either choose one possibly artificial canonical container and add cross-container links, or copy local reference content; it has no explicit unit/profile-level sharing model. It also conflates runtime ownership with extraction when one container uses several projects or one project participates in several runtime boundaries.

### Option C: unit/profile-canonical output with container-first views

Generate one canonical symbol reference for each validated implementation-unit/documentation-profile context. Generate container, component, and architectural-interface views as indexes and guides that link to those pages.

This preserves a container-first reader experience without making a container the physical owner of every symbol it uses. It handles several projects in one extraction, several extractions for different compile profiles, shared libraries used by multiple containers, and one interface consumed by several components. Its cost is a richer registry/schema, more validation rules, a new canonical output location, and a deliberate migration.

## Decision

**Approved Option C.** Canonical API pages are owned by a validated implementation unit and documentation profile. Every repository-owned container to which a configured profile is bound receives a generated entry index. Approved components receive filtered generated views only when symbols are bound to them. Architectural-interface views are generated only when provided or consumed source bindings exist. All views link to canonical pages rather than copying their content.

This is a publication model, not a mandate for one Doxyfile per container. A project may use one extraction for several projects when their profile is coherent, or several extractions when language, target, compile symbols, or parser configuration differ. Doxygen XML remains an intermediate; compiler/native documentation evidence remains authoritative for exact exported symbols.

A consuming project with one validated default profile needs only that profile. Profile comparison, consolidation, and multiple canonical contexts are required only when the project claims materially different source/build configurations or proposes that several configurations share one reference.

The decision does not claim complete compiler-semantic extraction or whole-container implementation coverage. It requires each generated view to disclose its configured source/language/visibility scope and exclusions, and it validates generated symbols against an independently established compiler/native inventory where that ecosystem provides one. Code outside a configured profile is neither silently included nor presented as documented coverage.

The decision does not require every container to have a C4 component decomposition. A container without approved components receives a container entry view only. It also does not make implementation types into C4 components: a component remains a cohesive responsibility behind architectural ports, implemented by zero or more source-level types at any particular stage.

## Approved publication model

The paths below are the default publication contract. Generator configuration schema version 2 registers approved containers, optional components, documentation profiles, canonical symbols, and role bindings. Schema version 1 remains accepted as a deprecated migration input.

```text
design/
  code/
    <implementation-unit>/
      <documentation-profile>/
        index.md
        api/<language-or-scope>/<stable-symbol-id>.md
        _code-diagrams/
  c4/containers/<container>/
    container.md                         # human-authored architecture
    code.md                              # generated container entry/index
    _code-views/interfaces.md            # generated architectural-interface view
    components/<component>/
      component.md                       # human-authored architecture
      code.md                            # generated filtered component guide
      _code-diagrams/                    # generated component-scoped relationship sources
```

The generated container entry should:

- identify every contributing implementation unit/profile and its generator/configuration identity;
- group links by approved component when decomposition exists;
- provide a distinct view of source contracts bound to the container's provided and consumed interfaces;
- distinguish owned implementation from a shared library or externally maintained dependency;
- link to canonical symbol pages, source declarations, native/compiler documentation evidence, and recorded tests without duplicating signatures;
- avoid claiming that a structural relationship is a complete runtime call graph.

The component guide should explain implemented call sequence, lifecycle/failure behavior, trust boundaries, extension points, and important dependencies using source-authored documentation, while linking exact signatures to canonical pages. The component diagram inside the container may show component-to-component and external interfaces. A generated code relationship view may show selected implementation types inside one component, but it must not redefine the component boundary or turn every private/helper class into architecture.

## Ownership and membership model

The configuration needs two layers instead of the current exact-one-component selector:

1. **Canonical source identity** — implementation unit, documentation profile, language, assembly/module/package where applicable, compiler/native stable symbol ID, source declaration, and generator/configuration identity.
2. **Architecture bindings** — stable C4 container/component IDs plus an explicit role such as `owned-implementation`, `provided-interface`, `consumed-interface`, or `supporting-code`.

Rules for the approved model:

- A canonical symbol key is unique within its documentation profile. Duplicate canonical keys fail.
- Ownership and use are separate. A symbol may have one explicit component owner, an explicit container/unit shared owner, or no component owner when no decomposition is approved. It may be consumed by several components or containers.
- Multiple `consumed-interface` bindings are valid; conflicting ownership bindings fail.
- A shared library used by several containers is generated once per materially distinct profile and linked from every consuming container view. It is not copied into each container's API tree.
- If the same source produces materially different public surfaces under different target/compile profiles, each validated profile has a separate canonical reference. Profiles with identical claimed APIs may be consolidated only with evidence and a deterministic identity rule.
- Every exported symbol in the profile's independently established expected inventory must have a canonical page. Every symbol selected as architecturally significant must have a valid architecture binding. Unmapped required bindings, stale C4 IDs, conflicting owners, and references to missing symbols fail closed.
- Third-party packages are linked to their authoritative external documentation; they are not republished as repository-owned symbols.
- Doxygen groups may be consumed as extraction metadata, but C4 bindings remain repository configuration validated against approved C4 IDs. Source comments do not silently create architecture.
- The approved binding roles are `owned-implementation`, `provided-interface`, `consumed-interface`, and `supporting-code`. Provided/consumed bindings explicitly classify their interface scope as `external-runtime` or `internal-component`; component presence alone does not decide that boundary. At most one `owned-implementation` source owner is valid for a symbol. Several providers or consumers may link the same interface declaration without acquiring its source ownership.

The known repository-intelligence APP still needs a container/runtime-boundary review before final selectors are designed, because its CLI, worker, broker, client, embedded storage, and MCP composition cross process and protocol boundaries. Its present mapping is useful migration evidence, not approval of a reusable ownership rule.

## Migration and affected blueprint assets

An approved migration should be additive first:

1. Add schema/fixtures and canonical output beside the current output; do not remove component pages yet.
2. Generate container and component filtered views that link to canonical pages.
3. Rewrite repository links and generate compatibility stubs at old per-component API paths. A stub contains only a generated moved notice and canonical link, not duplicated API content.
4. Retain stubs through the next blueprint major adoption by default. Each consuming project records its exact start/end window in Tech and removes stubs only after that window and clean inbound-link, orphan, and regeneration checks pass.
5. Migrate each consuming project independently after its unit/profile inventory and C4 bindings are reviewed. The war-strategy-game comparison assessed architectural navigation and handwritten contract drift only; it did not qualify that project's source languages, implementation profiles, or generator pipeline.
6. Treat namespace, project, package, visibility, or public API changes revealed by migration as a separate technical-design/refactoring slice with its own compatibility and test evidence.

The following blueprint assets require coordinated change rather than isolated edits:

- `AGENTS.md`
- `.blueprint/blueprint.toml`
- `.blueprint/instructions/file-types/api-documentation.md`
- `.blueprint/instructions/artifacts/c4.md`
- `.blueprint/instructions/standards/navigation.md`
- `.blueprint/templates/c4/container.template.md`
- `.blueprint/templates/c4/component.template.md`
- `.blueprint/templates/foundation/tech.template.md`
- `.blueprint/tooling.toml`
- `tools/README.md`
- `tools/docs/doxygen-tooling.md`
- `tools/docs/doxygen.example.json`
- `tools/docs/doxygen_markdown.py`
- `tools/docs/generate_doxygen_docs.py`
- `tools/docs/check_navigation.py` where compatibility-link policy requires it
- `tools/docs/test_generate_doxygen_docs.py`, `tools/docs/test_check_navigation.py`, and the generic source/XML/config fixtures

Consuming repositories then update their project-owned Doxyfiles, compiler/native adapters, documentation-profile registry, CI commands, generated outputs, and navigation. The portable manifest must carry every changed reusable tool, test, fixture, template, and instruction from the same blueprint revision.

## Consequences

Positive consequences:

- Readers enter through the container and drill into components/interfaces without losing the one canonical source contract.
- Shared interfaces and libraries can keep one canonical profile-scoped page while generated owner and consumer views link to it; they no longer require an arbitrary component home merely to participate in several generated views.
- C4 architecture remains human-authored while source contracts and code relationships remain generated.
- Extraction scope follows build/documentation evidence instead of assuming a project, namespace, component, and container are the same boundary.

Costs and risks:

- The registry and renderer become more complex, especially for profile identity, many-to-many bindings, and compatibility stubs.
- A new canonical output root requires navigation, freshness, orphan, and ownership protections.
- Container/component views can become noisy unless they distinguish provided interfaces, consumed interfaces, owned implementation, and supporting code.
- Incorrect architecture metadata can produce authoritative-looking but wrong views; validation must fail closed and C4 IDs must come from approved artifacts.
- Doxygen limitations remain. The model does not remove the need for native compiler inventories, comment sidecars, capability fixtures, and explicit exceptions.

## Validation and evolution

Review validation on 2026-10-26 is documentation-only: repository navigation passed for 18 Markdown files and tracked whitespace checks passed. These checks do not qualify a new renderer or establish source/parser coverage.

Implementation may begin only after approval and should start with failing fixtures for:

- a repository-owned container with implementation but no component decomposition;
- one canonical interface provided by one component and consumed by several components;
- one shared library used by several containers without duplicate API content;
- the same source under two materially different compile/documentation profiles;
- several language projects in one coherent extraction profile;
- unmapped required architecture bindings, conflicting ownership, duplicate canonical keys, stale C4 IDs, and missing expected symbols;
- generated container/component/interface backlinks, compatibility stubs, source links, and orphan cleanup;
- clean-checkout reproducibility and zero-diff freshness in CI;
- preservation of rich native comments, compiler/native symbol coverage, relationship provenance, and recorded parser limitations.

Fitness signals are: one canonical page per validated symbol context, no duplicated symbol content across configured C4 views, every generated C4 view linked to approved architecture, every canonical page linked back to all configured views, explicit included/excluded coverage, and deterministic regeneration on supported platforms. Reopen the decision if canonical profile identity is unstable, shared-library navigation requires copying content, architecture bindings cannot be validated without source coupling, or a selected language cannot support the required native/Doxygen evidence chain.

## Deferred decisions and open questions

- Define project-specific stable documentation-profile identities and establish evidence before consolidating two target configurations into one reference.
- Define project-specific inventory selectors for architecturally significant non-public ports without enabling blanket private extraction.
- Qualify each consuming project's implementation layout, language constructs, visibility scope, and compiler/native inventory before claiming coverage; the war-strategy-game document comparison alone does not do so.
- Reconcile handwritten contract documents and diagrams against source-backed contracts during each project migration; where they disagree, preserve the discrepancy as an unresolved finding until authoritative evidence identifies the correction.
- Complete the repository-intelligence APP runtime/container boundary review before assigning its final production selectors.
- Keep any source namespace, assembly, package, or visibility reorganization outside this decision until a separate design slice is approved.
