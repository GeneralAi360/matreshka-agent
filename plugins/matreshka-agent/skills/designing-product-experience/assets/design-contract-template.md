# Product Design Contract

- Status: `{{CURRENT_STALE_CONFLICT_DRAFT}}`
- Design identity/hash: `{{DESIGN_IDENTITY_OR_PENDING}}`
- Last material design decision: `{{DATE_OR_NONE}}`
- Product surfaces covered: {{WEB_MOBILE_DESKTOP_OR_OTHER}}
- Product UI locale: `{{PRODUCT_UI_LOCALE_OR_UNRESOLVED}}`

> This file is the durable UX/UI contract for the project. It is design context, not permission or behavioral proof. Current implementation, user decisions, technical/security requirements and this contract must be reconciled when they materially disagree.

## 1. Product personality and signature

- Desired feeling: {{CALM_CONFIDENT_PLAYFUL_PREMIUM_DIRECT_OR_OTHER}}
- Product personality in one sentence: {{PERSONALITY}}
- Product-specific signature idea: {{SIGNATURE_THAT_COULD_NOT_BE_PASTED_UNCHANGED_INTO_AN_UNRELATED_PRODUCT}}
- This product should feel like: {{POSITIVE_TRAITS}}
- This product should **not** feel like: {{ANTI_TRAITS}}
- Visual/interaction references approved by the user: {{REFERENCES_OR_NONE}}
- Generic/slop patterns deliberately avoided: {{ANTI_SLOP_DEFAULTS_OR_NONE}}

## 2. UX principles

- Primary users: {{USERS}}
- Primary jobs/tasks: {{TASKS}}
- Common path: {{COMMON_PATH}}
- Advanced path/disclosure: {{ADVANCED_PATH}}
- Wayfinding rule: {{HOW_USERS_KNOW_WHERE_THEY_ARE_AND_ESCAPE}}
- Feedback rule: {{STATUS_SUCCESS_WARNING_ERROR}}
- Agency/forgiveness rule: {{UNDO_CONFIRMATION_ESCAPE}}
- Responsibility/privacy/safety rule: {{RULE}}

## 3. Product language and localization

Conversation language and product UI language are separate.

- Product UI locale/language: {{LOCALE}}
- Locale source/decision authority: {{USER_EXISTING_PRODUCT_REPOSITORY_PROVISIONAL_FULL_AUTO}}
- Canonical product terminology: {{TERMS}}
- Date/number formatting: {{RULE}}
- Text expansion/wrapping rule: {{RULE}}
- Fallback/localization strategy: {{RULE_OR_NA}}
- Accessibility labels follow: {{LOCALE_AND_TERMINOLOGY_RULE}}

Do not silently switch product copy to English because framework examples/defaults are English.

## 4. Layout and app shell

- App shell/navigation pattern: {{PATTERN}}
- Container/grid strategy: {{RULE}}
- Page header pattern: {{RULE}}
- Main content width/density: {{RULE}}
- Sidebar/panel behavior: {{RULE_OR_NA}}
- Desktop composition: {{RULE}}
- Compact/tablet composition: {{RULE}}
- Mobile composition: {{RULE}}

## 5. Spacing and density system

- Spacing scale/source: {{TOKENS_OR_RULE}}
- Section spacing: {{RULE}}
- Card/panel padding: {{RULE}}
- Form vertical rhythm: {{RULE}}
- Dense data/table spacing: {{RULE_OR_NA}}

## 6. Typography

- Font family/fallback: {{RULE}}
- Signature/display type rationale: {{WHY_THIS_FACE_FITS_THIS_PRODUCT_OR_NA}}
- Display/H1: {{SIZE_WEIGHT_LINE_HEIGHT_TRACKING}}
- H2/H3: {{RULE}}
- Body: {{RULE}}
- Label/control text: {{RULE}}
- Caption/meta: {{RULE}}
- Numeric/tabular rules: {{RULE_OR_NA}}
- Responsive/text-scaling rule: {{RULE}}

## 7. Color and surfaces

- Canvas/background: {{TOKEN_RULE}}
- Primary surface: {{TOKEN_RULE}}
- Elevated/floating surface: {{TOKEN_RULE}}
- Primary text: {{TOKEN_RULE}}
- Secondary/muted text: {{TOKEN_RULE}}
- Accent/action: {{TOKEN_RULE}}
- Success/warning/error: {{TOKEN_RULE}}
- Light/dark mode strategy: {{RULE_OR_NA}}
- Contrast rule: {{RULE}}
- Palette rationale / avoided generic defaults: {{RULE}}

## 8. Radius, borders, shadows and depth

- Radius scale: {{TOKENS}}
- Border rule: {{RULE}}
- Card/panel depth: {{RULE}}
- Floating/popover/modal depth: {{RULE}}
- Translucency/blur policy: {{RULE_OR_NONE}}
- Shadow/glow rule: {{DIRECTIONAL_TONAL_OR_NONE}}

## 9. Components and primitives

Use existing project components/primitives first.

| Pattern | Canonical component/library | Key visual/behavior rules | Do not |
| --- | --- | --- | --- |
| Button | {{COMPONENT}} | {{RULE}} | {{ANTI_PATTERN}} |
| Input/Textarea | {{COMPONENT}} | {{RULE}} | {{ANTI_PATTERN}} |
| Select/Menu/Popover | {{COMPONENT}} | {{TRIGGER_PLUS_OPEN_STATE_WIDTH_LAYERING_FOCUS_KEYBOARD_MOBILE_RULES}} | {{NATIVE_OR_HANDROLLED_MISMATCH_ANTI_PATTERN}} |
| Date picker/Combobox | {{COMPONENT_OR_NA}} | {{OPEN_STATE_COLLISION_SCROLL_KEYBOARD_RULES}} | {{ANTI_PATTERN}} |
| Card/Panel | {{COMPONENT}} | {{RULE}} | {{ANTI_PATTERN}} |
| Table/List | {{COMPONENT}} | {{RULE}} | {{ANTI_PATTERN}} |
| Modal/Drawer/Sheet | {{COMPONENT}} | {{OPEN_STATE_FOCUS_LAYERING_ESCAPE_RULE}} | {{ANTI_PATTERN}} |
| Toast/Feedback | {{COMPONENT}} | {{RULE}} | {{ANTI_PATTERN}} |
| Navigation | {{COMPONENT}} | {{RULE}} | {{ANTI_PATTERN}} |

A native platform control is valid only when native appearance is an intentional part of the product experience. Closed-state screenshots are insufficient for layered controls.

## 10. Component states and feedback

- Hover: {{RULE}}
- Active/pressed: {{RULE}}
- Focus-visible: {{RULE}}
- Disabled: {{RULE}}
- Loading: {{RULE}}
- Empty: {{RULE}}
- Error/validation: {{RULE}}
- Success/completion: {{RULE}}
- Destructive confirmation: {{RULE}}
- Open/expanded layered-control states: {{SELECT_MENU_POPOVER_DIALOG_DATEPICKER_RULES_OR_NA}}

## 11. Screen patterns

### Dashboard / overview

{{RULE_OR_NA}}

### List / table

{{RULE_OR_NA}}

### Detail

{{RULE_OR_NA}}

### Form / editor

{{RULE_OR_NA}}

### Settings

{{RULE_OR_NA}}

### Authentication / onboarding

{{RULE_OR_NA}}

## 12. Responsive, input and touch rules

- Breakpoints/source: {{RULE}}
- Reflow priority: {{RULE}}
- Overflow/wrapping: {{RULE}}
- Keyboard navigation: {{RULE}}
- Pointer/hover: {{RULE}}
- Touch targets/press behavior: {{RULE}}
- Gesture conflicts/scroll behavior: {{RULE_OR_NA}}
- Overlay collision/viewport behavior: {{RULE}}

## 13. Accessibility

- Focus visibility: {{RULE}}
- Contrast: {{RULE}}
- Reduced motion: {{RULE}}
- Text scaling/localization: {{RULE}}
- Semantic labels/announcements: {{RULE}}
- Error recovery: {{RULE}}
- Touch/pointer accessibility: {{RULE}}
- Layered-control focus/escape/return behavior: {{RULE}}

## 14. Motion system

- Motion personality: {{CRISP_RESTRAINED_PHYSICAL_PLAYFUL_OR_OTHER}}
- High-frequency/keyboard actions: {{NO_OR_NEAR_IMPERCEPTIBLE_RULE}}
- Enter/exit easing: {{TOKEN_OR_RULE}}
- On-screen movement easing: {{TOKEN_OR_RULE}}
- Press feedback: {{RULE}}
- Popover/origin rule: {{RULE}}
- Spring/gesture rule: {{RULE_OR_NA}}
- Typical duration budget: {{RULE}}
- Stagger/delight rule: {{RULE_OR_NONE}}
- Performance rule: {{TRANSFORM_OPACITY_OR_PROJECT_RULE}}
- Reduced-motion alternative: {{RULE}}
- Content-visible-without-animation invariant: {{RULE}}

## 15. Approved design direction

- Direction name: {{DIRECTION_OR_EXISTING}}
- Selection mode: {{USER_SELECTED_FULL_AUTO_EXISTING_RECON}}
- Prototype/design evidence: {{REFS_OR_NONE}}
- Selection rationale: {{RATIONALE}}
- Main tradeoff accepted: {{TRADEOFF}}
- Anti-slop review at selection: {{PASS_CHANGES_REQUIRED_UNCHECKABLE_WITH_EVIDENCE}}

## 16. Design invariants

### ALWAYS

- Product copy follows the resolved `PRODUCT_UI_LOCALE`.
- Layered controls are checked in open/expanded state when materially present.
- Content remains visible without entrance-animation completion.
- {{INVARIANT}}
- {{INVARIANT}}

### NEVER

- Treat a generic AI template/palette/component default as a design direction without product-specific rationale.
- Treat a closed select/menu trigger as complete evidence for the open control.
- {{ANTI_INVARIANT}}
- {{ANTI_INVARIANT}}

## 17. Material design decisions

| Date | Decision | Reason | Affected patterns/screens | Approved by/source |
| --- | --- | --- | --- | --- |
| {{DATE}} | {{DECISION}} | {{RATIONALE}} | {{SCOPE}} | {{AUTHORITY}} |

## 18. Known design debt / drift

- {{NONE_OR_ITEM_WITH_SCOPE_AND_OWNER}}

## 19. Sources and freshness

- Current token/component sources: {{PATHS}}
- Current representative screens: {{PATHS_OR_ROUTES}}
- Design recon baseline/current identity: {{STATE}}
- Anti-slop review source: `skills/designing-product-experience/references/anti-slop.md`
- Refresh when: {{CONDITION}}

## Apple-inspired core reminder

Every material design choice should preserve: **Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight**. These are quality principles, not an instruction to imitate Apple's visual style.

## Anti-slop reminder

Avoiding generic patterns is not enough by itself. Preserve one coherent product-specific signature, use real accessible primitives, inspect open interactive states, and run the anti-slop review before clean design approval.
