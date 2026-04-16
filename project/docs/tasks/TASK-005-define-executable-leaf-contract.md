# TASK-005 — Define Executable Leaf Contract

## Purpose
Define the contract for executable leaf nodes so that no model executes context-free work detached from parent intent.

## Dependencies
- `FEAT-002-recursive-run-context-control.md`
- `TG-002-recursive-run-context-foundation.md`
- `TASK-002-define-run-context-node-invariants.md`

## Required Output
Document the executable leaf contract, including:
- required ancestry chain
- current node objective
- inherited constraints
- allowed writable surfaces
- local success criteria
- minimum project surfaces required for execution

## Completion Criteria
- execution doctrine forbids leaf execution without ancestry
- leaf execution is bounded and auditable
- writable-surface scope is explicit at leaf level
