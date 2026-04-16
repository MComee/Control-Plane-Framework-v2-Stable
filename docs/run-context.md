# Recursive Run Context

## Purpose

`project/run_context/` is the constrained-model working memory plane.

It exists to let smaller local models operate on bounded, auditable, logically connected execution context without requiring the full project prompt to remain in active model memory.

This subsystem is inspired by recursive decomposition discipline.

## Non-Goal

This subsystem does not replace:
- project vision
- project roadmap
- feature/task decomposition
- active-work handoff
- evidence retention

Those remain the stable project truth surfaces.

## Core Rule

The run context must be decomposed hierarchically.

The framework forbids flattening a full prompt directly into context-free leaf tasks.

Instead, decomposition must proceed through logical intermediate levels so that every executable node preserves:
- what larger objective it serves
- why it exists
- what constraints it inherits
- what dependencies still matter
- what completion means locally

## Separation of Planes

### Stable Project Truth
Lives under:
- `project/vision/`
- `project/docs/`
- `project/now/`
- `project/evidence/`

### Ephemeral Run Context
Lives under:
- `project/run_context/`

This plane may be regenerated at the start of a model's next pass on the same branch.

## Required Structure

A valid run-context tree should contain:
- a run root
- a recursive node tree
- an active execution state
- auditable snapshots of the last run

## Node Invariants

Every node must preserve:
- node id
- parent id
- root id
- objective
- rationale / why
- inherited constraints
- local success criteria
- dependencies
- allowed writable surfaces
- status

No executable leaf node may exist without an ancestry chain back to the root node.

## Execution Rule

A model should execute against:
- the current executable node
- the node ancestry chain
- the minimum project surfaces required
- explicit writable boundaries

A model should not be forced to hold the entire project prompt in active memory if the run-context tree already preserves the required ancestry and constraints.

## Audit Rule

At the start of a new pass series, the active run-context working set may be cleared and regenerated.

However, the previous run snapshot must remain auditable under `project/run_context/audit/`.

## Recommended Lifecycle

1. Save the full current run prompt.
2. Create the run root node.
3. Decompose recursively into logical children.
4. Continue decomposition until executable bounded leaves exist.
5. Mark one leaf as current.
6. Execute only that leaf with preserved ancestry.
7. Record results.
8. Update queue, blocked, and completed state.
9. Save audit snapshot.
