# Matreshka Agent

Matreshka Agent — набор из девяти переносимых skills для разработки с coding agents. Главный controller помогает исследовать проект, провести брейншторм, подготовить security-by-design спецификацию и план, ограниченно запустить implementer/reviewer, проверить результат и сохранить точный handoff.

Статус `0.3.0`: development preview. Пакет проходит локальную структурную и security-валидацию, но ещё не считается публичным релизом без native installation smoke tests, финальных publisher metadata и иконки.

## Первый запуск

Обычно нужен только `orchestrating-subagent-work`.

| Платформа | Явный вызов |
| --- | --- |
| Claude Code | `/matreshka-agent:orchestrating-subagent-work` |
| Cursor | `/orchestrating-subagent-work` |
| Antigravity | Наберите `/` и выберите `orchestrating-subagent-work` |
| Codex | Откройте `/skills` и выберите навык либо используйте доступный `$` skill picker; optional `/prompts:matreshka-orchestrate` — после установки wrapper |

Codex не превращает plugin skills в отдельные `/skill-name` команды. Для пользователей, которым нужен именно slash-вызов, в [`codex-prompts/`](codex-prompts/README.md) лежат девять необязательных local custom-prompt wrappers. После явного копирования в `~/.codex/prompts/` главный вызов будет `/prompts:matreshka-orchestrate`. Codex помечает custom prompts как устаревающий compatibility mechanism, поэтому обычный `$skill` или `/skills` остаётся предпочтительным путём.

Если в списке есть навыки с похожими названиями, выбирайте `matreshka-agent:<skill-name>` в Codex и Claude Code либо запись, у которой виден источник Matreshka Agent. Название само по себе не доказывает, что это навык из данного плагина.

В интерфейсах Codex карточки и плашки навыков версии `0.3.0` используют формат `Название действия · Matreshka Agent`, поэтому сначала видна задача, а затем источник навыка.

Пример для новичка:

```text
Помоги добавить вход через Google. Я не программист.
Сначала изучи проект в read-only режиме, предложи варианты простыми словами,
порекомендуй профиль и покажи, какие разрешения действительно нужны.
Не делай push, deploy и remote migration.
```

## Девять skills

| Skill | Назначение |
| --- | --- |
| `orchestrating-subagent-work` | Полный end-to-end controller |
| `specifying-software-work` | Брейншторм, 2–3 подхода и подробная security-by-design спецификация |
| `planning-software-work` | Coverage matrix и маленькие executable tasks |
| `writing-portable-agent-prompt` | Prompt для другого coding agent без выполнения |
| `implementing-with-tests` | Ограниченная реализация через focused RED/GREEN |
| `debugging-systematically` | Read-only доказательство первопричины |
| `reviewing-agent-work` | Независимый scoped review |
| `verifying-development-work` | Свежая проверка completion claims |
| `finishing-development-work` | Разрешённый commit/remote action или точный handoff |

## Профиль и автономность — разные решения

Controller предлагает один профиль выполнения:

- maximum speed — только для ясной low-risk механики;
- balanced — рекомендуемый вариант для большинства задач;
- maximum quality — для auth, isolation, migrations, secrets, persistence и production handoff.

Отдельно выбирается формат согласований:

- managed — подтверждение переходов между specification, plan и execution;
- autonomous local — самостоятельная работа внутри точного локального scope;
- extended autonomous — только дополнительно перечисленные Git/network/remote actions.

«Полная автономность» не означает безграничные права. После read-only preflight controller предлагает один конечный permission envelope: project root, scope, local writes/checks, Git, remote targets, secrets method, expiry и stop conditions. Уже подтверждённое действие в неизменившихся границах не запрашивается снова. System/developer instructions, repository policy, sandbox и native approvals всегда остаются выше текстового разрешения.

## Главные ограничения

- Controller владеет Git и remote boundaries; implementer/reviewer их не выполняют.
- Сбалансированный task использует максимум двух уникальных субагентов и четырёх agent turns.
- Fix и re-review продолжают исходные threads.
- Допускается только одна consolidated fixer-wave.
- Повторный Critical/Important finding приводит к `STOP_AND_RESCOPE`.
- Пишущие роли не работают параллельно в одном checkout.
- Completion требует свежего evidence: command, exit code, counts и relevant note.

## Quality Gate, project profile и направленное обучение

Перед implementation controller может прочитать или создать **project-local profile**: карту разрешённых навыков, известных команд, ограничений репозитория и источника каждого skill. Она не является вечной памятью: перед повторным использованием факты из неё заново сверяются с текущим репозиторием.

Для задачи controller фиксирует **quality gate** — небольшой список уже существующих и разрешённых проверок. Gate не создаёт hooks, не устанавливает зависимости и не даёт разрешения на network, secrets, commit или deploy. Невыполненная обязательная проверка остаётся причиной для `PARTIALLY_VERIFIED` или `BLOCKED`, а не скрытым предупреждением.

Направленное обучение имеет три режима:

- `OFF` — по умолчанию; ничего не собирается;
- `PROPOSE` — в конце можно подготовить один project-local candidate с командой, результатом и ограничением применимости;
- `LOCAL_REVIEWED` — такой candidate можно использовать только после отдельного согласия человека и независимой повторной проверки в следующей подходящей задаче.

Candidate никогда не изменяет сам Matreshka Agent, глобальные инструкции, hooks или настройки среды автоматически. В него нельзя переносить секреты, персональные данные, private URLs, полный raw log или скрытые рассуждения агента.

## Спецификации, планы и безопасность

После того как Matreshka задала и получила ответы на действительно важные вопросы, она сохраняет спецификацию в `docs/specs/YYYY-MM-DD-<задача>-spec.md`. После утверждения спецификации `planning-software-work` создаёт связанный план в `docs/plans/YYYY-MM-DD-<задача>-plan.md`.

Если в проекте уже есть ясная совместимая структура документации, она сохраняется. Если папок ещё нет, Matreshka создаёт только недостающие `docs/`, `docs/specs/` и `docs/plans/`; она не перемещает и не переписывает существующие документы. При отсутствии разрешения на запись она выдаёт полный документ и точный путь со статусом `SPEC_READY_TO_SAVE` или `PLAN_READY_TO_SAVE`.

Каждая спецификация получает обязательный Security by Design baseline. Для актуальных рисков создаются требования `S-01`, `S-02` и так далее: у каждого есть конкретный control, ответственный этап и negative proof. Это покрывает секреты, server-side authorization и tenant isolation, ввод/вывод, утечки данных, необратимые действия, зависимости и инфраструктуру; для AI/RAG/tool-use отдельно проверяются prompt injection, утечка данных и неразрешённый вызов tools. Высокорисковый scope требует threat model и security/code review.

Эти правила снижают риск, но не являются обещанием абсолютной неуязвимости. Matreshka не устанавливает security-scanner, не читает secrets и не запускает сетевые проверки без разрешения и без уже существующей команды проекта.

## Локальная проверка пакета

Из корня marketplace-репозитория:

```bash
python3 -B plugins/matreshka-agent/scripts/validate_package.py \
  plugins/matreshka-agent --marketplace-root . --self-test

python3 -B plugins/matreshka-agent/scripts/doctor.py \
  plugins/matreshka-agent --marketplace-root .
```

`doctor.py` работает read-only и offline. Он ничего не устанавливает, не создаёт hooks и не меняет настройки пользователя.

## Что намеренно не входит в 0.3.0

- hooks;
- MCP servers и apps;
- telemetry;
- автоматическая установка dependencies;
- доступ к secrets по умолчанию.
- глобальная или автоматическая «самонастройка» по итогам задач.

Hooks будут рассматриваться только после eval evidence, если повторяющуюся ошибку нельзя надёжно устранить инструкцией или детерминированной проверкой.
