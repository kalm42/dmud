dmud looks like an illuminated campaign book kept by the hearth: warm vellum, walnut-black ink, amber and gold leaf, engraved titles and a decorated initial at the start of each scene. It leans into fantasy, but the story itself is always set plainly in one readable book face. The ornament sits around the text, never in the way of it.

Components live in `components/bundle.js` as `window.Dmud` (React 18). Class names are prefixed `dm-`. Load `tokens.css` (colors, fonts, spacing) and `components/bundle.css`.

## Principles

- **The story is the page.** The transcript and composer sit on one framed `NotebookPage`; navigation and the character card wait outside it on `canvas`.
- **One typeface for reading.** Every voice in the transcript is Lora at the same size. Voices are told apart by the margin, paper tone and color, never by switching fonts.
- **Ornament frames, text reads.** Gilt rules, stars, flourishes, the drop cap and engraved capitals mark edges and beginnings. They never sit inside a paragraph, carry meaning alone, or reduce contrast.
- **Every voice is written in the margin.** Narration, Rowan, You, or the NPC's name sits in a left margin column. Scan down the margin to find who spoke.
- **Spacing does the grouping.** Turns are separated by whitespace. Only a real change of scene gets a flourish and a new engraved heading.
- **Mechanics stay in the background.** Rolls are small caption lines under their entry, and only their Details button asks for attention.
- **Truth before flourish.** Pending never looks like success. Waiting may be funny ("Corralling the goblins"), but it always says Rowan is working.
- **Only what the character knows.** No rosters, no hints, no suggested replies. An NPC's name opens what the player's character knows about them, and nothing more.
- **The browser owns text size.** All type is in `rem`/`em`; never set a pixel root size or add an in-game text-size control.

## Voice and copy

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

## Color

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

## Typography

Three families, each with one job. Files are in `fonts/` (Latin subset, SIL OFL; see `fonts/LICENSES.txt`).

- **Lora** (`serif`) carries all reading. `story` (1.125rem / 1.5) for every transcript voice, capped at `measure-story`. `interface` (1rem / 1.5) for intentions, overlays and forms. `voice` for margin names, `epithet` (italic) for the line under them, and `caption` for rolls, times and sources. Italic Lora is the quiet voice: "Narration", epithets, statuses, fact sources.
- **Cinzel** (`display`) is engraved Roman capitals. It's for `scene-title`, `overlay-title`, `npc-name`, `button` labels and small panel `label`s, and nothing longer than a heading. Never set a sentence in it.
- **Cinzel Decorative** (`initial`) is used only for the `drop-cap` and the character monogram.
- No handwriting fonts, no blackletter, and no parchment photographs.

## Ornament kit

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

## Layout and spacing

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

## Shape and depth

- Corners are lightly softened: `radius-sm` for notes, speech and small buttons; `radius-md` for controls; `radius-lg` for the overlay. Only the pending dots and the monogram seal are round.
- Depth comes from stacked vellum: `shadow-page` under the page, `shadow-paper-edge` under the player's scraps and the character card, and `shadow-overlay` for the one open overlay over `backdrop`. Never stack overlays.

## Focus, motion and states

- Focus ring: a solid 2px `focus` outline, 2px outside the control. On the walnut spine it sits outside a 2px `on-walnut` gap, because `focus` alone measures 2.2:1 against walnut in Hearth.
- State is always words plus a boundary change: selected (amber border + "Selected"), invalid (dashed oxblood + what's wrong), locked (says locked).
- The waiting dots may bob; under `prefers-reduced-motion` they're still. Status changes are announced politely without moving focus; rotating quips are not announced. There's no other motion. Ornament never animates.

## Iconography

No icon set or logo. The name is set in Cinzel ("dmud"). Controls use words, never icons alone. Typographic marks are the ornaments: ✦ (page stars), ▸ (current navigation item), · (separator), and the drawn flourish.

## Deferred (post-P0)

`SystemNotice` (P7–P8) and `AwardNotice` (P6–P8) are visual guardrails only. The System is `oxblood` and fourth-wall-breaking; an award is a centered, gilt-framed plate on `vellum-deep` with an engraved name, and appears only after the reward commits. Never merge them with each other, with Rowan or with mechanics.
