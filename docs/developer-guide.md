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
- execute bounded work on an appropriate branch
- keep a human in the loop at the approval gates
