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
