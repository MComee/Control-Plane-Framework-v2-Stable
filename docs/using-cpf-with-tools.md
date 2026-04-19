# Using CPF with Tools

## Intent

This guide explains how to use Control Plane Framework v2 Stable with existing public tools in generic terms.

It is intentionally tool-agnostic in structure and does not describe any private toolchains.

---

## Supported usage patterns

CPF is designed to work with:
- chat-based assistants that can inspect repository content
- command-line coding tools that can act on repository branches
- compatible custom-built tooling that respects CPF branch roles and human verification gates

CPF does not require any one executor.

---

## Using CPF with chat-based tools

Recommended pattern:
1. open the repository
2. if a `chat` branch exists, align to it first
3. read the planning truth surfaces:
   - `project/vision/`
   - `project/docs/roadmap.md`
   - `project/docs/priorities/`
   - relevant feature, task-group, and task files
   - `project/now/`
4. refine planning truth or produce a bounded implementation instruction
5. keep a human in the loop for material planning changes and approvals

---

## Using CPF with command-line coding tools

Recommended pattern:
1. align the tool or prompt to the repository planning truth
2. choose an appropriate non-stable working branch
3. perform bounded work only
4. summarize what changed and what should happen next
5. require human review before promotion into accepted lines

Do not treat CPF as permission for uncontrolled whole-repository rewrites.

---

## Recommended start pattern for one chosen build tool

A practical diagnostic pattern is to choose one build tool or coding agent for the next round of work and maintain a rolling prompt horizon for that one tool.

Recommended prompt set:
- `current_prompt`
- `draft_next_prompt`
- `draft_next_plus_one_prompt`

This does not mean all three prompts are automatically approved.
It means the operator keeps one active prompt and two conditional draft prompts ready for review.

### Why this helps
- it preserves continuity between audited rounds
- it helps reveal where prompt chains begin to fail
- it makes it easier to see whether the problem is the tool, the prompt, or the repository state
- it reduces the need to reconstruct the next step from scratch every round

### After each round
- audit the result
- promote, revise, or discard `draft_next_prompt`
- shift `draft_next_plus_one_prompt` forward when appropriate
- create a new farthest draft

The rolling prompt horizon is a diagnostic aid, not an automation bypass.

---

## Using the `chat` branch

If present, the `chat` branch should be treated as the persistent human-guided planning branch.

Use it to preserve:
- core vision
- constraints
- roadmap
- priorities
- decomposition
- next-step intent

The `chat` branch is not the main application-buildout branch.

---

## Using the reference layer

If the project depends on stack- or domain-specific knowledge, use `project/references/`.

Minimum intended structure:
- `project/references/README.md`
- `project/references/index.md`
- `project/references/stack_profile.json`

Use curated local references rather than indiscriminate dumps.

---

## Human verification rule

Human verification remains necessary for:
- doctrine changes
- core vision changes
- material priority changes
- convergence decisions
- promotion into accepted lines
- policy overrides
- major changes to reference bundles
- major `chat`-branch planning updates
- promotion or replacement decisions for draft prompts in a rolling prompt horizon

---

## Custom-tool note

CPF is friendly to compatible custom-built tooling.

A compatible custom tool should respect:
- repository truth surfaces
- branch roles
- active-work boundaries
- reference-layer boundaries where applicable
- mandatory human verification gates

The public framework intentionally does not prescribe one custom implementation approach.
