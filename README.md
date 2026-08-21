# Matreshka Agent

Matreshka Agent — переносимый permission-aware workflow для разработки с coding agents. Он превращает обычный запрос пользователя в трассируемую разработку: исходный замысел → Project/Design Intelligence → specification → plan → RED→GREEN → independent review → technical/browser/visual verification → blind acceptance → drift gates → честный handoff.

> **Текущий статус:** `0.5 development track` в ветке `dev/0.5-brief-traceability-observability`. Versioned plugin manifests намеренно остаются `0.4.0` до native/release gates. Это development snapshot, не опубликованный `0.5.0`.

Подробная документация пакета: [`plugins/matreshka-agent/README.md`](plugins/matreshka-agent/README.md).

## Одна точка входа

```text
$matreshka-agent:building-end-to-end
```

Режимы: `interview`, `assisted` (default), `full-auto`.

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
SPECIFICATION + SECURITY HARDENING ROUTING
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

## Security by Design + automatic hardening

Security не ждёт, пока пользователь сам вспомнит назвать конкретную уязвимость. Во время specification Matreshka проверяет пять стабильных boundary families и для каждой фиксирует `REQUIRED`, `N/A(reason)` или `HANDOFF`. Каждая `REQUIRED` family превращается в обычные `S-xx` requirements с owner + negative proof, а затем проходит через implementation → independent review → fresh verification.

```text
S-AUTH-HARDENING
→ password / login / recovery / privileged-admin auth
→ abuse throttling по source + account, non-enumerating errors,
  password policy, privileged MFA/step-up when applicable

S-FILE-EXECUTION
→ stored uploads
→ trusted content/type checks, generated storage keys,
  non-executable storage + safe serving boundary

S-ATOMIC-EFFECT
→ balances / credits / promo / inventory / withdrawals / one-time effects
→ transaction/lock/CAS/unique/idempotency equivalent
  + concurrent/replay negative proof

S-BAAS-AUTHZ
→ Supabase / Firebase / Appwrite / client-addressable BaaS
→ provider-side deny-by-default policies, RLS/rules where applicable,
  cross-user/cross-tenant read + write proof

S-PAID-API-BUDGET
→ LLM / image / SMS / voice / other metered APIs
→ per-user/tenant quotas + global fail-closed ceiling/circuit breaker,
  authoritative/concurrency-safe usage accounting
```

Это routing labels, а не замена `S-01`, `S-02`, ... . Например `S-BAAS-AUTHZ: REQUIRED` может материализоваться как несколько отдельных `S-xx`: RLS на таблицах, storage policies и cross-tenant negative tests.

Функционально зелёные тесты не могут автоматически закрыть security row. `VERIFIED` запрещён, пока выбранный `S-xx` не имеет свежего negative evidence.

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

Материальный UI-проект использует один root `DESIGN.md`: personality, UX principles, app shell/layout, spacing/density, typography, colors/surfaces/depth/radii, components/states, responsive/touch, accessibility, motion, выбранное направление, invariants и история material design decisions.

Если файла нет и exact design-doc write разрешён — Matreshka создаёт его. Без разрешения возвращает `DESIGN_READY_TO_SAVE`.

Когда пользователь не понимает, чего хочет, Matreshka может построить обычно 3, максимум 5 реально разных изолированных prototype directions. Production-код не меняется до выбора или валидного delegated decision.

### Apple-inspired design core

Apple-концепция входит в ядро UX-мышления, но не является visual preset «сделай как Apple»:

```text
Purpose · Agency · Responsibility · Familiarity
Flexibility · Simplicity · Craft · Delight
```

Плюс wayfinding, feedback, grouping/mapping, direct manipulation, spatial consistency, typography hierarchy, focus/contrast/touch targets/reduced motion/accessibility.

UI-task получает frozen design identity/hash и только нужный `DESIGN_CONTEXT_SET`. Случайные новые radius/color/component/layout patterns → `DESIGN_DRIFT`, а не автоматическое изменение дизайн-контракта.

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

Existing repository E2E используется первым. Personal Chrome profile/ambient session и неизвестный destructive test environment запрещены как автоматический test context.

G4 слепо проверяет исходный запрос и не читает `DESIGN.md`, prototypes, design-review/visual reports, spec/plan/dashboard.

## Русский dashboard и устойчивое run-state

При разрешённом run-state:

```text
.matreshka/runs/<run-id>/dashboard.html
.matreshka/runs/<run-id>/dashboard-state.js
```

Dashboard показывает progress, Project/Design Intelligence, tests/security, E2E/G4, permissions, время и truthful token telemetry. Если host не отдаёт точный token counter — `Недоступно`. Dashboard — projection, не authority/evidence.

После аудита ошибок Autopilot v1.0.1+ в 0.5 добавлен отдельный hardening:

- **A1 Embedded Snapshot** — `dashboard.html` несёт последний корректный snapshot и остаётся читаемым, даже если sibling `dashboard-state.js` недоступен в preview/data/file режиме;
- **A2 Atomic Run-State Sync** — `sync_run_state.py` валидирует state, атомарно пишет projection и обновляет только marked snapshot block; не запускает server/browser и не трогает PID/ports;
- **A3 Stage Invariants** — explicit `stageOrder` + механическая проверка конфликтующих active stages/transition timestamps; helper никогда не превращает переход по времени в semantic PASS;
- **A4 Context Cost Gate** — exact UTF-8 byte budgets для hot-path instruction surfaces без выдуманной оценки runtime tokens;
- **A5 Native Repeatability Matrix** — шесть blocking properties × 5 повторов на каждый release-claimed host. Один удачный native run больше не считается доказательством стабильности формулировки.

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

Из корня репозитория запускайте тот же набор, что и CI:

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

- `validate_dev_05.py` — strict package/negative self-tests for 11 skills;
- `check_dev_05.py` — static cross-component wiring;
- `check_dev_05_behavioral_contracts.py` — cross-skill behavioral coverage;
- `check_security_hardening.py` — five automatic security families + spec/review/S- flow + security eval matrix;
- `sync_run_state.py --self-test` — atomic snapshot/state invariant mechanics;
- `check_context_budget.py` — exact byte-budget regression guard;
- `evaluate_native_repeatability.py --validate-plan` — repeatability release matrix contract;
- `check_autopilot_regressions.py` — A1–A5 wiring/CI regression guard;
- `doctor_dev_05.py` — read-only development diagnostics.

Static budget bytes **не** являются runtime token usage и никогда не должны попадать в dashboard как token count.

## До release 0.5.0

Нужно получить:

1. final-development-HEAD deterministic validation/CI PASS;
2. disposable native full-stack acceptance для Project Intelligence + Design Intelligence + Security hardening + Browser E2E + Visual Design Check + G4 + Design/Docs Drift + dashboard/recovery;
3. repeatability evidence по `evals/native-repeatability.json` для каждого host, который будет заявлен в release;
4. затем version bump manifests/marketplaces/validators/evals до `0.5.0` и финальная publisher/security metadata проверка.

До этого ветка остаётся `0.5 development preview`.
