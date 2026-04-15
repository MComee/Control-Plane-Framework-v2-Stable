# Routing

Routing controls how one external tool receives and executes active work.

## Planning
Read:
- `project/vision/*`
- `project/docs/features/*`
- `project/docs/task_groups/*`
- `project/docs/tasks/*`
- `project/docs/priorities/*`
- `project/docs/roadmap.md`
- `project/docs/decisions.md`
- `project/docs/definition_of_done.md`
- `project/docs/execution_control.md`

Update planning files in-repo before execution handoff.

## Execution Preparation
Read:
- `project/now/description.md`
- `project/now/prompt.md`
- `project/now/metadata.json`

Confirm allowed and forbidden paths before editing anything.

## Execution
Consume `project/now/` only.

May change:
- Paths listed in `allowed_paths`

Must not change:
- Paths listed in `forbidden_paths`
- Protected planning artifacts outside explicit planning updates

## Validation
Validate:
- Required outputs and checks from `project/now/metadata.json`
- Boundary compliance against protected and forbidden paths
- Root `README.md` recursive tree remains an exact mirror of tracked repository structure
