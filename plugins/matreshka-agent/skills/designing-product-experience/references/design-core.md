# Matreshka Design Core

Use this reference whenever a user-facing interface is designed, reconciled, reviewed, or visually accepted. These principles are the default quality core for Matreshka Design Intelligence. They are not a style preset and do not grant implementation or tool authority.

## The eight mandatory principles

### 1. Purpose

Every screen, control, message and animation must have a reason tied to the user's task. Remove decorative complexity that does not improve comprehension, feedback, orientation, confidence, safety, or delight at an appropriate frequency.

Ask:

- What job is this element doing?
- What would break if it disappeared?
- Is the user's attention worth spending here?

### 2. Agency

Keep users in control.

- obvious escape/back/close paths;
- undo where practical for reversible mistakes;
- confirmation only for genuinely consequential or irreversible actions;
- avoid forced flows when a safe choice can remain with the user;
- do not lock input merely because an animation is running.

### 3. Responsibility

Design in the user's interest.

- request sensitive data/permissions only when needed and at the right moment;
- make destructive consequences clear;
- use honest status/error/success feedback;
- do not disguise failures as success;
- security/privacy/accessibility requirements outrank visual polish.

### 4. Familiarity

Use patterns people already understand unless a tested improvement justifies change.

- same-looking controls behave the same;
- repeated actions live in predictable places;
- platform-native expectations matter;
- spatial relationships should remain understandable across state changes.

Familiarity does not mean copying another product's appearance.

### 5. Flexibility

Design for context, device, input method and ability.

- responsive layouts adapt, not merely shrink;
- pointer, keyboard and touch are different interaction contexts;
- text scaling and localization should not break structure;
- dense expert workflows and simple common paths may need different disclosure levels;
- accessibility is part of the main flow.

### 6. Simplicity

Simplicity is clarity, not visual emptiness.

- show the common path first;
- use hierarchy to make the next action obvious;
- keep advanced detail available without overwhelming the default path;
- use direct language and specific labels;
- add context when it reduces uncertainty.

### 7. Craft

Small decisions compound.

- typography, spacing, alignment, radii, color, shadows, icon sizing and motion use coherent systems;
- default states are polished, not merely acceptable;
- loading/error/empty/disabled/focus/hover/active states are designed, not forgotten;
- inconsistent one-off values are drift unless explicitly approved;
- performance and responsiveness are part of perceived quality.

### 8. Delight

Delight is the result of purpose, agency, responsibility, familiarity, flexibility, simplicity and craft working together.

Do not bolt confetti, bounce, gradients or dramatic motion onto ordinary tasks as a substitute for a coherent product. Reserve expressive moments for rare/high-emotion contexts when they reinforce the product personality.

## UX foundations

### Wayfinding

Every material screen should make four things understandable:

1. Where am I?
2. What can I do here?
3. Where can I go next?
4. How do I get out/back?

A screen that is visually attractive but disorients the user is not design-complete.

### Grouping and mapping

- proximity implies relationship;
- controls should sit near the content/result they affect;
- structure should visually map to the user's mental model;
- avoid forcing users to infer which control acts on which region.

### Labels

Prefer specific, predictable labels over vague containers. Name navigation for its actual destination/content. Use plain language and repository/product terminology consistently.

### Feedback taxonomy

Design distinct feedback for:

- status/progress;
- completion/success;
- warning/risk;
- error/recovery.

Use inline validation when the problem can be detected before submit. Do not wait until the end of a form to reveal every preventable error.

## Response and direct manipulation

Interfaces should acknowledge input immediately.

- press feedback begins on press/pointer-down when appropriate;
- drag/gesture feedback tracks continuously rather than jumping only at release;
- gestures should be interruptible and redirectable;
- preserve velocity/continuity for physical interactions where the platform supports it;
- avoid artificial delays on the critical input path.

For gesture-driven interfaces, current on-screen state is the starting point for interruption. Do not teleport an element back to its logical start because a new gesture arrived mid-animation.

## Spatial consistency

- anchored surfaces should appear/disappear from a spatially understandable source;
- reversible transitions should preserve direction/identity;
- a panel entering from one edge should not randomly exit through another;
- trigger-attached popovers should feel attached to their trigger;
- modals are centered surfaces and need not pretend to originate from a button.

## Typography core

Typography is a system, not a collection of font sizes.

Define and reuse:

- family/fallback strategy;
- display/heading/body/label/caption hierarchy;
- size + weight + line-height as a set;
- tracking appropriate to size;
- readable measure and responsive scaling;
- tabular numerals where changing numbers must not shift layout.

Large headings usually need tighter leading/tracking than body text. Small text needs enough line-height and contrast to remain legible.

## Layout and density

Define:

- page/app shell;
- primary navigation;
- container/grid strategy;
- spacing scale;
- content density;
- page-header pattern;
- list/table/form/detail patterns;
- breakpoint behavior.

A professional dashboard may be intentionally denser than a marketing page. Consistency means coherent rules, not identical whitespace everywhere.

## Components and states

A reusable component pattern is incomplete without its relevant states:

- default;
- hover where pointer applies;
- active/pressed;
- focus-visible;
- disabled;
- loading;
- error;
- success;
- empty where the component owns content;
- destructive/confirmation state when applicable.

Do not create a visually new button/input/card/modal pattern for one screen when the design contract already defines the concept.

## Motion decision framework

Before motion, answer in order:

1. **Frequency** — the more often users see the interaction, the less motion it should carry. Keyboard/high-frequency actions usually need none.
2. **Purpose** — feedback, spatial continuity, state indication, explanation, or preventing a jarring change. “Looks cool” is not enough for routine UI.
3. **Responsiveness** — ordinary UI transitions should feel immediate and commonly stay below roughly 300ms. Rare explanatory/marketing moments can be longer.
4. **Function** — if motion makes information harder to read or slows an expert workflow, remove/reduce it.

### Recommended defaults

Reuse project tokens first. If the project has no equivalent and a new canonical motion token is justified, safe starting points include:

```text
enter/exit: strong ease-out
on-screen movement/morph: ease-in-out
hover/color: simple responsive easing
constant progress/marquee: linear
press feedback: subtle scale around 0.97, roughly 100–160ms
small popover/tooltip: roughly 125–200ms
select/dropdown: roughly 150–250ms
```

Avoid:

- `ease-in` for ordinary responsive UI entrances;
- `transition: all`;
- `scale(0)` entrances;
- animation on every keyboard-triggered/high-frequency action;
- decorative motion on data the user is trying to read;
- slow motion that blocks interaction.

### Physicality and interruption

- use origin-aware motion for trigger-attached UI;
- rapidly retriggered/reversible UI should use transitions/springs that retarget from current state rather than restarting fixed keyframes;
- gesture-driven motion may use springs/velocity when that preserves physical continuity;
- visible bounce should be rare and motivated by momentum/personality.

### Performance

Prefer compositor-friendly `transform` and `opacity` for continuous motion. Avoid repeatedly animating layout-heavy properties when a transform can express the same result. Treat dropped frames as a design defect.

### Reduced motion

Reduced motion is a first-class state. Replace movement/parallax/overshoot with gentler opacity/color/static transitions where they still communicate state. Do not simply remove all feedback.

## Materials and depth

Depth communicates hierarchy; it is not a decorative checklist.

- borders, shadows, translucency and blur must fit the product personality and readability needs;
- floating surfaces need enough separation from content beneath them;
- large surfaces may require stronger depth cues than small chips;
- do not stack translucent layers until text loses legibility;
- a crisp business dashboard may use very little translucency; a media/creative product may justify more.

Do not add glass effects simply because Apple-inspired principles are active.

## Platform adaptation

The core is intentionally platform-neutral.

### Web/desktop

- keyboard/focus are first-class;
- hover only where the input device supports hover;
- dense workflows can prioritize speed over decorative transitions.

### Touch/mobile

- no hover dependency;
- touch targets must remain comfortably tappable;
- press feedback replaces hover affordance;
- gestures must not fight scrolling/navigation;
- haptic/audio feedback, where platform-supported and authorized, is sparse and synchronized with meaningful causal events;
- real-device behavior matters for gesture/performance claims.

## Design quality hierarchy

When a design feels wrong, prefer fixes in this order:

1. clarify purpose/user flow;
2. fix information hierarchy/wayfinding;
3. fix layout/grouping/density;
4. reuse/repair component patterns;
5. fix typography/color/contrast/states;
6. remove/reduce unnecessary motion;
7. fix motion physicality/performance/accessibility;
8. add polish/delight last.

A polished animation cannot compensate for a confusing flow.

## Provenance note

This core is an original Matreshka synthesis informed by the design-engineering patterns studied in `emilkowalski/skills` and by Apple interface-design principles. It is used as a quality framework, not as a requirement to reproduce another product's visual identity.
