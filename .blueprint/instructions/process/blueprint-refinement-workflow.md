# Blueprint Refinement Workflow

Use this process to refine blueprint changes before merging to the blueprint repository.

## PR slicing strategy

1. `structure-only` PR
   - folders, modular instruction files, templates, sample stubs
2. `AGENTS-slimming` PR
   - remove duplicated detail from `AGENTS.md`
   - keep behavior stable by pointing to modular instructions
3. `validation-and-skills` PR
   - add or tune skills and validation scripts/checklists

## Review checklist

- Is `AGENTS.md` shorter and still authoritative?
- Are detailed schemas in `.blueprint/instructions/artifacts/` instead of duplicated?
- Do templates and samples match artifact instructions?
- Do workflow and approval gates still enforce pyramidal progression?
- Are any rules contradictory across `AGENTS.md` and modular instructions?

## Acceptance criteria

- All changed rule files have clear precedence.
- No duplicate normative rule is present in more than one file unless intentionally cross-referenced.
- Task tracker schema remains reproducible from instructions and templates alone.
