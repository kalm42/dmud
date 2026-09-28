---
baseline_commit: 3694c57
---

# Story 1.2: Open the Title and Start a New Game

Status: review

## Story

As a player,
I want to start a new campaign from a clear Title surface,
so that I can enter Session 0 even if save discovery fails.

## Acceptance Criteria

1. **Given** the application has opened and the save index is still loading, **when** the Title surface renders, **then** New Game and Continue are shown immediately, and Continue is unavailable with truthful loading context while New Game remains keyboard and pointer accessible.
2. **Given** all three save slots are empty, **when** the save-index request succeeds, **then** Continue remains visible but unavailable, and its accessible explanation states that no saved campaign exists.
3. **Given** the save index cannot be read or fails runtime validation, **when** the Title surface reports the failure, **then** it offers a safe retry and keeps New Game available, and malformed data is not presented as an empty save list.
4. **Given** the player activates New Game, **when** the entry action succeeds, **then** the application enters the Session 0 route or surface without deleting saves or selecting an occupied slot, and the transition advances no fictional time.
5. **Given** the Title surface is used with keyboard navigation, a screen reader, enlarged browser text, 200% zoom, reduced motion, or the 320 CSS px-equivalent layout, **when** the player operates every control, **then** labels, focus, status, target size, reading order, and functionality remain available, and the layout reflows without horizontal page scrolling.

## Tasks / Subtasks

- [x] Provide a read-only save-index boundary (AC: 1–3)
  - [x] Add a typed `GET /api/save-slots` route returning exactly three numbered, explicitly empty slots for the current foundation; reading this resource must not create, select, or load a branch. Define only the response states this story can truthfully supply, leaving persisted occupied-slot handling to Story 1.31.
  - [x] Export OpenAPI and regenerate the committed client, Zod schema, and TanStack Query options through the existing scripts. Add a small API adapter that passes the abort signal, validates `unknown` response data strictly, and reports transport/schema errors as errors, never as `[]` or empty slots.
- [x] Replace the startup shell with the Title and Session 0 entry surface (AC: 1–5)
  - [x] Put Title behavior and presentation in `frontend/src/features/title/`; keep `App.tsx` as the composition point. Show both actions on first render. Derive Continue availability from a validated compatible occupied slot only; loading, empty, and error states each need an explicit accessible reason. A failed read offers Retry using the same query, with New Game independent of query success.
  - [x] Make New Game enter a distinct Session 0 surface using the smallest local navigation state appropriate to the current app. Since Story 1.3 owns durable draft creation and Story 1.5 owns Rowan's first answer UI, the entry surface must not claim that a draft, character, campaign, or first question is saved. Do not add a persistence write or advance a game clock in this story.
  - [x] Apply the approved paper/ink/forest Title direction, semantic landmarks, visible focus, logical reading order, text reflow, reduced-motion behavior, and accessible button targets. Keep the reason for disabled Continue readable and programmatically available; native disabled controls alone cannot receive focus.
- [x] Verify the real boundary and player journey (AC: 1–5)
  - [x] Add backend ASGI integration coverage for the three-slot response and read-only behavior, plus strict frontend parsing coverage for malformed data.
  - [x] Extend the real Playwright startup journey to cover initial loading, empty slots, API failure and retry, and New Game entry; keep first-party API routes real. Add keyboard and narrow/zoom checks where they observe Title behavior. Preserve the Story 1.1 status/proxy and secret-canary assertions where still applicable.
  - [x] Run separate format, lint, strict typecheck, build, backend tests, frontend tests, browser tests, and generated-contract drift checks using the commands documented in `README.md` and the repository CI.

## Dev Notes

### Scope and handoffs

- Epic 1 makes Title entry usable before Session 0 mechanics. Story 1.2 owns immediate Title actions, loading/empty/error save-index states, safe retry, and the zero-time transition to a Session 0 surface. Story 1.3 owns the first SQLite migration and recoverable draft operation; Story 1.5 owns the first Rowan answer/composer; Story 1.31 owns occupied-slot selection and loading. The Session 0 entry here is a truthful handoff, not a durable draft. [Source: `_bmad-output/planning-artifacts/epics.md`, Epic 1 handoffs and Stories 1.2–1.5, 1.31; `_bmad-output/planning-artifacts/implementation-readiness-report-2026-09-23-p0.md`, P0 story boundary review]
- Architecture's eventual `GET /api/save-slots` contract distinguishes three numbered empty, occupied, or unavailable slots. In this stage there are no save records or database schema; return three explicit empty entries through a read-only query. Avoid a fake occupied slot, save selector, automatic Continue navigation, or schema work that belongs to later stories. New Game does not depend on this read, and a read/schema failure is unknown state rather than known-empty state. [Source: `_bmad-output/game-architecture.md`, Transport and Query-State Contracts; `_bmad-output/planning-artifacts/epics.md`, Stories 1.2, 1.3, 1.31]
- Keep the Title state model explicit: cold/loading; validated empty; validated compatible occupied (future Story 1.31); read/validation error; retrying. A retry must preserve New Game availability and cannot imply Continue is safe while the index is unknown. Avoid a general router dependency for this two-surface handoff unless the existing app actually requires one. [Source: `_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md`, State Patterns; `_bmad-output/game-architecture.md`, Transport and Query-State Contracts]

### Existing code to update and preserve

- `frontend/src/app/App.tsx` currently renders the semantic startup panel and validated `/api/status` readiness states. Replace its campaign-placeholder copy with Title composition, but preserve useful API-unavailable honesty and a semantic main landmark. `frontend/src/app/app.css` supplies paper-toned shell, relative text, and status/alert styles; adapt rather than discard its responsive base. `frontend/src/main.tsx` already provides a `QueryClientProvider`; reuse it. [Source: repository inspection, 2026-09-23; Story 1.1 Dev Agent Record]
- `frontend/src/api/useStatus.ts` uses generated query options/SDK, forwards the abort signal, disables hidden retries, and calls `parseStatus.ts` for strict generated-Zod validation. Follow this boundary pattern for save-index reads instead of raw feature-level `fetch` or handwritten transport types. Keep existing status behavior and tests where they continue to serve startup diagnostics. [Source: repository inspection, 2026-09-23; Story 1.1 review findings]
- `backend/src/dmud/main.py` builds the FastAPI app after SQLite/settings validation and registers the read-only status route. Register the new typed route there, with a cohesive query/model in a `saves` slice; preserve `/api/status`, backend-only settings, SQLite guard, and loopback Vite proxy. `tests/e2e/app.spec.ts` currently exercises the startup shell, API failure, and secret-canary boundary; update expectations to the Title without weakening those checks. [Source: repository inspection, 2026-09-23; Story 1.1 Dev Agent Record]

### Architecture, UX, and technical constraints

- Use `frontend/src/features/title/` for Title components and `frontend/src/features/session-zero/` for the minimal entry surface. Keep app composition in `frontend/src/app/`, shared API adapters in `frontend/src/api/`, and the read-only backend save-index query in `backend/src/dmud/saves/`. Domain code must not import FastAPI or SQLite; keep transport registration thin, query separate from writes, and one primary named function/component per application source file. Avoid speculative P1–P9 code or a generic service layer. [Source: `_bmad-output/game-architecture.md`, System Location Mapping; `_bmad-output/project-context.md`, Code Organization Rules; `/Users/kyle/.codex/standards/code-architecture.md`, Functions and Files]
- The checked-in lockfiles are authoritative. Story 1.1 pinned TypeScript **6.0.3** after the Architecture 1.2 recommendation of 7.0.2 conflicted with `typescript-eslint@8.69.0`; do not silently restore the earlier recommendation or float any dependency. React, TanStack Query, generated `@hey-api/openapi-ts` artifacts, and Zod already exist. No new runtime dependency is required by the specified behavior. [Source: `frontend/package.json`; `_bmad-output/implementation-artifacts/1-1-run-the-local-dmud-application-foundation.md`, Debug Log and Completion Notes]
- Keep Title copy factual: Continue is loading, no save exists, or save discovery failed. Do not tell the player a campaign or draft exists before one does. Error details must not expose SQL, stack traces, credentials, or hidden game state. No game time passes through menus or Session 0. [Source: `_bmad-output/game-architecture.md`, Transport and Query-State Contracts; `_bmad-output/project-context.md`, Engine-Specific and Critical Don't-Miss Rules]
- Use real buttons and semantic headings/status. Show a visible focus indicator and a reason adjacent to disabled Continue with an accessible association; ensure controls remain at least 24 × 24 CSS px or satisfy the documented spacing exception. Preserve browser text sizing and zoom, reflow at 320 CSS px without horizontal scrolling, and avoid motion essential to understanding. DESIGN specifies at least 4.5:1 normal text contrast and 3:1 focus/boundary contrast. [Source: `_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md`, Accessibility Floor, Component and State Patterns; `_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/DESIGN.md`, Accessibility and Components; [W3C Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum)]
- TanStack Query retries failed queries by default, so configure this foreground save-index read to expose a failure promptly and let the explicit Retry control refetch; preserve the query abort signal. Zod `parse`/`safeParse` provide the runtime success/error boundary, and schema failures must enter the error state. These are current library behaviors, not a reason to change pinned versions. [Source: [TanStack Query retry guide](https://tanstack.com/query/latest/docs/framework/react/guides/query-retries), [Zod basics](https://zod.dev/basics), `frontend/src/api/useStatus.ts`]

### Testing and completion evidence

- Map tests to each of the five acceptance criteria. Prefer real FastAPI ASGI and real Vite/FastAPI Playwright journeys; use parser tests for malformed payloads and observable UI states for failure/retry. Do not mock first-party routes or infer valid empty slots from failed network/schema reads. A loading-state browser test may hold the real backend response long enough to observe initial Title controls without substituting a fake route. [Source: `_bmad-output/project-context.md`, Testing Rules; `_bmad-output/planning-artifacts/epics.md`, NFR13, NFR16]
- Check keyboard order/activation, screen-reader names and disabled explanation, visible focus, 200% zoom/320 CSS px reflow, and reduced-motion operation. Record actual commands/results in the implementation report; the P0 exit plan retains the later full-stage gate. [Source: `_bmad-output/planning-artifacts/p0-verification-and-exit-plan.md`; `_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md`, Accessibility Floor]

### Project Context Rules

- Follow `_bmad-output/project-context.md` and the shared code-architecture standard: strict TypeScript/Python typing, validated external responses, vertical feature slices, explicit dependencies, generated API client, pure domain functions, one primary application function/component per file, and AAA tests of observable behavior. Use `PascalCase.tsx` components, `camelCase.ts` helpers/hooks, `snake_case.py` backend modules, and camelCase JSON. Exported and nontrivial functions need purpose/rationale/example documentation. No MCP integration is required. [Source: `_bmad-output/project-context.md`, Code Organization and Testing Rules; `/Users/kyle/.codex/standards/code-architecture.md`]

### References

- `_bmad-output/planning-artifacts/epics.md` — Epic 1; Story 1.2; Stories 1.3, 1.5, and 1.31; FR1; UX-DR18; NFR13 and NFR16.
- `_bmad-output/game-architecture.md` — System Location Mapping; Transport and Query-State Contracts; Runtime, Deployment, and Security.
- `_bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/gdd.md` — P0 Title and Session 0 entry.
- `_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md` and `DESIGN.md` — Title states, interaction and accessibility rules.
- `_bmad-output/implementation-artifacts/1-1-run-the-local-dmud-application-foundation.md` — established foundation and review fixes.
- `_bmad-output/project-context.md` — stack, organization, boundaries, testing, and platform rules.

## Dev Agent Record

### Agent Model Used

GPT-6 Codex

### Implementation Plan

1. Add a read-only FastAPI save-index query and contract tests, then regenerate OpenAPI and the frontend client.
2. Validate the complete generated response at the browser boundary and present its loading, empty, and error states on Title.
3. Enter a local Session 0 surface with no persistence or game-clock action; verify the journey with real API browser tests and all quality gates.

### Debug Log References

- Red phase: backend save-index test failed with 404; frontend parser suite failed because the parser did not exist.
- Sandbox uv cache access blocked the first browser run. The approved external browser test run passed. Direct `./.venv/bin/pyright` did not resolve its environment, so `uv run pyright` was used and passed.
- 2026-09-24: frontend format, lint, typecheck, build, Vitest (6 tests), backend Ruff format/lint, Pyright strict, pytest (5 tests), Playwright (5 tests), generated-contract drift, and `git diff --check` passed.
- 2026-09-24 follow-up: initially relocated browser tests to `frontend/tests/e2e/`; that setup was superseded by the fresh Playwright install under `frontend/e2e/`.
- 2026-09-24 follow-up: removed the config-side `@playwright/test` path mapping, then restored the three-server Playwright fixture in the new TypeScript config. The app browser journey passed in Chromium and Mobile Safari (10 tests).
- 2026-09-24 design-system follow-up: frontend format, lint, typecheck, build, Vitest (6 tests), Playwright (17 passed, 5 desktop-only tests skipped on Mobile Safari), and `git diff --check` passed.

### Completion Notes List

- Ultimate context engine analysis completed - comprehensive developer guide created.
- Added a read-only three-slot API; it never opens or writes a branch. Generated artifacts and a strict parser preserve read failures as errors.
- Replaced the startup panel with accessible Title states and a local, zero-time Session 0 handoff. Continue remains unavailable because this foundation has no compatible occupied slots.
- Covered the real proxy, loading, empty slots, failed reads and retry, keyboard entry, narrow layout with enlarged text, reduced motion, and secret-canary exclusion.
- The final browser test location is `frontend/e2e/`; the current config preserves the Chromium and Mobile Safari projects and starts all three local servers for the app journey.
- New Game browser coverage now checks that the current empty save index is unchanged; TODOs record the occupied-slot and fictional-time assertions that require future observable state.
- Paired the four player-flow browser checks with desktop keyboard-only tests and Axe scans, including enlarged text, narrow reflow, and reduced motion. Mobile Safari keeps the normal touch-flow coverage.
- Moved Title and Session 0 paragraph presentation into a typed CVA component styled with Tailwind 4; the roles and accessible descriptions remain on the rendered paragraphs.
- Applied the `docs/` campaign-book palette, typography, page framing, button treatment, and automatic dark theme to the existing Title and Session 0 surfaces.

### File List

- `_bmad-output/implementation-artifacts/1-2-open-the-title-and-start-a-new-game.md`
- `_bmad-output/implementation-artifacts/sprint-status.yaml`
- `_bmad-output/project-context.md`
- `backend/src/dmud/main.py`
- `backend/src/dmud/saves/__init__.py`
- `backend/src/dmud/saves/get_save_slots.py`
- `backend/src/dmud/saves/save_slots.py`
- `backend/tests/integration/test_save_slots.py`
- `contracts/openapi.json`
- `frontend/src/api/generated/@tanstack/react-query.gen.ts`
- `frontend/src/api/generated/index.ts`
- `frontend/src/api/generated/sdk.gen.ts`
- `frontend/src/api/generated/types.gen.ts`
- `frontend/src/api/generated/zod.gen.ts`
- `frontend/src/api/parseSaveSlots.test.ts`
- `frontend/src/api/parseSaveSlots.ts`
- `frontend/src/api/useSaveSlots.ts`
- `frontend/src/app/App.tsx`
- `frontend/src/app/app.css`
- `frontend/public/fonts/Lora-Regular.woff2`
- `frontend/public/fonts/Lora-Italic.woff2`
- `frontend/public/fonts/Lora-SemiBold.woff2`
- `frontend/public/fonts/Cinzel-SemiBold.woff2`
- `frontend/public/fonts/Cinzel-Bold.woff2`
- `frontend/public/fonts/LICENSES.txt`
- `frontend/src/components/ui/paragraph.tsx`
- `frontend/src/features/session-zero/SessionZero.tsx`
- `frontend/src/features/title/Title.tsx`
- `frontend/package.json`
- `frontend/package-lock.json`
- `frontend/.prettierrc.json`
- `frontend/eslint.config.js`
- `frontend/playwright.config.cjs` (replaced by TypeScript config)
- `frontend/playwright.config.ts`
- `frontend/e2e/app.spec.ts`
- `frontend/e2e/expectAccessiblePage.ts`
- `frontend/tsconfig.e2e.json`
- `frontend/tsconfig.json`
- `frontend/tsconfig.node.json`
- `frontend/vite.config.ts`
- `tests/e2e/app.spec.ts` (moved)

### Change Log

- 2026-09-24: Implemented Story 1.2 Title entry, read-only save discovery, strict browser validation, and real-boundary tests.
- 2026-09-24: Moved Playwright tests into the frontend package and updated paths, scripts, and project guidance.
- 2026-09-24: Connected the restored app browser suite to the API and Vite servers; verified both configured browser projects.
- 2026-09-24: Extended New Game browser coverage for the current save-index boundary and documented future occupied-slot and clock checks.
- 2026-09-24: Added keyboard accessibility counterparts and pinned `@axe-core/playwright` for automated page scans.
- 2026-09-24: Added Tailwind 4, CVA paragraph variants, and Tailwind-aware Prettier sorting; preserved Title and Session 0 semantics.
- 2026-09-24: Replaced Title's nested ternary with explicit branches and scoped Vitest to `src` after Playwright tests moved under `frontend/e2e/`.
- 2026-09-24: Updated the existing frontend surfaces to the new campaign-book design system and verified both color themes in Playwright.
