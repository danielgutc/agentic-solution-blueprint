# Portable Doxygen documentation tools

The [generator](generate_doxygen_docs.py) and [renderer](doxygen_markdown.py) use Python 3.11+ and the standard library. The tool reads Doxygen XML and emits component-owned `code.md`, per-type `api/<scope>/` Markdown, and `_code-diagrams/types.mmd`. Guides and API pages contain architecture/source backlinks, provenance and reproduction commands. Guides include authored type guidance and structural relationship tables/diagrams.

## Configure a project

Copy [doxygen.example.json](doxygen.example.json) and adapt every placeholder. The JSON paths `repository_root`, `doxyfile`, and `doxygen_xml` are relative to the JSON file. Component output and architecture paths are relative to `repository_root`. Adapt [Doxyfile.example](Doxyfile.example); Doxygen runs from its directory, so its relative input/output paths use that directory.

Pin the exact output of your accepted executable's `doxygen --version`, including a build identifier when present. There is no blueprint-wide Doxygen version. Build/native documentation validation and capability fixtures remain project-owned prerequisites. Configure an existing, approved component architecture page; the renderer leaves that page unchanged. After generation succeeds, add a direct link from its `Code documentation` section to `code.md`.

```powershell
python tools/docs/generate_doxygen_docs.py --config tools/docs/doxygen.json --run-doxygen
python tools/docs/generate_doxygen_docs.py --config tools/docs/doxygen.json --run-doxygen --check
python tools/docs/check_navigation.py
```

Use `--doxygen <executable>` for a tool outside PATH. Without `--run-doxygen`, generation reads an existing XML export; its declared release version must match the configured release. The build identifier is checked only when the executable is run. This mode does not prove XML freshness against source. CI must run the pinned exporter or separately establish freshness before checking the Markdown.

Ownership selectors are a union of configured qualified-name prefixes, source-path prefixes, and explicit Doxygen compound IDs. Every discovered supported public/protected compound must match exactly one component. `expected_symbols` is an independently established inventory, ideally emitted by the language compiler/native API validator. The tool compares it with the parsed inventory and fails on missing or unexpected types; it does not discover a compiler-complete inventory itself. Qualified names use native Doxygen notation, with C# namespace separators normalized to dots.

Generation fails for unresolved base relationships, unsupported documentation tags, missing source files, conflicting ownership, path collisions, missing expected types, and output files owned by another generator or an author. `--check` writes no Markdown and reports missing/stale/orphan outputs. Normal generation removes only orphan files carrying this generator's exact first-line marker, inside configured output directories. Inspect the configuration before applying it to an existing project.

## Tests and fixtures

```powershell
python -m unittest tools.docs.test_generate_doxygen_docs tools.docs.test_check_navigation tools.diagrams.test_export_drawio_svg_portable
```

Tests copy the neutral [fixture](fixtures/doxygen-generic/config.json) into ignored `artifacts/` temporary directories. They exercise rich XML rendering, references, code spacing, real Doxygen nested description shapes, ownership and coverage failures, architecture/source links, freshness/orphans, and protection of human-owned files. They do not require Doxygen or .NET. The checked-in XML is a renderer fixture, not evidence that every language construct was extracted correctly. A separate local smoke test with installed Doxygen 1.18.0 was performed on the fixture's simple C# interface/class sources; this is bounded capability evidence, not a universal tool pin.

## Supported scope and limits

The baseline renders class, interface, and struct compounds, their public/protected members, source locations, documented base relationships, and signature references reported by Doxygen. It preserves supported paragraphs, lists, parameter/type-parameter and exception descriptions, return sections, inline references, and code listings. Unknown description tags fail explicitly.

Namespace-level enum/free-function documentation, modern C# records/primary-constructor normalization, compiler XML sidecars for dropped XML tags, semantic inherited-documentation qualification, external base normalization, and full compiler-signature coverage need a project adapter and capability fixtures. The generic renderer does not implement those profiles. It cannot infer runtime calls, trust guarantees, test results, or architecture intent from code structure. Keep an existing project adapter when it supplies these semantics; do not replace it with this baseline merely because the baseline tool is available.

## Adopting updates

The [portable manifest](../../.blueprint/tooling.toml) lists the scripts, documentation, tests, and fixtures to copy from the same revision as the pinned `.blueprint/` files. The [tools guide](../README.md) describes the bundle. Keep project-specific source mappings, compiler adapters, accepted versions, CI acquisition details, and executable contracts outside that manifest. Doxygen itself is an external executable; Draw.io/Graphviz are external optional tools rather than bundled binaries.
