# Protected File Rules

## Protected paths
The following paths are protected and cannot be modified during standard execution:
- `README.md`
- `docs/*`
- `framework/rules/*`
- `framework/templates/*`
- `project/vision/*`
- `project/docs/features/*`
- `project/docs/task_groups/*`
- `project/docs/priorities/*`
- `project/docs/roadmap.md`
- `project/docs/decisions.md`
- `project/docs/definition_of_done.md`
- `project/docs/execution_control.md`

## Restricted paths
The following paths are restricted and may be modified only by planning-authorized updates:
- `project/docs/tasks/*`
- `project/now/*`

## Allowed paths
The following paths are allowed for standard execution outputs:
- `project/app/*`
- `project/evidence/*`

Violation = invalid execution.
