# Portable Doxygen documentation tools

The [generator](generate_doxygen_docs.py), [profile publication model](doxygen_publication.py), and bounded [Doxygen XML renderer](doxygen_markdown.py) use Python 3.11+ and the standard library. Schema version 2 publishes one canonical API reference per implementation-unit/documentation-profile context, then generates container, optional component, and interface link views. Exact signatures appear only on canonical API pages.

Schema version 1 remains executable for migration but is deprecated. It keeps its historical component-owned output and emits a CLI warning. New configurations use schema version 2.

## Configure schema version 2

Copy [doxygen.example.json](doxygen.example.json) and adapt every placeholder. Paths for `repository_root`, each `doxyfile`, and each `doxygen_xml` directory are relative to the JSON file. Architecture, evidence, compatibility, and output paths are repository-relative. Doxygen runs from each Doxyfile's directory.

The top-level shape is:

- `architecture.containers[]`: stable `id`, reader title, container `output_dir`, and existing human-authored `architecture_page`;
- optional `architecture.components[]`: the same fields plus `container_id`; an implementation-bearing container does not need a component decomposition;
- `profiles[]`: stable `id`, `implementation_unit`, Doxygen inputs, declared parser limitations and source coverage, native/compiler inventory evidence, expected symbols, architecture bindings, and optional migration stubs.

Each profile computes, rather than configures, its canonical root:

```text
design/code/<implementation-unit>/<profile>/index.md
design/code/<implementation-unit>/<profile>/api/<scope>/<stable-symbol-key>.md
```

A single `default` profile is the normal simple case. Add another profile only when target, compile symbols, language adapter, or another material build input yields a distinct validated public surface. Several projects may share a profile when their extraction and native inventory evidence are coherent.

Every `symbols[]` entry declares `key`, `qualified_name`, `api_scope`, and at least one explicit selector: `compound_ids[]`, `qualified_names[]`, or `source_prefixes[]`. These entries are the expected exported inventory for the supported compound set. `inventory_evidence` links the independently produced compiler/native evidence; the generic tool validates that the configured expected list exactly matches the Doxygen projection but does not parse arbitrary ecosystem inventory formats or claim compiler-complete extraction.

`parser_limitations[]` and `source_coverage.included[]` are required. `source_coverage.excluded[]` contains explicit `{scope, reason}` entries and may be empty. Generated canonical and architecture-view pages disclose coverage, bounded supported compound/visibility scope, parser limits, inventory evidence, and reproduction provenance.

## Architecture bindings and views

Bindings identify a `symbol_key`, `container_id`, optional `component_id`, and one role:

- `owned-implementation`: the one architectural owner of the source declaration in that profile;
- `provided-interface`: a configured provided port;
- `consumed-interface`: a configured consumed port;
- `supporting-code`: shared or supporting code used by the target.

Only `owned-implementation` is exclusive. Provided and consumed bindings describe architectural use; the same declaration may validly appear in several provided or consumed views. Interface roles also require `interface_scope` of `external-runtime` or `internal-component`. This exposure is an explicit architectural claim, not an inference from language visibility or from whether a component implements the port.

Bindings generate:

```text
design/c4/containers/<container>/code.md
design/c4/containers/<container>/_code-views/interfaces.md  # only with interface bindings
design/c4/containers/<container>/components/<component>/code.md  # only when bound
```

The container page is the reader entry. Interface pages distinguish external runtime ports from internal component ports. Component pages are optional filtered guides. These views may carry configured narrative and source-authored purpose text, but they link exact signatures to canonical pages rather than copying signature inventories. Each canonical page links back to every generated view deterministically.

Shared libraries are extracted once for each materially distinct profile and may bind to several containers. Shared interfaces keep one canonical page in that profile while owner, provider, and consumer views link to it.

## Migration stubs and cleanup

`compatibility_stubs[]` maps an old repository-relative API page `path` to a `symbol_key`. A stub contains only a generated moved notice and canonical link. Every stub must be inside a declared `legacy_stub_roots[]` boundary. The consuming project records its compatibility window and removal review separately.

Normal generation removes stale files only when they are inside a configured canonical root, configured architecture-view location, or declared legacy stub root and carry this generator's exact first-line ownership marker. It never deletes or overwrites a human-owned file. `--check` writes nothing and reports missing, stale, or orphan generated files.

## Run and validate

Pin the exact output of each accepted `doxygen --version`, including a build identifier when present. There is no blueprint-wide Doxygen executable pin.

```powershell
python tools/docs/generate_doxygen_docs.py --config tools/docs/doxygen.json --run-doxygen
python tools/docs/generate_doxygen_docs.py --config tools/docs/doxygen.json --run-doxygen --check
python tools/docs/check_navigation.py
python -m unittest tools.docs.test_generate_doxygen_docs tools.docs.test_check_navigation tools.diagrams.test_export_drawio_svg_portable
```

Use `--doxygen <executable>` when the selected executable is outside `PATH`. Without `--run-doxygen`, the generator consumes existing XML. That mode checks the XML release marker but does not establish freshness against source; CI must run the pinned extractor or separately prove XML freshness.

Generation fails closed for unsafe or colliding paths and IDs, missing source/native evidence, missing or ambiguous selectors, duplicate symbol keys, expected-inventory mismatches, stale architecture IDs/pages, component/container inconsistency, missing binding targets, conflicting `owned-implementation` bindings, output collisions, broken generated links, and attempts to replace human-owned files.

## Tests and bounded support

The portable fixtures exercise deprecated schema v1 and schema v2: no component decomposition, one shared interface with several providers/consumers, a shared profile bound to two containers, two distinct profiles, deterministic backlinks, compatibility stubs, invalid selectors and bindings, ownership/path collisions, staleness, coverage/provenance, and marker-only orphan cleanup. They require neither Doxygen nor .NET.

The generic parser deliberately supports public/protected class, interface, and struct compounds plus their public/protected members, source locations, documented base relationships, and signature references reported by Doxygen. It preserves the documented paragraph, list, parameter, exception, return, inline-reference, and code-listing subset covered by fixtures. Unsupported description tags fail explicitly.

Namespace-level enum/free-function documentation, compiler XML sidecars, modern language constructs not preserved by Doxygen, semantic inherited-documentation qualification, external base normalization, and complete compiler signature semantics require project adapters and capability fixtures. The renderer cannot infer runtime calls, trust guarantees, test results, source ownership, component boundaries, or interface exposure from code. Preserve a consuming project's adapter when it supplies those semantics.

## Adopting updates

The [portable manifest](../../.blueprint/tooling.toml) lists scripts, documentation, tests, and fixtures that must move together from the pinned blueprint revision. Keep project-specific inventory producers, adapters, Doxyfiles, accepted versions, CI acquisition details, architecture bindings, and executable contract tests outside that reusable manifest.
