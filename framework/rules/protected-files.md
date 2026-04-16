# Protected File Rules

## Canonical authority
`framework/policy/canonical-policy.json` is authoritative.

This file explains the protected/restricted/allowed model in prose. If this document conflicts with the canonical policy, the canonical policy wins.

## Standard execution
During `standard_execution`, protected and forbidden surfaces include:
- `README.md`
- `docs/*`
- `framework/rules/*`
- `framework/policy/*`
- `project/vision/*`
- `project/docs/*`
- `project/now/*`

Allowed standard execution outputs are expected under:
- `project/app/*`
- `project/evidence/*`
- `project/run_context/*`

## Planning-authorized execution
During `planning_authorized`, writable surfaces may include:
- `README.md`
- `docs/*`
- `framework/templates/*`
- `project/docs/*`
- `project/now/*`
- `project/evidence/*`
- `project/run_context/*`

Planning-authorized execution still forbids mutation of:
- `framework/rules/*`
- `framework/policy/*`
- `project/vision/*`
- `project/app/*`

## Restricted-path interpretation
Restricted or protected status is mode-dependent and must be evaluated against the active execution mode declared in `project/now/metadata.json`, subject to canonical policy precedence.

Violation = invalid execution.
