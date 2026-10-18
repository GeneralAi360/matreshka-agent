#!/usr/bin/env python3
"""Read-only source/ref/SHA and installed-package comparison; never edits a cache."""
import argparse
import json
from pathlib import Path
import re
import subprocess

from project_report_model import digest, file_hash


def inspect(source_root, installed_root=None):
    source_root = Path(source_root).absolute()
    def package(root):
        if root is None or not root.is_dir():
            return None
        versions = {}
        for relative in ('plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json', '.cursor-plugin/plugin.json'):
            manifest = root / relative
            try:
                value = json.loads(manifest.read_text(encoding='utf-8')).get('version')
                if value:
                    versions[relative] = value
            except (OSError, ValueError):
                continue
        version = next(iter(versions.values()), 'UNKNOWN')
        excluded = {'.git', '__pycache__', '.matreshka', 'results', 'workspaces'}
        hashes = {p.relative_to(root).as_posix(): file_hash(p) for p in root.rglob('*')
                  if p.is_file() and not p.is_symlink() and not excluded.intersection(p.relative_to(root).parts)
                  and p.suffix not in {'.pyc', '.pyo'}}
        return {'root': str(root), 'version': version, 'manifest_versions': versions, 'versions_consistent': len(set(versions.values())) == 1, 'tree_digest': digest(hashes), 'files': hashes}
    def git(*args):
        try:
            proc = subprocess.run(['git', '-C', str(source_root), *args], text=True,
                                  encoding='utf-8', capture_output=True, timeout=10)
            return proc.stdout.strip() if proc.returncode == 0 else 'UNAVAILABLE'
        except (OSError, subprocess.TimeoutExpired):
            return 'UNAVAILABLE'
    source, installed = package(source_root), package(Path(installed_root).absolute() if installed_root else None)
    remote = re.sub(r'(https?://)[^/@]+@', r'\1[redacted]@', git('remote', 'get-url', 'origin'))
    result = {'source': source, 'git': {'remote': remote, 'ref': git('symbolic-ref', '--short', 'HEAD'),
              'sha': git('rev-parse', 'HEAD'), 'dirty': git('status', '--porcelain', '--', '.')},
              'installed': installed, 'comparison': 'UNAVAILABLE' if not installed or not source else
              ('MATCH' if source['files'] == installed['files'] else 'DIFFERENT')}
    if source and installed:
        result['different_paths'] = sorted(k for k in source['files'].keys() | installed['files'].keys()
                                           if source['files'].get(k) != installed['files'].get(k))
    return result


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root', required=True)
    p.add_argument('--installed-root')
    a = p.parse_args()
    print(json.dumps(inspect(a.source_root, a.installed_root), ensure_ascii=False, indent=2))
