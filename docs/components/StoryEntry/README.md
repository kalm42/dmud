# StoryEntry

One voice in the transcript — narration, an NPC, Rowan, a clarification or a failure — with the voice written in the margin beside it.

**Consumer provides:** `kind`, the text as `children` (paragraphs), and an optional `mechanic` (a `MechanicalResult`). For NPCs: `speaker`, an `epithet` the player already knows ("moneylender", or "stranger in a grey coat" before a name is learned) and `onIdentify`. Set `continued` when the same voice speaks again right after itself, and `dropCap` on the first narration of a scene.

- **One typeface for every voice.** All entries are `story` (Lora 1.125rem / 1.5). Voices are told apart by the margin, the NPC wash and color — never by switching fonts.
- **Margin voices:** Narration is italic `ink-muted`; Rowan is `amber` with italic "your DM" (or "needs a detail" for a clarification); a failure is `oxblood` "Not committed".
- **NPCs:** the name is set in `npc-name` (Cinzel engraved capitals) as a button with a dotted `amber` underline, the italic epithet beneath it. Activating it opens `ReferenceOverlay` with `KnownCharacter` — only what the player's character has learned. It takes no time in the world. The speech sits on `npc-wash` behind a 3px `amber` rule and a faint inset `rule` line.
- **Epithets come from player knowledge only** — never from hidden state. A stranger stays a description until the player learns a name.
- `continued` hides the margin label visually (screen readers still hear "continued") and tightens the gap to `space-3`.
- **`dropCap`** turns the first letter into the illuminated initial (`drop-cap`: Cinzel Decorative in `amber` on `vellum-deep` inside a `gilt` double frame). Once per scene, right after `SceneHeading`. It is CSS `::first-letter`, so screen readers and copy-paste see the plain word.
- Append an entry only once its status is known; never collapse earlier consequences silently. Text stays selectable.
