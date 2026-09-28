# NotebookPage

The framed page the story is written on: a gilt double rule, two gilt stars on the top edge, a faint paper grain, and `shadow-page` lifting it off `canvas`.

**Consumer provides:** the page's content as `children` — `SceneHeading`, `StoryTurn`s, `SceneDivider`s and the `MessageComposer`. Optional `label` (accessible name), `as` (defaults to `main`), and `plain` to drop the frame and grain (use inside overlays or very narrow layouts if the frame crowds the text).

- Put exactly one NotebookPage around the transcript and composer; everything else (navigation, character card) sits outside it on `canvas`.
- The frame and stars are `gilt` — ornament only. The page's readability never depends on them.
- The grain is a 8%-opacity noise tile: texture you notice only if you look. Never replace it with a parchment photo.
- At narrow widths the padding drops to `space-4` so the story keeps its measure.
