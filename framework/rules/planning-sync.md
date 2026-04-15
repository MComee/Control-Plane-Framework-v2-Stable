# Planning Synchronization Rule

Planning must be synchronized to repository files.

Any planning cycle must update, as needed:
- `project/vision/`
- `project/docs/features/`
- `project/docs/task_groups/`
- `project/docs/tasks/`
- `project/docs/priorities/`
- `project/docs/roadmap.md`
- `project/docs/decisions.md`
- `project/docs/definition_of_done.md`
- `project/docs/execution_control.md`
- `project/now/`

No planning state may remain only in chat.

Repository visibility requirement:
- root `README.md` must contain a fully recursive and exact tracked file tree
- any tracked file or path change requires corresponding tree update in `README.md`
