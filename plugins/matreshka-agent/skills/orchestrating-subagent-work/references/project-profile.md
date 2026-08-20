# Project profile and skill-source preflight

Use a project profile to avoid rediscovering stable local facts, not to create a general memory system. Read or refresh it only for the current project and only after comparing it with current repository state.

Read [project-intelligence.md](project-intelligence.md) during controller preflight before building or reusing topology, area context, interfaces, runtime facts, documentation-impact state, or specialist routing. Project Intelligence applies even when no reusable profile is persisted.

When the current outcome creates or changes a material user-facing interface, also read [design-intelligence.md](design-intelligence.md) during preflight. Design Intelligence classifies design relevance, routes the source-qualified `designing-product-experience` skill, enforces root `DESIGN.md`, design identity/context, review/visual evidence, and design drift. It is separate from Project Intelligence and from permissions.

## Discover before trusting

During read-only preflight, inspect existing repository instructions, package/workspace scripts, CI configuration, test layout, Git state, host capabilities, architecture boundaries, entry points, runtime commands, and relevant existing documentation.

Build the smallest current `PROJECT_TOPOLOGY` and `RUNTIME_MAP` needed for the run. Do not assume frontend/backend, monorepo, browser, deployment, database, or service boundaries without evidence.

For UI-relevant work, also inspect root `DESIGN.md` when present and only the current token/component/layout/accessibility/motion sources needed to classify `DESIGN_CURRENT`, `DESIGN_RECON_REQUIRED`, `DESIGN_DIRECTION_REQUIRED`, or `DESIGN_BLOCKED`. Do not redesign an existing product merely because Design Intelligence is available.

An existing profile, context index, architecture guide, area document, runtime guide, design document, screenshot, or prototype is only a candidate. Reconfirm its project root, baseline/profile-input identity, area roots, entry points, command availability, interface ownership, runtime ownership, relevant design identity/pattern sources, sensitive boundaries, and expiry. Mark the conflicting subset `STALE`; current evidence and valid design/user authority must be reconciled rather than averaged.

Never use a profile or design artifact to widen paths, permissions, commands, network access, browser/process authority, secret access, Git, provider, database, deploy, migration, destructive, or remote authority.

## Create only with authority

Reuse a compatible repository-required project-profile path when one exists. Otherwise prefer the internal project-local cache:

```text
.matreshka/project-profile.md
```

Create or refresh it only when the exact project-profile state path is inside the Matreshka state-write envelope. It is not committed by default. If no profile write is authorized, keep the validated facts inline or in the current authorized run state.

Use [the profile template](../assets/project-profile-template.md). Keep only durable, reusable, validated facts:

- real project root and relevant repository instructions;
- project topology summary and area context index;
- existing package manager/workspaces and known command names, without environment values;
- focused test, typecheck, lint, build, E2E, and security-check candidates with their source;
- runtime units, ownership/status/log seams, and permission requirements;
- language/framework facts that affect execution;
- durable public/cross-area interface-doc locations when they actually exist;
- for UI-bearing projects, only a compact pointer to root `DESIGN.md`, current design identity, validated design-system/token/component source locations, and refresh condition — never the whole design document or prototype set;
- sensitive boundaries such as auth, isolation, migrations, secrets, persistence, providers, and production configuration;
- current profile-input identity, owner/reviewer, review date, and refresh condition.

Do not copy raw logs, issue text, personal data, credentials, environment-file contents, private URLs, broad file inventories, hidden reasoning, transient task status, stale agent reports, raw screenshots, brand assets, full prototype variants, or unverified claims. A profile is not loaded globally and is never authoritative over current repository evidence or valid design/user authority.

## Route task context through current areas and design

For every controller-dispatched task, derive the `AREA_CONTEXT_SET` from the current topology rather than copying the whole profile. Include only the primary area, required neighboring interface contracts/invariants, scoped commands/paths, and task-local security/data/runtime facts.

For UI-affecting tasks, derive a separate narrow `DESIGN_CONTEXT_SET` from the current design identity. Include only the relevant layout/component/token/state/responsive/accessibility/motion invariants for that task. Backend-only tasks normally receive no design payload.

If a reusable profile names an area, interface, runtime fact, design identity, or design source that no longer matches the repository/current accepted design, rebuild that subset before dispatch. Do not let a cached context index hide a current dependency or design change.

## Resolve skill sources explicitly

Before chaining a Matreshka skill, create a compact `SKILL_SOURCE_MAP` in the ledger:

| Needed role | Matreshka skill | Host-visible invocation | Source evidence | Result |
| --- | --- | --- | --- | --- |
| root cause | `debugging-systematically` | `<namespace or picker entry>` | `<plugin/source>` | `<selected/fallback/handoff>` |
| product experience | `designing-product-experience` | `<namespace or picker entry>` | `<plugin/source>` | `<selected/fallback/handoff>` |

On a namespaced host, use `matreshka-agent:<skill-name>`. On another host, record the plugin source shown by the host. A matching title, icon, description, automatic suggestion, or specialist role label is not evidence of ownership.

Specialist routing from Project/Design Intelligence still invokes the applicable existing Matreshka skill. For example, `FRONTEND_IMPLEMENTER`, `BACKEND_IMPLEMENTER`, `DESIGN_ENGINEER`, and `DESIGN_REVIEWER` are scoped role archetypes, not permission or automatic extra-agent grants.

If source identity cannot be verified, do not substitute another package. Use only the documented inline fallback with unchanged permissions, or return `HANDOFF_REQUIRED`.
