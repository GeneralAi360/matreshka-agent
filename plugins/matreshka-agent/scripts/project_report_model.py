"""Evidence-preserving project projection. Stdlib only; never executes source content."""
from __future__ import annotations

import copy
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path, PurePosixPath

STATUSES = {'UNKNOWN', 'NOT_STARTED', 'IN_PROGRESS', 'IMPLEMENTED_UNVERIFIED',
            'VERIFIED', 'WAITING_APPROVAL', 'BLOCKED'}
AXES = {'TECHNICAL', 'VISUAL', 'ACCEPTANCE'}
VERDICTS = {'PASS', 'FAIL', 'PARTIAL', 'BLOCKED', 'NOT_RUN', 'UNKNOWN'}
EVENTS = {'ADOPTED', 'STARTED', 'PHASE_FINISHED', 'VERIFIED', 'ERROR', 'PLAN_CHANGED',
          'USER_DECISION', 'STOPPED', 'TASK_FINISHED', 'RESOLVED', 'REFRESHED', 'RECOVERED'}
IDENTIFIER = re.compile(r'^[A-Za-z0-9][A-Za-z0-9_.-]{0,127}$')
SHA = re.compile(r'^[a-f0-9]{64}$')


class ReportError(ValueError):
    pass


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def file_hash(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def require(condition, message):
    if not condition:
        raise ReportError(message)


def timestamp(value):
    try:
        parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
        require(parsed.utcoffset() is not None, 'timestamps require a UTC offset')
        return parsed
    except (AttributeError, TypeError, ValueError) as exc:
        raise ReportError('invalid offset-aware timestamp: ' + str(value)) from exc


def identifier(value):
    require(isinstance(value, str) and bool(IDENTIFIER.fullmatch(value)), 'unsafe/missing id: ' + str(value))


def relative_path(value):
    require(isinstance(value, str) and bool(value), 'missing source path')
    path = PurePosixPath(value)
    require(not path.is_absolute() and all(p not in {'.', '..', ''} for p in value.split('/'))
            and '\\' not in value and ':' not in value and '\x00' not in value,
            'source paths must be portable root-relative paths without traversal')
    require(not any(p.lower() in {'.env', '.ssh', '.aws', 'credentials', 'secrets'}
                    or p.lower().startswith('.env.') for p in path.parts), 'sensitive source path')
    return path


def safe_file(root, path):
    parts = relative_path(path).parts
    base = Path(root)
    require(base.is_absolute(), 'roots must be absolute')
    require(not any(p.is_symlink() for p in (base, *base.parents)), 'symlink root is not supported')
    target = base
    # Check lexical ancestors before opening anything, including missing leaves.
    for part in parts:
        target = target / part
        require(not target.is_symlink(), 'symlink source/report path is not supported')
    require(target.resolve().is_relative_to(base.resolve()), 'source escapes its root')
    return target


def criterion_hash(criterion):
    return digest({k: criterion[k] for k in ('id', 'expected', 'method', 'required', 'axis')})


def nodes(document):
    def walk(node, kind):
        yield node, kind
        for phase in node.get('phases', []):
            yield from walk(phase, 'phase')
        for task in node.get('tasks', []):
            yield from walk(task, 'task')
    for step in document['plan']['steps']:
        yield from walk(step, 'step')


def criteria(document):
    return {c['id']: (c, node) for node, _ in nodes(document) for c in node.get('criteria', [])}


def refs(values, known, label):
    require(isinstance(values, list) and len(values) == len(set(values)), label + ': unique array required')
    require(all(v in known for v in values), label + ': unknown reference')


def approval(value, sources):
    require(isinstance(value, dict) and value.get('status') in
            {'UNKNOWN', 'NOT_REQUIRED', 'PENDING', 'APPROVED', 'REJECTED'}, 'invalid approval')
    refs(value.get('source_ids', []), sources, 'approval sources')
    if value['status'] in {'APPROVED', 'REJECTED', 'NOT_REQUIRED'}:
        require(value.get('source_ids') and all(sources[s]['kind'] == 'decision' for s in value['source_ids']),
                'approval/waiver needs an explicit decision source')


def validate(document):
    require(isinstance(document, dict), 'document must be an object')
    project = document['project']
    identifier(project['id'])
    require(project.get('title') and project.get('goal'), 'project title and goal required; use explicit unknown text')
    for key in ('product_root', 'documentation_root'):
        require(Path(project[key]).is_absolute(), key + ' must be an absolute host path')
        safe_file(project[key], 'path-check')
    plan = document['plan']
    require(type(plan['revision']) is int and plan['revision'] >= 0, 'invalid plan revision')
    require(plan['status'] in {'UNKNOWN', 'PROPOSED', 'AGREED'}, 'invalid plan status')
    require(isinstance(plan['steps'], list), 'plan steps must be an array')
    sources = {}
    for source in document.get('sources', []):
        identifier(source['id'])
        require(source['id'] not in sources, 'duplicate source id')
        require(source['kind'] in {'requirement', 'architecture', 'plan', 'decision', 'checkpoint',
                                  'verification', 'product', 'claim', 'other'}, 'invalid source kind')
        require(source['status'] in {'CURRENT', 'HISTORICAL', 'UNKNOWN', 'CONFLICT'}, 'invalid source status')
        require(source['root'] in {'product', 'documentation', 'statement'}, 'invalid source root')
        require(bool(SHA.fullmatch(source.get('sha256', ''))), 'source fingerprint is required')
        if source['root'] == 'statement':
            require(source.get('summary') and source['kind'] in {'claim', 'decision', 'other'},
                    'statement needs summary and cannot pretend file verification')
            require(source['sha256'] == digest(source['summary']), 'statement fingerprint mismatch')
        else:
            safe_file(project[source['root'] + '_root'], source['path'])
        sources[source['id']] = source
    for source in sources.values():
        refs(source.get('supersedes', []), sources, 'superseded sources')
    refs(plan.get('source_ids', []), sources, 'plan sources')
    approval(plan.get('approval', {'status': 'UNKNOWN'}), sources)
    if plan['status'] == 'AGREED':
        require(plan.get('source_ids') and plan.get('approval', {}).get('status') == 'APPROVED',
                'agreed plan requires plan provenance and explicit approval')
        require(bool(plan['steps']), 'agreed plan must contain actual steps')
    all_nodes, all_criteria = {}, {}
    for node, kind in nodes(document):
        identifier(node['id'])
        require(kind == 'step' or not node.get('phases'), 'only steps contain phases')
        require(kind == 'phase' or not node.get('tasks'), 'only phases contain tasks; tasks are leaves')
        require(node['id'] not in all_nodes, 'duplicate step/phase/task id')
        require(node.get('title') and node.get('status') in STATUSES, 'node title/status required')
        require(isinstance(node.get('expected_result', ''), str), 'expected result must be text')
        refs(node.get('source_ids', []), sources, 'node sources')
        approval(node.get('approval', {'status': 'UNKNOWN'}), sources)
        if kind == 'step':
            require(len(node.get('phases', [])) <= 5, 'at most five phases per step')
            if plan['status'] == 'AGREED':
                require(1 <= len(node.get('phases', [])) <= 5, 'agreed step needs one to five phases')
        if plan['status'] == 'AGREED' and kind != 'task':
            require(node.get('expected_result') and node.get('criteria') and
                    any(c.get('required') for c in node['criteria']), 'step/phase outcome and required proof criteria required')
        for c in node.get('criteria', []):
            identifier(c['id'])
            require(c['id'] not in all_criteria, 'duplicate criterion id')
            require(c.get('expected') and c.get('method') and type(c.get('required')) is bool
                    and c.get('axis') in AXES, 'criterion needs expected result, method, required flag and axis')
            all_criteria[c['id']] = c
        all_nodes[node['id']] = node
    evidence = {}
    for e in document.get('evidence', []):
        identifier(e['id'])
        require(e['id'] not in evidence, 'duplicate evidence id')
        identifier(e['criterion_id'])
        require(e.get('axis') in AXES and e.get('verdict') in VERDICTS, 'invalid evidence verdict/axis')
        require(e.get('quality') in {'FULL', 'PARTIAL', 'UNAVAILABLE'}, 'invalid evidence quality')
        require(e.get('check_id') and e.get('subject') and e.get('actual'), 'evidence requires check, subject and actual result')
        require(bool(SHA.fullmatch(e.get('criterion_hash', ''))), 'captured criterion_hash required')
        timestamp(e.get('observed_at'))
        refs(e.get('source_ids', []), sources, 'evidence sources')
        refs(e.get('subject_source_ids', []), sources, 'evidence subject sources')
        require(set(e.get('subject_source_ids', [])) <= set(e.get('source_ids', [])), 'subject sources need captured fingerprints')
        require(set(e.get('source_hashes', {})) == set(e.get('source_ids', [])), 'capture hashes of every evidence source')
        require(all(SHA.fullmatch(h) for h in e.get('source_hashes', {}).values()), 'invalid captured source hash')
        require(isinstance(e.get('limitations', []), list), 'evidence limitations must be an array')
        evidence[e['id']] = e
    for c in all_criteria.values():
        if 'evidence_ids' in c:
            refs(c['evidence_ids'], evidence, 'criterion evidence')
            require(all(evidence[e]['criterion_id'] == c['id'] for e in c['evidence_ids']), 'evidence bound to another criterion')
    current = document.get('current', {})
    require(current.get('status', 'UNKNOWN') in STATUSES, 'invalid current status')
    require(not current.get('phase_id') or current.get('step_id'), 'current phase requires its step')
    require(not current.get('task_id') or current.get('phase_id'), 'current task requires its phase')
    scope = None
    for kind in ('step', 'phase', 'task'):
        key = kind + '_id'
        if current.get(key):
            require(current[key] in all_nodes, 'current scope missing from plan')
            if kind == 'step':
                require(current[key] in {n['id'] for n in plan['steps']}, 'current step_id must name a step')
            if scope:
                child_key = 'phases' if kind == 'phase' else 'tasks'
                require(current[key] in {n['id'] for n in scope.get(child_key, [])}, 'current scope hierarchy mismatch')
            scope = all_nodes[current[key]]
    refs(current.get('evidence_ids', []), evidence, 'current evidence')
    refs(current.get('checkpoint', {}).get('evidence_ids', []), evidence, 'checkpoint evidence')
    action = current.get('next_action', {})
    require(action.get('permission', 'UNKNOWN') in {'ALLOWED', 'REQUIRES_APPROVAL', 'BLOCKED', 'UNKNOWN'}, 'invalid next-action permission')
    refs(action.get('source_ids', []), sources, 'next-action sources')
    run_ids = set()
    for run in document.get('runs', []):
        identifier(run['id'])
        require(run['id'] not in run_ids, 'duplicate run id')
        require(type(run.get('attempt')) is int and run['attempt'] >= 1, 'attempt must be a positive integer')
        require(run.get('status') in {'RUNNING', 'COMPLETE', 'FAILED', 'STOPPED', 'BLOCKED'}, 'invalid run status')
        step = next((n for n in plan['steps'] if n['id'] == run.get('step_id')), None)
        require(step is not None, 'run needs a plan step scope')
        run_scope = step
        if run.get('phase_id'):
            run_scope = next((n for n in step.get('phases', []) if n['id'] == run['phase_id']), None)
            require(run_scope is not None, 'run phase must belong to its step')
        if run.get('task_id'):
            require(run.get('phase_id') and any(n['id'] == run['task_id'] for n in run_scope.get('tasks', [])),
                    'run task must belong to its phase')
        refs(run.get('source_ids', []), sources, 'run sources')
        if run.get('report'):
            link = run['report']
            require(link.get('root') in {'product', 'documentation'}, 'invalid run report root')
            safe_file(project[link['root'] + '_root'], link['path'])
        run_ids.add(run['id'])
    conflict_ids = set()
    for conflict in document.get('conflicts', []):
        identifier(conflict['id'])
        require(conflict['id'] not in conflict_ids, 'duplicate conflict id')
        require(conflict.get('status') in {'OPEN', 'RESOLVED'} and conflict.get('summary'), 'invalid conflict')
        refs(conflict.get('source_ids', []), sources, 'conflict sources')
        refs(conflict.get('resolution_evidence_ids', []), evidence, 'resolution evidence')
        if conflict['status'] == 'RESOLVED':
            require(conflict.get('resolution_evidence_ids'), 'resolution needs separate evidence')
        conflict_ids.add(conflict['id'])
    return copy.deepcopy(document)


def plan_shape(document):
    p = copy.deepcopy(document['plan'])
    p.pop('revision', None)
    p.pop('approval', None)
    p.pop('source_ids', None)
    for node, _ in nodes({'plan': p}):
        for key in ('status', 'approval', 'source_ids', 'actual_result'):
            node.pop(key, None)
        for c in node.get('criteria', []):
            c.pop('evidence_ids', None)
    return p


def validate_transition(old, new, event, event_sources):
    require(old['project'] == new['project'], 'project identity/roots are immutable; explicit migration required')
    for collection in ('evidence',):
        before, after = old.get(collection, []), new.get(collection, [])
        require(after[:len(before)] == before, 'evidence is append-only and ordered; preserve original verdicts')
    for key in ('sources', 'runs', 'conflicts'):
        before = {x['id']: x for x in old.get(key, [])}
        after = {x['id']: x for x in new.get(key, [])}
        require(before.keys() <= after.keys(), key + ': historical records cannot be deleted')
        for id_, item in before.items():
            if key == 'sources':
                require(all(after[id_].get(k) == item.get(k) for k in ('root', 'path', 'kind', 'sha256', 'summary')),
                        'source identity is immutable; append a new revision source')
            if key == 'runs':
                require(all(after[id_].get(k) == item.get(k) for k in
                            ('id', 'step_id', 'phase_id', 'task_id', 'attempt', 'report')),
                        'run scope/attempt/report identity is immutable; create a new attempt')
            if key == 'runs' and item['status'] != 'RUNNING':
                require(after[id_] == item, 'terminal run verdict is immutable; create another attempt')
            if key == 'conflicts' and item['status'] == 'RESOLVED':
                require(after[id_] == item, 'resolved conflict is immutable; append a new conflict')
    old_c, new_c = criteria(old), criteria(new)
    for id_ in old_c.keys() & new_c.keys():
        before = old_c[id_][0].get('evidence_ids', [])
        require(new_c[id_][0].get('evidence_ids', [])[:len(before)] == before,
                'criterion evidence links are append-only')
    changed = plan_shape(old) != plan_shape(new)
    if changed:
        require(new['plan']['revision'] > old['plan']['revision'] and event == 'PLAN_CHANGED' and event_sources,
                'plan change requires a higher plan revision and sourced PLAN_CHANGED event')
        if new['plan']['status'] == 'AGREED':
            sources = {s['id']: s for s in new.get('sources', [])}
            require(all(sources[s]['kind'] == 'decision' for s in event_sources) and
                    set(event_sources) <= set(new['plan']['approval'].get('source_ids', [])),
                    'agreed plan change needs its explicit decision in the approval sources')
    else:
        require(new['plan']['revision'] == old['plan']['revision'], 'fixes/retries do not increase plan revision')
    resolved = [c for c in new.get('conflicts', []) if c['status'] == 'RESOLVED'
                and next((o['status'] for o in old.get('conflicts', []) if o['id'] == c['id']), None) != 'RESOLVED']
    require(not resolved or event == 'RESOLVED', 'conflict resolution requires a separate RESOLVED event')


def projection(document):
    """Conservative read-time projection; original claims are kept verbatim in snapshots."""
    sources = {s['id']: s for s in document.get('sources', [])}
    freshness, findings = {}, []
    for id_, s in sources.items():
        try:
            observed = digest(s['summary']) if s['root'] == 'statement' else file_hash(
                safe_file(document['project'][s['root'] + '_root'], s['path']))
            freshness[id_] = 'CURRENT' if s['status'] == 'CURRENT' and observed == s['sha256'] else 'STALE_OR_HISTORICAL'
        except (OSError, ReportError):
            freshness[id_] = 'MISSING_OR_UNSAFE'
    current_sources = lambda ids: bool(ids) and all(freshness.get(s) == 'CURRENT' for s in ids)
    cs = criteria(document)
    es = document.get('evidence', [])
    latest = {}
    for e in es:  # append order is authoritative, even for equal/backdated timestamps
        latest[e['criterion_id']] = e
    def supported(e):
        if not e or e['criterion_id'] not in cs:
            return False
        c = cs[e['criterion_id']][0]
        return (e['verdict'] == 'PASS' and e['quality'] == 'FULL' and not e.get('limitations')
                and e['axis'] == c['axis'] and e['criterion_hash'] == criterion_hash(c)
                and bool(e.get('subject_source_ids'))
                and all(sources[s]['root'] != 'statement' and sources[s]['kind'] != 'verification'
                        for s in e.get('subject_source_ids', []))
                and current_sources(e.get('source_ids', []))
                and all(sources[s]['sha256'] == e['source_hashes'][s] for s in e.get('source_ids', []))
                and any(sources[s]['kind'] == 'verification' and sources[s]['root'] != 'statement' for s in e.get('source_ids', [])))
    results = {id_: {'supported': bool(supported(latest.get(id_))), 'evidence': latest.get(id_)} for id_ in cs}
    def approval_status(value):
        value = value or {'status': 'UNKNOWN'}
        raw = value.get('status', 'UNKNOWN')
        return raw if raw in {'PENDING', 'UNKNOWN'} or current_sources(value.get('source_ids', [])) else 'UNKNOWN'
    derived = {}
    for node, kind in reversed(list(nodes(document))):
        required = [c for c in node.get('criteria', []) if c['required']]
        children = node.get('phases', []) + node.get('tasks', [])
        verified = bool(required) and all(results[c['id']]['supported'] for c in required)
        verified = verified and all(derived[n['id']]['technical'] == 'VERIFIED' for n in children)
        raw = node['status']
        technical = 'VERIFIED' if verified and raw in {'VERIFIED', 'WAITING_APPROVAL'} else (
            'IMPLEMENTED_UNVERIFIED' if raw in {'VERIFIED', 'WAITING_APPROVAL'} else raw)
        if raw == 'VERIFIED' and not verified:
            findings.append(node['id'] + ': заявлено «проверено», но достаточных актуальных доказательств нет')
        approval_ = approval_status(node.get('approval'))
        status = 'WAITING_APPROVAL' if raw == 'WAITING_APPROVAL' or (technical == 'VERIFIED' and approval_ == 'PENDING') else technical
        derived[node['id']] = {'status': status, 'technical': technical, 'approval': approval_, 'kind': kind}
    scoped = document.get('current', {})
    scope_id = scoped.get('task_id') or scoped.get('phase_id') or scoped.get('step_id')
    scope_node = next((n for n, _ in nodes(document) if n['id'] == scope_id), None)
    scope_criteria = set()
    if scope_node:
        # Nodes are traversed through a tiny synthetic plan, without inventing nodes.
        scope_criteria = set(criteria({'plan': {'steps': [scope_node]}}))
    def checkpoint_ok(ids):
        return bool(ids) and all(e['criterion_id'] in scope_criteria and supported(e)
                                and results[e['criterion_id']]['supported']
                                for e in (next(x for x in es if x['id'] == id_) for id_ in ids))
    checkpoint = scoped.get('checkpoint', {})
    checkpoint_verified = checkpoint_ok(checkpoint.get('evidence_ids', []))
    current_status = scoped.get('status', 'UNKNOWN')
    if current_status == 'VERIFIED' and (not checkpoint_ok(scoped.get('evidence_ids', [])) or
                                       derived.get(scope_id, {}).get('technical') != 'VERIFIED'):
        current_status = 'IMPLEMENTED_UNVERIFIED'
        findings.append('Текущая задача: VERIFIED не подкреплён проверкой её области')
    conflicts = []
    for conflict in document.get('conflicts', []):
        resolution_ids = conflict.get('resolution_evidence_ids', [])
        resolved = conflict['status'] == 'RESOLVED' and bool(resolution_ids) and all(
            supported(e) and results[e['criterion_id']]['supported']
            for e in (next(x for x in es if x['id'] == id_) for id_ in resolution_ids))
        if not resolved:
            conflicts.append(conflict)
    plan_current = (document['plan']['status'] == 'AGREED' and current_sources(document['plan'].get('source_ids', []))
                    and approval_status(document['plan'].get('approval')) == 'APPROVED')
    steps = document['plan']['steps']
    verified_steps = sum(derived[n['id']]['technical'] == 'VERIFIED' for n in steps)
    percent = round(100 * verified_steps / len(steps), 1) if plan_current and steps and not conflicts else None
    action = scoped.get('next_action', {})
    next_permission = action.get('permission', 'UNKNOWN')
    if next_permission == 'ALLOWED' and (not current_sources(action.get('source_ids', [])) or
                                         not all(sources[s]['kind'] == 'decision' for s in action.get('source_ids', []))):
        next_permission = 'UNKNOWN'
    checks = {(e['check_id'], e['subject']) for e in es}
    return {'nodes': derived, 'criteria': results, 'freshness': freshness, 'findings': findings,
            'plan_current': plan_current, 'plan_approval': approval_status(document['plan'].get('approval')),
            'verified_steps': verified_steps, 'total_steps': len(steps), 'percent': percent,
            'current_status': current_status, 'checkpoint_verified': checkpoint_verified,
            'next_permission': next_permission, 'open_conflicts': conflicts,
            'unique_checks': len(checks), 'evidence_records': len(es)}
