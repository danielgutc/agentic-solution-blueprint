# Tests

Assembled cross-unit integration and end-to-end verification workspaces live here.

Developer-level unit, component, and contract tests normally live with their owning implementation unit. A root test suite owns its own toolchain files, commands, dependencies, and generated output; it must not inherit a service SDK or package policy accidentally. The implementation-readiness pipeline must run the initial unit-local tests before full development begins.

Follow `.blueprint/instructions/process/integrated-verification.md` for test-level boundaries and record execution stages in `design/foundation/delivery.md`.
