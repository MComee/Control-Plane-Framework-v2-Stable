# TASK-004 — Define Run-Context Audit Retention Rules

## Purpose
Define what run-context materials must be preserved for audit after a pass series completes or a new pass series begins.

## Dependencies
- `FEAT-002-recursive-run-context-control.md`
- `TG-002-recursive-run-context-foundation.md`

## Required Output
Document audit retention rules covering:
- full prompt snapshot retention
- tree snapshot retention
- run summary retention
- branch/model/tool traceability
- storage location under `project/run_context/audit/`

## Completion Criteria
- audit retention doctrine is explicitly written
- regeneration is not allowed to erase required audit artifacts
- a reviewer can reconstruct the previous run-context state from preserved records
