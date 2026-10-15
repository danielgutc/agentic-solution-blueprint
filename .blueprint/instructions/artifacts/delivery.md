# Delivery Artifact

## Purpose

Use `design/foundation/delivery.md` to define project-specific CI/CD stages, evidence, trust boundaries, artifact flow, exceptions, and recovery before delivery automation becomes authoritative.

## Canonical shape

Use `.blueprint/templates/foundation/delivery.template.md`.

## Ownership boundary

- The blueprint defines reusable capability and evidence semantics.
- The project owns provider workflows, tools and versions, repository rules, credentials, environments, tests, registries, deployments, and promotions.
- Extract shared executable automation only after multiple projects prove meaningful duplication and stable contracts.

## Authoring rules

- State which checks are advisory, merge-blocking, deployment-blocking, or promotion-blocking.
- Keep untrusted proposed-change validation separate from trusted deployment authority.
- Prefer repository-owned commands over logic embedded only in provider YAML.
- Identify the implementation unit or aggregate repository scope and working directory for every command. Do not make one unit's toolchain configuration govern unrelated units accidentally.
- Build an immutable artifact once and promote it when practical.
- Map each applicable test level to its execution stage.
- Record evidence formats, retention, owners, retry behavior, rollback, and recovery.
- Make exceptions owned, expiring, and compensated by explicit evidence.
- Keep unit-local generated outputs separate from aggregate packages, reports, and API documentation under the registered repository artifacts path.

Framework-agnostic candidates such as Robot Framework, OPA/Conftest, JUnit, SARIF, portable coverage, CycloneDX/SPDX, and OCI attestations remain options until the project selects them in `tech.md`.
