"""Behavioral scenarios for durable project reporting, including injected I/O failures."""
from __future__ import annotations

import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import project_report_model as model
import project_report_store as store
from project_report_html import render
from project_reporting import record_run, template


def statement(id_, summary, kind='decision'):
    return {'id': id_, 'kind': kind, 'root': 'statement', 'summary': summary,
            'status': 'CURRENT', 'sha256': model.digest(summary)}


def criterion(id_):
    return {'id': id_, 'expected': 'Результат соответствует согласованному контракту',
            'method': 'Сопоставить результат с критерием; сохранить точный вывод проверки',
            'axis': 'TECHNICAL', 'required': True}


class ReportingTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='matreshka-проект-')
        self.root = Path(self.tmp.name)
        self.product, self.docs = self.root / 'product', self.root / 'development'
        self.product.mkdir()
        self.docs.mkdir()
        (self.docs / 'plan.md').write_text('Согласованы два крупных шага, по одной фазе.', encoding='utf-8')
        (self.product / 'feature.txt').write_text('Product baseline', encoding='utf-8')
        self.d = template(self.product, self.docs, 'example', 'Тестовый проект', 'Проверяемые результаты')
        self.d['sources'] = [self.source('plan', 'plan.md', 'plan'), statement('approval', 'Пользователь согласовал этот план'),
                             self.source('baseline', 'feature.txt', 'product', 'product')]
        steps = []
        for i in (1, 2):
            phase = {'id': f'S{i}.P1', 'title': 'Одна связная фаза', 'status': 'NOT_STARTED',
                     'expected_result': 'Законченный результат фазы', 'criteria': [criterion(f'P{i}')], 'tasks': []}
            steps.append({'id': f'S{i}', 'title': f'Шаг {i}', 'status': 'NOT_STARTED',
                          'expected_result': 'Законченный результат шага', 'criteria': [criterion(f'C{i}')],
                          'source_ids': ['plan'], 'phases': [phase]})
        self.d['plan'] = {'revision': 1, 'status': 'AGREED', 'source_ids': ['plan'],
                          'approval': {'status': 'APPROVED', 'source_ids': ['approval']}, 'steps': steps}
        self.d['current'].update({'step_id': 'S1', 'phase_id': 'S1.P1', 'title': 'Работа в первом шаге'})
        self.dir = store.location(self.d)

    def tearDown(self):
        self.tmp.cleanup()

    def source(self, id_, path, kind='verification', root='documentation'):
        base = self.docs if root == 'documentation' else self.product
        return {'id': id_, 'root': root, 'path': path, 'kind': kind, 'status': 'CURRENT', 'sha256': model.file_hash(base / path)}

    def prove(self, id_, verdict='PASS', quality='FULL', axis='TECHNICAL', eid=None, limitations=None):
        c = model.criteria(self.d)[id_][0]
        eid = eid or 'E' + str(len(self.d['evidence']) + 1)
        path = eid + '.log'
        (self.docs / path).write_text(verdict + ': проверка ' + id_, encoding='utf-8')
        source = self.source('LOG-' + eid, path)
        self.d['sources'].append(source)
        evidence = {'id': eid, 'criterion_id': id_, 'criterion_hash': model.criterion_hash(c),
                    'axis': axis, 'verdict': verdict, 'quality': quality,
                    'observed_at': '2026-10-18T09:30:00+00:00', 'check_id': 'check-' + id_,
                    'subject': 'baseline-a', 'actual': verdict + ': наблюдаемый результат ' + id_,
                    'source_ids': [source['id'], 'baseline'], 'subject_source_ids': ['baseline'],
                    'source_hashes': {source['id']: source['sha256'], 'baseline': self.d['sources'][2]['sha256']},
                    'limitations': limitations or []}
        self.d['evidence'].append(evidence)
        return evidence

    def verified(self):
        for n, _ in model.nodes(self.d):
            n['status'] = 'VERIFIED'
            for c in n['criteria']:
                self.prove(c['id'])
        return self.d

    def commit(self, event='REFRESHED', summary='Проверка', expected=None, source_ids=None):
        revision = store.load(self.dir)['revision'] if expected is None else expected
        return store.update(self.dir, self.d, revision, event, summary, source_ids)

    def tree(self):
        return {p.relative_to(self.root).as_posix(): (p.read_bytes(), p.stat().st_mtime_ns)
                for p in self.root.rglob('*') if p.is_file()}

    def cli(self, *args):
        return subprocess.run([sys.executable, '-B', str(SCRIPTS / 'project_reporting.py'), *map(str, args)],
                              text=True, encoding='utf-8', capture_output=True)

    def test_new_project_has_unknown_plan_and_one_report(self):
        d = template(self.product, self.docs, 'new', 'Новый проект', 'Цель пока уточняется')
        result = store.initialize(d)
        self.assertEqual(result['revision'], 1)
        self.assertEqual(model.projection(d)['percent'], None)
        self.assertTrue((self.dir / 'report.html').is_file())
        self.assertFalse((self.product / '.matreshka').exists())

    def test_adopt_existing_documents_without_claiming_execution(self):
        result = store.initialize(self.d)
        p = model.projection(result['document'])
        self.assertEqual((p['total_steps'], p['verified_steps'], p['percent']), (2, 0, 0.0))
        self.assertIn('plan.md', (self.dir / 'report.html').read_text(encoding='utf-8'))

    def test_repeated_init_does_not_create_another_main(self):
        store.initialize(self.d)
        with self.assertRaisesRegex(model.ReportError, 'already exists'):
            store.initialize(self.d)
        self.assertEqual(len(list(self.docs.rglob('report.html'))), 2)  # stable + immutable r1

    def test_new_chat_reads_existing_report_without_writes(self):
        store.initialize(self.d)
        before = self.tree()
        proc = self.cli('status', '--project-dir', self.dir)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual(json.loads(proc.stdout)['state']['revision'], 1)
        self.assertEqual(before, self.tree())

    def test_inventory_is_incremental_metadata_only(self):
        a = store.inventory(self.d)
        self.assertEqual(store.inventory(self.d, a['files'])['changed'], [])
        (self.docs / 'plan.md').write_text('Новый план', encoding='utf-8')
        b = store.inventory(self.d, a['files'])
        self.assertEqual([x['path'] for x in b['changed']], ['plan.md'])
        (self.docs / 'plan.md').unlink()
        self.assertEqual([x['path'] for x in store.inventory(self.d, b['files'])['removed']], ['plan.md'])

    def test_no_defined_project_cli_creates_nothing(self):
        before = self.tree()
        proc = self.cli('template')
        self.assertNotEqual(proc.returncode, 0)
        self.assertEqual(before, self.tree())

    def test_retries_do_not_inflate_progress_or_mutate_old_reports(self):
        store.initialize(self.d)
        first = next((self.dir / 'revisions').glob('*/report.html'))
        before = first.read_bytes()
        for i in (1, 2, 3):
            run_dir = self.docs / '.matreshka' / 'runs' / f'R{i}'
            run_dir.mkdir(parents=True)
            (run_dir / 'dashboard.html').write_text('Run detail', encoding='utf-8')
            run = {'id': f'R{i}', 'step_id': 'S1', 'attempt': i, 'status': 'COMPLETE',
                   'source_ids': [], 'report': {'root': 'documentation', 'path': f'.matreshka/runs/R{i}/dashboard.html'}}
            result = record_run(self.dir, i, run, 'Попытка первого шага')
        self.assertEqual(len(result['document']['plan']['steps']), 2)
        self.assertEqual(model.projection(result['document'])['verified_steps'], 0)
        self.assertEqual(first.read_bytes(), before)
        self.assertEqual(len(result['document']['runs']), 3)

    def test_terminal_run_verdict_cannot_be_rewritten(self):
        self.d['runs'] = [{'id': 'R1', 'step_id': 'S1', 'attempt': 1, 'status': 'FAILED', 'source_ids': []}]
        store.initialize(self.d)
        self.d['runs'][0]['status'] = 'COMPLETE'
        with self.assertRaisesRegex(model.ReportError, 'terminal run'):
            self.commit()

    def test_missing_proof_cannot_be_verified(self):
        self.d['plan']['steps'][0]['status'] = 'VERIFIED'
        p = model.projection(self.d)
        self.assertEqual(p['nodes']['S1']['technical'], 'IMPLEMENTED_UNVERIFIED')
        self.assertEqual(p['verified_steps'], 0)
        self.assertTrue(p['findings'])

    def test_expected_actual_comparison_and_percentage_formula(self):
        self.verified()
        p = model.projection(self.d)
        self.assertEqual((p['percent'], p['unique_checks']), (100.0, 4))
        report = render(store.initialize(self.d))
        self.assertIn('2 / 2 × 100', report)
        self.assertIn('наблюдаемый результат', report)
        self.assertIn('не трудозатрат', report)

    def test_waiting_approval_is_separate_from_technical_proof(self):
        self.verified()
        self.d['plan']['steps'][0]['approval'] = {'status': 'PENDING', 'source_ids': []}
        p = model.projection(self.d)
        self.assertEqual(p['nodes']['S1']['status'], 'WAITING_APPROVAL')
        self.assertEqual(p['nodes']['S1']['technical'], 'VERIFIED')
        self.assertEqual(p['percent'], 100.0)

    def test_approval_without_decision_is_rejected(self):
        self.d['plan']['approval']['source_ids'] = ['plan']
        with self.assertRaisesRegex(model.ReportError, 'decision source'):
            store.initialize(self.d)

    def test_stale_approval_source_is_not_effective(self):
        (self.docs / 'decision.md').write_text('Согласовано', encoding='utf-8')
        s = self.source('decision-file', 'decision.md', 'decision')
        self.d['sources'].append(s)
        self.d['plan']['approval']['source_ids'] = [s['id']]
        (self.docs / 'decision.md').write_text('Решение изменено', encoding='utf-8')
        self.assertEqual(model.projection(self.d)['plan_approval'], 'UNKNOWN')
        self.assertIsNone(model.projection(self.d)['percent'])

    def test_plan_change_needs_revision_and_sourced_event(self):
        store.initialize(self.d)
        self.d['plan']['steps'][0]['title'] = 'Изменённый согласованный шаг'
        with self.assertRaisesRegex(model.ReportError, 'plan change'):
            self.commit()
        self.d['plan']['revision'] = 2
        result = self.commit('PLAN_CHANGED', source_ids=['approval'])
        self.assertEqual(result['document']['plan']['revision'], 2)
        self.assertEqual(result['history'][-1]['event'], 'PLAN_CHANGED')

    def test_fix_cannot_increase_plan_revision(self):
        store.initialize(self.d)
        self.d['plan']['revision'] = 2
        with self.assertRaisesRegex(model.ReportError, 'fixes/retries'):
            self.commit()

    def test_agreed_step_requires_outcome_and_phase_proof(self):
        for key in ('expected_result', 'criteria'):
            d = copy.deepcopy(self.d)
            del d['plan']['steps'][0]['phases'][0][key]
            with self.subTest(key=key), self.assertRaises(model.ReportError):
                model.validate(d)

    def test_no_more_than_five_phases(self):
        phase = self.d['plan']['steps'][0]['phases'][0]
        self.d['plan']['steps'][0]['phases'] = [copy.deepcopy(phase) for _ in range(6)]
        with self.assertRaisesRegex(model.ReportError, 'five phases'):
            model.validate(self.d)

    def test_unknown_imported_plan_does_not_invent_phases(self):
        self.d['plan']['status'] = 'UNKNOWN'
        self.d['plan']['steps'][0]['phases'] = []
        self.d['plan']['steps'][0]['criteria'] = []
        self.d['current'].pop('phase_id')
        model.validate(self.d)
        self.assertIsNone(model.projection(self.d)['percent'])

    def test_wrong_axis_is_not_a_visual_check(self):
        self.verified()
        c = model.criteria(self.d)['P1'][0]
        c['axis'] = 'VISUAL'
        self.assertFalse(model.projection(self.d)['criteria']['P1']['supported'])

    def test_partial_results_and_quality_limitations_remain_partial(self):
        for verdict, quality, limitations in [('PARTIAL', 'FULL', []), ('PASS', 'PARTIAL', []),
                                               ('PASS', 'FULL', ['Browser not available'])]:
            self.d['evidence'] = []
            self.d['sources'] = self.d['sources'][:3]
            self.prove('P1', verdict, quality, limitations=limitations)
            with self.subTest(verdict=verdict, quality=quality):
                self.assertFalse(model.projection(self.d)['criteria']['P1']['supported'])

    def test_missing_or_modified_log_invalidates_success(self):
        self.verified()
        path = self.docs / 'E1.log'
        path.write_text('Changed log', encoding='utf-8')
        self.assertFalse(model.projection(self.d)['criteria']['C1']['supported'])
        path.unlink()
        self.assertEqual(model.projection(self.d)['freshness']['LOG-E1'], 'MISSING_OR_UNSAFE')

    def test_captured_product_hash_is_also_required(self):
        e = self.prove('P1')
        s = self.source('product-version', 'feature.txt', 'product', 'product')
        self.d['sources'].append(s)
        e['source_ids'].append(s['id'])
        e['source_hashes'][s['id']] = s['sha256']
        self.assertTrue(model.projection(self.d)['criteria']['P1']['supported'])
        (self.product / 'feature.txt').write_text('New code', encoding='utf-8')
        self.assertFalse(model.projection(self.d)['criteria']['P1']['supported'])

    def test_log_alone_without_captured_subject_cannot_verify_product(self):
        self.verified()
        for evidence in self.d['evidence']:
            evidence.pop('subject_source_ids')
        p = model.projection(self.d)
        self.assertEqual(p['verified_steps'], 0)
        self.assertFalse(p['criteria']['P1']['supported'])

    def test_product_change_invalidates_all_proof_of_its_baseline(self):
        self.verified()
        self.assertEqual(model.projection(self.d)['percent'], 100.0)
        (self.product / 'feature.txt').write_text('Entirely different product', encoding='utf-8')
        self.assertEqual(model.projection(self.d)['percent'], 0.0)

    def test_running_attempt_cannot_move_to_another_step(self):
        self.d['runs'] = [{'id': 'R1', 'step_id': 'S1', 'attempt': 1, 'status': 'RUNNING', 'source_ids': []}]
        store.initialize(self.d)
        self.d['runs'][0].update(step_id='S2', attempt=99)
        with self.assertRaisesRegex(model.ReportError, 'identity is immutable'):
            self.commit()

    def test_retests_count_once_and_latest_fail_wins(self):
        self.prove('P1')
        self.prove('P1', 'FAIL')
        p = model.projection(self.d)
        self.assertEqual((p['unique_checks'], p['evidence_records']), (1, 2))
        self.assertEqual(p['criteria']['P1']['evidence']['verdict'], 'FAIL')
        self.assertFalse(p['criteria']['P1']['supported'])

    def test_evidence_order_and_original_verdict_are_immutable(self):
        self.prove('P1')
        self.prove('P1', 'FAIL')
        store.initialize(self.d)
        original = copy.deepcopy(self.d['evidence'])
        for changed in (list(reversed(original)), original[:1], [{**original[0], 'verdict': 'FAIL'}, original[1]]):
            self.d['evidence'] = changed
            with self.assertRaisesRegex(model.ReportError, 'append-only'):
                self.commit()

    def test_criterion_links_cannot_hide_later_fail(self):
        a = self.prove('P1')
        b = self.prove('P1', 'FAIL')
        c = model.criteria(self.d)['P1'][0]
        c['evidence_ids'] = [a['id'], b['id']]
        store.initialize(self.d)
        c['evidence_ids'] = [a['id']]
        with self.assertRaisesRegex(model.ReportError, 'append-only'):
            self.commit()

    def test_checkpoint_cannot_borrow_fresh_proof_for_old_record(self):
        old = self.prove('P1')
        (self.docs / 'E1.log').write_text('Tampered', encoding='utf-8')
        self.prove('P1')
        self.d['current']['checkpoint'] = {'summary': 'Старый PASS', 'evidence_ids': [old['id']]}
        self.assertFalse(model.projection(self.d)['checkpoint_verified'])

    def test_checkpoint_rejects_wrong_axis_and_scope(self):
        wrong = self.prove('P1', axis='VISUAL')
        self.d['current']['checkpoint']['evidence_ids'] = [wrong['id']]
        self.assertFalse(model.projection(self.d)['checkpoint_verified'])
        good_other = self.prove('P2')
        self.d['current']['checkpoint']['evidence_ids'] = [good_other['id']]
        self.assertFalse(model.projection(self.d)['checkpoint_verified'])

    def test_current_verified_requires_actual_scoped_verification(self):
        self.d['current']['status'] = 'VERIFIED'
        self.assertEqual(model.projection(self.d)['current_status'], 'IMPLEMENTED_UNVERIFIED')
        self.verified()
        self.d['current']['evidence_ids'] = ['E2']
        self.assertEqual(model.projection(self.d)['current_status'], 'VERIFIED')

    def test_conflicting_statuses_disable_percentage(self):
        self.verified()
        self.d['conflicts'] = [{'id': 'X1', 'summary': 'Документы расходятся', 'status': 'OPEN', 'source_ids': ['plan']}]
        self.assertIsNone(model.projection(self.d)['percent'])

    def test_resolution_is_a_separate_event_with_evidence(self):
        self.d['conflicts'] = [{'id': 'X1', 'summary': 'Проверка была недоступна', 'status': 'OPEN', 'source_ids': ['plan']}]
        store.initialize(self.d)
        proof = self.prove('P1')
        self.d['conflicts'][0].update(status='RESOLVED', resolution_evidence_ids=[proof['id']])
        with self.assertRaisesRegex(model.ReportError, 'RESOLVED'):
            self.commit()
        result = self.commit('RESOLVED', 'Позднее проблема разрешена с доказательством')
        self.assertEqual(result['history'][-1]['event'], 'RESOLVED')
        self.assertEqual(model.projection(self.d)['open_conflicts'], [])

    def test_next_action_without_authority_remains_unknown(self):
        self.d['current']['next_action'].update(permission='ALLOWED', source_ids=[])
        self.assertEqual(model.projection(self.d)['next_permission'], 'UNKNOWN')

    def test_stale_revision_rejected_without_data_loss(self):
        store.initialize(self.d)
        self.commit(expected=1)
        before = self.tree()
        with self.assertRaisesRegex(model.ReportError, 'stale revision'):
            self.commit(expected=1)
        self.assertEqual(before, self.tree())

    def test_two_chats_can_only_commit_once_from_same_revision(self):
        store.initialize(self.d)
        input_path = self.root / 'candidate.json'
        input_path.write_text(json.dumps(self.d, ensure_ascii=False), encoding='utf-8')
        args = [sys.executable, '-B', str(SCRIPTS / 'project_reporting.py'), 'update', '--project-dir', str(self.dir),
                '--input', str(input_path), '--expected-revision', '1', '--event', 'REFRESHED', '--summary', 'Два чата']
        a = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        b = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        outputs = [a.communicate(timeout=20), b.communicate(timeout=20)]
        self.assertEqual(sorted([a.returncode, b.returncode]), [0, 1], outputs)
        self.assertEqual(store.load(self.dir)['revision'], 2)

    def test_actual_os_lock_rejects_another_process(self):
        store.initialize(self.d)
        input_path = self.root / 'candidate.json'
        input_path.write_text(json.dumps(self.d), encoding='utf-8')
        with store.locked(self.dir):
            p = self.cli('update', '--project-dir', self.dir, '--input', input_path,
                         '--expected-revision', 1, '--event', 'REFRESHED', '--summary', 'Другой чат')
        self.assertNotEqual(p.returncode, 0)
        self.assertIn('another chat', p.stderr)

    def test_invalid_update_preserves_last_good_html(self):
        store.initialize(self.d)
        before = (self.dir / 'report.html').read_bytes()
        self.d['plan']['steps'][0]['status'] = 'MADE_UP'
        with self.assertRaises(model.ReportError):
            self.commit()
        self.assertEqual((self.dir / 'report.html').read_bytes(), before)

    def test_write_failure_before_commit_preserves_previous_revision(self):
        store.initialize(self.d)
        before = (self.dir / 'report.html').read_bytes()
        original = store.atomic_write
        def fail(path, data):
            if path.name == 'state.json':
                raise OSError('Injected disk error')
            return original(path, data)
        with patch.object(store, 'atomic_write', side_effect=fail), self.assertRaises(OSError):
            self.commit()
        self.assertEqual(store.load(self.dir)['revision'], 1)
        self.assertEqual((self.dir / 'report.html').read_bytes(), before)

    def test_view_failure_after_commit_recovers_latest_committed_revision(self):
        store.initialize(self.d)
        self.d['current']['title'] = 'Важное новое состояние'
        original = store.atomic_write
        def fail(path, data):
            if path == self.dir / 'report.html':
                raise OSError('Injected view error')
            return original(path, data)
        with patch.object(store, 'atomic_write', side_effect=fail), self.assertRaisesRegex(model.ReportError, 'COMMITTED'):
            self.commit()
        token = model.file_hash(self.dir / 'report.html')
        result = store.recover(self.dir, token)
        self.assertEqual(result['document']['current']['title'], 'Важное новое состояние')
        self.assertIn('Важное новое состояние', (self.dir / 'report.html').read_text(encoding='utf-8'))

    def test_modified_visible_html_detected_even_with_intact_json(self):
        store.initialize(self.d)
        view = self.dir / 'report.html'
        view.write_text(view.read_text(encoding='utf-8').replace('<h1>', '<h1>Corrupt'), encoding='utf-8')
        with self.assertRaisesRegex(model.ReportError, 'stable HTML'):
            store.load(self.dir)
        result = store.recover(self.dir, model.file_hash(view))
        self.assertEqual(result['history'][-1]['event'], 'RECOVERED')
        self.assertNotIn('<h1>Corrupt', view.read_text(encoding='utf-8'))
        self.assertTrue(list((self.dir / 'recovery').rglob('report.html')))

    def test_corrupt_latest_state_falls_back_to_last_correct_revision(self):
        store.initialize(self.d)
        self.d['current']['title'] = 'Новое состояние'
        self.commit()
        commit, _, _ = store.latest(self.dir)
        (self.dir / 'revisions' / commit['bundle'] / 'state.json').write_text('{broken', encoding='utf-8')
        with self.assertRaises(model.ReportError):
            store.load(self.dir)
        recovered = store.recover(self.dir, model.file_hash(self.dir / 'report.html'))
        self.assertEqual(recovered['document']['current']['title'], 'Работа в первом шаге')
        self.assertEqual(recovered['revision'], 3)
        self.assertEqual(store.load(self.dir)['revision'], 3)

    def test_corrupt_head_and_commit_witness_can_be_recovered(self):
        store.initialize(self.d)
        self.commit()
        (self.dir / 'HEAD.json').write_text('broken', encoding='utf-8')
        (self.dir / 'revisions' / '00000002.commit.json').write_text('broken', encoding='utf-8')
        result = store.recover(self.dir, model.file_hash(self.dir / 'report.html'))
        self.assertEqual(result['revision'], 3)
        self.assertEqual(store.load(self.dir)['revision'], 3)

    def test_corrupt_marker_preserves_latest_valid_head_witness(self):
        store.initialize(self.d)
        self.d['current']['title'] = 'Сохрани последний подтверждённый срез'
        self.commit()
        (self.dir / 'revisions' / '00000002.commit.json').write_text('broken', encoding='utf-8')
        result = store.recover(self.dir, model.file_hash(self.dir / 'report.html'))
        self.assertEqual(result['document']['current']['title'], 'Сохрани последний подтверждённый срез')
        self.assertEqual(store.load(self.dir)['revision'], 3)

    def test_nested_phases_and_task_children_are_not_extra_plan_levels(self):
        for owner, key, child in [('phase', 'phases', {'id': 'nested'}),
                                  ('step', 'tasks', {'id': 'task-outside-phase'})]:
            d = copy.deepcopy(self.d)
            node = d['plan']['steps'][0] if owner == 'step' else d['plan']['steps'][0]['phases'][0]
            node[key] = [child]
            with self.subTest(owner=owner), self.assertRaises(model.ReportError):
                model.validate(d)

    def test_scope_ids_must_match_kinds_and_ancestry(self):
        self.d['current'] = {'step_id': 'S1.P1', 'status': 'UNKNOWN'}
        with self.assertRaisesRegex(model.ReportError, 'step_id'):
            model.validate(self.d)
        self.d['current'] = {'step_id': 'S1', 'status': 'UNKNOWN'}
        for run in ({'step_id': 'S1.P1'}, {'step_id': 'S1', 'phase_id': 'S2.P1'},
                    {'step_id': 'S1', 'phase_id': 'S1.P1', 'task_id': 'MISSING'}):
            self.d['runs'] = [{'id': 'bad-scope', 'attempt': 1, 'status': 'RUNNING', **run}]
            with self.subTest(run=run), self.assertRaises(model.ReportError):
                model.validate(self.d)

    def test_missing_view_can_be_recovered(self):
        store.initialize(self.d)
        (self.dir / 'report.html').unlink()
        store.recover(self.dir, 'MISSING')
        self.assertTrue((self.dir / 'report.html').exists())

    def test_recovery_rejects_stale_token(self):
        store.initialize(self.d)
        with self.assertRaisesRegex(model.ReportError, 'CAS rejected'):
            store.recover(self.dir, '0' * 64)

    def test_orphan_uncommitted_bundle_never_becomes_project_truth(self):
        store.initialize(self.d)
        self.d['current']['title'] = 'НЕ ЗАКОММИЧЕНО'
        original = store.atomic_write
        def fail(path, data):
            if path.name.endswith('.commit.json'):
                raise OSError('Interrupted before commit')
            return original(path, data)
        with patch.object(store, 'atomic_write', side_effect=fail), self.assertRaises(OSError):
            self.commit()
        recovered = store.recover(self.dir, model.file_hash(self.dir / 'report.html'))
        self.assertNotEqual(recovered['document']['current']['title'], 'НЕ ЗАКОММИЧЕНО')

    def test_symlink_recovery_does_not_copy_external_content(self):
        if os.name == 'nt':
            self.skipTest('Windows symlink creation needs a separate host privilege; POSIX covers no-follow semantics')
        store.initialize(self.d)
        external = self.root / 'private.txt'
        external.write_text('Private', encoding='utf-8')
        view = self.dir / 'report.html'
        view.unlink()
        view.symlink_to(external)
        with self.assertRaisesRegex(model.ReportError, 'symlink'):
            store.recover(self.dir, model.file_hash(external))
        self.assertFalse((self.dir / 'recovery').exists())

    def test_source_traversal_and_sensitive_paths_rejected(self):
        for path in ('../secret', '/etc/passwd', 'C:\\secret', '.env', 'a/.env.local', 'a//b'):
            with self.subTest(path=path), self.assertRaises(model.ReportError):
                model.relative_path(path)

    def test_identity_and_roots_cannot_silently_fork_report(self):
        store.initialize(self.d)
        self.d['project']['id'] = 'another-project'
        with self.assertRaisesRegex(model.ReportError, 'immutable'):
            self.commit()

    def test_html_is_self_contained_and_escapes_content(self):
        self.d['project']['title'] = '<script>alert(1)</script>'
        self.d['current']['title'] = '{{SNAPSHOT}} <img src=https://example.test/x>'
        output = render(store.initialize(self.d))
        self.assertIn('&lt;script&gt;', output)
        self.assertNotIn('<script>alert(1)', output)
        self.assertNotIn('<img src=', output)
        self.assertNotIn('<script src=', output)
        self.assertIn("default-src 'none'", output)
        from html.parser import HTMLParser
        class SnapshotParser(HTMLParser):
            data = ''
            reading = False
            def handle_starttag(self, tag_, attrs):
                if dict(attrs).get('id') == 'matreshka-project-state':
                    self.reading = True
            def handle_endtag(self, tag_):
                if tag_ == 'script': self.reading = False
            def handle_data(self, data):
                if self.reading: self.data += data
        parsed = SnapshotParser()
        parsed.feed(output)
        self.assertEqual(json.loads(parsed.data)['document']['project']['title'], self.d['project']['title'])

    def test_run_synchronizer_binds_detail_without_advancing_step(self):
        from sync_run_state import sync_bound, ASSIGNMENT, SNAPSHOT_START, SNAPSHOT_END
        store.initialize(self.d)
        run_dir = self.docs / '.matreshka' / 'runs' / 'R1'
        run_dir.mkdir(parents=True)
        state = {'runId': 'R1', 'stageOrder': ['source'], 'stages': [
            {'id': 'source', 'status': 'PASS', 'startedAt': '2026-10-18T09:00:00Z',
             'finishedAt': '2026-10-18T09:01:00Z'}], 'stateIntegrity': {'allowedConcurrentStagePairs': []}}
        (run_dir / 'dashboard-state.js').write_text(ASSIGNMENT + ' = ' + json.dumps(state) + ';', encoding='utf-8')
        (run_dir / 'dashboard.html').write_text('<html><script>' + SNAPSHOT_START +
                '\nwindow.MATRESHKA_RUN_STATE_SNAPSHOT=null;\n' + SNAPSHOT_END + '</script></html>', encoding='utf-8')
        sync_bound(run_dir, self.dir, 1, 'S1', 'S1.P1', None, 1, 'COMPLETE')
        from sync_run_state import load_state
        binding = load_state(run_dir / 'dashboard-state.js')[1]['projectBinding']
        self.assertEqual(binding['projectId'], 'example')
        self.assertEqual(binding['reportUrl'], (self.dir / 'report.html').as_uri())
        current = store.load(self.dir)
        self.assertEqual(current['document']['runs'][0]['status'], 'COMPLETE')
        self.assertEqual(model.projection(current['document'])['verified_steps'], 0)
        self.assertIn('R1', (self.dir / 'report.html').read_text(encoding='utf-8'))
        before = (run_dir / 'dashboard.html').read_bytes()
        with self.assertRaisesRegex(model.ReportError, 'stale'):
            sync_bound(run_dir, self.dir, 1, 'S1', None, None, 2, 'RUNNING')
        self.assertEqual((run_dir / 'dashboard.html').read_bytes(), before)

    def test_plugin_source_comparison_detects_same_version_different_bytes(self):
        from inspect_plugin_origin import inspect
        source, installed = self.root / 'source', self.root / 'installed'
        for path in (source, installed):
            path.mkdir()
            (path / 'plugin.json').write_text('{"version":"0.4.0"}', encoding='utf-8')
            (path / 'SKILL.md').write_text('Same content', encoding='utf-8')
        self.assertEqual(inspect(source, installed)['comparison'], 'MATCH')
        (installed / 'SKILL.md').write_text('Different cached content', encoding='utf-8')
        result = inspect(source, installed)
        self.assertEqual(result['comparison'], 'DIFFERENT')
        self.assertEqual(result['different_paths'], ['SKILL.md'])
        self.assertEqual(result['source']['version'], result['installed']['version'])
        self.assertEqual(inspect(source)['comparison'], 'UNAVAILABLE')

    def test_all_original_verdicts_are_readable_history(self):
        self.prove('P1', 'FAIL')
        self.prove('P1', 'PASS')
        output = render(store.initialize(self.d))
        self.assertIn('FAIL: наблюдаемый результат P1', output)
        self.assertIn('PASS: наблюдаемый результат P1', output)


if __name__ == '__main__':
    unittest.main()
