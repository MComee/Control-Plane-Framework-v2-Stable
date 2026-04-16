#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
POLICY = ROOT / 'framework' / 'policy' / 'canonical-policy.json'
METADATA = ROOT / 'project' / 'now' / 'metadata.json'
RUN_CONTEXT_ROOT = ROOT / 'project' / 'run_context'
README = ROOT / 'README.md'


def fail(msg: str) -> None:
    print(f'FAIL: {msg}')
    raise SystemExit(1)


def load_json(path: Path):
    if not path.exists():
        fail(f'missing file: {path}')
    return json.loads(path.read_text(encoding='utf-8'))


def main() -> int:
    policy = load_json(POLICY)
    metadata = load_json(METADATA)

    if metadata.get('policy_source') != 'framework/policy/canonical-policy.json':
        fail('metadata policy_source does not point to canonical policy')

    if metadata.get('policy_version') != policy.get('policy_version'):
        fail('metadata policy_version does not match canonical policy version')

    mode = metadata.get('execution_mode') or policy.get('default_execution_mode')
    modes = policy.get('execution_modes', {})
    if mode not in modes:
        fail(f'unknown execution mode: {mode}')

    mode_cfg = modes[mode]
    if metadata.get('allowed_paths') != mode_cfg.get('allowed_paths'):
        fail('metadata allowed_paths does not match canonical policy mode')
    if metadata.get('forbidden_paths') != mode_cfg.get('forbidden_paths'):
        fail('metadata forbidden_paths does not match canonical policy mode')

    required_paths = [
        ROOT / 'project' / 'docs' / 'priorities',
        ROOT / 'project' / 'evidence',
        RUN_CONTEXT_ROOT,
        RUN_CONTEXT_ROOT / 'active',
        RUN_CONTEXT_ROOT / 'audit',
        RUN_CONTEXT_ROOT / 'root',
        RUN_CONTEXT_ROOT / 'tree',
    ]
    for path in required_paths:
        if not path.exists():
            fail(f'missing required path: {path.relative_to(ROOT)}')

    readme_text = README.read_text(encoding='utf-8')
    for needle in [
        'framework/policy/',
        'canonical-policy.json',
        'project/run_context/',
        'framework/validators/',
    ]:
        if needle not in readme_text:
            fail(f'README tree appears missing reference: {needle}')

    template = ROOT / 'framework' / 'templates' / 'run-context-node-template.md'
    if not template.exists():
        fail('missing run-context node template')
    template_text = template.read_text(encoding='utf-8')
    for field in policy.get('run_context_node_invariants', []):
        if field.replace('_', ' ') not in template_text.lower() and field not in template_text:
            fail(f'run-context template appears missing invariant field: {field}')

    print('PASS: canonical policy, metadata, README references, and run-context scaffold are aligned')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
