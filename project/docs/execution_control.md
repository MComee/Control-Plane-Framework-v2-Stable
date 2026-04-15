# Execution Control

Execution is bound to the current active-work package under `project/now/`.

## Current binding surfaces
- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

## Rules
- Read required context before editing anything.
- Change only allowed paths.
- Do not mutate protected planning artifacts during standard execution.
- Record evidence under `project/evidence/`.
- If tracked paths changed, update the root `README.md` tree in the same change set.
