# Control Model

The framework uses a four-layer control model.

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

## Layer 4 — Recursive Run Context
Applies under `project/run_context/` and governs bounded execution for constrained models.

This layer must:
- preserve the full run root objective
- recursively decompose objectives through logical intermediate levels
- prevent direct flattening from root prompt to context-free leaf tasks
- preserve parent-child ancestry for every node
- preserve inherited constraints and local completion criteria
- preserve audit snapshots of prior run-context trees

### Run-Context Separation Rule
`project/run_context/` is not a replacement for project truth.

Project truth remains under the stable project surfaces, especially:
- `project/vision/`
- `project/docs/`
- `project/now/`
- `project/evidence/`

The run context is an execution-local working memory generated from those sources for one model, one branch, and one pass series.

### Execution Node Rule
No executable leaf node may exist without:
- a root id
- a parent id
- a statement of why the node exists
- inherited constraints
- local success criteria
- allowed writable surfaces

## Control Assertions
- This framework controls repository truth and execution alignment, not AI internals.
- One repository instance controls one project.
- Planning state must be synchronized to repository files.
- Execution must consume `project/now/`.
- Validation must confirm protected boundaries were respected.
- Root `README.md` must remain a fully recursive, exact mirror of all repository paths.
- Recursive run-context decomposition must preserve logical ancestry from root objective to executable leaf.
