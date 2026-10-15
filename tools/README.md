# Tools

Repository-local scripts and developer utilities live here.

Before implementation readiness can be approved, the selected technology stack must expose stable repository-owned commands for:

- Clean build
- Unit, component, and contract tests
- Formatting and static analysis
- API documentation and code-projection generation
- Generated-document freshness verification
- Versioned artifact packaging
- Non-production delivery

Record each concrete command, its working directory, and whether it applies to one implementation unit or the assembled repository in `design/foundation/tech.md`. CI/CD workflows should invoke these commands rather than duplicate their logic.
