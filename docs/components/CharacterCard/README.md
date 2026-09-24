# CharacterCard

One compact card for the current player character — a monogram and text identity, a few facts, and a way into the character sheet.

**Consumer provides:** `name`, optional `monogram`, `descriptor`, `facts` (`{label, value}`), and `onOpen`.

- Only the player's own character. Never a roster of nearby characters, and never anything derived from hidden simulation state.
- No portrait art required; the monogram is an `amber` wax-seal disc with an `on-amber` Cinzel Decorative initial; the name is set in engraved capitals and the card has a thin `gilt` double frame.
- Lives in the right margin on desktop and becomes a compact block in the single-column layout.
