# TASK-001 Normalize v2 structure and control locations

**Task ID:** `TASK-001`

**Title:** Normalize v2 structure and control file locations

**Parent Feature:**
- `FEAT-001`

**Parent Task Group:**
- `TG-001`

**Purpose:**
Ensure the repository uses one canonical layout for planning, active work, evidence, and visibility control.

**Dependencies:**
- `framework/rules/planning-sync.md`
- `framework/rules/protected-files.md`

**Allowed Scope:**
- `README.md`
- `docs/`
- `framework/templates/`
- `project/docs/`
- `project/now/`
- `project/evidence/`

**Forbidden Scope:**
- `project/vision/`
- `project/app/` implementation files unrelated to control framework setup

**Completion Criteria:**
- All controlled surfaces exist in canonical locations
- Only one priorities location exists at `project/docs/priorities/`
- Only one evidence surface exists at `project/evidence/`
- README reflects the exact tracked tree

**Validation Expectations:**
- Spot-check all referenced paths
- Confirm no duplicate control surfaces remain

**Evidence Expectations:**
- Validation evidence under `project/evidence/run_logs/`

**Status:** `done`
