# MessageComposer

The single input for everything the player does: questions for Rowan, character actions, and in-world speech.

**Consumer provides:** `onSubmit(text)`, optional controlled `value`/`onChange`, `disabled`.

- Visible label, 2px `ink-muted` boundary, generous padding, adjacent `ActionButton`.
- Enter sends; Shift+Enter inserts a line (IME composition is respected). The hint says so.
- No modes, prefixes, suggestion chips or generated replies — ordinary words only.
- Don't leave it disabled without a status; pair it with `ResponseStatus`.
