# StoryTurn

One exchange in the transcript: the player's intention, then everything Rowan returns for it, grouped by spacing rather than boxes.

**Consumer provides:** a `PlayerIntention` followed by its `StoryEntry` replies (and a `ResponseStatus` while pending) as `children`, and optionally the in-world `time` the turn began.

- Spacing carries the structure: `space-7` between turns, `space-5` from the intention to the first reply, `space-4` between replies, `space-3` when the same voice continues.
- Every row writes its voice in the left margin (`margin-label`, 8.5rem) — scan down the margin to find who spoke. Under a 34rem story column the margin folds above the text.
- It is a size container, so the fold follows the story column, not the window — the transcript reflows correctly beside navigation and the character card.
- No dividers between turns — only spacing. Scene changes get a `SceneDivider` and `SceneHeading`; the whole transcript sits in one `NotebookPage`.
