# Developer Guide

## Intent

This guide explains how to use Control Plane Framework v2 Stable in public, executor-agnostic terms.

It is written for developers who want to use CPF with existing chat tools, existing command-line coding agents, or their own compatible tooling.

This guide does not prescribe one required executor.
It does not describe any private toolchains.

---

## What CPF is

Control Plane Framework v2 Stable is a repository-native control framework for AI-assisted software development.

Its purpose is to preserve project truth in repository files rather than in transient chat context alone.

CPF gives you:
- a controlled project structure under `project/`
- explicit vision, constraints, roadmap, priorities, features, task groups, and tasks
- active-work handoff surfaces under `project/now/`
- evidence surfaces under `project/evidence/`
- optional local reference structure under `project/references/`
- optional `chat` branch support for persistent planning alignment

---

## Branch roles

### `main`
Accepted stable line.

### `dev`
Accepted working development baseline.

### `chat` (optional)
Persistent human-guided planning branch derived from `dev`.

Use it to preserve:
- vision
- constraints
- roadmap
- priorities
- feature/task decomposition
- next-step intent

The `chat` branch is planning-heavy and implementation-light by default.

### working branches
Use additional branches for bounded implementation or experimental work as needed.

---

## Basic project flow

1. create a new repository from the CPF template
2. define the project vision under `project/vision/`
3. define priorities, features, task groups, and tasks under `project/docs/`
4. define the current active work under `project/now/`
5. optionally create a `chat` branch from `dev` for persistent planning alignment
6. use your preferred tool to execute bounded work on an appropriate working branch
7. review results with a human in the loop
8. promote accepted work into `dev` and later into `main`

---

## Recommended repository familiarization

Before asking a chat tool or build tool to propose implementation prompts, it is usually best to align it to the full repository doctrine first.

Recommended familiarization order:
1. read the root `README.md`
2. read `project/vision/`
3. read `project/docs/roadmap.md`
4. read `project/docs/priorities/`
5. read relevant feature, task-group, and task files
6. read `project/now/`
7. read `project/references/` when the project depends on local manuals or stack references

This improves continuity and reduces the risk that the chosen tool invents a parallel plan that conflicts with repository truth.

---

## Rolling prompt horizon for one chosen build tool

When using one chosen build tool or coding agent, a useful diagnostic pattern is to maintain a rolling prompt horizon rather than only a single current prompt.

Recommended structure:
- `current_prompt`
- `draft_next_prompt`
- `draft_next_plus_one_prompt`

This is not a commitment to execute future prompts unchanged.
It is a planning and diagnostic aid.

### Why it is useful
- it preserves momentum between audited rounds
- it reveals where prompt chains begin to drift
- it helps distinguish tool weakness from prompt weakness
- it makes prompt revision points easier to identify

### Promotion rule
After each audited round:
- run and review `current_prompt`
- either promote `draft_next_prompt`, revise it, or discard it
- shift `draft_next_plus_one_prompt` forward when appropriate
- regenerate a new farthest draft

### Validity condition
A draft prompt should only be promoted when the prior round remained acceptably aligned to:
- repository truth
- target stack and platform
- directory-placement expectations
- active-work boundaries
- human review requirements

### Human review rule
Draft prompts do not replace human judgment.
The operator should still decide whether the next prompt is close enough to promote, needs revision, or should be replaced by a corrective prompt.

---

## Human verification rule

CPF is human-supervised by design.

Human verification remains necessary for:
- doctrine changes
- core vision changes
- material priority changes
- convergence decisions
- promotion into accepted working or stable lines
- policy overrides
- major updates to reference bundles
- major `chat`-branch planning changes
- promotion, revision, or discard decisions for draft prompts when using a rolling prompt horizon

---

## Custom-tool compatibility

CPF is compatible with custom-built tooling as long as that tooling respects:
- repository truth surfaces
- branch roles
- active-work boundaries
- reference-layer boundaries where applicable
- mandatory human verification gates

The public framework does not require any one custom tool.

---

## Start-here checklist

- define the vision
- define constraints
- define priorities
- decompose into features, task groups, and tasks
- define current active work
- optionally create and maintain a `chat` branch
- align the chosen tool to repository doctrine before prompting for implementation work
- optionally maintain a rolling `current / next / next+1` prompt horizon for diagnostic use
- execute bounded work on an appropriate branch
- keep a human in the loop at the approval gates
