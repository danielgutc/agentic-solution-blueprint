# Reusable repository tools

The blueprint includes executable documentation utilities, their tests, and neutral fixtures. They require Python 3.11 or later and the standard library. Doxygen is an external, project-pinned prerequisite when extracting source; Draw.io and Graphviz are not bundled.

| Tool | Purpose | Usage |
| --- | --- | --- |
| [Doxygen Markdown generator](docs/generate_doxygen_docs.py) | Render a configured Doxygen XML inventory into component guides, API pages, and relationship sources. | [Configuration and limits](docs/doxygen-tooling.md); `python tools/docs/generate_doxygen_docs.py --help` |
| [Markdown checker](docs/check_navigation.py) | Check local files, heading anchors, and contents lists. | `python tools/docs/check_navigation.py --help` |
| [Draw.io SVG utility](diagrams/export_drawio_svg.py) | Export/check supported uncompressed diagrams, source freshness, and drill-down links. | [Supported subset](diagrams/README.md); `python tools/diagrams/export_drawio_svg.py --help` |

Copy the tool files listed in [the portable manifest](../.blueprint/tooling.toml) from the same revision as the adopted `.blueprint/` copy. Preserve project-specific adapters, source ownership maps, tool pins, configuration, and executable contract tests. Example configuration is not a project decision and must be adapted and capability-qualified before it drives enduring generated documentation.

The generic tools do not contain a solution's container/component names, application source, approved architecture diagrams, build/package commands, or framework-specific parser workarounds. Keep those in the consuming repository. Record known parser limitations and uncovered quality gates rather than describing tool availability as implementation readiness.

Before implementation readiness can be approved, the selected stack must also expose repository-owned build, unit/component/contract test, formatting/static-analysis, packaging, and delivery commands. Record their working directories in `design/foundation/tech.md`; CI should invoke the repository commands.
