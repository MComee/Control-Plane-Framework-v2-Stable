# Chat Branch Model

## Intent

This document defines the role of a `chat` branch for projects created from this framework.

The purpose of the `chat` branch is to preserve a high-fidelity human-guided planning state so future chat sessions can realign to the project without reconstructing everything from memory.

---

## Core rule

A CPF-derived project may include a `chat` branch derived from `dev`.

The `chat` branch is not a primary implementation lane.
It is the persistent human-guided alignment branch.

---

## Why the `chat` branch exists

Long-running or restarted chat sessions can lose:
- project identity
- constraints
- priority order
- recursive decomposition
- next-step intent
- the distinction between accepted planning truth and raw brainstorming

The `chat` branch exists to preserve those things in repository form.

---

## What the `chat` branch should preserve

The `chat` branch should emphasize:
- core vision
- constraints
- roadmap
- priorities
- feature decomposition
- task-group decomposition
- atomic tasks
- recursive list-of-lists style planning where useful
- next-step intent
- human-guided interpretation of what the implementation lanes are trying to become

---

## What the `chat` branch should not primarily do

The `chat` branch should not be used as the main place for:
- broad application implementation
- uncontrolled experimentation in app files
- random transcript dumping
- replacing accepted implementation branches

It may read the whole project for alignment, but it should remain planning-heavy and implementation-light by default.

---

## Relationship to other branches

### `main`
Accepted stable line.

### `dev`
Accepted working development baseline.

### model lanes
Candidate planning or implementation lanes used for bounded generation and comparison.

### `chat`
Persistent human-guided alignment lane used to preserve high-fidelity project planning state across chat sessions.

---

## Human verification rule

The `chat` branch is not a silent auto-authority.

Human verification remains mandatory when changes to `chat` materially affect:
- core vision
- constraints
- project direction
- priority ordering
- accepted decomposition
- convergence decisions
- promotion of planning truth into accepted working or stable lines

Automation and chat assistance may propose or structure these changes, but final acceptance remains a human-in-the-loop gate.

---

## Mental model

The `chat` branch is to project planning what pseudocode is to code.

It captures the truest structured intent first so future chat sessions and later implementation lanes can translate from that intent without losing hierarchy or priorities.

---

## Recommended operating loop

1. align the chat session to the `chat` branch
2. read vision, constraints, roadmap, priorities, features, task groups, and tasks
3. inspect implementation branches as needed
4. update planning truth in `chat`
5. verify human approval for material planning changes
6. generate better bounded prompts for implementation lanes
7. review implementation results
8. fold accepted planning updates back into `chat`
9. converge accepted implementation results into `dev` or later stable branches

---

## Lisp-like sketch

```lisp
(chat-branch
  (role persistent-human-guided-alignment)
  (preserves
    (vision)
    (constraints)
    (roadmap)
    (priorities)
    (features)
    (task-groups)
    (tasks)
    (next-step-intent))
  (reads whole-project-for-alignment)
  (human-verification-required-at-material-planning-gates)
  (not primary-implementation-lane))
```
