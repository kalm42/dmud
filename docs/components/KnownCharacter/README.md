# KnownCharacter

The body of the "What you know about …" overlay opened from an NPC's name — dmud's version of casting *identify* on someone.

**Consumer provides:** `epithet`, `facts` (`{text, source}` — each fact with where the character learned it), optional `lastSeen`, and the player's `characterName`. Render it inside `ReferenceOverlay` titled "What you know about {name}".

- Lists only what the player's character legitimately knows: seen, heard or been told. Never hidden motives, stats, relationships the player hasn't observed, or anything from simulation state.
- Every fact carries its source in `caption`, so the player can judge how reliable it is (a rumor from Tessa vs. something they saw).
- The empty state is honest: "Nothing yet beyond what you've seen here." — never a guess.
- Opening it advances no fictional time; the note at the foot says so.
