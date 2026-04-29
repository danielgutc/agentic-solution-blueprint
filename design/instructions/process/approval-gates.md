# Approval Gates

Use this file to enforce abstraction-level gates before proceeding deeper.

## Gate sequence

```text
foundation design approved
-> system approved
-> containers approved
-> components approved
-> code phase 1 approved
-> code phase 2 approved
-> implementation interfaces approved
-> implementation tests approved
-> implementation internals approved
-> implementation
```

## Gate definitions

- Foundation design approved:
  - `design/foundation/design.md` updated and reviewed.
- System approved:
  - `design/c4/system/system.md` and system context diagram reviewed.
- Containers approved:
  - `design/c4/containers/system-containers.md` reviewed.
  - target container docs and container diagrams reviewed.
- Components approved:
  - component decomposition and interfaces reviewed per container.
- Code phase 1 approved:
  - contracts and interfaces accepted for the container.
- Code phase 2 approved:
  - architecture-level class or domain design accepted for the container.
  - no runtime implementation code required at this gate.
- Implementation interfaces approved:
  - implementation-facing skeletons apply approved C4 contracts/interfaces.
  - any implementation-only extensions are documented without violating approved C4 boundaries.
- Implementation tests approved:
  - unit and component test definitions are approved.
  - external systems are mocked at component-test level.
- Implementation internals approved:
  - internal runtime implementation satisfies approved contracts and tests.
  - implementation drift requiring architecture change is reflected in C4 artifacts and re-approved before continuation.

Do not move to the next gate until the current gate is explicitly approved.
