# Human Review Model

## Purpose

This framework is human-supervised by design.

It may automate bounded execution mechanics, validation support, artifact capture, recursive run-context preparation, and draft generation, but it must not remove the operator from judgment-heavy decisions.

## Human review must remain

The operator must remain in the loop for:
- prompt approval before execution
- policy override decisions
- keep / reject / defer decisions across competing branch outputs
- convergence approval before selected results are applied to a convergence branch
- promotion approval before results move into a stable or accepted branch
- doctrine or vision changes that alter framework intent or project intent

## Automation is acceptable

Automation is acceptable for bounded, pre-approved support work such as:
- local branch checkout and branch hygiene
- bounded generation within approved writable surfaces
- validator execution
- artifact capture and evidence writing
- recursive run-context generation and refresh
- changed-file summaries and diff summaries
- staging only allowed paths
- preparing convergence drafts after human decisions are already recorded

## Rule

Automation may assist judgment.
Automation may not replace the operator at judgment gates.

## Practical interpretation

A valid workflow is:
1. a human approves the prompt and run intent
2. the tool performs bounded local work
3. the human reviews branch outcomes
4. the human decides what to keep, reject, revise, or defer
5. the approved decision is recorded durably in the repository
6. only then may approved changes be applied to a convergence or stable line
