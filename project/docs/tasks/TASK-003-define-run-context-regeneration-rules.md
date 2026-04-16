# TASK-003 — Define Run-Context Regeneration Rules

## Purpose
Define how the active run-context working set is regenerated at the start of a model's next pass series without destroying auditability.

## Dependencies
- `FEAT-002-recursive-run-context-control.md`
- `TG-002-recursive-run-context-foundation.md`

## Required Output
Document regeneration rules covering:
- when the active run-context tree may be cleared
- what must be rebuilt from stable project truth and current prompt
- what prior run materials must be preserved under audit
- how current-node and queue state are re-established

## Completion Criteria
- regeneration rules are documented in framework doctrine
- regeneration rules distinguish active working memory from preserved audit history
- the rules do not allow silent destruction of prior run evidence
