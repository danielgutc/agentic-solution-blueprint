---
name: blueprint-sync-pr
description: Sync upstreamable blueprint-governance changes to the blueprint repository and create or update the required pull request. Use when governance changes fall under the blueprint sync scope.
---

# Blueprint Sync PR Skill

Use this skill when upstreamable blueprint-governance changes must be synced to the blueprint repository.

## Trigger conditions

- Changed files fall inside the governance scope defined in `.blueprint/instructions/process/blueprint-sync.md`.
- A governance change commit is ready for upstream sync.

## Prechecks

- Confirm scope and policy from `.blueprint/instructions/process/blueprint-sync.md`.
- Confirm governance commit is isolated from solution-specific changes.

## Workflow

1. Execute the sync flow from `.blueprint/instructions/process/blueprint-sync.md`.
2. Push governance commit to solution `origin` before final reporting.
3. Push to the blueprint remote using the same stable branch name as the local sync branch, for example `blueprint/war-strategy-game`.
4. If needed, remediate branch state or cherry-pick issues without violating `blueprint/main` base policy.

## Failure handling

- If auth token is expired or unavailable, report exact remediation and keep sync branch pushed.
- If an existing PR branch exists, update the stable `blueprint/{project-name}` branch rather than opening duplicates or creating per-change branch names.

## Validation checklist

- Sync result conforms to `.blueprint/instructions/process/blueprint-sync.md`.
- Final report includes branch name and PR link (or explicit auth blocker).
