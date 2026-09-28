# StatAssignment

The Session 0 grid that pairs Body, Agility, Constitution, Mind and Presence with 8, 10, 12, 13 and 14 — each used exactly once.

**Consumer provides:** `value`/`onChange` (or `defaultValue`), `onConfirm`, and `locked` once Rowan's reflection is confirmed.

- Every attribute shows its state in words: Unassigned, Assigned, Duplicate, Locked — with a boundary change (`amber` set, dashed `oxblood` duplicate).
- Duplicate, missing and unassigned problems are listed inline and block confirmation without discarding answers.
- After confirmation the starting array is read-only in ordinary use.
