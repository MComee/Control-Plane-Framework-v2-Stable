# Execution Boundaries

Execution is bounded by the active handoff package under `project/now/`.

## Required reads
- `framework/policy/canonical-policy.json`
- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

## Boundary source and precedence
The machine-readable boundary source of truth is:
- `framework/policy/canonical-policy.json`

`project/now/metadata.json` is the execution-instance binding surface. It must conform to the canonical policy and may not override higher-precedence policy rules.

## Boundary fields consumed during execution
The active execution package should expose:
- `execution_mode`
- `allowed_paths`
- `forbidden_paths`
- `validation_requirements`
- `evidence_paths`

These fields are valid only insofar as they remain aligned with the canonical policy contract.

## Execution rules
- Execute one active task at a time.
- Change only allowed paths for the active execution mode.
- Do not modify forbidden paths.
- Write evidence only under declared evidence paths.
- If repository paths changed, update the root `README.md` tree in the same change set.

Validation must confirm boundary compliance before work is considered complete.
