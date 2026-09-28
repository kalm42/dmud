# ReferenceOverlay

The shared framed-leaf dialog (`vellum`, inset `gilt` double frame, Cinzel `overlay-title`) for Inventory, Character sheet, Roll details and Save / Load.

**Consumer provides:** `open`, `title`, `onClose`, and the content as `children` (top-level children are separated by `rule` dividers).

- Centered, bounded by the viewport, scrolls internally; `radius-lg`, `shadow-overlay` over `backdrop`.
- `role="dialog"`, `aria-modal`, named by its title; Escape and the Close button dismiss; focus is contained and returns to the invoker.
- One at a time — never stack overlays, never open reference content in a new tab.
- Opening it advances no fictional time.
- `contained` positions it inside the nearest positioned ancestor (docs and previews only).
