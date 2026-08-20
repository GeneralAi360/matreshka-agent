# Matreshka Agent 0.5 — Browser E2E & G4 Browser Acceptance

- Status: `CONFIRMED_BY_USER`
- Date: `2026-08-20`
- Branch: `dev/0.5-brief-traceability-observability`
- Source inspiration: `amorev/vibecode-setup-public` browser/E2E patterns only; no Pi-specific configuration is adopted.

## Goal

Extend Matreshka Agent's existing verification and G4 blind-acceptance model so web projects can be proved through browser behavior without weakening the current permission, security, review, recovery, or source-intent boundaries.

The browser layer must remain host-neutral. Codex, Claude Code, Cursor, Antigravity, or another supported host may expose different browser tools; Matreshka must detect real capabilities rather than depend on `.pi/mcp.json`, Pi subagents, or a specific MCP configuration.

## Core model

```text
implementation
→ independent review
→ technical/security verification
   ├─ focused/unit/integration/static/build checks
   └─ automated browser E2E when applicable
→ G4 blind acceptance
   ├─ CLI/API observation when applicable
   └─ independent browser observation for web outcomes when applicable
→ finish
```

Automated E2E and G4 browser acceptance are deliberately different:

- automated E2E proves declared test scenarios against the current state;
- G4 browser acceptance independently derives observable outcomes from the original source brief and checks the actual product without consulting specification, manifest, plan, task, implementation, review, verification, progress, or dashboard interpretations.

## B-01 — Browser capability preflight

For a web-relevant run, record a `BROWSER_E2E` capability with evidence for:

- existing E2E framework and configuration;
- existing repository-declared E2E command;
- managed browser availability;
- optional Chrome/Chromium CDP availability;
- host browser-tool availability;
- isolated browser-context support;
- screenshot support;
- trace/video support when available;
- console inspection support;
- relevant network inspection support;
- whether application runtime is already available;
- whether browser/dependency installation, local process start, port binding, test-data mutation, or destructive setup would be required.

Never infer a capability from the platform name alone.

## B-02 — Existing E2E first

Prefer current repository infrastructure. If Playwright, Cypress, Selenium, WebdriverIO, another E2E framework, or an existing browser-testing convention is already present and valid, use it rather than installing or scaffolding a second framework.

Do not replace Cypress with Playwright merely because Playwright is Matreshka's recommended default for a new setup.

## B-03 — Optional E2E setup

When browser behavior is acceptance-relevant and no usable E2E infrastructure exists, Matreshka may propose an E2E setup. The recommended default for a new setup is Playwright with a managed isolated Chromium browser unless repository constraints justify another choice.

The following remain separate permissions and are never implied by `FULL_AUTO`:

- dependency installation;
- package-registry/network access;
- browser binary download;
- browser launch;
- local application/service process start;
- port binding/listening;
- local test-data mutation;
- destructive test reset/setup.

Without required authority, record the row as `NOT_RUN`, `BLOCKED`, or `HANDOFF_REQUIRED` rather than silently installing or starting anything.

## B-04 — Browser modes

Portable capability labels:

- `PLAYWRIGHT_MANAGED` — framework manages an isolated browser/context;
- `CHROME_CDP` — connect to an explicitly approved test Chrome/Chromium debugging endpoint;
- `HOST_BROWSER_TOOL` — use a host-provided browser capability after verifying its scope and isolation;
- `UNAVAILABLE` — no trustworthy browser path exists.

Do not require Chrome CDP when managed Playwright is sufficient.

## B-05 — Isolation

Never use a personal browser profile, personal authenticated session, unrelated open tabs, or ambient cookies as test authority.

For managed Playwright use a fresh browser context per independent scenario where practical. For CDP require an explicitly approved test browser/profile or isolated `user-data-dir`. Treat a personal profile as `BLOCKED` until a safe isolated target exists.

## B-06 — Automated E2E verification

The technical verifier may run a repository-declared browser E2E command when it is inside the permission envelope.

Record:

- exact command;
- current state/ref/hash;
- exit code;
- pass/fail/skip counts;
- browser/framework/mode when known;
- evidence references for screenshots, traces, or video without copying private payloads;
- unexpected working-state mutation;
- environment caveats.

The verifier does not fix tests, loosen assertions, install dependencies, mutate production data, or create a second test framework.

## B-07 — Browser G4 blind acceptance

When a source-brief outcome is inherently visual/browser-interactive and a trustworthy browser capability exists, G4 should prefer direct browser observation over code inspection.

Allowed blind inputs remain:

- redacted original source brief;
- actual current product/repository state required to operate the product;
- exact approved application URL/runtime target;
- approved browser capability;
- permitted run/test interactions.

Forbidden blind inputs remain:

- specification;
- `U-` manifest;
- plan/tasks;
- implementation reports;
- review findings/reports;
- technical verification report;
- progress/dashboard;
- controller completion claims.

For each material source outcome return `DELIVERED`, `PARTIAL`, `MISSING`, or `UNCHECKABLE` with observable evidence. Browser G4 never repairs code or changes requirement state.

A page that visually appears successful while a required network request fails is not `DELIVERED`. A stored value that the user asked to see but cannot see is not `DELIVERED`.

## B-08 — Destructive E2E firewall

A command or global setup that resets, truncates, recreates, seeds, migrates, or otherwise mutates a database/test environment requires explicit proof that the target is disposable or otherwise approved for that exact mutation.

Require:

- exact environment identity;
- evidence that it is not production and does not contain valuable uncontrolled data;
- exact destructive/test-data action;
- permission for the mutation;
- reset/rollback expectation.

If this cannot be proved, block that setup even when the command is named `test:e2e`.

## B-09 — Test credentials and private browser evidence

Use test accounts, fixtures, generated temporary credentials, or named secret references. Never copy secret values into ledger, dashboard, source brief, screenshots, traces, or reports.

Avoid evidence that captures unrelated personal data or complete request/response payloads. Prefer minimal screenshot/trace references and compact console/network findings.

## B-10 — Donor patterns adopted

Adapt these patterns from `amorev/vibecode-setup-public`:

- Playwright browser E2E as a practical default for new web setups;
- optional CDP connection through `chromium.connectOverCDP()`;
- a fresh browser context for scenarios;
- separated automatic E2E runner and independent browser checker roles;
- screenshots/traces/video-on-failure where supported;
- console/network inspection for browser acceptance;
- compact reports rather than full logs/DOM dumps.

Do not adopt:

- `.pi/mcp.json` or Pi-specific setup;
- automatic known-password normalization;
- automatic destructive DB resets without an environment gate;
- personal Chrome profiles;
- implicit network/dependency/browser-install authority;
- a generic `test-fixer` that bypasses Matreshka's implementer → review → verify correction loop;
- unpinned `@latest` runtime dependencies as a required mechanism.

## B-11 — Dashboard and ledger

Record browser capability and evidence as projection/state, not authority:

- E2E framework and mode;
- automated E2E status/counts;
- browser G4 status;
- evidence reference count/paths when safe;
- console/network blocking findings count;
- permissions that were unavailable.

Dashboard never starts a server/browser or grants permissions.

## B-12 — Completion rule

For a web outcome where browser behavior is required by the confirmed acceptance contract:

- unavailable required automated E2E evidence prevents technical `VERIFIED` when that row is mandatory;
- a material browser-G4 `PARTIAL` or `MISSING` prevents G4 `PASS` and final `COMPLETE`;
- an acceptance-critical `UNCHECKABLE` yields a truthful partial/block/handoff state.

`E2E PASS` alone is never equivalent to `G4 PASS`.

## Non-goals

- Do not bundle a browser binary with Matreshka Agent.
- Do not add a required external dependency to the plugin package.
- Do not make Playwright mandatory for repositories that use another valid E2E stack.
- Do not add Pi-specific MCP configuration.
- Do not grant runtime, network, browser, Git, secret, or destructive permissions from a browser-test request.
- Do not replace security verification with browser checks.
