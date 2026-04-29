# Blueprint Sync PR Skill

Use this skill when upstreamable blueprint-governance changes must be synced to the blueprint repository.

## Trigger conditions

- Changed files fall inside the governance scope defined in `design/instructions/process/blueprint-sync.md`.
- A governance change commit is ready for upstream sync.

## Prechecks

- Confirm scope and policy from `design/instructions/process/blueprint-sync.md`.
- Confirm governance commit is isolated from solution-specific changes.

## Workflow

1. Execute the sync flow from `design/instructions/process/blueprint-sync.md`.
2. Push governance commit to solution `origin` before final reporting.
3. If needed, remediate branch state or cherry-pick issues without violating `blueprint/main` base policy.

## Failure handling

- If auth token is expired or unavailable, report exact remediation and keep sync branch pushed.
- If an existing PR branch exists, update it rather than opening duplicates.

## Validation checklist

- Sync result conforms to `design/instructions/process/blueprint-sync.md`.
- Final report includes branch name and PR link (or explicit auth blocker).
