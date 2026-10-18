"""Locked CAS store with immutable revisions and atomic commit witnesses.

A .commit.json file is the commit point. HEAD.json and report.html are repairable
views written afterwards. An interrupted bundle without a commit witness is never
adopted. No lock/file repair is performed by read-only operations.
"""
from __future__ import annotations

import contextlib
import copy
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from project_report_model import (EVENTS, SHA, ReportError, canonical, digest, file_hash,
                                  identifier, projection, refs, require, validate,
                                  validate_transition)


def now():
    return datetime.now(timezone.utc).isoformat(timespec='microseconds')


def guard(path):
    path = Path(path).absolute()
    for part in (path, *path.parents):
        require(not part.is_symlink(), 'symlink storage path is not supported: ' + str(part))
    return path


def location(document):
    return guard(Path(document['project']['documentation_root']) / '.matreshka' / 'project')


def atomic_write(path, data):
    path = guard(path)
    fd, tmp = tempfile.mkstemp(prefix='.' + path.name + '-', dir=path.parent)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data if isinstance(data, bytes) else data.encode('utf-8'))
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(tmp, path)
        if os.name != 'nt':
            directory_fd = os.open(path.parent, os.O_RDONLY)
            try:
                os.fsync(directory_fd)
            finally:
                os.close(directory_fd)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


@contextlib.contextmanager
def locked(directory, create=False):
    directory = guard(directory)
    if create:
        directory.mkdir(parents=True, exist_ok=True)
    require(directory.is_dir(), 'project report is not initialized')
    lock_path = guard(directory / '.lock')
    with lock_path.open('a+b') as stream:
        if os.name == 'nt':
            import msvcrt
            stream.seek(0, 2)
            if not stream.tell():
                stream.write(b'\0')
                stream.flush()
            stream.seek(0)
            try:
                msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
            except OSError as exc:
                raise ReportError('another chat owns the report lock; reread and retry') from exc
            try:
                yield
            finally:
                stream.seek(0)
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
        else:
            import fcntl
            try:
                fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError as exc:
                raise ReportError('another chat owns the report lock; reread and retry') from exc
            try:
                yield
            finally:
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def read_json(path):
    try:
        return json.loads(guard(path).read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        raise ReportError('cannot read valid JSON: ' + str(path)) from exc


def manifests(directory):
    directory = guard(directory)
    guard(directory / 'revisions')
    found, broken = [], []
    for path in sorted((directory / 'revisions').glob('*.commit.json')):
        guard(path)
        try:
            value = read_json(path)
            require(digest(value['commit']) == value['checksum'], 'commit witness checksum mismatch')
            commit = value['commit']
            require(all(isinstance(commit.get(k), str) and SHA.fullmatch(commit[k])
                        for k in ('digest', 'html_sha256')), 'invalid commit hash')
            require(type(commit['revision']) is int and commit['revision'] > 0, 'invalid commit revision')
            require(path.name == f"{commit['revision']:08d}.commit.json", 'commit filename mismatch')
            require(commit['bundle'] == f"{commit['revision']:08d}-{commit['digest'][:16]}", 'invalid bundle name')
            found.append(commit)
        except (ReportError, KeyError, TypeError):
            broken.append(path)
    return sorted(found, key=lambda m: m['revision']), broken


def read_bundle(directory, commit):
    require(all(isinstance(commit.get(k), str) and SHA.fullmatch(commit[k])
                for k in ('digest', 'html_sha256')), 'invalid commit hash')
    require(type(commit['revision']) is int and commit['revision'] > 0 and
            commit['bundle'] == f"{commit['revision']:08d}-{commit['digest'][:16]}", 'unsafe commit bundle identity')
    bundle = guard(directory / 'revisions' / commit['bundle'])
    envelope = read_json(bundle / 'state.json')
    without_digest = {k: v for k, v in envelope.items() if k != 'digest'}
    require(envelope['digest'] == digest(without_digest) == commit['digest'], 'state digest mismatch')
    require(envelope['schema_version'] == 1 and envelope['revision'] == commit['revision'], 'state schema/revision mismatch')
    report_path = guard(bundle / 'report.html')
    require(file_hash(report_path) == commit['html_sha256'], 'revision HTML is corrupt')
    validate(envelope['document'])
    require(location(envelope['document']) == directory, 'report directory differs from bound documentation root')
    return envelope, report_path.read_bytes()


def latest(directory):
    directory = guard(directory)
    found, broken = manifests(directory)
    require(found and not broken, 'commit witness is missing/corrupt; explicit recovery required')
    commit = found[-1]
    envelope, html = read_bundle(directory, commit)
    return commit, envelope, html


def load(directory):
    """Read-only: no mkdir, lock, touch, cache repair or evidence rewriting."""
    directory = guard(directory)
    commit, envelope, _ = latest(directory)
    require(read_json(directory / 'HEAD.json') == commit, 'HEAD view is stale/corrupt; explicit recovery required')
    view = guard(directory / 'report.html')
    require(view.is_file() and file_hash(view) == commit['html_sha256'], 'stable HTML is stale/corrupt; explicit recovery required')
    return envelope


def _commit(directory, document, previous, event, summary, source_ids, revision=None):
    from project_report_html import render
    sources = {s['id']: s for s in document.get('sources', [])}
    refs(source_ids, sources, 'event sources')
    require(event in EVENTS and bool(summary), 'known event and summary required')
    stamp = now()
    rev = revision or (previous['revision'] + 1 if previous else 1)
    history = copy.deepcopy(previous['history']) if previous else []
    history.append({'revision': rev, 'at': stamp, 'event': event, 'summary': summary, 'source_ids': source_ids})
    envelope = {'schema_version': 1, 'revision': rev, 'updated_at': stamp,
                'previous_digest': previous['digest'] if previous else None,
                'document': document, 'history': history}
    envelope['digest'] = digest(envelope)
    html = render(envelope).encode('utf-8')
    commit = {'revision': rev, 'digest': envelope['digest'],
              'html_sha256': __import__('hashlib').sha256(html).hexdigest(),
              'bundle': f"{rev:08d}-{envelope['digest'][:16]}"}
    revisions = guard(directory / 'revisions')
    revisions.mkdir(exist_ok=True)
    bundle = guard(revisions / commit['bundle'])
    require(not bundle.exists(), 'revision bundle already exists; recover before retrying')
    bundle.mkdir()
    atomic_write(bundle / 'state.json', canonical(envelope))
    atomic_write(bundle / 'report.html', html)
    marker = revisions / f'{rev:08d}.commit.json'
    require(not marker.exists(), 'revision number already committed')
    atomic_write(marker, canonical({'commit': commit, 'checksum': digest(commit)}))
    # The immutable bundle is committed NOW. View failures cannot undo it.
    try:
        atomic_write(directory / 'HEAD.json', canonical(commit))
        atomic_write(directory / 'report.html', html)
    except OSError as exc:
        raise ReportError(f'revision {rev} COMMITTED; view refresh failed, run recover: {exc}') from exc
    return envelope


def initialize(document):
    document = validate(document)
    directory = location(document)
    with locked(directory, create=True):
        found, broken = manifests(directory)
        require(not found and not broken and not (directory / 'HEAD.json').exists()
                and not (directory / 'report.html').exists(), 'a persistent report already exists; load/update/recover it')
        return _commit(directory, document, None, 'ADOPTED', 'Проект подключён; неподтверждённые сведения обозначены явно', [])


def update(directory, document, expected_revision, event, summary, source_ids=None):
    directory = guard(directory)
    with locked(directory):
        previous = load(directory)
        require(previous['revision'] == expected_revision, 'stale revision: reload the report and reconcile changes')
        document = validate(document)
        validate_transition(previous['document'], document, event, source_ids or [])
        return _commit(directory, document, previous, event, summary, source_ids or [])


def recover(directory, expected_file_sha256):
    directory = guard(directory)
    with locked(directory):
        # Guard BEFORE hashing or quarantining, including when dangling symlinks exist.
        report = guard(directory / 'report.html')
        head = guard(directory / 'HEAD.json')
        observed = file_hash(report) if report.exists() else 'MISSING'
        require(observed == expected_file_sha256, 'stable report changed since inspection; recovery CAS rejected')
        found, broken = manifests(directory)
        # HEAD is written only after the atomic commit witness. It is a redundant
        # commit witness if that marker is later damaged or removed.
        try:
            head_commit = read_json(head)
            read_bundle(directory, head_commit)
            if not any(m == head_commit for m in found):
                found.append(head_commit)
                found.sort(key=lambda m: m['revision'])
        except (ReportError, OSError, KeyError, TypeError):
            pass
        candidates, damaged = [], list(broken)
        for commit in found:
            try:
                envelope, html = read_bundle(directory, commit)
                candidates.append((commit, envelope, html))
            except (ReportError, OSError, KeyError, TypeError):
                damaged.append(directory / 'revisions' / f"{commit['revision']:08d}.commit.json")
        require(candidates, 'no committed valid revision exists; originals preserved for manual recovery')
        commit, previous, html = candidates[-1]
        # Preserve damaged cache/witness bytes without following redirected paths.
        quarantine = guard(directory / 'recovery' / now().replace(':', '-'))
        quarantine.mkdir(parents=True)
        for path in [report, head, *damaged]:
            path = guard(path)
            if path.exists():
                atomic_write(quarantine / path.name, path.read_bytes())
        # Markers of damaged bundles are retired only after a complete backup.
        for path in damaged:
            guard(path).unlink()
        max_revision = max([m['revision'] for m in found] + [previous['revision']] +
                           [int(p.name.split('.')[0]) for p in broken if p.name.split('.')[0].isdigit()])
        # Avoid collision with interrupted, never-committed bundles, too.
        for path in (directory / 'revisions').iterdir():
            if path.is_dir() and path.name[:8].isdigit():
                max_revision = max(max_revision, int(path.name[:8]))
        return _commit(directory, previous['document'], previous, 'RECOVERED',
                       f"Восстановлена подтверждённая ревизия {previous['revision']}; исходные повреждения сохранены",
                       [], revision=max_revision + 1)


def inventory(document, previous=None):
    """Metadata-only orientation; the agent decides which documents are authoritative."""
    records = []
    ignored = {'.git', 'node_modules', '.matreshka', '.venv', '__pycache__'}
    for root_name in ('documentation', 'product'):
        root = guard(Path(document['project'][root_name + '_root']))
        if not root.is_dir():
            continue
        for base, directories, filenames in os.walk(root, followlinks=False):
            directories[:] = sorted(d for d in directories if d not in ignored and not (Path(base) / d).is_symlink())
            for filename in sorted(filenames):
                path = Path(base) / filename
                if path.is_symlink() or path.suffix.lower() not in {'.md', '.txt', '.json', '.yaml', '.yml', '.html'}:
                    continue
                rel = path.relative_to(root).as_posix()
                try:
                    from project_report_model import relative_path
                    relative_path(rel)
                    stat = path.stat()
                    records.append({'root': root_name, 'path': rel, 'size': stat.st_size, 'mtime_ns': stat.st_mtime_ns})
                except (OSError, ReportError):
                    continue
    old = {(x['root'], x['path']): x for x in (previous or [])}
    new = {(x['root'], x['path']): x for x in records}
    return {'files': records, 'changed': [x for key, x in new.items() if old.get(key) != x],
            'removed': [x for key, x in old.items() if key not in new],
            'notice': 'Metadata is navigation, not proof. Read affected documents; fingerprint evidence explicitly.'}
