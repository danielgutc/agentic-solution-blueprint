# Blueprint Sync

Use this process when an upstreamable blueprint change is made.

## Default policy

- Treat `AGENTS.md` changes as upstreamable by default.
- Treat other files as solution-specific unless explicitly requested for blueprint sync.

## Sync flow

1. Create the local change in the solution repository.
2. Commit `AGENTS.md` in a dedicated commit.
3. For blueprint sync, create or reset a local sync branch from `blueprint/main`.
4. Cherry-pick the upstreamable commit(s) onto that branch.
5. Push to `blueprint/codex/sync-agents-war-strategy-game`.
6. Create or update PR titled:
   - `Sync AGENTS.md from {solution repo name}`
7. Report branch name and PR URL.

## History safety rule

Always base the sync branch on `blueprint/main` before pushing. Do not push a branch based on `origin/main` into blueprint.
