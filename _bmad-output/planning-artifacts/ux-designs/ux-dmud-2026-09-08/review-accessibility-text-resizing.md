# Accessibility and Text-Resizing Review — dmud

## Overall verdict

**Needs revision.** The authoritative `DESIGN.md` and `EXPERIENCE.md` contracts clearly adopt browser-owned text sizing: they use relative typography, prohibit an app text-size control, and state measurable 200% zoom and 320 CSS px reflow outcomes. However, the only promoted visual reference—and its byte-identical working copy—cannot demonstrate those outcomes and would clip or hide content if its CSS were reused. The documentation keeps this from being critical by explicitly making the spines authoritative over the mock, but the package still presents a high-impact handoff contradiction.

Finding counts: **0 critical · 2 high · 3 medium · 2 low**.

## Scope checked

- `DESIGN.md`: browser-root inheritance, relative typography tokens, focus treatment, zoom/reflow rules, and mock authority.
- `EXPERIENCE.md`: IA, component/focus behavior, Accessibility Floor, Responsive & Platform, keyboard/pointer behavior, and testability.
- `.decision-log.md`: the 2026-09-15 stakeholder correction and earlier accessibility baseline.
- `reconcile-gdd.md`: treatment of the superseded GDD text-control requirement and mock limitations.
- `.working/direction-dm-notebook.html` and `mockups/direction-dm-notebook.html`: responsive CSS, overflow, fixed dimensions, text units, control sizing, focus, overlays, and absence of an app text-size control. The two files are byte-identical, so every mock finding applies to both.
- Referenced GDD v0.7 only at `G15` (`gdd.md:473,593`) to confirm the documented upstream conflict: it still calls for an adjustable 16–24 px control.

This was a static artifact review, not a runtime conformance test of an implemented application. The mock failures below are deterministic from its CSS; no application build was in scope.

## Findings

### High

- **The sole visual reference cannot reflow at 320 CSS px or at a typical 200% page-zoom viewport.** The mock forces `body` to at least 1040 px, fixes both the rationale and browser frame to 1180 px, and retains a three-column grid with fixed side columns. Its only media query is for reduced motion; there is no responsive collapse. This directly contradicts the one-column contract in `DESIGN.md:184` and `EXPERIENCE.md:151,161`, even though `reconcile-gdd.md:56` correctly labels the frame as non-normative (`.working/direction-dm-notebook.html:14-17,27-29,38-42,71,195-197`; identical in `mockups/direction-dm-notebook.html`). *Fix:* make the visual reference responsive: remove the body minimum width, use `width: min(100%, …)`/fluid tracks, add a narrow-width one-column layout with navigation first and the character block compacted, and verify no page-level horizontal scrolling at 320 CSS px and 200% zoom. Preserve the desktop composition only as the wide-layout branch.

- **Browser-root text enlargement can hide transcript, navigation, character, and composer content.** The 780 px frame, fixed 42 px browser bar, fixed-height app, 480 px transcript, fixed-position composer, and multiple `overflow: hidden` rules leave no growth path when `rem` text expands. The non-resizable 58 px textarea also poorly supports the contracted Shift+Enter multiline behavior at an enlarged root size (`.working/direction-dm-notebook.html:38-42,48-56,71,98-107,117,149-165`; identical in the promoted mock). This conflicts with the no-loss requirement in `.decision-log.md:174` and `EXPERIENCE.md:151`. *Fix:* use content-driven/minimum heights, normal document flow or a non-obscuring sticky composer, page/transcript scrolling that retains all content, a vertically resizable or auto-growing composer, and no hidden overflow on regions containing meaningful content or focusable controls. Test text-only/root-size enlargement to 200% separately from page zoom.

### Medium

- **Essential mock text is materially smaller than the declared design tokens and the user's browser preference.** At a 16 px root, repeated 0.625 rem, 0.6875 rem, and 0.75 rem styles render at 10, 11, and 12 px for navigation labels, save metadata, speaker labels, the mechanical-details control, pending status copy, the composer label, Send, character-sheet controls, and overlay controls. These are functional or state-bearing, not decorative (`.working/direction-dm-notebook.html:56,88-93,102-103,113-119,125-130,146-158,173-176,184-191`; identical in the promoted mock). `DESIGN.md` instead defines `{typography.label}` as 0.8125 rem, `{typography.caption}` as 0.875 rem, and `{typography.interface}` as 1 rem (`DESIGN.md:23-63`). *Fix:* align functional mock text to the named tokens, keep essential control/status copy at least at the label/caption scale, and reserve smaller text only for genuinely nonessential decoration. Validate readability at the default root and after browser-root enlargement.

- **The mock advertises dialogs without implementing the contracted dialog/focus behavior.** Invokers use `aria-haspopup="dialog"`, but each target is a generic `<section popover>` with only `aria-label`; it has no dialog role or modal semantics, and the native popover attribute alone does not provide the contracted contained focus behavior (`.working/direction-dm-notebook.html:177-190,217-218,234,254-272`; identical in the promoted mock). This disagrees with `EXPERIENCE.md:79,153,162`. Enlargement makes predictable containment and internal scrolling more important, not less. *Fix:* use an accessible dialog primitive or add the correct `role="dialog"`, labelling, modal semantics where applicable, initial focus, containment, Escape/close behavior, and invoker focus restoration. Exercise the same tests at 200% zoom and 320 CSS px.

- **The custom focus indicator has no resilient fallback and may be clipped.** The mock removes outlines globally and replaces them with an external box-shadow ring (`.working/direction-dm-notebook.html:22-26`; identical in the promoted mock). Box shadows can disappear in forced-colors modes, and external rings can be cut off by the mock's hidden-overflow containers. That does not reliably demonstrate the visible, unobscured focus requirement in `EXPERIENCE.md:148`. *Fix:* do not blanket-disable outlines; use an outline-based `:focus-visible` indicator (plus any aesthetic shadow), provide a forced-colors-safe fallback, and give focused controls enough scroll margin/inset space that the full indicator remains visible at enlarged text and narrow widths.

### Low

- **One reconciliation sentence leaves the rejected text-size control slightly ambiguous.** `reconcile-gdd.md:43` says an additional convenience control remains optional, while `DESIGN.md:176`, `EXPERIENCE.md:48,150`, and the later reconciliation at `reconcile-gdd.md:55` prohibit an in-game text-size control. The authoritative spines resolve the conflict, so impact is limited, but a downstream reader could still treat a custom text-size widget as permitted. *Fix:* narrow the optional-control sentence to the reduced-motion convenience control, or state explicitly that it does not include text sizing.

- **Component contracts do not make the WCAG 2.2 AA target-size floor explicit.** The global AA baseline technically imports the requirement, but component language such as “compact” plus the mock's very small control labels leaves implementers without a local, testable minimum (`DESIGN.md:198`; `EXPERIENCE.md:72-86,145`; mock lines `126-130,156-159,176,186`). *Fix:* add a component-level acceptance rule that pointer targets meet at least 24 by 24 CSS px or an allowed spacing exception, retain that hit area as text enlarges/reflows, and verify the inline mechanics and overlay close controls in particular.

## Strengths

- The direct stakeholder decision is recorded consistently and traceably in `.decision-log.md:172-176`, `DESIGN.md:176`, and `EXPERIENCE.md:48,150-157`: browser settings own preferred text size and the application must not add a text-size control.
- Every declared typography token uses `rem`; the mock also uses `html { font-size: 100%; }` and `rem` for text, so it does not override the browser root with a fixed-pixel size.
- The written acceptance outcomes are unusually concrete: support through 200% browser zoom, reflow at the equivalent of 320 CSS px, one-dimensional page operation, one-column regional collapse, viewport-bounded internally scrolling overlays, and preserved input semantics.
- The IA and mock contain no Settings surface or custom sizing widget, matching the new decision.
- Keyboard operation, visible/unobscured focus, screen-reader labels, live status without focus theft, reduced motion, selectable text, no hover-only information, and overlay focus return are all explicitly part of the authoritative experience contract.
- `reconcile-gdd.md:55` correctly identifies the remaining GDD `G15` conflict instead of silently pretending the source already agrees, and `DESIGN.md:151` clearly states that the spines win over the mock.
