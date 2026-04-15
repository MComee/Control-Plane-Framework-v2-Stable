# Overview

Control Plane Framework v2 Stable is a repository-native control framework for AI-assisted software development.

## Scope
- Governs repository truth, planning state, and execution alignment.
- Governs one controlled project per repository instance.
- Does not attempt to control AI model internals.

## Required Project Surfaces
- `project/vision/` for project doctrine.
- `project/docs/features/`, `project/docs/task_groups/`, and `project/docs/tasks/` for decomposition.
- `project/docs/priorities/` for lane state.
- `project/now/` for active-work handoff.
- `project/evidence/` for run logs, test runs, and artifacts.

## Execution Contract
- Planning and routing must stay synchronized to repository files.
- External execution consumes `project/now/prompt.md` and `project/now/metadata.json`.
- Allowed and forbidden path boundaries must be respected and validated.
- The root `README.md` tree must always exactly match tracked repository paths.
