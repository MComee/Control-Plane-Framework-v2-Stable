# Control Plane Framework v2 Stable

Repository-native control framework for AI-assisted software development.

## Operating Intent
- Govern repository truth and execution alignment.
- Control one project per repository instance under `project/`.
- Keep planning state synchronized to repository files.
- Drive execution from `project/now/` with one-tool-at-a-time handoff.
- Validate that protected and forbidden boundaries were respected.
- Preserve a complete recursive repository map in this root `README.md`.
- Add a recursive run-context layer that helps constrained local models execute bounded work without losing parent intent.

## Scope Statement
This framework governs repository truth, planning state, task decomposition, active work, and evidence.
It does not govern AI internals.

## Core Model

### Layer 1 — Framework Self-Governance
Protects doctrine, routing, protected paths, planning synchronization, execution boundaries, and repository-visibility compliance.

### Layer 2 — Single-Project Control
Governs one project under `project/`, including vision, decomposition, priorities, active work, and evidence.

### Layer 3 — Execution Guidance
Guides one chosen tool at a time through `project/now/`, with explicit allowed and forbidden scope.

### Layer 4 — Recursive Run Context
Provides a repository-backed working memory for constrained models.

This layer does not replace project truth. It translates project truth and current execution intent into a recursive, auditable tree of bounded execution nodes.

Each execution node must preserve:
- root objective traceability
- parent objective traceability
- inherited constraints
- local success criteria
- dependency context
- allowed writable surfaces

No leaf task may exist without an ancestry chain back to the current run root.

## Compliance Rule: Full Repository Visibility
The root `README.md` is the universal inspection entrypoint.

This file must always contain a fully recursive, exact tree of every file and every directory in this repository.

No repository paths are excluded from visibility compliance based on file type, stack, language, framework role, or subsystem role.

If any path is added, removed, renamed, moved, or reclassified, this tree must be updated in the same change set. Any mismatch is framework non-compliance.

## Recursive Run-Context Rule
Run-context decomposition must be hierarchical, recursive, and ancestry-preserving.

This framework forbids one-shot flattening of a full prompt directly into context-free leaf tasks.

Decomposition must proceed through logical levels so that every executable leaf node preserves why it exists, what larger objective it serves, and what inherited constraints remain in force.

At the start of a model's next pass on the same branch, the active run-context working set may be regenerated. Prior run-context snapshots must remain auditable under `project/run_context/audit/`.

## Repository Tree (All Paths)
```text
.
├── README.md
├── docs/
│   ├── control-model.md
│   ├── overview.md
│   ├── routing.md
│   ├── run-context.md
│   └── start-here.md
├── framework/
│   ├── rules/
│   │   ├── execution-boundaries.md
│   │   ├── planning-sync.md
│   │   └── protected-files.md
│   └── templates/
│       ├── active-work-template.md
│       ├── feature-template.md
│       ├── run-context-node-template.md
│       ├── task-group-template.md
│       └── task-template.md
└── project/
    ├── app/
    │   └── README.md
    ├── docs/
    │   ├── decisions.md
    │   ├── definition_of_done.md
    │   ├── execution_control.md
    │   ├── features/
    │   │   ├── FEAT-001-repository-truth-control.md
    │   │   └── README.md
    │   ├── priorities/
    │   │   ├── blocked.md
    │   │   ├── done.md
    │   │   ├── later.md
    │   │   ├── next.md
    │   │   └── now.md
    │   ├── roadmap.md
    │   ├── task_groups/
    │   │   ├── README.md
    │   │   └── TG-001-structural-compliance-and-active-work-control.md
    │   └── tasks/
    │       ├── README.md
    │       └── TASK-001-normalize-v2-structure-and-control-locations.md
    ├── evidence/
    │   ├── artifacts/
    │   │   └── .gitkeep
    │   ├── run_logs/
    │   │   └── .gitkeep
    │   └── test_runs/
    │       └── .gitkeep
    ├── now/
    │   ├── description.md
    │   ├── metadata.json
    │   └── prompt.md
    ├── run_context/
    │   ├── README.md
    │   ├── active/
    │   │   ├── blocked.md
    │   │   ├── completed.md
    │   │   ├── current_node.md
    │   │   └── execution_queue.md
    │   ├── audit/
    │   │   ├── last_run_prompt.md
    │   │   ├── last_run_summary.md
    │   │   └── last_tree_snapshot.md
    │   ├── root/
    │   │   └── README.md
    │   └── tree/
    │       └── README.md
    └── vision/
        ├── brainstorming.md
        ├── constraints.md
        └── core_vision.md
```
