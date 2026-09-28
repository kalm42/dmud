# ResponseStatus

The `candle`-paper strip that tells the truth about a request: pending, clarification, resolved, interrupted or failed.

**Consumer provides:** `state`, optionally a `quip` (pending only), a `detail` saying what did or didn't commit, and `onRetry` for failed/interrupted.

- Appears immediately on submit (within 100ms) and changes state in place without moving focus.
- The state text is a polite live region; rotating quips are `aria-hidden` so screen readers aren't re-read.
- Pending may be playful ("Corralling the goblins") but always says Rowan is working and never implies progress or success.
- Failed/interrupted: `oxblood` border, plain recovery copy, a retry that cannot duplicate committed state.
- Under `prefers-reduced-motion` the bobbing mark is static.
