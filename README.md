# Matreshka Agent

Matreshka Agent — переносимый permission-aware workflow для разработки с coding agents. Он превращает обычный запрос пользователя в трассируемую спецификацию, план, ограниченные задачи для субагентов, RED→GREEN реализацию, независимый review, свежую техническую/браузерную проверку и честный финальный handoff.

> **Текущий статус:** ветка `dev/0.5-brief-traceability-observability` содержит функциональный scope 0.5 и проходит отдельный hardening. Versioned plugin manifests пока намеренно остаются `0.4.0`; это development snapshot, а не опубликованный `0.5.0`.

Подробная документация пакета: [`plugins/matreshka-agent/README.md`](plugins/matreshka-agent/README.md).

## Одна точка входа

Для разработки проекта целиком:

```text
$matreshka-agent:building-end-to-end
```

В Claude Code используется namespaced slash-вызов, в Cursor/Antigravity — зарегистрированный skill/slash entry, в Codex — `$skill`, `/skills` или optional `/prompts:matreshka-build` wrapper.

### Режимы

```text
interview   — сначала подробно опросить по продукту
assisted    — спрашивать только важное (по умолчанию)
full-auto   — самостоятельно принимать безопасные обратимые локальные решения
```

### Сценарии проекта

```text
NEW_PROJECT       — новый проект
CONTINUE_PROJECT  — продолжить проект, который уже вела Matreshka
EXISTING_PROJECT  — подключить Matreshka к существующему проекту
```

`FULL_AUTO` управляет количеством вопросов, **не полномочиями**. Git, network, dependency/browser install, secrets, process/port, test-data mutation, deploy и remote действия остаются отдельными permissions.

## Workflow 0.5

```text
SOURCE_BRIEF
   ↓
U-REQUIREMENTS + S-SECURITY
   ↓
G1
   ↓
SPECIFICATION
   ↓
G2 independent brief → spec
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
BROWSER E2E (если применимо)
   ↓
G4 BLIND ACCEPTANCE
   ↓
DOCUMENTATION DRIFT GATE
   ↓
FINISH / HANDOFF
```

## Что добавлено в 0.5 development track

### Source Intent Traceability

- исходный `SOURCE_BRIEF` сохраняется отдельно от последующих интерпретаций;
- пользовательские outcomes получают `U-01`, `U-02`, ...;
- security controls остаются отдельными `S-01`, `S-02`, ...;
- G1 проверяет полноту уточнений;
- G2 свежим независимым контекстом сверяет brief со specification;
- G3 проверяет `requirement ↔ task ↔ evidence` в обе стороны;
- G4 свежим blind checker-ом проверяет фактический продукт по исходному brief, не читая spec/plan/reports/dashboard.

Материальный `PARTIAL`, `MISSING` или acceptance-critical `UNCHECKABLE` не позволяет назвать проект `COMPLETE`.

### Project Intelligence Layer

Matreshka не предполагает, что любой сайт обязательно состоит из frontend/backend. Она сначала строит фактическую карту проекта.

```text
P1 PROJECT_TOPOLOGY
P2 AREA_CONTEXT_SET
P3 CROSS-AREA IC-xx CONTRACTS
P4 RUNTIME_MAP
P5 DOCUMENTATION_DRIFT_GATE
P6 SPECIALIST_ROLE_ROUTING
```

Пример full-stack topology:

```text
AREA-FRONTEND
AREA-BACKEND
AREA-DATA
AREA-E2E
```

Пример CLI:

```text
AREA-CLI
AREA-PERSISTENCE
```

Каждая task получает только нужный area-context. Cross-area producer/consumer seam фиксируется одним `IC-xx`; frontend и backend не должны независимо придумывать разные формы одного API. Runtime Map отделяет чтение status/logs от start/stop/kill authority. Documentation Drift Gate обновляет docs только когда verified behavior реально изменил durable contract. Specialist roles сужают ответственность, но не увеличивают agent budget и permissions.

### Browser E2E + Browser G4

Matreshka сначала использует существующий repository-native Playwright/Cypress/Selenium/WebdriverIO/E2E seam. Она не устанавливает второй framework без отдельного разрешения.

Automated E2E и Browser G4 — разные проверки:

```text
E2E PASS ≠ G4 PASS
```

Browser G4 использует только разрешённый изолированный test context. Personal Chrome profile, ambient cookies/session и неизвестные destructive DB setup не считаются безопасными по умолчанию.

### Русский dashboard, время и токены

При разрешённом run-state:

```text
.matreshka/runs/<run-id>/dashboard.html
.matreshka/runs/<run-id>/dashboard-state.js
```

Dashboard показывает по-русски:

- общий прогресс;
- brief coverage;
- этапы и задачи;
- тесты и Security proofs;
- Project Topology / interfaces / Runtime / docs state / specialist;
- Browser/E2E и G4;
- текущие permissions;
- wall-clock / implementation time, если есть точные timestamps;
- token usage только из реально доступных host counters.

Если токены недоступны, dashboard пишет `Недоступно`; Matreshka не выдумывает оценку по символам или времени.

Dashboard — только projection и никогда не является permission или доказательством completion.

## Десять skills

| Skill | Назначение |
| --- | --- |
| `building-end-to-end` | пользовательская end-to-end точка входа |
| `orchestrating-subagent-work` | controller, permissions, recovery, Project Intelligence |
| `specifying-software-work` | security-by-design specification |
| `planning-software-work` | task plan, U/S coverage, topology/interface/context routing |
| `writing-portable-agent-prompt` | переносимый prompt |
| `implementing-with-tests` | scoped RED→GREEN implementation |
| `debugging-systematically` | root-cause debugging |
| `reviewing-agent-work` | independent scoped review |
| `verifying-development-work` | technical/security/E2E/G4 evidence |
| `finishing-development-work` | docs gate, Git/remote boundary или handoff |

## Профили выполнения

- **maximum speed** — маленькая low-risk механика;
- **balanced** — рекомендуется большинству задач;
- **maximum quality** — auth/isolation/migrations/secrets/persistence/production boundaries.

Профиль не является permission. Balanced обычно ограничивает задачу двумя основными ролями и четырьмя started agent turns; maximum quality — тремя ролями и шестью turns. Только одна consolidated fixer wave. Writer-ы не работают параллельно в одном checkout.

## Проверка development-пакета

Из корня репозитория:

```bash
python3 -B plugins/matreshka-agent/scripts/validate_package.py \
  plugins/matreshka-agent --marketplace-root . --self-test

python3 -B plugins/matreshka-agent/scripts/check_dev_05.py \
  plugins/matreshka-agent

python3 -B plugins/matreshka-agent/scripts/doctor.py \
  plugins/matreshka-agent --marketplace-root .
```

GitHub Actions запускает эти проверки на Python 3.11 для `main`, `dev/**` и pull requests.

`validate_package.py` проверяет упаковку, manifests/marketplaces, skills/evals, links, secret-like files, symlink containment, executable policy, запрещённые runtime/dependency components и negative fixtures.

`check_dev_05.py` дополнительно проверяет наличие и cross-skill wiring именно development-функций 0.5: launch UX, source brief/G1–G4, Russian dashboard/timing/tokens, Browser/E2E, Project Intelligence P1–P6 и eval JSON.

`doctor.py` остаётся read-only/offline диагностикой и отдельно сообщает release metadata warnings.

## Что намеренно не является встроенной властью Matreshka

- Pi `.pi/mcp.json` или обязательный MCP server;
- hooks/telemetry;
- автоматическая установка dependency/browser;
- автоматический доступ к secrets;
- Git/push/deploy/production authority;
- destructive test/database setup;
- использование личного browser profile;
- автоматическая глобальная память/самоизменение skill-ов.

## Перед выпуском 0.5.0

Нужно получить не только static package PASS, но и native evidence:

1. финальный CI PASS;
2. latest-checkout package validator/self-test + 0.5 integrity + doctor;
3. disposable full-stack acceptance для Project Intelligence + Browser/E2E/G4 + docs drift + dashboard;
4. native smoke для реально заявляемых hosts;
5. затем version bump manifests/marketplaces/validator/doctor/evals до `0.5.0` и финальная publisher/security metadata проверка.

До этого `dev/0.5-brief-traceability-observability` остаётся development preview.
