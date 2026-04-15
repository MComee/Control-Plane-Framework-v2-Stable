# FEAT-001 Repository Truth Control

**Feature ID:** `FEAT-001`

**Name:** Repository Truth Control and Handoff Discipline

**Objective:**
Keep repository truth stable so one tool can execute one bounded task at a time without ambiguity.

**Scope:**
- Canonical project structure under `project/`
- Stable planning decomposition across features, task groups, and tasks
- Active-work handoff through `project/now/`
- Evidence capture in `project/evidence/`

**Out of Scope:**
- AI model internals, prompting internals, or model policy control
- Multi-project orchestration inside one repository instance

**Dependencies:**
- `project/vision/core_vision.md`
- `project/vision/constraints.md`
- `framework/rules/protected-files.md`
- `framework/rules/planning-sync.md`

**Related Task Groups:**
- `TG-001`

**Acceptance Conditions:**
- Repository paths match the required v2 architecture
- Planning state exists in `project/docs/` and not in chat-only form
- `project/now/` is initialized with one active task and explicit boundaries
- `README.md` contains a fully recursive, exact tree of tracked files
