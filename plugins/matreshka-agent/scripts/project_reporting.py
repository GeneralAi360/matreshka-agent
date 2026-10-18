#!/usr/bin/env python3
"""One project / one stable offline report. Run with --help; all input is JSON data."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

from project_report_model import (EVENTS, ReportError, digest, file_hash, projection,
                                  require, validate)
from project_report_store import guard, initialize, inventory, load, location, read_json, recover, update


def template(product_root, documentation_root, project_id, title, goal):
    return {'project': {'id': project_id, 'title': title, 'goal': goal,
                        'product_root': str(Path(product_root).absolute()),
                        'documentation_root': str(Path(documentation_root).absolute())},
            'plan': {'revision': 0, 'status': 'UNKNOWN', 'source_ids': [],
                     'approval': {'status': 'UNKNOWN', 'source_ids': []}, 'steps': []},
            'sources': [], 'evidence': [], 'runs': [], 'conflicts': [],
            'current': {'title': 'Восстановление требований и плана', 'status': 'IN_PROGRESS',
                        'checkpoint': {'summary': 'Подтверждённое состояние ещё не установлено', 'evidence_ids': []},
                        'next_action': {'summary': 'Изучить актуальные документы и определить разрешённый объём',
                                        'permission': 'UNKNOWN', 'source_ids': []},
                        'blockers': [], 'questions': []},
            'limitations': ['Сведения восстанавливаются по источникам; неизвестное не считается выполненным.']}


def record_run(directory, expected_revision, run, summary):
    """Explicit run binding records detail only. It never completes a step or adds proof."""
    previous = load(directory)
    document = copy.deepcopy(previous['document'])
    existing = next((r for r in document['runs'] if r['id'] == run['id']), None)
    if existing:
        if existing == run:
            require(previous['revision'] == expected_revision, 'stale revision: reload')
            return previous
        document['runs'][document['runs'].index(existing)] = run
    else:
        document['runs'].append(run)
    return update(directory, document, expected_revision, 'REFRESHED', summary)


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest='command', required=True)
    new = sub.add_parser('template', help='Print an unknown-state document; writes no files')
    for option in ('product-root', 'documentation-root', 'id', 'title', 'goal'):
        new.add_argument('--' + option, required=True)
    init = sub.add_parser('init', help='Initialize the single report under the documentation root')
    init.add_argument('--input', required=True)
    for name in ('status', 'inspect', 'recover', 'update'):
        cmd = sub.add_parser(name)
        cmd.add_argument('--project-dir', required=True)
        if name == 'update':
            cmd.add_argument('--input', required=True)
            cmd.add_argument('--expected-revision', required=True, type=int)
            cmd.add_argument('--event', required=True, choices=sorted(EVENTS - {'ADOPTED', 'RECOVERED'}))
            cmd.add_argument('--summary', required=True)
            cmd.add_argument('--source-id', action='append', default=[])
        if name == 'recover':
            cmd.add_argument('--expected-file-sha256', required=True)
    inv = sub.add_parser('inventory', help='Print metadata delta; never assigns document authority')
    inv.add_argument('--input', required=True)
    inv.add_argument('--previous', help='Previous inventory JSON; output remains stdout only')
    return p


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    args = parser().parse_args()
    try:
        if args.command == 'template':
            result = template(args.product_root, args.documentation_root, args.id, args.title, args.goal)
            validate(result)
        elif args.command == 'init':
            result = initialize(read_json(Path(args.input)))
        elif args.command == 'update':
            result = update(Path(args.project_dir), read_json(Path(args.input)), args.expected_revision,
                            args.event, args.summary, args.source_id)
        elif args.command == 'recover':
            result = recover(Path(args.project_dir), args.expected_file_sha256)
        elif args.command == 'inspect':
            path = guard(Path(args.project_dir) / 'report.html')
            guard(Path(args.project_dir) / 'HEAD.json')
            result = {'report': str(path), 'file_sha256': file_hash(path) if path.exists() else 'MISSING',
                      'notice': 'Inspection is read-only. Recovery requires a separate explicit command.'}
        elif args.command == 'inventory':
            previous = read_json(Path(args.previous))['files'] if args.previous else None
            result = inventory(validate(read_json(Path(args.input))), previous)
        else:
            envelope = load(Path(args.project_dir))
            result = {'state': envelope, 'projection': projection(envelope['document'])}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ReportError, OSError, KeyError, TypeError) as exc:
        print('Project reporting: BLOCKED — ' + str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
