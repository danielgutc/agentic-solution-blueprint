# MVP Version 1.0 Quality

## Purpose

The MVP is the first production-quality version 1.0 of the product, with the smallest approved useful feature scope. It establishes the lasting foundation for the known product roadmap. A proof of concept (PoC) is a separate experiment that establishes feasibility; a successful PoC is evidence, not an MVP release.

## Rules

1. **Use the final technical architecture for the approved scope.** Implement the MVP against the approved intended system/container boundaries, component responsibilities, contracts, data ownership and operational design. Resolve architecture-significant decisions before implementing their scope. Do not knowingly ship a temporary architecture that must be replaced to continue the approved roadmap.
2. **Treat the MVP as version 1.0.** The supported MVP journeys must be complete and releasable within their declared limits, with all applicable functional, quality, documentation, delivery and acceptance obligations met. Reduce features or supported scope to stay minimal; do not reduce engineering standards. Development builds, walking skeletons, pilots and experimental packages are not automatically release 1.0.
3. **Build later capabilities on the MVP foundation.** The known approved roadmap must be able to extend the architecture without first replacing or correcting shortcut-driven structure in the MVP. Record extension evidence or a reasoned design review for known later capabilities. Do not prebuild those features, speculative abstractions or infrastructure merely to claim extensibility.
4. **Keep PoC shortcuts out of the MVP.** Temporary storage, combined roles, broad dependencies, stubs, manual procedures or other simplified approaches are acceptable only when they satisfy the approved production architecture and release obligations for the supported scope. If used solely to accelerate an experiment, label and bound them as PoC-only. Reused experiment code must meet the same architecture, implementation and verification standards as newly written product code before version 1.0 acceptance; relabeling or a passing smoke test is insufficient.

A final architecture is the approved production-intent baseline for the implemented scope and known roadmap, not a claim that future requirements cannot change. Routine code refactoring to maintain that architecture remains valid. New requirements, discoveries or operating evidence may justify architectural evolution through the owning role and approval gate. That possibility does not excuse a known structural rewrite planned as a prerequisite for delivering the existing roadmap.

## Evidence and release decision

- Product and MVP artifacts identify the version 1.0 outcome, included and deferred scope, and any separate PoC or pilot evidence.
- Architecture and technical design explain how the implemented foundation supports the known next capabilities; unsupported assumptions remain open decisions. The solution/project/package layout follows approved ownership and dependency needs. A shared solution or release is not itself a shortcut; weakening required boundaries for MVP speed is.
- Traceability and integrated verification establish the supported journeys and applicable quality contracts. A walking skeleton proves selected seams; it does not establish complete version 1.0 acceptance.
- Track PoC-to-product gaps, temporary mechanisms and their removal or qualification under named owners before release. Existing scoped evidence remains valid for its recorded revision and guarantee; it must not silently become proof of production readiness.
- Record version 1.0 release acceptance separately from implementation-readiness approval. An approved process exception or bounded experiment may permit learning work; it cannot waive the production-quality baseline while retaining the version 1.0 MVP claim. Resolve the gap or obtain approval to reduce the supported feature scope and update its evidence.

## Adoption and ownership

This is project-authoring guidance for the blueprint. Develop the rationale in the project's product and architecture artifacts; do not install it as a blanket policy in global Codex/Copilot coordinator instructions or repeat it in every engineering role.

- The product owner owns the product rationale in `design/foundation/product.md` and `mvp.md`: users, smallest useful outcome, included and deferred journeys, quality and acceptance intent, learning evidence, and sequencing. Architecture choices remain with the architects.
- The solutions architect owns the solution rationale in `design/foundation/design.md`: why the selected production architecture satisfies that scope and its quality scenarios, alternatives and tradeoffs, known roadmap extension evidence, assumptions, and re-review triggers. Supporting technology decisions belong in `tech.md`.
- The technical architect owns the technical rationale in container/component-owned documents under `design/c4/containers/`: responsibilities, contracts, dependencies, data structures, test seams, and evidence that realizes the approved direction. Foundation links this detail without duplicating it.
- Implementation and infrastructure roles satisfy the resulting approved project contracts and delivery obligations. Independent verification assesses the recorded acceptance criteria and reports evidence and gaps. These roles do not redefine the MVP rationale.
- The coordinator routes work, records approval and downstream re-review needs in the task tracker, and preserves phase ownership. A role definition or generic skill assigns responsibility and method; it does not substitute for project-specific rationale or approval.

When adopting these rules in an existing project, preserve earlier PoC results and approvals as scoped history. Record any required MVP compliance review without marking existing builds or the product version as 1.0-ready. Do not silently broaden functional scope, prescribe a project per container, or start a structural refactor as part of a policy update.
