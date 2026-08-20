# Matreshka Agent

Matreshka Agent — переносимый набор из десяти skills для разработки с coding agents. Главная точка входа `building-end-to-end` принимает обычное описание проекта и передаёт его permission-aware controller-у, который сохраняет исходный замысел, изучает проект, строит спецификацию и план, организует реализацию/ревью/проверку и завершает работу только на основании свежих доказательств.

> **Статус ветки:** `0.5 development track`. Функциональный scope 0.5 находится в `dev/0.5-brief-traceability-observability`. Versioned plugin manifests пока намеренно остаются `0.4.0`, поэтому установленный development snapshot может отображаться как `0.4.0`. Это не означает отсутствие 0.5-функций. Версия будет повышена только после native acceptance и release-hardening.

## Самый простой запуск

Для проекта целиком используйте `building-end-to-end`.

| Платформа | Явный вызов |
| --- | --- |
| Claude Code | `/matreshka-agent:building-end-to-end` |
| Cursor | `/building-end-to-end` |
| Antigravity | Наберите `/` и выберите `building-end-to-end` |
| Codex | `$matreshka-agent:building-end-to-end`, `/skills`, либо optional `/prompts:matreshka-build` |

### Пользовательские режимы

- `interview` / `INTERVIEW` — сначала подробно опросить по продукту; вопросы только по решениям, которые нельзя безопасно получить из проекта.
- `assisted` / `ASSISTED` — режим по умолчанию; спрашивать только о действительно важных решениях.
- `full-auto` / `FULL_AUTO` — самостоятельно принимать безопасные обратимые локальные технические решения.

`FULL_AUTO` — это не «все права». Он не разрешает автоматически Git, сеть, установку зависимостей, browser download/launch, secrets, provider calls, deploy, изменение production/test data или другие внешние эффекты.

### Сценарии проекта

- `NEW_PROJECT` — новый проект;
- `CONTINUE_PROJECT` — проект уже вёлся Matreshka; незавершённый run восстанавливается, новая функция получает новый run;
- `EXISTING_PROJECT` — существующий проект, который раньше не использовал Matreshka; сначала выполняется read-only adoption/orientation.

Пользователю обычно не нужно указывать сценарий вручную: controller определяет его по фактическому состоянию репозитория.

## Главный workflow 0.5

```text
SOURCE_BRIEF
    ↓
U-REQUIREMENTS + S-SECURITY
    ↓
G1 — полнота уточнений
    ↓
SPECIFICATION
    ↓
G2 — независимая brief → spec сверка
    ↓
PROJECT INTELLIGENCE
    ↓
PLAN + G3
    ↓
RED → GREEN
    ↓
INDEPENDENT REVIEW
    ↓
TECHNICAL / SECURITY VERIFY
    ↓
BROWSER E2E, если применимо
    ↓
G4 BLIND ACCEPTANCE
    ↓
DOCUMENTATION DRIFT GATE
    ↓
FINISH / HANDOFF
```

## Исходный замысел и G1–G4

Matreshka 0.5 хранит три разных слоя требований:

- `SOURCE_BRIEF` — исходный запрос пользователя после безопасной редактуры credential values; исходное содержание не переписывается задним числом;
- `U-01`, `U-02`, ... — наблюдаемые пользовательские результаты;
- `S-01`, `S-02`, ... — требования Security by Design и negative proofs.

Четыре gates:

- **G1** — все материальные пользовательские требования имеют честный статус до завершения спецификации;
- **G2** — свежий независимый checker получает только source brief + candidate specification и ищет потерянные/суженные требования;
- **G3** — каждый живой `U-`/`S-` связан с task/proof, а каждая product-task имеет источник;
- **G4** — свежая blind acceptance получает исходный brief + фактический продукт и запрещено читать spec/manifest/plan/reports/dashboard. Материальный `PARTIAL`, `MISSING` или acceptance-critical `UNCHECKABLE` блокирует `COMPLETE`.

## Project Intelligence Layer

0.5 добавляет шесть coordination capabilities, не создавая шесть новых skills.

### P1 — Project Topology

Controller в read-only режиме определяет реальные архитектурные области, например:

```text
AREA-FRONTEND
AREA-BACKEND
AREA-DATA
AREA-E2E
```

или для CLI:

```text
AREA-CLI
AREA-PERSISTENCE
```

Frontend/backend не выдумываются по типу продукта. Код/config и применимые repository instructions важнее устаревшей документации.

### P2 — Area Context Router

Каждая task получает минимальный `AREA_CONTEXT_SET`: task brief, релевантные U/S, primary area, необходимые соседние interface contracts, scoped paths/commands и security/data/runtime invariants. Unrelated UI/deploy/history/raw logs/full branch diff исключаются.

Если корректность нельзя сохранить в узком контексте — `CONTEXT_TOO_BROAD` или split, а не скрытая потеря зависимостей.

### P3 — Cross-Area Interface Contract

Для producer/consumer seam создаётся один `IC-xx`, например frontend ↔ backend API. Он фиксирует input/output, errors, auth/data boundary, compatibility и integration proof. Producer и consumer используют одну identity/hash. Материальное изменение после freeze требует controller reconciliation (`INTERFACE_CHANGED`).

Run-local путь по умолчанию:

```text
.matreshka/runs/<run-id>/interfaces/IC-xx-<slug>.md
```

### P4 — Runtime Map

Matreshka отдельно знает, как наблюдать и как мутировать runtime:

```text
service / owner area
start / stop / status / logs
port/socket when evidenced
environment class
process ownership
mutation implications
```

Наличие status/log command не разрешает start/restart/kill. Неизвестный процесс на нужном порту нельзя массово убивать без доказанного ownership и permission.

### P5 — Documentation Drift Gate

После свежей проверки controller классифицирует:

```text
DOCS_NOT_REQUIRED
DOCS_CURRENT
DOCS_UPDATE_REQUIRED
DOCS_BLOCKED
DOCS_CONFLICT
```

Public API/interface, topology, runtime, persistence, auth/security, env semantics, durable test/deploy procedures и документированные user flows считаются durable truth. Private helper refactor обычно не требует docs update.

### P6 — Specialist Role Routing

Это role archetypes поверх существующих Matreshka skills, а не новые skills и не дополнительный agent budget:

```text
GENERAL_IMPLEMENTER
FRONTEND_IMPLEMENTER
BACKEND_IMPLEMENTER
DATA_MIGRATION_IMPLEMENTER
UI_SPECIALIST
TEST_E2E_SPECIALIST
DOCUMENTATION_MAINTAINER
BROWSER_CHECKER
REMOTE_OPERATOR
FILE_TRANSFER_OPERATOR
```

Например `UI_SPECIALIST` не может самовольно изменить backend API/business logic. Количество areas не создаёт по одному implementer на каждую область.

## Browser/E2E и Browser G4

Для web-проектов Matreshka сначала ищет существующую E2E-инфраструктуру. Playwright, Cypress, Selenium, WebdriverIO или другой repository-native seam имеют приоритет над установкой нового framework.

Раздельно фиксируются:

1. **Automated E2E** — техническая проверка существующим test runner;
2. **Browser G4** — независимая пользовательская приёмка в свежем контексте.

`E2E PASS` не означает `G4 PASS`.

Без отдельного разрешения Matreshka не устанавливает browser/framework, не скачивает Chromium/Chrome, не запускает server, не bind-ит port и не reset-ит test database. Personal Chrome profile, ambient cookies/session и чужие вкладки не являются доверенным test context.

## Dashboard, время и токены

При разрешённом run-state Matreshka может создать:

```text
.matreshka/runs/<run-id>/dashboard.html
.matreshka/runs/<run-id>/dashboard-state.js
```

Dashboard — только projection. Он не даёт authority и не доказывает completion.

Русскоязычный run показывает по-русски:

- общий прогресс;
- покрытие brief;
- текущий этап;
- задачи/тесты/требования/security;
- Project Topology, interfaces, Runtime Map, docs drift и specialist;
- Browser/E2E;
- permissions;
- последнюю проверенную точку и следующее действие;
- wall-clock и implementation time, если есть точные timestamps;
- token usage только из host counters.

Token status:

- `EXACT` — доступен полный совместимый счётчик;
- `PARTIAL` — видна только точная наблюдаемая часть;
- `UNAVAILABLE` — host не отдаёт надёжный counter.

Matreshka не оценивает токены по символам, времени или числу сообщений.

## Профиль качества, автономность и permissions — разные измерения

Execution profile:

- **maximum speed** — только ясная low-risk механика;
- **balanced** — рекомендуется большинству задач;
- **maximum quality** — auth/isolation/migrations/secrets/persistence/production-boundaries.

Internal controller autonomy:

- managed;
- autonomous local;
- extended autonomous — только явно перечисленные Git/network/browser/runtime/remote операции.

Permission envelope отдельно ограничивает filesystem, commands, browser/process/port, Git workspace/history/remote, dependencies/network, secrets, test-data mutation, remote/production/destructive actions и срок действия.

## Десять bundled skills

| Skill | Назначение |
| --- | --- |
| `building-end-to-end` | одна plain-language точка входа для нового/существующего проекта |
| `orchestrating-subagent-work` | controller, recovery, audit, Project Intelligence, permissions и dispatch |
| `specifying-software-work` | security-by-design specification |
| `planning-software-work` | U/S coverage, topology/interfaces/context и executable task plan |
| `writing-portable-agent-prompt` | переносимый prompt без выполнения |
| `implementing-with-tests` | scoped RED → GREEN implementation |
| `debugging-systematically` | root-cause investigation |
| `reviewing-agent-work` | independent scoped code/security/interface review |
| `verifying-development-work` | fresh technical/security/E2E/G4 evidence |
| `finishing-development-work` | docs gate, разрешённый Git/remote action или точный handoff |

## Бюджеты и независимость

- balanced task: максимум два уникальных основных subagent roles и четыре started agent turns;
- maximum quality: максимум три основных роли и шесть turns;
- только одна consolidated fixer wave;
- fix и targeted re-review продолжают исходные threads, когда host поддерживает resume;
- повторный Critical/Important после fixer wave → `STOP_AND_RESCOPE`;
- только один writer в checkout одновременно;
- parallel по умолчанию только для независимых read-only roles;
- specialist routing не увеличивает budget автоматически.

## Локальная проверка development-пакета

Из корня репозитория:

```bash
python3 -B plugins/matreshka-agent/scripts/validate_package.py \
  plugins/matreshka-agent --marketplace-root . --self-test

python3 -B plugins/matreshka-agent/scripts/check_dev_05.py \
  plugins/matreshka-agent

python3 -B plugins/matreshka-agent/scripts/doctor.py \
  plugins/matreshka-agent --marketplace-root .
```

`validate_package.py`, `check_dev_05.py` и `doctor.py` работают read-only/offline. GitHub Actions на `main` и `dev/**` выполняет эти проверки на Python 3.11.

## Что 0.5 не добавляет автоматически

- Pi `.pi/mcp.json` или обязательный MCP-server;
- hooks;
- telemetry/analytics;
- dependency installation;
- browser download;
- secret access;
- Git/remote/deploy authority;
- production database mutation;
- автоматическую глобальную память/самоизменение Matreshka.

## До release 0.5.0

Development scope может считаться release-ready только после:

- deterministic package/self-test + 0.5 integrity + doctor PASS;
- native acceptance core workflow;
- disposable full-stack web acceptance для Browser/E2E + Project Intelligence;
- проверенных native claims для реально заявляемых hosts;
- version bump manifests/marketplaces/validator/doctor/evals;
- финальной publisher/security metadata проверки.

До этого ветка остаётся development preview и не должна называться опубликованным `0.5.0`.
