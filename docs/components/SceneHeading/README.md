# SceneHeading

An engraved title that opens a new place or time, set in `scene-title` (Cinzel) over a short `gilt` double rule.

**Consumer provides:** `title` (the place, and time if it matters — "Mill Lane, at dusk"), optional `detail` (an italic caption line, e.g. "Day 3"), and `level` (heading level, default 2).

- Aligns with the story column, not the margin.
- Only for real scene changes — a new location or a jump in time. Ordinary turns are separated by spacing alone.
- Follow it with a `StoryEntry` of narration with `dropCap` to open the scene like a chapter.
