# FEAT-002 — Recursive Run-Context Control

## Objective
Add a constrained-model run-context subsystem that preserves logical ancestry from root objective to executable leaf and supports auditable regeneration between pass series.

## Why
Smaller local models cannot safely rely on full prompt retention across long execution cycles. The framework needs a repository-backed working-memory plane that reduces active context while preserving parent intent and inherited constraints.

## Scope
In scope:
- recursive run-context doctrine
- node invariants
- regeneration rules
- execution-node contract
- audit retention rules
- scaffold files and templates

Out of scope:
- specific app implementation logic
- model-specific vendor tuning
- replacement of stable project truth surfaces

## Acceptance Conditions
- `project/run_context/` exists as a governed project surface.
- Recursive decomposition is defined as ancestry-preserving and anti-flattening.
- Executable leaf nodes require explicit ancestry, constraints, and writable-surface boundaries.
- Prior run-context state remains auditable after regeneration.
- Feature decomposition is represented by an explicit task group and atomic tasks.

## Related Task Groups
- `TG-002-recursive-run-context-foundation.md`
