---
title: 'Game Architecture'
project: 'dmud'
date: '2026-09-07'
author: 'Kyle'
version: '1.0'
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9]
status: 'complete'
engine: 'React SPA with authoritative FastAPI API'
platform: 'Local desktop browser'

# Source Documents
gdd: '/Users/kyle/Documents/Work/dmud/_bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/gdd.md'
epics: '/Users/kyle/Documents/Work/dmud/_bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/epics.md'
brief: '/Users/kyle/Documents/Work/dmud/_bmad-output/planning-artifacts/briefs/brief-dmud-2026-09-05/brief.md'
---

# Game Architecture

## Executive Summary

dmud uses a local-first React SPA and authoritative FastAPI API, with a deterministic Python domain engine owning all mechanics and persistent truth while bounded LLM integrations interpret intent and narrate committed outcomes. Transactional SQLite state, durable idempotent operations, provenance-aware NPC knowledge, and a deterministic event clock make consequences recoverable, inspectable, and reproducible. One feature-oriented monorepo maps 11 P0 systems and five gated future systems, with seven mandatory implementation patterns ready to guide approved P0 work after implementation-readiness review.

## Document Status

This architecture document was completed through the GDS Architecture Workflow.

**Steps Completed:** 9 of 9 (Complete)

---

## Project Context

### Game Overview

**dmud — A World That Remembers** is a solo, text-based fantasy RPG and simulation in which free-text intentions produce persistent, rule-governed consequences.

An LLM interprets player intent, portrays NPCs, judges thematic fit, and narrates outcomes. The game engine remains authoritative over feasibility, mechanical validation, dice, time, ownership, resources, progression, and persistent world state.

The initial P0 proof takes place in Brackenford using three authored locations, four named NPCs, one social conflict, and a controlled gift/no-gift scenario. It must prove that NPC plans change for grounded reasons, information travels through actual contact, beliefs can differ from facts, and all consequences survive save/load.

### Technical Scope

**Primary platform:** Locally run desktop browser  
**Genre:** Text-based RPG / social simulation  
**Project level:** High architectural complexity, deliberately constrained to a medium-sized P0 implementation  
**Play mode:** Solo only for P0 and P1  
**Future networking:** Small-party co-op is conditional future scope and must not shape the initial runtime architecture prematurely

P0 is the implementation boundary. P1 systems—community viability, alchemy, affinities, achievements, titles, and daily quests—remain conditional. P2 hidden bonus objectives remain conditional on P1 evidence.

### Core Systems

| System | Scope | Complexity | Architectural significance |
| --- | --- | --- | --- |
| Free-text intent pipeline | P0 | High | Converts player language into a structured proposal without treating player claims as authoritative state |
| Rules and transaction engine | P0 | High | Validates feasibility, prerequisites, ownership, costs, stakes, and outcomes before committing an atomic change |
| LLM boundary and narration | P0 | High | Separates interpretation and presentation from authoritative mechanics; rejected or malformed proposals cannot mutate state |
| World-state model | P0 | High | Represents people, locations, items, money, relationships, obligations, commitments, plans, and progression |
| Facts, observations, and beliefs | P0 | High | Keeps historical truth distinct from NPC knowledge, received claims, uncertainty, and distortion |
| NPC planning and agency | P0 | High | Makes explicit needs, desires, resources, obligations, knowledge, and relationships affect feasible plans |
| Action clock and event scheduling | P0 | High | Advances time in seconds through validated actions and processes scheduled contacts, plans, and interrupted waits |
| Checks and progression | P0 | Medium | Resolves natural 1/20 behavior, contextual difficulty, success probability, XP, levels, skill bonuses, and attribute allocation |
| Persistence and save branches | P0 | High | Restores complete state across three manual slots and supports controlled divergent-path comparisons |
| Text interface and journal | P0 | Medium | Supports free-text input, factual navigation, explicit request state, known information, and keyboard accessibility without suggested actions |
| Diagnostics and replay evidence | P0 | High | Records proposals, validation, rolls, mutations, latency, model usage, and contradiction repairs for causal verification |
| Alchemy and persistent item effects | Conditional P1 | High | Adds recipes, ingredient consumption, crafting checks, poison application, effect duration, and narrow recipe unlock tracks |
| Community viability and commitments | Conditional P1 | High | Evaluates concrete safety, food, and protection or relocation conditions rather than narrative declarations |
| Affinities and earned progression | Conditional P1 | High | Supports limited per-affinity slots, bounded generated abilities, rarity, awards, prerequisites, and selected evolution |
| Daily quests and gacha rewards | Conditional P1 | Medium–High | Adds clock-based refresh, visible success conditions, idempotent rewards, declared pools, and distinct System presentation |
| Hidden bonus objectives | Conditional P2 | High | Stores hidden generated conditions, uses LLM judgment at completion, and validates rewards against a mechanical budget |

### Technical Requirements

#### Authority and consistency

- Player input expresses intent, not direct state mutation.
- The LLM may propose interpretations and contextual consequences but never directly commits authoritative state.
- Rules validate every persistent change before it becomes true.
- Narration must be generated from committed results and cannot invent a successful outcome.
- Mechanical changes must be atomic and idempotent: retries cannot duplicate purchases, rewards, rolls, XP, elapsed time, or resource consumption.
- Generated definitions and reusable rulings require stable identities and recorded versions.

#### Simulation and knowledge

- World facts, NPC observations or received beliefs, and player-facing presentation are separate records.
- Information spreads only through plausible observation or contact.
- A belief can be distorted, doubted, concealed, or false without changing historical truth.
- NPC plans must be constrained by resources, needs, obligations, relationships, and individual knowledge.
- Routine behavior can run through deterministic rules; consequential replanning and dialogue may involve the LLM.

#### Time and actions

- The shared game clock uses seconds and pauses while the game is closed.
- Travel uses distance divided by supported movement speed.
- Conversation, handling, transactions, and waiting advance time according to validated contextual durations.
- Reading, typing, inspecting known information, menus, inventory, journal access, and saving consume no game time.
- Event-based waits depend on actual simulated events; an LLM estimate cannot manufacture a future event.
- Long waits must stop for developments requiring player attention.

#### Persistence and reproducibility

- Three manual save slots restore the complete branch state.
- Saves include the clock, ownership, inventory, relationships, commitments, beliefs, NPC plans, XP, levels, bonuses, attribute allocation, and reward records.
- Captured structured proposals, initial state, and seeded random results must reproduce mechanical outcomes.
- Fresh LLM prose is not required to reproduce identically.
- There is no per-action undo or cross-branch reward carryover.

#### Interface and accessibility

- The primary interaction is unrestricted free-text intent within the engine's supported capabilities.
- No suggested actions, recommended dialogue, action chips, or other strategy-steering controls appear.
- Linked exits, inventory, journal, save/load, and optional roll details remain available as factual controls.
- Enter submits; Shift+Enter inserts a line; all controls are keyboard reachable.
- Speaker identity cannot depend on color alone.
- Text size should be adjustable within the proposed 16–24 px range.
- Pending, resolved, rejected, failed, and interrupted requests require clear visible states.

#### Performance and operations

Provisional evaluation targets:

- Visible input acknowledgement within 100 ms
- Local menu response within 200 ms
- Save/load within 2 seconds
- 95% of completed LLM-mediated actions within 10 seconds
- Recoverable interruption state by 30 seconds
- Test workload of a 60-minute, 100-action session with four NPCs
- Record action latency, model calls, tokens, session cost, rejected proposals, duplicate attempts, and contradiction repairs

No hard frame-rate, resolution, or memory ceiling is currently specified because the prototype is text-driven. Memory growth should still be measured across sessions.

### Complexity Drivers

#### High Complexity

1. Maintaining a hard boundary between probabilistic LLM judgment and authoritative deterministic state.
2. Committing multi-part actions exactly once despite retries, interruptions, malformed model output, or narration failure.
3. Modeling NPC knowledge separately from historical truth while making that knowledge causally affect behavior.
4. Advancing schedules and off-screen plans consistently on the same action-driven clock.
5. Saving and restoring every causal dependency needed for believable continuation and controlled replay.
6. Diagnosing whether a surprising outcome came from rules, world state, NPC knowledge, random resolution, or LLM judgment.
7. Preserving stable mechanics while allowing generated names, descriptions, rulings, and later progression content.

#### Novel Elements

- A proposal–validate–commit–narrate pipeline for free-text RPG actions.
- Inspectable social transmission where observations become fallible beliefs through actual encounters.
- NPC memory that changes feasible planning rather than merely changing dialogue.
- Later history-shaped generated progression whose theme is judged by the LLM but whose effects remain mechanically bounded.

### Technical Risks

- **Narrative contradiction:** LLM output describes facts that were rejected or never committed.
- **Partial or duplicate mutation:** interrupted or repeated requests consume resources, time, rolls, or rewards more than once.
- **Decorative memory:** NPCs can mention past events but their plans remain unaffected.
- **NPC omniscience:** information appears without observation, contact, or a recorded source.
- **State-model insufficiency:** prose implies consequences that the authoritative model cannot represent or preserve.
- **Temporal inconsistency:** travel, conversations, waits, or off-screen plans advance on incompatible clocks.
- **Save drift:** loaded branches omit beliefs, commitments, pending operations, or progression state.
- **Non-reproducible mechanics:** random or model-mediated decisions cannot be reconstructed for diagnosis.
- **Latency and provider cost:** model-mediated turns interrupt the intended 20–60-minute session rhythm.
- **Generated-content drift:** a saved ability or ruling changes mechanics because its description is regenerated.
- **Scope expansion:** conditional P1/P2 systems distort P0 before the causal-world proof passes.
- **Premature multiplayer design:** future co-op concerns introduce complexity before shared-time and concurrent-action rules exist.

### Architectural Focus

The architecture should make the following decision families explicit:

1. Runtime and engine/framework
2. Domain state and invariant boundaries
3. Structured LLM contracts
4. Action transaction lifecycle and idempotency
5. Time, events, and NPC scheduling
6. Facts, observations, beliefs, and memory retrieval
7. Persistence, saves, migrations, and replay evidence
8. UI request states, accessibility, diagnostics, and observability

The primary success criterion is explainable causal consistency, not breadth of generated content.

## Engine & Framework

### Selected Application Stack

dmud uses a browser SPA and authoritative Python API rather than a traditional game engine.

| Layer | Technology | Verified stable version |
| --- | --- | --- |
| JavaScript runtime | Node.js LTS | 24.20.0 |
| Frontend scaffold | create-vite | 9.2.0 |
| UI library | React | 19.2.8 |
| DOM renderer | React DOM | 19.2.8 |
| UI language | TypeScript | 7.0.2 |
| Frontend build | Vite | 8.2.2 |
| React build plugin | `@vitejs/plugin-react` | 6.1.1 |
| API framework | FastAPI | 0.141.1 |
| Backend language | Python | 3.14.7 |
| Python project manager | uv | 0.12.0 |
| Boundary validation | Pydantic | 2.13.5 |
| Backend settings | Pydantic Settings | 2.15.0 |
| YAML parser | PyYAML | 6.0.3 |
| API specification | OpenAPI | 3.1.0 |
| Generated API client | `@hey-api/openapi-ts` | 0.99.0 |
| Frontend runtime validation | Zod | 4.5.4 |
| Frontend server state | TanStack Query | 5.102.8 |
| Browser automation and E2E tests | Playwright | 1.63.0 |
| TypeScript tests | Vitest | 5.0.0 |
| Component test DOM | jsdom | 30.0.1 |
| React component tests | React Testing Library | 16.3.3 |
| DOM test queries | DOM Testing Library | 10.4.1 |
| Test interaction simulation | Testing Library user-event | 14.6.7 |
| DOM assertions | Testing Library jest-dom | 7.0.1 |
| TypeScript linting | ESLint | 10.9.1 |
| Type-aware linting | typescript-eslint | 8.69.0 |
| React Hooks linting | `eslint-plugin-react-hooks` | 7.1.1 |
| React Refresh linting | `eslint-plugin-react-refresh` | 0.5.6 |
| Python integration tests | pytest | 9.1.1 |
| Python static typing | Pyright strict | 1.1.411 |
| Python linting | Ruff | 0.16.6 |

Primary versions were verified on 2026-09-07 and the complete direct toolchain was revalidated on 2026-09-08. Node.js 24 is selected over the newer Current line because production tooling should use an LTS release. Exact resolved versions are committed through the frontend and backend lockfiles.

### Rationale

The SPA/API split matches dmud's authority boundary:

- React owns presentation, accessible input, request feedback, and views of server-provided state.
- FastAPI owns game rules, world state, time, random resolution, persistence, NPC decisions, and LLM orchestration.
- The browser never calculates or commits authoritative mechanical outcomes.
- Pydantic validates all data entering or leaving the Python application boundary.
- TypeScript treats API responses, browser storage, environment values, and cross-window data as unknown until runtime validation succeeds.
- OpenAPI supplies a machine-readable contract between the two applications.
- A graphics-oriented engine would add rendering, physics, scene, and asset systems that P0 does not require.

### Project Initialization

Use create-vite 9.2.0's minimal React/TypeScript scaffold and a small uv 0.12.0-managed FastAPI application:

```bash
npm create vite@9.2.0 frontend -- --template react-ts
uv init --app backend
cd backend
uv add "fastapi[standard]==0.141.1" "pydantic==2.13.5" \
  "pydantic-settings==2.15.0" "PyYAML==6.0.3"
```

Add project quality tooling after initialization:

```bash
cd frontend
npm install --save-exact \
  react@19.2.8 react-dom@19.2.8 \
  @tanstack/react-query@5.102.8 zod@4.5.4
npm install --save-dev --save-exact \
  typescript@7.0.2 vite@8.2.2 @vitejs/plugin-react@6.1.1 \
  vitest@5.0.0 jsdom@30.0.1 @playwright/test@1.63.0 \
  @testing-library/react@16.3.3 @testing-library/dom@10.4.1 \
  @testing-library/user-event@14.6.7 @testing-library/jest-dom@7.0.1 \
  eslint@10.9.1 typescript-eslint@8.69.0 \
  eslint-plugin-react-hooks@7.1.1 eslint-plugin-react-refresh@0.5.6 \
  @hey-api/openapi-ts@0.99.0
npx playwright install

cd ../backend
uv add --dev "pytest==9.1.1" "pyright==1.1.411" "ruff==0.16.6"
```

The checked-in lockfiles, not floating `latest` tags, define reproducible development versions.

**PROVIDED BY STARTER:** create-vite supplies the React entry point, Vite configuration, TypeScript project configuration, development scripts, and baseline ESLint configuration. It does not provide the feature structure, TanStack Query, generated API contract, runtime validation policy, Playwright/Vitest strategy, or any game architecture. The backend is intentionally initialized from scratch with uv rather than from a third-party FastAPI template.

### Framework-Provided Architecture

| Component | Solution | Notes |
| --- | --- | --- |
| Rendering | React DOM and CSS | Text-first semantic interface; no canvas renderer |
| Physics | None | Not required by P0/P1 |
| Audio | None | Browser audio APIs may be considered only if later scope requires them |
| Input | React and native DOM events | Free text plus factual controls; keyboard accessibility required |
| View composition | React component tree | Organize by cohesive game-facing vertical slices |
| Client routing | Not required initially | Add routing only when distinct browser URLs provide user value |
| Frontend build | Vite | Development server, React Fast Refresh, asset processing, production SPA build |
| API routing | FastAPI routers | Thin HTTP adapters invoke application use cases |
| Boundary validation | Pydantic models | External input is validated before domain logic receives it |
| API description | OpenAPI | Basis for generated or verified client contracts |
| Python environment | uv | Manages interpreter constraints, dependencies, commands, and lockfile |
| Static SPA serving | FastAPI production build output | Packaged builds use one FastAPI-served origin; development uses separate servers |
| Browser automation | Playwright | Exercises the real SPA against the real local API |
| TypeScript tests | Vitest with Testing Library conventions | Integration-first component and feature tests using accessible queries and user interactions |
| TypeScript linting | ESLint with type-aware rules | Runs separately from Vite because Vite transpiles TypeScript without type-checking |
| Python integration tests | pytest | Exercises real FastAPI routes, domain behavior, and test persistence |
| Python static analysis | Pyright strict | Complete application annotations; no implicit `Any` |
| Python linting | Ruff | Broad, explicit rule selection with narrowly documented exclusions |

### Testing and Quality Policy

#### Frontend

- Vitest covers TypeScript functions, components, and locally integrated feature behavior.
- React Testing Library uses role-, label-, and text-based queries.
- User interactions use `userEvent`; low-level event dispatch is reserved for events it cannot express.
- Playwright controls real browsers and covers full SPA-to-FastAPI workflows.
- Playwright tests use the real local API and test persistence.
- TypeScript uses `strict` compiler settings.
- ESLint runs with type-aware TypeScript and React rules.
- Vite's transpilation is never treated as a substitute for `tsc --noEmit`.

#### Backend

- pytest provides integration-first coverage through the real FastAPI ASGI application.
- Domain behavior is tested through observable API responses and persisted state where practical.
- Test persistence uses a real isolated test store rather than mocked first-party repositories.
- Pyright runs in strict mode across application code.
- Every function and application boundary has precise annotations.
- Third-party libraries lacking useful types are isolated behind typed adapters.
- Ruff enforces imports, correctness, complexity, async safety, annotations, and maintainability rules.
- Formatting, linting, type-checking, and tests are separate failing quality gates.

#### Mocking Boundary

First-party APIs, rules, persistence, and browser behavior are not mocked when they can run locally. The external LLM provider may be replaced by a deterministic contract fixture because it is paid, non-deterministic, and externally unavailable. Tests must still validate the complete proposal-validation-commit flow through the provider adapter boundary.

### MCP Decision

No engine-specific or documentation MCP is included.

Playwright, Vitest, ESLint, pytest, Pyright, and Ruff are repository dependencies and quality tools rather than MCP services. Their configuration and commands remain versioned with the project.

## Architectural Decisions

### Decision Summary

| # | Category | Decision | Verified version | Rationale |
| --- | --- | --- | --- | --- |
| 1 | State management | Authoritative current state with transactional command commits and an append-only action log | N/A | Preserves inspectability and replay evidence without full event-sourcing complexity |
| 2 | Persistence | SQLite STRICT tables, canonical versioned JSON state, relational action records, explicit migrations, snapshots, and three save slots | SQLite ≥3.37.0; current 3.53.4 | Provides local atomicity, branching, auditability, and simple distribution |
| 3 | AI systems | Provider-neutral propose → validate → commit → narrate pipeline | N/A | Prevents probabilistic model output from becoming authoritative state |
| 4 | Time and NPC simulation | Deterministic discrete-event scheduler with selective LLM-assisted replanning | N/A | Makes waits, schedules, and off-screen consequences reproducible and efficient |
| 5 | API and frontend state | OpenAPI-generated fetch client, TypeScript types, Zod schemas, TanStack Query server state, and local React presentation state | `@hey-api/openapi-ts` 0.99.0; TanStack Query 5.102.8 | Maintains one validated transport contract and one authoritative source of game state |
| 6 | Request lifecycle | Persisted operation resources with typed SSE progress, recovery polling, idempotency, and pre-commit cancellation | FastAPI 0.141.1 | Supports slow model calls, refresh recovery, visible progress, and exactly-once commits |
| 7 | Repository structure | Monorepo organized into cohesive frontend and backend vertical slices | N/A | Keeps related behavior and tests together without premature service boundaries |
| 8 | Authored content | Version-controlled YAML validated by Pydantic into an immutable content registry | N/A | Gives authors readable diffs while preserving strict runtime validation and save compatibility |
| 9 | Runtime and deployment | Split development servers; packaged FastAPI serves the SPA and API on loopback | N/A | Produces a simple local application with one production origin and backend-only secrets |

Technology versions were verified on 2026-09-07 and revalidated on 2026-09-08. Lockfiles define the exact versions used by builds and tests.

### State Management

**Approach:** Authoritative transactional domain state with an append-only action log.

The backend owns all game truth. The browser submits commands and renders query results; it never computes or commits mechanical outcomes.

Commands and queries are separate application paths:

- Commands validate intent, expected world revision, permissions, prerequisites, resources, time, and invariants before mutation.
- A successful command atomically writes the new current state and an immutable action record.
- Queries return purpose-built views without mutating state.
- Every committed mutation increments the branch's world revision and records a resulting state hash.
- A stale `expectedWorldRevision` produces a typed conflict response.
- A unique `requestId` makes mutating requests idempotent.

The append-only log supports audit, diagnostics, and replay, while snapshots remain the primary restoration mechanism. This is deliberately not full event sourcing.

Historical facts, observations, received claims, and NPC beliefs are distinct domain records. Beliefs carry provenance, confidence, subject, source, acquisition time, and truth relationship when known. Changing a belief cannot rewrite historical truth.

### Data Persistence

**Save system:** SQLite-backed local saves with versioned snapshots and relational action records.

The Python standard-library `sqlite3` module sits behind a typed persistence adapter. Domain and application code do not import SQLite APIs.

Canonical JSON text stores versioned world-state documents. Relational records index lifecycle and audit concerns, including:

- `active_branches`
- `save_slots`
- `action_records`
- `request_results`
- `operations`
- `operation_events`
- `schema_migrations`

Each branch and save records stable IDs, schema version, world revision, state hash, and timestamps. A save slot points to a complete immutable snapshot, so loading a slot restores every causal dependency rather than reconstructing an incomplete subset.

Database migrations are explicit, ordered SQL files. World-state schema changes use typed migration functions with fixtures for every supported historical version. Save/load, migration, branch divergence, request deduplication, and crash recovery receive integration coverage against real SQLite databases.

Application-owned tables use SQLite `STRICT` mode. Startup rejects SQLite versions older than 3.37.0 rather than assuming the development machine's runtime is compatible. Version 3.53.4 was the current release at validation.

### AI Systems

**Approach:** Provider-neutral propose → validate → commit → narrate pipeline.

Only the `LlmGateway` adapter knows provider-specific request and response formats. Unknown model output is validated through versioned Pydantic contracts before application code can inspect it.

An intent proposal may contain:

- Proposed action and actor
- Targets
- Player speech separated from asserted claims
- Proposed duration
- Clarification requirements
- Contextual difficulty or stakes
- Candidate consequences

The engine independently checks feasibility, chooses or validates difficulty, resolves randomness, advances time, processes events, and commits the transaction.

Narration receives committed facts and presentation context only. It cannot request mutations. Narration failure never rolls back committed mechanics; presentation can be retried independently.

Routine NPC behavior uses deterministic plans and schedules. Consequential dialogue or replanning may use the same proposal pipeline, but the engine validates the result against the NPC's actual resources, obligations, relationships, knowledge, and feasible actions.

Diagnostics record operation ID, provider, model, prompt and contract versions, latency, token usage, validated proposal, and resolution outcome. Raw provider responses are restricted to local diagnostics and excluded from normal saves and player-facing output.

### Time, Events, and NPC Processing

**Clock:** Integer seconds from a defined campaign epoch.

Actions advance the clock only by committed durations. Closing the game or waiting on an LLM does not advance simulation time.

Scheduled events are typed, versioned, and persisted with stable IDs. Deterministic ordering is:

1. Due game time
2. Event priority
3. Insertion sequence

After an action advances time, the engine processes due events within a bounded work budget. Events requiring player attention interrupt a long wait at the event's actual time. Loop detection and processing limits prevent one action from creating an unbounded event cascade.

NPC simulation is hybrid:

- Routine schedules and explicit plans execute deterministically.
- The LLM is consulted only when a consequential situation requires interpretation or replanning.
- Every proposed plan is checked against NPC knowledge, resources, relationships, obligations, and available time.
- No continuously running autonomous agents are used.

### API Contract and Frontend State

FastAPI's OpenAPI document is the transport-contract source of truth.

`@hey-api/openapi-ts` generates:

- A native fetch client
- TypeScript request and response types
- Zod runtime schemas
- TanStack Query bindings

Generated output is committed. CI regenerates it and fails on drift. The frontend validates both success and error responses at runtime.

#### Wire Format

- Successful responses use resource-specific `application/json` models rather than a generic envelope.
- Error responses use RFC 9457 `application/problem+json` with `type`, `title`, `status`, `detail`, and `instance`, extended by stable `code`, `classification`, `correlationId`, and optional `operationId` and `worldRevision` fields.
- API and provider-boundary Pydantic models use strict validation and reject unknown fields unless a contract explicitly documents extensibility.
- Generated Zod response schemas reject unknown fields at the browser boundary.
- Wall-clock timestamps use RFC 3339 UTC strings with `Z`; game time uses integer seconds from the campaign epoch; measured durations use integer milliseconds.
- JSON fields use `camelCase`, while wire enum values use lowercase `snake_case`.
- OpenAPI documents every success and problem response so generated clients require no handwritten error casting.

Example problem response:

```json
{
  "type": "/problems/insufficient-funds",
  "title": "Not enough gold",
  "status": 409,
  "detail": "You need 10 gold but have 4.",
  "instance": "/api/operations/op_019...",
  "code": "insufficient_funds",
  "classification": "rejected",
  "correlationId": "corr_019...",
  "operationId": "op_019...",
  "worldRevision": 41
}
```

Every mutation includes `requestId` and `expectedWorldRevision`. The server returns an authoritative view and new revision or a typed conflict. The browser never merges competing authoritative game states.

TanStack Query owns server-derived state, cache invalidation, request status, and recovery. Successful mutations replace or invalidate the applicable authoritative view. Mutation retries are disabled unless explicitly driven through the idempotent operation contract; safe reads may retry.

Local React state is limited to presentation concerns such as:

- Draft input
- Open panels
- Selection
- Text size
- Roll-log visibility
- Focus state

Browser storage may persist presentation preferences, but not authoritative game state. React Context remains narrow and is not used as a second state store.

### Request Lifecycle and Transport

Mutating actions use persisted operation resources:

1. `POST /api/branches/{branchId}/actions` validates the envelope and returns `202 Accepted` with an operation ID, status URL, and events URL.
2. One mutating operation executes at a time per branch. Read endpoints remain available.
3. `GET /api/operations/{operationId}/events` sends typed, versioned SSE progress.
4. `GET /api/operations/{operationId}` recovers current status and the final authoritative result.
5. `POST /api/operations/{operationId}/cancel` requests cancellation.

Representative lifecycle states include:

- `accepted`
- `interpreting`
- `needs_clarification`
- `validating`
- `resolving`
- `committed`
- `narrating`
- `complete`
- `failed`
- `interrupted`

SSE event IDs increase monotonically. Reconnection uses `Last-Event-ID`, while status polling provides a recovery path if streaming is unavailable.

Cancellation is cooperative and can abort provider work before commit. Once mechanics are committed, they remain authoritative; cancellation may only stop or defer narration.

P0 uses a supervised in-process worker with persisted lifecycle state. It does not require WebSockets, Redis, Celery, or an external broker. Refreshing, reconnecting, or retrying recovers the existing operation and never executes the action twice.

#### Restart Recovery

At startup, the operation supervisor reconciles every nonterminal operation with the atomic `request_results` record:

- If a committed request result exists, the operation is restored to `committed` or `narrating`; only narration and presentation delivery may resume.
- If no committed result exists, pre-commit work becomes `interrupted` and may be explicitly retried under the same operation and request identity.
- `needs_clarification` operations remain paused with their validated clarification contract.
- No provider call or mechanical resolution resumes automatically without first checking the authoritative request result.
- Atomic commit writes the world state, action record, request result, and committed operation state together, eliminating an ambiguous crash window.

The immutable content registry is the only backend read cache in P0. TanStack Query provides browser request caching; authoritative mutations always invalidate or replace affected game views.

### Repository and Dependency Structure

The project uses one monorepo:

```text
dmud/
├── frontend/
│   └── src/
│       ├── app/
│       ├── api/generated/
│       └── features/
│           ├── game-session/
│           ├── journal/
│           ├── inventory/
│           ├── saves/
│           └── diagnostics/
├── backend/
│   ├── src/dmud/
│   │   ├── actions/
│   │   ├── knowledge/
│   │   ├── npc_planning/
│   │   ├── simulation_time/
│   │   ├── world/
│   │   ├── saves/
│   │   ├── operations/
│   │   └── platform/
│   └── tests/
├── content/
└── tests/e2e/
```

Each feature slice groups its API adapter, commands, queries, domain behavior, persistence adapter, and tests while retaining inward dependency direction.

Domain logic cannot import FastAPI, SQLite, provider SDKs, or frontend code. HTTP handlers remain thin. Cross-cutting platform code is restricted to concrete technical capabilities such as database connections, clocks, random sources, logging, and provider adapters. Shared domain primitives are introduced only when multiple slices genuinely require the same stable concept.

### Asset and Authored-Content Management

**Loading strategy:** Preload and validate the complete P0 authored-content set at startup.

Locations, items, NPC templates, encounters, and rules are stored as version-controlled YAML with stable IDs and explicit schema versions. The loader uses `yaml.safe_load` from PyYAML, then strict Pydantic models validate structure, reject unknown fields, detect duplicate IDs, resolve cross-references, and verify compatibility before constructing an immutable in-memory registry.

Saves reference stable content IDs and content versions rather than embedding uncontrolled copies. Changes that would alter existing saved meaning require an explicit content or state migration.

Procedurally generated people, items, abilities, or rulings are persisted as versioned game state. They never silently modify authored source files.

Development reloads content through application restart. Production does not hot-reload definitions during an active session. P0 needs neither streaming asset infrastructure nor a CMS.

### Runtime, Deployment, and Security

Development runs Vite and FastAPI separately, with Vite proxying `/api` to avoid development CORS coupling.

The packaged local application builds the SPA and serves its static output and API from FastAPI on a loopback-only address. This gives P0 one process and one browser origin.

A private, local, single-user build does not require player authentication. However:

- LLM provider credentials remain backend-only.
- Secrets come from environment or OS-backed secret configuration.
- Secrets never enter browser storage, saves, authored content, generated clients, or normal logs.
- All external and persisted inputs receive runtime validation.
- Security headers and conservative request-size limits apply locally.
- SQLite data lives in an explicit application-data directory with backup and export support.

Remote binding, accounts, TLS termination, cloud hosting, or multi-user access require a separate threat model and deployment decision before implementation.

### Deferred Decisions

The following choices remain deliberately outside P0:

- Multiplayer synchronization and concurrent player actions
- Cloud hosting and cloud saves
- Remote authentication and account management
- Specific LLM provider and model selection; candidates must support the validated contract, cooperative cancellation, and usage telemetry behind `LlmGateway`
- Audio architecture
- Graphical asset streaming
- P1/P2 system internals until their evidence gates pass

These deferred concerns must not introduce abstractions or infrastructure into the P0 implementation prematurely.

### Architecture Decision Records

#### ADR-001: Current State Plus Action Log

Use transactional current-state persistence and an immutable action log rather than full event sourcing. This retains direct, comprehensible saves while preserving enough evidence for idempotency, replay diagnostics, and causal inspection.

#### ADR-002: Deterministic Engine Authority

All game truth is committed by deterministic application and domain code. LLMs may interpret, propose, judge bounded thematic questions, and narrate; they may not directly mutate state.

#### ADR-003: Durable Operations for LLM-Mediated Actions

Represent long-running actions as persisted operations with SSE progress and polling recovery. The operation boundary separates request acknowledgement, model latency, atomic commit, and recoverable narration.

#### ADR-004: Generated Transport Contract

Generate the browser client, types, runtime schemas, and query bindings from FastAPI OpenAPI. This prevents handwritten client contracts from drifting from the authoritative API.

#### ADR-005: Local-First Monolith

Use one repository and one packaged local process while maintaining strict internal dependency boundaries. Distributed infrastructure is deferred until actual deployment or multiplayer requirements justify it.

## Cross-cutting Concerns

These patterns apply to every system and are mandatory for all implementations.

### Error Handling

**Strategy:** Typed results for expected outcomes, with global boundaries for unexpected failures.

Expected gameplay outcomes return explicit result variants. Examples include rejection, clarification, revision conflict, or successful resolution. They do not raise exceptions.

Unexpected programming, persistence, and provider-adapter failures use typed exceptions caught at the HTTP or operation-worker boundary.

**Error classes:**

| Class | Meaning | State effect | Player response |
| --- | --- | --- | --- |
| `rejected` | Valid request that game rules refuse | No commit | Explain the grounded reason |
| `conflict` | Client acted against a stale revision | No commit | Refresh authoritative state |
| `recoverable` | Infrastructure or presentation work can retry | Depends on commit boundary | Preserve operation and offer recovery |
| `fatal` | Broken invariant or unrecoverable corruption | Abort and quarantine operation | Safe failure message and correlation ID |

Rules:

- Domain code must not broadly catch exceptions and continue.
- Pre-commit failures leave authoritative state unchanged.
- Post-commit narration failures retain committed mechanics.
- API responses use a consistent discriminated error schema.
- Players see actionable messages and correlation IDs, never stack traces, secrets, SQL, or provider payloads.
- Unknown exceptions are logged once at the boundary and mapped to a safe internal-error response.

**Example:**

```python
match purchase_item(command, world):
    case Accepted(change_set=changes, events=events):
        return commit_action(changes, events)
    case InsufficientFunds(required=required, available=available):
        return RejectedAction(
            code="insufficient_funds",
            message=f"You need {required} coins but have {available}.",
        )
```

Buying a 10-coin item with 4 coins returns `InsufficientFunds` and consumes no money or time. A SQLite write failure rolls back the transaction, marks the operation failed, logs its correlation ID, and returns a safe recovery response.

### Logging

**Format:** Structured JSON  
**Destinations:** Rotating local JSONL file and human-readable development console

Every operation record includes applicable correlation fields:

- `timestamp`
- `level`
- `event`
- `correlationId`
- `operationId`
- `branchId`
- `worldRevision`
- Duration and outcome fields

**Log levels:**

- `ERROR`: failed operation, broken invariant, data corruption, or exhausted recovery
- `WARN`: handled degradation, retry, contradiction repair, invalid provider output, or suspicious state
- `INFO`: operation milestones, committed actions, save/load, and lifecycle transitions
- `DEBUG`: validation decisions, scheduler execution, and adapter detail
- `TRACE`: opt-in local diagnosis only; never enabled by default

The immutable action log remains authoritative audit evidence. Operational logs explain application execution but cannot establish game truth.

Secrets, credentials, hidden objectives, complete save state, and unrestricted provider payloads are excluded. Frontend failures retain the same correlation ID and may use a narrow backend diagnostics endpoint.

No external observability service is required for P0.

**Example:**

```json
{
  "timestamp": "2026-09-07T19:42:10.152Z",
  "level": "INFO",
  "event": "action.committed",
  "correlationId": "corr_01...",
  "operationId": "op_01...",
  "branchId": "branch_main",
  "worldRevision": 42,
  "actionType": "purchase",
  "gameSecondsAdvanced": 30,
  "durationMs": 1840
}
```

### Configuration

**Approach:** Typed configuration separated by ownership.

| Configuration type | Storage | Validation |
| --- | --- | --- |
| Game invariants | Typed code constants | Static typing and tests |
| Balance and authored rules | Versioned YAML | Pydantic at startup |
| Backend platform settings | Defaults plus environment overrides | Pydantic Settings |
| Secrets | Environment or OS-backed secret storage | Backend startup validation |
| Presentation preferences | Browser storage | Zod with safe defaults |
| Authoritative game settings | SQLite world state | Domain and Pydantic validation |
| Public frontend build settings | Vite environment | Typed boundary validation |

Rules:

- Feature and domain modules never read process environment directly.
- Configuration is constructed and injected at application composition roots.
- Invalid required configuration fails startup with its exact path and reason.
- Frontend environment values are public and must never contain credentials.
- Browser storage cannot hold authoritative game state.
- P0 has no remote-configuration service.
- Balance changes that affect saved meaning require explicit schema or content migration.

**Example:**

```text
content/rules/movement.yaml       Base travel speed and movement rules
backend environment              LLM provider and application-data settings
browser preferences              Text size and roll-detail visibility
SQLite world state               Character-specific movement modifiers
```

The travel calculator receives validated movement rules and character state as explicit inputs; it does not open YAML files or inspect environment variables.

### Event System

**Pattern:** Typed domain-event values with explicit application dispatch  
**Naming:** PascalCase event types and dotted lowercase telemetry names

Examples:

- Domain event: `PurchaseCommitted`
- Scheduled event: `NpcMeetingDue`
- Operation event: `NarrationStarted`
- Telemetry event: `action.committed`

Rules:

- Domain functions return events as data; they do not publish to a global mutable bus.
- Authoritative handlers execute synchronously and deterministically inside the transaction.
- Handler ordering is explicit and tested.
- Scheduled game events use the persisted deterministic scheduler.
- Post-commit handlers may update SSE clients or telemetry but cannot mutate committed mechanics.
- External side effects never occur before the authoritative transaction commits.
- Persisted action records contain the domain events needed for diagnosis and replay evidence.
- P0 does not use an external message queue.

**Example:**

```python
result = resolve_purchase(command, world)

match result:
    case Accepted(change_set=changes, events=events):
        transaction.apply(changes)
        dispatcher.handle_authoritative(events, transaction)
        transaction.commit()
        dispatcher.handle_post_commit(events)
    case Rejected() as rejection:
        return rejection
```

`PurchaseCommitted` updates ownership and merchant inventory through deterministic authoritative handlers before commit. After commit, an SSE handler may notify the browser but cannot alter the purchase.

### Debug and Development Tools

**Strategy:** Two-tier diagnostics

#### Always available

- Player-safe request status and recovery
- Optional roll details
- Action correlation IDs
- Save integrity and application-version information
- Exportable redacted diagnostic bundles

#### Development-only

- Read-only world-state inspector
- Fact, observation, belief, and provenance viewer
- NPC resources, commitments, plans, and replanning reasons
- Game clock and scheduled-event queue
- Operation lifecycle timeline
- Redacted LLM contract viewer
- World revision and state-hash comparison
- Action replay and branch diff
- Latency, token, and session-cost summaries

Development tools activate only when the backend is loopback-bound with `DMUD_DEVTOOLS=true`. The backend publishes a typed capability response; the frontend does not infer access from its build mode.

Debug views use ordinary application queries and cannot bypass domain invariants. State-changing cheats, seed injection, and fixture controls exist only in automated-test infrastructure and are never registered as release routes.

**Example:**

Opening operation `op_01...` in the development inspector shows:

1. Submitted player intent
2. Validated structured proposal
3. Rules validation and rejected alternatives
4. Random seed and result
5. Committed change set
6. Resulting revision and state hash
7. Narration status
8. Correlated structured logs

The view redacts credentials and unrestricted raw provider data.

## Project Structure

### Organization Pattern

**Pattern:** Feature-oriented monorepo with domain-driven backend slices.

The frontend groups code by player-facing feature. The backend groups code by game-system responsibility while preserving inward dependency direction. Infrastructure remains replaceable and cannot enter domain logic.

### Directory Structure

```text
dmud/
├── frontend/
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.ts
│   ├── vitest.config.ts
│   ├── playwright.config.ts
│   ├── openapi-ts.config.ts
│   ├── eslint.config.js
│   ├── tsconfig.json
│   ├── index.html
│   ├── public/
│   └── src/
│       ├── main.tsx
│       ├── test/
│       │   └── setup.ts
│       ├── app/
│       │   ├── App.tsx
│       │   ├── ErrorBoundary.tsx
│       │   ├── queryClient.ts
│       │   └── styles.css
│       ├── api/
│       │   ├── client.ts
│       │   └── generated/
│       ├── features/
│       │   ├── game-session/
│       │   ├── operation-progress/
│       │   ├── journal/
│       │   ├── inventory/
│       │   ├── saves/
│       │   ├── roll-details/
│       │   ├── diagnostics/
│       │   └── preferences/
│       └── ui/
│           ├── Button.tsx
│           ├── Dialog.tsx
│           ├── StatusMessage.tsx
│           └── VisuallyHidden.tsx
├── backend/
│   ├── pyproject.toml
│   ├── uv.lock
│   ├── src/dmud/
│   │   ├── main.py
│   │   ├── bootstrap.py
│   │   ├── foundation/
│   │   │   ├── ids.py
│   │   │   ├── results.py
│   │   │   └── revisions.py
│   │   ├── actions/
│   │   │   ├── api.py
│   │   │   ├── contracts.py
│   │   │   ├── interpret.py
│   │   │   ├── resolve.py
│   │   │   ├── commit.py
│   │   │   └── narrate.py
│   │   ├── operations/
│   │   │   ├── api.py
│   │   │   ├── lifecycle.py
│   │   │   ├── worker.py
│   │   │   ├── store.py
│   │   │   └── stream.py
│   │   ├── world/
│   │   │   ├── models.py
│   │   │   ├── changes.py
│   │   │   ├── invariants.py
│   │   │   ├── queries.py
│   │   │   └── store.py
│   │   ├── knowledge/
│   │   │   ├── models.py
│   │   │   ├── transmission.py
│   │   │   └── queries.py
│   │   ├── npc_planning/
│   │   │   ├── models.py
│   │   │   ├── routines.py
│   │   │   ├── replan.py
│   │   │   └── feasibility.py
│   │   ├── simulation_time/
│   │   │   ├── clock.py
│   │   │   ├── events.py
│   │   │   └── scheduler.py
│   │   ├── checks/
│   │   │   ├── models.py
│   │   │   ├── resolve.py
│   │   │   └── progression.py
│   │   ├── inventory/
│   │   │   ├── models.py
│   │   │   └── transactions.py
│   │   ├── saves/
│   │   │   ├── api.py
│   │   │   ├── application.py
│   │   │   ├── models.py
│   │   │   ├── store.py
│   │   │   └── state_migrations/
│   │   ├── authored_content/
│   │   │   ├── models.py
│   │   │   ├── loader.py
│   │   │   └── registry.py
│   │   ├── diagnostics/
│   │   │   ├── api.py
│   │   │   ├── queries.py
│   │   │   └── export.py
│   │   ├── integrations/
│   │   │   └── llm/
│   │   │       ├── gateway.py
│   │   │       ├── provider.py
│   │   │       └── telemetry.py
│   │   └── platform/
│   │       ├── config.py
│   │       ├── logging.py
│   │       └── sqlite/
│   │           ├── connection.py
│   │           ├── migrate.py
│   │           └── migrations/
│   │               └── 0001_initial_schema.sql
│   └── tests/
│       ├── integration/
│       ├── contract/
│       ├── fixtures/
│       │   ├── worlds/
│       │   │   ├── p0-start.yaml
│       │   │   ├── p0-gift-committed.yaml
│       │   │   └── p0-no-gift.yaml
│       │   └── llm/
│       │       ├── proposals/
│       │       └── narrations/
│       └── unit/
├── content/
│   ├── manifest.yaml
│   ├── rules/
│   │   ├── movement.yaml
│   │   ├── checks.yaml
│   │   └── progression.yaml
│   └── worlds/
│       └── brackenford/
│           ├── world.yaml
│           ├── locations/
│           │   ├── market-square.yaml
│           │   ├── maras-stall.yaml
│           │   └── common-room.yaml
│           ├── npcs/
│           │   ├── mara.yaml
│           │   ├── oren.yaml
│           │   ├── tessa.yaml
│           │   └── ivo.yaml
│           ├── items/
│           │   └── drink.yaml
│           ├── conflicts/
│           │   └── maras-debt.yaml
│           └── checks/
│               └── payment-extension.yaml
├── contracts/
│   └── openapi.json
├── tests/
│   └── e2e/
├── docs/
├── scripts/
│   ├── export_openapi.py
│   └── check_contract_drift.py
├── .github/
│   └── workflows/
│       └── quality.yml
├── _bmad/
├── _bmad-output/
├── .env.example
├── .gitignore
└── README.md
```

Runtime databases, saves, logs, provider responses, secrets, build output, and test artifacts live outside source control.

### System Location Mapping

| System | Location | Responsibility |
| --- | --- | --- |
| Free-text action lifecycle | `backend/src/dmud/actions/` | Interpret, validate, resolve, commit, and narrate |
| Durable request processing | `backend/src/dmud/operations/` | Operation state, worker execution, SSE, recovery, cancellation |
| Authoritative world state | `backend/src/dmud/world/` | World model, change sets, invariants, query views |
| Facts and beliefs | `backend/src/dmud/knowledge/` | Facts, observations, claims, provenance, transmission |
| NPC agency | `backend/src/dmud/npc_planning/` | Needs, obligations, routines, feasible plans, replanning |
| Clock and scheduled events | `backend/src/dmud/simulation_time/` | Campaign clock, ordering, bounded event processing |
| Checks and P0 progression | `backend/src/dmud/checks/` | Difficulty, seeded rolls, XP, levels, bonuses |
| Inventory and transactions | `backend/src/dmud/inventory/` | Ownership, quantity, money, gifts, purchases |
| Save slots and branches | `backend/src/dmud/saves/` | Complete snapshots, loading, branching, state migration |
| Authored-content runtime | `backend/src/dmud/authored_content/` | YAML validation and immutable lookup |
| LLM provider boundary | `backend/src/dmud/integrations/llm/` | Provider-neutral gateway and provider adapter |
| Runtime infrastructure | `backend/src/dmud/platform/` | SQLite, migrations, configuration, logging |
| Stable shared primitives | `backend/src/dmud/foundation/` | Typed IDs, revisions, hashes, result primitives |
| Game transcript and input | `frontend/src/features/game-session/` | Free-text input, transcript, factual exits |
| Request feedback | `frontend/src/features/operation-progress/` | Progress, interruption, recovery, cancellation |
| Known-information journal | `frontend/src/features/journal/` | Facts, concerns, commitments, known evidence |
| Inventory interface | `frontend/src/features/inventory/` | Owned items, money, factual transaction controls |
| Save/load interface | `frontend/src/features/saves/` | Three slots, branch selection, load confirmation |
| Roll evidence | `frontend/src/features/roll-details/` | Targets, modifiers, probability, rolls |
| Diagnostics interface | `frontend/src/features/diagnostics/` | Capability-gated read-only inspection |
| Presentation preferences | `frontend/src/features/preferences/` | Text size and local presentation settings |
| API contract | `contracts/openapi.json` and `frontend/src/api/generated/` | Exported OpenAPI and generated browser client |
| Brackenford content | `content/worlds/brackenford/` | Authored locations, NPCs, items, conflict, check |
| Backend integration coverage | `backend/tests/integration/` | Real FastAPI, SQLite, save, transaction, and worker behavior |
| Browser journeys | `tests/e2e/` | Playwright against the real SPA and API |
| LLM test contracts | `backend/tests/fixtures/llm/` | Deterministic substitutes at the external boundary |

Conditional systems receive dedicated slices only after their evidence gates pass:

- `alchemy/`
- `community_viability/`
- `affinities/`
- `achievements/`
- `daily_quests/`
- `hidden_objectives/`

They must not be folded into generic P0 modules in anticipation of later scope.

### Content and Asset Rules

- `content/manifest.yaml` declares content schema and package versions.
- Stable content IDs are explicit and do not depend on file paths.
- Brackenford geography and connections are authored in `world.yaml`.
- Locations are never procedurally generated.
- Production content and controlled test starting states remain separate.
- `frontend/public/` contains only static files actually used by the browser.
- CSS tokens and interface styling remain under `frontend/src/app/`.
- P0 creates no empty art, audio, portrait, sprite, animation, or generated-image directories.
- Any later media is organized by its owning feature after that scope is approved.

### Naming Conventions

#### Files

- Python modules use `snake_case.py`.
- Python tests use `test_<behavior>.py`.
- React components use `PascalCase.tsx`.
- React hooks use `useCamelCase.ts`.
- Other TypeScript modules use `camelCase.ts`.
- TypeScript tests use `<subject>.test.ts` or `<subject>.test.tsx`.
- Feature directories and YAML files use `kebab-case`.
- SQL migrations use a zero-padded sequence and description.
- Generated OpenAPI files follow generator conventions and are never manually renamed.

#### Code and Data Elements

| Element | Convention | Example |
| --- | --- | --- |
| Python function or variable | `snake_case` | `resolve_purchase` |
| Python class or result variant | `PascalCase` | `InsufficientFunds` |
| Python constant | `UPPER_SNAKE_CASE` | `MAX_EVENTS_PER_ACTION` |
| TypeScript function or variable | `camelCase` | `formatGameTime` |
| React component | `PascalCase` | `ActionComposer` |
| Boolean | Predicate form | `isTransferable`, `hasWitness` |
| API path | Plural `kebab-case` nouns | `/api/operations/{operationId}` |
| JSON field | `camelCase` | `expectedWorldRevision` |
| Wire enum value | Lowercase `snake_case` | `needs_clarification` |
| Database table or column | `snake_case` | `operation_events.world_revision` |
| YAML key | `snake_case` | `movement_speed` |
| Stable content ID | Namespaced lowercase | `location:brackenford:market-square` |
| Domain event | Past-tense `PascalCase` | `PurchaseCommitted` |
| Scheduled event | Descriptive `PascalCase` | `NpcMeetingDue` |
| Telemetry event | Dotted lowercase | `action.committed` |
| Server-owned resource ID | Prefix plus UUIDv7 | `op_019...`, `branch_019...` |
| Browser request ID | Prefix plus UUIDv4 | `req_550e8400...` |

Commands use imperative names such as `PurchaseItem`. Queries use descriptive names such as `GetKnownInformation`. Acronyms are treated as words: `LlmGateway`, `SseStream`, and `NpcPlan`.

Python models expose `snake_case` internally and explicit aliases produce `camelCase` JSON. Server-owned resource IDs use Python 3.14's UUIDv7 for sortable locality. Browser-generated `requestId` values prefix `crypto.randomUUID()` UUIDv4 values; they promise uniqueness, not ordering.

### Architectural Boundaries

1. **Authority:** Only backend command handlers may request authoritative changes. The frontend, SSE handlers, diagnostics, and narration cannot mutate game truth.

2. **Dependency direction:** HTTP and infrastructure adapters depend inward on application and domain behavior. Domain modules cannot import FastAPI, SQLite, provider SDKs, environment access, or frontend code.

3. **Transaction ownership:** `actions/commit.py` coordinates atomic game-state and action-record commits. Individual features return validated changes and events rather than opening independent transactions.

4. **LLM isolation:** Provider-specific code exists only under `integrations/llm/`. Game systems depend on the provider-neutral `LlmGateway`.

5. **Persistence access:** SQLite access occurs through explicit typed stores or the platform connection layer. HTTP handlers and domain functions never execute SQL.

6. **Event safety:** Authoritative handlers execute deterministically before commit. Post-commit handlers may publish progress or telemetry but cannot change mechanics.

7. **Content immutability:** Authored YAML is validated once into an immutable registry. Runtime-generated content is persisted as state and never rewrites authored files.

8. **Frontend state:** TanStack Query owns server state. Feature-local React state owns presentation only. Features use the generated API client rather than handwritten fetch calls.

9. **Generated code:** `frontend/src/api/generated/` and `contracts/openapi.json` are regenerated from FastAPI OpenAPI. Generated files are committed but never manually edited.

10. **Feature coupling:** Cross-feature behavior flows through explicit application commands, queries, or typed events. Features do not reach into one another's persistence implementation.

11. **Testing boundary:** First-party rules, routes, persistence, and browser behavior use real local implementations in integration tests. Only external providers may use deterministic contract fixtures.

12. **Scope gates:** Conditional P1/P2 directories and abstractions are introduced only after their requirements are approved.

## Implementation Patterns

These patterns are mandatory for consistent implementation across all contributors.

### Novel Patterns

#### Causal Action Transaction

**Purpose:** Ensure free-text actions produce at most one authoritative, recoverable commit despite retries, interruptions, model failures, or narration failures.

**Components:**

- Action API
- Operation store
- Intent interpreter
- Rule validator
- Resolver
- Commit coordinator
- Narrator
- Query projector

**Data flow:**

```text
request
  → recover/create operation
  → interpret proposal
  → validate feasibility
  → resolve check and time
  → construct complete change set
  → atomic commit
  → narrate committed facts
  → return authoritative view
```

**Rules:**

- `requestId` identifies one logical attempt.
- Duplicate submissions recover the original operation or result.
- `expectedWorldRevision` is checked before resolution and inside the write transaction.
- Random inputs are sampled once and recorded.
- One action produces at most one authoritative commit.
- An interrupted composite action commits only completed effects.
- Narration occurs after the authoritative transaction.
- Pre-commit cancellation changes no game state.
- Post-commit narration failure preserves mechanics.

**Example:**

```python
async def execute_action(
    command: SubmitAction,
    dependencies: ActionDependencies,
) -> ActionResult:
    operation = dependencies.operations.recover_or_create(
        command.request_id
    )
    proposal = await dependencies.interpreter.propose(command.intent)
    validated = validate_proposal(proposal, operation.initial_world)

    match validated:
        case Rejected() as rejection:
            return dependencies.operations.reject(operation, rejection)
        case NeedsClarification() as clarification:
            return dependencies.operations.await_clarification(
                operation,
                clarification,
            )
        case Accepted() as accepted:
            resolution = resolve_action(
                accepted,
                operation.initial_world,
                dependencies.random_source,
            )
            committed = dependencies.committer.commit_once(
                operation,
                command.expected_world_revision,
                resolution,
            )

    narration = await dependencies.narrator.describe(committed.facts)
    return dependencies.operations.complete(committed, narration)
```

**Use when:** Processing any player or consequential NPC action that may change authoritative state.

#### Provenanced Belief Propagation

**Purpose:** Allow information to spread through actual observation and contact without confusing claims or beliefs with historical truth.

**Components:**

- Fact ledger
- Observation builder
- Claim builder
- Transmission handler
- Belief updater
- Knowledge query
- NPC planner
- Diagnostic projector

**Data flow:**

```text
committed event
  → historical fact
  → witness-specific observation
  → optional spoken claim
  → encounter-based transmission
  → listener belief update
  → optional NPC replanning
```

**Rules:**

- Facts, observations, claims, and beliefs use separate types.
- Each derived record points to its immediate source and causation chain.
- An observation records witness, place, game time, perceptible details, and uncertainty.
- A claim records speaker, listener, encounter, communicated meaning, and source disclosure.
- A belief records subject, proposition, confidence, provenance, acquisition time, and status.
- Belief updates preserve prior history.
- A claim may be truthful, mistaken, distorted, deceptive, or incomplete.
- Belief changes may trigger replanning but cannot compel a predetermined response.
- Retry IDs deduplicate transmissions; genuinely repeated reports remain new events.

**Example:**

```python
def transmit_claim(
    encounter: Encounter,
    claim: Claim,
    listener: NpcKnowledge,
) -> BeliefUpdateResult:
    if claim.speaker_id not in encounter.participant_ids:
        return TransmissionRejected("speaker_not_present")

    if listener.owner_id not in encounter.participant_ids:
        return TransmissionRejected("listener_not_present")

    confidence = evaluate_confidence(
        prior_beliefs=listener.beliefs,
        source_id=claim.speaker_id,
        relationship=encounter.relationship,
        disclosed_source=claim.disclosed_source,
    )

    return BeliefUpdated(
        belief=Belief.from_claim(claim, confidence),
        provenance=Provenance(
            source_claim_id=claim.id,
            encounter_id=encounter.id,
            acquired_at=encounter.game_time,
        ),
    )
```

For the P0 rumor variant, Tessa can tell Ivo about the witnessed gift only when they meet in the Common Room. Ivo's distrust may lower confidence and cause him to seek confirmation. Without the meeting, no information propagates.

**Use when:** Recording knowledge, dialogue claims, rumors, corrections, deception, or knowledge-driven NPC decisions.

#### Interruptible Deterministic Time Advance

**Purpose:** Advance the seconds-based simulation reproducibly while allowing meaningful scheduled events to interrupt longer actions.

**Components:**

- Action phase planner
- Campaign clock
- Persisted event queue
- Deterministic scheduler
- Event-handler registry
- Attention classifier
- Resolution accumulator

**Ordering:**

```text
(due_game_time, priority, insertion_sequence)
```

**Data flow:**

```text
resolved timed phases
  → determine next event or phase boundary
  → advance working clock
  → apply completed phase effects
  → process events at that instant
  → stop if player attention is required
  → otherwise continue
  → return one accumulated resolution for commit
```

**Rules:**

- Time advances only through committed action resolution.
- LLM latency, browser activity, menus, and application downtime consume no game time.
- Event handlers are deterministic for the same state and recorded random inputs.
- Events created during processing receive a stable insertion sequence.
- Interruptions occur at the event's actual game time.
- Only completed phases produce their completion effects.
- The queue, insertion counter, clock, and processed-event evidence are saved.
- A bounded event budget prevents recursive or same-time loops.
- "Wait until X" cannot invent an event when X is impossible or unscheduled.

**Example:**

```python
def advance_until_interrupted(
    world: WorldState,
    phases: tuple[ActionPhase, ...],
    scheduler: Scheduler,
    event_budget: int,
) -> TimeAdvanceResult:
    working = world.copy()
    completed_effects: list[WorldChange] = []
    processed_events: list[ProcessedEvent] = []
    remaining_events = event_budget

    for phase in phases:
        while scheduler.has_due_event_before(phase.ends_at):
            if remaining_events == 0:
                return EventBudgetExceeded()

            event = scheduler.pop_next()
            working.clock = event.due_game_time
            outcome = scheduler.handle(event, working)
            processed_events.append(outcome.record)
            remaining_events -= 1

            if outcome.requires_player_attention:
                return Interrupted(
                    world=working,
                    completed_effects=tuple(completed_effects),
                    processed_events=tuple(processed_events),
                )

        working.clock = phase.ends_at
        phase.apply_completion_effects(working)
        completed_effects.extend(phase.completion_effects)

    return Completed(
        world=working,
        completed_effects=tuple(completed_effects),
        processed_events=tuple(processed_events),
    )
```

If a five-second pouch transfer is interrupted after three seconds, three seconds and the interrupting event may commit, but ownership remains unchanged because the transfer phase did not complete.

**Use when:** Resolving travel, conversation, handling, waiting, NPC schedules, and any action whose intended duration crosses scheduled events.

### Communication Patterns

**Pattern:** Explicit dependency injection with typed calls and events.

Rules:

- Composition roots construct concrete dependencies.
- Application services receive dependencies through constructors or function parameters.
- Direct typed calls handle request/response behavior within a slice.
- Typed events handle one-to-many reactions.
- Generated HTTP clients are used across the browser/API boundary.
- Global service registries, mutable singletons, and feature-owned containers are prohibited.
- Tests replace only explicit external boundaries.

**Example:**

```python
@dataclass(frozen=True)
class ActionDependencies:
    operations: OperationStore
    worlds: WorldStore
    llm: LlmGateway
    random_source: RandomSource
    dispatcher: DomainEventDispatcher


def build_action_service(settings: Settings) -> ActionService:
    database = open_database(settings.database_path)
    return ActionService(
        dependencies=ActionDependencies(
            operations=SqliteOperationStore(database),
            worlds=SqliteWorldStore(database),
            llm=ConfiguredLlmGateway(settings.llm),
            random_source=RecordedRandomSource(),
            dispatcher=build_event_dispatcher(),
        )
    )
```

### Entity Patterns

**Creation:** Slice-owned typed factory functions.

Rules:

- Factories accept validated inputs and explicit dependencies.
- Factories return complete valid entities or typed rejections.
- IDs come from an injected typed ID source.
- Authored templates and runtime entities remain distinct types.
- Snapshot rehydration uses a separate validated migration path.
- Test builders remain in test code.
- Universal entity factories and managers are prohibited.

**Example:**

```python
def create_npc(
    template: NpcTemplate,
    location_id: LocationId,
    ids: IdSource,
) -> NpcCreationResult:
    if location_id not in template.allowed_start_locations:
        return InvalidStartLocation(location_id)

    return NpcCreated(
        npc=Npc(
            id=ids.next_npc_id(),
            template_id=template.id,
            location_id=location_id,
            resources=template.initial_resources,
            obligations=template.initial_obligations,
            plan=template.initial_plan,
            knowledge=NpcKnowledge.from_template(
                template.initial_knowledge
            ),
        )
    )
```

### State Patterns

**Pattern:** Explicit finite-state transitions for lifecycle-bearing records.

Rules:

- Use discriminated unions or enums, not combinations of lifecycle booleans.
- Each transition declares allowed sources, target, required data, and emitted event.
- Invalid transitions return typed rejections.
- Transition functions are pure; owning commands persist their results.
- Python and TypeScript matches must be exhaustive.
- NPC plans use explicit statuses rather than behavior trees.
- Ordinary changes use validated change sets rather than unnecessary state machines.

**Example:**

```python
def transition_operation(
    operation: Operation,
    command: OperationTransition,
) -> OperationTransitionResult:
    match operation.status, command:
        case OperationStatus.ACCEPTED, BeginInterpretation():
            return Transitioned(
                operation=operation.with_status(
                    OperationStatus.INTERPRETING
                ),
                event=InterpretationStarted(operation.id),
            )
        case OperationStatus.COMMITTED, BeginNarration():
            return Transitioned(
                operation=operation.with_status(
                    OperationStatus.NARRATING
                ),
                event=NarrationStarted(operation.id),
            )
        case _:
            return InvalidOperationTransition(
                current=operation.status,
                attempted=command.name,
            )
```

### Data Patterns

**Access:** Slice-specific typed stores plus explicit command and query paths.

Rules:

- Store protocols use owning-domain terminology.
- SQLite adapters implement those protocols.
- Commands load only state required for validation and change construction.
- Queries use dedicated read projections.
- Multi-slice writes use one commit coordinator and transaction.
- Domain models contain no SQL, file paths, persistence methods, or lazy database relationships.
- Authored content enters through an injected immutable `ContentRegistry`.
- Generic data managers, catch-all repositories, and active-record models are prohibited.

**Example:**

```python
class WorldStore(Protocol):
    def get_branch(
        self,
        branch_id: BranchId,
        expected_revision: WorldRevision,
    ) -> WorldSnapshot | RevisionConflict:
        ...

    def stage_changes(
        self,
        transaction: Transaction,
        branch_id: BranchId,
        changes: WorldChangeSet,
    ) -> StagedWorld:
        ...


class GetGameView:
    def __init__(self, queries: GameViewQueries) -> None:
        self._queries = queries

    def execute(self, branch_id: BranchId) -> GameView:
        return self._queries.for_branch(branch_id)
```

### Consistency Rules

| Pattern | Convention | Enforcement |
| --- | --- | --- |
| Action authority | One idempotent commit per logical request | Integration tests over retries and failures |
| Knowledge provenance | Facts, observations, claims, and beliefs remain distinct | Model types, content fixtures, causal scenario tests |
| Time advancement | Ordered events and completed action phases only | Seeded scheduler integration tests |
| Dependencies | Explicit injection from composition roots | Import rules, review, strict typing |
| Entity construction | Slice-owned factories | Factory tests and restricted constructors where useful |
| Lifecycle changes | Exhaustive transition functions | Type checking and transition-table tests |
| Data access | Typed stores and separate query paths | Import rules and real SQLite integration tests |
| API usage | Generated client only | ESLint restrictions and contract-drift CI |
| Runtime validation | Pydantic backend, Zod frontend | Boundary tests |
| Errors | Typed expected results, boundary exceptions | API contract tests |
| Events | Typed values with explicit ordering | Handler registration tests |
| Generated files | Never manually edited | Regeneration and clean-diff CI |
| External mocking | LLM provider boundary only | Test review and fixture ownership |

## Architecture Validation

### Validation Summary

| Check | Result | Notes |
| --- | --- | --- |
| Decision Compatibility | PASS | SPA/API, persistence, operations, simulation, and LLM boundaries are compatible |
| GDD Coverage | PASS | All 16 P0 and conditional systems have architectural support |
| Pattern Completeness | PASS | Seven patterns cover authority, knowledge, time, communication, creation, lifecycle, and data access |
| Epic Mapping | PASS | E1–E6 map to implemented or explicitly gated slices |
| Document Completeness | PASS | All mandatory sections exist; no placeholders or stale decisions remain |
| Technology Compatibility | PASS | Runtime versions, framework requirements, storage minimums, and direct dependencies are explicit |
| Security Boundary | PASS | Loopback-only P0, backend-only secrets, strict validation, and safe errors are defined |

### Coverage Report

**Systems Covered:** 16/16  
**P0 Systems Covered:** 11/11  
**Conditional Systems Mapped:** 5/5  
**Epics Mapped:** 6/6  
**Patterns Defined:** 7  
**Decisions Made:** 9  
**Mandatory Sections Present:** 7/7

### Issues Resolved

1. Added a two-sentence executive summary.
2. Removed the obsolete remaining-decisions section.
3. Added verified direct toolchain and supporting dependency versions.
4. Recorded Node.js LTS selection and exact starter commands.
5. Marked what create-vite provides and what remains project-owned.
6. Defined RFC 9457 errors and canonical wire formats.
7. Defined strict Pydantic and Zod boundary validation.
8. Added deterministic restart recovery for nonterminal operations.
9. Distinguished server UUIDv7 resource IDs from browser UUIDv4 request IDs.
10. Established SQLite 3.37.0 as the minimum and selected `STRICT` tables.
11. Reconciled the earlier repository sketch with the final `actions/` structure.
12. Explicitly deferred LLM provider/model selection behind compatibility criteria.
13. Defined frontend and backend caching boundaries.

### Readiness Boundary

The architecture is ready to guide repository scaffolding and approved P0 implementation. The GDD and epics remain draft-for-correction documents; unresolved G03, G04, and G18 tuning and all conditional P1/P2 requirements must pass their own specification gates before implementation.

A separate implementation-readiness review should validate GDD, architecture, and story alignment before production work begins.

### Validation Date

2026-09-08

## Development Environment

### Prerequisites

| Requirement | Version or constraint |
| --- | --- |
| Git | Current supported release |
| Node.js | 24.20.0 LTS |
| npm | Version bundled with Node.js 24.20.0 |
| Python | 3.14.7 |
| uv | 0.12.0 |
| SQLite | 3.37.0 minimum through Python `sqlite3` |
| Browser binaries | Installed and managed by Playwright |
| LLM credentials | Required only for real-provider runs; never needed for deterministic contract tests |

Startup must reject an incompatible SQLite runtime before opening application data.

### AI Tooling

No engine-specific or documentation MCP server was selected. The project uses repository-managed Playwright, Vitest, ESLint, pytest, Pyright, and Ruff tooling. An MCP integration may be evaluated later if it provides concrete value without changing architectural authority.

### Initial Setup

```bash
npm create vite@9.2.0 frontend -- --template react-ts
uv init --app backend

cd backend
uv add "fastapi[standard]==0.141.1" "pydantic==2.13.5" \
  "pydantic-settings==2.15.0" "PyYAML==6.0.3"
uv add --dev "pytest==9.1.1" "pyright==1.1.411" "ruff==0.16.6"

cd ../frontend
npm install --save-exact \
  react@19.2.8 react-dom@19.2.8 \
  @tanstack/react-query@5.102.8 zod@4.5.4
npm install --save-dev --save-exact \
  typescript@7.0.2 vite@8.2.2 @vitejs/plugin-react@6.1.1 \
  vitest@5.0.0 jsdom@30.0.1 @playwright/test@1.63.0 \
  @testing-library/react@16.3.3 @testing-library/dom@10.4.1 \
  @testing-library/user-event@14.6.7 @testing-library/jest-dom@7.0.1 \
  eslint@10.9.1 typescript-eslint@8.69.0 \
  eslint-plugin-react-hooks@7.1.1 eslint-plugin-react-refresh@0.5.6 \
  @hey-api/openapi-ts@0.99.0
npx playwright install
```

Commit both lockfiles after scaffolding.

### Required Configuration Files

- `frontend/openapi-ts.config.ts` defines fetch, types, Zod, and TanStack Query generation from `contracts/openapi.json`.
- `frontend/src/test/setup.ts` installs Vitest DOM assertions.
- `frontend/playwright.config.ts` points to `tests/e2e/` and starts the real SPA and API.
- `backend/pyproject.toml` contains strict Pyright and Ruff policy.
- `.env.example` documents non-secret backend configuration names.

### Contract Generation

```bash
uv run --project backend python scripts/export_openapi.py
npm --prefix frontend run api:generate
git diff --exit-code -- contracts/openapi.json frontend/src/api/generated
```

CI fails when the generated contract differs from committed output.

### Quality Commands

```bash
uv run --project backend ruff format --check backend/src backend/tests
uv run --project backend ruff check backend/src backend/tests
uv run --project backend pyright
uv run --project backend pytest

npm --prefix frontend run lint
npm --prefix frontend exec tsc -- --noEmit
npm --prefix frontend exec vitest run
npm --prefix frontend exec playwright test
```

### Local Development

```bash
uv run --project backend fastapi dev backend/src/dmud/main.py
npm --prefix frontend run dev
```

Vite proxies `/api` to the loopback FastAPI server. Real LLM runs receive backend-only credentials through validated settings; ordinary tests use deterministic provider fixtures.

### First Implementation Steps

1. Create the approved directory structure and composition roots.
2. Add SQLite version checking and the first strict migration.
3. Load and validate the Brackenford content registry.
4. Export OpenAPI and generate the browser contract.
5. Establish green lint, type, integration-test, and browser-test baselines.
6. Implement P0 stories only after the implementation-readiness review confirms their inputs.
