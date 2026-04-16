# Start Here

This framework governs repository truth and execution alignment. It does not govern AI internals.

## Invariants
- One repository instance controls one project under `project/`.
- Planning state must live in repository files, not chat-only state.
- Execution must consume `project/now/`, with `project/now/prompt.md` as handoff source.
- Validation must confirm protected boundaries and forbidden paths were respected.
- Root `README.md` must remain a fully recursive, exact mirror of tracked repository paths.
- Human review must remain at convergence and promotion gates.

## Operator Sequence
1. Read `project/vision/core_vision.md`.
2. Read `docs/overview.md`, `docs/control-model.md`, `docs/routing.md`, and `docs/human-review-model.md`.
3. Read `project/now/description.md`, `project/now/prompt.md`, and `project/now/metadata.json`.
4. Approve or reject the prompt and run intent before execution.
5. Execute only within metadata and prompt boundaries.
6. Write evidence under `project/evidence/` and validate boundary compliance.
7. Review branch outcomes before any keep / reject / defer decision.
8. Approve convergence or promotion explicitly before applying accepted results.
9. If tracked paths changed, update the root README tree in the same change set.
