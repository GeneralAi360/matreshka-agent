# Design Prototype Exploration

Use this reference only when a material UX/UI direction is unresolved and seeing alternatives is more reliable than asking the user to describe taste abstractly.

The goal is divergence followed by an explicit selection, not permanent prototype infrastructure.

Read `anti-slop.md` before creating comparison directions. Prototype exploration is an early design gate, so generic AI templates should be removed before the user is asked to choose among them.

## When to prototype

Use prototype exploration when one or more are true:

- a new UI-bearing product has no established visual/interaction direction;
- the user explicitly says they do not know what style/layout they want;
- a major redesign has multiple credible interaction/hierarchy models;
- one decision will propagate across many screens/components and is expensive to discover late.

Do not prototype when:

- `DESIGN.md` already covers the pattern and no material design decision changed;
- the task is a small implementation inside an established component/system;
- the question is backend/data-only;
- prototype infrastructure would cost more than the design uncertainty warrants.

## Resolve product UI locale first

Product copy inside prototypes must use the resolved `PRODUCT_UI_LOCALE`.

- Conversation language is not automatically product UI language.
- In `INTERVIEW`/`ASSISTED`, when a new product has meaningful interface copy and no explicit/repository-established locale, ask one material language question before generating directions.
- Direction names, explanation, and neutral picker/test chrome may use the conversation language.
- Use realistic localized copy lengths, date/number conventions and labels when those influence layout.

A prototype with English product copy is not acceptable merely because the coding examples were easier in English when the product locale was never resolved.

## Direction count

Default to **3** directions. Allow 2 for a narrow binary decision or up to 5 only when the design space is genuinely broad.

Every direction must have:

```text
name
axis
product-specific signature
what changes
what remains invariant
when this direction wins
its main cost/tradeoff
anti-slop defaults deliberately avoided
```

Names describe the design direction: `Calm`, `Dense`, `Editorial`, `Direct`, `Playful`, `Focused`, etc. Never use `Option A/B/C` as the only distinction.

## Real divergence

Valid axes include:

- navigation/layout model;
- information density;
- hierarchy/type scale;
- surface/depth strategy;
- interaction/disclosure model;
- motion personality;
- touch/desktop workflow emphasis.

Invalid fake divergence:

- same layout with three accent colors;
- same card with 8px/10px/12px radius;
- copy changes with no structural/interaction difference;
- variants whose only distinction is an arbitrary font swap;
- three known generic templates recolored as if they were product-specific directions.

If two variants converge, merge/drop one rather than padding the set.

## Recon before variants

Use current project evidence:

- stack/styling method;
- existing product UI locale/terminology;
- existing tokens;
- shared components;
- app shell/context;
- product personality;
- target screen sizes/input modes;
- accessibility and motion constraints.

Existing confirmed design rules remain invariants unless the exploration explicitly challenges them through valid design authority.

## Run-state before prototype writes

In a controller-managed Build End-to-End run, prototype creation is a state-changing action.

When durable Matreshka run-state writes are authorized, require the controller-owned run ledger/state to exist **before** writing prototype files. Record at minimum:

- run identity;
- current `DESIGN_DIRECTION_REQUIRED` state;
- exact permission/prototype-write scope;
- current Project/Design Intelligence state;
- exact next action.

When run-observability/dashboard projection is enabled for the run, initialize its `stageOrder`/`stateIntegrity` projection before or together with the first prototype write rather than creating prototypes first and reconstructing state later.

If durable run state was explicitly required but cannot be initialized safely, return the exact controller handoff/blocker instead of silently proceeding with untracked design writes.

## Prototype isolation

Prototype writes are not production feature implementation.

Preferred order:

1. **run-local static prototype** under an authorized Matreshka run-state/design path when sufficient for the decision;
2. **isolated project prototype route/surface** only when fidelity requires real project components and exact temporary write scope is authorized;
3. **inline design specification** when no safe prototype write/browser capability exists.

A useful default internal path when state writes are authorized:

```text
.matreshka/runs/<run-id>/design/prototypes/
```

Do not commit it by default.

A project route such as `/prototypes/<slug>` must be clearly isolated from production navigation/data and removed after selection unless the user explicitly asks to keep it.

Never infer permission for:

- dependency installation;
- network/browser download;
- local server/process start;
- port binding;
- browser launch;
- secrets/test credentials;
- Git actions.

## Prototype fidelity

Each direction should be complete enough to judge the decision:

- realistic surrounding context;
- realistic product-shaped content in the resolved UI locale without private data;
- working primary interaction when that interaction differentiates the direction;
- representative loading/empty/error only when those states matter to the decision;
- proper reduced-motion/accessibility basics when motion is part of the comparison;
- representative layered-control open states when a select/menu/popover/date-picker pattern materially affects the design language.

Do not build an entire product to choose a navigation/card direction.

### Layered/open control fidelity

A select/menu/popover/dropdown is not judged only by its closed trigger.

When such a control appears in a presented direction, verify at least one realistic open/expanded state when browser capability exists. Check visual coherence, width, clipping, collision, portal/z-index, selected/focus state, scrolling, keyboard behavior and mobile/touch suitability.

A native platform control is valid when native appearance is deliberately part of the direction. It is not acceptable as an accidental style break inside an otherwise custom-art-directed interface.

Do not make static prototype controls look live if they cannot actually respond. Dead controls are prototype defects.

## Picker behavior

When a browser-rendered comparison is possible, use a small neutral picker that is clearly test chrome, not product UI.

Requirements:

- one variant displayed at full realistic scale at a time;
- buttons/number keys `1..N` and left/right arrows switch instantly;
- a visible direction name and optional one-line axis description;
- picker does not inherit brand styling that could bias the comparison;
- picker never covers the design area being judged; move it top/bottom only as needed;
- replay control only when motion comparison requires it;
- switching variants itself is instant because it is a very high-frequency test action;
- the selected variant may persist locally in URL/query/state for reload convenience when safe.

Do not compare postage-stamp screenshots side by side when scale, spacing or interaction matters.

## Anti-slop verification before user choice

Before presenting:

- every direction renders;
- differentiating interactions work;
- no obvious console/runtime error in the prototype path when observable;
- product copy uses resolved `PRODUCT_UI_LOCALE`;
- direction axes are still genuinely distinct;
- each direction names a product-specific signature;
- known generic AI layout/palette/component defaults were challenged rather than accepted automatically;
- key open states for layered controls were checked when materially present;
- content remains visible without entrance-animation completion;
- no obvious clipping, contrast, centering, edge-gutter, horizontal-overflow, focus, dead-control, or overlay-layering defect remains;
- none violates confirmed security/source-intent/accessibility constraints merely to look different.

If a direction still reads primarily as a reusable cream editorial template, cool-blue SaaS dashboard, gray/purple component-kit dashboard, or other generic composition without product-specific reason, redesign it before presenting.

When browser evidence is available, capture at most one representative screenshot per direction unless more is required to explain a responsive/interaction/open-state difference.

## Handoff to user

Present one compact table:

| Direction | Signature / axis | Best when | Main cost |
| --- | --- | --- | --- |
| Calm | restrained information model | trust/readability matter | lower information density |
| Dense | compact data-first organization | expert daily workflow | visually busier |
| Timeline | sequence-first interaction | chronology is the user's mental model | less summary-first |

Do not silently select a winner in `INTERVIEW`/`ASSISTED` when the user is explicitly comparing directions. If asked for a recommendation, give one grounded in product personality/frequency, but keep the choice explicit.

In `FULL_AUTO`, the controller may choose a restrained direction only when the decision is reversible and not a missing brand/business truth. Record the selected direction and rationale.

## Promotion

After a direction is selected:

1. record selected direction/prototype identity;
2. translate the winning rules, product UI locale/terminology and anti-slop invariants into root `DESIGN.md`;
3. compute/record design identity;
4. remove/retire unselected prototype surfaces when cleanup is authorized;
5. route production implementation through the normal plan/task/RED-GREEN/review/verify workflow;
6. do not copy prototype shortcuts that violate production architecture/accessibility/security;
7. preserve open-state primitive requirements for production design review/visual verification.

Prototype success is design evidence, not production verification.
