# Spine Pair Review — dmud

## Overall verdict

**Thin.** The 2026-09-15 browser-owned text-sizing change is coherent and extractable: the type tokens are relative, the browser root preference is preserved, and zoom/reflow behavior is committed without adding a duplicate in-game control. The P0 interaction contract remains substantially complete, but the pair is not yet a clean downstream handoff because several passages still describe the pre-v0.7 epic map and superseded source statuses.

## 1. Flow coverage — adequate

The direct sources contain no separately numbered user journeys. For the normative P0 scope, the spine provides a named-protagonist, numbered Session 0 flow plus Key Flows for E1 and E2; each has a climax and applicable failure/recovery path (`EXPERIENCE.md:180`, `EXPERIENCE.md:193`, `EXPERIENCE.md:207`). Conditional E3–E11 work does not require current Key Flows because the pair explicitly limits implementation scope to P0, although its deferral map needs correction under inheritance discipline.

### Findings

- **[medium]** The E1 Key Flow and Phase Scope use `E1 — Act in a small persistent world`, but GDD v0.7 names the work package `E1 — Enter and act in a small persistent world`; the flow is behaviorally complete but fails the exact-name check (`EXPERIENCE.md:26`, `EXPERIENCE.md:193`; `../../gdds/gdd-dmud-2026-09-07/gdd.md:503`). *Fix:* Use the v0.7 title verbatim in both locations.

## 2. Token completeness — strong

The frontmatter defines 12 hex color tokens, seven typography roles, five radii, seven spacing tokens, and 15 component token objects (`DESIGN.md:10`). All 26 distinct `{path.to.token}` references across both spines resolve, every typography `fontSize` is expressed in `rem`, and load-bearing contrast targets are stated for reading text, controls, focus, and essential boundaries (`DESIGN.md:170`, `DESIGN.md:176`).

### Findings

None.

## 3. Component coverage — thin

All 15 formal component identifiers have substantive, exact-name visual rows in DESIGN.md and behavioral rows in EXPERIENCE.md (`DESIGN.md:194`, `EXPERIENCE.md:66`). Most are implementation-ready, including the zoom-independent `message-composer`, truthful `response-status`, overlay focus contract, allocation workflow, and save-slot recovery behavior.

### Findings

- **[high]** The P0 `stat-assignment` contract says the exact array and attribute names are open, and Open Items says Session 0 must not invent them, while GDD v0.7 approves Body, Agility, Constitution, Mind, Presence and the fixed array 8, 10, 12, 13, 14 (`EXPERIENCE.md:84`, `EXPERIENCE.md:173`; `../../gdds/gdd-dmud-2026-09-07/gdd.md:116`). A downstream consumer cannot implement the required P0 character-creation component correctly from the spine as written. *Fix:* Commit the five names and five values in the IA, component behavior, states/flow, and remove the obsolete open item.

## 4. State coverage — strong

Every IA surface has applicable operational states: Title, Session 0, Main Notebook, Journal, Inventory, Character sheet, Roll details, and Save selection cover cold/load, empty, ready, valid/invalid, pending, success, interruption, failure, and recovery as appropriate (`EXPERIENCE.md:35`, `EXPERIENCE.md:90`). Cross-surface focus return, live announcements, idempotent retry, reduced motion, browser zoom, and reflow are also committed.

### Findings

None.

## 5. Visual reference coverage — strong

Artifact inventory: `mockups/direction-dm-notebook.html` is the only promoted mock; `imports/` is empty; `wireframes/` is absent. Both spines link the mock inline, name its Main Notebook/Inventory/Character sheet/Roll details coverage, explicitly classify Title/Session 0/Save selection/Journal as spine-only, and state once that the spines win on conflict (`DESIGN.md:151`, `EXPERIENCE.md:46`). The mock preserves browser root sizing with `html { font-size: 100%; }`; its fixed 1040/1180 px demonstration frame is explicitly rejected as an implementation constraint by both spines (`mockups/direction-dm-notebook.html:14`, `mockups/direction-dm-notebook.html:17`, `DESIGN.md:184`, `EXPERIENCE.md:163`).

### Findings

None.

## 6. Bloat & overspecification — strong

The pair is table-forward and generally confines itself to visual and behavioral decisions. Detailed mechanics remain inherited from the GDD rather than copied, while later-stage System and award treatments are explicitly non-P0 guardrails. The browser sizing rule is stated only where downstream consumers need it: typography, IA, accessibility, and responsive behavior.

### Findings

None.

## 7. Inheritance discipline — broken

Both frontmatter source paths and the DESIGN.md peer reference resolve. Component identifiers match across token definitions and both component sections, and every EXPERIENCE.md token reference resolves. However, the source vocabulary and approval statuses have drifted materially from the referenced GDD v0.7.

### Findings

- **[high]** Phase Scope and the deferred sections still encode the old E1–E6/P0–P2 map: E3–E6 are assigned obsolete titles/stages, E7–E11 are absent, and alchemy, recognition, System quests, and hidden bonuses are repeatedly called conditional P1 rather than P5–P8 (`EXPERIENCE.md:22`, `EXPERIENCE.md:28`, `EXPERIENCE.md:60`, `EXPERIENCE.md:81`, `EXPERIENCE.md:115`, `EXPERIENCE.md:165`; `DESIGN.md:149`, `DESIGN.md:207`; `../../gdds/gdd-dmud-2026-09-07/gdd.md:503`). This can send later planning to the wrong work package even though none is P0 scope. *Fix:* Replace the phase table with exact E1–E11 names/stages from v0.7 and relabel deferred voice/component guidance by its actual P6–P8 stage or generically as post-P0.
- **[medium]** Two P0 source statuses are stale beyond the array issue: the UX calls G16 latency numbers “proposed usability targets” and contextual-difficulty/anti-scaling tuning “provisional,” while v0.7 marks both approved (`EXPERIENCE.md:130`, `EXPERIENCE.md:203`; `../../gdds/gdd-dmud-2026-09-07/gdd.md:487`, `../../gdds/gdd-dmud-2026-09-07/gdd.md:581`). *Fix:* Preserve them as approved inherited requirements, while leaving implementation detail to architecture and testing.
- **[medium]** DESIGN.md says the persistent character card is “for James only,” although the GDD defines James solely as the journey persona and requires the player to supply the protagonist's name (`DESIGN.md:204`, `DESIGN.md:220`; `../../gdds/gdd-dmud-2026-09-07/gdd.md:94`). *Fix:* Say “the current player character” in the normative visual contract and reserve James for journeys and illustrative mock copy.
- **[medium]** The selected browser-owned text-sizing rule intentionally overrides G15, but the referenced GDD still requires an adjustable 16–24 px in-game control, so the source set remains contradictory despite the spine's clear local precedence (`DESIGN.md:176`, `EXPERIENCE.md:150`, `EXPERIENCE.md:156`; `../../gdds/gdd-dmud-2026-09-07/gdd.md:473`, `../../gdds/gdd-dmud-2026-09-07/gdd.md:593`; `.decision-log.md:169`). *Fix:* Correct G15 upstream to require browser-owned text sizing, relative units, and zoom/reflow, then remove the temporary supersession warning from the finalized spines.

## 8. Shape fit — strong

DESIGN.md follows the canonical order exactly: Brand & Style → Colors → Typography → Layout & Spacing → Elevation & Depth → Shapes → Components → Do's and Don'ts (`DESIGN.md:147`). EXPERIENCE.md includes all required defaults plus justified Phase Scope, Text UI & Information Boundaries, Input Schemes, Game Feel & Juice, Inspiration & Anti-patterns, Responsive & Platform, deferred-scope, and open-item sections (`EXPERIENCE.md:14`). Responsive & Platform is required and present for desktop, 200% zoom, narrow reflow, overlays, and interaction parity; no HUD-specific section is needed for this text-first interface.

### Findings

None.

## Mechanical notes

- Frontmatter parses in both files; peer `name`, `status: draft`, `implementation_scope: P0`, sources, and `updated: 2026-09-15` match.
- Token check: 12 hex colors, seven typography roles with `rem` sizes, five radii, seven spacing tokens, 15 component objects, 26 distinct cross-references, zero unresolved references.
- Component check: all 15 identifiers pair exactly across DESIGN.md frontmatter, DESIGN.md Components, and EXPERIENCE.md Component Patterns.
- Visual artifacts: one promoted mock, zero imports, no wireframes; its link resolves from both spines. The `.working/` copy is byte-identical to the promoted mock and is not a promoted-reference orphan.
- Browser-sizing regression check: no in-game sizing control is specified; all spine type sizes use `rem`; the mock's root is `100%`; 200% zoom, 320 CSS px-equivalent reflow, preserved reading order, and no two-dimensional page scrolling are explicit. The fixed-width mock remains reference-only and is explicitly superseded.
- Source paths resolve, but GDD v0.7 still conflicts with the stakeholder's newer G15 correction and contains the authoritative E1–E11 map and P0 values missing from the spine.
- Mermaid: none present.
- Findings: **critical 0 · high 2 · medium 4 · low 0**.
