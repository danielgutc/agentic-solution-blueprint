# Verification Evidence

## Default

Report verification results in the conversation. Do not create or maintain a standalone verification report for routine tests, reviews, retries, or handoffs.

At a meaningful handoff or approval gate, retain only the evidence needed for the next decision in the existing task tracker, traceability matrix, readiness record, or other owning artifact. Prefer updating the current entry over appending a chronological log of every command or retry. Routine iteration results may remain in chat until such a boundary.

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

Create a separate report only when the user explicitly requests it or an approved project-specific delivery, audit, or compliance obligation explicitly requires that deliverable. Identify that obligation and scope. Existing report files, examples, skill wording such as "report results," and a specialist handoff do not establish such a requirement.

Executable evidence, independent verification where required, honest verdicts, traceability, and approval gates remain mandatory for their applicable scope. A missing standalone report must not block a gate when the required evidence is already available in the existing records.

Apply this policy when coordinating specialist output: request conclusions, evidence, limits, and owner actions in the reply, without requiring a report path.
