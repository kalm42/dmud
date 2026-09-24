---
name: dmud — The Campaign Book
description: Illuminated campaign-book visual system for a persistent text-first fantasy role-playing game.
status: final
implementation_scope: P0
sources:
  - ../../briefs/brief-dmud-2026-09-05/brief.md
  - ../../gdds/gdd-dmud-2026-09-07/gdd.md
  - ../../../../docs/README.md
  - ../../../../docs/tokens.json
  - ../../../../docs/design-system.json
  - ../../../../docs/components/
updated: 2026-09-24
colors:
  vellum: "#f8f1e3"
  vellum-dark: "#16120e"
  vellum-deep: "#efe4cf"
  vellum-deep-dark: "#201a14"
  canvas: "#d6c7aa"
  canvas-dark: "#0c0a07"
  ink: "#2b2016"
  ink-dark: "#ede1cb"
  ink-muted: "#6b5b48"
  ink-muted-dark: "#a8977f"
  amber: "#8c4a14"
  amber-dark: "#e3a45c"
  on-amber: "#fff8ec"
  on-amber-dark: "#1e140a"
  walnut: "#3b2a1c"
  walnut-dark: "#2c2117"
  on-walnut: "#f3e7d2"
  on-walnut-dark: "#ede1cb"
  gilt: "#9c7730"
  gilt-dark: "#c9a45a"
  oxblood: "#9e3526"
  oxblood-dark: "#ee8b78"
  rule: "#dccbaa"
  rule-dark: "#3a2f24"
  candle: "#f1e0b0"
  candle-dark: "#3a2f18"
  sage: "#e6e8da"
  sage-dark: "#1b2018"
  npc-wash: "#f1e6d0"
  npc-wash-dark: "#231b14"
  focus: "#1b5fbf"
  focus-dark: "#8ab8ff"
  backdrop: "rgba(43, 32, 22, 0.55)"
  backdrop-dark: "rgba(0, 0, 0, 0.65)"
typography:
  title: {fontFamily: "Cinzel, Georgia, serif", fontSize: "2.5rem", fontWeight: "700", lineHeight: "1.1", letterSpacing: "0.03em"}
  scene-title: {fontFamily: "Cinzel, Georgia, serif", fontSize: "1.5rem", fontWeight: "600", lineHeight: "1.2", letterSpacing: "0.05em"}
  overlay-title: {fontFamily: "Cinzel, Georgia, serif", fontSize: "1.375rem", fontWeight: "600", lineHeight: "1.25", letterSpacing: "0.04em"}
  npc-name: {fontFamily: "Cinzel, Georgia, serif", fontSize: "0.9375rem", fontWeight: "700", lineHeight: "1.2", letterSpacing: "0.04em"}
  button: {fontFamily: "Cinzel, Georgia, serif", fontSize: "0.875rem", fontWeight: "700", lineHeight: "1", letterSpacing: "0.08em"}
  label: {fontFamily: "Cinzel, Georgia, serif", fontSize: "0.8125rem", fontWeight: "600", lineHeight: "1.3", letterSpacing: "0.06em"}
  story: {fontFamily: "Lora, Georgia, serif", fontSize: "1.125rem", fontWeight: "400", lineHeight: "1.5"}
  interface: {fontFamily: "Lora, Georgia, serif", fontSize: "1rem", fontWeight: "400", lineHeight: "1.5"}
  interface-strong: {fontFamily: "Lora, Georgia, serif", fontSize: "1rem", fontWeight: "600", lineHeight: "1.4"}
  voice: {fontFamily: "Lora, Georgia, serif", fontSize: "0.9375rem", fontWeight: "600", lineHeight: "1.25"}
  epithet: {fontFamily: "Lora, Georgia, serif", fontSize: "0.875rem", fontWeight: "400", lineHeight: "1.3", fontStyle: "italic"}
  caption: {fontFamily: "Lora, Georgia, serif", fontSize: "0.875rem", fontWeight: "400", lineHeight: "1.45"}
  drop-cap: {fontFamily: "\"Cinzel Decorative\", Cinzel, Georgia, serif", fontSize: "2.6em", fontWeight: "700", lineHeight: "1"}
rounded:
  sm: "4px"
  md: "6px"
  lg: "8px"
  xl: "12px"
  full: "9999px"
spacing:
  "1": "4px"
  "2": "8px"
  "3": "12px"
  "4": "16px"
  "5": "24px"
  "6": "32px"
  "7": "48px"
  measure-story: "68ch"
  margin-label: "8.5rem"
  target-min: "24px"
components:
  action-button: {background: "{colors.amber}", foreground: "{colors.on-amber}"}
  notebook-navigation: {background: "{colors.walnut}", foreground: "{colors.on-walnut}"}
  notebook-page: {background: "{colors.vellum}", foreground: "{colors.ink}"}
  scene-heading: {background: "{colors.vellum}", foreground: "{colors.ink}"}
  scene-divider: {background: "{colors.vellum}", foreground: "{colors.gilt}"}
  story-turn: {background: "{colors.vellum}", foreground: "{colors.ink}"}
  story-entry: {background: "{colors.vellum}", foreground: "{colors.ink}"}
  player-intention: {background: "{colors.sage}", foreground: "{colors.ink}"}
  known-character: {background: "{colors.vellum}", foreground: "{colors.ink}"}
  message-composer: {background: "{colors.vellum}", foreground: "{colors.ink}"}
  response-status: {background: "{colors.candle}", foreground: "{colors.ink}"}
  character-card: {background: "{colors.vellum}", foreground: "{colors.ink}"}
  reference-overlay: {background: "{colors.vellum}", foreground: "{colors.ink}"}
  mechanical-result: {background: "{colors.vellum}", foreground: "{colors.ink-muted}"}
  journal-entry: {background: "{colors.vellum}", foreground: "{colors.ink}"}
  stat-assignment: {background: "{colors.vellum-deep}", foreground: "{colors.ink}"}
  attribute-allocation: {background: "{colors.vellum-deep}", foreground: "{colors.ink}"}
  save-slot: {background: "{colors.vellum}", foreground: "{colors.ink}"}
  system-notice: {background: "{colors.vellum}", foreground: "{colors.oxblood}"}
  award-notice: {background: "{colors.vellum-deep}", foreground: "{colors.ink}"}
---

# dmud — Visual Identity Spine

## Brand & Style

dmud looks like an illuminated campaign book kept by the hearth: warm vellum, walnut-black ink, amber and gold leaf, engraved titles and a decorated initial at the start of each scene. It leans into fantasy, but the story itself is always set plainly in one readable book face. The ornament sits around the text, never in the way of it.

The `docs/` package is the source of truth for this visual contract. Its tokens and component README files supersede earlier decisions and the [historical notebook mock](./mockups/direction-dm-notebook.html) wherever they differ. DESIGN.md and EXPERIENCE.md are the implementation spines; this resolved contract follows `docs/` on any conflict.

### Principles

- **The story is the page.** The transcript and composer sit on one framed `NotebookPage`; navigation and the character card wait outside it on `canvas`.
- **One typeface for reading.** Every voice in the transcript is Lora at the same size. Voices are told apart by the margin, paper tone and color, never by switching fonts.
- **Ornament frames, text reads.** Gilt rules, stars, flourishes, the drop cap and engraved capitals mark edges and beginnings. They never sit inside a paragraph, carry meaning alone, or reduce contrast.
- **Every voice is written in the margin.** Narration, Rowan, You, or the NPC's name sits in a left margin column. Scan down the margin to find who spoke.
- **Spacing does the grouping.** Turns are separated by whitespace. Only a real change of scene gets a flourish and a new engraved heading.
- **Mechanics stay in the background.** Rolls are small caption lines under their entry, and only their Details button asks for attention.
- **Truth before flourish.** Pending never looks like success. Waiting may be funny ("Corralling the goblins"), but it always says Rowan is working.
- **Only what the character knows.** No rosters, no hints, no suggested replies. An NPC's name opens what the player's character knows about them, and nothing more.
- **The browser owns text size.** All type is in `rem`/`em`; never set a pixel root size or add an in-game text-size control.

### Voice and copy

| Voice | How it sounds | Example |
| --- | --- | --- |
| Rowan (DM) | Warm, attentive, direct; admits uncertainty. | "You haven't heard anyone say how much Mara owes — only that Oren has been asking." |
| Narration | Grounded and concrete; committed facts and what can be perceived. | "Oren doesn't stop counting. The coins go into the box in stacks of ten." |
| NPC | Attributed and credible, limited to what they know. Named as the player knows them, with an epithet ("Oren · moneylender", "Stranger · grey coat, by the well"). | Oren: "A week. Not a day more, and not because I like you." |
| Mechanics | Factual, transparent, untheatrical. | "Persuasion · rolled 14 + 3 = 17 vs 15 · success" |
| Clarification | Neutral; asks for the missing distinction, proposes no tactic. | "Do you want to ask Mara about the debt in general, or discuss a specific arrangement?" |
| Waiting | Truthful, with brief backstage absurdity. | "Rowan is working. Backstage: corralling the goblins." |
| Failure | Plain, specific, recoverable. | "Nothing was committed. Your message is still in the composer." |

Sentence case in running copy; engraved Cinzel labels are short (one to three words). Say "you" to the player. No emoji, no exclamation marks in interface copy. Fantasy lives in the look and in the fiction, not in faux-archaic interface words ("Send", not "Dispatch thy missive").

## Colors

Two themes: **Hearth** (`light`) and **Hearth by night** (`dark`). Every pair below is checked in both.

- **Surfaces:** the page is `vellum`; recessed panels (stat grids, allocation, awards, the drop-cap box) are `vellum-deep`; the desk behind the page is `canvas`.
- **Text:** story and controls in `ink` (14:1 on `vellum`). `ink-muted` is for the margin's "Narration", epithets, captions and roll summaries (5.2:1 or better on every surface in both themes).
- **Amber** is the one accent: primary buttons (label in `on-amber`), Rowan's name, the NPC speech rule, the drop cap, selected borders and the Details button.
- **Gilt** is gold leaf and is ornament only: the page frame, stars, rules under scene titles, the scene flourish and the drop-cap frame. Never text, and never the only boundary of a control.
- **Walnut** is the navigation spine, a leather binding with text in `on-walnut` and a gilt border. In Hearth by night the walnut is close to the page, so the gilt border is what separates it.
- **Sage** is the player's own words, the only cool tone on the page, so "what I said" stands apart from "what the world said".
- **npc-wash** sits behind NPC speech; **candle** lights the pending status strip; **oxblood** marks errors and the deferred System voice, always beside words.
- `rule` is for faint ruled lines only (decorative). A control's boundary is `ink-muted`, or `amber` when selected.
- `focus` is for keyboard focus only.

The frontmatter gives Hearth (`light`) and Hearth by night (`dark`) colors as base and `-dark` pairs. `docs/tokens.json` owns the values and intended contrast pairs.

## Typography

Three families, each with one job. Files are in `fonts/` (Latin subset, SIL OFL; see `fonts/LICENSES.txt`).

- **Lora** (`serif`) carries all reading. `story` (1.125rem / 1.5) for every transcript voice, capped at `measure-story`. `interface` (1rem / 1.5) for intentions, overlays and forms. `voice` for margin names, `epithet` (italic) for the line under them, and `caption` for rolls, times and sources. Italic Lora is the quiet voice: "Narration", epithets, statuses, fact sources.
- **Cinzel** (`display`) is engraved Roman capitals. It's for `scene-title`, `overlay-title`, `npc-name`, `button` labels and small panel `label`s, and nothing longer than a heading. Never set a sentence in it.
- **Cinzel Decorative** (`initial`) is used only for the `drop-cap` and the character monogram.
- No handwriting fonts, no blackletter, and no parchment photographs.

## Layout & Spacing

4px scale: `space-2` for tight relationships, `space-4` for component padding, `space-5`–`space-7` between regions.

**Transcript rhythm.** The size of the gap shows how related two rows are:

| Gap | Between |
| --- | --- |
| `space-7` (48px) | one turn and the next; a scene flourish above |
| `space-5` (24px) | the player's intention and Rowan's first reply |
| `space-4` (16px) | replies within a turn |
| `space-3` (12px) | paragraphs, or the same voice continuing |
| `space-2` (8px) | an entry and its roll annotation |

The margin column is `margin-label` (8.5rem) with a `space-5` gutter; voices are right-aligned against the text. When the story column is narrower than 34rem, the margin folds above each entry.

- **Desktop:** navigation spine, the framed page, and a narrow column holding the `CharacterCard`, all on `canvas`.
- **200% zoom / 320px reflow:** one column. Navigation becomes a labeled top row, the card a compact block, and the page padding drops to `space-4`. No horizontal scroll.
- Every pointer target is at least `target-min` (24×24px) at any zoom. Test NPC names, Details and Close explicitly.

At 200% zoom and 320 CSS px-equivalent reflow, keep all content and controls available without horizontal page scroll. The fold follows the story-column width.

## Elevation & Depth

Use the `shadow-paper-edge`, `shadow-page`, and `shadow-overlay` theme values in `docs/tokens.json`; do not stack overlays.

## Shapes

- Corners are lightly softened: `radius-sm` for notes, speech and small buttons; `radius-md` for controls; `radius-lg` for the overlay. Only the pending dots and the monogram seal are round.
- Depth comes from stacked vellum: `shadow-page` under the page, `shadow-paper-edge` under the player's scraps and the character card, and `shadow-overlay` for the one open overlay over `backdrop`. Never stack overlays.

### Ornament kit

Use these, sparingly, in these places only:

| Ornament | Where | Token |
| --- | --- | --- |
| Double gilt frame + two stars | `NotebookPage`, once per screen | `gilt` |
| Faint paper grain (8% noise) | inside `NotebookPage` only | none (it's a texture) |
| Engraved title over a double rule | `SceneHeading`, once per scene | `scene-title`, `gilt` |
| Illuminated initial | first narration after a `SceneHeading` (`dropCap`) | `drop-cap`, `amber`, `vellum-deep`, `gilt` |
| Drawn flourish | `SceneDivider`, between scenes | `gilt` |
| Inset double line | primary buttons, overlay panel, composer field, character card, award | `on-amber`, `gilt` |

If a screen has more ornaments than this, remove some. Never place ornament between an NPC's name and their words, or inside a paragraph.

## Components

The [component README files](../../../../docs/components/) specify anatomy and states, [`index.d.ts`](../../../../docs/components/index.d.ts) specifies the supplied React API, and [`bundle.css`](../../../../docs/components/bundle.css) is the styling reference. The table records the visual decisions that must survive integration; EXPERIENCE.md carries behavior.

| Component | Visual contract |
| --- | --- |
| `ActionButton` | Solid amber plate, on-amber engraved Cinzel label, fine inset line, `{rounded.md}`; quiet variant uses amber outline. |
| `NotebookNavigation` | Walnut leather spine, gilt double border, on-walnut text; current item adds amber fill and ▸. |
| `NotebookPage` | One framed vellum page, two gilt stars, 8% grain, and page shadow; `plain` removes frame and grain in cramped contexts. |
| `SceneHeading`, `SceneDivider` | Engraved title over a gilt double rule; a gilt flourish separates actual scenes. |
| `StoryTurn` | Voice labels in a `{spacing.margin-label}` left margin, `{spacing.5}` gutter, and spacing rather than turn dividers. |
| `StoryEntry` | Lora story text for every voice; Narration muted italic, Rowan amber, failure oxblood; NPC speech on npc-wash with an amber rule and engraved actionable name. First narration after a scene gets one illuminated initial. |
| `KnownCharacter` | Vellum reference content with Lora fact text and muted source captions. |
| `PlayerIntention` | Verbatim words on sage scrap, written status, and “You · as [character]” in the margin. |
| `MessageComposer` | Vellum field with visible label, 2px ink-muted boundary, generous padding, and adjacent action button. |
| `ResponseStatus` | Candle strip with explicit state; failed and interrupted states add an oxblood boundary. |
| `CharacterCard` | Compact identity with amber wax-seal monogram, engraved name, and thin gilt double frame. |
| `ReferenceOverlay` | Vellum framed leaf, inset gilt double line, Cinzel title, section rules, backdrop, and overlay shadow. |
| `MechanicalResult` | Unboxed muted caption beneath its entry and one small amber-outlined Details button. |
| `JournalEntry` | Text-first known fact or commitment separated by a faint rule; status in words. |
| `StatAssignment`, `AttributeAllocation` | Recessed vellum grids; amber selection and dashed oxblood invalid boundaries, both paired with written state. |
| `SaveSlot` | Vellum row; selection uses amber border plus word, empty slot a dashed border plus label. |
| `SystemNotice`, `AwardNotice` | Deferred: System uses oxblood on vellum; committed award uses amber and a gilt frame on deep vellum. |

### Focus, motion and states

- Focus ring: a solid 2px `focus` outline, 2px outside the control. On the walnut spine it sits outside a 2px `on-walnut` gap, because `focus` alone measures 2.2:1 against walnut in Hearth.
- State is always words plus a boundary change: selected (amber border + "Selected"), invalid (dashed oxblood + what's wrong), locked (says locked).
- The waiting dots may bob; under `prefers-reduced-motion` they're still. Status changes are announced politely without moving focus; rotating quips are not announced. There's no other motion. Ornament never animates.

## Do's and Don'ts

No icon set or logo. The name is set in Cinzel ("dmud"). Controls use words, never icons alone. Typographic marks are the ornaments: ✦ (page stars), ▸ (current navigation item), · (separator), and the drawn flourish.

- Use the story page as the dominant surface and keep navigation and the character card outside it.
- Use margin labels and words for speaker and state; color is supplementary.
- Use gilt only as ornament, never as text or the sole boundary of a control.
- Keep mechanics beneath their own entry and inspectable through Details.
- Preserve browser-owned text size, both themes, keyboard focus, and narrow reflow.

### Deferred visual guardrails

`SystemNotice` (P7–P8) and `AwardNotice` (P6–P8) are visual guardrails only. The System is `oxblood` and fourth-wall-breaking; an award is a centered, gilt-framed plate on `vellum-deep` with an engraved name, and appears only after the reward commits. Never merge them with each other, with Rowan or with mechanics.
