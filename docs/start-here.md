# Start Here

This framework governs repository truth and execution alignment. It does not govern AI internals.

## Invariants
- One repository instance controls one project under `project/`.
- Planning state must live in repository files, not chat-only state.
- Execution must consume `project/now/`, with `project/now/prompt.md` as handoff source.
- Validation must confirm protected boundaries and forbidden paths were respected.
- Root `README.md` must remain a fully recursive, exact mirror of repository paths.
- Recursive run-context decomposition must preserve logical ancestry from root objective to executable leaf.

## Operator Sequence
1. Read `project/vision/core_vision.md`.
2. Read `docs/overview.md`, `docs/control-model.md`, `docs/routing.md`, and `docs/run-context.md`.
3. Read `project/now/description.md`, `project/now/prompt.md`, and `project/now/metadata.json`.
4. If using a constrained model, regenerate `project/run_context/` from current project truth and current prompt.
5. Select only the current executable node plus its ancestry chain.
6. Execute only within metadata and prompt boundaries.
7. Write evidence under `project/evidence/` and run-context audit material under `project/run_context/audit/`.
8. If repository paths changed, update the root README tree in the same change set.
