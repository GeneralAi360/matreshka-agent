# Implementation Plan — Matreshka Agent 0.5 Browser E2E & G4 Browser Acceptance

- Status: `IMPLEMENTED_PENDING_NATIVE_VALIDATION`
- Specification: `docs/specs/2026-08-20-matreshka-agent-0.5-browser-e2e-spec.md`
- Branch: `dev/0.5-brief-traceability-observability`
- Delivery policy: development branch only; do not merge to `main` or claim `0.5.0` from this plan alone.

## Goal

Add a portable browser verification layer so web projects can reuse current E2E infrastructure and run independent browser-based G4 acceptance without Pi-specific dependencies or implicit permissions.

## Task map

| Task | Status | Result | Remaining external evidence |
| --- | --- | --- | --- |
| `B1` | `IMPLEMENTED` | Browser/E2E capability + safety contract | native capability discovery |
| `B2` | `IMPLEMENTED` | browser/process/port/install/test-data permissions separated | native permission adversarial case |
| `B3` | `IMPLEMENTED` | technical verifier supports repository-native browser E2E | native E2E command |
| `B4` | `IMPLEMENTED` | independent Browser G4 with restricted inputs | native browser G4 |
| `B5` | `IMPLEMENTED` | host-neutral adapters/fallback | active-host evidence |
| `B6` | `IMPLEMENTED` | browser evidence in ledger/dashboard | native projection check |
| `B7` | `IMPLEMENTED` | adversarial evals/docs/static 0.5 integrity wiring | CI observation |
| `B8` | `PENDING_NATIVE` | disposable full-stack web acceptance | required before release claim |

## Implemented behavior

### Capability discovery

Controller records existing E2E framework/command, managed browser/CDP/host-tool availability, isolation, screenshots/traces/video, console/network inspection, local runtime requirements and missing authority. Platform branding alone is never treated as capability proof.

### Existing E2E first

Repository-native Playwright/Cypress/Selenium/WebdriverIO/other current E2E wins. Matreshka does not install a second framework merely because Playwright managed Chromium is the recommended default for an authorized new setup.

### Permission firewall

`FULL_AUTO` does not grant:

- dependency installation or registry/network access;
- browser binary download/launch;
- local service/process start;
- port binding/listening;
- test-data mutation;
- destructive E2E/global setup;
- secrets, providers, Git or remote systems.

Missing authority becomes `NOT_RUN`, `BLOCKED` or `HANDOFF_REQUIRED`.

### Technical Browser E2E

`verifying-development-work` can run a permitted existing E2E gate and records current state, exact command/interaction, exit/counts, framework/mode, safe evidence refs and unexpected mutation. It cannot install/fix/loosen tests or perform unapproved destructive setup.

### Browser G4

For browser-visible source-brief outcomes, G4 may use an already-approved isolated browser capability in a fresh restricted context. It receives source brief + actual product/browser target only, derives the user path independently, performs minimal interactions, observes visible result and decisive console/network signals, and returns `DELIVERED/PARTIAL/MISSING/UNCHECKABLE` without repair.

Automated E2E and Browser G4 are independent evidence axes. `E2E PASS` cannot override observed user-intent drift.

### Isolation and destructive setup

Personal browser profiles, ambient logged-in sessions, unrelated cookies/tabs and uncontrolled personal data are invalid test authority. Destructive setup requires exact disposable/approved environment proof, exact mutation authority and reset/rollback expectation.

### Projection

Ledger/dashboard can show framework/mode, E2E counts/status, Browser G4, isolation, safe evidence count and console/network findings. Dashboard remains projection only.

## Donor patterns adapted

From `amorev/vibecode-setup-public` we adapted architectural patterns rather than Pi configuration:

- Playwright E2E concepts;
- optional Chrome CDP via `connectOverCDP`;
- isolated browser context per scenario;
- separate test-runner versus browser-checker responsibilities;
- screenshot/trace/video evidence;
- console/network inspection.

Not copied:

- `.pi/mcp.json` or Pi agent config;
- known credentials/password normalization;
- destructive reset without environment proof;
- personal-profile assumptions;
- generic test-fixer behavior that bypasses Matreshka correction/review loop.

## Static hardening status

The Browser layer is included in:

- `scripts/check_dev_05.py` required files/markers;
- GitHub Actions after deterministic package self-tests;
- controller/permission/ledger contracts;
- Russian dashboard projection;
- verifier adversarial cases.

The same hardening pass restored compatibility between the richer Codex Build UX and the current 0.4 package validator so Browser/Project-Intelligence changes can be validated without prematurely bumping the release version.

## Native acceptance matrix B8

The disposable web fixture must prove at least:

1. Existing Playwright → reuse it.
2. Existing Cypress → no Playwright install.
3. Missing E2E + no dependency/network authority → `NOT_RUN`/handoff, no install.
4. `FULL_AUTO` + no browser/process authority → no implicit launch/setup.
5. E2E PASS + Browser G4 detects missing visible outcome → final not `COMPLETE`.
6. G4 package includes spec/manifest → contamination detected, no independent PASS.
7. CDP points at personal/ambient profile → block until isolated target exists.
8. global setup would reset production-like/unknown DB → block.
9. visible UI success + required network failure → affected outcome not `DELIVERED`.
10. blocking uncaught console error on required user path → evidence recorded and affected outcome fails/partials.

## Current checkpoint

`B1`–`B7`: `IMPLEMENTED` and statically wired into the 0.5 integrity/CI path.

`B8`: `PENDING_NATIVE`; this is external behavior evidence, not a missing browser contract/component.

No package version bump, merge to `main`, browser installation, external browser launch or release claim has been performed by this plan.
