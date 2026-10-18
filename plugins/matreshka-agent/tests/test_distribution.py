"""Exercise shipped archives after copying only the selected install directory."""
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from package_distribution import PackageError, build, probe, source_probe, unpack_archive, verify_archive
import package_distribution as distribution


class DistributionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory(prefix='matreshka-distribution-')
        cls.base = Path(cls.temp.name)
        cls.archives = build(ROOT, cls.base / 'built')

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def installed(self, archive):
        destination = self.base / self.id().split('.')[-1] / archive.stem
        unpacked = unpack_archive(archive, destination / 'download')
        installed = destination / 'unrelated-project' / '.agents' / 'skills' / unpacked.name
        installed.parent.mkdir(parents=True)
        shutil.copytree(unpacked, installed)
        shutil.rmtree(destination / 'download')
        return installed

    def test_complete_plugin_archive_forms_and_updates_report(self):
        result = verify_archive(self.archives[0])
        self.assertEqual(result['status'], 'VERIFIED')
        self.assertEqual(len(result['entries']), 11)
        self.assertEqual(result['report_smoke']['revisions'], [1, 2])
        self.assertFalse(result['report_smoke']['visual_checked'])
        self.assertTrue(result['runtime_context_check']['ok'])

    def test_every_selected_skill_survives_folder_only_install(self):
        for archive in self.archives[1:]:
            with self.subTest(archive=archive.name):
                installed = self.installed(archive)
                stamp = json.loads((installed / 'distribution.json').read_text())
                entry = stamp['selected_entry']
                result = probe(installed, entry, stamp['source']['tree_digest'])
                self.assertEqual(result['status'], 'VERIFIED')
                self.assertTrue(Path(result['workflow']).is_relative_to(installed))
                self.assertEqual(list(installed.rglob('SKILL.md')), [installed / 'SKILL.md'])
                checked = verify_archive(archive)
                self.assertEqual(checked['report_smoke']['revisions'], [1, 2])
                self.assertTrue(checked['runtime_context_check']['ok'])

    def test_plain_old_skill_copy_is_not_a_valid_distribution(self):
        installed = self.base / self.id().split('.')[-1]
        shutil.copytree(ROOT / 'skills/planning-software-work', installed)
        with self.assertRaisesRegex(PackageError, 'HANDOFF_REQUIRED'):
            probe(installed, 'planning-software-work')

    def test_portable_canonical_preflight_and_internal_handoff_use_same_bundle(self):
        installed = self.installed(self.archives[1])
        stamp = json.loads((installed / 'distribution.json').read_text())
        package = installed / stamp['package_root']
        for entry in ('building-end-to-end', 'planning-software-work'):
            result = source_probe(package, entry)
            self.assertEqual(result['status'], 'VERIFIED')
            self.assertEqual(Path(result['workflow']), package / 'skills' / entry / 'WORKFLOW.md')

    def test_missing_report_contract_blocks_before_project_writes(self):
        installed = self.installed(self.archives[1])
        stamp = json.loads((installed / 'distribution.json').read_text())
        contract = installed / stamp['package_root'] / 'references/project-reporting.md'
        contract.unlink()
        with self.assertRaisesRegex(PackageError, 'missing|inventory'):
            probe(installed, stamp['selected_entry'])
        self.assertFalse(list(installed.rglob('.matreshka')))

    def test_missing_renderer_and_template_are_detected(self):
        for relative in ('scripts/project_report_model.py', 'assets/project-report-template.html'):
            with self.subTest(relative=relative):
                installed = self.installed(self.archives[2])
                stamp = json.loads((installed / 'distribution.json').read_text())
                (installed / stamp['package_root'] / relative).unlink()
                with self.assertRaises(PackageError):
                    probe(installed, stamp['selected_entry'])
                shutil.rmtree(installed.parents[4])

    def test_same_version_does_not_hide_changed_workflow(self):
        installed = self.installed(self.archives[3])
        stamp = json.loads((installed / 'distribution.json').read_text())
        workflow = installed / stamp['entrypoints'][stamp['selected_entry']]
        workflow.write_text(workflow.read_text() + '\nchanged behavior\n')
        with self.assertRaisesRegex(PackageError, 'hash|digest'):
            probe(installed, stamp['selected_entry'])

    def test_wrong_source_pin_and_wrong_direct_entry_are_rejected(self):
        installed = self.installed(self.archives[4])
        stamp = json.loads((installed / 'distribution.json').read_text())
        with self.assertRaisesRegex(PackageError, 'source'):
            probe(installed, stamp['selected_entry'], '0' * 64)
        other = next(e for e in stamp['entrypoints'] if e != stamp['selected_entry'])
        with self.assertRaisesRegex(PackageError, 'selected'):
            probe(installed, other)

    def test_stamp_cannot_redirect_planning_into_implementation(self):
        installed = self.installed(self.archives[5])
        path = installed / 'distribution.json'
        stamp = json.loads(path.read_text())
        stamp['entrypoints']['planning-software-work'] = stamp['entrypoints']['implementing-with-tests']
        path.write_text(json.dumps(stamp))
        with self.assertRaisesRegex(PackageError, 'entrypoint'):
            probe(installed, 'planning-software-work')

    def test_removed_workflow_name_in_runtime_config_cannot_pass_probe(self):
        installed = self.installed(self.archives[1])
        manifest = installed / 'distribution.json'
        stamp = json.loads(manifest.read_text())
        relative = stamp['package_root'] + '/evals/context-budget.json'
        config_path = installed / relative
        config = json.loads(config_path.read_text())
        config['surfaces'][0]['files'][0] = 'skills/building-end-to-end/SKILL.md'
        config_path.write_text(json.dumps(config))
        # A byte-consistent manifest still cannot make a nonexistent runtime path valid.
        stamp['files'][relative] = hashlib.sha256(config_path.read_bytes()).hexdigest()
        manifest.write_text(json.dumps(stamp))
        with self.assertRaisesRegex(PackageError, 'runtime configuration'):
            probe(installed, stamp['selected_entry'])

    def test_full_plugin_entry_guard_checks_installed_hashes(self):
        installed = self.installed(self.archives[0])
        self.assertEqual(source_probe(installed, 'planning-software-work')['status'], 'VERIFIED')
        path = installed / 'skills/planning-software-work/SKILL.md'
        path.write_text(path.read_text() + '\nchanged\n')
        with self.assertRaisesRegex(PackageError, 'hash'):
            source_probe(installed, 'planning-software-work')

    def test_full_plugin_missing_stamp_cannot_downgrade_to_source_check(self):
        installed = self.installed(self.archives[0])
        workflow = installed / 'skills/planning-software-work/SKILL.md'
        self.assertIn('package_distribution.py probe --root', workflow.read_text())
        (installed / 'distribution.json').unlink()
        (installed / 'assets/project-report-template.html').write_text('damaged')
        with self.assertRaisesRegex(PackageError, 'stamp'):
            source_probe(installed, 'planning-software-work')
        # Even removal of both metadata files cannot relax the actual exported
        # entry's mandatory probe command into a source-presence claim.
        (installed / 'installation.json').unlink()
        proc = subprocess.run([sys.executable, '-B', '-S', str(installed / 'scripts/package_distribution.py'),
                               'probe', '--root', str(installed), '--entry', 'planning-software-work'],
                              capture_output=True, text=True, encoding='utf-8', timeout=20)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn('HANDOFF_REQUIRED', proc.stderr)

    def test_untracked_executable_payload_cannot_join_install(self):
        installed = self.installed(self.archives[5])
        stamp = json.loads((installed / 'distribution.json').read_text())
        (installed / 'unexpected.py').write_text('raise SystemExit(0)\n')
        with self.assertRaisesRegex(PackageError, 'inventory|unexpected'):
            probe(installed, stamp['selected_entry'])

    def test_missing_or_damaged_archive_cannot_pass(self):
        broken = self.base / 'broken.zip'
        broken.write_bytes(b'not a zip')
        with self.assertRaises(PackageError):
            verify_archive(broken)
        with self.assertRaises(PackageError):
            verify_archive(self.base / 'missing.zip')

    def test_unsafe_archives_are_rejected_without_escape(self):
        for member in ('../escape.txt', '/absolute.txt', 'C:/escape.txt', 'root/../escape.txt',
                       'root\\escape.txt', 'root/escape.txt\x00hidden'):
            with self.subTest(member=member):
                archive = self.base / 'unsafe.zip'
                with zipfile.ZipFile(archive, 'w') as z:
                    # Preserve the raw malformed header on every platform:
                    # ZipInfo's constructor normalizes backslashes on Windows.
                    info = zipfile.ZipInfo('placeholder')
                    info.filename = member
                    z.writestr(info, 'must not be written')
                with self.assertRaises(PackageError):
                    unpack_archive(archive, self.base / 'unsafe-output')
        self.assertFalse((self.base / 'escape.txt').exists())

    def test_archive_symlinks_and_case_collisions_are_rejected(self):
        archive = self.base / 'unsafe-link.zip'
        with zipfile.ZipFile(archive, 'w') as z:
            info = zipfile.ZipInfo('root/link')
            info.create_system = 3
            info.external_attr = (stat.S_IFLNK | 0o777) << 16
            z.writestr(info, '../../outside')
        with self.assertRaisesRegex(PackageError, 'symlink'):
            unpack_archive(archive, self.base / 'link-output')
        with zipfile.ZipFile(archive, 'w') as z:
            z.writestr('root/a', 'first')
            z.writestr('root/A', 'second')
        with self.assertRaisesRegex(PackageError, 'duplicate'):
            unpack_archive(archive, self.base / 'case-output')

    def test_interrupted_build_does_not_publish_partial_archives(self):
        destination = self.base / 'failed-build'
        before = {p.name: p.read_bytes() for p in self.archives}
        with mock.patch.object(distribution, 'write_archive', side_effect=OSError('simulated disk full')):
            with self.assertRaisesRegex(OSError, 'disk full'):
                build(ROOT, destination)
        self.assertFalse(destination.exists())
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.archives})

    def test_failed_rebuild_keeps_last_correct_archives(self):
        before = {p.name: p.read_bytes() for p in self.archives}
        with self.assertRaisesRegex(PackageError, 'exists'):
            build(ROOT, self.base / 'built')
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.archives})

    def test_archives_are_reproducible_and_exclude_internal_runs(self):
        other = build(ROOT, self.base / 'repeat-build')
        self.assertEqual([p.read_bytes() for p in self.archives], [p.read_bytes() for p in other])
        for archive in self.archives:
            with zipfile.ZipFile(archive) as z:
                names = z.namelist()
                self.assertFalse(any('/tests/' in p or '/.matreshka/' in p or '/results/' in p for p in names))
                self.assertFalse(any('Project-Start' in p or 'find-skills' in p for p in names))

    def test_installed_preflight_cli_is_read_only_from_another_cwd(self):
        installed = self.installed(self.archives[6])
        stamp = json.loads((installed / 'distribution.json').read_text())
        script = installed / stamp['package_root'] / 'scripts/package_distribution.py'
        before = {p.relative_to(installed): p.read_bytes() for p in installed.rglob('*') if p.is_file()}
        proc = subprocess.run([sys.executable, '-B', '-S', str(script), 'probe', '--root', str(installed),
                               '--entry', stamp['selected_entry'], '--expected-source-digest', stamp['source']['tree_digest']],
                              cwd=self.base, env={**os.environ, 'PYTHONPATH': ''}, capture_output=True, text=True,
                              encoding='utf-8', timeout=20)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(json.loads(proc.stdout)['status'], 'VERIFIED')
        self.assertEqual(before, {p.relative_to(installed): p.read_bytes() for p in installed.rglob('*') if p.is_file()})

    def test_cli_supports_localized_paths_with_ascii_console_default(self):
        original = self.installed(self.archives[3])
        localized = original.parent / 'Рабочая папка' / original.name
        localized.parent.mkdir()
        shutil.move(original, localized)
        stamp = json.loads((localized / 'distribution.json').read_text())
        script = localized / stamp['package_root'] / 'scripts/package_distribution.py'
        proc = subprocess.run([sys.executable, '-B', '-S', str(script), 'probe', '--root', str(localized),
                               '--entry', stamp['selected_entry']],
                              env={**os.environ, 'PYTHONIOENCODING': 'ascii', 'PYTHONPATH': ''},
                              capture_output=True, text=True, encoding='utf-8', timeout=20)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn('Рабочая папка', json.loads(proc.stdout)['workflow'])

    def test_source_prompts_cannot_select_generic_same_named_skill(self):
        for path in (ROOT / 'skills').glob('*/agents/openai.yaml'):
            with self.subTest(skill=path.parent.parent.name):
                self.assertIn('$matreshka-agent:' + path.parent.parent.name, path.read_text())


if __name__ == '__main__':
    unittest.main()
