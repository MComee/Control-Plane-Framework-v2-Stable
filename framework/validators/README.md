# Validators

This directory contains lightweight validation tools and validator specifications for the control plane.

## Current validation focus
- metadata conformity to `framework/policy/canonical-policy.json`
- required path existence
- run-context node invariant presence
- README tree parity support
- forbidden-path drift checks

## Intended use
Validators are support tools for the human-in-the-loop workflow. They do not replace operator review; they reduce avoidable policy drift and hidden-state mistakes.
