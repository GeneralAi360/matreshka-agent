# Browser E2E and Browser G4 Contract

Use this reference when the current acceptance surface is browser-visible or when the repository already declares browser E2E checks. This contract is portable and does not depend on Pi, `.pi/mcp.json`, or one specific browser integration.

## Two evidence axes

Keep these independent:

1. **Automated browser E2E** — technical verification of repository-declared scenarios.
2. **Browser G4 blind acceptance** — independent observation derived from the original source brief.

`E2E PASS` does not imply `G4 PASS`, and browser G4 never replaces unit/integration/static/security evidence that the confirmed quality gate requires.

## Capability preflight

Before browser work, inspect safely and record:

```text
BROWSER_E2E
web_relevant: YES | NO
existing_framework: Playwright | Cypress | Selenium | WebdriverIO | other | none
existing_command: <repository-declared command or none>
managed_browser: YES | NO | UNKNOWN
chrome_cdp: YES | NO | UNKNOWN
host_browser_tool: YES | NO | UNKNOWN
isolated_context: YES | NO | UNKNOWN
screenshots: YES | NO | UNKNOWN
trace_or_video: YES | NO | UNKNOWN
console_inspection: YES | NO | UNKNOWN
network_inspection: YES | NO | UNKNOWN
app_runtime_available: YES | NO | UNKNOWN
install_required: YES | NO
local_process_start_required: YES | NO
port_bind_required: YES | NO
test_data_mutation_required: YES | NO
destructive_setup_possible: YES | NO
```

Never infer availability from the words Codex, Claude, Cursor, Antigravity, Chrome, or Playwright alone. Verify actual current host/project capabilities.

## Existing E2E first

Prefer a valid repository-native browser framework and command. Inspect package scripts, framework config, E2E directories, CI configuration, repository instructions, and current test documentation.

Examples of strong existing seams:

- `playwright.config.*` plus a declared Playwright command;
- `cypress.config.*` plus a declared Cypress command;
- an explicit Selenium/WebdriverIO test target;
- an existing host browser test command documented by the repository.

Do not create a second framework just because Matreshka prefers Playwright for a new setup.

## Optional new setup

When no valid browser E2E exists but browser behavior is acceptance-critical, the controller may propose a setup. The portable default recommendation is Playwright with a managed isolated Chromium browser, unless repository/host facts favor another stack.

A proposal is not permission. Separate authority is required for any of:

- dependency installation;
- registry/network access;
- browser binary download;
- browser launch;
- local service/process start;
- port binding/listening;
- test database/data mutation;
- destructive reset or migration.

Without authority, mark the required row `NOT_RUN`, `BLOCKED`, or `HANDOFF_REQUIRED`.

## Browser modes

Use portable labels only after evidence:

- `PLAYWRIGHT_MANAGED` — framework launches/manages an isolated browser/context;
- `CHROME_CDP` — explicitly approved test Chrome/Chromium endpoint over CDP;
- `HOST_BROWSER_TOOL` — host exposes suitable browser controls with known scope/isolation;
- `UNAVAILABLE` — no trustworthy browser path.

Do not require CDP when managed browser execution is sufficient.

### CDP isolation

A CDP target must not be a user's ordinary personal browser profile or ambient authenticated session. Require an explicitly approved test profile/isolated `user-data-dir` or other evidence that unrelated cookies, sessions, tabs, and personal data are excluded.

If only a personal profile is available, return `BLOCKED` or request a safe test target.

## Automated E2E technical verification

The normal technical verifier may run an existing E2E command only when the command and any required runtime/setup actions are inside the permission envelope.

Record:

```text
BROWSER_E2E_VERIFICATION
framework: <name>
mode: <PLAYWRIGHT_MANAGED|CHROME_CDP|HOST_BROWSER_TOOL|other>
command: <exact command>
state: <ref/hash/baseline identity>
exit: <code>
passed: <count or unavailable>
failed: <count or unavailable>
skipped: <count or unavailable>
evidence: <safe screenshot/trace/video/report refs or none>
console_findings: <count/summary or unavailable>
network_findings: <count/summary or unavailable>
mutation_check: PASS | FAIL | UNKNOWN
status: PASS | FAIL | NOT_RUN | BLOCKED
```

Do not:

- fix code or tests;
- loosen assertions;
- rewrite fixtures merely to obtain green;
- install a framework from verifier role;
- run an unapproved destructive setup;
- treat zero executed tests as a meaningful pass;
- copy full private traces, DOM dumps, or request payloads into reports.

A failing E2E command is current technical evidence, not an instruction to repair from the verifier role.

## Layered-control open-state verification

For UI work, a closed screenshot is not enough to prove a select/menu/popover/dropdown/dialog/date-picker/combobox. When a layered control is affected or materially visible in the accepted design, browser verification should exercise its open/expanded state.

Representative checks:

```text
LAYERED_CONTROL_CHECK
control: <select|menu|combobox|date-picker|popover|dialog|sheet|other>
trigger_state: PASS | FAIL | UNCHECKABLE
open_state: PASS | FAIL | UNCHECKABLE
keyboard: PASS | FAIL | UNCHECKABLE
focus_return: PASS | FAIL | UNCHECKABLE
viewport_collision: PASS | FAIL | UNCHECKABLE
portal_z_index: PASS | FAIL | UNCHECKABLE
scroll_long_content: PASS | FAIL | NOT_APPLICABLE | UNCHECKABLE
mobile_touch: PASS | FAIL | NOT_APPLICABLE | UNCHECKABLE
visual_language: PASS | FAIL | UNCHECKABLE
evidence: <safe refs>
```

When applicable, verify:

- open surface visually belongs to the frozen design identity;
- width/min-width/wrapping are intentional;
- surface does not clip at viewport/container edges;
- portal/z-index does not place it behind unrelated content;
- selected/hover/focus states are readable;
- keyboard arrows/typeahead/tab/enter/escape work as appropriate;
- focus returns after close when expected;
- mobile/touch target and scrolling behavior are usable;
- reduced-motion/theme state remains coherent.

A native platform `<select>` may intentionally use platform UI. If the frozen design contract expects a custom art-directed primitive and the open native system popup visibly breaks that contract, record design evidence as FAIL rather than approving from the trigger alone.

A control that looks interactive but cannot be operated is a failure. Do not preserve dead prototype behavior into production.

## Product-locale visual evidence

When product UI language/locale is part of the design contract, browser/visual evidence should use the resolved product copy rather than framework/example English. Check materially relevant wrapping, dates/numbers, labels, form widths and truncation. Matreshka's dashboard/test chrome may use the conversation language; that is separate from product copy.

## Destructive E2E firewall

Before a browser command/global setup may reset, truncate, recreate, migrate, seed, or otherwise mutate data, prove and record:

```text
TEST_ENVIRONMENT
identity: <exact target>
disposable_or_explicitly_approved: YES
data_value_boundary: <why valuable production-like data is not at risk>
mutation: <exact reset/seed/migration>
authority: <approval source>
rollback_or_reset_expectation: <exact result>
```

If any required field is missing, block the destructive setup even if the command is named `test`, `test:e2e`, `globalSetup`, or `db:reset`.

Never infer safety from `localhost` alone; localhost can proxy or point to valuable data.

## Test credentials

Prefer disposable fixtures, generated temporary accounts, or named secret references. Never record secret values in source brief, ledger, dashboard, browser report, screenshot captions, traces, or final handoff.

If a browser run would expose unrelated personal or production credentials, stop or switch to a clean test context.

## Browser G4 blind acceptance

Use browser observation for G4 when a material source-brief outcome is inherently web/UI-interactive and a trustworthy browser capability exists.

### Allowed inputs

- redacted source brief;
- actual current product state needed to operate the app;
- exact approved application URL/runtime target;
- approved browser capability;
- permitted interactions/commands;
- project/current-state identity.

### Forbidden inputs

Do not consult:

- specification;
- `U-` manifest;
- plan/tasks;
- implementation report;
- review report/findings;
- technical verification report;
- progress/dashboard;
- controller completion claims.

If those artifacts were supplied into the accepted blind context, report contamination and request a clean fresh-context rerun rather than claiming independent G4.

### Browser observation sequence

For each independently observable source outcome:

1. derive the expected user-visible behavior only from the source brief;
2. open the approved app target;
3. use a clean browser context/session;
4. perform the minimum real user interactions needed;
5. inspect visible result;
6. inspect relevant console/network signals when supported and materially useful;
7. capture minimal screenshot/trace evidence when useful and safe;
8. classify `DELIVERED`, `PARTIAL`, `MISSING`, or `UNCHECKABLE`;
9. do not repair anything.

A visually rendered success state is not `DELIVERED` when a required underlying request failed or the resulting user state is inconsistent. A backend value is not `DELIVERED` when the source brief requires that the user can see/use it and the UI does not expose it.

Return a browser-specific block inside the normal G4 report:

```text
BROWSER_G4
mode: <verified browser mode>
target: <safe URL/environment label>
isolated_context: YES | NO | DEGRADED
outcomes:
- <short source outcome> -> DELIVERED | PARTIAL | MISSING | UNCHECKABLE -> <observable reason>
console: <blocking summary or none/unavailable>
network: <blocking summary or none/unavailable>
evidence: <safe refs or none>
```

Any material browser outcome marked `PARTIAL` or `MISSING` prevents G4 `PASS`. Acceptance-critical `UNCHECKABLE` yields partial/block/handoff according to the missing environment/operator.

## Evidence hygiene

Prefer:

- one decisive screenshot over repeated full-page captures;
- trace/video only on failure or when required by project policy;
- console error summaries over complete console history;
- request status/method/path summaries over full bodies;
- report paths/hashes over embedded binary evidence.

Do not expose secrets, cookies, auth headers, personal data, or unrelated browser state.

## Host portability

The controller chooses the browser path from the active host adapter only after verifying the capability. A host may support only automated Playwright commands, only browser-tool interactions, both, or neither.

Missing browser tooling is an evidence gap, not permission to install or configure a new one automatically.
