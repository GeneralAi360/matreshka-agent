# Interaction modes

Use this reference to resolve how often the user participates in product and stage decisions. An interaction mode is presentation and decision-delegation policy. It is not an execution profile or a permission grant.

## Mode contract

| Mode | Product questions | Specification and plan gates | Execution start | Ordinary reversible technical choices |
| --- | --- | --- | --- | --- |
| `GUIDED` | Ask one material question at a time until the result is sufficiently defined | Require explicit specification and plan confirmation | Require explicit confirmation | Recommend first; wait when the choice changes behavior or architecture |
| `ASSISTED` | Ask only material unknowns that read-only inspection cannot resolve | Show plain summaries; do not add a separate gate when the recorded decision delegation covers the stage | Start only inside the existing permission envelope | Choose repository-aligned defaults inside the recorded decision envelope |
| `AUTONOMOUS_LOCAL` | Ask only for unassumable business, security, legal, cost, irreversible, or authority facts | The controller may confirm inside delegated local decision scope | Start only inside authorized local scope | Choose the safest reversible local option and record it |

Default to `ASSISTED`.

## Resolution rules

1. Prefer one explicit user selection over the default.
2. Treat equivalent plain-language requests such as “guide me at every stage,” “ask only important questions,” or “work locally without unnecessary questions” as a mode signal only when unambiguous.
3. Ask one exact clarification when two explicit signals conflict.
4. Resolve and announce the mode before the first state-changing action.
5. Apply a mid-run change only at the next safe stage boundary.
6. Never replay completed stages because the mode changed.

Use a short announcement in the user's language. For example:

```text
Mode: Assisted — I will ask only questions that materially change the result, then use the approved local workflow end to end.
```

The announcement must not claim authority that has not been granted.

## Controller mapping

| Interaction mode | Controller mapping | Required guardrail |
| --- | --- | --- |
| `GUIDED` | `MANAGED` | Keep specification, plan, and execution-start confirmations |
| `ASSISTED` | Usually `AUTONOMOUS_LOCAL` only after the controller records a bounded permission and decision envelope | Keep material product questions available |
| `AUTONOMOUS_LOCAL` | `AUTONOMOUS_LOCAL` with broader delegation for ordinary reversible local choices | Never infer `EXTENDED_AUTONOMOUS` |

The controller independently selects maximum speed, balanced, or maximum quality. A mode never selects or downgrades that profile. High-risk work cannot use maximum speed merely because the user wants fewer questions.

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
