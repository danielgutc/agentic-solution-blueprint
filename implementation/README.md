# Implementation

This folder is the default implementation root. It contains repository-owned implementation units: independently understandable build, test, or packaging workspaces for code, schemas, migrations, customized images, or other source-controlled implementation assets.

Implementation units and C4 containers answer different questions. A unit owns repository files and tool scope; a C4 container owns a runtime responsibility or data boundary. Record their mapping in `design/foundation/tech.md` instead of copying C4 identifiers into the directory tree.

## Delivery phases

- During technical design, create only the walking skeleton, source interfaces, representative tests, and documentation-tool integration needed for implementation readiness.
- Begin full feature implementation only after `design/foundation/implementation-readiness.md` approves the relevant scope.
- Implement approved behavior through TDD and keep generated code documentation current through repository tooling.

## Typical shape

```text
implementation/
  <unit>/
    src/          # optional, ecosystem dependent
    tests/        # optional developer-close tests
    docs/         # optional unit-local documentation
    artifacts/    # generated unit output, ignored
    <toolchain files>
```

Use sibling units for independently built or released services. A documented single-unit project can use this directory as its toolchain root. A unit may be polyglot when its files share one owner and lifecycle. Do not create empty directories for future containers, languages, or test levels.

Cross-unit integration and end-to-end suites belong under `tests/`. Deployment topology belongs under `deployment/`, repository automation under `tools/`, and aggregate generated output under `artifacts/`. If a registered implementation, test, or aggregate-artifact path changes, update the root `.gitignore` rules for both direct and nested workspace outputs. Follow `.blueprint/instructions/standards/implementation-layout.md` for the normative rules.
