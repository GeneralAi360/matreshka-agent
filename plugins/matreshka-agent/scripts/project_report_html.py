"""Offline HTML renderer. No JavaScript runtime or network dependency."""
from __future__ import annotations

import html
import json
import re
from pathlib import Path

from project_report_model import projection, safe_file

LABELS = {'UNKNOWN': 'Неизвестно', 'NOT_STARTED': 'Не начато', 'IN_PROGRESS': 'В работе',
          'IMPLEMENTED_UNVERIFIED': 'Реализовано, не проверено', 'VERIFIED': 'Проверено',
          'WAITING_APPROVAL': 'Ожидает одобрения', 'BLOCKED': 'Заблокировано', 'PENDING': 'Ожидается',
          'APPROVED': 'Одобрено', 'REJECTED': 'Отклонено', 'NOT_REQUIRED': 'Не требуется — есть решение',
          'PASS': 'PASS', 'FAIL': 'FAIL', 'PARTIAL': 'Частичный результат', 'NOT_RUN': 'Не запускалось',
          'FULL': 'Полная', 'UNAVAILABLE': 'Недоступна', 'ALLOWED': 'Разрешено по указанному основанию',
          'REQUIRES_APPROVAL': 'Требуется одобрение', 'COMPLETE': 'Запуск завершён', 'STOPPED': 'Остановлен',
          'FAILED': 'Ошибка', 'RUNNING': 'В работе', 'AGREED': 'Согласован', 'PROPOSED': 'Предложен',
          'TECHNICAL': 'Техническая', 'VISUAL': 'Визуальная', 'ACCEPTANCE': 'Приёмочная'}


def esc(value):
    return html.escape(str(value if value is not None else ''), quote=True)


def tag(value):
    return '<span class="tag ' + esc(value) + '">' + esc(LABELS.get(value, value)) + '</span>'


def render(envelope):
    d = envelope['document']
    p = projection(d)
    project, plan, current = d['project'], d['plan'], d.get('current', {})
    sources = {s['id']: s for s in d.get('sources', [])}
    def source_links(ids):
        links = []
        for id_ in ids:
            s = sources[id_]
            title = esc(s.get('summary') or s.get('path') or id_)
            if s['root'] == 'statement':
                links.append('<span title="Записанное утверждение/решение; не технический тест">' + esc(id_) + ': ' + title + '</span>')
            else:
                uri = safe_file(project[s['root'] + '_root'], s['path']).as_uri()
                links.append('<a href="' + esc(uri) + '">' + esc(id_) + ': ' + title + '</a>')
        return ' · '.join(links) or '<span class="muted">Основание неизвестно</span>'
    def list_items(values):
        return '<ul>' + ''.join('<li>' + esc(v) + '</li>' for v in values) + '</ul>' if values else '<p class="muted">Не зафиксировано</p>'
    def node_html(node, level):
        result = p['nodes'][node['id']]
        opening = ' open' if node['id'] == current.get('step_id') else ''
        text = '<details' + opening + '><summary>' + esc(node['id'] + ' · ' + node['title']) + ' ' + tag(result['status']) + '</summary><div>'
        text += '<p><strong>Ожидаемый результат:</strong> ' + esc(node.get('expected_result') or 'Неизвестен') + '</p>'
        text += '<p>Техническое состояние: ' + tag(result['technical']) + ' Одобрение: ' + tag(result['approval']) + '</p>'
        text += '<p class="scope">Исходное заявление: ' + esc(node['status']) + ' · ' + source_links(node.get('source_ids', [])) + '</p>'
        if node.get('actual_result'):
            text += '<p><strong>Фактический результат (заявлен):</strong> ' + esc(node['actual_result']) + '</p>'
        if node.get('criteria'):
            text += '<div class="table-wrap"><table><thead><tr><th>Критерий / ожидается</th><th>Как проверяем</th><th>Получено / доказательство</th></tr></thead><tbody>'
            for c in node['criteria']:
                r = p['criteria'][c['id']]
                e = r['evidence']
                actual = tag('PASS') if r['supported'] else tag(
                    'IMPLEMENTED_UNVERIFIED' if e and e['verdict'] == 'PASS' else (e['verdict'] if e else 'NOT_RUN'))
                if e:
                    actual += '<p>' + esc(e['actual']) + '</p><small>' + esc(e['observed_at']) + ' · ' + esc(e['id']) + '</small><p>' + source_links(e.get('source_ids', [])) + '</p>'
                    if not r['supported']:
                        actual += '<p><small>Исходный вердикт: ' + esc(e['verdict']) + '; качество: ' + esc(LABELS[e['quality']]) + '</small></p>' + list_items(e.get('limitations', []))
                        actual += '<small>Не подтверждает полную актуальную проверку: учитываются ось, качество, ограничения, версия критерия и источников.</small>'
                text += '<tr><td><code>' + esc(c['id']) + '</code><p>' + esc(c['expected']) + '</p><small>' + ('Обязательный' if c['required'] else 'Дополнительный') + '</small></td><td>' + esc(c['method']) + '<p>' + esc(LABELS[c['axis']]) + '</p></td><td>' + actual + '</td></tr>'
            text += '</tbody></table></div>'
        else:
            text += '<p class="note">Критерии и доказательства неизвестны. Завершение не подтверждено.</p>'
        for child in node.get('phases', []) + node.get('tasks', []):
            text += node_html(child, level + 1)
        return text + '</div></details>'
    percent = p['percent']
    progress = (str(percent) + '%') if percent is not None else 'Не определён'
    body = '<header><div class="eyebrow">Matreshka Agent · постоянный отчёт проекта</div><h1>' + esc(project['title']) + '</h1><p>' + esc(project['goal']) + '</p><p class="muted">Срез на ' + esc(envelope['updated_at']) + ' · ревизия ' + str(envelope['revision']) + ' · проект <code>' + esc(project['id']) + '</code></p></header>'
    body += '<div class="grid"><div class="card"><div class="eyebrow">Весь проект</div><h2>Подтверждённые шаги</h2><div class="metric">' + progress + '</div>'
    body += '<p>' + str(p['verified_steps']) + ' из ' + str(p['total_steps']) + ' известных шагов технически проверено</p>'
    if percent is not None:
        body += '<div class="progress"><span style="width:' + str(percent) + '%"></span></div><small>Формула: ' + str(p['verified_steps']) + ' / ' + str(p['total_steps']) + ' × 100. Это доля шагов согласованного плана, а не трудозатрат.</small>'
    else:
        body += '<p class="note">Процент не рассчитывается: нет актуального согласованного плана или есть открытые противоречия.</p>'
    body += '<p>План r' + str(plan['revision']) + ': ' + tag(plan['status']) + ' Одобрение: ' + tag(p['plan_approval']) + '</p><p>' + source_links(plan.get('source_ids', [])) + '</p></div>'
    body += '<div class="card"><div class="eyebrow">Текущая работа</div><h2>' + esc(current.get('title') or 'Задача не определена') + '</h2>' + tag(p['current_status'])
    body += '<p class="scope">' + esc(' → '.join(current[k] for k in ('step_id', 'phase_id', 'task_id') if current.get(k))) + '</p>'
    checkpoint = current.get('checkpoint', {})
    body += '<h3>Последнее подтверждённое состояние</h3><p>' + esc(checkpoint.get('summary') or 'Не установлено') + '</p>'
    body += tag('VERIFIED' if p['checkpoint_verified'] else 'UNKNOWN') + '<p><small>Доказательства: ' + esc(', '.join(checkpoint.get('evidence_ids', [])) or 'отсутствуют') + '</small></p>'
    action = current.get('next_action', {})
    body += '<h3>Следующий шаг</h3><p>' + esc(action.get('summary') or 'Нужно определить') + '</p>' + tag(p['next_permission']) + '<p>' + source_links(action.get('source_ids', [])) + '</p><small>Обновление отчёта не разрешает продолжать разработку.</small></div></div>'
    body += '<section><h2>Ограничения и решения</h2><h3>Что мешает продолжению</h3>' + list_items(current.get('blockers', []))
    body += '<h3>Что требуется решить</h3>' + list_items(current.get('questions', []))
    body += '<h3>Ограничения проверки</h3>' + list_items(d.get('limitations', []))
    for conflict in p['open_conflicts']:
        body += '<div class="note"><strong>Противоречие ' + esc(conflict['id']) + '</strong><p>' + esc(conflict['summary']) + '</p>' + source_links(conflict.get('source_ids', [])) + '</div>'
    body += list_items(p['findings']) if p['findings'] else ''
    body += '</section><section><h2>План проекта: шаги и фазы</h2><p class="muted">Исправления и повторные попытки остаются внутри своего шага.</p><div class="legend">' + ''.join(tag(s) for s in ('NOT_STARTED', 'IN_PROGRESS', 'IMPLEMENTED_UNVERIFIED', 'VERIFIED', 'WAITING_APPROVAL', 'BLOCKED', 'UNKNOWN')) + '</div>'
    body += ''.join(node_html(n, 0) for n in plan['steps']) or '<p class="note">Шаги неизвестны. Сначала восстановите или согласуйте план.</p>'
    body += '</section><section><h2>Проверки и исходные вердикты</h2><p>' + str(p['unique_checks']) + ' уникальных проверок (check_id + subject); ' + str(p['evidence_records']) + ' записей доказательств. Повторные прогоны не увеличивают число уникальных проверок.</p>'
    for e in d.get('evidence', []):
        body += '<details><summary>' + esc(e['id'] + ' · ' + e['check_id'] + ' · ' + e['criterion_id']) + ' ' + tag(e['verdict']) + '</summary><div><p>' + esc(e['actual']) + '</p><p>Ось: ' + esc(LABELS[e['axis']]) + ' · качество: ' + tag(e['quality']) + '</p><p>' + esc(e['observed_at']) + ' · объект: ' + esc(e['subject']) + '</p>' + list_items(e.get('limitations', [])) + source_links(e.get('source_ids', [])) + '<p><code>Критерий: ' + esc(e['criterion_hash']) + '</code></p></div></details>'
    body += '</section><section><h2>Запуски и попытки</h2><p class="muted">Завершение запуска не означает завершение проекта.</p>'
    for run in d.get('runs', []):
        link = run.get('report')
        href = safe_file(project[link['root'] + '_root'], link['path']).as_uri() if link else None
        body += '<p>' + ('<a href="' + esc(href) + '">' + esc(run['id']) + '</a>' if href else esc(run['id'])) + ' · ' + esc(run['step_id']) + ' · попытка ' + str(run['attempt']) + ' ' + tag(run['status']) + '</p>'
    body += '</section><section><h2>Основания и актуальность</h2><p class="muted">Хеш подтверждает неизменность файла, а не истинность его содержания. Исторический документ не становится текущим автоматически.</p><p>Продукт: <code>' + esc(project['product_root']) + '</code><br>Документация разработки: <code>' + esc(project['documentation_root']) + '</code></p>'
    for s in sources.values():
        body += '<details><summary>' + esc(s['id']) + ' · ' + esc(s['status']) + ' · ' + esc(p['freshness'][s['id']]) + '</summary><div><p>' + source_links([s['id']]) + '</p><p><code>' + esc(s['sha256']) + '</code></p><p>Заменяет: ' + esc(', '.join(s.get('supersedes', [])) or '—') + '</p></div></details>'
    body += '</section><section class="history"><h2>История изменений</h2><ol>'
    for e in envelope['history']:
        body += '<li><strong>r' + str(e['revision']) + ' · ' + esc(e['event']) + '</strong> · ' + esc(e['at']) + '<p>' + esc(e['summary']) + '</p>' + source_links(e.get('source_ids', [])) + '</li>'
    body += '</ol></section><footer>Самодостаточный локальный HTML. Показан сохранённый срез; изменения источников требуют REFRESHED. Визуальная проверка подтверждается только отдельным фактическим просмотром.</footer>'
    snapshot = json.dumps(envelope, ensure_ascii=False, separators=(',', ':')).replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e')
    template = (Path(__file__).resolve().parents[1] / 'assets/project-report-template.html').read_text(encoding='utf-8')
    # Replace fixed tokens once; user content must never be interpreted as a token.
    values = {'TITLE': esc(project['title']), 'BODY': body, 'SNAPSHOT': snapshot}
    return re.sub(r'\{\{(TITLE|BODY|SNAPSHOT)\}\}', lambda match: values[match.group(1)], template)
