# Foundation Artifact: agent-topology.md (optional)

## Purpose

Define how agent roles collaborate on complex tasks without embedding workflow mechanics into product/design artifacts.

## Canonical structure

- Use `.blueprint/templates/foundation/agent-topology.template.md` when this artifact is needed.

## Authoring rules

- Keep roles responsibility-focused, not person-specific.
- Define ownership boundaries and handoff contracts.
- Apply `.blueprint/instructions/standards/design-by-contract.md` to handoff contracts.
- Keep escalation paths explicit for approval gates and blocked work.
- Keep this artifact optional and lightweight; use only when multi-agent coordination adds value.

## Quality checklist

- Each role has clear scope and outputs.
- Handoffs are contract-based and testable.
- Handoff preconditions, outputs, and failure/escalation semantics are explicit.
- Escalation and authority boundaries are explicit.
