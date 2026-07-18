# Project profile and skill-source preflight

Use a project profile to avoid rediscovering stable local facts, not to create a general memory system. Read or refresh it only for the current project and only after comparing it with current repository state.

## Discover before trusting

During read-only preflight, inspect existing repository instructions, package scripts, CI configuration, test layout, Git state, and host capabilities. Then decide whether a profile is useful.

An existing profile is only a candidate. Reconfirm its project root, baseline or profile-input hash, command availability, sensitive boundaries, and expiry. Discard or mark stale facts that no longer match. Never use a profile to widen paths, permissions, commands, network access, or remote authority.

## Create only with authority

Create or refresh `docs/matreshka/project-profile.md` only when Matreshka state writes are inside the permission envelope. Otherwise return the proposed profile inline or in an approved run artifact.

Use [the profile template](../assets/project-profile-template.md). Keep only durable, task-relevant facts:

- real project root and relevant repository instructions;
- existing package manager and known command names, without values from environment files;
- focused test, typecheck, lint, build, and security-check candidates with their source;
- language/framework facts that affect the current task;
- sensitive boundaries such as auth, isolation, migrations, secrets, persistence, and production configuration;
- current profile-input identity, owner, review date, and expiry.

Do not copy raw logs, issue text, personal data, credentials, private URLs, broad file inventories, hidden reasoning, or unverified claims. A profile is not loaded globally and is not authoritative over current repository evidence.

## Resolve skill sources explicitly

Before chaining a Matreshka skill, create a compact `SKILL_SOURCE_MAP` in the ledger:

| Needed role | Matreshka skill | Host-visible invocation | Source evidence | Result |
| --- | --- | --- | --- | --- |
| root cause | `debugging-systematically` | `<namespace or picker entry>` | `<plugin/source>` | `<selected/fallback/handoff>` |

On a namespaced host, use `matreshka-agent:<skill-name>`. On another host, record the plugin source shown by the host. A matching title, icon, description, or automatic suggestion is not evidence of ownership.

If source identity cannot be verified, do not substitute another package. Use only the documented inline fallback with unchanged permissions, or return `HANDOFF_REQUIRED`.
