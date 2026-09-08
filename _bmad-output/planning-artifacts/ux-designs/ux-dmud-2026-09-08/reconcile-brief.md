---
title: "UX reconciliation with dmud — A World That Remembers"
status: accepted reconciliation with noted proposed/deferred items
created: 2026-09-08
sources:
  - ../../briefs/brief-dmud-2026-09-05/brief.md
  - .decision-log.md
  - mockups/direction-dm-notebook.html
---

# Brief-to-UX reconciliation

The approved product brief remains authoritative for game vision and working defaults. The UX decision log is authoritative for accepted experience decisions, and the promoted DM's Notebook mockup is a first-pass visual reference rather than a new game-design specification.

## Preserved in the accepted UX direction

| Brief intent | Accepted UX expression |
| --- | --- |
| Self-directed play with tabletop freedom | One natural-language composer accepts questions to Rowan, character actions, and in-world speech without modes, command syntax, suggested actions, or reply choices. Rowan clarifies ambiguity without steering or committing state. |
| Creative actions have consistent, understandable consequences | Every submission exposes pending, resolved, or failed status. Inline mechanical results disclose uncertainty, modifiers and their sources, stakes, and rationale; routine feasible observations can explicitly require no roll. |
| NPCs have limited knowledge and lives beyond the player | The interface may show only what the character perceives or legitimately knows. The rejected nearby-character roster cannot leak hidden or merely simulated presence. Narrative steering in Session 0 may create tensions and opportunities but may not override NPC agency or predetermine outcomes. |
| A persistent world that remembers | Save/load remains part of the main surface. On return, the player can ask Rowan for a recap bounded by the character's knowledge; journal and transcript treatments preserve readable continuity. |
| A personable LLM Dungeon Master | Rowan is a named, visible personality expressed through writing, clarification, reflection, and playful waiting updates. Rowan does not receive privileged persistent portrait space. |
| Text-first, readable presentation | The notebook direction uses restrained typography, labeled narration/NPC/mechanics/player/System voices, and temporary reference overlays to keep long-form play skimmable. Comic Sans is explicitly prohibited. |
| Easy save/resume for solo desktop play | The surface map begins at New Game or Continue, then returns to the main notebook. Inventory, character sheet, and mechanical details open without leaving play or advancing fictional time. |
| Character history shapes progression | The character sheet owns separate titles and achievements, while personalized achievements, titles, and ability upgrades arise from play rather than Session 0. First-pass novelty is save/character-local. |
| Hobby prototype before any indie release | The accepted direction targets the local desktop-browser, solo first pass and does not assume accounts, online services, cooperative play, or a public release. |
| Accessible browser experience | WCAG 2.2 AA is the accepted baseline, including semantics for generated content, keyboard and focus behavior, live status announcements, accessible overlays, non-color distinctions, 200% zoom/reflow, and reduced-motion preference support. |

## Intentionally omitted or deferred from this UX pass

- Detailed Brackenford content, victory conditions, NPC simulation, reputation propagation, world time, economy, businesses, crafting, affinities, awakening, and ability-generation rules remain game-design or implementation concerns. Their absence from the visual reference does not remove them from the approved brief.
- Exact attributes, standard-array values, validation rules, rarity curves, slot counts, unlock rules, latency/cost limits, and delivery schedule remain open as recorded; the UX does not settle them.
- Achievements, titles, affinities, and earned ability variants remain outside P0. Conditional P1 retains one generated achievement/prize, one title, and one earned ability variant, preserving the brief's distinct reward meanings.
- Cross-player world-first recognition is a **proposed later indie-release feature**, not accepted first-pass scope. The accepted first pass recognizes only novelty within a character/save history.
- Cooperative campaigns remain deferred until solo play succeeds.
- Graphics, audio, maps, portraits, sprites, and animation remain unnecessary for the prototype. The mockup's visual player-card treatment and playful waiting motion are reference treatments, not new content requirements; motion must respect reduced-motion preferences.

## Resolved tensions

- **Roll log:** The brief permits an optional roll log. The accepted UX omits a global roll-details destination and instead opens details from the relevant transcript result. Mechanical transparency is preserved with less navigation.
- **Reward terminology:** The UX does not merge rewards. Achievements award item prizes, titles grant buffs, and earned ability variants are optional upgrades; either of the first two may be a prerequisite without automatically granting an upgrade.
- **D&D reference versus original rules:** Direct assignment from a fixed array “similar to D&D” is accepted for Session 0, while exact values and attributes remain open. This does not replace the brief's small original resolution system or turn D&D into the full ruleset.
- **Visible characters versus hidden state:** Persistent presentation is limited to the player's character. NPCs appear through legitimately perceived narrative and dialogue, preserving the brief's fallible, limited-knowledge world and avoiding scale problems in crowded scenes.
- **Story steering versus simulation:** Session 0 captures hopes, cool ideas, and agreed character facts so Rowan can establish relevant conflict and growth opportunities. Outcomes remain unplanned, and neither player nor NPC agency may be railroaded.
- **Accessibility settings:** WCAG AA remains required, but a dedicated settings surface is not. Browser zoom/text controls and the operating system's reduced-motion preference are honored while the application still owns semantics, contrast, reflow, focus, and announcements.

## Qualitative ideas at risk of being dropped

- The experience must feel like talking with a tabletop Dungeon Master, not entering prompts into generic chat software or a traditional MUD parser.
- Waiting is part of the emotional arc: it should create playful anticipation with absurd backstage humor while still communicating meaningful pending, resolved, or failed state.
- “A world that remembers” needs player-visible evidence in later encounters, recaps, journals, and consequences; save/load alone does not express the promise.
- Text must remain easy to scan even as history grows. The visual distinction among narration, NPC speech, the player's intention, mechanics, awards, and the System is functional, not decorative.
- Session 0 must ask the player to author the character first. Rowan offers background suggestions only when asked, then reflects the character back for explicit confirmation before opening on a personally relevant situation.
- Narrative personalization must create opportunities for conflict and growth without quietly becoming a fixed plot or recommended-action system.
- Achievement announcements should retain the brief's funny, opinionated voice, while Rowan's waiting humor and the LitRPG System remain perceptibly distinct voices.
- The notebook metaphor should continue to feel like a shared tabletop artifact without weakening the accepted readability, reflow, keyboard, screen-reader, or reduced-motion requirements.
