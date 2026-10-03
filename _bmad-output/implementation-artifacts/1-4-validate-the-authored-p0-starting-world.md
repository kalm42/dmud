# Story 1.4: Validate the Authored P0 Starting World

Status: ready-for-dev

## Story

As a player,
I want character confirmation to use a validated starting world,
so that I enter the same coherent Brackenford fixture every time.

## Acceptance Criteria

1. **Given** the application starts with the P0 content package, **when** authored YAML is loaded, **then** strict validation accepts exactly the approved three locations, four named NPCs, social conflict, five one-gold drinks, routes, movement rules, and controlled check content, **and** duplicate IDs, invalid references, unknown fields, or incompatible content versions fail before campaign mutation.
2. **Given** the validated starting package, **when** its deterministic fixture factory produces a pre-confirmation seed, **then** the seed provides Market Square, Mara's Stall, the Common Room, Mara, Oren, Tessa, Ivo, Mara's initial drink stock and transaction funds, and one prepared 10,000-gold pouch with no other player gold, **and** Mara and Tessa have authored starting positions that make the handover at Mara's Stall perceptible to Tessa but not to Oren or Ivo; the seed has a stable content version and immutable fixture origin suitable for later isolated branch creation without itself creating a campaign.
3. **Given** the authored payment-extension situation, **when** the P0 seed is validated and instantiated, **then** it contains one authoritative obligation record linking debtor Mara and creditor Oren, with 20 gold outstanding and an authored due second of 115,200 (day 2 at 08:00), **and** that stable record ID, balance, and deadline are part of the same branch state later extended by Story 1.24 and enriched with NPC motives by Story 2.1; neither story creates a replacement debt model.
4. **Given** authored content fails validation, **when** New Game or confirmation needs that content, **then** the player receives a recoverable, factual content-unavailable state, **and** no partial campaign, fixture funding, or world clock is created.

## Tasks / Subtasks

- [ ] Author the P0 content package (AC: 1–3)
  - [ ] Create `content/manifest.yaml` (content schema version, package ID and version) and the YAML files listed under *Project Structure Notes*. Use stable namespaced IDs (`location:brackenford:market-square`); IDs never derive from file paths. Add nothing outside the approved P0 set: no P1–P9 content, no fifth NPC, no `progression.yaml`, no speech or transfer timing rules (those belong to Stories 1.21/1.22/1.25).
  - [ ] Locations: Market Square, Mara's Stall, Common Room, each with an authored 60–120 word introduction (GDD G07) and readable exits. Market Square connects to both other locations; no other connections.
  - [ ] Routes and movement rules (G04): Market Square↔Mara's Stall 7 m, Market Square↔Common Room 140 m; speeds walk 1.4, jog 2.8, sprint 5.6, crawl 0.5 m/s; per-segment travel time rounds **up** to a whole second. Store values exactly (see *Technical guardrails*); do not use binary floats.
  - [ ] NPCs: Mara (stallholder), Oren (creditor), Tessa (neighboring trader), Ivo (courier, Tessa's friend). Identity, role, and starting location only. Needs, desires, plans, relationships, and knowledge are Story 2.1.
  - [ ] Item and funds: one `drink` definition priced 1 gold; Mara's stock of exactly 5; the prepared-pouch definition holding exactly 10,000 gold.
  - [ ] Social conflict (`maras-debt`) and the single `PaymentObligation` (debtor Mara, creditor Oren, 20 gold outstanding, due second 115,200).
  - [ ] Controlled check content `payment-extension`: Presence-based, Persuasion-skill, difficulty 12; success adds 86,400 s to the obligation deadline (115,200 → 201,600), failure leaves it unchanged. It references the obligation by ID. It does **not** carry player attribute values (see guardrails).
- [ ] Implement the strict loader and immutable registry in `backend/src/dmud/authored_content/` (AC: 1, 4)
  - [ ] Load with `yaml.safe_load` through a loader subclass that rejects duplicate mapping keys (plain `safe_load` silently keeps the last one). Then validate with strict Pydantic models (`extra="forbid"`, `strict=True`).
  - [ ] Validate in pure functions: exact P0 counts, unique IDs across all content kinds, every reference resolves, route endpoints exist, exits match routes, obligation parties are NPC IDs, check ↔ obligation linkage, extension arithmetic, introduction word counts, manifest schema/package version supported.
  - [ ] Return a typed result (`ContentLoaded` with an immutable `ContentRegistry`, or `ContentUnavailable` with bounded issues). Expected validation failures are data, not exceptions. Issues carry a code, content-relative file path, and field path; never absolute paths, stack traces, or raw YAML.
  - [ ] Do not read files at import time. The loader is the only I/O function; validation and registry construction are pure.
- [ ] Build the deterministic pre-confirmation seed (AC: 2, 3)
  - [ ] Add a pure factory that maps a loaded registry to a typed `P0StartingSeed`: locations, NPCs with starting locations, Mara's stock and funds, the pouch, the obligation, perception topology for the handover, content version, immutable fixture origin ID, and a digest of the canonical seed.
  - [ ] The seed creates no campaign, branch, clock, SQLite row, player character, attributes, or inventory entry. Same registry in, byte-identical canonical seed out.
  - [ ] Seed invariants: the only player gold is the single 10,000-gold pouch; every other gold holding is explicitly authored; the obligation ID, balance, and due second are fixed.
- [ ] Wire load-once-at-startup and the content-unavailable state (AC: 1, 4)
  - [ ] Add a validated `content_directory` setting (default: the repository `content/` directory) read only at the composition root. Load in `application_lifespan` off the event loop (`asyncio.to_thread`), store the result on `app.state`, and keep serving when content is invalid.
  - [ ] Importing the app or exporting OpenAPI must still read no content and open no database.
  - [ ] Gate New Game on availability: in `post_draft`, after the same-request duplicate lookup (so a previously accepted request is still recoverable) and before durable acceptance, return a typed RFC 9457 `content_unavailable` problem (`classification: "unavailable"`, factual detail, no operation or draft created). Add the code to the problem model, regenerate contracts.
  - [ ] Expose a pure `require_content`-style accessor for Story 1.9 so confirmation can fail before any mutation. Do not add confirmation logic.
- [ ] Surface the state in the frontend (AC: 4)
  - [ ] Parse the new problem via the generated schema. In `submitDraft.ts` today any error becomes `Error(problem.code)`, which the hook treats as an unknown outcome and offers "Recover request". A definitive `content_unavailable` rejection is not an unknown outcome: show factual text (what could not load, that nothing was started, that fixing the content and restarting the application is the recovery), keep New Game focusable, move no focus, and announce politely once.
  - [ ] Do not retain a recovery locator for a rejected creation (see Story 1.3 R7/R9 for locator rules). Do not store anything authoritative in browser storage.
- [ ] Verify (AC: 1–4)
  - [ ] Backend tests (see *Testing requirements*) against the real committed `content/` package plus deliberately broken copies in `tmp_path`.
  - [ ] Frontend component/parser tests for the new problem and a Playwright journey with an isolated broken content directory.
  - [ ] Run every gate listed under *Testing requirements* independently.

## Dev Notes

### Scope and handoffs

- Stories 1.1–1.3 are done. 1.3 built the durable draft operation contract; this story adds the first authored content, strictly validated, plus the seed that Story 1.9 will instantiate. It creates **no** campaign, branch, clock, or save.
- Downstream consumers that fix names/IDs you choose here: 1.5 (contradiction checks against the fixture), 1.9 (confirmation instantiates the seed at Market Square, second 28,800 and owns the clock and branch), 1.14/1.17/1.19/1.20 (routes, speeds, locations), 1.21–1.22 (drink purchase, pouch transfer), 1.24 (payment-extension check against the obligation ID), 2.1 (NPC state extends the same obligation), 2.4 (witness perception at Mara's Stall). Treat chosen IDs as permanent. [Source: `_bmad-output/planning-artifacts/epics.md` Stories 1.5, 1.9, 1.14–1.24, 2.1–2.4]
- Traceability: FR6, FR19, FR21, FR22, FR83, FR84 (`epics.md#P0 Story-Level FR Traceability`). This is feature evidence, not the P0 gate. [Source: `p0-verification-and-exit-plan.md`]

### Technical guardrails (the non-obvious ones)

- **Duplicate YAML keys**: PyYAML `safe_load` accepts them and keeps the last value. AC1 requires duplicate IDs to fail, so the loader must reject duplicate keys itself and also detect duplicate `id` values across files.
- **No coercion**: use Pydantic strict mode so `"20"` is not accepted as 20 and `yes`/`no`/`on` YAML scalars cannot become booleans by accident. Unknown fields are errors in every model, including nested ones.
- **Exact travel arithmetic**: `7 / 1.4` style float division followed by `ceil` can misround. Store lengths and speeds as integers in a smaller unit (e.g. millimetres and millimetres per second) or as quoted decimal strings parsed to `Decimal`, and test that walking is exactly 5 s and 100 s, and every mode on both routes matches integer ceiling division. Story 1.20 will consume these values.
- **Controlled evidence values vs. player character**: Presence 14, Persuasion +1 belong to the controlled evidence fixture (GDD "controlled payment-extension check"), not to every player. Session 0 lets the player assign the 8/10/12/13/14 array (Story 1.7). The seed must contain no player attributes and no skill bonuses. Difficulty 12 and the +86,400 s consequence are check content.
- **10,000 gold is fixture funding, not an ordinary balance**: it must carry an explicit fixture origin so conservation checks cannot merge it with other ledgers. Purchase, gift, and no-gift evidence branches each start from an isolated copy of this same seed; the seed itself must be immutable and copyable. [Source: Architecture, ADR-007; GDD G05]
- **Production content vs. test starting states**: the starting-state definition used by real confirmation (Story 1.9 puts the pouch in the player's real initial inventory) lives in the content package, e.g. `content/worlds/brackenford/start.yaml`. `backend/tests/fixtures/worlds/` stays reserved for later captured states (`p0-gift-committed`, `p0-no-gift`) and is not created here.
- **Handover perception (AC2)**: perception must be authored data, not inferred from prose. Recommended: Mara and Tessa start at Mara's Stall; Oren and Ivo start at the Common Room. Add a validated invariant that the handover location's perceivers are exactly {Tessa} plus the participants, and Oren and Ivo are not co-located. Story 2.3/2.4 record witnesses from this topology. *(Starting positions other than Mara and Tessa are unspecified by the GDD; see open questions.)*
- **Registry immutability**: frozen models, tuples, and read-only mappings only. Production never hot-reloads. Lookup is by stable ID.
- **Bounded failure reporting**: log an issue count and codes at warning level; never log content bodies, absolute paths, or secrets. Player-facing text states only that the starting world could not be loaded and nothing was started.
- **Strict domain purity**: validation, seed building, and digest calculation are pure and import no FastAPI, SQLite, `os.environ`, or file APIs. Only the loader touches the filesystem.
- **One named function per source file**, named after it, with purpose/rationale/example docstring; snake_case Python, camelCase JSON, snake_case YAML keys and wire enums, kebab-case YAML filenames. [Source: `_bmad-output/project-context.md#Code Organization Rules`]

### Existing files: current state and what changes

| File | Current behavior | Change | Preserve |
| --- | --- | --- | --- |
| `backend/src/dmud/main.py` | `create_app` validates SQLite, builds `Settings`, registers routes, lifespan; constructs `app` at import | Nothing beyond passing settings; keep composition root thin | No file/DB access at import; OpenAPI export stays side-effect-free |
| `backend/src/dmud/platform/settings.py` | `llm_api_key`, `application_data_directory` (`DMUD_` prefix) | Add `content_directory` with repo-`content/` default | Secret stays backend-only; features never read env |
| `backend/src/dmud/platform/application_lifespan.py` | Initialize DB, reconcile, start worker, shutdown | Load content once (thread), set `app.state.content` | Startup order for DB/worker; invalid content must not stop the app |
| `backend/src/dmud/operations/post_draft.py` | Accepts via `run_database(accept_operation, …)` then wakes worker | Content-availability gate after duplicate lookup, before acceptance | Idempotent replay, wake-after-accept behavior, 1.3 recovery contract |
| `backend/src/dmud/operations/models.py`, `problem_response.py`, `render_problem.py` | `ProblemCode` and classifications `conflict`/`invalid_input`/`not_found`/`unavailable` | Add `content_unavailable` code (`unavailable`) | Existing codes, correlation IDs, RFC 9457 shape |
| `frontend/src/api/submitDraft.ts`, `operationProblem.ts`, `parseProblem.ts`, `features/operation-progress/useDraftOperation.ts`, `OperationProgress.tsx`, `features/title/Title.tsx` | Errors become unknown-outcome recovery; New Game retains request ID | Handle definitive `content_unavailable` as a rejection, not an unknown outcome | Request-ID retention for genuinely unknown outcomes, 30 s deadline, heading focus, stable focus, save-retry, deduplicated status |
| `contracts/openapi.json`, `frontend/src/api/generated/` | Generated | Regenerate with existing scripts; never hand-edit | Drift gate |
| `backend/tests/conftest.py` | Autouse isolated data dir | Add content-directory isolation only for broken-content tests | Existing isolation |

Read these files fully before editing; the table summarizes the state captured on 2026-10-02 from the 1.3 review baseline (`466c249`).

### Project Structure Notes

- **NEW (content, repository root):** `content/manifest.yaml`, `content/rules/movement.yaml`, `content/worlds/brackenford/{world.yaml, start.yaml, locations/{market-square,maras-stall,common-room}.yaml, npcs/{mara,oren,tessa,ivo}.yaml, items/drink.yaml, conflicts/maras-debt.yaml, checks/payment-extension.yaml}`. This follows the architecture tree except `start.yaml` (the starting-state/fixture definition) and the deliberate omission of `progression.yaml` and checks beyond payment extension. `world.yaml` owns geography and routes. Note in the Dev Agent Record that packaging `content/` into the served build is Story 1.35.
- **NEW (backend):** `backend/src/dmud/authored_content/` (`models`, loader, validators, registry, `build_p0_seed`, `require_content`), one function/model family per file; tests under `backend/tests/` using `test_<behavior>.py`.
- **Edits:** files in the table above. Do not add `services/`, `managers/`, generic helpers, a global registry, a hot-reload, or P1+ modules.

### Previous story intelligence (1.3)

- The operation store, worker, and recovery are fragile in specific ways that were hardened in review (SQLite reads in snapshots, DB calls off the event loop via `run_database`, 30 s deadlines, locator rules, rejected recovery commands retired). Do not alter them; add the content gate as a small step ahead of acceptance and reuse `run_database`-style off-loop discipline for file I/O.
- 1.3 deliberately created an empty draft with no content compatibility evidence. Do not add content version fields to `SessionZeroDraft` here; Story 1.5/1.9 decide when compatibility evidence is recorded.
- Quality gates were run independently and recorded; backend 51 passed, frontend 18 passed, Playwright 50 passed with 6 existing skips at the end of 1.3. Treat as historical baseline, not proof for this branch.

### Git intelligence

Recent: `466c249 Story 1.3 (#2)`, `3c1d121 Merge PR #1 (story 1.2)`, CI fixes to uv 0.12.0 and Python 3.14. Pattern: one story per `feat/story-N-M` branch, review findings fixed on-branch, generated contracts committed.

### Library and framework requirements

PyYAML 6.0.3 and Pydantic 2.13.5 are already pinned in `backend/pyproject.toml`; no new dependency. Frontend pins unchanged (React 19.2.8, TanStack Query 5.102.8, Zod 4.5.4, `@hey-api/openapi-ts` 0.99.0). No web research was needed; do not float versions.

### Testing requirements

Real code paths only; no mocks of first-party content, routes, or persistence. AAA, one behavior per test, top-level `describe` named for the subject.

| AC | Evidence |
| --- | --- |
| 1 | Committed package loads and registry has exactly 3/4/1/5-stock/2 routes/4 speeds/1 check; separate tests for duplicate YAML key, duplicate ID across files, dangling reference, unknown field (top-level and nested), wrong type (`"20"`), unsupported manifest/schema version, extra/missing location or NPC, exit/route mismatch, introduction outside 60–120 words; each failure returns `ContentUnavailable` with a path-relative issue and mutates nothing |
| 1 | Walk/jog/sprint/crawl times on both routes equal exact integer ceiling; walking is 5 s and 100 s |
| 2 | Seed content: three locations, four NPCs with starting positions, 5 drinks at 1 gold, Mara's explicit funds, exactly one 10,000-gold pouch, no other player gold, no attributes/clock/campaign; perception topology: Tessa perceives, Oren and Ivo do not; same registry yields byte-identical seed and digest; mutating a returned seed copy cannot change the registry |
| 3 | One obligation: debtor Mara, creditor Oren, 20 gold, due 115,200; payment-extension arithmetic gives 201,600 on success and leaves 115,200 on failure; no second debt record exists anywhere in the seed |
| 4 | With a broken `content_directory`, the real ASGI app starts, `POST /api/session-zero-drafts` returns the typed `content_unavailable` problem and the database has no operation, draft, campaign, funding, or clock rows; an already-accepted request ID still replays after content later fails; import/OpenAPI export reads no content |
| 4 (UI) | Component/parser test for the problem; Playwright: New Game against broken content shows the factual state, keeps New Game focusable, creates no recovery locator, and announces once; existing Title and recovery journeys still pass |

Gates (run independently):

```text
frontend: npm run format:check
frontend: npm run lint
frontend: npm run typecheck
frontend: npm run build
frontend: npm test
backend: uv run ruff format --check src tests scripts
backend: uv run ruff check src tests scripts
backend: uv run pyright
backend: uv run pytest
repository root: python3 scripts/check_contract.py
frontend: npm run test:e2e
repository root: git diff --check
```

### Project Context Rules

From `_bmad-output/project-context.md` (all apply): the FastAPI backend is authoritative and React only renders server state; authored YAML is versioned with stable IDs and validated strictly into an immutable registry loaded at startup and never hot-reloaded; runtime content never rewrites authored files; dependencies point inward and are injected from composition roots; no env reads in feature/domain modules; one named function or component per file; pure by default; no nested ternaries; document exported and non-trivial functions with purpose, rationale, and an example call; React components use named props types, destructure in the body, and default-export at the bottom; never trust persisted or external data without strict runtime validation; return typed results for expected failures and catch exceptions only at boundaries; never create locations procedurally; never add speculative P1/P2 modules; never log secrets or raw payloads; keep the generated API client uncommitted-by-hand; browser storage holds no authoritative state; no suggested actions or strategy-steering controls. No MCP integration is required.

### Open questions for Kyle (non-blocking; defaults chosen above)

1. **Mara's "transaction funds"** (AC2): the GDD does not state Mara's starting gold. Default: author an explicit value of 0 so gold conservation is exact and her only liquidity comes from the player. Confirm or give a number.
2. **Starting positions of Oren and Ivo**: GDD fixes only that Tessa meets Ivo in the Common Room 1,800 s after the gift opportunity and that Oren/Ivo must not perceive the handover. Default: Mara and Tessa at Mara's Stall; Oren and Ivo at the Common Room.
3. **Gating New Game on content**: AC4 says "when New Game or confirmation needs that content". Default: New Game is refused with `content_unavailable` before durable acceptance. If you prefer New Game to keep working and only confirmation (Story 1.9) to fail, drop the `post_draft` gate and the frontend task, and keep only the `require_content` accessor.

### References

- `_bmad-output/planning-artifacts/epics.md` — Story 1.4; Epic 1 handoffs (1.5, 1.9, 1.14–1.24); Story 2.1; Shared Delivery Definition of Done.
- `_bmad-output/game-architecture.md` — Asset and Authored-Content Management; Content and Asset Rules; Directory Structure; Data Patterns; ADR-007; Persistence and Verification Matrix.
- `_bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/gdd.md` — G04 fixture values; G05 scenario; G07 location text; payment-extension check; P0 content inventory.
- `_bmad-output/planning-artifacts/p0-story-dependency-review-2026-09-23.md` — obligation ownership across 1.4, 1.24, 2.1.
- `_bmad-output/planning-artifacts/p0-verification-and-exit-plan.md` — isolated ledgers, `p0-gift-opportunity` marker (not created here).
- `_bmad-output/project-context.md`.
- `_bmad-output/implementation-artifacts/1-3-track-a-recoverable-session-0-operation.md` — operation, problem, and recovery contracts to preserve.

## Dev Agent Record

### Agent Model Used

Claude Sonnet 5.5 (story context creation).

### Debug Log References

- Workflow customization resolved: no prepend/append steps, persistent facts, or completion instruction.

### Completion Notes List

- Ultimate context engine analysis completed - comprehensive developer guide created.

### File List
