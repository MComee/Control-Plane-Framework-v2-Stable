# TASK-002 — Define Run-Context Node Invariants

## Purpose
Define the minimum required fields and behavioral guarantees for every recursive run-context node.

## Dependencies
- `FEAT-002-recursive-run-context-control.md`
- `TG-002-recursive-run-context-foundation.md`

## Required Output
Document the required invariant fields for every node, including:
- node id
- parent id
- root id
- objective
- rationale
- inherited constraints
- dependencies
- local success criteria
- allowed writable surfaces
- status

## Completion Criteria
- invariants are written into framework doctrine
- invariants are reflected in the run-context node template
- no executable node is left context-free
