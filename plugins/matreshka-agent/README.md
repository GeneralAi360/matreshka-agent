# Matreshka Agent

Matreshka Agent — переносимый permission-aware набор из **одиннадцати bundled skills** для разработки с coding agents. Главная точка входа `building-end-to-end` принимает обычное описание проекта и передаёт его controller-у, который сохраняет исходный замысел, изучает реальную структуру проекта, ведёт UX/UI-контракт для пользовательских интерфейсов, строит specification/plan, организует RED→GREEN реализацию, независимые review/verification и завершает работу только на основании свежих доказательств.

> **Статус ветки:** `0.5 development track` в `dev/0.5-brief-traceability-observability`. Versioned plugin manifests намеренно остаются `0.4.0`, поэтому development snapshot может показываться как `0.4.0`. Это не release claim.

## Самый простой запуск

| Платформа | Явный вызов |
| --- | --- |
| Claude Code | `/matreshka-agent:building-end-to-end` |
| Cursor | `/building-end-to-end` |
| Antigravity | `/` → `building-end-to-end` |
| Codex | `$matreshka-agent:building-end-to-end`, `/skills`, optional `/prompts:matreshka-build` |

Пользовательские режимы:

- `interview` — сначала подробно опросить по продукту;
- `assisted` — задавать только важные вопросы (default);
- `full-auto` — самостоятельно принимать безопасные обратимые локальные решения.

Сценарии проекта:

- `NEW_PROJECT`;
- `CONTINUE_PROJECT`;
- `EXISTING_PROJECT`.

`FULL_AUTO` не означает полный доступ. Git/network/dependency/browser/process/port/design-doc/prototype/secrets/test-data/deploy/remote остаются отдельными permissions.

## Workflow 0.5

```text
SOURCE_BRIEF
→ U-REQUIREMENTS + S-SECURITY
→ G1
→ PROJECT INTELLIGENCE
→ DESIGN INTELLIGENCE (если UI/UX материален)
→ SPECIFICATION
→ G2
→ PLAN + G3
   + AREA_CONTEXT_SET
   + DESIGN_CONTEXT_SET
   + IC-xx
→ RED → GREEN
→ CODE / SECURITY / DESIGN REVIEW
→ TECHNICAL / SECURITY VERIFY
→ BROWSER E2E
→ VISUAL DESIGN CHECK
→ G4 BLIND ACCEPTANCE
→ DESIGN DRIFT GATE
→ DOCUMENTATION DRIFT GATE
→ FINISH / HANDOFF
```

## Source Intent: G1–G4

- `SOURCE_BRIEF` хранит исходный запрос отдельно от последующей интерпретации;
- `U-xx` — пользовательские outcomes;
- `S-xx` — Security by Design controls.

Gates:

- **G1** — честная полнота уточнений;
- **G2** — fresh brief→spec coverage;
- **G3** — requirement↔task↔evidence в обе стороны;
- **G4** — blind acceptance против фактического продукта.

G4 не читает spec/manifest/plan/reports/Project Intelligence/`DESIGN.md`/design reports/dashboard.

## Project Intelligence Layer

```text
P1 PROJECT_TOPOLOGY
P2 AREA_CONTEXT_SET
P3 CROSS_AREA_INTERFACE_CONTRACT (IC-xx)
P4 RUNTIME_MAP
P5 DOCUMENTATION_DRIFT_GATE
P6 SPECIALIST_ROLE_ROUTING
```

Project Intelligence отвечает, **из каких областей состоит проект и кто чем владеет**.

- frontend/backend не выдумываются автоматически;
- каждый task получает узкий area-context;
- producer/consumer используют один frozen `IC-xx`;
- runtime observation отделён от start/stop/kill permission;
- docs обновляются только при реальном verified drift;
- specialists не увеличивают agent budget автоматически.

## Design Intelligence Layer

Design Intelligence отвечает, **как пользовательский продукт должен ощущаться, выглядеть и оставаться цельным**.

### D1 — Design relevance & recon

Controller определяет:

```text
DESIGN_NOT_APPLICABLE
DESIGN_CURRENT
DESIGN_RECON_REQUIRED
DESIGN_DIRECTION_REQUIRED
DESIGN_BLOCKED
```

Существующий UI/токены/components/screens сначала исследуются read-only. `EXISTING_PROJECT` не получает произвольный редизайн.

### D2 — Design direction / prototype exploration

Если пользователь сам не понимает, чего хочет, Matreshka может сделать 3 реально разных направления (maximum 5), различающихся layout/density/personality/hierarchy/motion/interaction model.

Прототипы изолированы от production до выбора. Fake divergence типа «три одинаковых экрана разных цветов» не принимается.

### D3 — единый root `DESIGN.md`

Материальный UI-проект использует один:

```text
DESIGN.md
```

Если файл отсутствует и exact design-doc write разрешён — Matreshka создаёт его. Иначе возвращает `DESIGN_READY_TO_SAVE` и не притворяется, что контракт существует.

Контракт содержит personality, UX principles, app shell/layout, spacing/density, typography, colors/surfaces/depth/radii, components/primitives/states, responsive/touch, accessibility, motion, approved direction, invariants и history of material design decisions.

### Apple-inspired design core

В ядро дизайна входят как обязательная reasoning vocabulary:

```text
Purpose
Agency
Responsibility
Familiarity
Flexibility
Simplicity
Craft
Delight
```

Плюс wayfinding, feedback, grouping/mapping, direct manipulation, spatial consistency, typography hierarchy, touch/focus/contrast/reduced motion/accessibility.

Это **не Apple visual preset**. Matreshka не добавляет iOS/glass стиль без продуктовой причины.

### D4 — DESIGN_CONTEXT_SET

UI task получает current design identity/hash и только нужные разделы design contract. Backend-only task не получает UI design context без реальной UX-зависимости.

### D5 — existing-first primitive policy

1. existing design system/component library;
2. existing compatible shared component;
3. repository-approved accessible primitive;
4. hand-roll только при реальной необходимости.

Новая UI/motion dependency всё равно требует dependency/network authority.

### D6 — independent Design Review

Проверяет UX flow/wayfinding, hierarchy, layout/spacing/density, typography, color/contrast/depth, component consistency/states, responsive/touch, accessibility, motion/perceived performance, cross-screen consistency и compliance с frozen `DESIGN.md`.

`DESIGN_REVIEWER` read-only и не добавляется автоматически при каждой задаче; balanced может использовать combined reviewer.

### D7 — Visual Design Check

При доступном безопасном browser/native visual tooling проверяет реальные экраны/состояния/viewports против design identity.

```text
DESIGN_VERIFICATION:
PASS | PARTIAL | FAIL | BLOCKED | UNCHECKABLE
```

Visual Design Check ≠ Browser E2E ≠ G4.

### D8 — Design Drift Gate

Перед чистым finish:

```text
DESIGN_NOT_APPLICABLE
DESIGN_CURRENT
DESIGN_UPDATE_REQUIRED
DESIGN_DRIFT
DESIGN_CONFLICT
DESIGN_BLOCKED
```

Legitimate contract change → `DESIGN_CHANGED` + controller reconciliation + refreshed design identity.

Random new radius/color/component/layout on one screen → `DESIGN_DRIFT`, а не автоматическое изменение `DESIGN.md`.

## Specialist roles

Project + Design Intelligence могут маршрутизировать:

```text
GENERAL_IMPLEMENTER
FRONTEND_IMPLEMENTER
BACKEND_IMPLEMENTER
DATA_MIGRATION_IMPLEMENTER
UI_SPECIALIST
DESIGN_ENGINEER
DESIGN_REVIEWER
TEST_E2E_SPECIALIST
DOCUMENTATION_MAINTAINER
BROWSER_CHECKER
REMOTE_OPERATOR
FILE_TRANSFER_OPERATOR
```

`DESIGN_ENGINEER` использует bundled `designing-product-experience`; `DESIGN_REVIEWER` остаётся read-only. Roles не дают новые permissions и не увеличивают execution-profile budget автоматически.

## Browser/E2E

Для web сначала используется repository-native E2E. Не устанавливать Playwright поверх существующего Cypress/Selenium/WebdriverIO без причины/permission.

Отдельно:

1. Automated Browser E2E — техническое доказательство;
2. Visual Design Check — дизайн-согласованность;
3. Browser G4 — blind user-intent acceptance.

Personal browser profile/ambient cookies/session не считаются безопасным test context. Destructive E2E требует exact disposable/approved environment proof.

## Dashboard, время и токены

При разрешённом run-state:

```text
.matreshka/runs/<run-id>/dashboard.html
.matreshka/runs/<run-id>/dashboard-state.js
```

Русский dashboard показывает:

- progress/brief coverage/stages/tasks;
- tests/security;
- Project Topology / IC / Runtime / docs;
- `DESIGN.md`, design identity, direction, prototypes, design review, visual check, Design Drift Gate;
- Browser E2E/G4;
- permissions;
- exact/partial timing;
- token telemetry только из host counters (`EXACT | PARTIAL | UNAVAILABLE`).

Dashboard — projection, не authority/evidence.

## Одиннадцать bundled skills

| Skill | Назначение |
| --- | --- |
| `building-end-to-end` | end-to-end entry для new/continue/existing project |
| `orchestrating-subagent-work` | controller, permissions, recovery, Project + Design Intelligence |
| `designing-product-experience` | UX/UI recon, prototypes, Apple-inspired core, `DESIGN.md` |
| `specifying-software-work` | security-by-design specification |
| `planning-software-work` | U/S, area/design contexts, interfaces, plan |
| `writing-portable-agent-prompt` | portable prompt |
| `implementing-with-tests` | scoped RED→GREEN |
| `debugging-systematically` | root-cause debugging |
| `reviewing-agent-work` | code/security/interface/design review |
| `verifying-development-work` | technical/security/E2E/visual/G4 evidence |
| `finishing-development-work` | Design/Docs Drift + authorized Git/remote/handoff |

Design skill explicit calls:

| Platform | Design skill |
| --- | --- |
| Claude Code | `/matreshka-agent:designing-product-experience` |
| Cursor/Antigravity | registered `designing-product-experience` skill |
| Codex | `$matreshka-agent:designing-product-experience`, `/skills`, optional `/prompts:matreshka-design` |

## Budgets and independence

- balanced: обычно максимум 2 main roles / 4 started turns;
- maximum quality: до 3 main roles / 6 turns;
- one consolidated fixer wave;
- same-thread fixer/re-review when host supports resume;
- one writer per checkout;
- parallel by default only for independent read-only work;
- specialist/design routing does not inflate budget automatically.

## Проверка 0.5 development package

Из корня репозитория:

```bash
python3 -B plugins/matreshka-agent/scripts/validate_dev_05.py \
  plugins/matreshka-agent --marketplace-root . --self-test

python3 -B plugins/matreshka-agent/scripts/check_dev_05.py \
  plugins/matreshka-agent --marketplace-root .

python3 -B plugins/matreshka-agent/scripts/doctor_dev_05.py \
  plugins/matreshka-agent --marketplace-root .
```

- `validate_dev_05.py` переиспользует строгий release-line validator, но расширяет development package inventory до 11 skills и design wrapper;
- `check_dev_05.py` проверяет 0.5 cross-component wiring, включая Project/Design Intelligence и eval coverage;
- `doctor_dev_05.py` выполняет development-aware read-only diagnostics.

GitHub Actions запускает development validation на Python 3.11.

## Что не появляется автоматически

- Pi `.pi/mcp.json`/обязательный MCP;
- hooks/telemetry;
- dependency/browser installation;
- secret access;
- Git/push/deploy authority;
- process/port/data reset;
- `DESIGN.md`/prototype writes без explicit permission;
- personal browser profile;
- автоматическая глобальная память/самоизменение Matreshka.

## До release 0.5.0

Нужно получить deterministic final-head validation и disposable native full-stack acceptance, который одновременно проверит Project Intelligence, Design Intelligence, Browser E2E, Visual Design Check, G4, Design/Docs Drift, русский dashboard и recovery. Затем — native evidence по заявляемым hosts, version bump и publisher/security metadata.

До этого development branch не должна называться released `0.5.0`.
