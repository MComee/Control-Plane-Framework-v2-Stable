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
- `project/run_context/` for recursive, auditable, constrained-model working memory.

## Execution Contract
- Planning and routing must stay synchronized to repository files.
- External execution consumes `project/now/prompt.md` and `project/now/metadata.json`.
- Allowed and forbidden path boundaries must be respected and validated.
- The root `README.md` tree must always exactly match repository paths.

## Recursive Run-Context Intent
The framework now supports a hybrid recursive execution style inspired by hierarchical decomposition.

This does not replace stable project truth. Instead, it creates a run-local working tree for one model and one branch so that smaller models can operate on bounded context without losing parent intent.

A valid run-context tree must:
- begin with a run root node derived from the current prompt and project truth
- decompose through intermediate logical levels before creating executable leaves
- preserve ancestry, rationale, constraints, and success criteria at every node
- keep audit snapshots of prior run trees rather than silently overwriting history
