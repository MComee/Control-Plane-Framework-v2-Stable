# Execution Boundaries

Execution is bounded by the active handoff package under `project/now/`.

## Required reads
- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

## Boundary source
`project/now/metadata.json` defines:
- `allowed_paths`
- `forbidden_paths`
- `validation_requirements`
- `evidence_paths`

## Execution rules
- Execute one active task at a time.
- Change only allowed paths.
- Do not modify forbidden paths.
- Write evidence only under `project/evidence/`.
- If tracked paths changed, update the root `README.md` tree in the same change set.

Validation must confirm boundary compliance before work is considered complete.
