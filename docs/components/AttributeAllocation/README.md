# AttributeAllocation

The in-play surface for spending earned attribute points: counts, a preview, explicit confirmation, and only persisted results.

**Consumer provides:** `attributes`, `earned`, `spent`, `state` (`idle` / `pending` / `persisted`) and `onConfirm(attribute)`.

- Shows Earned · Spent · Unspent as numbers in words.
- Previewing marks the row with an `amber` border and "Previewing +1"; overspending shows a dashed `oxblood` border and says nothing changed.
- Reflects only persisted allocations; never alters the starting-array record.
