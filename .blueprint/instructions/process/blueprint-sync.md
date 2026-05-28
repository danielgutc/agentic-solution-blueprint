# Blueprint Sync

Use this process when an upstreamable blueprint change is made.

## Default policy

- Treat blueprint-governance changes as upstreamable by default.
- Blueprint governance scope:
  - `AGENTS.md`
  - `.blueprint/instructions/**`
  - `.blueprint/templates/**`
  - `.blueprint/samples/**`
  - `.codex/skills/**`
  - `tasks.md`
- Treat files outside this scope as solution-specific unless explicitly requested for blueprint sync.

## Sync flow

1. Create the local change in the solution repository.
2. Commit upstreamable blueprint-governance files in a dedicated commit.
3. For blueprint sync, create or reset the stable local sync branch from `blueprint/main`.
   - Branch naming convention: `blueprint/{project-name}`.
   - For this repository, use `blueprint/war-strategy-game`.
4. Cherry-pick the upstreamable commit(s) onto that branch.
5. Push to the blueprint remote using the same branch name as the local sync branch.
   - Example: local branch `blueprint/war-strategy-game` pushes to remote branch `blueprint/war-strategy-game`.
   - Reuse this branch for future syncs instead of creating new per-change sync branches.
6. Create or update PR titled:
   - `Sync blueprint governance from {solution repo name}`
7. Report branch name and PR URL.

## History safety rule

Always base the sync branch on `blueprint/main` before pushing. Do not push a branch based on `origin/main` into blueprint. When updating an existing sync branch, reset or rebase the local `blueprint/{project-name}` branch onto `blueprint/main`, replay the isolated governance commit(s), and push back to the same remote branch name.
