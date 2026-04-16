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

## Canonical Policy Rule
`framework/policy/canonical-policy.json` is the machine-readable policy source of truth.

Precedence order is:
1. `framework/policy/canonical-policy.json`
2. framework rules and doctrine docs
3. `project/now/metadata.json`
4. runner routing packet
5. tool/model behavior

Any lower-precedence surface that conflicts with the canonical policy is non-authoritative and must be brought back into alignment.

## Human Review Boundary Rule
This framework is human-supervised by design.

Human review must remain at these judgment gates:
- prompt approval before execution
- keep / reject / defer decisions across branch outputs
- convergence approval before selected results are applied
- promotion approval before accepted results move into a stable branch
- policy override decisions
- doctrine or vision changes that alter framework or project intent

Automation is acceptable for bounded support work such as:
- local execution inside approved path boundaries
- validation support
- artifact capture
- recursive run-context generation and refresh
- branch hygiene
- changed-file and diff summaries
- staging only approved writable surfaces
- applying already-approved convergence decisions

## Control Assertions
- This framework controls repository truth and execution alignment, not AI internals.
- One repository instance controls one project.
- Planning state must be synchronized to repository files.
- Execution must consume `project/now/`.
- Validation must confirm protected boundaries were respected.
- Root `README.md` must remain a fully recursive, exact mirror of all repository paths.
- Recursive run-context decomposition must preserve logical ancestry from root objective to executable leaf.
- Active metadata must conform to the canonical policy contract.
- Human judgment must remain at convergence and promotion gates.
