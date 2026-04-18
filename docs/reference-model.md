# Reference Model

## Intent

This framework may govern repositories that depend on authoritative local reference material.

The purpose of the reference layer is to reduce guesswork, preserve local-first operation, and make implementation work more reliable for constrained or smaller local models.

This is especially important when the target project depends on:
- languages
- frameworks
- libraries
- APIs
- platform tooling
- system manuals
- version-sensitive conventions

---

## Rule

When a project materially depends on an external technical stack or technical domain knowledge, the repository should include a local **reference layer** under `project/references/`.

This layer is intended to hold:
- curated local manuals
- stack guidance
- API references
- framework notes
- compatibility notes
- local reference indexes
- troubleshooting notes

The reference layer is read-oriented by default.
It is not an ordinary implementation surface.

---

## Purpose of the reference layer

The reference layer exists to support:
- local-first development
- bounded offline or low-connectivity operation
- more reliable code generation
- framework- and stack-aware planning
- branch- or domain-specific knowledge expansion

It should help the active tool or model reason from authoritative local material rather than from weak memory or stale assumptions alone.

---

## Expected repository structure

The canonical framework shape includes:
- `project/references/README.md`
- `project/references/index.md`
- `project/references/stack_profile.json`

Subdirectories may then be added per project need, such as:
- `languages/`
- `frameworks/`
- `libraries/`
- `apis/`
- `platforms/`
- `tooling/`
- `troubleshooting/`
- domain-specific reference packs

This structure is intentionally extensible.

---

## Stack profile rule

The project should declare its active stack in `project/references/stack_profile.json`.

This should identify, at minimum:
- project type
- major languages
- frameworks
- major libraries
- tooling
- major API dependencies
- reference priority order if known

This allows reference use to be explicit rather than implicit.

---

## Read/write doctrine

The reference layer is read-only by default for normal implementation rounds.

Reference maintenance should occur only when explicitly authorized.

Ordinary implementation or planning passes may read from the reference layer but should not modify it unless the round explicitly includes reference maintenance in scope.

---

## Human review rule

The operator should review which references are included for a project and whether they are:
- relevant
- authoritative
- appropriately versioned
- legally safe to store in the chosen repository context

Large documentation dumps are discouraged when a curated reference bundle would serve better.

---

## Best practice

Prefer:
- curated summaries
- indexed official excerpts where permitted
- version-aware notes
- focused troubleshooting references
- stack-specific local bundles

Do not rely on a large unstructured document dump as the primary knowledge plane.
