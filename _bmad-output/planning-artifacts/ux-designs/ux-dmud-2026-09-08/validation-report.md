# Validation Report — dmud

- **DESIGN.md:** `DESIGN.md`
- **EXPERIENCE.md:** `EXPERIENCE.md`
- **Run at:** 2026-09-15T14:38:37-07:00
- **Selected lenses:** rubric walker; accessibility and text resizing

## Overall verdict

The initial rubric verdict was **thin** and the accessibility verdict was **needs revision**. Neither review challenged the browser-owned text-sizing decision itself; both found downstream source drift and a promoted mock that could clip or hide content when text enlarged.

The UX package was remediated after review. The spines now match the GDD's P0 names, values, approved statuses, and E1–E11 stage map; the mock now uses fluid, content-driven layouts, relative functional type, responsive collapse, resilient focus, accessible dialog behavior, and enlargement-safe controls. Static closure checks pass. GDD v0.8 now records the same browser-owned sizing decision, closing the final upstream conflict.

## Category verdicts after remediation

- Flow coverage — **strong**
- Token completeness — **strong**
- Component coverage — **strong**
- State coverage — **strong**
- Visual reference coverage — **strong**
- Bloat & overspecification — **strong**
- Inheritance discipline — **strong**
- Shape fit — **strong**
- Accessibility and text resizing — **adequate** (runtime conformance remains an implementation test)

## Findings by severity

### Critical (0)

None.

### High (0 open, 4 resolved)

**[Resolved · Inheritance discipline] — GDD text-sizing requirement contradicted the stakeholder decision** (`GDD G15`; `DESIGN.md` Typography; `EXPERIENCE.md` Accessibility Floor)

The authoritative UX contract assigned preferred text size to browser settings while GDD v0.7 still required an adjustable 16–24 px control.

Resolution: GDD v0.8 now assigns preferred text size to browser settings, removes the in-game control, and retains the zoom/reflow requirements; the temporary UX warnings were removed.

**[Resolved · Inheritance discipline] — obsolete epic/stage map**

The UX now uses exact E1–E11 names and P0–P9 stages while keeping E3–E11 outside the P0 implementation contract.

**[Resolved · Accessibility] — visual reference could not reflow**

The mock now has a fluid frame and responsive one-column branches without a page minimum width.

**[Resolved · Accessibility] — enlarged text could be hidden**

Fixed content heights, hidden overflow, and the fixed composer were replaced with content-driven flow and a resizable multiline composer.

### Medium (0 open, 7 resolved)

- **Flow coverage:** E1 now uses the exact v0.7 title.
- **Component coverage:** Session 0 now commits Body, Agility, Constitution, Mind, Presence and `8, 10, 12, 13, 14`.
- **Inheritance discipline:** approved G16 latency and contextual-difficulty/anti-scaling status are now inherited accurately.
- **Inheritance discipline:** normative character-card language now refers to the current player character; James remains only the journey/example persona.
- **Accessibility:** functional mock text now follows the design tokens instead of 10–12 px equivalents.
- **Accessibility:** popovers now expose dialog naming/modal semantics and implement initial focus, containment, Escape behavior, and focus return.
- **Accessibility:** focus uses an outline with a forced-colors fallback and scroll margin rather than disabling native outlines globally.

### Low (0 open, 2 resolved)

- The reconciliation now makes clear that an optional convenience control can apply to reduced motion, not text sizing.
- Both spines now state the WCAG 2.2 24 by 24 CSS px target-size floor or spacing exception and preserve it during enlargement/reflow.

## Closure checks

- YAML frontmatter parsed for both spines; both were finalized with `status: final` and `updated: 2026-09-15` after review closure.
- All token references resolved.
- All 15 component names matched across DESIGN.md tokens, DESIGN.md Components, and EXPERIENCE.md Component Patterns.
- Working and promoted HTML mocks were byte-identical.
- Static regression scan found no prior fixed 1040/1180 px frame, fixed 780/480 px content height, hidden meaningful overflow, non-resizable composer, disabled focus outline, or sub-label functional font sizes.
- Responsive branches, dialog semantics, focus containment/return logic, and forced-colors focus fallback were present.
- A browser renderer was unavailable in this environment; 200% zoom, browser-root enlargement, 320 CSS px reflow, keyboard traversal, and screen-reader behavior remain runtime acceptance tests for implementation.

## Reviewer files

- `review-rubric.md`
- `review-accessibility-text-resizing.md`
