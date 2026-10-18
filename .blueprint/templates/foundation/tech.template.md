# Tech

[README](../../../README.md) / Foundation / Tech

Related foundation documents:
- [Product](./product.template.md)
- [MVP and prioritization](./mvp.template.md)
- [Requirements](./requirements.template.md)
- [Design](./design.template.md)
- [Delivery governance](./delivery.template.md)
- [Traceability matrix](./traceability-matrix.template.md)
- [Task tracker](./task.template.md)
- [Implementation readiness](./implementation-readiness.template.md)

## Table of contents

- [Languages and runtimes](#languages-and-runtimes)
- [Frameworks and platforms](#frameworks-and-platforms)
- [Build and package tools](#build-and-package-tools)
- [Implementation workspace map](#implementation-workspace-map)
- [Selected framework capabilities](#selected-framework-capabilities)
- [Testing approach](#testing-approach)
- [Developer feedback and delivery commands](#developer-feedback-and-delivery-commands)
- [API documentation and code projections](#api-documentation-and-code-projections)
- [Diagram tooling](#diagram-tooling)
- [CI/CD platform and quality gates](#cicd-platform-and-quality-gates)
- [Persistence and data ownership](#persistence-and-data-ownership)
- [Deployment model](#deployment-model)
- [Constraints](#constraints)
- [Key technical decisions](#key-technical-decisions)

## Languages and runtimes

## Frameworks and platforms

## Build and package tools

## Implementation workspace map

Use stable unit IDs. A unit maps to one or more approved C4 containers, or names its non-runtime owner and purpose. Paths are relative to the registered implementation root unless stated otherwise.

| Unit ID | Path | C4 container(s) or non-runtime owner and purpose | Toolchain root(s) | Build, test, and package entry points | Produced artifacts |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

## Selected framework capabilities

## Testing approach

## Developer feedback and delivery commands

| Capability | Unit ID or aggregate scope | Working directory | Repository command |
| --- | --- | --- | --- |
| Clean build | | | |
| Unit and component tests | | | |
| Contract tests | | | |
| Integration and end-to-end tests | | | |
| Formatting and static analysis | | | |
| API documentation and code projections | | | |
| Draw.io SVG export and link check | | | |
| Generated-document freshness check | | | |
| Versioned artifact packaging | | | |
| Non-production delivery | | | |

## API documentation and code projections

- Default parser: Doxygen
- Accepted Doxygen version and configuration path:
- Native API comment format by language:
- Capability-fixture scope and command:
- Known parser limitations and deterministic normalization:
- Approved language-specific generator exception, evidence, owner, and revisit trigger:
- Doxygen XML and other unit-local intermediate output:
- Markdown renderer and committed component guide/API-page patterns:
- Code-relationship renderer and edge-evidence policy:
- Aggregate API reference output: `artifacts/api-docs/`
- Generation, freshness, and link-validation commands:
- Publication target and retention:

## Diagram tooling

- Human-authored source format: Draw.io (`.drawio`) unless an approved exception is recorded here.
- Embedded export format: sibling `.svg`, committed with its source.
- Export command or editor workflow:
- Source/export freshness and link-validation command:
- Approved format exception, owner, and rationale (if any):

## CI/CD platform and quality gates

- Platform:
- Required implementation-readiness checks:
- Artifact strategy:
- Non-production delivery path:

## Persistence and data ownership

## Deployment model

## Constraints

## Key technical decisions
