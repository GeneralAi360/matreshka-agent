# Interaction modes

Use this reference to resolve how often the user participates in product and stage decisions. An interaction mode is presentation and decision-delegation policy. It is not an execution profile, controller-autonomy state, or permission grant.

## User-facing mode contract

| Mode | Product questions | Specification and plan gates | Execution start | Ordinary reversible technical choices |
| --- | --- | --- | --- | --- |
| `INTERVIEW` | Ask one material question at a time until the product is sufficiently defined | Require explicit specification and plan confirmation | Require explicit confirmation | Recommend first; wait when the choice materially changes visible behavior, business rules, architecture, or acceptance |
| `ASSISTED` | Ask only material unknowns that read-only inspection cannot resolve | Show plain summaries; do not add a separate gate when the recorded decision delegation covers the stage | Start only inside the existing permission envelope | Choose repository-aligned defaults inside the recorded decision envelope |
| `FULL_AUTO` | Ask only for facts that cannot be safely assumed: business, security, legal, cost, irreversible, or authority facts | The controller may confirm inside delegated local decision scope | Start only inside authorized local scope | Choose the safest reversible local option and record it |

Default to `ASSISTED`.

These are the canonical public names. Do not show `AUTONOMOUS_LOCAL` as an interaction-mode label to ordinary users.

## Compatibility aliases

For compatibility with older Matreshka prompts only:

- legacy `GUIDED` maps to public `INTERVIEW`;
- legacy interaction wording `AUTONOMOUS_LOCAL` maps to public `FULL_AUTO`.

Normalize the alias immediately and announce the canonical public name. Do not preserve the legacy label in new user-facing state or documentation.

This compatibility rule does **not** rename the controller's internal autonomy state. The controller may still use technical states such as `MANAGED`, `AUTONOMOUS_LOCAL`, and `EXTENDED_AUTONOMOUS` internally.

## Resolution rules

1. Prefer one explicit user selection over the default.
2. Treat equivalent plain-language requests such as “interview me first,” “ask only important questions,” or “full auto / decide the local technical details yourself” as a mode signal only when unambiguous.
3. Ask one exact clarification when two explicit mode signals conflict.
4. Resolve and announce the canonical public mode before the first state-changing action.
5. Apply a mid-run change only at the next safe stage boundary.
6. Never replay completed stages because the mode changed.

Use a short announcement in the user's language. Examples:

```text
Mode: Interview — I will ask one important product question at a time, then build after the specification and plan are approved.
```

```text
Mode: Assisted — I will ask only questions that materially change the result, then continue through the approved local workflow.
```

```text
Mode: Full Auto — I will make safe reversible local technical decisions myself and ask only when a fact or authority cannot be assumed.
```

The announcement must not claim authority that has not been granted.

## Controller mapping

| Public interaction mode | Internal controller mapping | Required guardrail |
| --- | --- | --- |
| `INTERVIEW` | `MANAGED` | Keep the product interview plus specification, plan, and execution-start confirmations |
| `ASSISTED` | Usually internal `AUTONOMOUS_LOCAL` only after the controller records a bounded permission and decision envelope | Keep material product questions available |
| `FULL_AUTO` | Internal `AUTONOMOUS_LOCAL` with broader delegation for ordinary reversible local choices | Never infer `EXTENDED_AUTONOMOUS` |

The controller independently selects maximum speed, balanced, or maximum quality. A mode never selects or downgrades that profile. High-risk work cannot use maximum speed merely because the user wants fewer questions.

## INTERVIEW behavior

The interview is not a fixed questionnaire. Ask one question at a time and stop when the product is sufficiently defined for a trustworthy specification.

Ask only questions whose answers materially affect at least one of:

- user-visible behavior or acceptance;
- business rules or actors;
- data ownership or lifecycle;
- security/privacy boundary;
- external provider/cost/legal commitment;
- hard-to-reverse architecture;
- scope inclusion/exclusion.

Recommend a default with the question when a safe recommendation is possible. Inspect repository facts instead of asking for them. Do not manufacture questions to reach a target count.

## FULL_AUTO behavior

`FULL_AUTO` means **maximum decision delegation inside the already-authorized local scope**, not unlimited authority.

The skill may decide reversible technical details such as local structure, naming, repository-aligned libraries already present, test organization, and other implementation choices when current evidence supports them.

It must still ask or stop for facts that cannot be invented, including prices, policies, legal terms, customer data, provider accounts, production configuration, security-sensitive product rules, or new authority.

## Authority firewall

None of the three modes grants:

- broader filesystem access;
- dependency, package, provider, or network use;
- secrets;
- Git or worktree actions;
- messages, payments, webhooks, or remote database actions;
- deploy, publish, production configuration, migration application, deletion, or cleanup.

Pass only the authority the user actually expressed, subject to higher-priority repository, host, sandbox, and approval policy. Keep absent authority explicitly absent.

## Business-truth rule

Do not fill missing prices, policies, legal terms, accounts, credentials, customer data, provider entitlements, production URLs, or billing behavior with invented values.

- Use `NEEDS_CONTEXT` when the fact blocks safe specification or acceptance.
- Use an explicit documentation placeholder when later confirmation is valid.
- Use a local fake or adapter only when local implementation is authorized and the real provider is outside scope.
- Keep the final result below `COMPLETE` when an acceptance-critical placeholder remains.

## Decision-map boundary

Use `SPLIT_REQUIRED` plus `DECISION_MAP_REQUIRED` when one trustworthy specification cannot contain the destination. The decision map records the destination, confirmed and open decisions, dependency edges, the next decision, and the return condition. It does not authorize implementation or create external work items.
