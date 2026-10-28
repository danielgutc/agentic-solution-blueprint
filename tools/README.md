# Reusable repository tools

The blueprint includes executable documentation utilities, their tests, and neutral fixtures. They require Python 3.11 or later and the standard library. Doxygen is an external, project-pinned prerequisite when extracting source; Draw.io and Graphviz are not bundled.

| Tool | Purpose | Usage |
| --- | --- | --- |
| [Doxygen Markdown generator](docs/generate_doxygen_docs.py) | Publish profile-canonical API pages plus configured container, component, interface, and migration-link views. | [Configuration and limits](docs/doxygen-tooling.md); `python tools/docs/generate_doxygen_docs.py --help` |
| [Markdown checker](docs/check_navigation.py) | Check local files, heading anchors, and contents lists. | `python tools/docs/check_navigation.py --help` |
| [Draw.io SVG utility](diagrams/export_drawio_svg.py) | Export/check supported uncompressed diagrams, source freshness, and drill-down links. | [Supported subset](diagrams/README.md); `python tools/diagrams/export_drawio_svg.py --help` |

Copy the tool files listed in [the portable manifest](../.blueprint/tooling.toml) from the same revision as the adopted `.blueprint/` copy. Preserve project-specific adapters, source ownership maps, tool pins, configuration, and executable contract tests. Example configuration is not a project decision and must be adapted and capability-qualified before it drives enduring generated documentation.

The schema-version-2 example is intentionally the simple one-profile, no-component-decomposition case. Consuming projects supply stable architecture IDs, expected compiler/native symbol inventories, explicit source ownership and interface-exposure bindings, source coverage/exclusions, compatibility windows, and any ecosystem adapter. Schema version 1 remains executable only as a deprecated migration path.

The generic tools do not contain a solution's container/component names, application source, approved architecture diagrams, build/package commands, or framework-specific parser workarounds. They validate configured expected symbols against Doxygen's bounded supported compounds but do not claim compiler-complete semantics. Keep project-specific inventory producers and adapters in the consuming repository. Record known parser limitations and uncovered quality gates rather than describing tool availability as implementation readiness.

Before implementation readiness can be approved, the selected stack must also expose repository-owned build, unit/component/contract test, formatting/static-analysis, packaging, and delivery commands. Record their working directories in `design/foundation/tech.md`; CI should invoke the repository commands.
