# MechanicalResult

A quiet caption-weight line under the entry it belongs to — skill, whether a roll happened, the result — with a small outlined **Details** button that opens Roll details.

**Consumer provides:** `skill`, `rolled` (false → "no roll needed"), optional `roll` summary, `result`, and `onDetails` (opens Roll details in `ReferenceOverlay`).

- Sits back: `caption` size in `ink-muted`, no box, no fill. Skill and result are bold so they can still be skimmed.
- **Details** is the one thing that asks for attention: a small Cinzel label with an `amber` outline, fills `amber` on hover, `target-min` or larger. Its accessible name includes the skill ("Details of the Persuasion roll").
- The summary is plain text, so it stays selectable.
- Always reads: skill · rolled/no roll · result, then Details. "No roll needed" is a real, inspectable result.
- Belongs to exactly one entry — never a global roll log.
