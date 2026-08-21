# Matreshka Agent

Matreshka Agent — переносимый permission-aware набор из **Одиннадцати bundled skills** для coding agents. Он объединяет source-intent traceability, Project Intelligence, Design Intelligence, Security by Design, планирование, test-first implementation, независимые review/verification, Browser E2E, Visual Design Check, G4 blind acceptance и безопасный finish/handoff.

> **Статус:** `0.5 development track` на `dev/0.5-brief-traceability-observability`. Versioned manifests пока намеренно `0.4.0`; это development snapshot, а не release `0.5.0`.

## Запуск проекта целиком

```text
$matreshka-agent:building-end-to-end
```

Режимы: `interview`, `assisted` (default), `full-auto`.

Сценарии: `NEW_PROJECT`, `CONTINUE_PROJECT`, `EXISTING_PROJECT`.

`FULL_AUTO` не расширяет permissions: Git/network/dependencies/browser/process/port/design-doc/prototype/secrets/destructive/deploy/remote остаются отдельными полномочиями.

## Workflow

```text
SOURCE_BRIEF + U-/S-
→ G1
→ PROJECT INTELLIGENCE
→ DESIGN INTELLIGENCE (если UI material)
→ SPECIFICATION
→ G2
→ PLAN + G3
   + AREA_CONTEXT_SET
   + DESIGN_CONTEXT_SET
   + frozen IC-xx
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

## Project Intelligence Layer

- P1 `PROJECT_TOPOLOGY` — фактические области проекта;
- P2 `AREA_CONTEXT_SET` — узкий task context;
- P3 frozen `IC-xx` — один producer/consumer contract;
- P4 `RUNTIME_MAP` — ownership-aware runtime evidence;
- P5 `DOCUMENTATION_DRIFT_GATE`;
- P6 specialist routing без автоматического роста agent budget.

Project Intelligence отвечает **где и чем владеет код**. Он не предполагает frontend/backend без repository evidence.

## Design Intelligence Layer

Design Intelligence отвечает **как пользовательский продукт должен ощущаться, выглядеть и сохранять цельность между экранами/агентами**.

### Design Recon + root `DESIGN.md`

Материальный UI-проект использует один root `DESIGN.md`. Контракт хранит personality, UX principles, layout/shell, spacing/density, typography, colors/surfaces/depth/radii, components/states, responsive/touch, accessibility, motion, approved direction, invariants и историю material design decisions.

Если `DESIGN.md` отсутствует:

- с exact design-doc write authority — создать после recon/direction resolution;
- без него — `DESIGN_READY_TO_SAVE`, не ложная persistence claim.

Existing UI сначала изучается; Matreshka не делает gratuitous redesign.

### Prototype exploration

Когда пользователь не понимает, чего хочет, обычно создаются 3 genuinely different isolated directions (maximum 5). Различия должны быть по layout/density/personality/hierarchy/motion/interaction model, а не только цвету. Production интеграция — только после выбора/валидного delegated decision.

### Apple-inspired design core

В обязательное UX-ядро входят:

```text
Purpose · Agency · Responsibility · Familiarity
Flexibility · Simplicity · Craft · Delight
```

Плюс wayfinding, feedback, grouping/mapping, direct manipulation, spatial consistency, typography hierarchy, focus/contrast/touch/reduced motion/accessibility.

Это **не Apple visual preset**: стекло/iOS-стиль не добавляются без продуктовой причины.

### DESIGN_CONTEXT_SET и drift

UI task получает frozen design identity/hash и минимальный `DESIGN_CONTEXT_SET`. Backend-only task не получает лишний UI context.

Legitimate design change → `DESIGN_CHANGED` + controller reconciliation + новый identity.

Случайное отклонение implementation → `DESIGN_DRIFT`; clean completion запрещён.

### Design review / visual verification

- combined reviewer в balanced проверяет применимые design dimensions;
- maximum-quality всё равно имеет максимум два reviewer slots после implementer; `DESIGN_REVIEWER` занимает один существующий slot, а не добавляет четвёртого агента;
- `VISUAL_DESIGN_CHECK` read-only проверяет реальные states/viewports против frozen design identity;
- material visual property без render evidence → `UNCHECKABLE`, не выдуманный PASS.

## Browser evidence axes

```text
Browser E2E ≠ Visual Design Check ≠ Browser G4
```

Existing repository E2E first. Personal browser profile/ambient session запрещён. Destructive E2E требует exact disposable/approved environment proof.

G4 получает source brief + actual product + разрешённые observations и специально не читает spec/manifest/plan/Project Intelligence/`DESIGN.md`/prototypes/design reports/dashboard.

## Одиннадцать bundled skills

| Skill | Назначение |
| --- | --- |
| `building-end-to-end` | turnkey entry |
| `orchestrating-subagent-work` | controller, permissions, recovery, Project + Design Intelligence |
| `designing-product-experience` | UX/UI recon, prototypes, Apple-inspired core, `DESIGN.md` |
| `specifying-software-work` | security-by-design spec + frozen design reference |
| `planning-software-work` | U/S, area/design context, IC, plan |
| `writing-portable-agent-prompt` | portable prompt |
| `implementing-with-tests` | RED→GREEN with area/IC/design boundaries |
| `debugging-systematically` | root cause |
| `reviewing-agent-work` | independent code/security/interface/design review |
| `verifying-development-work` | technical/security/E2E/visual/G4 evidence |
| `finishing-development-work` | design/docs drift + authorized Git/remote/handoff |

Прямой design-вызов:

```text
$matreshka-agent:designing-product-experience
```

Optional Codex wrapper: `/prompts:matreshka-design` после копирования файлов из `codex-prompts/` в `~/.codex/prompts/`.

## Dashboard и observability

При разрешённом run-state dashboard показывает по-русски progress, Project/Design Intelligence, E2E/G4, permissions, timing и truthful token counters. Dashboard — projection и не может дать permission/COMPLETE.

## Development validation

Из корня marketplace запускайте **все четыре** проверки:

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

`validate_dev_05.py` переиспользует proven 0.4 package validator core, но расширяет development inventory до 11 skills/11 Codex wrappers.

`check_dev_05.py` проверяет static cross-component wiring: Build→Controller→Design→Spec→Plan→Implement→Review→Verify→Finish/Recovery/Dashboard.

`check_dev_05_behavioral_contracts.py` проверяет cross-skill design evals, reviewer-budget rules и то, что CI действительно запускает behavioral contract gate.

`doctor_dev_05.py` — read-only/offline diagnostics с development inventory.

CI запускает ту же четырёхслойную последовательность на Python 3.11.

## До release 0.5.0

Static validation не равна native behavior proof. До release нужны:

1. observable final-HEAD deterministic/CI PASS;
2. disposable native full-stack acceptance для Project + Design Intelligence, IC/contexts, Browser E2E, Design Review, Visual Design Check, G4, Design/Docs Drift, dashboard/recovery;
3. native evidence для каждого заявляемого host;
4. затем version bump и publisher/security metadata.
