# Testing from bootstrap through delivery

Use the selected [layout](project-layouts.md) and existing runners first. No mandatory Jest, Node backend, provider or Docker. [Browser E2E](../../verifying-development-work/references/browser-e2e.md) owns capability/isolation/setup/credentials/G4 rules.

## Stage contract

| Stage / owner | Input and action | Output / exit condition |
| --- | --- | --- |
| Interview and specification / wrapper → controller | Existing spec + material unanswered questions; identify actors, critical journeys, errors, access and persistence | Confirmed requirements and independent frontend/backend/data/hosting decisions; unresolved items explicit |
| Bootstrap / controller-routed writer | Resolved shape, existing files and authorized writes | Actual code/test directories, stack-valid manifests/configs, docs and bootstrap map; no install/start implied |
| Test preparation / same bounded writer | Existing runner or chosen compatible runner, per-layer commands and safe target | Config, real script/command source, synthetic fixtures with setup/cleanup ownership, first meaningful test; unavailable runtime is NOT_RUN/BLOCKED |
| Planning / planning skill | Confirmed spec, area map, test rows and interface contracts | Each requirement has task, owner, permitted paths, cwd, focused RED/GREEN command and proof; existing G3 before product-code implementation |
| Implementation / implementer | Narrow task brief, relevant design/API contracts | Run focused RED, implement minimal behavior, run GREEN and nearest regressions; report evidence and limitations |
| Review / independent reviewer | Scoped current diff and criteria | Findings with evidence; one consolidated correction wave and targeted recheck per existing policy |
| Verification / read-only verifier | Current project identity, approved runtime/targets and expected checks | Actual per-layer command/exit/counts/evidence; API PASS is not browser PASS; do not fix or loosen assertions |
| Documentation / controller-routed docs role | Fresh verified behavior and exact affected-doc allowlist | Update command/API/data/runtime facts; preserve canonical docs and no unrelated rewrites |
| Acceptance and finish / controller | Existing applicable G1–G4 and design/docs gates | Honest result, dashboard/checkpoint and authorized finish; commit/push/deploy are never inferred from a test or session command |

This table routes into the current controller; its exact gate order and authority take precedence. G4 uses a clean context with source brief + current product + permitted operations, not this map, plans, verification reports or dashboard. Session recovery rechecks changed files and known evidence, not every test regardless of need.

## Prepare concrete checks, not empty labels

Adapt [testing-plan-template.md](../assets/testing-plan-template.md). For every applicable layer name its app owner, scenario, exact cwd/command, declaration source, prerequisites, safe target, status and proof. Unknown commands remain unresolved, never plausible copy-paste commands. Frontend/npm commands cannot stand in for Python/Go/other backend checks.

| Layer | Responsibility | First useful check when behavior exists |
| --- | --- | --- |
| Frontend unit/component | Local rules, inputs, states | An input changes a visible state; empty/error/loading state is handled |
| Backend unit | Business rules without infrastructure | Validation or a state transition, including one invalid input |
| Backend API/integration | Requests, authorization, persistence, failure shape | Valid request persists; invalid request is rejected; database failure is handled |
| Data/access | Real chosen engine and trust boundary | Relevant constraints/transactions/migrations; denied wrong-user/anonymous request at API and/or database |
| Cross-service integration | Shared contracts | Producer response/error matches consumer expectation |
| Browser E2E | Actual UI interaction across required services | User action → backend/data → visible result → reload persists when required |
| Visual/accessibility | Rendered states and input methods | Keyboard/focus, relevant viewport, open menu/dialog; separate from technical E2E |

Create real configs, test source, commands and fixtures once tooling is resolved. First smoke tests exercise confirmed UI/API behavior; do not invent a health endpoint for coverage. Unimplemented behavior may yield RED. `expect(true)`, success-only scripts, zero-test pass flags and all-skipped suites are not proof.

Avoid trivial markup tests and duplicate app/root suites. Static sites may use manual browser checks without a runtime. Managed-backend unit tests may be reasoned NOT_APPLICABLE without own pure functions; integration/access coverage remains applicable.

Supertest/API E2E does not operate the rendered UI. Browser tests with mocked API verify UI behavior but not real persistence. Test a real chosen engine for its database-specific guarantees; SQLite in-memory cannot prove PostgreSQL constraints/RLS behavior. RLS applies only when selected; it does not replace API authorization. A privileged fixture client must not impersonate ordinary-user denial tests.

## Runtime and evidence

Before executing, identify the exact environment, isolated accounts/data, allowed mutation, setup/cleanup owner, process/port ownership and prerequisite authority using the existing browser/runtime contracts. A command named test/reset/globalSetup is not automatically safe. No database/provider setup, installs, browser downloads or personal browser profiles from bootstrap permission alone.

Run focused checks per task, broad regression/build at integration boundaries; repeat only for changes/failures/unresolved risk. Record baseline, command/cwd, exit/counts, target and safe evidence. Missing runtime is NOT_RUN/BLOCKED; old reports are not fresh runs.

For runnable scaffold acceptance, detect controlled UI and backend defects in an isolated owned fixture, then restore it. Never damage user code. Record unavailable execution and its next prerequisite honestly; structural checks cannot grant runtime PASS.
