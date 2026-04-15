# Control Model

The framework uses a three-layer control model.

## Layer 1 — Framework Self-Governance
Protects framework doctrine, routing rules, protected paths, planning synchronization, execution boundaries, and repository visibility compliance.

## Layer 2 — Single-Project Control
Applies under `project/` and governs:
- `project/vision/`
- `project/docs/features/`
- `project/docs/task_groups/`
- `project/docs/tasks/`
- `project/docs/priorities/`
- `project/now/`
- `project/evidence/`

## Layer 3 — Execution Guidance
Guides one chosen tool at a time by defining:
- required reads
- allowed changes
- forbidden changes
- validation and evidence obligations

`project/now/prompt.md` is the execution handoff source.

## Control Assertions
- This framework controls repository truth and execution alignment, not AI internals.
- One repository instance controls one project.
- Planning state must be synchronized to repository files.
- Execution must consume `project/now/`.
- Validation must confirm protected boundaries were respected.
- Root `README.md` must remain a fully recursive, exact mirror of tracked repository paths.
