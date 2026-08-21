# Matreshka Agent

Matreshka Agent — переносимый permission-aware workflow для разработки с coding agents. Он превращает обычный запрос пользователя в трассируемую разработку: исходный замысел → Project/Design Intelligence → спецификация → план → RED→GREEN → независимые review → техническая/браузерная/визуальная проверка → blind acceptance → drift gates → честный handoff.

> **Текущий статус:** `0.5 development track` в ветке `dev/0.5-brief-traceability-observability`. Versioned plugin manifests намеренно остаются `0.4.0` до native/release gates. Это development snapshot, не опубликованный `0.5.0`.

Подробная документация пакета: [`plugins/matreshka-agent/README.md`](plugins/matreshka-agent/README.md).

## Одна точка входа

```text
$matreshka-agent:building-end-to-end
```

Режимы:

```text
interview   — сначала подробно опросить по продукту
assisted    — задавать только важные вопросы (по умолчанию)
full-auto   — самостоятельно принимать безопасные обратимые локальные решения
```

Сценарии: `NEW_PROJECT`, `CONTINUE_PROJECT`, `EXISTING_PROJECT`.

`FULL_AUTO` не даёт дополнительных полномочий: Git, network, dependencies/browser, process/port, `DESIGN.md`/prototype writes, secrets, destructive setup, deploy и remote actions остаются отдельными permissions.

## Workflow 0.5

```text
SOURCE_BRIEF + U-/S-
↓ G1
PROJECT INTELLIGENCE
↓
DESIGN INTELLIGENCE (если UI/UX материален)
↓
SPECIFICATION
↓ G2
PLAN + G3
  ├─ AREA_CONTEXT_SET
  ├─ DESIGN_CONTEXT_SET
  └─ frozen IC-xx
↓
RED → GREEN
↓
CODE / SECURITY / DESIGN REVIEW
↓
TECHNICAL / SECURITY VERIFY
↓
BROWSER E2E
↓
VISUAL DESIGN CHECK
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

- исходный `SOURCE_BRIEF` сохраняется отдельно от последующей интерпретации;
- `U-xx` — пользовательские outcomes;
- `S-xx` — Security by Design controls;
- G1 — полнота уточнений;
- G2 — fresh brief→spec coverage;
- G3 — requirement↔task↔evidence;
- G4 — blind acceptance по фактическому продукту.

Материальный `PARTIAL`, `MISSING` или acceptance-critical `UNCHECKABLE` блокирует `COMPLETE`.

## Project Intelligence Layer

```text
P1 PROJECT_TOPOLOGY
P2 AREA_CONTEXT_SET
P3 CROSS-AREA IC-xx CONTRACTS
P4 RUNTIME_MAP
P5 DOCUMENTATION_DRIFT_GATE
P6 SPECIALIST_ROLE_ROUTING
```

Matreshka не предполагает frontend/backend только потому, что проект — сайт. Она строит фактическую topology, даёт task только нужный area-context, фиксирует один `IC-xx` на producer/consumer seam и отделяет runtime observation от process authority.

## Design Intelligence Layer

Для UI-проектов дизайн — часть ядра разработки, а не polish после кода.

### Единый `DESIGN.md`

Материальный UI-проект использует один root `DESIGN.md`. Он фиксирует personality, UX principles, app shell/layout, spacing/density, typography, colors/surfaces/depth/radii, components/states, responsive/touch, accessibility, motion, выбранное направление, invariants и историю материальных design decisions.

Если файла нет и точный design-doc write разрешён — Matreshka создаёт его. Без разрешения возвращает `DESIGN_READY_TO_SAVE`.

UI-task получает frozen design identity/hash и только нужный `DESIGN_CONTEXT_SET`. Случайные новые radius/color/component/layout patterns → `DESIGN_DRIFT`, а не автоматическое изменение дизайн-контракта.

### Когда пользователь не знает, чего хочет

Matreshka может построить обычно 3, максимум 5 реально разных изолированных prototype directions. Они различаются layout/density/personality/hierarchy/motion/interaction model, а не только цветом. Production-код не меняется до выбора или валидного delegated decision.

### Apple-inspired design core

Apple-концепция входит в **ядро UX-мышления**, но не является визуальным preset «сделай как Apple»:

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

Плюс wayfinding, feedback, grouping/mapping, direct manipulation, spatial consistency, typography hierarchy, focus/contrast/touch targets/reduced motion/accessibility.

Matreshka не добавляет iOS/glass стиль без продуктовой причины.

Отдельный design skill:

```text
$matreshka-agent:designing-product-experience
```

## Browser E2E + Browser G4

Три разные оси доказательств:

```text
Automated Browser E2E
≠ Visual Design Check
≠ Browser G4
```

- E2E доказывает технические browser scenarios;
- Visual Design Check сравнивает реальные states/viewports с frozen design identity;
- G4 слепо проверяет исходный запрос и не читает `DESIGN.md`, prototypes, design-review/visual reports, spec/plan/dashboard.

Existing repository E2E используется первым. Personal Chrome profile/ambient session и неизвестный destructive test environment запрещены как автоматический test context.

## Русский dashboard

При разрешённом run-state:

```text
.matreshka/runs/<run-id>/dashboard.html
.matreshka/runs/<run-id>/dashboard-state.js
```

Dashboard показывает progress, Project/Design Intelligence, tests/security, E2E/G4, permissions, время и truthful token telemetry. Если host не отдаёт точный token counter — `Недоступно`. Dashboard — projection, не authority/evidence.

## Одиннадцать bundled skills

| Skill | Назначение |
| --- | --- |
| `building-end-to-end` | end-to-end entry |
| `orchestrating-subagent-work` | controller, permissions, recovery, Project + Design Intelligence |
| `designing-product-experience` | UX/UI recon, prototypes, Apple-inspired core, `DESIGN.md` |
| `specifying-software-work` | security-by-design specification + frozen design reference |
| `planning-software-work` | U/S, area/design contexts, IC contracts, plan |
| `writing-portable-agent-prompt` | portable prompt |
| `implementing-with-tests` | scoped RED→GREEN with area/IC/design boundaries |
| `debugging-systematically` | root-cause debugging |
| `reviewing-agent-work` | code/security/interface/design review |
| `verifying-development-work` | technical/security/E2E/visual/G4 evidence |
| `finishing-development-work` | Design/Docs Drift + authorized Git/remote/handoff |

Specialist roles, включая `DESIGN_ENGINEER`/`DESIGN_REVIEWER`, не увеличивают budget автоматически. Balanced использует combined reviewer; maximum-quality имеет максимум два reviewer slots после implementer.

## Проверка 0.5 development track

Из корня репозитория запускается тот же четырёхслойный набор, что и CI:

```bash
python3 -B plugins/matreshka-agent/scripts/validate_dev_05.py \
  plugins/matreshka-agent --marketplace-root . --self-test

python3 -B plugins/matreshka-agent/scripts/check_dev_05.py \
  plugins/matreshka-agent --marketplace-root .

python3 -B plugins/matreshka-agent/scripts/check_dev_05_behavioral_contracts.py \
  plugins/matreshka-agent --marketplace-root .

python3 -B plugins/matreshka-agent/scripts/doctor_dev_05.py \
  plugins/matreshka-agent --marketplace-root .
```

- `validate_dev_05.py` расширяет строгий release-line validator до 11 skills/11 Codex wrappers;
- `check_dev_05.py` проверяет сквозное статическое wiring Build→Controller→Design→Spec→Plan→Implement→Review→Verify→Finish/Recovery/Dashboard;
- `check_dev_05_behavioral_contracts.py` проверяет обязательные cross-skill design evals и budget/CI linkage;
- `doctor_dev_05.py` выполняет development-aware read-only diagnostics.

## До release 0.5.0

Нужно получить:

1. final-development-HEAD deterministic validation/CI PASS;
2. disposable native full-stack acceptance для Project Intelligence + Design Intelligence + Browser E2E + Visual Design Check + G4 + Design/Docs Drift + dashboard/recovery;
3. native evidence для каждого host, который будет заявлен в release;
4. затем version bump manifests/marketplaces/validators/evals до `0.5.0` и финальная publisher/security metadata проверка.

До этого ветка остаётся `0.5 development preview`.
