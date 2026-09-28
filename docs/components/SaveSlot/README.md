# SaveSlot

A vellum row for one of three manual save slots, with enough branch context to choose safely.

**Consumer provides:** `slot`, `campaign`, `place`, `worldTime`, `savedAt`, `selected`, `onSelect` — or `empty`.

- Selection is an `amber` border plus the word "Selected" in the label.
- Empty slots are dashed and say "Empty slot".
- Overwriting requires confirmation; a failed save/load preserves the prior durable state and says so.
