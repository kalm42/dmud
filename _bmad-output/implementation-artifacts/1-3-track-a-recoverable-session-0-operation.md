# Story 1.3: Track a Recoverable Session 0 Operation

Status: ready-for-dev

## Story

As a player,
I want the start of Session 0 to have a durable request and status,
so that refresh or interruption cannot leave me unsure whether it started.

## Acceptance Criteria

1. **Given** the first durable Session 0 operation needs local storage, **when** the backend initializes application data, **then** its first ordered migration creates only the draft and operation records needed by this story in SQLite `STRICT` tables through typed infrastructure adapters, **and** a SQLite runtime older than 3.37.0 fails before application data opens or mutates with a clear, secret-free error.
2. **Given** New Game starts a Session 0 draft subject, **when** the first zero-time operation is accepted, **then** the server creates one idempotent, revisioned `SessionZeroDraft` and durably records its subject, request ID, payload digest, revision, and ordered status events before returning its operation ID, **and** duplicate IDs with identical payloads return the same operation while changed payloads receive a typed conflict.
3. **Given** a draft-subject operation is accepted, running, complete, failed, or interrupted, **when** its status is queried, **then** the typed response reports the authoritative state and last event ID, **and** the Session 0 surface never treats an unacknowledged request as committed.
4. **Given** the event connection drops or the browser refreshes, **when** the client reconnects with its last event ID or polls the status endpoint, **then** it recovers the same ordered operation and draft subject without rerunning the request, **and** the pending or terminal state remains visible and accessible.
5. **Given** the backend restarts with a nonterminal draft operation, **when** startup reconciliation reads its durable operation record, **then** an uncommitted request becomes explicitly interrupted and a committed draft result remains available, **and** recovery never fabricates a campaign or advances fictional time.
6. **Given** a failed or interrupted draft operation is retried, **when** its recovery action runs, **then** only the supported uncommitted work is retried under the same draft subject, **and** later answer, reflection, and confirmation operations can use this same contract without a second operation store.

The criteria above preserve the governing backlog. Cooperative cancellation, strict success/problem/event validation, atomic commit evidence, and accessible recovery also apply through FR31–FR33, NFR4/NFR13/NFR16/NFR19, and the shared delivery definition of done.

## Tasks / Subtasks

- [ ] Initialize durable application data safely (AC: 1, 5)
  - [ ] Extend backend-only validated settings with an explicit application-data directory and inject the resolved configuration from `create_app`. Keep SQLite version validation ahead of directory creation and database access.
  - [ ] Add an ordered, transactional first SQL migration and typed SQLite adapters for draft state, operations, ordered operation events, request results, minimal immutable draft-commit evidence, and migration bookkeeping. Do not create campaign, branch, save, world, NPC, or future-stage tables.
  - [ ] Initialize/migrate/reconcile during FastAPI lifespan; shut down the supervised worker and close resources safely. Importing the app or exporting OpenAPI must not open a database, run migrations, or start work.
  - [ ] Give integration tests and Playwright explicit isolated temporary data directories; update lifecycle-aware tests to enter `TestClient` as a context manager. Document the data directory and restart behavior in README.
- [ ] Define and persist the shared operation contract (AC: 2, 3, 5, 6)
  - [ ] Implement a versioned minimal `SessionZeroDraft`, `CreateSessionZeroDraft`, and `GetSessionZeroDraft` in `session_zero/`, with stable ID, draft revision, collecting lifecycle, schema version, and active-operation reference. Establish empty draft material without fabricated answers, attributes, reflection, or content compatibility evidence.
  - [ ] Add strict Pydantic request/resource/result/event/problem models with camelCase wire fields, typed subject identity, commit boundary, committed revision, last event ID, and explicit safe recovery capability. Creation has no expected prior draft revision; commands against an existing draft require `expectedDraftRevision`.
  - [ ] Add pure legal lifecycle transitions plus separate read/write persistence paths in `operations/`. Enforce a unique logical request identity, canonical payload digest, and a single executing mutation for a draft subject. Duplicate acceptance must be resolved transactionally, including simultaneous requests.
  - [ ] Persist acceptance before exposing its ID; supervise a real in-process draft-create command. Commit the draft, its revision, immutable audit evidence, request result, and committed operation/event together. Complete delivery afterward without a second draft mutation.
  - [ ] Implement startup reconciliation against request results before any resumption; uncommitted nonterminal work becomes interrupted and committed work exposes the original result. Retry must check that same result again inside its transaction.
- [ ] Expose strict creation, status, streaming, and recovery boundaries (AC: 2–6)
  - [ ] Register `POST /api/session-zero-drafts`, `GET /api/session-zero-drafts/{draftId}`, `GET /api/operations/{operationId}`, `GET /api/operations/{operationId}/events`, and `POST /api/operations/{operationId}/cancel` through thin handlers.
  - [ ] Implement `POST /api/operations/{operationId}/retry` without changing the original operation/request/subject identity. Cancel/retry envelopes carry a separate recovery-command `requestId` and `expectedLastEventId`; persist their idempotent outcome so repeats cannot launch concurrent attempts. This retry route is a selected story extension, not a previously specified architecture endpoint.
  - [ ] Return `202 Accepted` with operation/status/events references after durable acceptance. Identical original submissions retrieve existing status/result; changed payloads return a typed conflict. Use RFC 9457 problems for conflicts, invalid input, unknown IDs, and unavailable/corrupt reads.
  - [ ] Persist typed versioned SSE events with monotonic IDs, replay strictly after `Last-Event-ID`, and provide polling independently of streaming. Validate cursor input and document recovery for invalid/out-of-range cursors; never invent missing history or rerun work to rebuild it.
  - [ ] Implement cooperative cancellation before commit. If commit wins the race, return the authoritative committed result and stop only delivery work. A disconnected browser or SSE consumer must not cancel the operation.
  - [ ] Export OpenAPI and regenerate the committed client, types, Zod schemas, and Query bindings using the existing scripts. Document event payload schemas in OpenAPI so event parsing uses generated schemas too.
- [ ] Connect New Game to truthful operation recovery (AC: 2–6)
  - [ ] Replace the local placeholder-only handoff with one user-triggered creation request. Acknowledge immediately, retain its request ID before sending, and prevent repeat activation while its outcome is unknown. Avoid mutation-on-mount, including React StrictMode duplicate effects.
  - [ ] Preserve a validated non-authoritative refresh locator using the smallest existing-app-compatible mechanism, such as URL state. It may identify the request/operation/draft and event cursor, but may contain no authoritative draft content. Before the operation ID is received, preserve enough request identity to recover a lost acceptance response safely.
  - [ ] Use generated SDK adapters, strict runtime validation, identity-scoped Query keys, and polling fallback. Recover the original operation on refresh; stale events or query responses for a different subject cannot replace the active view. Never let a failed read look like a failed authoritative mutation or known-empty draft.
  - [ ] Show accepted/running, complete, failed, interrupted, and unknown/unavailable status in text with the commit boundary and supported recovery controls. Keep status and controls keyboard accessible, preserve focus through retry, and announce changes politely without repeated announcements on every poll.
  - [ ] Preserve Title New Game independence from save discovery, empty Continue semantics, and Session 0 heading focus. Use current runtime UI primitives/theme; no composer, Rowan question, answer editing, review, or campaign entry in this story.
- [ ] Verify real persistence and recovery behavior (AC: 1–6)
  - [ ] Add real FastAPI/isolated SQLite integration tests for migration, acceptance/idempotency, typed reads, SSE replay, cancellation/retry, rollback, concurrent requests, and restart before/after commit.
  - [ ] Extend Playwright against real Vite/FastAPI for New Game, response-loss/refresh recovery, SSE loss with polling, and accessible failure/retry. Use deterministic scheduling barriers, not sleeps, to observe intermediate states of the fast local operation.
  - [ ] Preserve Title save retry/focus, secret-canary, Chromium/Mobile Safari, and existing parser coverage. Map each AC to observable tests and record commands/results without claiming future Session 0 or P0 completion.
  - [ ] Run the independent existing format, lint, strict typing, backend/frontend tests, build, browser, and contract drift gates listed below.

## Dev Notes

### Scope, dependencies, and handoffs

- Stories 1.1 and 1.2 are done. This story introduces the first storage and durable operation flow. Story 1.4 owns authored-content validation; 1.5 owns Rowan's name question, exact-answer persistence, the shared composer, and the shared conversation `response-status`; 1.6 extends recovery to answered drafts and known-draft resumption; 1.7–1.8 own attributes/reflection; 1.9–1.10 own atomic campaign confirmation. Stories 1.14–1.18 later reuse and extend operations for world actions. [Source: `_bmad-output/planning-artifacts/epics.md#Epic 1: Enter and Act in a Small Persistent World`]
- Creation here is deterministic and local: no provider call, tactical suggestion, authored world, campaign origin, branch, clock, inventory, or gold. Do not add an LLM gateway or pretend interpretation/narration occurred merely to exercise lifecycle labels. Implement the common operation infrastructure now, with only the draft-create command registered. Future command kinds extend that same store/worker/transport, rather than introducing another conversation engine. [Source: Architecture, Request Lifecycle and Transport; ADR-006; current Story 1.3/1.5 boundaries]
- Traceability: FR2–FR3 (durable draft foundation), FR31–FR33 (operations/recovery/idempotency); particularly NFR2, NFR4, NFR6, NFR12–NFR13, NFR15–NFR16, NFR19. This story supplies feature evidence, not the full P0 promotion gate. [Source: Epics, P0 Story-Level FR Traceability; `_bmad-output/planning-artifacts/p0-verification-and-exit-plan.md`]

### Acceptance, commitment, and operation state

An accepted operation is durable coordination evidence, not proof that its subject mutation committed. Reserve a stable draft ID and operation/request identity during acceptance; create the authoritative collecting draft and positive initial revision in the atomic draft commit. In AC2, creation is the accepted operation's eventual subject result; the `202` response acknowledges durable acceptance, not a saved draft. Do not persist a provisional draft as authoritative empty content. Before commit, a draft read returns a documented typed `draft_not_committed` 404 with operation/recovery metadata; the operation read remains available. A failed attempt retains the reserved subject so retry cannot allocate a second draft. Every returned operation ID must already be recoverable from SQLite. [Source: Epics Story 1.3; Architecture, Restart Recovery and ADR-006; selected implementation interpretation of the acceptance/commit boundary]

Use explicit discriminated states. The common contract may represent `accepted`, `interpreting`, `needs_clarification`, `validating`, `resolving`, `committed`, `narrating`, `complete`, `failed`, and `interrupted`; draft creation only visits stages it actually performs. Public “running” is a truthful projection of reached states, not a competing persisted boolean. Draft lifecycle stays `collecting`; provider/task status belongs to the operation. [Source: Architecture, Request Lifecycle and Transport; ADR-006; Project Context, Engine-Specific Rules]

| Durable evidence | Authoritative meaning | Safe recovery |
| --- | --- | --- |
| No accepted ID/result known by client | Outcome unknown; never claim saved or failed-before-commit | Recover using original creation request identity and payload |
| Accepted/nonterminal; no request result | Uncommitted work for the reserved draft subject | Query; cooperative cancel; after explicit interruption, retry supported work |
| Committed result; delivery pending | Draft exists at the recorded revision, boundary `draft` | Return/read original result; finish delivery only |
| Complete | Original draft result remains authoritative | Read/replay status; repeated creation request returns original identity |
| Failed/interrupted without result | No draft mutation committed by that attempt, boundary `none` | Explicit retry under original operation/request/subject identity |
| Status transport/schema failure | Current operation outcome cannot be established from that read | Preserve prior data as stale, query again; never start a new logical request automatically |

Store the canonical validated creation envelope and its digest; include command kind/subject and applicable expected revision in identity comparison. Perform duplicate lookup before allocating IDs or rejecting a previously successful request against a now-stale revision. A same-ID replay is a read/recovery path, not permission to start another worker. The explicit retry command can reopen only a recoverable uncommitted attempt after rechecking its authoritative result and subject eligibility. Multiple retries/cancel/commit must serialize through SQLite uniqueness and transactional checks. [Source: Architecture, Wire Format; Restart Recovery; ADR-006; Epics FR33]

Creation has no existing revision and must not require `expectedWorldRevision`. Return a positive initial draft revision, document its convention, and reserve `expectedDraftRevision` for commands changing an existing authoritative draft. Cancel/retry of uncommitted creation cannot require a nonexistent draft revision. Their separate recovery-command `requestId` identifies only that recovery action; the route identifies the original operation, and the server loads its immutable original creation request/payload/subject. Check `expectedLastEventId` and eligibility transactionally after duplicate recovery-command lookup. Stale/ineligible recovery returns a typed 409 with current status; accepted retry returns the same operation reference, and committed retry returns the original result without scheduling work. `committedRevision` is absent/null before commit. Operation results identify `session_zero_draft`, draft ID, boundary `none`/`draft`, and supported recovery. Do not fabricate `world` evidence. Server resource IDs use a prefix plus Python 3.14 UUIDv7; browser request IDs use `req_` plus `crypto.randomUUID()` UUIDv4. [Source: Architecture, Wire Format; Transport and Query-State Contracts; Naming Conventions; selected recovery-envelope extension]

### Persistence, atomicity, and supervision

- Use Python standard-library `sqlite3` behind typed infrastructure adapters. The minimal migration needs `session_zero_drafts`, `operations`, `operation_events`, `request_results`, migration bookkeeping, and minimal draft audit evidence. The audit evidence can be a small slice-owned record or the common action-record representation restricted to draft commits; do not create the entire architecture schema upfront. All application-owned tables use `STRICT`, appropriate unique/check constraints, and relational linkage. Strict SQL typing does not replace strict Pydantic validation of persisted JSON. [Source: Architecture, Data Persistence and Restart Recovery]
- Acceptance is one transaction; authoritative draft commit is another transaction. The latter writes draft state/revision, immutable commit evidence, original request result, committed operation state, and its event atomically. If any write fails, rollback leaves all authoritative commit artifacts absent. A subsequent safe operation-failure record must not claim a draft commit. Do not hold a transaction or connection lock open while streaming, awaiting model work, or waiting on browser delivery. [Source: Architecture, Causal Action Transaction; Restart Recovery]
- Migrations are explicit ordered SQL files, not implicit create-on-query. Repeated startup does not rerun applied migrations; failed migration does not record success or leave a half-created schema. Reject unsupported newer schema versions safely. Configure connection concurrency/foreign-key behavior deliberately and use transactional revision/uniqueness checks rather than browser locks. [Source: Architecture, Data Persistence; NFR13/NFR20]
- The supervised in-process worker must claim each runnable operation at most once, coordinate cancellation at the commit boundary, persist failure/interruption, and survive consumer disconnects. Reads remain available during work. Do not rely solely on ephemeral background tasks or an in-memory queue for recovery. On restart, check `request_results` first; never auto-execute uncommitted work. This story has no narration job, so a recovered committed create operation may finish result delivery directly without inventing prose work. [Source: Architecture, Request Lifecycle and Transport; Restart Recovery]
- Configure data in an explicit writable backend-owned location, excluded from git. Read validated settings only at the composition root. Contract export must remain side-effect-free. Test suites must not use the developer's real database, share mutation state between parallel workers, or silently require an ambient data directory. [Source: Project Context, Platform & Build Rules; repository `main.py`, `export_openapi.py`, Playwright config]

### Transport and frontend recovery

- Creation: `POST /api/session-zero-drafts` with a strict versioned command envelope and unique `requestId`. Accepted responses expose the durable operation identity, typed subject, status/events URLs; duplicates expose that same identity/result. Read endpoints never create a draft or execute work. Unknown IDs are typed 404s. Document every success/problem status and content type in OpenAPI. [Source: Architecture, Wire Format and Transport and Query-State Contracts]
- RFC 9457 problems use `type`, `title`, `status`, `detail`, `instance`, stable `code`, `classification`, `correlationId`, and applicable operation/draft revision/recovery metadata. New draft metadata is an explicit contract extension, not a world revision. Schema failures, busy conflicts, changed payloads, recoverable infrastructure failures, and terminal failures remain distinct. Return safe correlation context, never secrets, SQL, stack traces, or provider payloads. [Source: Architecture, Error Handling; Wire Format]
- SSE is a read-only projection of persisted events; IDs increase across interruption and retry and never reset per attempt. Event identity and body must agree on operation/subject/version, with runtime validation before cache changes. Resume after the last validated event; ignore duplicates and never let older events regress a newer status snapshot. Close terminal streams, clean up subscriptions on subject switch/unmount, and fall back to bounded polling when streaming is unavailable or invalid. Polling stops on confirmed terminal state; an unavailable read preserves an explicit unknown/recovering state. [Source: Architecture, Request Lifecycle and Transport; Transport and Query-State Contracts]
- A full browser refresh loses React state and an in-memory query cache. Preserve a validated recovery locator before send and update it after acknowledgement. A URL request/operation locator is a bounded implementation choice for this story; a validated local pointer is also allowed, containing identifiers only. Story 1.6 still owns choosing/resuming older answered drafts and distinct-New-Game confirmation. If the acceptance response is lost, replay the original creation envelope with the same ID to locate the existing operation; do not generate a new ID. Failed/unknown recovery never silently starts a different draft. [Source: ADR-006; Epics Stories 1.3 and 1.6]
- Acknowledge New Game within the 100 ms target without saying “saved.” A recoverable unknown/pending/interrupted view must exist by 30 seconds; that threshold triggers a status/recovery path and must not falsely declare that the server cancelled or failed. Success copy may say the draft was started only after validated `draft` commit evidence. Controls are recovery actions, not game-strategy suggestions. Keep presentation lightweight; the full composer/conversation status is Story 1.5. [Source: NFR2; GDD, Platform and Performance Requirements; EXPERIENCE, State Patterns]

### Existing files: current behavior, changes, and preservation

| File / current behavior | Change for this story | Preserve |
| --- | --- | --- |
| `backend/src/dmud/main.py`: validates SQLite/Settings, registers two read routes, constructs app at import | Inject validated configuration, register draft/operation routes and lifespan dependencies | Guard before data access, thin root, status/save reads; import/OpenAPI export without storage side effects |
| `backend/src/dmud/platform/settings.py`: optional backend-only secret, no data configuration | Add validated application-data configuration | Secret remains backend-only; feature modules do not read environment |
| `backend/src/dmud/platform/require_sqlite.py`: rejects versions below 3.37.0 | Reuse ahead of all persistence initialization; no rewrite needed | Clear secret-free failure and existing test seam |
| `frontend/src/app/App.tsx`: ephemeral Title/Session 0 surface state | Compose creation/recovery location and selected authoritative operation | Semantic main; no router dependency unless the bounded locator requires it |
| `frontend/src/features/title/Title.tsx`: immediate New Game/Continue, read-only save query, stable retry focus | Connect existing New Game callback to one durable creation intent | New Game independent of save-index failures; Continue reserved for campaign saves |
| `frontend/src/features/session-zero/SessionZero.tsx`: heading focus on entry, character-creation placeholder | Render truthful draft-start operation and its recovery controls | Heading focus on entry; no focus theft during polling or retry |
| `frontend/src/api/useSaveSlots.ts`, `parseSaveSlots.ts`: generated SDK/Query plus strict ingress validation | Reuse pattern for new operation adapters; no rewrite needed | Signals, explicit failure, generated schema validation |
| `backend/scripts/export_openapi.py`, `frontend/openapi-ts.config.ts`, `scripts/check_contract.py`: deterministic export/generation/drift | Extend backend contract; only change scripts if needed to maintain side-effect-free generation | Generator-owned artifacts; existing plugin chain and drift gate |
| `backend/tests/integration/test_status.py`, `test_save_slots.py`: real ASGI reads, no lifespan/data currently | Introduce isolated app fixtures/lifespan when required | Status, read-only empty saves, canary and unsupported SQLite assertions |
| `frontend/e2e/`, `frontend/playwright.config.ts`: real API/available and unavailable proxies, parallel browser journeys | Isolate persistent data and extend durable entry/recovery journeys | Real first-party boundary, Chromium and Mobile Safari, canary exclusion, stable focus and save retry |
| `README.md`, `.github/workflows/quality.yml`: local commands and independent gates | Document data/restart semantics; adjust setup only where persistence needs it | Locked installs, both browser engines, independent quality gates |

These current source files were read during context creation. The architecture's diagram is a target map, not proof that its proposed modules already exist.

### Project Structure Notes

- **NEW:** `backend/src/dmud/session_zero/` for creation models, pure command validation, query projection, and draft-specific typed adapters; `backend/src/dmud/operations/` for lifecycle, worker, reads/writes, streams and recovery; `backend/src/dmud/platform/sqlite/` for concrete connections/migration capabilities, with `migrations/0001_initial_schema.sql` beneath it. Use one coherently named function per application source file rather than copying the diagram's multi-handler `api.py` or catch-all `store.py` literally. [Source: Architecture, Directory Structure and System Location Mapping; Project Context, Code Organization Rules]
- **NEW:** API adapters in `frontend/src/api/`; operation tracking in `frontend/src/features/operation-progress/`; Session 0 composition stays in `features/session-zero/`. Reuse actual `components/ui/` primitives and `app/theme.css`/`app.css` styling. Existing browser tests are `frontend/e2e/`, superseding the older architecture/context paths. [Source: repository; Story 1.2 Completion Notes and whole-branch review]
- **GENERATED:** `contracts/openapi.json`, `frontend/src/api/generated/`. Regenerate, never hand-edit or handwrite competing transport types. Define slice-owned types before promoting stable concepts to `foundation/`; do not create generic managers, services, global buses, speculative later-stage directories, or external brokers. [Source: Project Context; shared code standards]

### Previous story and git intelligence

- Story 1.2 is `done`, with no unresolved application/API review findings. Preserve its fixes: heading focus after New Game, stable save Retry during pending/failure/success, observable retry tests, secret-canary exclusion, and Chromium plus WebKit install. Its browser suite recorded 22 passes and 6 desktop-only skips on Mobile Safari; that is historical evidence, not a pass for this implementation. [Source: `_bmad-output/implementation-artifacts/1-2-open-the-title-and-start-a-new-game.md#Review Findings`]
- The whole-branch follow-up records Kyle's correction: the old theme is deprecated; `docs/components/bundle.js` and preview composer handlers are unused reference artifacts. Use active frontend components/theme as runtime evidence. Normal mobile layout must be decent; extreme mobile zoom breakage is not a review blocker under that recorded user clarification. Keep applicable desktop enlargement/reflow, keyboard, visible-focus, status, reduced-motion and target-size behavior without importing obsolete docs components. [Source: previous story, Review Findings — Whole Branch Follow-up]
- Recent commits: `d6acddb` marks 1.2 done; `860c1ce` fixes its review findings; `df6912a` records implementation/review; `96c6913` adds the campaign-book Title UI; `7e7e78b` adds read-only save discovery. Reuse their generated API patterns and focus-preserving recovery. No existing operation/draft/database subsystem was found. [Source: repository git history and source inspection, 2026-09-28]

### Library/framework requirements and current technical research

- Keep installed exact pins and lockfiles: Python 3.14.7, FastAPI 0.141.1, Pydantic 2.13.5/Settings 2.15.0, React 19.2.8, TanStack Query 5.102.8, Zod 4.5.4, `@hey-api/openapi-ts` 0.99.0, TypeScript 6.0.3, Vite 8.2.2, Playwright 1.63.0 and pytest 9.1.1. TypeScript 6.0.3 is the reviewed compatibility choice; do not revert to architecture's historical 7.0.2 recommendation. Preserve the generator's patched `js-yaml` override. No dependency upgrade is required for this story. [Source: `frontend/package.json`, `backend/pyproject.toml`, lockfiles, README]
- Official docs checked 2026-09-28: SQLite supports `STRICT` from 3.37.0; its allowed types require JSON/timestamps to use appropriate native storage types. Validate structured JSON separately. Transactions serialize writes; plan explicitly for contention, and use short transactions for commit/revision checks. [SQLite STRICT tables](https://www.sqlite.org/stricttables.html), [SQLite transactions](https://www.sqlite.org/lang_transaction.html).
- FastAPI's built-in `fastapi.sse.EventSourceResponse` and `ServerSentEvent` were added in 0.135.0, below the installed pin. Use that capability after checking its installed API rather than adding a separate SSE package. The documented event ID and `Last-Event-ID` support transport replay; durable event retention/recovery remains application responsibility. [FastAPI SSE guide](https://fastapi.tiangolo.com/tutorial/server-sent-events/).
- TanStack Query polling uses `refetchInterval`; v5 passes the query object to its interval callback. Use terminal-aware polling and explicit idempotent mutation recovery rather than uncontrolled mutation retries. Verify against the installed generated Query options. [TanStack v5 migration guide](https://github.com/TanStack/query/blob/main/docs/framework/react/guides/migrating-to-v5.md), [QueryClient documentation](https://github.com/TanStack/query/blob/main/docs/reference/QueryClient.md).
- This research confirms applicable APIs, not permission to float pins or claim a fresh dependency/security audit. Provider choice, cost tuning, and later narration are deferred.

### Testing requirements and completion evidence

| AC / inherited behavior | Required observable evidence |
| --- | --- |
| 1: initialization | Fresh real DB has only scoped `STRICT` records; rerun preserves state; failed migration rolls back; unsupported SQLite creates no application data; contract export opens no DB |
| 2: identity/creation | Concurrent identical requests return one operation/draft and one result/audit commit; changed payload conflicts; initial revision is authoritative; three save slots stay unchanged |
| 3: truthful status | Tests observe accepted/running/complete/failed/interrupted with matching subject, last event and commit boundary; malformed success/problem/event data cannot become committed UI |
| 4: reconnect/refresh | Event replay returns strictly newer ordered IDs; repeated delivery is ignored; polling recovers same subject with SSE unavailable; refresh/lost 202 retains the original request identity |
| 5: restart | New app over same DB reconciles precommit operation to interrupted; postcommit/pre-complete crash returns original result without a second draft/revision/audit; no campaign or fictional clock is created |
| 6: explicit recovery | Failed/interrupted supported work retries under original subject/request/operation; repeat retry has one worker outcome; a committed replay never creates another draft |
| Cancellation/atomicity | Cancellation wins before commit with no mutation, or loses to commit with the original result intact; injected write failure leaves no partial commit evidence; read queries still work |
| Accessible UI/regressions | Immediate acknowledgement, keyboard recovery controls, stable retry/heading focus, deduplicated status, reduced motion, applicable narrow desktop/enlargement and normal mobile flow; save checks and canary remain sound |

Use real FastAPI/SQLite and observable responses/persisted state, not mocks of first-party persistence or route call counts. Lifecycle tests may pause execution at injected scheduling barriers and inject a concrete I/O failure at the infrastructure seam; these must exercise the real transaction/worker and be recorded as controlled fault injection. Browser transport tests may delay/drop an actual API response or sever streaming, but must not fabricate first-party responses. Test-only pause/fault controls belong in test composition, never release routes. No paid/non-deterministic external provider is needed for draft creation. [Source: Project Context, Testing Rules; previous story review]

Use AAA, one behavior per test, accessible role/label queries, and `userEvent` for normal component interactions. Required commands run independently from the appropriate directories:

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

Follow `_bmad-output/project-context.md` and `/Users/kyle/.codex/standards/code-architecture.md`. Strict TypeScript and Pyright/Pydantic boundaries; inward dependencies; separate command/query files; domain logic is pure and cannot import FastAPI/SQLite/environment/provider adapters. Construct dependencies at roots and inject them explicitly. Each application source file owns one named function/component, with purpose/rationale/example block documentation; precise types and no casts concealing boundary mismatches. React uses named props, destructuring in the body, and default export at the bottom. Use Python snake_case, component PascalCase, TypeScript camelCase, JSON camelCase, and snake_case wire enums. Server state belongs to TanStack Query; browser storage contains no authoritative data. No MCP integration is required. The actual `frontend/e2e/` path and current runtime theme override stale illustrative paths. [Source: Project Context; shared standards; Story 1.2]

### References

- `_bmad-output/planning-artifacts/epics.md` — Story 1.3; all Epic 1 handoffs; FR2–FR3, FR31–FR33; NFR2/NFR4/NFR6/NFR12–NFR13/NFR15–NFR16/NFR19; Shared Delivery Definition of Done.
- `_bmad-output/game-architecture.md` — Data Persistence; Wire Format; Request Lifecycle and Transport; Restart Recovery; Error Handling; System Location Mapping; Causal Action Transaction; ADR-006; Transport and Query-State Contracts.
- `_bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/gdd.md` — P0 Entry and Session 0; Platform and Performance Requirements; P0 Scope.
- `_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md` and `DESIGN.md` — pending/failure/recovery truth, status/focus/accessibility; applied subject to the later user clarifications in Story 1.2.
- `_bmad-output/implementation-artifacts/1-2-open-the-title-and-start-a-new-game.md` — implementation, review patches, whole-branch user clarifications, current UI/test paths.
- `_bmad-output/project-context.md`; `/Users/kyle/.codex/standards/code-architecture.md` — project and personal implementation/testing rules.
- `_bmad-output/planning-artifacts/p0-verification-and-exit-plan.md` — later stage-wide evidence; not a Story 1.3 completion claim.
- Repository source and recent commits inspected 2026-09-28; official external documentation linked above.

## Dev Agent Record

### Agent Model Used

GPT-6 Codex (story context creation).

### Debug Log References

- Workflow customization resolved: no prepend/append steps, persistent facts, or terminal completion instruction.
- Research covered governing Story 1.3 and Epic 1 handoffs, canonical architecture, GDD/UX context, project rules, Story 1.2 reviews, actual source, recent commits, and official SQLite/FastAPI/Query documentation.

### Completion Notes List

- Ultimate context engine analysis completed - comprehensive developer guide created.
- Story preparation only; implementation tasks are unchecked and no application-test execution is claimed.

### File List

- `_bmad-output/implementation-artifacts/1-3-track-a-recoverable-session-0-operation.md`
- `_bmad-output/implementation-artifacts/sprint-status.yaml`

### Change Log

- 2026-09-28: Created the ready-for-dev Story 1.3 context and scoped the durable Session 0 foundation with recovery, atomicity, current-source guardrails, and test evidence requirements.
