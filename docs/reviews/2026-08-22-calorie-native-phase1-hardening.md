# Matreshka Agent 0.5 — Calorie Native Acceptance Phase 1 Findings

- Date: `2026-08-22`
- Branch: `dev/0.5-brief-traceability-observability`
- Native fixture: `matreshka-calorie-acceptance`
- Status: `HARDENED_PENDING_RETEST`

## What passed

The native run correctly:

- selected `ASSISTED`;
- created an isolated disposable project;
- stopped before production implementation;
- kept root `DESIGN.md` as `DESIGN_DIRECTION_REQUIRED` draft with no frozen identity;
- produced three structurally different prototype directions;
- kept production source/dependencies/Git absent before design choice.

## Native findings

### F1 — product UI locale was not resolved

The conversation was Russian, but prototype product copy was created in English without asking which language the actual application should use.

Fix:

- conversation language and `PRODUCT_UI_LOCALE` are separate;
- `INTERVIEW`/`ASSISTED` asks one material locale question before meaningful prototype copy when no repository/user locale evidence exists;
- prototype/product copy uses resolved locale.

### F2 — prototype directions still contained generic AI slop

The three directions were structurally distinct, but each leaned on recognizable generic defaults: cream editorial, cool blue-charcoal SaaS dashboard, or gray/purple component-kit treatment, plus repeated kicker/headline/pill/card patterns.

Fix:

- added `designing-product-experience/references/anti-slop.md`;
- every direction now needs a product-specific signature and anti-slop pass before presentation;
- generic template divergence is not sufficient merely because layouts differ.

### F3 — dropdown open state broke the design language

The closed Meal field fit the prototype, but opening it exposed an unrelated native macOS select popup. The prototype flow had no explicit open-state quality gate.

Fix:

- selects/menus/popovers/comboboxes/date pickers/dialogs/sheets must be checked open/expanded;
- verify visual language, width, collision, portal/z-index, scrolling, keyboard/focus, touch/mobile and theme;
- native platform controls are allowed only when native appearance is deliberate;
- existing accessible primitives are preferred over hand-rolled generic controls.

### F4 — `S-ATOMIC-EFFECT` over-triggered on ordinary SQLite CRUD

The native run marked the family `REQUIRED` merely because food CRUD and daily-goal persistence use SQLite.

Fix:

- ordinary local CRUD/settings persistence is explicitly a normal correctness/transaction concern, not automatically `S-ATOMIC-EFFECT`;
- the family triggers when concurrent/replayed actions can multiply value, consume a one-time right, oversell scarcity, duplicate grant/payment/redemption, or create another materially irreversible/multiplicative effect;
- added a calorie-tracker regression eval requiring `N/A(reason)` for this scope.

### F5 — durable run state was initialized too late

Prototype files were created while only partial progress state existed; ledger/stage integrity state was absent and `stateIntegrity=NOT_AVAILABLE`.

Fix:

- controller-managed prototype creation is explicitly state-changing;
- when durable Matreshka run-state writes are authorized/required, controller run state must exist before prototype writes;
- when run-observability/dashboard is enabled, `stageOrder`/`stateIntegrity` projection should be initialized before or with the first prototype write.

## New behavioral coverage

Added Design Intelligence cases:

- `ui-locale-unresolved-assisted-prototype`
- `anti-slop-generic-directions`
- `dropdown-open-state-quality`
- `prototype-write-requires-run-state`

Added Security Hardening case:

- `security-atomic-effect-ordinary-crud-na`

The existing cross-skill behavioral checker now requires these cases and static contract markers.

## Retest expectation

Restart the disposable acceptance run from a clean project using the new Matreshka snapshot.

Before prototype generation in `ASSISTED`, the expected first unresolved product question is the product UI language/locale. After that, prototype directions should:

- use that locale;
- contain genuine structural divergence;
- pass anti-slop review;
- show/verify representative open layered-control state when such a control is part of the design;
- have controller run-state initialized before prototype files appear.

The calorie fixture should classify all five automatic hardening families as `N/A(reason)` unless the architecture/scope itself introduces a trigger.
