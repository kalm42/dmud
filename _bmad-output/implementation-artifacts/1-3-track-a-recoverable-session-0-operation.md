---
baseline_commit: fab1c2ab8e8136a05d06fdeec987ff900b9f99c2
---

# Story 1.3: Track a Recoverable Session 0 Operation

Status: done

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

- [x] Initialize durable application data safely (AC: 1, 5)
  - [x] Extend backend-only validated settings with an explicit application-data directory and inject the resolved configuration from `create_app`. Keep SQLite version validation ahead of directory creation and database access.
  - [x] Add an ordered, transactional first SQL migration and typed SQLite adapters for draft state, operations, ordered operation events, request results, minimal immutable draft-commit evidence, and migration bookkeeping. Do not create campaign, branch, save, world, NPC, or future-stage tables.
  - [x] Initialize/migrate/reconcile during FastAPI lifespan; shut down the supervised worker and close resources safely. Importing the app or exporting OpenAPI must not open a database, run migrations, or start work.
  - [x] Give integration tests and Playwright explicit isolated temporary data directories; update lifecycle-aware tests to enter `TestClient` as a context manager. Document the data directory and restart behavior in README.
- [x] Define and persist the shared operation contract (AC: 2, 3, 5, 6)
  - [x] Implement a versioned minimal `SessionZeroDraft`, `CreateSessionZeroDraft`, and `GetSessionZeroDraft` in `session_zero/`, with stable ID, draft revision, collecting lifecycle, schema version, and active-operation reference. Establish empty draft material without fabricated answers, attributes, reflection, or content compatibility evidence.
  - [x] Add strict Pydantic request/resource/result/event/problem models with camelCase wire fields, typed subject identity, commit boundary, committed revision, last event ID, and explicit safe recovery capability. Creation has no expected prior draft revision; commands against an existing draft require `expectedDraftRevision`.
  - [x] Add pure legal lifecycle transitions plus separate read/write persistence paths in `operations/`. Enforce a unique logical request identity, canonical payload digest, and a single executing mutation for a draft subject. Duplicate acceptance must be resolved transactionally, including simultaneous requests.
  - [x] Persist acceptance before exposing its ID; supervise a real in-process draft-create command. Commit the draft, its revision, immutable audit evidence, request result, and committed operation/event together. Complete delivery afterward without a second draft mutation.
  - [x] Implement startup reconciliation against request results before any resumption; uncommitted nonterminal work becomes interrupted and committed work exposes the original result. Retry must check that same result again inside its transaction.
- [x] Expose strict creation, status, streaming, and recovery boundaries (AC: 2–6)
  - [x] Register `POST /api/session-zero-drafts`, `GET /api/session-zero-drafts/{draftId}`, `GET /api/operations/{operationId}`, `GET /api/operations/{operationId}/events`, and `POST /api/operations/{operationId}/cancel` through thin handlers.
  - [x] Implement `POST /api/operations/{operationId}/retry` without changing the original operation/request/subject identity. Cancel/retry envelopes carry a separate recovery-command `requestId` and `expectedLastEventId`; persist their idempotent outcome so repeats cannot launch concurrent attempts. This retry route is a selected story extension, not a previously specified architecture endpoint.
  - [x] Return `202 Accepted` with operation/status/events references after durable acceptance. Identical original submissions retrieve existing status/result; changed payloads return a typed conflict. Use RFC 9457 problems for conflicts, invalid input, unknown IDs, and unavailable/corrupt reads.
  - [x] Persist typed versioned SSE events with monotonic IDs, replay strictly after `Last-Event-ID`, and provide polling independently of streaming. Validate cursor input and document recovery for invalid/out-of-range cursors; never invent missing history or rerun work to rebuild it.
  - [x] Implement cooperative cancellation before commit. If commit wins the race, return the authoritative committed result and stop only delivery work. A disconnected browser or SSE consumer must not cancel the operation.
  - [x] Export OpenAPI and regenerate the committed client, types, Zod schemas, and Query bindings using the existing scripts. Document event payload schemas in OpenAPI so event parsing uses generated schemas too.
- [x] Connect New Game to truthful operation recovery (AC: 2–6)
  - [x] Replace the local placeholder-only handoff with one user-triggered creation request. Acknowledge immediately, retain its request ID before sending, and prevent repeat activation while its outcome is unknown. Avoid mutation-on-mount, including React StrictMode duplicate effects.
  - [x] Preserve a validated non-authoritative refresh locator using the smallest existing-app-compatible mechanism, such as URL state. It may identify the request/operation/draft and event cursor, but may contain no authoritative draft content. Before the operation ID is received, preserve enough request identity to recover a lost acceptance response safely.
  - [x] Use generated SDK adapters, strict runtime validation, identity-scoped Query keys, and polling fallback. Recover the original operation on refresh; stale events or query responses for a different subject cannot replace the active view. Never let a failed read look like a failed authoritative mutation or known-empty draft.
  - [x] Show accepted/running, complete, failed, interrupted, and unknown/unavailable status in text with the commit boundary and supported recovery controls. Keep status and controls keyboard accessible, preserve focus through retry, and announce changes politely without repeated announcements on every poll.
  - [x] Preserve Title New Game independence from save discovery, empty Continue semantics, and Session 0 heading focus. Use current runtime UI primitives/theme; no composer, Rowan question, answer editing, review, or campaign entry in this story.
- [x] Verify real persistence and recovery behavior (AC: 1–6)
  - [x] Add real FastAPI/isolated SQLite integration tests for migration, acceptance/idempotency, typed reads, SSE replay, cancellation/retry, rollback, concurrent requests, and restart before/after commit.
  - [x] Extend Playwright against real Vite/FastAPI for New Game, response-loss/refresh recovery, SSE loss with polling, and accessible failure/retry. Use deterministic scheduling barriers, not sleeps, to observe intermediate states of the fast local operation.
  - [x] Preserve Title save retry/focus, secret-canary, Chromium/Mobile Safari, and existing parser coverage. Map each AC to observable tests and record commands/results without claiming future Session 0 or P0 completion.
  - [x] Run the independent existing format, lint, strict typing, backend/frontend tests, build, browser, and contract drift gates listed below.

### Review Findings

Reviewed 2026-09-29: `feat/story-1-3` at `8575b79` against `main` at `3c1d121`, using `main...HEAD`. Full scope: 79 files, 4,880 insertions and 48 deletions. Blind Hunter, Edge Case Hunter, and Acceptance Auditor completed independently; the installed adversarial and edge-case review lenses supplied the legacy named reviewers' instructions. Triage: **0 decision needed, 9 patch, 0 defer, 3 dismissed**. Kyle authorized Apply every patch; all nine findings were resolved on 2026-09-29. The original finding descriptions below refer to the reviewed baseline.

- [x] [Review][Patch] **R1 — P1: Keep the worker alive when scanning or failure persistence fails** [`backend/src/dmud/operations/run_worker.py:16`]. `list_nonterminal()` runs outside the exception boundary, and the exception handler's `transition_operation(..., "failed")` can itself raise. Either path terminates the sole task while HTTP handlers continue returning durable acceptance and signaling an abandoned wake event. A real temporary SQLite probe confirmed that an invalid nonterminal record kills the worker and leaves a subsequently accepted unrelated operation unprocessed. Protect enumeration and failure recording, isolate damaged records, and supervise/reschedule transient failures without requiring restart. Covers AC3/AC6 and the supervised-worker requirement.

- [x] [Review][Patch] **R2 — P1: Bound stalled mutation transport and unlock same-request recovery by 30 seconds** [`frontend/src/features/operation-progress/useDraftOperation.ts:20`]. Neither creation nor recovery submission supplies a transport deadline. If an accepted response stalls instead of rejecting, `mutation.isPending` and `busy.current` remain true indefinitely, disabling Recover request while no operation ID is known. A browser probe withheld the real accepted response and advanced the clock 31 seconds; the surface still said Awaiting durable acceptance with recovery disabled. Add a bounded deadline, preserve the original locator, and transition to an explicit unknown/recoverable outcome without claiming server cancellation or generating another request ID. Covers AC3/AC4 and the specified 30-second recovery threshold.

- [x] [Review][Patch] **R3 — P2: Reschedule delivery after a postcommit exception** [`backend/src/dmud/operations/run_worker.py:31`]. A delivery-stage exception falls through to a `failed` transition even when the draft result already committed. `committed → failed` is illegal, so a successful failure-handler call leaves the record at `committed`; the wake was cleared and the worker waits indefinitely rather than finishing delivery. A real SQLite probe with a controlled postcommit I/O failure confirmed this state with a live, sleeping worker. Recheck authoritative result evidence and schedule completion only, preserving the original draft/result and avoiding any repeated mutation. Covers AC3/AC5 and independent postcommit delivery recovery.

- [x] [Review][Patch] **R4 — P2: Move synchronous database adapters off the asynchronous event loop** [`backend/src/dmud/operations/post_draft.py:13`]. Async creation/recovery/status handlers, the SSE generator, and the worker call blocking SQLite adapters directly. Under contention from another connection, `connect_database()` permits a five-second lock wait on the same event loop that serves status, cancellation, and streams. Dispatch each complete adapter call through a thread boundary, keeping connection ownership and each transaction within that call. Verify contention with a real second SQLite connection and an independent responsiveness check. Covers the requirement that reads remain available during work and bounded local operation responsiveness.

- [x] [Review][Patch] **R5 — P2: Read operation evidence and history within one SQLite snapshot** [`backend/src/dmud/operations/get_operation.py:11`]. SELECT-only `with db:` blocks do not begin a transaction; resource, result, audit, and event queries can observe different commits when another connection writes concurrently. Deterministic interleaving of a real second-connection draft commit caused `get_operation()` to report `operation_unavailable`, and `get_events()` to report `event_history_unavailable`, although subsequent reads were valid. Establish explicit short read transactions around complete reads in `get_operation`, `get_events`, `get_request_operation`, `list_nonterminal`, and `get_session_zero_draft`; write paths already begin transactions. Covers AC3/AC4 and authoritative, concurrency-safe reads.

- [x] [Review][Patch] **R6 — P2: Resolve a lost recovery-response error when fresh authoritative evidence arrives** [`frontend/src/features/operation-progress/useDraftOperation.ts:83`]. `unavailable` remains true for the lifetime of `mutation.isError`, even after successful polling or SSE resolves the operation's current outcome. A browser probe dropped the real cancellation response; polling obtained `interrupted`, but the status still said unavailable and Retry draft remained disabled until manual error reset/replay. Track unresolved recovery transport separately and clear its availability error when validated matching evidence establishes the outcome; genuine failed reads must still remain unknown. Covers AC3/AC4/AC6 and truthful accessible recovery.

- [x] [Review][Patch] **R7 — P2: Retire definitively rejected recovery commands instead of persisting a stale replay** [`frontend/src/api/recoverOperation.ts:21`]. A real `409 stale_event` can occur if the worker advances between the displayed cursor and cancel submission. The adapter discards the typed problem's current operation, and the hook leaves the rejected command's original `expectedLastEventId` in the URL. Recover request repeats that rejected cursor, including after refresh; Check status resets the mutation error but does not remove the stale recovery command. Preserve typed problem context, validate its identity before updating the cache, and remove a definitively rejected recovery locator so eligible controls use current evidence. Keep unknown transport failures replayable under their original recovery-command identity. Covers AC4/AC6 and the strict recovery/problem contract.

- [x] [Review][Patch] **R8 — P2: Validate semantic event evidence and envelope cursors on backend reads** [`backend/src/dmud/operations/get_events.py:24`]. Historical replay validates fields but omits original `requestId` and lifecycle/result/commit-boundary consistency; latest-event validation in `read_operation.py:52` compares only the nested operation and ignores the envelope `eventId`. A real SQLite probe changed historical event 1 to another valid request ID and `complete` with boundary `none`; replay still returned it. Validate historical operation semantics and identity, each envelope cursor against its row/nested snapshot, and the latest envelope against `lastEventId`, returning typed unavailable problems for contradictory persisted evidence. Frontend rejection is useful but does not satisfy the authoritative backend contract. Covers AC3/AC4 and strict success/event validation.

- [x] [Review][Patch] **R9 — P2: Reject a recovery locator without its operation and draft identity** [`frontend/src/features/operation-progress/locatorSchema.ts:20`]. The locator refinement allows both subject IDs to be absent even when `recovery` is present. A browser probe loaded this URL: it passed validation and hid Title, but every Recover request failed with No recovery identity and no creation path was available. Require operation/draft identity whenever recovery coordinates exist and discard invalid external locators at ingress. Covers AC4 and validated, non-authoritative refresh recovery.

**Review-time verification (before fixes):** Existing backend tests: 35 passed. Existing frontend tests: 16 passed. Existing browser suite: 40 passed, 6 existing skips across Chromium and Mobile Safari. Frontend/backend formatting, lint, strict typing, frontend build, API contract drift, and `git diff --check` passed independently. Three temporary Chromium probes against real Vite/FastAPI reproduced R2, R6, and R9; these probes asserted the current defects, not repaired behavior. Real temporary SQLite probes established R1, R3, R5, and R8; R4 and R7 follow directly from the blocking call and error/locator paths. Controlled scheduling and fault injection did not fabricate first-party responses. Temporary probes live outside the repository; no regression tests or application patches were added. An initial retry-response-loss probe did not observe automatic polling because its prior terminal state stopped polling; the final R6 probe used cancellation response loss while polling was active.

**Dismissed:** Requiring UUIDv7 syntax at every recovery pointer adds little beyond unknown-ID handling and does not establish a separate behavior defect; simultaneous application startup on one data directory is outside the current single-process scope; stale-attempt failure after cancellation/retry requires the current test-only awaited hook and has no corresponding production await in this story. These were not promoted into future-scope implementation work.

#### Patch Resolution and Validation

- R1/R3: Separated claimed attempt execution from supervision and failure settlement. Corrupt records are isolated; storage scan and failure-recording failures remain supervised and retryable. Committed delivery is completed from the original result, and a failed older attempt cannot change a newer retry.
- R4/R5: Offloaded complete database adapters at HTTP, streaming, worker, and lifespan boundaries. Repeated cancellation drains the adapter before propagating, and creation/retry always notify the worker after draining. Explicit read transactions preserve one evidence/history snapshot. These introduced asynchronous boundaries made attempt fencing necessary, so the initially dismissed stale-attempt scenario now has a supported guard and real regression coverage.
- R2/R6/R7/R9: Creation and recovery transport have a 30-second deadline. Validated current evidence resolves lost recovery responses; typed definitive conflicts retire stale commands. Unknown delivery retains its recovery-command identity across refresh and status checks, and both controls and the hook prevent replacing it with another command. Locators without required operation/draft coordinates are rejected at ingress.
- R8: Shared pure snapshot validation checks lifecycle, recovery capabilities, subject/result, commit boundary, revision, and URLs. Replay validates request identity, row/envelope cursors, immutable committed results, lifecycle ordering, and the transition from the resume cursor; only newer events are returned.
- Final independent gates passed: backend `uv run pytest` (**51 passed**), Ruff format/check, Pyright strict (**0 errors**); frontend `npm test` (**18 passed**), format/check, ESLint, TypeScript, and production build; root contract regeneration/drift and `git diff --check`; Playwright (**50 passed, 6 existing skips**) across Chromium and Mobile Safari.
- New persisted regressions exercise real SQLite corruption, concurrent snapshot reads, lock contention, failure-persistence recovery, postcommit delivery recovery, attempt fencing, and real ASGI requests cancelled twice during a database lock. Five new browser journeys cover deadlines, lost cancellation delivery, stale conflict recovery, malformed locators, and unresolved recovery identity after refresh. First-party services and persistence were not mocked; connector tracing and concrete SQLite triggers provided scheduling/fault injection only.
- Follow-up frontend and backend review checks were performed independently. No schema migration, API contract change, dependency upgrade, later-story functionality, or commit was required.

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

- 2026-09-29 review fixes: recorded the original failing worker/event regression phase (6 failures, 1 pass), implemented the nine authorized patches, and added real concurrency/cancellation and browser recovery regressions. Independent follow-up reviews exposed cancellation wake/drain and unresolved-command edges, which were fixed before final validation.

- Workflow customization resolved: no prepend/append steps, persistent facts, or terminal completion instruction.
- Research covered governing Story 1.3 and Epic 1 handoffs, canonical architecture, GDD/UX context, project rules, Story 1.2 reviews, actual source, recent commits, and official SQLite/FastAPI/Query documentation.

- Implementation used GPT-6 Codex and the resolved gds-dev-story workflow; no custom activation or completion steps were present.
- Red phases observed: storage tests rejected the missing settings/lifespan seam; durable-operation tests could not import the absent operation slice; API tests received 404 for absent routes; frontend operation parser tests rejected the absent adapter. Each foundation was implemented before proceeding.
- Implementation plan: isolated lifespan migrations → shared durable acceptance/commit/reconciliation → strict HTTP/SSE/recovery routes and generated contracts → explicit New Game intent with URL locator, validated Query cache, monotonic SSE/polling → real database and browser recovery evidence.
- Controlled fault injection only: injected SQLite abort trigger verified complete transaction rollback; composition-injected asyncio barriers observed pre/postcommit states and cancellation; browser-test composition barriers and an injected infrastructure failure observed retry. Browser routes dropped actual responses or streams; no fabricated first-party responses, provider mocks, or release test routes were added.
- Final independent gates passed: frontend `npm run format:check`, `npm run lint`, `npm run typecheck`, `npm run build`, `npm test` (16 passed); backend `uv run ruff format --check src tests scripts`, `uv run ruff check src tests scripts`, `uv run pyright` (0 errors), `uv run pytest` (35 passed); root `python3 scripts/check_contract.py` (no drift), `git diff --check`; frontend `npm run test:e2e` (40 passed, 6 existing desktop-only skips across Chromium/Mobile Safari).
- Early sandbox failures accessing uv's cache were rerun with the authorized escalation. Installed pins and lockfiles remain unchanged. Existing httpx/TestClient deprecation and Pyright update notices were observed; they did not fail gates.

### Completion Notes List

- 2026-09-29: Resolved all nine code review patch findings, added the regression evidence listed under Patch Resolution and Validation, and completed the independent quality gates. Story 1.3 is done; no review action items remain.

- Implemented ordered transactional SQLite STRICT storage, short typed adapters, version guarding, lifespan initialization, supervised worker shutdown and startup reconciliation. Imports/OpenAPI export remain storage-free; test and browser data directories are isolated.
- Creation reserves one operation/request/draft subject before acknowledgement. Canonical replay and concurrent acceptance preserve identity; changed accepted payloads return typed conflicts. Initial authoritative collecting revision is 1, without answers, campaign material, or fictional time.
- Atomic draft commit includes draft state, immutable commit evidence, request result, operation boundary/revision and ordered event. Transaction rollback leaves no partial authoritative artifacts. Transactional claims and attempt event checks prevent duplicate execution or an old cancelled attempt from committing a retry.
- Added creation/draft/status/SSE/cancel/retry boundaries, strict camelCase models, RFC 9457 problems with typed classifications and safe correlation context, cursor validation/replay, cooperative precommit cancellation and same-identity idempotent recovery. Polling is independent of streaming.
- New Game now retains its original request ID before sending, acknowledges immediately, and cannot start twice while unknown. URL recovery pointers contain identifiers/cursor only. Explicit recovery handles lost acceptance/retry responses; validated identity-scoped Query state, generated SSE schemas, monotonic snapshots, polite status and focus-stable controls preserve truthful outcomes on refresh or failed reads.
- AC1 evidence: `test_application_data.py` checks unopened construction/export, only scoped STRICT tables, repeat startup, rollback and unsupported/newer schema behavior. AC2: `test_durable_operations.py` and `test_operation_routes.py` check durable acceptance, concurrency, canonical replay/conflicts and initial revision. AC3: route/recovery tests plus frontend parser tests validate authoritative boundaries, failed/interrupted/committed/complete states, strict errors and malformed data rejection. AC4: route replay and `operations.spec.ts` cover lost acceptance, refresh, SSE loss/polling and stale/duplicate snapshot rejection. AC5: real app restarts and transaction evidence preserve pre/postcommit truth. AC6: cancellation/retry integration and browser tests preserve the original subject/request/operation and prevent repeat execution.
- Existing Title/save focus, empty Continue, current theme, heading focus, keyboard accessibility, canary and browser coverage remain green. This is the durable Session 0 foundation only; later character content, campaign confirmation and the P0 promotion gate remain outside this story.
- Enhanced definition-of-done checklist passed. All tasks/subtasks are complete; story and sprint status are `review`. Suggested next step: independent `gds-code-review`.

### File List

- `backend/src/dmud/operations/execute_operation.py`
- `backend/src/dmud/operations/execution_failure.py`
- `backend/src/dmud/operations/settle_execution_failure.py`
- `backend/src/dmud/operations/validate_operation_snapshot.py`
- `backend/src/dmud/platform/sqlite/run_database.py`
- `backend/tests/integration/test_cancelled_transport.py`
- `backend/tests/integration/test_database_concurrency.py`
- `backend/tests/integration/test_event_evidence.py`
- `backend/tests/integration/test_worker_supervision.py`
- `frontend/e2e/operationRecovery.spec.ts`
- `frontend/src/api/operationDeadline.ts`
- `frontend/src/api/operationProblem.ts`
- `frontend/src/features/operation-progress/locatorSchema.test.ts`
- `frontend/src/features/operation-progress/operationLocator.ts`
- `frontend/src/features/operation-progress/recoveryOutcomeKnown.ts`
- `frontend/src/features/operation-progress/rejectedRecoveryProblem.ts`

- `.gitignore`
- `README.md`
- `_bmad-output/implementation-artifacts/1-3-track-a-recoverable-session-0-operation.md`
- `_bmad-output/implementation-artifacts/sprint-status.yaml`
- `backend/src/dmud/main.py`
- `backend/src/dmud/operations/accept_operation.py`
- `backend/src/dmud/operations/claim_operation.py`
- `backend/src/dmud/operations/commit_draft.py`
- `backend/src/dmud/operations/event_cursor.py`
- `backend/src/dmud/operations/execution_hooks.py`
- `backend/src/dmud/operations/get_events.py`
- `backend/src/dmud/operations/get_operation.py`
- `backend/src/dmud/operations/get_request_operation.py`
- `backend/src/dmud/operations/invalid_request.py`
- `backend/src/dmud/operations/legal_transition.py`
- `backend/src/dmud/operations/list_nonterminal.py`
- `backend/src/dmud/operations/models.py`
- `backend/src/dmud/operations/payload_digest.py`
- `backend/src/dmud/operations/post_cancel.py`
- `backend/src/dmud/operations/post_draft.py`
- `backend/src/dmud/operations/post_retry.py`
- `backend/src/dmud/operations/problem_response.py`
- `backend/src/dmud/operations/read_events.py`
- `backend/src/dmud/operations/read_operation.py`
- `backend/src/dmud/operations/read_status.py`
- `backend/src/dmud/operations/reconcile_operations.py`
- `backend/src/dmud/operations/recover_operation.py`
- `backend/src/dmud/operations/register_operation_routes.py`
- `backend/src/dmud/operations/render_problem.py`
- `backend/src/dmud/operations/run_worker.py`
- `backend/src/dmud/operations/stream_events.py`
- `backend/src/dmud/operations/transition_operation.py`
- `backend/src/dmud/operations/write_event.py`
- `backend/src/dmud/platform/application_lifespan.py`
- `backend/src/dmud/platform/settings.py`
- `backend/src/dmud/platform/sqlite/connect_database.py`
- `backend/src/dmud/platform/sqlite/initialize_database.py`
- `backend/src/dmud/platform/sqlite/migrations/0001_initial_schema.sql`
- `backend/src/dmud/session_zero/create_session_zero_draft.py`
- `backend/src/dmud/session_zero/get_session_zero_draft.py`
- `backend/src/dmud/session_zero/models.py`
- `backend/src/dmud/session_zero/read_draft.py`
- `backend/tests/browser_app.py`
- `backend/tests/conftest.py`
- `backend/tests/integration/test_application_data.py`
- `backend/tests/integration/test_durable_operations.py`
- `backend/tests/integration/test_operation_recovery.py`
- `backend/tests/integration/test_operation_routes.py`
- `backend/tests/integration/test_save_slots.py`
- `backend/tests/integration/test_status.py`
- `contracts/openapi.json`
- `frontend/e2e/holdDraftCommit.ts`
- `frontend/e2e/operations.spec.ts`
- `frontend/playwright.config.ts`
- `frontend/src/api/generated/@tanstack/react-query.gen.ts`
- `frontend/src/api/generated/index.ts`
- `frontend/src/api/generated/sdk.gen.ts`
- `frontend/src/api/generated/types.gen.ts`
- `frontend/src/api/generated/zod.gen.ts`
- `frontend/src/api/operationSchema.ts`
- `frontend/src/api/parseOperation.test.ts`
- `frontend/src/api/parseOperation.ts`
- `frontend/src/api/parseOperationEvent.ts`
- `frontend/src/api/parseProblem.ts`
- `frontend/src/api/readOperation.ts`
- `frontend/src/api/recoverOperation.ts`
- `frontend/src/api/submitDraft.ts`
- `frontend/src/app/App.tsx`
- `frontend/src/features/operation-progress/OperationProgress.tsx`
- `frontend/src/features/operation-progress/locatorSchema.ts`
- `frontend/src/features/operation-progress/operationKey.ts`
- `frontend/src/features/operation-progress/operationStatusText.ts`
- `frontend/src/features/operation-progress/readLocator.ts`
- `frontend/src/features/operation-progress/selectOperationSnapshot.test.ts`
- `frontend/src/features/operation-progress/selectOperationSnapshot.ts`
- `frontend/src/features/operation-progress/useDraftOperation.ts`
- `frontend/src/features/operation-progress/useOperationEvents.ts`
- `frontend/src/features/operation-progress/writeLocator.ts`
- `frontend/src/features/session-zero/SessionZero.tsx`

### Change Log

- 2026-09-29: Applied all nine authorized review fixes, verified durable recovery and cancellation/concurrency boundaries, added backend/frontend/browser regressions, and marked Story 1.3 done.

- 2026-09-28: Created the ready-for-dev Story 1.3 context and scoped the durable Session 0 foundation with recovery, atomicity, current-source guardrails, and test evidence requirements.

- 2026-09-28: Implemented and verified the durable Session 0 operation foundation, generated transport contract, accessible refresh/retry recovery and isolated persistence/restart evidence; moved Story 1.3 to review.
