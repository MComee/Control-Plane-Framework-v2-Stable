# Start Here

This framework governs repository truth and execution alignment. It does not govern AI internals.

## Invariants
- One repository instance controls one project under `project/`.
- Planning state must live in repository files, not chat-only state.
- Execution must consume `project/now/`, with `project/now/prompt.md` as handoff source.
- Validation must confirm protected boundaries and forbidden paths were respected.
- Root `README.md` must remain a fully recursive, exact mirror of repository paths.
- Recursive run-context decomposition must preserve logical ancestry from root objective to executable leaf.
- Human review must remain at convergence and promotion gates.

## Operator Sequence
1. Read `project/vision/core_vision.md`.
2. Read `docs/overview.md`, `docs/control-model.md`, `docs/routing.md`, `docs/run-context.md`, and `docs/human-review-model.md`.
3. Read `project/now/description.md`, `project/now/prompt.md`, and `project/now/metadata.json`.
4. Approve or reject the prompt and run intent before execution.
5. If using a constrained model, regenerate `project/run_context/` from current project truth and current prompt.
6. Select only the current executable node plus its ancestry chain.
7. Execute only within metadata and prompt boundaries.
8. Write evidence under `project/evidence/` and run-context audit material under `project/run_context/audit/`.
9. Review branch outcomes before any keep / reject / defer decision.
10. Approve convergence or promotion explicitly before applying accepted results.
11. If repository paths changed, update the root README tree in the same change set.
