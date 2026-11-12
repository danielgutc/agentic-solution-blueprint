# Blueprint Templates

Before authoring, choose the canonical existing owner and update it in place. Materialize registered canonical artifacts only when their lifecycle requires them, using only the sections needed for current enduring decisions and contracts. Omit empty sections, redundant links, and unnecessary contents lists under [navigation](../instructions/standards/navigation.md). Follow [documentation and verification evidence](../instructions/standards/verification-evidence.md): keep acceptance criteria in requirements/tests, current decisions and needed evidence references in existing gate records, and execution results in chat or generated outputs. Template headings and requests for reports, evidence, acceptance, or handoffs do not require a document per task, phase, or handoff, or standalone acceptance/assessment/evidence documents. Additional enduring documents require a `documentation.additional_authored_documents` entry with `path`, `owner`, `reason`, and `review_trigger`; an explicit user report request overrides the default only for its named scope.

These files define canonical starting shapes for enduring project artifacts.

- Instructions explain why and how to author an artifact.
- Templates define its reusable structure.
- Canonical files under `design/` contain current project decisions and needed evidence references.

When a structural convention changes, update the instruction, template, seeded artifact, navigation README, and `.blueprint/blueprint.toml` path or gate declaration together. Implementation workspace changes also follow `.blueprint/instructions/standards/implementation-layout.md`.

Foundation templates link to sibling `.template.md` files so they are navigable in this repository. When materializing one in `design/foundation/`, change those links to the artifact `.md` names and adjust the README, C4, and diagram links for the destination directory. The seeded foundation files already have project-relative links.

C4 templates include navigation examples that resolve in this blueprint checkout. When materializing them deeper in `design/c4/`, adjust the breadcrumb and next-level paths, then embed only diagrams whose Draw.io source and sibling SVG export exist. Do not create or approve C4 views before the design gate.
