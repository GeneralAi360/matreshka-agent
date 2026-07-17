# Coding-Agent Platform Adapters

Load only the section for the named target host. Verify behavior against the active version when a mechanic is essential.

## Portable default

When the host is unknown:

- omit slash commands and tool-call syntax;
- use capability language such as “start an isolated subagent” and “resume the same thread”;
- require the executing agent to read applicable project instructions;
- state that native sandbox and approvals remain authoritative;
- list any required capability that must be confirmed before execution.

Do not name a model. Describe fast/economical, standard, or high-judgment capability needs.

## Codex

For a controller prompt that delegates roles:

- request a fresh subagent context with `fork_turns: "none"`;
- require the controller to save returned agent IDs;
- require fixes and rechecks to use follow-up on those same IDs;
- forbid child agents;
- use technical tool restrictions for read-only reviewers when available;
- keep native approval and sandbox behavior authoritative.

Do not hard-code an individual model name in the portable contract. Map the requested capability tier at runtime.

For a simple single-agent implementation prompt, omit subagent mechanics entirely.

## Claude Code

- Tell the agent to read applicable project instructions and use isolated subagents only when the task actually calls for roles.
- Restrict role tools explicitly when the host supports it.
- Preserve and resume the same agent identifier for a follow-up when supported by the active host.
- Treat plugin metadata as discovery/UI configuration, not as proof of effective write restrictions.
- Keep native permission prompts authoritative.

Do not include a plugin slash command inside an execution prompt unless the user explicitly asked for a command they will type.

## Cursor

- Tell the agent to read project rules and inspect the real workspace boundary.
- Preserve agent IDs for same-thread follow-up when subagents are used.
- Request read-only reviewer mode when available and verify no mutation occurred.
- Forbid nested subagents and concurrent writers even if the host can technically create them.
- Avoid assuming that background context contains the drafting conversation.

## Antigravity

- Write the canonical task contract without invented CLI flags or model identifiers.
- Ask the executing agent to detect the installed host capabilities before selecting a subagent profile.
- Require declared degraded or handoff behavior when same-thread resume or safe reviewer isolation is unavailable.
- Use registered skill/slash syntax only when the user explicitly requests a launch command and the installed version has been verified.

## Adapter decision table

| Requirement | Verified capability | Prompt behavior |
| --- | --- | --- |
| Independent implementation/review | Isolated subagents and safe read-only review | Include bounded roles and handoff contracts |
| Same-role fix/recheck | Stable thread resume | Require reuse of saved IDs |
| Same-role fix/recheck | Resume unknown or absent | Require capability preflight; degrade or hand off by risk |
| Read-only review | Technical restriction absent | Require immutable package or isolated checkout; state procedural limitation |
| Role capability tier | Routing unavailable | Use best permitted tier and report the variance |
| Usage reporting | Counters unavailable | Report turns and elapsed time; never fabricate token totals |

Keep adapter text shorter than the canonical contract. If removing the adapter leaves the task semantically incomplete, host mechanics have leaked into the task definition and should be refactored.
