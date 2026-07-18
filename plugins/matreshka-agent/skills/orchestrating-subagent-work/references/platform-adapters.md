# Platform Adapters

Keep the controller contract portable. Detect host behavior at runtime and use only capabilities that are actually available.

## Common adapter contract

For every host:

1. Start role contexts without inheriting the controller conversation when supported.
2. Capture the stable agent or thread identifier returned by the host.
3. Use a follow-up or resume operation on that same identifier for fixes and rechecks.
4. Restrict reviewer tools to read-only when supported.
5. Record whether restrictions are technical or prompt-only.
6. Prevent child-agent creation through role instructions and tool restriction when available.
7. Permit only one writer in a checkout at a time.
8. Record capability and reasoning tiers rather than portable model names.
9. Respect host-native approval, sandbox, and organization controls.

Never infer a capability from platform branding alone. Versions, policies, and host applications can differ.

## Bundled-skill identity

The controller may chain only the nine skills bundled with the active Matreshka plugin. Before chaining a skill, confirm its package identity; a matching title, trigger description, or output style is not proof of ownership.

| Host behavior | Required routing rule |
| --- | --- |
| Plugin namespace is visible | Invoke `matreshka-agent:<skill-name>`. For root-cause work, use `matreshka-agent:debugging-systematically`. |
| Plugin source is shown in a picker | Choose the entry sourced from Matreshka Agent, then confirm the exact skill name. |
| Source/namespace cannot be inspected | Do not choose a similarly named external skill. Follow the relevant Matreshka protocol inline only when its permissions and scope are unchanged; otherwise return `HANDOFF_REQUIRED`. |

This rule applies equally to automatic skill suggestions. An automatic suggestion is an input to verify, not authority to replace a bundled skill.

## Codex adapter

- Use a fresh subagent dispatch with `fork_turns: "none"`.
- Save the returned agent ID in the ledger.
- Send corrections and rechecks through follow-up to that ID.
- Use role/tool restrictions for read-only work when exposed; otherwise use an immutable package or isolated checkout and declare the guarantee level.
- Treat the controller's sandbox and approval restrictions as inherited constraints, not permissions that a prompt can widen.
- Use capability tiers in the portable plan; map them to available model/reasoning settings only at dispatch time.
- When chaining a Matreshka skill, select its `matreshka-agent:` namespace explicitly. Do not accept an unqualified debugging suggestion as equivalent.

## Claude Code adapter

- Start isolated subagents with the narrowest applicable tool set.
- Preserve the returned agent identifier and resume the same agent for its follow-up turn when supported by the active version.
- Do not rely on plugin-agent permission metadata as the sole enforcement mechanism; verify effective tools and host approvals.
- Invoke bundled skills through the host's namespaced plugin command when a user launches them manually.
- Keep the same namespaced identity when the controller chains a bundled skill.

## Cursor adapter

- Start subagents with narrow context and preserve their agent IDs for resume.
- Apply host read-only configuration for reviewers when available and verify that no file mutation occurred.
- Do not use nested subagents even if the host supports them.
- Keep project rules and current task scope explicit because background agents may operate in separate contexts.
- If several skills share a title, select only the entry whose source is Matreshka Agent; otherwise use the common fallback rule.

## Antigravity adapter

- Detect the installed CLI or host version and inspect available subagent, resume, and permission controls before promising a profile.
- Use the host's registered skill command for manual invocation.
- If same-thread resume or safe reviewer isolation cannot be verified, declare `DEGRADED_MODE` or `HANDOFF_REQUIRED` according to risk.
- Do not invent command flags, model identifiers, or aliases that were not verified in the active environment.
- If the skill picker does not expose source identity, do not treat a matching title as a bundled Matreshka skill.

## Capability fallback table

| Missing capability | Low-risk response | High-risk response |
| --- | --- | --- |
| Subagents | `INLINE_MODE` with checkpoints | `HANDOFF_REQUIRED` if independent roles are essential |
| Same-thread resume | Declared degraded fix/controller verification | `HANDOFF_REQUIRED` for balanced security or maximum quality |
| Technical reviewer read-only | Immutable package or isolated checkout; otherwise declared procedural restriction | `HANDOFF_REQUIRED` when neither safe alternative exists |
| Worktree isolation | Continue in approved current checkout if ownership is clear | Pause on dirty overlap or unsafe host-managed state |
| Role model routing | Use best permitted tier and record variance | `HANDOFF_REQUIRED` if critical judgment is unavailable |
| Usage counters | Report turns and elapsed time only | Continue; never fabricate token totals |

Do not silently replace a missing guarantee with a fresh agent, broader permission, or an unverified tool claim.
