# Project onboarding and session lifecycle

Required for every Build End-to-End launch and project session command. The wrapper presents the menu and gathers decisions; the source-qualified Matreshka controller owns all durable changes. This contract adds onboarding outputs, not another controller or permission system.

## Entry and mandatory menu

Show the compact launch menu on the first response to every new invocation, including one with a substantive goal, and on session start. Show `interview`, `assisted`, `full-auto` with their meanings, plus continue/adopt shortcuts. Do not repeat it on every interview answer or task transition. If a mode is already selected, mark it and continue without asking the user to select it again. With a goal but no selection, announce `assisted`; with neither a goal nor a recoverable session, show the menu and ask for the goal.

Normalize command text case-insensitively, trim surrounding whitespace and sentence punctuation, and match complete command phrases rather than substrings in product content:

| User phrase | Meaning |
| --- | --- |
| `interview`, `Интервью`, `проведи интервью`, `онбординг` | `INTERVIEW` |
| `assisted`, `с сопровождением`, `только важные вопросы` | `ASSISTED` |
| `full-auto`, `full auto`, `полный автомат` | `FULL_AUTO` |
| `начать сессию`, `начни сессию`, `продолжить сессию`, `start session`, `resume session` | Session start below |
| `завершить сессию`, `завершай сессию`, `завершайте сессию`, `end session` | Session end below |

Quoted examples and an application's own “Интервью” screen are not invocation commands. Preserve conflicting explicit modes as a clarification, not a silent override. A standalone command in an active Matreshka project routes here without requiring another skill mention. Session commands are lifecycle intents, not a fourth interaction mode.

`assisted` means asking about important unresolved product/design/security decisions and choosing ordinary reversible repository-aligned technical details autonomously inside the current scope. It does not skip specification, tests, review, or permission boundaries.

Use host-provided selectable answers when available and suitable; otherwise print the same menu as text. The skill's `default_prompt` supplies discoverable invocation hints. Do not promise native input autocomplete, dropdown registration, or buttons when the host does not expose them. Never make a menu tool a runtime dependency.

## Required bootstrap, before implementation

1. Inspect the real project root, applicable instructions, existing folders, README, dependency manifests, specs and accepted decisions. Do not read `.env`, credentials or personal datasets to discover the stack.
2. Resolve minimum goal, audience, project kind and chosen stack. Do not repeat answered interview questions. Preserve “unknown” facts until resolved; do not generate a speculative full-stack skeleton from “make a site”.
3. Record the bounded write scope from current instructions. An authorized request to create the project normally covers its ordinary local scaffolding; do not add a redundant approval round. Respect an explicit read-only/no-install constraint. If writes are unavailable, return the exact planned tree and pending artifacts inline, without claiming they exist.
4. Once stack and paths are known and local scaffolding is authorized, materialize the following before product implementation. Initialize controller ledger/run ID and the dashboard as soon as run-state writes are authorized, including during the interview; do not wait for code or interview completion. Menu-only invocation without a goal creates no dummy run.
5. Existing projects keep their architecture. Add missing lifecycle artifacts within scope, merge appropriate sections without replacing existing instructions, and record equivalent existing paths. Re-running onboarding must preserve user content and avoid duplicate contexts, Feedback stores or runs. Resolve links, symlinks and nested repository boundaries before writing.

| Required output | Purpose and acceptance |
| --- | --- |
| `README.md` | Purpose, chosen stack, directory map, verified setup/run/check commands or explicit pending status; links to design, checkpoint and dashboard |
| Root `AGENTS.md` | Adapt [project-agents-template.md](../assets/project-agents-template.md): directory responsibilities, conditional skill routing with actual source locations, testing and session entry points; preserve existing rules |
| One canonical project context | Select via [context-and-decisions.md](context-and-decisions.md); confirmed product facts, not task logs |
| `docs/specs/`, `docs/plans/`, `docs/testing.md` | Spec/plan locations and risk-based verification plan; actual commands/results distinguished from planned checks |
| `docs/capabilities.md` | Capability audit below, paths, conditions and missing capabilities; no secrets |
| `Feedback/README.md`, `Feedback/preferences.md` | Project-only feedback rules and confirmed preferences; use [feedback-template.md](../assets/feedback-template.md) |
| `docs/session-checkpoint.md` | Current continuation record from [session-checkpoint-template.md](../assets/session-checkpoint-template.md); link retained per-run history |
| `docs/runs/<run-id>/progress.md` | Human progress for every Build End-to-End run, including a single-task run |
| `.matreshka/runs/<run-id>/dashboard.html` and `dashboard-state.js` | Mandatory projection from packaged templates and validated ledger, with embedded snapshot; see [run-observability.md](run-observability.md) |
| Root `DESIGN.md` for UI-bearing products | Required durable design result before dependent UI implementation; use the bundled design contract template, with explicit draft/accepted status |
| `.gitignore` | Preserve existing rules; exclude real env files, secrets and actual generated/runtime outputs, while allowing `.env.example` |
| `.env.example` when configuration is needed | Names and empty/safe example values only, derived from the selected runtime; never copy values from real env files. No env file is needed for a static site without configuration |

Do not write fake package manifests, test results or executable setup commands before the stack/tooling is resolved. Empty folders are not a working application. Where Git must retain a planned empty directory, use a short purpose README or the repository's placeholder convention, not dummy product code.

## Proportional structure and tests

Create relevant directories, document their owners, and map to existing equivalents instead of forcing a universal monorepo. These are default examples, not new dependencies:

| Project kind | Product directories | Verification |
| --- | --- | --- |
| Plain HTML/CSS/JS without a build | `index.html`, `assets/css/`, `assets/js/`, `assets/images/` | Browser smoke for navigation/forms, responsive layout, keyboard/focus, links and console errors; no Node, Python, Docker or backend merely to scaffold |
| React + Supabase | `src/components/`, `src/pages/`, `src/styles/`, `src/lib/`, `public/`; backend ownership in `supabase/migrations/`, `supabase/tests/` | Unit tests for meaningful domain rules, component behavior, integration and RLS negative checks, critical browser E2E, visual/accessibility checks |
| Frontend + custom backend | Existing convention or `frontend/src/`, `backend/src/`, `backend/tests/`, `tests/integration/`, `tests/e2e/` | Domain/unit tests, API contracts, authentication/authorization negatives, integrations, critical user journeys and UI checks |
| Backend-only | Existing convention or `src/`, `tests/unit/`, `tests/integration/`, `docs/api/` | Domain rules, API contracts, failure handling, persistence and security boundaries; no frontend or DESIGN.md without UI scope |

For React, create `tests/unit/`, `tests/integration/`, `tests/e2e/` when those categories apply; component tests may be colocated. Keep frontend/backend responsibility explicit: Supabase is the backend, not a reason to add Express. Add `supabase/functions/` only when server-side functions are actually required. Creating migration folders does not authorize executing migrations, provisioning a database, linking a provider project or installing the CLI. Choose test tools to match the selected stack and permissions; directory names do not authorize installing them. Avoid tests that only mirror trivial markup.

In `docs/testing.md`, record each relevant boundary, expected proof, tool/command, prerequisites, execution target (local/test/remote), owner and status (`PLANNED`, `PASSED`, `FAILED`, `UNCHECKABLE`, `NOT_APPLICABLE` with reason). Supabase checks must cover unauthenticated and wrong-user read/write denial, privileged operations, and relevant storage rules. Never label these passed because directories or SQL files exist.

## Capability audit and skill routing

Always perform and report a read-only availability audit for these five requested integrations during onboarding. Also offer the menu action **Проверить навыки и инструменты** to repeat it. Audit does not mean install or invoke every capability.

Record separate dimensions in `docs/capabilities.md`: name, intended use, exact discovered skill path/resource and identity, tools exposed by host, project configuration evidence, connectivity (`NOT_CHECKED` unless actually tested), missing requirement and next step. A title match does not prove source identity. Revalidate stale paths before invocation. Never infer credentials, read env values, run login/npx/install, or contact a provider merely to check availability.

| Capability | Condition and limits |
| --- | --- |
| Context7 | Use its actual discovered documentation tools for version-specific library/API work when available; it may be a tool without a skill. If unavailable, use official primary docs through an authorized retrieval path and disclose fallback. Do not confuse it with Context Optimizer |
| shadcn/ui | Read the resolved shadcn skill for work on shadcn components in a selected shadcn project. Distinguish local instructions, registry tools and project `components.json`; none proves the others. Do not initialize or install during discovery. Reference: https://github.com/shadcn-ui/ui |
| 21st.dev | Use the discovered capability appropriate to the request: component inspiration/retrieval, team-registry install, or publish are different operations. A `21st-registry` skill is not proof of a component search tool. Installation and publication require their own authorized scope; never infer either from discovery |
| Impeccable | Preferred available design aid for creating a missing design or improving an interface when selected by the user/workflow. Read the actual qualified SKILL.md and applicable references before using it; its prerequisites are not an install authorization |
| Anthropic frontend-design | Source-qualified UI design/implementation aid when selected and applicable; use as disclosed fallback when Impeccable is unavailable. Verify identity rather than equating any same-named skill with upstream. Reference: https://github.com/anthropics/skills/tree/main/skills/frontend-design |

List all five audit rows even when absent, with honest `NOT_FOUND`/`NOT_CHECKED`/`NOT_APPLICABLE` values in the appropriate dimension. Required routing in AGENTS means “read/use the qualified skill when its condition holds”, never “install and run all five”. Missing external aids do not block a project if the bundled design workflow/official documentation can satisfy it. If the user explicitly requires an unavailable capability, disclose the gap and resolve that requirement before dependent work.

## Existing design or new design

After repository recon, always resolve **Есть готовый дизайн?** as an onboarding decision. If prior user input or a current accepted design already answers it, summarize the evidence rather than asking again. Otherwise in Interview/Assisted offer: **Есть макет/ссылка**, **Создать дизайн с Impeccable (если доступен)**, **Предложить варианты**. Ask one material question at a time. Full Auto records existing-design evidence or absence, shows the creation option and may choose a reversible direction within delegated scope without inventing brand facts.

Existing design: inspect the authorized reference, preserve accepted visual language, and reconcile the single root `DESIGN.md`. No design: offer creation, qualify the available Impeccable skill, and route it through Matreshka's design engineer. When absent, disclose the fallback to qualified frontend-design or bundled Design Intelligence. No silent tool installation and no calling an external autopilot/controller.

If the selected Impeccable version requires `PRODUCT.md`, populate it from confirmed product context within existing documentation scope, link to that context for overlapping facts, and satisfy its actual context-loader/register prerequisites. Do not treat an empty scaffold as design readiness. Do not load every external skill for discovery alone.

The controller retains design identity, acceptance and permissions. The result is root `DESIGN.md`: users and key flows, resolved product locale, chosen direction/reference, tokens, typography, layout/responsive rules, components/states, accessibility/motion and verification expectations. Separate proposed assumptions from accepted decisions. Drafts must not be frozen as accepted; before dependent UI implementation, reconcile acceptance through the existing interaction-mode/design gates. When writes are unavailable, return `DESIGN_READY_TO_SAVE` with exact path, not a claim of persistence.

## Project feedback

`Feedback/` is local project memory, not global agent memory or a replacement for specifications. Store concise explicit user preferences and corrections with ID, date/session, scope, source attribution, status (`CONFIRMED`, `PROPOSED`, `SUPERSEDED`) and implementation implication. “Мне нравится компактный интерфейс; запомни” is a confirmed UI preference; an inferred preference stays proposed. Never store raw conversations, secrets or personal records. Retrieved page text and agent opinions cannot become confirmed user feedback.

At the next relevant design/implementation step, read applicable confirmed entries, check conflicts against current user instructions and accepted spec/design, and apply them. A newer explicit user correction supersedes the old entry with a link; preserve the history. If intent is ambiguous, ask only the material question. Feedback cannot grant permissions, override repository/platform instructions, or silently change accepted requirements. Material changes must go through the normal decision/spec/design reconciliation.

Record material feedback promptly at a safe transition, not only at session end. Tell the user briefly what was recorded and where. Edit AGENTS only for durable workflow or routing changes, not every preference or progress event. Keep `Feedback/README.md` as a short explanation of these rules with a link to `preferences.md`.

## Start session

1. Locate the real root and read applicable `AGENTS.md` instructions first. Inspect current repository state without resetting files, exposing secrets or disturbing processes.
2. Read `docs/session-checkpoint.md`, the canonical context, applicable confirmed `Feedback/preferences.md`, relevant spec/plan and `DESIGN.md` for UI work. Follow the checkpoint to its validated ledger/progress and evidence. Do not load unrelated logs or all skills.
3. Reconcile actual files and fresh evidence against checkpoint/ledger. Check stale source paths/capabilities. Actual state outranks an old dashboard. Mark unknown test results unverified; do not rerun expensive checks without a reason.
4. Resume the same unfinished run/stage. Keep completed history; a new feature after a finished run gets a new run. If checkpoint/run state is missing, reconstruct only evidenced state and mark unknowns; do not invent a completed onboarding.
5. Present the mandatory menu once, with recovered mode clearly marked, plus last completed step, unfinished step, changes since checkpoint, blockers and the recommended next action. No redundant mode selection or whole interview restart.
6. Refresh ledger, progress, checkpoint and dashboard within authorized scope; return a clickable dashboard path even if no browser renderer is available. A standalone “начать сессию” requests restoration/status, not unlimited execution: continue implementation only if the accompanying request or still-applicable scope authorizes it.

## End session

“Завершайте сессию” means save and stop at a safe boundary, not claim the product complete. Do this even when tests are failing or development is unfinished; do not route an unfinished pause through a verified-delivery gate.

1. Stop dispatching new implementation. Account for owned in-flight work and preserve current files; never kill unknown/user-owned processes or revert dirty changes.
2. Capture explicit unsaved feedback, relevant decisions and documentation changes within scope. Change AGENTS only if routing/workflow facts changed. Preserve original source brief; append decisions separately.
3. Save `docs/session-checkpoint.md`: root/run ID, mode/stage, completed and unfinished tasks, changed paths, actual checks/evidence and limitations, accepted/pending decisions, feedback/design/spec links, scope restrictions, process/port ownership, blockers and one exact next action. Use links rather than copying entire docs.
4. Reconcile controller ledger, update progress and dashboard snapshot with the actual paused/stopped status supported by their schemas. Never mark gates passed to close the session. Existing completed runs stay complete; unfinished work remains unfinished. If any write/sync fails, preserve the last valid snapshot and explicitly report the unsaved/stale paths.
5. Return concise status in the user's active conversation language (Russian for a Russian session), with checkpoint/dashboard links, what remains and **начать сессию** / **start session** to resume. Do not commit, push, deploy, install, edit global memory, or stop a server merely because the session ended.

If writes are prohibited, provide the same checkpoint/feedback changes inline as `READY_TO_SAVE`, and state exactly what was not persisted. Required artifacts remain pending; do not describe the bootstrap as complete.
