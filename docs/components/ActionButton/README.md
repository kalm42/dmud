# ActionButton

The one button: solid `amber` with an `on-amber` label set in the `button` style (Cinzel engraved capitals) and a thin inset line like a tooled plate; `radius-md` corners. Use it for the action the surface exists for — Send, Confirm, Try again.

**Consumer provides:** a short verb-first label (one or two words — Cinzel renders it in capitals) (`children`), `onClick`, and — when disabled for a reason that isn't obvious — `disabledReason`, which is rendered under the button and linked with `aria-describedby`.

- `variant="quiet"` (thin `amber` outline, amber label) for secondary actions such as "Open character sheet".
- Never icon-only. Target is at least `target-min` (24px) at every zoom.
- Focus is a solid 2px `focus` ring, 2px outside the button.
- Don't use it for suggested actions, dialogue replies or choice chips — dmud has none.
