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

The product owner records MVP scope and version 1.0 acceptance intent. Solution and technical architects own alignment with the intended architecture and extension evidence. Implementation and infrastructure roles satisfy the approved contracts and delivery obligations; independent verification owns the acceptance verdict. The coordinator records policy approval, downstream re-review needs and the next owner in the task tracker.

When adopting these rules in an existing project, preserve earlier PoC results and approvals as scoped history. Record any required MVP compliance review without marking existing builds or the product version as 1.0-ready. Do not silently broaden functional scope, prescribe a project per container, or start a structural refactor as part of a policy update.
