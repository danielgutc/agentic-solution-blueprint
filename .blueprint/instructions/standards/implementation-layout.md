# Implementation Workspace Layout

## Purpose

Use implementation workspaces to contain repository-owned source, configuration, validation, packaging, and developer commands without making the filesystem mirror the C4 model.

## Terms

- The **repository root** contains cross-unit governance, assembled verification, deployment assets, orchestration, and aggregate outputs.
- The **implementation root** is the concrete path registered as `paths.implementation` in `.blueprint/blueprint.toml`.
- An **implementation unit** is an independently understandable build, test, or packaging workspace under the implementation root. It can contain application code, schemas, migrations, a customized image, generated-client inputs, or more than one language.
- A **toolchain root** is the directory from which a language or build tool resolves its workspace-wide configuration and commands.

## Relationship to C4

- C4 containers describe runtime responsibilities and deployment or data boundaries. Implementation units describe repository ownership and tool scope. Do not create either boundary solely to mirror the other.
- Map each implementation unit in `design/foundation/tech.md` to its approved C4 container or containers. When a unit is not a runtime container, record its owner and purpose instead.
- A managed service or stock image can be a C4 container without a repository implementation unit.
- One implementation unit can own an application and an embedded data store when they share source, lifecycle, and packaging.
- Separately deployed or independently released runtime containers normally use separate implementation units. Record and justify an exception in `tech.md`.
- Keep source paths out of C4 identifiers and diagrams. Record the mapping in foundation and traceability artifacts.

## Placement rules

- In a blueprint project, use `<implementation-root>/<unit>/` for multiple units. A documented single-unit project can use the implementation root directly.
- A non-blueprint repository can retain an established root-level workspace. A blueprint consumer that places implementation at the repository root must explicitly change `paths.implementation` and document the exception.
- Name units for stable owned responsibilities, not a language, framework, IDE solution, or temporary delivery phase.
- A unit can use ecosystem-native structure. When useful, prefer unit-local `src/`, `tests/`, `docs/`, and generated `artifacts/` directories plus the unit's solution, package, workspace, or build files.
- Place toolchain configuration at the narrowest scope that intentionally governs all affected projects. Do not let one unit inherit another unit's SDK, dependency, analyzer, output, or formatting policy by accident.
- Keep developer-close unit, component, and contract tests with their implementation unit. Keep assembled integration and end-to-end suites at the registered repository test paths, with suite-local generated output ignored like unit output.
- Keep deployable topology, infrastructure, and environment composition at `paths.deployment`; repository automation at `paths.tools`; and aggregate packages, reports, and API documentation at `paths.repository_artifacts`.
- Generated unit output belongs under the unit's `artifacts/` directory unless the selected tool requires a different ignored location. Aggregate outputs belong under the registered repository artifacts path.
- When registered implementation, test, or repository-artifact paths change, update root-anchored ignore rules to cover the concrete paths, including both direct workspaces and nested units or suites.
- Do not create empty directories to anticipate a future C4 container, language, test level, or deployment target.

## Commands and evolution

- Record every build, test, documentation, packaging, and delivery command with its working directory and unit or aggregate scope in `design/foundation/tech.md`.
- CI must invoke those commands from the recorded working directory and assemble cross-unit evidence explicitly.
- Preserve an existing valid workspace layout unless an approved migration has a clear benefit, owner, rollback path, and updated commands.
- Reassess implementation readiness when a unit boundary, toolchain root, package boundary, or command working directory changes.

## Review scenarios

Check the layout against at least these cases when the convention changes:

- one blueprint implementation unit using the implementation root directly
- two independent .NET services with different SDK or dependency policies
- a mixed-language implementation unit with one owned lifecycle
- an application with an embedded data store and a managed external data service
