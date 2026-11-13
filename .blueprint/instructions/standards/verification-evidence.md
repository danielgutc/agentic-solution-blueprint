# Documentation and Verification Evidence

## Minimal and stable documentation

Keep human-authored documentation limited to current enduring decisions, contracts, constraints, rationale, and operating guidance. Before authoring, identify the canonical existing artifact that owns the content and update it in place. A task, phase, handoff, review, or test run is not a reason to create a document. Do not retain intermediate drafts, investigation narratives, per-handoff assessments, test evidence logs, or chronological status histories as project documentation. Version control preserves earlier document states.

Use the existing owners rather than adding parallel documents:

- Product and MVP artifacts own user outcomes, scope, priorities, and acceptance intent; requirements own testable acceptance criteria and quality targets.
- Design and Tech own system decisions and technical direction; approved container/component artifacts own their contracts, internal rationale, and test seams. Use a section in the owning artifact. Additional enduring documents require the registry exception below; an `Owned technical documents` heading is not permission to create one.
- Executable tests own verification scenarios and assertions; traceability links requirement IDs to architecture, implementation, and tests without repeating acceptance criteria.
- Delivery and implementation-unit/deployment guides own reproducible commands and operating procedures.
- Task and readiness artifacts are compact current-state summaries: scope, status, blockers, next owner, approval decisions, exceptions, and re-review triggers. Update or remove superseded entries rather than appending a diary. Retain the scope, authority, and conditions of approvals still relied on; removing a history never grants or broadens approval.

These rules do not change generated API documentation: retain the existing canonical per-symbol pages, source-backed views, generation, freshness, and publication obligations in [API documentation](../file-types/api-documentation.md).

## Pre-authoring decision

Before creating or expanding human-authored documentation:

1. Identify the existing canonical owner from the path registry and the responsibilities above. Update its current decision, contract, or guidance in place; consolidate superseded material rather than appending a task or phase narrative.
2. Keep execution results in the conversation or registered generated outputs. At an existing gate, retain only the current decision and the evidence references needed to assess it, including its scope, authority, conditions, and unresolved limits. Words such as "report," "assessment," "evidence," "acceptance," "approval," and "handoff" describe required information or decisions; they do not imply a new file.
3. If additional enduring content cannot fit its canonical owner, record an explicit exception in `.blueprint/blueprint.toml` under `documentation.additional_authored_documents` before creating the document. Each entry supplies `path` (the exact additional document), `owner` (the existing canonical artifact), `reason` (why the content cannot fit that owner), and `review_trigger` (when to reconsider, consolidate, or remove it). Linking a file from navigation is not an exception. Review or remove the entry and document when that trigger occurs.

The registry is an explicit exception record, not another approval gate. It does not authorize a change to product scope, architecture boundaries, or existing gate requirements. Materializing registered canonical artifacts follows their existing lifecycle; generated API pages and other registered generated outputs follow their generation policies rather than this additional-authored-document exception.

## Automated ownership check

The existing `python tools/docs/check_navigation.py` command enforces `authored_design_policy = "canonical-only"` across `authored_design_roots` in the documentation registry, including when explicit navigation inputs are selected. It admits registered foundation and system artifacts, canonical container/component pages, and their directory navigation. Other authored Markdown requires the scoped exception above. Keep the roots inclusive of the project's enduring design documentation; do not narrow them to hide reports.

Generated documentation must match the registered publication patterns or an exact `additional_generated_documents` path and carry its generator's `<!-- Generated ... -->` marker near the start. A marker alone does not admit an arbitrary file. Preserve source-backed generation and freshness checks.

The check also rejects date-first section headings and common execution-history headings. Approval dates in current decision fields remain valid. These structural checks cannot determine whether prose is durable, evidence is sufficient, or approval was granted; reviewers still assess those questions. Existing navigation checks in CI enforce the same policy without creating another report or approval gate.

## Default

Report verification results in the conversation. Do not create a report per task, phase, or handoff, or standalone acceptance, assessment, or evidence documents by default. Apply the pre-authoring decision even when a template, role, or skill asks to report results.

At a meaningful handoff or approval gate, retain only the current decision and the evidence references needed to assess it in the existing task tracker, traceability matrix, readiness record, or other owning artifact. Keep test results in the reply or generated outputs, not a narrative command/retry history. Link the applicable revision, environment, test definition, or CI run when needed to bound a claim.

## Required content

Keep the result concise and proportionate to the risk:

- Identify the scope, requirement or contract, tested revision or package, and relevant environment.
- Give the reproducible command or test identifier and observed result.
- Distinguish passing, failing, blocked, and unrun checks; state material evidence limits.
- Record unresolved defects or risks and the next owner or decision.

Link existing CI runs, test definitions, or generated evidence when useful. A new Markdown file is not needed to make evidence durable.

## Generated output

Keep logs, screenshots, machine-readable results, and other necessary generated evidence under the registered output paths for the implementation unit or assembled verification workspace. Capture only what supports reproduction, diagnosis, or an approved retention obligation. Do not add a narrative report around every generated result or copy raw output into the tracker.

## Exceptions and gates

An explicit user request for a report overrides the default only for the named deliverable and scope. It never grants blanket permission for later task, phase, handoff, or evidence reports. An approved project-specific delivery, audit, or compliance obligation may also require a specific deliverable; identify the obligation and scope. If either deliverable is retained as additional enduring project documentation, register its `path`, `owner`, `reason`, and `review_trigger` as above. Existing report files, examples, skill wording such as "report results," and a specialist handoff do not establish such a requirement. Acceptance criteria belong in requirements and executable tests, not a standalone acceptance plan or report. Record release acceptance as a distinct scoped decision in the existing MVP/task artifacts, separate from implementation-readiness approval, without creating another document.

Executable evidence, independent verification where required, honest verdicts, traceability, and approval gates remain mandatory for their applicable scope. A missing standalone report must not block a gate when the required evidence is already available in the existing records.

Apply this policy when coordinating specialist output: request conclusions, evidence, limits, and owner actions in the reply, without requiring a report path.
