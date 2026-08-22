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

## Conversation language vs product UI language

Matreshka's user-facing narration/dashboard language and the product's interface language are separate dimensions.

Use:

```text
CONVERSATION_LANGUAGE = language used to talk to the user and explain the run
PRODUCT_UI_LOCALE = language/locale used by the product interface itself
```

Rules:

1. Never infer `PRODUCT_UI_LOCALE` only because the conversation is in that language.
2. Reuse an established existing product locale/content convention when repository evidence is clear and the requested change does not challenge it.
3. In `INTERVIEW` or `ASSISTED`, if a new UI needs meaningful product copy and `PRODUCT_UI_LOCALE` is not explicit or established, ask one material language question before comparison prototypes or production UI copy are authored.
4. Do not silently default a new product to English because examples/framework defaults are English.
5. In `FULL_AUTO`, prefer an established repository locale. A brand-new product with no locale evidence may use only an explicitly recorded provisional reversible assumption; it must not become invisible product truth.
6. Product prototype copy follows `PRODUCT_UI_LOCALE`; test chrome, Matreshka status labels and explanations may follow `CONVERSATION_LANGUAGE`.
7. Pass the resolved locale/assumption into source decisions/design context so specification, design, implementation and visual verification use the same product language.

Language choice is material when it changes actual interface copy, terminology, layout/wrapping, date/number formatting, accessibility labels or acceptance. Do not ask it for backend-only work with no user-visible text.

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
- product UI language/locale when user-visible copy is required;
- business rules or actors;
- data ownership or lifecycle;
- security/privacy boundary;
- external provider/cost/legal commitment;
- hard-to-reverse architecture;
- scope inclusion/exclusion.

Recommend a default with the question when a safe recommendation is possible. Inspect repository facts instead of asking for them. Do not manufacture questions to reach a target count.

## ASSISTED behavior

Ask only material unknowns that cannot be safely resolved by inspection/current decisions. A new product's interface language is one of those material unknowns when real UI copy/prototypes are about to be authored and no locale evidence exists.

If the user says they do not know the visual style, prefer bounded visual exploration after the product UI locale and other acceptance-critical facts are resolved rather than a long taste questionnaire.

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
