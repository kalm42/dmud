---
project_name: 'dmud'
user_name: 'Kyle'
date: '2026-09-08'
sections_completed: ['technology_stack', 'engine_rules', 'performance_rules', 'organization_rules', 'testing_rules', 'platform_rules', 'anti_patterns']
existing_patterns_found: 7
status: 'complete'
rule_count: 134
optimized_for_llm: true
---

# Project Context for AI Agents

_This file contains critical rules and patterns that AI agents must follow when implementing game code in this project. Focus on unobvious details that agents might otherwise miss._

---

## Technology Stack & Versions

- Custom text-game stack; do not introduce Unity, Unreal, Godot, or graphics-engine abstractions.
- Node.js 24.20.0 LTS with npm.
- React 19.2.8 and React DOM 19.2.8.
- TypeScript 6.0.3 in strict mode (the version pinned by the frontend lockfile).
- Vite 8.2.2 with `@vitejs/plugin-react` 6.1.1.
- Tailwind CSS 4.3.3 with `@tailwindcss/vite` 4.3.3 for frontend utility styles; `class-variance-authority` 0.7.1 for typed UI variants and `prettier-plugin-tailwindcss` 0.8.1 for class ordering.
- Python 3.14.7 managed with uv 0.12.0.
- FastAPI 0.141.1 with Pydantic 2.13.5 and Pydantic Settings 2.15.0.
- SQLite 3.37.0 or newer; reject older runtimes at startup.
- PyYAML 6.0.3 for authored content, always followed by strict Pydantic validation.
- OpenAPI 3.1.0 is the transport-contract source of truth.
- Generate the frontend client with `@hey-api/openapi-ts` 0.99.0.
- Validate frontend boundaries with Zod 4.5.4.
- Manage server-derived frontend state with TanStack Query 5.102.8.
- Test with Vitest 5.0.0, Playwright 1.63.0, and pytest 9.1.1.
- Enforce quality with ESLint 10.9.1, Pyright strict 1.1.411, and Ruff 0.16.6.
- Lockfiles define exact resolved versions; agents must not replace pinned versions with floating `latest` dependencies.

## Critical Implementation Rules

### Engine-Specific Rules

- The FastAPI backend is authoritative for mechanics, world state, time, randomness, persistence, NPC decisions, and LLM orchestration; React only submits commands and renders server-provided state.
- Treat player text as intent, never as an authoritative state change.
- Every consequential action follows `propose → validate → resolve → commit → narrate`.
- LLM output must pass a versioned, strict Pydantic contract before application code inspects it; the LLM may propose or narrate but never commit mutations.
- Narration receives committed facts only. Narration failure must not roll back or alter committed mechanics.
- Each logical mutation uses `requestId` and `expectedWorldRevision`; retries recover the original operation or result and never repeat mechanics.
- Commit world state, action record, request result, and committed operation status in one SQLite transaction.
- Keep historical facts, observations, communicated claims, and NPC beliefs as distinct provenance-linked types; a belief never rewrites truth.
- Advance game time only through committed action phases. Browser activity, menus, LLM latency, and application downtime consume no game time.
- Order scheduled events by `(due_game_time, priority, insertion_sequence)` and persist the clock, queue, insertion counter, and processing evidence.
- Long actions stop at the actual time of an event requiring player attention; only completed phases apply their completion effects.
- Domain functions return typed changes and events as data; they do not publish through global mutable buses or perform external side effects.
- Use explicit finite-state transitions for operations and NPC plans; do not model lifecycle with combinations of booleans.
- Routine NPC behavior is deterministic. Use the LLM only for consequential interpretation or replanning, then validate proposals against actual knowledge, resources, obligations, relationships, and time.

### Performance Rules

- This text-first game has no defined FPS, frame-budget, resolution, or object-pooling requirement; do not introduce graphics-engine optimization patterns without evidence.
- Acknowledge submitted input visibly within 100 ms.
- Keep local menu interactions under 200 ms.
- Complete save/load operations within 2 seconds.
- Target completion of 95% of LLM-mediated actions within 10 seconds.
- Preserve a recoverable operation state when work reaches 30 seconds; never leave the UI in an ambiguous pending state.
- Validate performance against a 60-minute, 100-action session with four NPCs.
- Bound scheduled-event processing per action and detect recursive or same-time event loops.
- Do not run continuously active NPC agents; execute routine schedules deterministically and invoke LLM-assisted replanning selectively.
- Preload and validate the complete P0 authored-content set into one immutable registry; do not hot-reload production content during an active session.
- TanStack Query may cache browser reads, but authoritative mutations must invalidate or replace affected views.
- Do not add backend caches beyond the immutable content registry in P0 without measured need and an invalidation design.
- Measure action latency, model calls, tokens, session cost, rejected proposals, duplicate attempts, contradiction repairs, and memory growth across sessions.
- Keep operational diagnostics bounded and redacted; never log complete saves, secrets, hidden objectives, or unrestricted provider payloads.

### Code Organization Rules

- Use one monorepo with `frontend/` (including `frontend/tests/e2e/`), `backend/`, `content/`, and `contracts/`.
- Organize the frontend by player-facing feature under `frontend/src/features/`; organize the backend by game-system slice under `backend/src/dmud/`.
- Keep reusable, presentation-only UI primitives in `frontend/src/components/ui/`; define their Tailwind variants with CVA.
- Keep code that changes together in the same vertical slice. Avoid generic `services`, `managers`, `helpers`, or catch-all repositories.
- Dependencies point inward: domain code must not import FastAPI, SQLite, provider SDKs, environment access, or frontend code.
- Keep HTTP handlers thin; they validate transport data and invoke application commands or queries.
- Separate command/write paths from query/read paths. Multi-slice writes go through the action commit coordinator and one transaction.
- Restrict `platform/` to concrete technical capabilities such as SQLite connections, configuration, clocks, randomness, and logging.
- Add shared primitives to `foundation/` only after multiple slices require the same stable concept.
- Construct dependencies at composition roots and inject them explicitly; prohibit global service registries, mutable singletons, and feature-owned containers.
- Use the generated API client across the browser boundary. Commit generated output, but never manually edit `contracts/openapi.json` or `frontend/src/api/generated/`.
- Store authored definitions as versioned YAML with stable IDs. Runtime-generated content belongs in persisted state and must never rewrite authored files.
- Do not create conditional P1/P2 feature directories or abstractions before their scope gates pass.
- Each application source file defines one named function or React component. Move every additional named helper, formatter, factory, handler, or component into its own coherently named file.
- Functions must have one concern and be pure by default. Domain calculations, validation, transitions, and projections must be pure.
- Never nest ternary expressions; use explicit branches for multi-state decisions.
- Functions at explicit I/O boundaries may be effectful, but each must coordinate only one boundary concern and delegate calculations to pure functions.
- Refactor a function when it develops multiple responsibilities, substantial branching or nesting, mixed read/write behavior, multiple unrelated effects, or tests that require complex setup or excessive mocking.
- Colocate only types and constants exclusively owned by the file’s single function; move reusable or independently meaningful definitions into their own modules.
- Inline callbacks required by language or framework APIs do not count as additional application functions when they contain no reusable domain behavior.
- Test files may contain multiple test cases, while each test still verifies one observable behavior.
- Generated files, declarative configuration, and SQL migrations are exempt from the one-function rule.
- Name each application source file after its function or component, following the project’s language-specific naming conventions.
- Document exported and non-trivial functions with purpose, rationale, and an example call.
- React components use named props types, destructure props inside the function body, remain pure where practical, and export default at the bottom.
- Python modules use `snake_case.py`; Python tests use `test_<behavior>.py`.
- React components use `PascalCase.tsx`; hooks use `useCamelCase.ts`; other TypeScript modules use `camelCase.ts`.
- TypeScript tests use `<subject>.test.ts` or `<subject>.test.tsx`; feature directories and YAML files use `kebab-case`.
- Use `snake_case` internally in Python and YAML, `camelCase` in JSON and TypeScript, and lowercase `snake_case` for wire enum values.
- Use stable namespaced content IDs, past-tense `PascalCase` domain events, descriptive `PascalCase` scheduled events, and dotted-lowercase telemetry names.

### Testing Rules

- Write tests in Arrange → Act → Assert form, with one observable behavior per test.
- Name the top-level `describe` after the exported component or function under test. Use nested `describe` blocks for state or setup context, not acceptance-criterion or ticket labels.
- Make each test title a precise failure message; do not join multiple behaviors with “and.”
- Map every acceptance criterion to at least one test, using roughly 70% coverage as a sanity check rather than an exhaustive target.
- Prefer integration tests over unit tests whenever the real local boundary is available.
- Exercise backend behavior through the real FastAPI ASGI application and isolated real SQLite databases.
- Exercise browser journeys with Playwright against the real SPA and API.
- Do not mock first-party routes, rules, persistence, or browser behavior.
- Mock only unavailable, paid, or non-deterministic external providers. Each mock requires a one-line justification in the test report.
- Replace the external LLM provider with deterministic contract fixtures, but still test the complete proposal, validation, resolution, commit, and narration-adapter flow.
- Test behavior through API responses, persisted state, rendered UI, and other caller-visible outcomes—not private methods, internal call order, or mock invocation counts.
- Use Testing Library queries in accessibility order: role, label, placeholder, text, display value, alt text, title, then test ID only as a last resort.
- Use `userEvent` for normal interactions; reserve `fireEvent` for low-level events that `userEvent` cannot express.
- Give save/load, migrations, branch divergence, idempotent retries, stale revisions, crash recovery, narration failure, and scheduler ordering real integration coverage.
- Verify fact, observation, claim, and belief separation with causal scenario fixtures, including the presence and absence of required encounters.
- Test deterministic time with seeded randomness, persisted event queues, interruption boundaries, completed-phase effects, and event-budget exhaustion.
- Keep production content separate from controlled test starting states and test-only seed or cheat infrastructure.
- Run formatting, linting, static typing, contract drift, unit/integration tests, and browser tests as separate failing quality gates.
- Do not treat Vite transpilation as TypeScript type-checking; run `tsc --noEmit`.
- Keep Pyright strict across Python application code and require complete type annotations.

### Platform & Build Rules

- Target a locally run desktop browser; P0 and P1 are single-player only.
- During development, run Vite and FastAPI separately and proxy `/api` through Vite.
- For packaged builds, FastAPI serves the compiled SPA and API from one loopback-only origin.
- Do not add remote hosting, authentication, cloud saves, TLS termination, or multiplayer synchronization without a separate approved threat model and architecture decision.
- Keep LLM credentials and all secrets backend-only. Load them through validated environment or OS-backed configuration.
- Never place secrets in frontend environment values, browser storage, saves, authored content, generated clients, or normal logs.
- Apply conservative request-size limits and security headers even for loopback-only builds.
- Store SQLite databases, saves, logs, provider responses, build output, and test artifacts outside source control.
- Browser storage may persist validated presentation preferences only; it must never contain authoritative game state.
- Use native DOM and React input handling. Enter submits; Shift+Enter inserts a line.
- Keep every control keyboard reachable, identify speakers without relying on color, and preserve the user's browser text-size and zoom choices without an in-game text-size control.
- Do not add suggested actions, recommended dialogue, action chips, or other strategy-steering controls.
- Show explicit pending, resolved, rejected, failed, and interrupted request states.
- Use typed, versioned SSE for operation progress and polling for recovery; reconnect with monotonically increasing event IDs and `Last-Event-ID`.
- Generate the frontend client, types, Zod schemas, and TanStack Query bindings from FastAPI OpenAPI.
- Commit both lockfiles and generated contracts. CI must regenerate contracts and fail on drift.
- Build and verify formatting, linting, strict typing, tests, and contract drift as independent quality gates.
- Reject unsupported SQLite versions and invalid required configuration before opening application data.
- Bind development diagnostics only when the backend is loopback-bound and `DMUD_DEVTOOLS=true`; expose capabilities explicitly rather than inferring them from frontend build mode.

### Critical Don't-Miss Rules

- Never let the frontend, narration layer, SSE handlers, diagnostics, or LLM provider mutate authoritative game state.
- Never treat fluent model output as valid merely because it parses; validate its contract and independently verify feasibility, costs, duration, stakes, and consequences.
- Never narrate an uncommitted success. Narration consumes committed facts and may be retried without rerunning mechanics.
- Never execute a logical request twice. Recover by `requestId`, recheck `expectedWorldRevision` inside the write transaction, and record random inputs once.
- Never automatically resume provider or mechanical work after restart without first checking the atomic authoritative request result.
- Cancellation may prevent pre-commit work; after commit it may stop only narration or presentation delivery.
- Never apply partial completion effects for an interrupted phase. Commit elapsed time and completed phases only.
- Never manufacture an event to satisfy “wait until X.” The event must exist and remain feasible in the persisted scheduler.
- Never propagate knowledge without a recorded observation or participant encounter. NPC belief changes require provenance and cannot rewrite historical facts.
- Never allow NPC plans to exceed their knowledge, resources, obligations, relationships, location, or available time.
- Never mix expected gameplay outcomes with unexpected failures: return typed results for rejection, clarification, or conflict; catch unexpected exceptions only at application boundaries.
- Never catch broad exceptions in domain code and continue with potentially inconsistent state.
- Never perform external side effects before the authoritative transaction commits.
- Never store an incomplete save. Preserve the clock, event queue, ownership, inventory, relationships, commitments, beliefs, plans, progression, operation evidence, schema version, world revision, and state hash.
- Never silently change the meaning of a saved content ID or generated definition; use explicit content or state migrations.
- Never manually edit generated API artifacts or handwrite competing frontend transport types.
- Never trust external or persisted data without strict runtime validation. Reject unknown fields unless extensibility is explicitly documented.
- Never read process environment variables inside feature or domain modules; inject validated configuration from composition roots.
- Never log secrets, unrestricted provider payloads, hidden objectives, complete save state, stack traces, SQL, or credentials to player-facing output.
- Never introduce global mutable buses, service locators, active-record domain models, generic data managers, or continuously running autonomous NPC agents.
- Never add Redis, Celery, WebSockets, external brokers, speculative caches, routing, multiplayer abstractions, or conditional P1/P2 systems before approved requirements justify them.
- Never add per-action undo or carry rewards between save branches.
- Never create locations procedurally; Brackenford geography is authored content.

---

## Usage Guidelines

**For AI Agents:**

- Read this file before implementing any game code.
- Follow every rule exactly as documented; when uncertain, prefer the more restrictive interpretation.
- Update this file when an approved implementation establishes a new unobvious pattern.

**For Humans:**

- Keep this file lean and focused on agent implementation needs.
- Update it when the technology stack or architectural decisions change.
- Review it quarterly and remove rules that are outdated or have become obvious from enforced tooling.

Last Updated: 2026-09-08
