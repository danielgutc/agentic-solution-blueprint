# Blueprint Sync

Use this process when an upstreamable blueprint change is made.

## Default policy

- Treat blueprint-governance changes as upstreamable by default.
- Blueprint governance scope:
  - `AGENTS.md`
  - `design/instructions/**`
  - `design/templates/**`
  - `design/samples/**`
  - `.codex/skills/**`
  - `tasks.md`
- Treat files outside this scope as solution-specific unless explicitly requested for blueprint sync.

## Sync flow

1. Create the local change in the solution repository.
2. Commit upstreamable blueprint-governance files in a dedicated commit.
3. For blueprint sync, create or reset a local sync branch from `blueprint/main`.
4. Cherry-pick the upstreamable commit(s) onto that branch.
5. Push to a blueprint sync branch (for example `blueprint/codex/sync-blueprint-governance-{solution-repo}`).
6. Create or update PR titled:
   - `Sync blueprint governance from {solution repo name}`
7. Report branch name and PR URL.

## History safety rule

Always base the sync branch on `blueprint/main` before pushing. Do not push a branch based on `origin/main` into blueprint.
