---
name: dmud — The DM's Notebook
description: A warm, readable notebook visual system for a persistent text-first fantasy role-playing game.
status: final
implementation_scope: P0
sources:
  - ../../briefs/brief-dmud-2026-09-05/brief.md
  - ../../gdds/gdd-dmud-2026-09-07/gdd.md
updated: 2026-09-08
colors:
  paper: '#F3EAD6'
  paper-light: '#FFFAF0'
  canvas: '#CFC5B1'
  ink: '#25211D'
  ink-muted: '#756B60'
  forest: '#31584B'
  forest-deep: '#173A31'
  red-pencil: '#A84637'
  rule: '#C9BDA8'
  note: '#F7DF8B'
  player-note: '#D9E9ED'
  focus: '#1265A8'
typography:
  story:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: '18px'
    fontWeight: '400'
    lineHeight: '1.65'
  scene-title:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: '28px'
    fontWeight: '700'
    lineHeight: '1.2'
  overlay-title:
    fontFamily: 'Georgia, "Times New Roman", serif'
    fontSize: '24px'
    fontWeight: '700'
    lineHeight: '1.25'
  interface:
    fontFamily: '"Trebuchet MS", Arial, sans-serif'
    fontSize: '16px'
    fontWeight: '400'
    lineHeight: '1.5'
  interface-strong:
    fontFamily: '"Trebuchet MS", Arial, sans-serif'
    fontSize: '16px'
    fontWeight: '700'
    lineHeight: '1.4'
  label:
    fontFamily: '"Trebuchet MS", Arial, sans-serif'
    fontSize: '13px'
    fontWeight: '700'
    lineHeight: '1.4'
    letterSpacing: '0.08em'
  caption:
    fontFamily: '"Trebuchet MS", Arial, sans-serif'
    fontSize: '14px'
    fontWeight: '400'
    lineHeight: '1.45'
rounded:
  sm: '4px'
  md: '6px'
  lg: '8px'
  xl: '12px'
  full: '9999px'
spacing:
  '1': '4px'
  '2': '8px'
  '3': '12px'
  '4': '16px'
  '5': '24px'
  '6': '32px'
  '7': '48px'
components:
  action-button:
    background: '{colors.forest}'
    foreground: '{colors.paper-light}'
    border-radius: '{rounded.md}'
    focus-ring: '{colors.focus}'
  notebook-navigation:
    background: '{colors.forest-deep}'
    foreground: '{colors.paper}'
    active-background: '{colors.forest}'
  story-entry:
    background: '{colors.paper-light}'
    foreground: '{colors.ink}'
    type: '{typography.story}'
  player-intention:
    background: '{colors.player-note}'
    foreground: '{colors.ink}'
    border-radius: '{rounded.sm}'
  message-composer:
    background: '{colors.paper-light}'
    foreground: '{colors.ink}'
    border: '{colors.ink-muted}'
    border-radius: '{rounded.md}'
  response-status:
    background: '{colors.note}'
    foreground: '{colors.forest-deep}'
    border: '{colors.rule}'
  character-card:
    background: '{colors.paper-light}'
    foreground: '{colors.ink}'
    border: '{colors.rule}'
    border-radius: '{rounded.sm}'
  reference-overlay:
    background: '{colors.paper-light}'
    foreground: '{colors.ink}'
    border: '{colors.ink-muted}'
    border-radius: '{rounded.lg}'
  mechanical-result:
    background: '{colors.paper}'
    foreground: '{colors.ink}'
    border: '{colors.ink-muted}'
    border-radius: '{rounded.sm}'
  system-notice:
    background: '{colors.paper-light}'
    foreground: '{colors.ink}'
    accent: '{colors.red-pencil}'
  award-notice:
    background: '{colors.paper}'
    foreground: '{colors.ink}'
    accent: '{colors.forest}'
  journal-entry:
    background: '{colors.paper-light}'
    foreground: '{colors.ink}'
    divider: '{colors.rule}'
  stat-assignment:
    background: '{colors.paper}'
    foreground: '{colors.ink}'
    selected-border: '{colors.forest}'
    error-border: '{colors.red-pencil}'
  attribute-allocation:
    background: '{colors.paper}'
    foreground: '{colors.ink}'
    selected-border: '{colors.forest}'
    error-border: '{colors.red-pencil}'
  save-slot:
    background: '{colors.paper-light}'
    foreground: '{colors.ink}'
    border: '{colors.rule}'
    selected-border: '{colors.forest}'
---

# dmud — Visual Identity Spine

## Brand & Style

dmud looks like a living tabletop notebook shared between a player and Dungeon Master Rowan: warm paper, ruled structure, readable ink, and small tactile details. It should feel personal and accumulated rather than antique, ornate, or like a generic chat application. The interface stays quiet enough for long reading sessions while labels make narration, NPC speech, James's intentions, and mechanics easy to skim. Conditional-P1 System and award treatments are retained as deferred visual guardrails, not P0 implementation requirements.

The promoted main-notebook composition is illustrated in [The DM's Notebook direction](./mockups/direction-dm-notebook.html). DESIGN.md and EXPERIENCE.md are authoritative wherever that mockup conflicts with them.

## Colors

| Role | Token | Use |
| --- | --- | --- |
| Main page | `{colors.paper-light}` | Transcript, overlays, primary reading surfaces |
| Secondary paper | `{colors.paper}` | Margins, mechanical details, quiet grouping |
| Outer canvas | `{colors.canvas}` | Frames the notebook without competing with it |
| Primary ink | `{colors.ink}` | Long-form text and essential controls |
| Muted ink | `{colors.ink-muted}` | Secondary metadata; never required information by itself |
| Forest | `{colors.forest}` | Primary actions, NPC accents, selected state |
| Deep forest | `{colors.forest-deep}` | Notebook navigation and high-contrast status text |
| Red pencil | `{colors.red-pencil}` | System accent and error emphasis, always paired with text |
| Rule | `{colors.rule}` | Dividers and quiet boundaries |
| Note | `{colors.note}` | Pending-response and taped-note accents |
| Player note | `{colors.player-note}` | James's submitted intention |
| Focus | `{colors.focus}` | Keyboard focus only; never decorative |

Contrast targets: `{colors.ink}` on `{colors.paper-light}` must meet at least 7:1; all normal text and control labels must meet 4.5:1 against their rendered backgrounds; focus rings and essential component boundaries must meet 3:1 against adjacent colors. Speaker and state meaning must never depend on hue.

## Typography

Use `{typography.story}` for narration and sustained reading. Use `{typography.interface}` for controls, player intentions, mechanics, status copy, and overlays; `{typography.interface-strong}` provides emphasis. Scene and overlay headings use `{typography.scene-title}` and `{typography.overlay-title}`. Small categorical labels use `{typography.label}`, but the visible text must remain meaningful without capitalization or letter spacing.

Prefer short line lengths of roughly 55–75 characters for narration. Do not introduce handwriting fonts for player notes: separation comes from paper treatment and explicit labels. Comic Sans is prohibited everywhere.

## Layout & Spacing

Use the 4px-based scale in `spacing`, with `{spacing.2}` for tight relationships, `{spacing.4}` for component padding, and `{spacing.5}`–`{spacing.7}` between major regions. On an ordinary desktop viewport, the notebook may use three regions: navigation, the dominant story page, and a narrow player-character reference margin. The transcript and composer remain the visual center.

At zoomed or narrow widths, regions reflow into one reading column without horizontal page scrolling or lost controls. Navigation compacts into a labeled top region, overlays fit within the viewport, and the player-character reference becomes a compact block rather than forcing a persistent third column. The implementation must not retain the promoted mockup's fixed minimum width.

## Elevation & Depth

Use tonal layers and restrained shadows to suggest stacked paper. The page itself stays nearly flat; `{components.reference-overlay}` receives the strongest shadow and a subdued backdrop. Player notes and the character card may use a slight one-edge paper shadow. Never stack overlays.

## Shapes

Corners are lightly softened, not pill-shaped: `{rounded.sm}` for notes and inline results, `{rounded.md}` for controls, and `{rounded.lg}` for overlays. Organic rotation may be used sparingly on decorative paper scraps, but not on long text, controls, focus indicators, or error content.

## Components

| Component | Visual contract |
| --- | --- |
| `action-button` | Solid `{colors.forest}` with `{colors.paper-light}` text, compact rectangular silhouette, and a clearly external `{colors.focus}` focus ring. |
| `notebook-navigation` | `{colors.forest-deep}` spine with explicit labels; selected items use `{colors.forest}` plus a non-color marker. |
| `story-entry` | Long-form `{typography.story}` on `{colors.paper-light}`; speaker or message-type label precedes content. NPC speech may add a `{colors.forest}` rule and subtle `{colors.player-note}` wash. |
| `player-intention` | A labeled `{colors.player-note}` scrap using interface type; legible and selectable, with decorative tilt optional only when motion/reflow are unaffected. |
| `message-composer` | High-contrast field with a 2px `{colors.ink-muted}` boundary, visible label, generous internal spacing, and adjacent `action-button`. |
| `response-status` | `{colors.note}` paper strip with a truthful text state, Rowan attribution, and optional small playful activity mark. Failed state adds a `{colors.red-pencil}` border and explicit recovery copy. |
| `character-card` | One compact card for James only. Use a monogram or text identity block, not required portrait art; do not imply a roster of nearby characters. |
| `reference-overlay` | Centered, viewport-bounded paper panel with title, close control, subdued backdrop, and clear section dividers. Inventory, character sheet, roll details, and save/load share this shell. |
| `mechanical-result` | Inline dashed or ruled control attached to the relevant story entry; always states skill/result and whether a roll occurred before “Details.” |
| `system-notice` | Deferred conditional-P1 treatment for the fourth-wall-breaking LitRPG System: `{colors.red-pencil}` border/label, visually distinct from Rowan, award narration, NPC speech, and ordinary mechanics. It is not a P0 implementation requirement. |
| `award-notice` | Deferred conditional-P1 treatment for a committed achievement, title, prize, or earned variant: `{colors.forest}` accent on `{colors.paper}`, distinct from the System voice and never shown before the underlying reward commits. It is not a P0 implementation requirement. |
| `journal-entry` | Text-first row separated by `{colors.rule}`; status is written in words, never a color chip alone. |
| `stat-assignment` | Clear attribute/value pairing on `{colors.paper}`; available, assigned, invalid, and locked states use text plus boundary changes. |
| `attribute-allocation` | In-play P0 progression surface on `{colors.paper}`: unspent, previewed, confirmed, invalid, and persisted states use explicit counts and text plus `{colors.forest}` or `{colors.red-pencil}` boundaries. |
| `save-slot` | Paper row showing slot identity, campaign/place, in-world time, and saved-at metadata; current selection uses border and text, not color alone. |

## Do's and Don'ts

| Do | Don't |
| --- | --- |
| Make the transcript the dominant visual surface. | Make the interface resemble a command terminal or generic messenger. |
| Label narration, NPCs, intentions, mechanics, and Rowan explicitly; keep deferred System and award treatments separate. | Distinguish voices with color alone or merge the LitRPG System with award narration. |
| Show only James in the persistent character reference. | Build an omniscient nearby-character roster or leak hidden actors. |
| Use overlays for inventory, character sheet, roll details, and save/load. | Open reference content in new tabs or stack modal layers. |
| Keep absurdity in small waiting details; reserve deferred P1 humor for the distinct System voice. | Let decorative humor obstruct status truth, reading, or focus. |
| Preserve browser zoom, text selection, and responsive reflow. | Fix the notebook to a desktop canvas width. |
| Use system-safe serif and sans-serif families. | Use Comic Sans, faux handwriting, dense medieval display faces, or illegible parchment textures. |
