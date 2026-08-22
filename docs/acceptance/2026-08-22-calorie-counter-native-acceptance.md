# Matreshka Agent 0.5 — Native Full-Stack Acceptance Fixture: Calorie Counter

- Date: 2026-08-22
- Branch under test: `dev/0.5-brief-traceability-observability`
- Purpose: first disposable native full-stack acceptance after Project Intelligence, Design Intelligence, Browser/E2E, run-state hardening and Security-by-Design hardening.
- Product type: local single-user web application.
- Release claim: this fixture alone cannot release `0.5.0`.

## Product brief

Build a small calorie-tracking web application for one local user.

User outcomes:

1. The user can add a food entry with name, calories, meal category and date.
2. The user can edit and delete an entry.
3. The user can set a personal daily calorie target. The app does not calculate or recommend a medical/nutritional target.
4. The dashboard shows consumed calories, remaining calories, progress toward the target and a meal breakdown for the selected day.
5. The user can switch between dates and see persisted entries for that date.
6. Empty, loading, validation and error states are understandable.
7. The interface works at desktop, tablet/compact and mobile widths without horizontal overflow.
8. Keyboard focus remains visible and common actions are operable without relying on hover.

## Deliberate non-goals

Keep the first fixture small and diagnosable:

- no authentication/accounts;
- no multi-user/tenant behavior;
- no Supabase/Firebase/Appwrite/BaaS;
- no paid/external API;
- no AI calorie estimation;
- no image/file upload;
- no payments;
- no deploy/production hosting;
- no medical or nutritional recommendation engine.

These exclusions should cause the corresponding automatic security-hardening families to be recorded as `N/A(reason)`, not silently omitted.

## Expected topology

The exact stack may be chosen by the source-qualified controller inside granted local authority, but the project should expose distinct responsibility boundaries equivalent to:

```text
AREA-FRONTEND
AREA-BACKEND
AREA-DATA
AREA-E2E
```

A recommended simple reference stack for the disposable fixture is:

```text
frontend: React + Vite + TypeScript
backend: FastAPI or another small repository-appropriate HTTP API
persistence: local SQLite
browser E2E: Playwright or the repository-declared equivalent
```

Do not create fake areas merely to satisfy this document. If the chosen architecture differs, Project Topology must explain the actual boundaries.

## Cross-area interfaces

At least one producer/consumer contract must be frozen before dependent frontend/backend implementation. A reasonable shape is:

```text
IC-01 Daily calorie entries

GET    /api/day?date=YYYY-MM-DD
POST   /api/entries
PATCH  /api/entries/:id
DELETE /api/entries/:id
PUT    /api/settings/daily-goal
```

The controller may refine the exact API but frontend and backend must consume the same frozen `IC-xx` identity.

## Design Intelligence test

The user intentionally does not specify a visual style.

Matreshka must therefore exercise Design Intelligence rather than inventing production UI ad hoc:

1. classify UI/design as material;
2. perform Design Recon for the empty/new project;
3. propose normally three genuinely different design directions;
4. variants must differ on real design axes, not only color;
5. keep exploration isolated from production implementation;
6. ask the user to choose a direction in `ASSISTED` mode;
7. after selection create/reconcile the single root `DESIGN.md` when authorized;
8. freeze a design identity/hash before dependent UI tasks;
9. create task-local `DESIGN_CONTEXT_SET` rather than passing all design history;
10. apply the Apple-inspired Matreshka design core as UX-quality reasoning, not as an Apple visual preset.

## Security selection expectation

The normal baseline still applies for input validation, safe errors, dependencies, localhost CORS/origin configuration and secret hygiene.

For this intentionally bounded fixture the five automatic hardening families are expected to resolve approximately as:

```text
S-AUTH-HARDENING: N/A(no authentication/password/admin accounts)
S-FILE-EXECUTION: N/A(no uploads/external stored files)
S-ATOMIC-EFFECT: N/A(no race-sensitive value/entitlement/money effect)
S-BAAS-AUTHZ: N/A(no client-addressable BaaS)
S-PAID-API-BUDGET: N/A(no metered external API)
```

If implementation choices introduce one of those triggers, the matching family becomes `REQUIRED`; the controller may not keep the predeclared N/A merely because this fixture expected a simpler architecture.

## Required Matreshka evidence

### Source intent

- source brief preserved;
- U requirements atomized;
- G1 truthfully resolved;
- G2 independent brief→spec coverage;
- G3 requirement↔task↔proof mapping;
- G4 fresh blind acceptance against actual application.

### Project Intelligence

- current `PROJECT_TOPOLOGY` from repository evidence;
- one primary area per implementation task;
- narrow `AREA_CONTEXT_SET` with explicit exclusions;
- shared frozen `IC-xx` for drift-prone frontend/backend seam;
- `RUNTIME_MAP` with observed ownership/status/log/port facts;
- specialist routing without agent-budget inflation;
- Documentation Drift Gate before finish.

### Design Intelligence

- design relevance/recon;
- three real directions unless valid evidence makes exploration unnecessary;
- one selected direction;
- one canonical root `DESIGN.md`;
- frozen design identity;
- narrow `DESIGN_CONTEXT_SET`;
- independent Design Review;
- fresh Visual Design Check;
- Design Drift Gate before finish.

### Implementation/review/verification

- valid RED before product implementation for executable task behavior;
- fresh GREEN + nearby regressions;
- independent read-only review;
- technical/security verification;
- browser E2E on exact current state;
- visual verification remains separate from E2E;
- G4 remains blind to spec/plan/Project Intelligence/`DESIGN.md`/design reports/dashboard.

## Browser acceptance scenarios

At minimum prove:

1. Add `Овсянка`, 350 kcal, breakfast, selected date → daily consumed total becomes 350.
2. Add a second meal → total and meal breakdown update.
3. Edit calories on an existing entry → total recomputes correctly.
4. Delete an entry → total recomputes and the entry disappears.
5. Change the personal daily target → progress/remaining values update.
6. Switch date → entries persist per date and do not leak to another date.
7. Invalid calories (empty, non-numeric, zero/negative according to confirmed validation policy) are rejected safely.
8. Mobile representative viewport (~390 px) has no horizontal overflow and primary controls remain usable.
9. Keyboard focus is visible on primary interactive elements.
10. Empty day state is understandable.

Keep screenshots/trace evidence minimal and safe.

## Run-state hardening acceptance

The current run should use the updated dashboard projection contract:

- `dashboard-state.js` carries `stageOrder`/`stateIntegrity`;
- `sync_run_state.py` may be used only with exact run-state/local-command authority;
- synchronized `dashboard.html` carries a last-known-good embedded snapshot;
- missing live sibling state must not produce an irrecoverably blank dashboard;
- conflicting sequential active stages must be rejected/flagged;
- mechanical normalization may derive timestamps but never semantic PASS.

Do not start an HTTP server merely for the Matreshka dashboard unless separately authorized and actually needed by the host.

## Completion criteria

A clean fixture result requires all applicable gates to agree:

```text
technical/security verification: sufficient current evidence
browser E2E: PASS when required
Design Review: no blocking design finding
Visual Design Check: PASS/PARTIAL only according to actual evidence
G4: PASS for all material source outcomes
Design Drift Gate: DESIGN_CURRENT or valid resolved state
Documentation Drift Gate: DOCS_CURRENT or DOCS_NOT_REQUIRED / authorized resolved update
run-state integrity: no unresolved contradiction
```

A green E2E suite must not override a visual-design failure or G4 missing outcome.

## What this first fixture does NOT prove

Even a perfect run does not yet prove:

- the five security-hardening families under positive trigger conditions;
- native repeatability across five repetitions;
- every supported host/platform;
- deployment/remote-operation behavior.

Those require dedicated later fixtures/repeated runs.
