# Control Plane Framework v2 Stable

Repository-native control framework for AI-assisted software development.

## Operating Intent
- Govern repository truth and execution alignment.
- Control one project per repository instance under `project/`.
- Keep planning state synchronized to repository files.
- Drive execution from `project/now/` with one-tool-at-a-time handoff.
- Validate that protected and forbidden boundaries were respected.
- Preserve a complete recursive repository map in this root `README.md`.
- Preserve human approval at convergence, promotion, and other judgment gates.

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

## Compliance Rule: Full Repository Visibility
The root `README.md` is the universal inspection entrypoint.

This file must always contain a fully recursive, exact tree of all tracked files and tracked subdirectories in this repository.

If any tracked path is added, removed, renamed, or moved, this tree must be updated in the same change set. Any mismatch is framework non-compliance.

## Human Review Rule
This framework is human-supervised by design.

The operator must remain in the loop for:
- prompt approval before execution
- keep / reject / defer decisions across branch outputs
- convergence approval before selected results are applied
- promotion approval before accepted results move into a stable branch
- policy override decisions
- doctrine or vision changes that alter framework or project intent

Automation is acceptable for bounded support work such as:
- branch checkout and branch hygiene
- bounded generation within approved writable surfaces
- validation support
- artifact capture
- changed-file and diff summaries
- staging only approved writable surfaces
- applying already-approved convergence decisions

## Repository Tree (Tracked Paths)
```text
.
├── README.md
├── docs/
│   ├── control-model.md
│   ├── human-review-model.md
│   ├── overview.md
│   ├── routing.md
│   └── start-here.md
├── framework/
│   ├── rules/
│   │   ├── execution-boundaries.md
│   │   ├── planning-sync.md
│   │   └── protected-files.md
│   └── templates/
│       ├── active-work-template.md
│       ├── feature-template.md
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
    └── vision/
        ├── brainstorming.md
        ├── constraints.md
        └── core_vision.md
```
