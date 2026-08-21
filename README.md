# Matreshka Agent

Matreshka Agent — переносимый permission-aware workflow для разработки с coding agents. Он превращает обычный запрос пользователя в трассируемую разработку: исходный замысел → спецификация → архитектурная и дизайн-карта проекта → план → RED→GREEN реализация → независимые review → техническая/браузерная/визуальная проверка → blind acceptance → честный handoff.

> **Текущий статус:** `0.5 development track` в ветке `dev/0.5-brief-traceability-observability`. Versioned plugin manifests намеренно остаются `0.4.0` до native/release gates. Это development snapshot, не опубликованный `0.5.0`.

Подробная package-документация: [`plugins/matreshka-agent/README.md`](plugins/matreshka-agent/README.md).

## Одна точка входа

Для проекта целиком:

```text
$matreshka-agent:building-end-to-end
```

### Пользовательские режимы

```text
interview   — сначала подробно опросить по продукту
assisted    — задавать только важные вопросы (по умолчанию)
full-auto   — самостоятельно принимать безопасные обратимые локальные решения
```

### Сценарии проекта

```text
NEW_PROJECT       — новый проект
CONTINUE_PROJECT  — продолжить проект, который уже вела Matreshka
EXISTING_PROJECT  — подключить Matreshka к существующему проекту
```

`FULL_AUTO` влияет на количество вопросов и делегированные обратимые решения, **но не даёт полномочий**. Git, network, dependency/browser install, secrets, process/port, design-doc/prototype writes, test-data mutation, deploy и remote actions остаются отдельными permissions.

## Workflow 0.5

```text
SOURCE_BRIEF
   ↓
U-REQUIREMENTS + S-SECURITY
   ↓
G1
   ↓
PROJECT INTELLIGENCE
   ↓
DESIGN INTELLIGENCE (если UI/UX материален)
   ↓
SPECIFICATION
   ↓
G2 independent brief → spec
   ↓
PLAN + G3
   ├── AREA_CONTEXT_SET
   ├── DESIGN_CONTEXT_SET
   └── IC-xx
   ↓
RED → GREEN
   ↓
CODE / SECURITY / DESIGN REVIEW
   ↓
TECHNICAL / SECURITY VERIFY
   ↓
BROWSER E2E (если применимо)
   ↓
VISUAL DESIGN CHECK (если применимо)
   ↓
G4 BLIND ACCEPTANCE
   ↓
DESIGN DRIFT GATE
   ↓
DOCUMENTATION DRIFT GATE
   ↓
FINISH / HANDOFF
```

## Source Intent Traceability

- исходный `SOURCE_BRIEF` сохраняется отдельно от последующих интерпретаций;
- пользовательские outcomes получают `U-01`, `U-02`, ...;
- Security by Design остаётся отдельным `S-01`, `S-02`, ...;
- **G1** проверяет полноту уточнений;
- **G2** свежим контекстом сверяет brief со specification;
- **G3** проверяет `requirement ↔ task ↔ evidence` в обе стороны;
- **G4** независимо проверяет фактический продукт по исходному brief и не читает spec/plan/reports/dashboard/Design Intelligence.

Материальный `PARTIAL`, `MISSING` или acceptance-critical `UNCHECKABLE` блокирует `COMPLETE`.

## Project Intelligence Layer

Matreshka сначала выясняет фактическую структуру проекта, а не предполагает, что любой сайт автоматически имеет отдельные frontend/backend.

```text
P1 PROJECT_TOPOLOGY
P2 AREA_CONTEXT_SET
P3 CROSS-AREA IC-xx CONTRACTS
P4 RUNTIME_MAP
P5 DOCUMENTATION_DRIFT_GATE
P6 SPECIALIST_ROLE_ROUTING
```

Например full-stack проект может иметь:

```text
AREA-FRONTEND
AREA-BACKEND
AREA-DATA
AREA-E2E
```

а CLI:

```text
AREA-CLI
AREA-PERSISTENCE
```

Cross-area producer/consumer seam фиксируется одним `IC-xx`; Runtime Map отделяет observation от start/stop/kill authority; task получает только свой area-context; specialist routing не создаёт по одному агенту на каждую область.

## Design Intelligence Layer

Для пользовательских интерфейсов дизайн теперь является частью ядра разработки, а не косметическим этапом после кода.

### Один долговременный `DESIGN.md`

Материальный UI-проект использует единый root:

```text
DESIGN.md
```

Если его нет, Matreshka сначала восстанавливает/выбирает дизайн-направление и создаёт контракт при наличии точного design-doc permission. Без права записи она возвращает `DESIGN_READY_TO_SAVE`, а не делает вид, что контракт сохранён.

`DESIGN.md` фиксирует:

- product personality и желаемое ощущение;
- UX principles / primary tasks / wayfinding;
- app shell, layout, spacing/density;
- typography;
- colors/surfaces/radii/depth;
- components/primitives/states;
- responsive/mobile/touch rules;
- accessibility;
- motion system;
- выбранное дизайн-направление;
- `ALWAYS` / `NEVER` invariants;
- историю материальных дизайн-решений.

UI-задачи получают design identity/hash и узкий `DESIGN_CONTEXT_SET`. Если следующий экран случайно вводит другие radius/color/spacing/component patterns, это `DESIGN_DRIFT`, а не «творческое решение».

### Когда пользователь сам не знает, чего хочет

Matreshka может использовать изолированное prototype exploration: обычно 3 реально разных направления, максимум 5. Варианты должны различаться layout/density/personality/hierarchy/motion/interaction model, а не только цветом. Production-код не меняется до выбора/валидного auto-decision.

### Apple-inspired design core

Apple-концепция входит в **ядро дизайн-мышления**, но не является визуальным preset «сделай как Apple».

Обязательные принципы:

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

Плюс wayfinding, feedback, grouping/mapping, direct manipulation, spatial consistency, typography hierarchy, focus/contrast/touch targets/reduced motion/accessibility и осмысленная motion-система.

Matreshka не добавляет glassmorphism/iOS-стиль автоматически: визуальный язык определяется самим продуктом и его `DESIGN.md`.

Отдельный design skill можно вызвать напрямую:

```text
$matreshka-agent:designing-product-experience
```

## Browser E2E + Browser G4

Matreshka сначала использует существующую repository-native E2E инфраструктуру: Playwright/Cypress/Selenium/WebdriverIO или другой подтверждённый seam. Новый framework не устанавливается без отдельного permission.

```text
Automated Browser E2E
≠
Visual Design Check
≠
Browser G4
```

- **E2E** доказывает технические сценарии;
- **Visual Design Check** проверяет фактические UI states/viewports против `DESIGN.md`;
- **G4** слепо проверяет исходный запрос пользователя и специально не читает дизайн-контракт/дизайн-отчёты.

Personal Chrome profile, ambient cookies/session и неизвестные destructive DB setup не считаются безопасным test context.

## Русский dashboard, время и токены

При разрешённом run-state:

```text
.matreshka/runs/<run-id>/dashboard.html
.matreshka/runs/<run-id>/dashboard-state.js
```

Dashboard показывает по-русски:

- общий прогресс и brief coverage;
- этапы/задачи/tests/security;
- Project Topology / interfaces / Runtime / docs;
- `DESIGN.md`, design identity/direction/prototype/design review/visual check/Design Drift Gate;
- Browser/E2E и G4;
- permissions;
- wall-clock / implementation time при точных timestamps;
- token usage только из реальных host counters.

Если точного token counter нет — `Недоступно`; Matreshka не выдумывает оценку по символам/времени.

Dashboard — projection, не permission и не доказательство completion.

## Одиннадцать bundled skills

| Skill | Назначение |
| --- | --- |
| `building-end-to-end` | plain-language end-to-end entry |
| `orchestrating-subagent-work` | controller, permissions, recovery, Project + Design Intelligence |
| `designing-product-experience` | UX/UI recon, prototypes, Apple-inspired core, `DESIGN.md` |
| `specifying-software-work` | security-by-design specification |
| `planning-software-work` | U/S, area/design contexts, IC contracts, executable plan |
| `writing-portable-agent-prompt` | переносимый prompt |
| `implementing-with-tests` | scoped RED→GREEN implementation |
| `debugging-systematically` | root-cause debugging |
| `reviewing-agent-work` | independent code/security/interface/design review |
| `verifying-development-work` | technical/security/E2E/visual/G4 evidence |
| `finishing-development-work` | design/docs drift + разрешённый Git/remote/handoff |

## Профили выполнения

- **maximum speed** — маленькая low-risk механика;
- **balanced** — рекомендуется большинству задач;
- **maximum quality** — auth/isolation/migrations/secrets/persistence/production/design-critical boundaries.

Specialist roles (`FRONTEND_IMPLEMENTER`, `DESIGN_ENGINEER`, `DESIGN_REVIEWER` и др.) не увеличивают agent budget автоматически. Один writer на checkout; только одна consolidated fixer wave.

## Проверка development-пакета

Из корня репозитория:

```bash
python3 -B plugins/matreshka-agent/scripts/validate_dev_05.py \
  plugins/matreshka-agent --marketplace-root . --self-test

python3 -B plugins/matreshka-agent/scripts/check_dev_05.py \
  plugins/matreshka-agent --marketplace-root .

python3 -B plugins/matreshka-agent/scripts/doctor_dev_05.py \
  plugins/matreshka-agent --marketplace-root .
```

GitHub Actions запускает эти проверки на Python 3.11 для `main`, `dev/**` и pull requests.

- `validate_dev_05.py` переиспользует строгий 0.4 validator core, расширяя development inventory до 11 skills/11 optional Codex wrappers;
- `check_dev_05.py` проверяет cross-component wiring 0.5: launch/source/G1-G4, Browser, Project Intelligence, Design Intelligence, dashboard и eval coverage;
- `doctor_dev_05.py` использует read-only doctor с development inventory.

## Что Matreshka не получает автоматически

- Pi `.pi/mcp.json` или обязательный MCP;
- hooks/telemetry;
- dependency/browser installation;
- secrets;
- Git/push/deploy/production authority;
- process/port/data reset authority;
- `DESIGN.md`/prototype writes без разрешения;
- использование личного browser profile;
- автоматическую глобальную память/самоизменение skills.

## Перед выпуском 0.5.0

Нужно получить:

1. final-development-HEAD deterministic validation PASS;
2. disposable native full-stack acceptance для Project Intelligence + Design Intelligence + Browser/E2E/Visual/G4 + drift gates + dashboard;
3. native evidence для каждого host, который будет заявлен в release;
4. затем version bump manifests/marketplaces/validators/evals до `0.5.0` и финальная publisher/security metadata проверка.

До этого ветка остаётся `0.5 development preview`.
