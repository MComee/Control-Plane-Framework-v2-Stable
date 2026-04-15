# TG-001 Structural Compliance and Active-Work Control

**Task Group ID:** `TG-001`

**Linked Feature:**
- `FEAT-001`

**Purpose:**
Keep structure, priorities, and active-work handoff synchronized to repository truth.

**Included Tasks:**
- `TASK-001` Normalize v2 structure and control file locations

**Dependencies:**
- `project/docs/definition_of_done.md`
- `project/docs/execution_control.md`

**Ordering:**
1. Complete structure normalization first.
2. Refresh routing/control docs and path policies.
3. Rebuild README tree last, after all file moves and edits.

**Risks:**
- Drift between README tree and actual tracked files
- Scope leakage into protected planning artifacts during execution
- Duplicate control surfaces for priorities or evidence

**Exit Condition:**
All tasks in this group are complete and all required path, boundary, and evidence checks pass.
