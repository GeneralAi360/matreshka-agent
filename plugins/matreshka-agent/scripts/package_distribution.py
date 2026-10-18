#!/usr/bin/env python3
"""Build and verify self-contained Matreshka distributions. Offline; no host install."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import zipfile

sys.dont_write_bytecode = True
PLUGIN = 'matreshka-agent'
STAMP = 'distribution.json'
INSTALLATION = 'installation.json'
SHA = re.compile(r'^[0-9a-f]{64}$')
LINK = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')
SKILLS = (
    'building-end-to-end', 'orchestrating-subagent-work', 'designing-product-experience',
    'specifying-software-work', 'planning-software-work', 'writing-portable-agent-prompt',
    'implementing-with-tests', 'debugging-systematically', 'reviewing-agent-work',
    'verifying-development-work', 'finishing-development-work',
)
IGNORED = {'.git', '__pycache__', '.matreshka', '.DS_Store'}


class PackageError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise PackageError('HANDOFF_REQUIRED: ' + message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')


def files(root):
    result = {}
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        require(not path.is_symlink(), 'symlink payload: ' + relative.as_posix())
        if IGNORED.intersection(relative.parts) or path.suffix in {'.pyc', '.pyo'}:
            continue
        if path.is_file():
            result[relative.as_posix()] = path.read_bytes()
    return result


def contained(root, relative):
    path = PurePosixPath(relative)
    require(isinstance(relative, str) and relative and not path.is_absolute()
            and '..' not in path.parts and '\\' not in relative and ':' not in relative,
            'unsafe package path: ' + str(relative))
    target = root / Path(*path.parts)
    require(not any(p.is_symlink() for p in (target, *target.parents) if p != root and p.is_relative_to(root)),
            'symlink package path: ' + relative)
    require(target.resolve().is_relative_to(root.resolve()), 'package path escapes root')
    return target


def check_links(root, payload):
    from urllib.parse import unquote
    for relative, data in payload.items():
        if Path(relative).suffix not in {'.md', '.mdc', '.markdown'}:
            continue
        for raw in LINK.findall(data.decode('utf-8')):
            raw = raw.strip().strip('<>').split(' "', 1)[0]
            if not raw or raw.startswith('#') or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', raw):
                continue
            part = unquote(raw.split('#', 1)[0].split('?', 1)[0])
            if not part:
                continue
            require(not Path(part).is_absolute() and '\\' not in part, 'absolute resource link: ' + relative)
            target = (root / relative).parent / part
            require(target.resolve().is_relative_to(root.resolve()) and target.exists(),
                    'missing or escaped resource link: ' + relative + ' -> ' + raw)


def origin(root, payload):
    def git(*args):
        try:
            p = subprocess.run(['git', '-C', str(root), *args], capture_output=True, text=True,
                               encoding='utf-8', timeout=10)
            return p.stdout.strip() if p.returncode == 0 else 'UNAVAILABLE'
        except (OSError, subprocess.TimeoutExpired):
            return 'UNAVAILABLE'
    remote = re.sub(r'(https?://)[^/@]+@', r'\1[redacted]@', git('remote', 'get-url', 'origin'))
    status = git('status', '--porcelain', '--', '.')
    return {'remote': remote, 'ref': git('symbolic-ref', '--short', 'HEAD'), 'sha': git('rev-parse', 'HEAD'),
            'dirty': None if status == 'UNAVAILABLE' else bool(status),
            'tree_digest': digest(encoded({p: digest(b) for p, b in payload.items()}))}


def source_probe(root, entry):
    """Read-only preflight for a full source/plugin checkout without an export stamp."""
    root = root.absolute()
    require(entry in SKILLS, 'unknown Matreshka entry')
    try:
        if (root / INSTALLATION).exists() or (root / STAMP).exists():
            require((root / STAMP).is_file(), 'installed package is missing its distribution stamp')
            return probe(root, entry)
        # The exported canonical document uses WORKFLOW.md and keeps this same
        # preflight. Its outer adapter's stamp owns the complete dependency tree.
        if (root / 'skills' / entry / 'WORKFLOW.md').is_file():
            outer = root.parent.parent
            stamp = json.loads((outer / STAMP).read_text(encoding='utf-8'))
            require(contained(outer, stamp['package_root']) == root, 'wrong bundled source root')
            checked = probe(outer, stamp['selected_entry'])
            checked['entry'] = entry
            checked['workflow'] = str(contained(outer, stamp['entrypoints'][entry]))
            return checked
        identity = json.loads(contained(root, '.codex-plugin/plugin.json').read_text(encoding='utf-8'))
        require(identity['name'] == PLUGIN, 'wrong plugin identity')
        for relative in ('references/project-reporting.md', 'assets/project-report-template.html',
                         'scripts/project_reporting.py', 'scripts/project_report_model.py',
                         'scripts/project_report_store.py', 'scripts/project_report_html.py'):
            require(contained(root, relative).is_file(), 'missing Matreshka resource: ' + relative)
        for name in SKILLS:
            require(contained(root, 'skills/' + name + '/SKILL.md').is_file(), 'incomplete Matreshka skill set')
        return {'status': 'SOURCE_PRESENT', 'plugin': PLUGIN, 'manifest_version': identity['version'],
                'package_root': str(root), 'workflow': str(root / 'skills' / entry / 'SKILL.md'),
                'notice': 'Source presence is not installed-version, native-host or acceptance proof.'}
    except (OSError, KeyError, ValueError) as exc:
        raise PackageError('HANDOFF_REQUIRED: incomplete source package: ' + str(exc)) from exc


def probe(root, entry, expected_source_digest=None):
    """Verify an installed export before reading its workflow; never writes files."""
    root = root.absolute()
    try:
        require(not (root / STAMP).is_symlink(), 'symlink distribution stamp')
        stamp = json.loads((root / STAMP).read_text(encoding='utf-8'))
        require(stamp['schema'] == 1 and stamp['plugin'] == PLUGIN, 'wrong distribution identity')
        installation = json.loads(contained(root, INSTALLATION).read_text(encoding='utf-8'))
        require(installation == {'schema': 1, 'plugin': PLUGIN, 'requires': STAMP}, 'invalid installation marker')
        require(stamp['mode'] in {'plugin', 'skill'}, 'unknown distribution mode')
        portable = stamp['mode'] == 'skill'
        require(stamp['package_root'] == ('references/plugin' if portable else '.'), 'wrong package root')
        require((stamp['selected_entry'] in SKILLS) if portable else stamp['selected_entry'] is None,
                'wrong selected entry identity')
        require(stamp['selected_entry'] is None or entry == stamp['selected_entry'], 'wrong selected entry')
        prefix, filename = ('references/plugin/', 'WORKFLOW.md') if portable else ('', 'SKILL.md')
        expected_entries = {s: prefix + 'skills/' + s + '/' + filename for s in SKILLS}
        require(entry in SKILLS and stamp['entrypoints'] == expected_entries, 'invalid entrypoint mapping')
        require(SHA.fullmatch(stamp['source']['tree_digest']), 'invalid source tree digest')
        if expected_source_digest is not None:
            require(stamp['source']['tree_digest'] == expected_source_digest, 'source digest differs from adapter pin')
        current = files(root)
        current.pop(STAMP, None)
        require(set(current) == set(stamp['files']), 'missing or unexpected package inventory')
        for relative, data in current.items():
            require(digest(data) == stamp['files'][relative], 'file hash mismatch: ' + relative)
        check_links(root, current)
        package = contained(root, stamp['package_root'])
        identity = json.loads((package / '.codex-plugin/plugin.json').read_text(encoding='utf-8'))
        require(identity['name'] == PLUGIN and identity['version'] == stamp['manifest_version'], 'manifest identity mismatch')
        config = json.loads((package / 'evals/context-budget.json').read_text(encoding='utf-8'))
        for surface in config['surfaces']:
            for relative in surface['files']:
                require(contained(package, relative).is_file(), 'missing runtime configuration resource: ' + relative)
        for name in SKILLS:
            workflow = contained(root, stamp['entrypoints'][name])
            text = workflow.read_text(encoding='utf-8')
            require('project-reporting.md' in text, 'workflow lacks project report contract')
        return {'status': 'VERIFIED', 'plugin': PLUGIN, 'entry': entry, 'source': stamp['source'],
                'manifest_version': stamp['manifest_version'], 'package_root': str(package),
                'workflow': str(contained(root, stamp['entrypoints'][entry])),
                'notice': 'Byte/resource integrity only; no native behavior, visual or user approval claim.'}
    except (OSError, KeyError, TypeError, ValueError) as exc:
        if isinstance(exc, PackageError):
            raise
        raise PackageError('HANDOFF_REQUIRED: invalid distribution: ' + str(exc)) from exc


def adapter(entry, description, source):
    name = PLUGIN + '-' + entry
    text = f'''---
name: {name}
description: {json.dumps(description, ensure_ascii=False)}
---

# Matreshka Agent / {entry}

Use the packaged Matreshka workflow for this direct call. Resolve this skill directory
from this SKILL.md location, never from the working project or a similarly named skill.
Before project actions, run the read-only integrity preflight:

```text
python3 -B <this-skill-dir>/references/plugin/scripts/package_distribution.py probe --root <this-skill-dir> --entry {entry} --expected-source-digest {source['tree_digest']}
```

On a missing file, mismatch or unavailable preflight, return HANDOFF_REQUIRED with
the reason and no development/report success claim. Do not use an older generic
skill or search plugin caches as a fallback. A report update grants no authority.

After VERIFIED, read the [canonical workflow](references/plugin/skills/{entry}/WORKFLOW.md)
and apply it completely. Its plugin root is `<this-skill-dir>/references/plugin`;
its relative resource links already resolve inside this export. For a bounded direct
task, use that workflow without starting the full end-to-end process. For delegated
work, retain the existing report owner, permission envelope and blind-review limits.

When that workflow requires another Matreshka skill, resolve its WORKFLOW.md under
the same verified `references/plugin/skills/` directory. These bundled documents are
canonical workflow instructions, not separately installed generic skills. Keep all
source-qualified Matreshka handoffs within this package; external peer integrations
retain their own discovery and permissions. Do not substitute a same-named skill.

The source ref/SHA, development snapshot flag and exact file fingerprints are in
distribution.json. A matching hash proves unchanged bytes, not trusted authorship,
technical acceptance, visual inspection, user approval or readiness for release.
'''
    metadata = f'''interface:
  display_name: "Matreshka Agent / {entry}"
  short_description: "Source-qualified Matreshka workflow adapter"
  default_prompt: "Use ${name} for this task with its bundled Matreshka workflow."
policy:
  allow_implicit_invocation: true
'''
    return {'SKILL.md': text.encode('utf-8'), 'agents/openai.yaml': metadata.encode('utf-8')}


def rewrite_resource_paths(value):
    """Rewrite package-owned JSON paths without changing external skill discovery."""
    mapping = {'skills/' + s + '/SKILL.md': 'skills/' + s + '/WORKFLOW.md' for s in SKILLS}
    if isinstance(value, str):
        return mapping.get(value, value)
    if isinstance(value, list):
        return [rewrite_resource_paths(item) for item in value]
    if isinstance(value, dict):
        return {key: rewrite_resource_paths(item) for key, item in value.items()}
    return value


def write_archive(path, folder, payload):
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for relative, data in sorted(payload.items()):
            info = zipfile.ZipInfo(folder + '/' + relative, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, data)


def build(root, output):
    root, output = root.absolute(), output.absolute()
    require(not output.exists(), 'output already exists; preserve it and choose a new directory')
    require(not output.is_relative_to(root), 'output must be outside the packaged source')
    from validate_dev_05 import load_base, configure_dev_05
    validator = load_base()
    configure_dev_05(validator)
    findings = validator.validate_package(root)
    require(not findings, 'source validation failed: ' + '; '.join(f'{f.code}: {f.path}' for f in findings[:8]))
    payload = {p: b for p, b in files(root).items() if p != STAMP and 'tests' not in PurePosixPath(p).parts
               and not {'results', 'workspaces'}.intersection(PurePosixPath(p).parts)}
    source = origin(root, payload)
    version = json.loads(payload['.codex-plugin/plugin.json'])['version']
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.matreshka-build-', dir=output.parent) as scratch:
        stage = Path(scratch) / 'artifacts'
        stage.mkdir()
        names = []
        for entry in (None, *SKILLS):
            name = PLUGIN if entry is None else PLUGIN + '-' + entry
            content = dict(payload) if entry is None else {}
            prefix = '' if entry is None else 'references/plugin/'
            if entry is None:
                # An installed full plugin must never fall back to checkout-only
                # presence checks, even if both installation metadata files vanish.
                for skill in SKILLS:
                    key = 'skills/' + skill + '/SKILL.md'
                    content[key] = content[key].replace(b'package_distribution.py source --root',
                                                        b'package_distribution.py probe --root')
            if entry is not None:
                for relative, data in payload.items():
                    target = relative.replace('/SKILL.md', '/WORKFLOW.md')
                    if Path(relative).suffix in {'.md', '.markdown', '.mdc'}:
                        data = data.replace(b'SKILL.md', b'WORKFLOW.md')
                    elif Path(relative).suffix == '.json':
                        value = json.loads(data)
                        rewritten = rewrite_resource_paths(value)
                        if rewritten != value:
                            data = json.dumps(rewritten, ensure_ascii=False, indent=2).encode('utf-8') + b'\n'
                    content[prefix + target] = data
                from validate_package import parse_frontmatter
                front, errors = parse_frontmatter(payload['skills/' + entry + '/SKILL.md'].decode('utf-8'))
                require(not errors, 'invalid skill metadata')
                content.update(adapter(entry, front['description'], source))
            content[INSTALLATION] = encoded({'schema': 1, 'plugin': PLUGIN, 'requires': STAMP}) + b'\n'
            stamp = {'schema': 1, 'plugin': PLUGIN, 'mode': 'plugin' if entry is None else 'skill',
                     'manifest_version': version, 'track': '0.5-development', 'source': source,
                     'package_root': '.' if entry is None else 'references/plugin', 'selected_entry': entry,
                     'entrypoints': {s: prefix + 'skills/' + s + ('/SKILL.md' if entry is None else '/WORKFLOW.md') for s in SKILLS},
                     'files': {p: digest(b) for p, b in content.items()}}
            content[STAMP] = encoded(stamp) + b'\n'
            archive = stage / (name + '.zip')
            write_archive(archive, name, content)
            # Validate each finished archive before it can become a visible build.
            with tempfile.TemporaryDirectory(prefix='matreshka-built-check-') as check:
                installed = unpack_archive(archive, Path(check) / 'installed')
                probe(installed, entry or SKILLS[0], source['tree_digest'])
            names.append(archive.name)
        require(not output.exists(), 'output already exists; concurrent build did not replace it')
        latest = {p: b for p, b in files(root).items() if p in payload}
        require(latest == payload, 'source changed during build; previous artifacts were preserved')
        stage.rename(output)
    return [output / name for name in names]


def unpack_archive(archive, destination):
    require(not destination.exists(), 'extraction destination already exists')
    try:
        with zipfile.ZipFile(archive) as zipped:
            infos = zipped.infolist()
            require(infos and len(infos) <= 12000 and sum(i.file_size for i in infos) <= 64 * 1024 * 1024,
                    'invalid or excessive archive size')
            seen, tops = set(), set()
            for info in infos:
                path = PurePosixPath(info.filename)
                require(info.filename and not path.is_absolute() and '..' not in path.parts
                        and '\\' not in info.filename and ':' not in info.filename and len(path.parts) >= 2,
                        'unsafe archive member: ' + info.filename)
                require(info.filename.casefold() not in seen and not stat.S_ISLNK(info.external_attr >> 16),
                        'duplicate or symlink archive member')
                seen.add(info.filename.casefold())
                tops.add(path.parts[0])
            require(len(tops) == 1, 'archive must contain one installable root')
            destination.mkdir(parents=True)
            for info in infos:
                target = contained(destination, info.filename)
                require(not info.is_dir(), 'unexpected directory-only archive member')
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(zipped.read(info))
            return destination / next(iter(tops))
    except (OSError, zipfile.BadZipFile, RuntimeError) as exc:
        raise PackageError('HANDOFF_REQUIRED: cannot unpack distribution: ' + str(exc)) from exc


def report_smoke(package, scratch):
    """Run only the installed CLI; PYTHONPATH and cwd cannot provide source helpers."""
    product, docs = scratch / 'product', scratch / 'development-docs'
    product.mkdir()
    docs.mkdir()
    script = package / 'scripts/project_reporting.py'
    def run(*args):
        p = subprocess.run([sys.executable, '-B', '-S', str(script), *map(str, args)], cwd=product,
                           env={**os.environ, 'PYTHONPATH': '', 'PYTHONDONTWRITEBYTECODE': '1'},
                           capture_output=True, text=True, encoding='utf-8', timeout=20)
        require(p.returncode == 0, 'installed report CLI failed: ' + p.stderr)
        return json.loads(p.stdout)
    document = run('template', '--product-root', product, '--documentation-root', docs,
                   '--id', 'PACKAGE-SMOKE', '--title', 'Проверка установленного пакета', '--goal', 'Сформировать и обновить постоянный отчёт')
    candidate = scratch / 'candidate.json'
    candidate.write_text(json.dumps(document, ensure_ascii=False), encoding='utf-8')
    first = run('init', '--input', candidate)
    project_dir = docs / '.matreshka/project'
    before = (project_dir / 'report.html').read_bytes()
    document['current']['title'] = 'Продолжение той же задачи после установки'
    candidate.write_text(json.dumps(document, ensure_ascii=False), encoding='utf-8')
    second = run('update', '--project-dir', project_dir, '--input', candidate, '--expected-revision', first['revision'],
                 '--event', 'REFRESHED', '--summary', 'Проверка продолжения сохраняет адрес и историю')
    status = run('status', '--project-dir', project_dir)
    require(status['state']['revision'] == second['revision'] == 2, 'report revision mismatch')
    require(any(p.read_bytes() == before for p in (project_dir / 'revisions').rglob('report.html')), 'previous report missing')
    require(not list(product.iterdir()), 'internal report leaked into product')
    html = (project_dir / 'report.html').read_text(encoding='utf-8')
    require('Продолжение той же задачи' in html and '<html' in html.lower(), 'report HTML was not generated')
    return {'revisions': [first['revision'], second['revision']], 'same_address': True,
            'history_preserved': True, 'external_docs_root': True, 'visual_checked': False}


def verify_archive(archive):
    with tempfile.TemporaryDirectory(prefix='matreshka-isolated-install-') as scratch:
        base = Path(scratch)
        download = unpack_archive(archive.absolute(), base / 'download')
        installed = base / 'host' / '.agents' / 'skills' / download.name
        installed.parent.mkdir(parents=True)
        shutil.copytree(download, installed)
        shutil.rmtree(base / 'download')
        stamp = json.loads((installed / STAMP).read_text(encoding='utf-8'))
        entries = [stamp['selected_entry']] if stamp['selected_entry'] else list(SKILLS)
        for entry in entries:
            result = probe(installed, entry)
        package = Path(result['package_root'])
        budget = subprocess.run([sys.executable, '-B', '-S', str(package / 'scripts/check_context_budget.py'),
                                 str(package), '--json'], cwd=base,
                                env={**os.environ, 'PYTHONPATH': '', 'PYTHONDONTWRITEBYTECODE': '1'},
                                capture_output=True, text=True, encoding='utf-8', timeout=20)
        require(budget.returncode == 0, 'installed runtime context paths/budget failed: ' + budget.stdout + budget.stderr)
        smoke = report_smoke(package, base)
        return {'status': 'VERIFIED', 'archive': str(archive), 'entries': entries, 'source': stamp['source'],
                'report_smoke': smoke, 'runtime_context_check': json.loads(budget.stdout),
                'limitations': ['No native host dispatch or visual browser verification.']}


def main():
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    make = sub.add_parser('build')
    make.add_argument('--source', type=Path, default=Path(__file__).resolve().parents[1])
    make.add_argument('--output', type=Path, required=True)
    for action in ('probe', 'source'):
        p = sub.add_parser(action)
        p.add_argument('--root', type=Path, required=True)
        p.add_argument('--entry', choices=SKILLS, required=True)
        if action == 'probe':
            p.add_argument('--expected-source-digest')
    verify = sub.add_parser('verify')
    verify.add_argument('--archive', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == 'build':
            result = {'archives': [str(p) for p in build(args.source, args.output)]}
        elif args.command == 'probe':
            result = probe(args.root, args.entry, args.expected_source_digest)
        elif args.command == 'source':
            result = source_probe(args.root, args.entry)
        else:
            result = verify_archive(args.archive)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (PackageError, OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
