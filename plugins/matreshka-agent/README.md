# Matreshka Agent

Matreshka Agent — переносимый permission-aware набор из **одиннадцати bundled skills** для coding agents. Он объединяет source-intent traceability, Project Intelligence, Design Intelligence, Security by Design, планирование, test-first implementation, независимые review/verification, Browser E2E, Visual Design Check, G4 blind acceptance и безопасный finish/handoff.

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
→ SPECIFICATION + SECURITY HARDENING ROUTING
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

## Security by Design: пять automatic hardening families

Matreshka не ждёт, пока пользователь сам назовёт rate limiting, RLS, race condition или API budget. Для каждой specification автоматически оцениваются пять stable family labels. Каждый family status должен быть `REQUIRED`, `N/A(reason)` или `HANDOFF`; `REQUIRED` превращается в нормальные `S-xx` requirements с owner + negative proof.

### `S-AUTH-HARDENING`

Trigger: password login/recovery, privileged/admin accounts.

Проверяется: authoritative server-side abuse control по source/network + target account, non-enumerating auth/recovery errors, application-owned password policy (default minimum 12 characters unless stronger existing/provider policy), privileged MFA/step-up where applicable, safe session/recovery behavior.

### `S-FILE-EXECUTION`

Trigger: stored user/integration uploads.

Проверяется: trusted-boundary content/type/size, generated opaque storage key, path ownership, storage outside executable code roots or equivalent non-execution boundary, safe serving headers/disposition, representative spoofed/active-content/path negative proof.

### `S-ATOMIC-EFFECT`

Trigger: balance/credits/promo/inventory/withdrawal/one-time entitlement/payment effects where concurrency/replay can multiply value.

Проверяется datastore-appropriate atomicity: transaction/lock/CAS/unique operation/idempotency or equivalent. Sequential green test недостаточен — нужен concurrent/replay proof.

### `S-BAAS-AUTHZ`

Trigger: browser/mobile client directly addresses Supabase/Firebase/Appwrite/equivalent data/storage.

Проверяется provider-side deny-by-default authorization for every touched browser-accessible table/collection/bucket; Supabase RLS/policy inventory or provider-equivalent rules; service-role credentials server-only; unauthenticated + wrong-user/cross-tenant read/write negative proofs. Public anon/client key сам по себе не считается секретом, если provider architecture предполагает его публичность.

### `S-PAID-API-BUDGET`

Trigger: metered LLM/image/audio/SMS/voice/email/search/etc. request caused by a user.

Проверяется per-user/relevant tenant quota, global fail-closed usage/spend ceiling or equivalent circuit breaker, authoritative server-side attribution, concurrency-safe reservation/accounting, safe exhausted-budget response and monitoring. Exact money не выдумывается, если доступны только provider usage units.

Функциональные тесты не заменяют эти negative proofs. Independent review проверяет выбранный family at authoritative boundary; fresh verifier не может вернуть clean `VERIFIED`, пока required security row не доказан.

Behavioral matrix: `evals/security-hardening-evals.json`. Static/CI gate: `scripts/check_security_hardening.py`.

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

Материальный UI-проект использует один root `DESIGN.md`. Контракт хранит personality, UX principles, layout/shell, spacing/density, typography, colors/surfaces/depth/radii, components/states, responsive/touch, accessibility, motion, approved direction, invariants и material design decisions.

Если `DESIGN.md` отсутствует:

- с exact design-doc write authority — создать после recon/direction resolution;
- без него — `DESIGN_READY_TO_SAVE`, не ложная persistence claim.

Existing UI сначала изучается; Matreshka не делает gratuitous redesign.

Когда пользователь не понимает, чего хочет, обычно создаются 3 genuinely different isolated directions (maximum 5). Различия — layout/density/personality/hierarchy/motion/interaction model, а не только цвет. Production интеграция — только после выбора/валидного delegated decision.

### Apple-inspired design core

Обязательное UX-ядро:

```text
Purpose · Agency · Responsibility · Familiarity
Flexibility · Simplicity · Craft · Delight
```

Плюс wayfinding, feedback, grouping/mapping, direct manipulation, spatial consistency, typography hierarchy, focus/contrast/touch/reduced motion/accessibility.

Это **не Apple visual preset**: стекло/iOS-стиль не добавляются без продуктовой причины.

UI task получает frozen design identity/hash и минимальный `DESIGN_CONTEXT_SET`. Legitimate design change → `DESIGN_CHANGED`; случайное отклонение → `DESIGN_DRIFT`.

Design Review и `VISUAL_DESIGN_CHECK` остаются отдельными от technical correctness и G4. `DESIGN_REVIEWER` занимает существующий reviewer slot, не создаёт четвёртого агента.

## Browser evidence axes

```text
Browser E2E ≠ Visual Design Check ≠ Browser G4
```

Existing repository E2E first. Personal browser profile/ambient session запрещён. Destructive E2E требует exact disposable/approved environment proof.

G4 получает source brief + actual product + разрешённые observations и не читает spec/manifest/plan/Project Intelligence/`DESIGN.md`/prototypes/design reports/dashboard.

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

## Dashboard / run-state hardening

Dashboard — projection и не может дать permission/COMPLETE. После сравнения с ошибками Autopilot v1.0.1+ добавлены отдельные механические guardrails:

- `dashboard.html` carries an embedded last-known-good snapshot and survives missing sibling state;
- `scripts/sync_run_state.py` validates state, preserves the previous snapshot on failure and atomically refreshes the projection without server/PID/port/process logic;
- explicit `stageOrder` + `stateIntegrity` catch duplicate/conflicting active stages and transition-timestamp contradictions;
- helper may derive only mechanically provable timestamps for stages already semantically terminal — it never turns chronology into PASS;
- render errors do not permanently stop polling;
- no dashboard mechanism grants browser/server/network/process authority.

## Context-cost and repeatability guardrails

`evals/context-budget.json` defines exact UTF-8 byte ceilings for `build-entry-core`, `controller-preflight-core`, and `ui-design-increment`. `check_context_budget.py` fails on budget regression. It **never** estimates runtime tokens; runtime token telemetry stays host-reported `EXACT | PARTIAL | UNAVAILABLE`.

`evals/native-repeatability.json` defines six blocking behavior properties with 5 repetitions each per release-claimed host. `evaluate_native_repeatability.py` requires all required repetitions to PASS when native results are evaluated. CI validates the matrix shape only; it does not fabricate native evidence.

## Development validation

Из корня marketplace запускайте весь CI-equivalent набор:

```bash
python3 -B plugins/matreshka-agent/scripts/validate_dev_05.py \
  plugins/matreshka-agent --marketplace-root . --self-test

python3 -B plugins/matreshka-agent/scripts/check_dev_05.py \
  plugins/matreshka-agent --marketplace-root .

python3 -B plugins/matreshka-agent/scripts/check_dev_05_behavioral_contracts.py \
  plugins/matreshka-agent

python3 -B plugins/matreshka-agent/scripts/check_security_hardening.py \
  plugins/matreshka-agent --marketplace-root .

python3 -B plugins/matreshka-agent/scripts/sync_run_state.py --self-test

python3 -B plugins/matreshka-agent/scripts/check_context_budget.py \
  plugins/matreshka-agent

python3 -B plugins/matreshka-agent/scripts/evaluate_native_repeatability.py \
  --validate-plan

python3 -B plugins/matreshka-agent/scripts/check_autopilot_regressions.py \
  plugins/matreshka-agent --marketplace-root .

python3 -B plugins/matreshka-agent/scripts/doctor_dev_05.py \
  plugins/matreshka-agent --marketplace-root .
```

`validate_dev_05.py` переиспользует proven 0.4 package validator core, но расширяет development inventory до 11 skills/11 Codex wrappers.

`check_dev_05.py` проверяет static cross-component wiring: Build→Controller→Design→Spec→Plan→Implement→Review→Verify→Finish/Recovery/Dashboard.

`check_dev_05_behavioral_contracts.py` проверяет cross-skill design evals, reviewer-budget rules и CI linkage.

`check_security_hardening.py` проверяет пять automatic security families, specification selection table, review checklist, existing S- implementation/review/verification flow, security eval matrix и CI linkage.

`check_autopilot_regressions.py` — A1–A5 regression-class gate: embedded snapshot, atomic state sync, stage invariants, context budgets и repeatability contract должны оставаться подключены к CI.

`doctor_dev_05.py` — read-only/offline diagnostics с development inventory.

## До release 0.5.0

Static validation не равна native behavior proof. До release нужны:

1. observable final-HEAD deterministic/CI PASS;
2. disposable native full-stack acceptance для Project + Design Intelligence, Security hardening, IC/contexts, Browser E2E, Design Review, Visual Design Check, G4, Design/Docs Drift, dashboard/recovery;
3. 5× repeatability evidence по blocking scenarios для каждого реально заявляемого host;
4. затем version bump и publisher/security metadata.
