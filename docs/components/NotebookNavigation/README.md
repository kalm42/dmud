# NotebookNavigation

The `walnut` spine — a leather binding with a `gilt` double border — that lists Main Notebook destinations and factual campaign controls, labels always visible, with `on-walnut` text.

**Consumer provides:** `items` (`{id, label}`), `currentId`, `onSelect`, and optionally a `title` (campaign name).

- The current item takes an `amber` fill, `on-amber` text, bold weight, a `▸` marker and `aria-current="page"` — never color alone.
- Keep a stable reading order: Notebook, Journal, Inventory, Character sheet, then Save / Load.
- Focus ring sits outside a 2px `on-walnut` gap so it holds 3:1 on the spine.
- At narrow widths (≤40rem) the list wraps into a labeled top region; it never hides behind an icon-only menu.
