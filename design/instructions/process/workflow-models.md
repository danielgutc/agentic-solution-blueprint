# Workflow Models

Use one of these models per change set, and keep the selected model explicit in the related design conversation.

## Model 1: Requirements-first

Choose this model when desired behavior and user outcomes are clearer than technical implementation.

```text
product -> requirements -> tech -> design -> approval -> c4 -> traceability -> implementation
```

## Model 2: Design-first

Choose this model when constraints, integrations, or architecture feasibility drive decisions first.

```text
product -> tech -> design -> approval -> requirements -> c4 -> traceability -> implementation
```

## Pyramidal decomposition rule

- Start at the highest relevant abstraction level.
- Confirm and complete the current level before drilling down.
- Keep details in the artifact type matching the decision level.
- Use domain-driven boundaries while decomposing each level.

## Execution principles

Use these principles together across C4 and implementation work:

1. Domain-driven design decides what the parts are.
2. Design by Contract defines how the parts interact.
3. Test-driven development proves the contracts during implementation.

Do not introduce additional framework labels unless they add concrete workflow value.
