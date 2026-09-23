---
title: 'Game Architecture'
project: 'dmud'
date: '2026-09-07'
author: 'Kyle'
version: '1.2'
updated: '2026-09-15'
revisionScope: 'GDD 0.8 staged-systems reconciliation'
gddVersion: '0.8'
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9]
status: 'complete'
engine: 'React SPA with authoritative FastAPI API'
platform: 'Local desktop browser'

# Source Documents
gdd: '/Users/kyle/Documents/Work/dmud/_bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/gdd.md'
epics: '_bmad-output/planning-artifacts/epics.md'
gddCompanionEpics: '_bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/epics.md'
uxDesign: '_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/DESIGN.md'
uxExperience: '_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md'
brief: '/Users/kyle/Documents/Work/dmud/_bmad-output/planning-artifacts/briefs/brief-dmud-2026-09-05/brief.md'
---

# Game Architecture

## Executive Summary

dmud uses a local-first React SPA and authoritative FastAPI API, with a deterministic Python domain engine owning all mechanics and persistent truth while bounded LLM integrations interpret intent and narrate committed outcomes. Transactional SQLite state, durable idempotent operations, provenance-aware NPC knowledge, and a deterministic event clock make consequences recoverable, inspectable, and reproducible. The feature-oriented monorepo keeps P0 as the only authorized implementation scope while defining compatible, evidence-gated boundaries for P1–P9 resources, effects, access, survival, livelihoods, crafting, spells, quests, and combat.

## Document Status

This architecture document was completed through the GDS Architecture Workflow.

**Steps Completed:** 9 of 9 (Complete)

Version 1.2 incorporates the approved GDD 0.8 staged-design baseline on 2026-09-15. It preserves the GDD 0.4 Session 0 and P0 UX contracts while adding architecture for the conditional P1–P9 sequence. This is a documentation reconciliation; implementation authorization, readiness review, and runtime verification remain separate checks.

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
**Play mode:** Solo throughout P0–P9
**Future networking:** Small-party co-op is conditional future scope and must not shape the initial runtime architecture prematurely

P0 is the implementation boundary. The approved design sequence is P1 effects and resources; P2 places, access, and ownership; P3 needs and shelter; P4 autonomous livelihoods; P5 community and alchemy; P6 spells and recognition; P7 daily quests; P8 hidden quest bonuses; and P9 combat. Each stage remains conditional on evidence from the stage before it and must not be pulled into an earlier implementation merely because its design is approved.

### Core Systems

| System | Scope | Complexity | Architectural significance |
| --- | --- | --- | --- |
| Campaign entry and Session 0 | P0 | High | Persists categorized drafts, validates starting attributes, and atomically confirms one campaign |
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
| Resources and shared effects | Conditional P1 | High | Derives Health, Mana, and Stamina; validates bounded effect definitions; resolves stacking, ticks, removal, clamping, and death deterministically |
| Places, access, and ownership | Conditional P2 | High | Models local resources, entrances, keys, permission, capacity, force, theft, evidence, and separate property truth from character knowledge |
| Needs, food, and shelter | Conditional P3 | High | Tracks hunger and sleep thresholds, `Starved`, `Exhausted`, `Exposed`, food batches, spoilage, adequate sleep, and recovery |
| Autonomous livelihoods | Conditional P4 | High | Executes wants-driven work, purchase, cooking, eating, sleep, and replanning through finite resources on the shared clock |
| Community viability and alchemy | Conditional P5 | High | Evaluates lived stability through causal meals, sleep, and protection while adding bounded alchemy recipes and demand |
| Spells and recognition | Conditional P6 | High | Supports affinity-owned spell slots, stable generated presentation, fixed mechanics, Mana costs, earned evolution, titles, and achievements |
| Daily quests and gacha rewards | Conditional P7 | Medium–High | Adds clock-based refresh, visible success conditions, idempotent rewards, a declared pool, and distinct System presentation |
| Hidden bonus objectives | Conditional P8 | High | Stores private generated conditions, uses bounded LLM judgment at completion, and commits at most one budgeted reward |
| Bounded combat | Conditional P9 | High | Reuses resources, effects, access, items, and time for one authored encounter with deterministic rounds, exits, death, and persistence |

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
- Property truth never grants knowledge by itself; observations, testimony, evidence, and inference are the only paths into character belief.
- Player and NPC characters use the same resource, need, effect, access, and death rules when their owning stage is enabled.

#### Time and actions

- The shared game clock uses seconds and pauses while the game is closed.
- Travel uses distance divided by supported movement speed.
- Conversation, handling, transactions, and waiting advance time according to validated contextual durations.
- Reading, typing, inspecting known information, menus, inventory, journal access, and saving consume no game time.
- Event-based waits depend on actual simulated events; an LLM estimate cannot manufacture a future event.
- Long waits must stop for developments requiring player attention.
- Same-timestamp work resolves in the GDD-defined order: completed actions and continuous intervals; effect ticks and need thresholds; expirations and environmental transitions; then derived-value recalculation, clamping, and terminal states.
- Off-screen work occurs only as game time advances and uses the same costs, access checks, and commit path as observed work.

#### Staged mechanics

- The save ruleset version records the highest implemented stage once later stages ship; P0 does not build a generic feature-flag or capability-registry framework in anticipation.
- P1 initializes prior P0 characters' Health, Mana, and Stamina at their derived maxima through an explicit save migration.
- Generated effects, spells, rewards, and reusable rulings have stable identities, schema versions, immutable accepted mechanics, and separately generated presentation.
- Physical access is resolved from location, entrance state, permission, keys, tools, capacity, and paid action costs; ownership is neither remote access nor an automatic prohibition on physical use.
- Hunger, fatigue, work, crafting, quests, and combat are ordinary validated actions and scheduled events, not alternate mutation channels.
- Later-stage modules may depend on proven lower-stage domain contracts; lower-stage modules cannot import later-stage rules.

#### Persistence and reproducibility

- Three manual save slots restore the complete branch state.
- Saves include the clock, ownership, inventory, relationships, commitments, beliefs, NPC plans, XP, levels, bonuses, attribute allocation, and reward records.
- When enabled, saves also include ruleset stage/version, resource pools, effect definitions and instances, scheduled ticks, need timers, access state, permissions, keys, item identity or batch provenance, crafting jobs, quest state, hidden conditions, reward claims, and combat state.
- Captured structured proposals, initial state, and seeded random results must reproduce mechanical outcomes.
- Fresh LLM prose is not required to reproduce identically.
- There is no per-action undo or cross-branch reward carryover.

#### Interface and accessibility

- The primary interaction is unrestricted free-text intent within the engine's supported capabilities.
- No suggested actions, recommended dialogue, action chips, or other strategy-steering controls appear.
- Linked exits, inventory, journal, save/load, and optional roll details remain available as factual controls.
- Enter submits; Shift+Enter inserts a line; all controls are keyboard reachable.
- Speaker identity cannot depend on color alone.
- WCAG 2.2 AA is the UX floor, including keyboard and screen-reader operation, browser-owned preferred text size, 200% zoom, 320 CSS px reflow, contrast, focus management, and reduced motion. No separate in-game text-size control is provided.
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

No hard frame-rate or resolution ceiling is currently specified because the prototype is text-driven. The accepted endurance evaluation uses a 100 MB memory-growth ceiling across the defined 60-wall-clock-minute, roughly 100-action workload; it is an evidence target, not a claim of current compliance.

### Complexity Drivers

#### High Complexity

1. Maintaining a hard boundary between probabilistic LLM judgment and authoritative deterministic state.
2. Committing multi-part actions exactly once despite retries, interruptions, malformed model output, or narration failure.
3. Modeling NPC knowledge separately from historical truth while making that knowledge causally affect behavior.
4. Advancing schedules and off-screen plans consistently on the same action-driven clock.
5. Saving and restoring every causal dependency needed for believable continuation and controlled replay.
6. Diagnosing whether a surprising outcome came from rules, world state, NPC knowledge, random resolution, or LLM judgment.
7. Preserving stable mechanics while allowing generated names, descriptions, rulings, and later progression content.
8. Adding P1–P9 rules without bypassing evidence gates or forcing later-stage state into P0 saves and interfaces.
9. Resolving interacting actions, timed effects, need thresholds, environment changes, clamping, and death reproducibly at the same game second.
10. Keeping property, possession, access, evidence, observation, suspicion, and belief causally separate.

#### Novel Elements

- A proposal–validate–commit–narrate pipeline for free-text RPG actions.
- Inspectable social transmission where observations become fallible beliefs through actual encounters.
- NPC memory that changes feasible planning rather than merely changing dialogue.
- Later history-shaped generated progression whose theme is judged by the LLM but whose effects remain mechanically bounded.
- One shared effect language used by resources, conditions, item treatments, crafting, spells, and combat without granting the LLM direct mechanical authority.
- Wants-driven NPC plans that execute through the same physical access, economy, time, and failure rules as player actions.

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
- **Scope expansion:** conditional P1–P9 systems distort an earlier stage before its evidence gate passes.
- **Effect-order drift:** identical same-second events produce different pools, conditions, or death outcomes.
- **Property omniscience:** ownership records leak an unseen loss or thief identity into NPC knowledge.
- **Economy fabrication:** NPC plans create wages, stock, tools, access, or food without recorded counterparties and transfers.
- **Stage contamination:** later-stage content or migrations activate in a save whose ruleset metadata does not allow them.
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
9. Stage gating and one-way dependencies across P1–P9
10. Resources, effects, access, needs, economy, crafting, quests, rewards, and combat reuse

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
| Physics | None | P0–P9 use authored text-space, deterministic rules, and no physics simulation |
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
| 10 | Stage gating | One-way dependency rules plus explicit save/ruleset migrations introduced with each authorized stage | N/A | Keeps P0 simple while allowing later stages to consume only proven lower-stage contracts |
| 11 | Resources and effects | Character-owned derived pools plus stable, source-bounded effect definitions and instances | N/A | Gives crafting, conditions, spells, and combat one deterministic mechanical language |
| 12 | Places and property | Physical access and possession resolve independently from ownership claims and character knowledge | N/A | Prevents remote use, automatic prohibition, and ownership-driven omniscience |
| 13 | Needs and livelihoods | Persisted need clocks create planning pressures; all NPC plans execute through ordinary actions | N/A | Makes off-screen survival and economy causal, finite, and replayable |
| 14 | Later-stage play | Crafting, spells, quests, rewards, and combat extend the common transaction, scheduler, item, and effect contracts | N/A | Avoids parallel rules engines and duplicate mutation paths |

Technology versions were verified on 2026-09-07 and revalidated on 2026-09-08. Lockfiles define the exact versions used by builds and tests.

### State Management

**Approach:** Authoritative transactional domain state with an append-only action log.

The backend owns all game truth. The browser submits commands and renders query results; it never computes or commits mechanical outcomes.

Commands and queries are separate application paths:

- Commands validate intent, expected world revision, permissions, prerequisites, resources, time, and invariants before mutation.
- A successful command atomically writes the new current state and an immutable action record.
- Queries return purpose-built views without mutating state.
- Every committed world mutation increments the branch's world revision and records a resulting state hash.
- A stale `expectedWorldRevision` produces a typed conflict response.
- A unique `requestId` makes mutating requests idempotent.

The append-only log supports audit, diagnostics, and replay, while snapshots remain the primary restoration mechanism. This is deliberately not full event sourcing.

P0 snapshots retain the existing schema and content versions. When the first later stage is authorized, the save format adds a `rulesetStage` and `rulesetVersion` through the normal typed migration path. Commands for unimplemented stages simply do not exist; P0 does not add a generic runtime feature-flag service. A newer application binary never invents later-stage state without executing the owning migration.

Historical facts, observations, received claims, and NPC beliefs are distinct domain records. Beliefs carry provenance, confidence, subject, source, acquisition time, and truth relationship when known. Changing a belief cannot rewrite historical truth.

### Data Persistence

**Save system:** SQLite-backed local saves with versioned snapshots and relational action records.

The Python standard-library `sqlite3` module sits behind a typed persistence adapter. Domain and application code do not import SQLite APIs.

Canonical JSON text stores versioned world-state documents. Relational records index lifecycle and audit concerns, including:

- `session_zero_drafts` (versioned categorized draft and draft revision)
- `campaign_origins` (immutable confirmed character and starting-array record)
- `active_branches`
- `save_slots`
- `action_records`
- `request_results`
- `operations`
- `operation_events`
- `schema_migrations`

Each branch and save records stable IDs, schema/content version, world revision, state hash, and timestamps; later-stage formats also record their ruleset stage/version. A save slot points to a complete immutable snapshot, so loading a slot restores every causal dependency rather than reconstructing an incomplete subset.

Database migrations are explicit, ordered SQL files. World-state schema changes use typed migration functions with fixtures for every supported historical version. Each authorized stage adds a typed ruleset migration that initializes only the state owned by that stage—for example, P1 resource pools—without enabling later content. Save/load, schema migration, ruleset migration, branch divergence, request deduplication, and crash recovery receive integration coverage against real SQLite databases.

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

Scheduled events are typed, versioned, and persisted with stable IDs. The scheduler first orders work by due game second, event priority, and insertion sequence. Within one game second, the domain reducer applies the GDD 0.8 phase order:

1. Completed actions and continuous intervals in recorded commit order
2. Scheduled effect ticks and unmet need thresholds in stable creation order
3. Effect expirations and environmental transitions
4. Recalculation of base/effective values, current-pool clamping, and terminal states such as death

The phase order is data-independent and cannot be changed by narration or an LLM proposal. A meal or completed adequate sleep at its exact threshold prevents the corresponding need stack; treatment at a Bleeding tick removes the linked instance before the tick; a final tick resolves before ordinary expiry; and protection ending exactly when an adequate-sleep interval completes remains valid for that interval.

After an action advances time, the engine processes due events within a bounded work budget. Events requiring player attention interrupt a long wait at the event's actual time. Loop detection and processing limits prevent one action from creating an unbounded event cascade.

NPC simulation is hybrid:

- Routine schedules and explicit plans execute deterministically.
- The LLM is consulted only when a consequential situation requires interpretation or replanning.
- Every proposed plan is checked against NPC knowledge, resources, relationships, obligations, and available time.
- Selected plans become ordinary typed commands; they acquire locations and access, reserve inputs, pay time and resource costs, and commit through the same world transaction as player actions.
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

Every mutation includes `requestId` and the revision of its target: `expectedWorldRevision` for an existing branch, `expectedDraftRevision` for Session 0, or `expectedSlotRevision` for a save-slot write. Creating a draft has no prior revision; its request identity deduplicates creation. The server returns an authoritative view and new revision or a typed conflict. The browser never merges competing authoritative game states.

TanStack Query owns server-derived state, cache invalidation, request status, and recovery. Successful mutations replace or invalidate the applicable authoritative view. Mutation retries are disabled unless explicitly driven through the idempotent operation contract; safe reads may retry.

Local React state is limited to presentation concerns such as:

- Draft input
- Open panels
- Selection
- Inline roll-detail selection
- Focus state

The application does not store or override preferred text size; browser font and zoom choices are authoritative. Browser storage may persist other non-authoritative presentation preferences, but never game state. React Context remains narrow and is not used as a second state store.

### Request Lifecycle and Transport

Rowan work and campaign confirmation share persisted operation resources. Operations identify a typed subject (`session_zero_draft` or `branch`); a branch is not required before confirmation. Mutating actions use these resources:

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
- Atomic commit writes the subject state, audit record, request result, and committed operation state together, eliminating an ambiguous crash window. For draft commands the subject is a Session 0 draft; confirmation also creates the campaign origin and branch in that transaction.

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
│           ├── title/
│           ├── session-zero/
│           ├── character/
│           ├── game-session/
│           ├── journal/
│           ├── inventory/
│           ├── saves/
│           └── diagnostics/
├── backend/
│   ├── src/dmud/
│   │   ├── session_zero/
│   │   ├── characters/
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
- P1–P9 implementation-specific endpoints, UI composition, and code decomposition beyond the contracts in this document; introduce them only when their owning stage is authorized

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
browser preferences              Non-authoritative view choices only; never text sizing or game state
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
│       │   ├── title/
│       │   ├── session-zero/
│       │   ├── character/
│       │   ├── game-session/
│       │   ├── operation-progress/
│       │   ├── journal/
│       │   ├── inventory/
│       │   ├── saves/
│       │   ├── roll-details/
│       │   └── diagnostics/
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
│   │   ├── session_zero/
│   │   ├── characters/
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
| Campaign draft and confirmation | `backend/src/dmud/session_zero/` | Draft commands/queries, reflection, validation, atomic campaign creation |
| Character identity and allocation | `backend/src/dmud/characters/` | Immutable origin, character views, separate earned-point allocation commands |
| Title and campaign entry | `frontend/src/features/title/` | Save-index states and New Game/Continue routing |
| Session 0 interface | `frontend/src/features/session-zero/` | Conversation, categorized review, draft recovery, explicit confirmation |
| Character interface | `frontend/src/features/character/` | Starting assignment, current stats, earned-point preview and confirmation |
| Free-text action lifecycle | `backend/src/dmud/actions/` | Interpret, validate, resolve, commit, and narrate |
| Durable request processing | `backend/src/dmud/operations/` | Operation state, worker execution, SSE, recovery, cancellation |
| Authoritative world state | `backend/src/dmud/world/` | World model, change sets, invariants, query views |
| Facts and beliefs | `backend/src/dmud/knowledge/` | Facts, observations, claims, provenance, transmission |
| NPC agency | `backend/src/dmud/npc_planning/` | Needs, obligations, routines, feasible plans, replanning |
| Clock and scheduled events | `backend/src/dmud/simulation_time/` | Campaign clock, ordering, bounded event processing |
| Checks and P0 progression | `backend/src/dmud/checks/` | Difficulty, seeded rolls, XP, levels, bonuses |
| Inventory and transactions | `backend/src/dmud/inventory/` | Possession, ownership claims, identity/quantity, money, gifts, purchases |
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
| API contract | `contracts/openapi.json` and `frontend/src/api/generated/` | Exported OpenAPI and generated browser client |
| Brackenford content | `content/worlds/brackenford/` | Authored locations, NPCs, items, conflict, check |
| Backend integration coverage | `backend/tests/integration/` | Real FastAPI, SQLite, save, transaction, and worker behavior |
| Browser journeys | `tests/e2e/` | Playwright against the real SPA and API |
| LLM test contracts | `backend/tests/fixtures/llm/` | Deterministic substitutes at the external boundary |

Conditional systems receive dedicated slices only after their evidence gates pass:

- P1: `effects/` plus resource-pool behavior in `characters/`
- P2: `places/` plus item identity and transfer behavior in `inventory/`
- P3: `needs/` and `crafting/food/`
- P4: livelihood behavior in `npc_planning/` using existing actions, inventory, places, and needs contracts
- P5: `community_viability/` and `crafting/alchemy/`
- P6: `spells/` and `recognition/`
- P7: `quests/daily/`
- P8: `quests/hidden_objectives/`
- P9: `combat/`

Each slice is created only when its stage is authorized. Later slices depend on stable lower-stage domain contracts; no lower stage imports a later slice, and no speculative folder or abstraction is added to P0.

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

12. **Scope gates:** Conditional P1–P9 directories and abstractions are introduced only when the owning stage is authorized after the preceding evidence gate.

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

## Session 0 and P0 UX Contracts

### Source Authority and Scope

This revision uses [GDD 0.8](planning-artifacts/gdds/gdd-dmud-2026-09-07/gdd.md), its companion E1–E11 design epics, the [current implementation epics](planning-artifacts/epics.md), and the final [DESIGN.md](planning-artifacts/ux-designs/ux-dmud-2026-09-08/DESIGN.md) and [EXPERIENCE.md](planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md). GDD 0.8 preserves the approved P0 entry and character rules, resolves the P1–P9 staged design, isolates the 10,000-gold P0 fixture branches, and makes browser-owned text sizing authoritative. “James” is an example persona; all normative views use the player-selected name. The UX spines govern over the illustrative mockup. Companion design epics and current implementation epics are separate namespaces.

The existing React/FastAPI/SQLite decisions remain in force. This revision does not revalidate historical dependency pins or claim that executable accessibility or integration checks have passed.

### ADR-006: Durable Session 0 Before World Creation

`session_zero/` owns a versioned `SessionZeroDraft`: ID, draft revision, lifecycle, exact submitted answers, categorized statements with source-answer IDs, starting assignments, content/schema versions, reflection revision and digest, and active operation reference. Required answers cover name, origin, cares, hates, cool ideas, and campaign hopes; an explicit “none” is a valid answer where applicable. Backend validation distinguishes an unanswered field from that answer.

Statements have distinct types: `character_fact`, `campaign_premise`, `player_preference`, and `story_hope`. Preferences and hopes never enter the historical fact ledger or guarantee an outcome. Proposed facts and premises remain unconfirmed draft material until review. Content validation rejects contradictions with the authored P0 fixture and asks for neutral clarification; Rowan cannot rewrite geography, grant resources or rewards, or predetermine an NPC decision. Character background is not automatically knowledge of NPC secrets.

Draft lifecycle is `collecting` → `ready_for_review` → `confirmed`. Readiness requires complete answers, a valid full stat assignment, and a reflection matching the current draft revision. Any edit invalidates the previous reflection and returns to collecting until a new reflection is ready. Provider pending/failure belongs to the operation lifecycle, not additional contradictory draft booleans. Reviewing and correcting a draft creates no campaign events or fictional time.

Commands are `CreateSessionZeroDraft`, `SubmitSessionZeroAnswer`, `AssignStartingAttributes`, `RequestCharacterReflection`, and `ConfirmCampaign`; queries are `GetSessionZeroDraft` and `GetCharacterReview`. Thin routes and strict Pydantic ingress feed typed application commands. Query projections and SQLite write adapters remain separate files within the slice. The existing operation worker, gateway, SSE, status polling, and request-result store serve Session 0 from the first story; no disposable conversation subsystem is introduced.

Submitted answers and valid assignment updates persist in SQLite. The browser retains unsent input and invalid assignment previews while showing field errors; it never presents unacknowledged input as saved. Refresh retrieves the draft and existing operation. A validated local pointer may identify the last draft, but it contains no authoritative draft data. New Game creates a distinct draft without deleting saves or a prior draft; a known unfinished draft can resume directly without making Continue mean “resume draft.”

Starting attributes are exactly Body, Agility, Constitution, Mind, and Presence. A complete mapping uses the multiset `8, 10, 12, 13, 14` exactly once. Partial mappings may persist during assignment if keys and values are allowed and assigned values are unique; only a complete mapping is reviewable. Duplicate, unknown, or out-of-array assignments return field errors without changing the last valid persisted mapping. Concurrent edits require the current draft revision.

### ADR-007: Atomic Campaign Confirmation and Character Origin

Confirmation submits the reviewed draft revision and reflection digest plus a request ID. The server rechecks completeness, assignment validity, content compatibility, and reflection freshness inside the transaction. It atomically creates the immutable character origin, categorized confirmed information, complete initial branch, initial world revision and state hash, operation evidence and request result, and the draft-to-campaign link. A uniqueness constraint on the source draft prevents two campaigns even if concurrent confirmations use different request IDs. Repeated confirmation returns the existing campaign; a stale review before confirmation returns a conflict and requires fresh review.

The initial location is Market Square and the clock is 28,800 seconds from day 1 at 00:00. Session 0 consumes zero seconds. Initial world content stays within three locations, four NPCs, and the approved conflict. Opening narration is generated afterward from committed player-perceptible facts with separately labeled personalization context. It may make the situation relevant without promising the player's hopes. Failure before commit leaves the draft editable; failure after commit preserves the campaign and retries only narration.

The controlled P0 starting state contains one prepared, known-value pouch with exactly 10,000 gold and no other player gold. It is fixture funding, not an ordinary campaign balance or later-stage progression resource. The 1-gold purchase, full-pouch gift, and no-gift comparisons each load an isolated copy of the same captured state; outcomes never merge. The separate 100-loose-coin handling fixture is not player wealth. Fixture identity and branch origin are recorded so conservation checks cannot accidentally combine these ledgers.

`characters/` owns immutable starting scores, current scores, and allocated/unspent attribute points. `checks/` continues to own check resolution and XP/level progression; character allocation consumes its awarded point balance through the common atomic commit boundary. A pure allocation validator checks positive integer increases and available points; the confirmed allocation command is idempotent, revision-checked, zero-time, and cannot rewrite the starting record. A local preview never changes authoritative scores. Save snapshots include the confirmed origin, current scores, both XP tracks, levels, skill bonuses, allocations, and unspent balance; loading restores these branch-local records together.

G03 and G18 are approved rules, not unresolved tuning: modifier `floor((score - 10) / 2)`, natural 1 failure/natural 20 success, and otherwise the documented d20 threshold. Successful meaningful checks award `floor(100 * (0.95 - p) / 0.90)` XP to player and relevant skill, with `p` obtained by counting successful faces; failures award zero. Tracks start at level 1/0 XP, consume `100 * current level` per level, carry excess, and grant one attribute point or one skill bonus per applicable level. No design cap is added. Presence 14 and Persuasion +1 are controlled-test settings, not mandatory character assignments.

G04 fixture rules live in validated authored rule data: speeds 1.4/2.8/5.6/0.5 m/s, route lengths 7/140 m, travel rounded up per segment, completed speech `15 * ceil(spokenWords / 30)` seconds, and the prepared-pouch transfer 5 seconds. Persist the validated speech segments used for duration before commitment; post-commit prose cannot alter those segments or charge additional time. Only completed segments count when interrupted. Morning means next 06:00; the 60-second silence return applies to face-to-face waiting, not uneventful overnight waits.

### Transport and Query-State Contracts

These resource routes extend the existing generated OpenAPI contract; they do not bypass strict runtime validation. Mutating responses return authoritative resource revisions or a `202` operation reference. Operation results include subject identity, commit boundary (`none`, `draft`, or `world`), committed revision when present, and a safe recovery capability. New payload under an existing request ID is a conflict, never a second command.

| Resource / command | Transport | Observable contract |
| --- | --- | --- |
| Save index | `GET /api/save-slots` | Three numbered slots, each explicitly empty, occupied, or unavailable; occupied metadata contains campaign identity, known place, game second, saved-at time, compatibility, and slot revision. Reading does not load a branch. |
| Create draft | `POST /api/session-zero-drafts` | Idempotent creation; first question asks the name. No branch required. |
| Resume draft / review | `GET /api/session-zero-drafts/{draftId}` and `/review` | Saved answers, categorized review, assignment completeness, draft revision, active operation; unknown draft is a typed 404. |
| Answers / reflection | `POST /api/session-zero-drafts/{draftId}/answers` and `/reflection` | Durable Rowan operation under the draft subject; repeat submission never duplicates an answer. |
| Starting assignment | `PUT /api/session-zero-drafts/{draftId}/attributes` | Revision-checked mapping update; typed inline errors preserve prior valid state. |
| Confirm campaign | `POST /api/session-zero-drafts/{draftId}/confirmation` | Exact reviewed revision/digest, explicit player confirmation, recoverable operation and resulting branch ID. |
| Character view / allocation | `GET /api/branches/{branchId}/character`; `POST .../character/allocations` | Current and immutable starting values are separate; allocation returns persisted state or field/conflict errors. |
| Journal / inventory | `GET /api/branches/{branchId}/journal` and `/inventory` | Validated empty arrays mean known-empty, never failed reads. Views include branch ID and world revision. |
| Result details | `GET /api/branches/{branchId}/results/{resultId}` | Discriminated rolled/no-roll evidence; missing (404) or corrupt/unreadable evidence is explicit and never reconstructed by the LLM. |
| Save / load | `PUT /api/save-slots/{slotId}`; `POST /api/save-slots/{slotId}/loads` | Save uses expected slot and branch revisions; load uses the selected slot revision and request ID. Failed writes preserve the previous slot; load activates its recovered branch only after successful validation/commit. |

Title renders New Game and Continue immediately while the save index loads. Continue is unavailable with an explanation until a compatible occupied slot is known; index failure offers retry and leaves New Game available. Continue opens save selection, never silently chooses a slot. Overwrite confirmation names the existing save and uses its slot revision to prevent overwriting a changed selection.

All views distinguish cold/loading, successful empty or populated data, and errors. Character views additionally distinguish creation editing, no/unspent points, local allocation preview, invalid preview, confirmation pending, and persisted allocation. Failed reads may retain explicitly stale prior content but cannot enable mutations from an unknown revision. Schema failures surface a safe data error, not an empty state. RFC 9457 problems add documented field errors and recovery metadata; raw provider text, SQL, and hidden state never appear in failure details.

Query keys include draft or branch identity and result identity where applicable. A load replaces the active branch only after success and invalidates prior branch views; late SSE events and query responses for the previous subject cannot append to the newly active transcript. Operation status remains recoverable through the existing ID. Save/load cannot race an unresolved branch mutation: recover or settle it first and return a typed busy conflict while settlement is unknown.

### Notebook Presentation and Information Boundaries

The one composer routes validated interpretation to a known-information Rowan question, in-world speech/action, or neutral clarification. Known-information questions and clarification persist operation/transcript evidence without advancing world time or fabricating events. Before consequential commitment, show knowable interpretation, stakes, and costs; materially changed intent or rare-resource spending requires clarification. No modes, prefixes, unsolicited suggestions, dialogue chips, or generated tactical replies are added. Session 0 creative help is offered only when explicitly requested.

`game-session/` renders labeled, selectable transcript entries and the exact submitted intention. `operation-progress/` maps accepted/interpreting/validating/resolving/narrating to truthful pending; needs-clarification to clarification; complete to resolved; and failure/interruption to explicit recovery. Committed-but-narrating states explicitly disclose that world or draft state is already saved. Rejected and unsupported intentions receive factual explanations without time cost. Decorative waiting copy never claims measured progress and never re-announces every rotation.

Backend player-view queries enforce knowledge limits before serialization and before Rowan recall context is built. Transcript, journal, inventory, character sheet, result details, and save labels cannot leak concealed actors, private NPC plans, or unknown beliefs. Diagnostics stay separately capability-gated. The sole persistent character card belongs to the player; there is no nearby roster or privileged Rowan portrait. Inventory, character, save selection, and result-specific mechanics use one shared overlay shell. There is no global roll-details tab. Routine no-roll results remain inspectable. P6–P8 titles, achievements, System notices, quests, and award notices remain absent from P0 surfaces.

### Accessibility and Visual Implementation Gates

`frontend/src/app/styles.css` owns the DESIGN token translation, including paper/ink/forest colors, system-safe Georgia story type at the specified 18px baseline, interface type, spacing, focus color, and readable 55–75-character lines. Token use must satisfy rendered contrast; decorative rule colors cannot become essential low-contrast boundaries. No Comic Sans, fixed 1040px minimum width, mandatory portrait pipeline, or accessibility-settings screen is introduced.

`ui/Dialog.tsx` owns accessible naming, modal role, contained focus, Escape/close, and return to the invoker (or a stable logical target if it no longer exists). The app permits one reference overlay at a time, including overwrite confirmation within that shell. `StatusMessage` owns polite, deduplicated semantic state announcements without focus theft. Landmarks, headings, speaker/type labels, labels for all inputs, visible unobscured focus, keyboard activation, and hover parity apply to generated content too.

Acceptance checks cover 200% browser zoom and 320 CSS px reflow with no lost controls or horizontal page scrolling; overlays remain viewport-bounded and scroll internally. Reduced-motion preference replaces looping movement with a static mark. No timed reading, auto-dismissed narrative, or interaction timeout is introduced. Normal text/labels require 4.5:1, large text 3:1, essential boundaries/focus 3:1, and primary ink on paper-light the DESIGN target of 7:1. Automated checks supplement manual keyboard, real browser zoom, and screen-reader verification; they do not alone establish WCAG conformance.

### Requirement-to-Verification Map

These are implementation acceptance gates, not test results from this documentation pass. Use real FastAPI/SQLite and browser integration journeys; deterministic fixtures replace only the external LLM boundary.

| Source | Architecture owner / required evidence |
| --- | --- |
| GDD P0 entry; Epic 1, Stories 1.1–1.2; UX Title/Session 0 | Title cold/empty/error/retry; New Game despite failed save index; persisted answers and draft refresh; reused operations without duplicate entries. |
| G03; Stories 1.3–1.4 | Partial/duplicate/missing stat inputs; stale review invalidation; simultaneous confirmation with same and different request IDs; exactly one campaign at second 28,800; pre/post-commit narration failure. |
| G18; Story 3.5; character-sheet UX | XP boundary and multi-level progression; no failure XP; allocation preview/cancel/overspend; idempotent allocation; starting record unchanged across save/load. |
| Epic 2; Notebook and request UX | Zero-time known recall and clarification; synonyms; explicit commit boundary; reconnect and late prior-branch responses; no recommended actions or hidden-state leaks. |
| G04; Stories 3.1–3.2 | Fixture travel/speech/transfer durations, interrupted completed segments, real-event waits, morning and silence rules; no duplicate time. |
| Epic 4; UX information boundaries | Real causal contact scenarios and negative player projections for concealed NPCs, private plans, and unsupported knowledge. |
| Epic 5; save and result-detail UX | Three-slot index, overwrite revision conflict, failed save/load preservation, branch isolation, complete character restore, rolled/no-roll/missing/corrupt details. |
| DESIGN + EXPERIENCE accessibility floor | Keyboard and screen-reader journeys across all eight surfaces; focus containment/return, state announcements, contrast, zoom, reflow, reduced motion, generated-content semantics. |

Historical implementation mapping: the earlier five-epic P0 plan mapped title/session-zero, actions, world/checks, knowledge/NPC planning, and saves/diagnostics. The current implementation-epics artifact is being revised against GDD 0.8 and must establish its own final mapping before readiness review; this architecture does not treat its legacy stories as approved.

## GDD 0.8 Staged Systems Contracts

### Stage Authority and Dependency Direction

The stage sequence is an architectural boundary, not just a roadmap label or player-progression system. It governs implementation and save compatibility: each authorized release contains one highest stage and all proven stages beneath it. Once later stages exist, content packages declare a minimum ruleset stage; loading incompatible later-stage content into an earlier save is a validation error rather than an implicit migration.

| Stage | Owning capability | Permitted dependency direction |
| --- | --- | --- |
| P0 | Causal world, Session 0, checks, time, knowledge, saves | Foundation only |
| P1 | Character resources and shared effects | P0 transactions, time, characters, saves |
| P2 | Places, access, ownership, and evidence | P0 knowledge/inventory plus P1 costs/effects |
| P3 | Needs, food, and shelter | P1 resources/effects plus P2 places/access |
| P4 | Autonomous livelihoods | P0 planning/time plus P2 access and P3 needs/crafting |
| P5 | Community viability and alchemy | P1 effects, P3 crafting/needs, P4 economy/planning |
| P6 | Spells and recognition | P1 resources/effects plus P0 progression/history |
| P7 | Daily quests and gacha rewards | P0 progression/time plus proven P3–P6 action capabilities |
| P8 | Hidden quest bonuses | P7 quest lifecycle and bounded rewards |
| P9 | Bounded combat | P1 resources/effects, P2 positioning/access, P6 spells, P0 checks/time |

Cross-stage calls use typed domain contracts and immutable values. A later slice may invoke a lower-stage command or pure rule; it may not reach into another slice's persistence adapter or mutate its models directly. Shared primitives move to `foundation/` only after at least two owning slices require the same stable concept.

### ADR-008: Versioned Ruleset Migration and Stage Boundaries

P0 continues to use the existing schema/content versions and does not add a general-purpose stage registry. When P1 is authorized, its save migration adds:

- `rulesetStage`, from `p1` through the highest implemented stage (with migrated P0 saves explicitly recorded as the source)
- `rulesetVersion`
- enabled content-package IDs and versions
- the world-state schema version already required by save migration

This is release/save compatibility metadata, not a player reward, campaign level, remote feature flag, or reason to keep multiple rulesets live indefinitely. The composition root registers only modules implemented by the current release. Authored-content loading rejects packages above that release's ruleset stage, and save loading rejects a newer unsupported ruleset before mutation.

Stage adoption is a typed, idempotent save migration executed by the release that first implements that stage—not a gameplay command. It validates the source ruleset, initializes only the new stage's state, records the destination ruleset, and commits atomically. A failed migration leaves the original save readable and unchanged. Skipping an intermediate stage is invalid.

Every stage migration has a real-SQLite fixture from the immediately preceding stage plus save/load and rollback-on-failure coverage. P1 initializes all existing characters' current Health, Mana, and Stamina to their derived maxima. Later migrations initialize only their own fixtures and records; they do not retroactively fabricate elapsed needs, wages, observations, quest completions, or combat outcomes.

### ADR-009: Character Resources and Shared Effect Kernel

`characters/` owns raw attributes and the three current resource pools. Pure derivation functions calculate Base Maximum Health (`Body × Constitution`), Mana (`Body × Mind`), and Stamina (`Agility × Constitution`). A permanent attribute increase adds the positive maximum difference to the applicable current pool; a decrease clamps to the new Effective Maximum. This preserves spent points and damage as absolute deficits. All current values are bounded from zero through Effective Maximum, and death occurs when Health reaches zero.

`effects/` owns two immutable concepts:

- `EffectDefinition`: stable ID, schema version, source category, polarity, tier, eligible target and one primary mechanical shape, magnitude, duration/use limit or terminating condition, duplicate policy, removal contract, and presentation metadata.
- `EffectInstance`: stable ID, definition ID/version, source entity/event, target, creation sequence, start/expiry data, remaining uses or ticks, stack linkage, and knowledge visibility.

The LLM may propose a definition only within a validated source budget fixed before any uncertain check. Strict Pydantic contracts reject unsupported targets, missing termination, or out-of-budget magnitude. The engine either accepts a complete immutable definition or rejects/reduces it before commitment; narration cannot alter it later. Authored multi-component effects are separate validated content and do not weaken the one-primary-shape rule for generated effects.

Duplicate behavior is definition-owned: `stack` creates independent instances, `refresh` keeps magnitude and resets duration/uses, and `replace` keeps the stronger eligible application. The modifier reducer sums percentages, applies them to the base, rounds once, then adds flat modifiers. `Starved` and `Exhausted` remain explicit multiplicative exceptions. Removal is category- and cause-aware; numerically cancelling effects remain separate instances and expire independently.

Effect ticks, expiry, source removal, resource recalculation, clamping, and death use the shared scheduler phase order. No slice may calculate these in an HTTP handler, UI component, provider prompt, or private alternative clock. Query projections expose full mechanics only when known to the viewing character; unknown effects expose observed symptoms rather than hidden definitions or timers.

### ADR-010: Physical Places, Access, Property, and Evidence

`places/` owns locations, resource placement, entrances, locks, door state, capacity, and environmental protection. `inventory/` owns possession and item movement plus a separate legitimate-ownership claim. The pure access decision consumes actor location, target location, entrance state, permission, compatible keys, required tools, capacity, proposed method, and payable time/Stamina costs. Ownership may grant permission but neither teleports a resource nor makes unauthorized physical use impossible.

Items use the identity model appropriate to their rules:

- Distinctive items retain an item ID, current possessor, ownership claim, provenance, and observable identifying marks.
- Fungible goods retain type, quantity, location/possessor, and causal transfer events; after mixing, they do not expose an instance identity that proves theft.
- Crafted or perishable batches retain a batch ID, recipe/version, quantity or servings, completion time, and one expiration timestamp.

Lockpicking, forced entry, theft, transfer, bed sharing, and ordinary use are typed world commands. Each attempt reserves and consumes its declared tools, time, and Stamina exactly once at commitment. Repeated attempts are new requests and remain legal only if the actor can still pay every cost. Door damage, noise, witnesses, possession changes, and evidence are explicit committed outcomes.

Property mutation and knowledge mutation are separate. An unwitnessed removal changes possession and event history but creates no owner observation. Later inspection may produce an absence observation; comparison with remembered state may produce a missing-item belief; suspicion or accusation requires further evidence. The knowledge slice alone converts perceived events or received claims into observations and beliefs. Authoritative ownership data is never copied directly into an NPC prompt or player projection.

### ADR-011: Needs, Food, Shelter, and Livelihood Execution

`needs/` owns persisted last-meal and last-adequate-sleep times, next thresholds, stack counts, and the causal application/removal of `Starved` and `Exhausted`. `Exposed` belongs to a sleeping place or household environment, not a character effect. Need thresholds are scheduled domain events and are recalculated after a qualifying meal or completed adequate sleep. Crossing a threshold applies one stack; removing a stack restores available maximum but does not heal or refill current resources except where the GDD explicitly grants recovery.

Adequate sleep is a persisted continuous interval requiring a usable bed and valid protection for its full eight hours. Interruption, leaving, loss of capacity, or protection loss before completion makes it inadequate. Crafting and work likewise distinguish occupied action time from scheduled unoccupied processing. Long-running intervals store start time, planned completion, reserved inputs, actor participation, and interruption policy so save/load and event interruption remain deterministic.

`crafting/food/` owns versioned recipes and batch creation. A recipe declares inputs, tools/facilities, occupied and unoccupied time, Stamina, yield, servings, shelf life, and optional effects. Completion consumes reserved inputs and creates a fresh batch expiration timestamp from completion time; ingredient age does not alter it in the current scope. Eating an expired serving still satisfies hunger, then resolves the recorded spoilage risk and any Constitution check through the ordinary check/XP path.

NPC needs create planning pressure; they never mutate inventory or resources directly. `npc_planning/` selects a feasible goal using need priority, personality, taste, obligations, relationships, knowledge, risk, time, and cost. It compiles the chosen plan into ordinary travel, access, work, purchase, craft, eat, and sleep commands. Employers, customers, shops, and actors have finite ledgers. Wages and purchases require counterparties and balanced transfers. Failure records its cause and triggers replanning rather than invented resources.

Observed and off-screen execution use the same command handlers, scheduler, random source, and transaction boundary. Presentation differs, but mechanical state does not. The simulation advances no NPC plan while the game clock is paused.

### ADR-012: Crafting, Spells, Quests, and Recognition Use Stable Definitions

Later-stage authored and accepted generated mechanics share a definition/instance convention:

- Definitions have stable IDs, schema/content versions, immutable mechanics, eligibility rules, and presentation seeds or accepted presentation.
- Instances reference an exact definition version and record owner, source event, acquisition time, current state, and consumed/remaining uses.
- Mechanical resolution never reparses player-facing prose.
- Saved instances continue using their recorded definition version after content updates; migrations are explicit.

P5 alchemy extends `crafting/` with authored recipes, substitutions, progress tracks, and item-applied effects. Inputs, failure consumption, work time, stock, prices, and demand commit through existing inventory/economy transactions. Fermentation or other unattended work is a scheduled crafting job, not a background task.

P6 `spells/` owns affinity packages, affinity-owned slots, spell definitions, Mana costs, and replacement/evolution rules. Generated names and manifestations may use Session 0 and committed history, but mechanics come from the accepted definition. `recognition/` keeps titles, achievement triggers, generated presentation, and fixed rewards distinct so one cannot silently substitute for another.

P7–P8 `quests/` owns a versioned quest instance with issuer/voice, visible success contract, lifecycle, evaluator, reward authority, refresh/expiry data, and idempotent completion claim. Daily refresh is a scheduled event at 06:00. Hidden bonuses are private child records containing one condition contract, evaluator version, and one bounded reward; they never enter player projections or ordinary narration. LLM judgment returns a strict evaluation proposal, while deterministic rules validate evidence, reward budget, and prior claim before one atomic completion commit.

Reward claims use a unique `(questInstanceId, rewardKind)` identity. Completion, player/skill XP, item draw, hidden-bonus reward, inventory change, and notification record commit atomically or not at all. The gacha draw records pool version, eligible entries, random seed/result, and awarded item; retries return the prior outcome.

### ADR-013: Combat Reuses the World Transaction Engine

P9 `combat/` is an encounter coordinator, not a second game engine. It owns encounter membership, six-second round/turn state, initiative order, relative position in the authored encounter space, legal exits, and surrender state. It delegates checks, damage, resource costs, effects, items, movement, spells, death, rewards, time advancement, and persistence to the already proven lower-stage slices.

Each combat action is a normal revision-checked, idempotent world command. Validation fixes targets, costs, movement, difficulty, and declared consequences before the roll. Commit advances the shared clock, applies the action, processes same-second effects through the common phase order, and records the next encounter state. Victory, escape, robber surrender, and player surrender are explicit terminal outcomes; reaching zero Health applies immediate death before narration.

Mid-combat saves contain the complete encounter coordinator state plus every ordinary world dependency. Loading cannot reroll initiative, attacks, damage, rewards, or effect ticks. XP and loot claims have stable encounter/outcome identities and commit at most once. The text projection exposes positions, current/effective maxima, legal known targets, committed costs, damage, and exits without adding a tactical-map subsystem.

### Staged Query and Presentation Contracts

Stage-specific screens are knowledge-filtered projections over authoritative state, not client-side calculators:

- P1 adds character resource/effect inspection, including known sources, stacks, impacts, and removal conditions.
- P2 adds known entrance state, access facts, item location/possession, permissions, and observed evidence without revealing hidden ownership or beliefs.
- P3 adds last-meal/sleep information and exact thresholds only when knowable, food batch state, and active rest/crafting intervals.
- P4–P6 add known plans/commitments, crafting progress, spells, affinity slots, and recognition records.
- P7–P8 add visible quest success conditions and rewards while excluding hidden bonus conditions and evaluator reasoning.
- P9 adds the bounded combat projection described above.

The browser validates every new projection with generated Zod schemas. Server state remains in TanStack Query; unsent form input, open panels, and selection remain local. No stage introduces an in-game text-size control. New factual controls must not become suggested actions, optimal-strategy hints, or hidden-state leaks.

### Persistence and Verification Matrix

| Stage | Additional snapshot state | Architectural evidence gate |
| --- | --- | --- |
| P0 | Fixture origin and isolated branch ledger for purchase/gift/no-gift | Exact 10,000-gold starting pouch, no other gold, no cross-branch merge, deterministic replay |
| P1 | Pools, definitions/instances, ticks, uses, source/removal data | Formula/growth/clamp tests; every tier/shape boundary; stacking; same-second order; 0-Stamina; save/load |
| P2 | Places, doors, locks, keys, permissions, capacity, possession, ownership claims, evidence | Permitted/forced/locked access; finite-cost retries; witnessed/unwitnessed theft; no property omniscience |
| P3 | Need clocks/stacks, sleep intervals, food batches, crafting jobs, expiry | Threshold boundaries; adequate/interrupted sleep; recipes; spoilage probability/check/XP; save/load |
| P4 | Wants, plans, work commitments, finite counterparty ledgers | Ivo/Tessa success and each failure/replan branch; observed/off-screen equivalence; conservation |
| P5 | Household streaks/protection plus alchemy jobs/tracks/items | Causal lived stability, isolated household reset, recipe/failure/effect/demand coverage |
| P6 | Affinities, slots, spells, evolution, titles, achievements | Stable mechanics under generated presentation; Mana/slot ownership; distinct reward identities |
| P7 | Quest instances, refresh/expiry, pool versions, reward claims | Three categories, visible contracts, one-time XP/draw, distinct System voice |
| P8 | Private condition/evaluation records and bounded bonus claims | Trigger/non-trigger coverage, no disclosure, no routine over-award, at-most-one reward |
| P9 | Encounter/round/initiative/position/outcome plus reward claim | Four exits, six-second rounds, shared costs/effects/death, mid-combat save/load, no duplicate rewards |

These gates are required test and play evidence, not claims that implementation exists. Each stage uses real FastAPI and isolated real SQLite storage; only the external LLM provider may be replaced by deterministic contract fixtures.

## Architecture Validation

### Validation Summary

The assessments below are document-level architecture checks, not executable test results. GDD system and design-epic coverage include this revision; implementation-epic alignment is pending completion of the separate planning revision. Technology compatibility remains the historical September 8 assessment.

| Check | Result | Notes |
| --- | --- | --- |
| Decision Compatibility | PASS | SPA/API, persistence, operations, simulation, and LLM boundaries are compatible |
| GDD Coverage | PASS | All 21 P0 and conditional system families have documented architectural support |
| Pattern Completeness | PASS | Seven original patterns plus staged-system contracts cover authority, knowledge, time, effects, access, needs, content, rewards, and combat |
| Design Epic Mapping | PASS | GDD companion E1–E11 map to P0 and conditional P1–P9 boundaries |
| Implementation Epic Mapping | PENDING | The separate P0 implementation-epics artifact is mid-revision and must be rechecked against Architecture 1.2 |
| Document Completeness | PASS | Mandatory sections, Session 0/UX contracts, and GDD 0.8 staged contracts are documented; executable verification is pending |
| Technology Compatibility | NOT REVALIDATED | The documented stack remains coherent, but dependency currency is still the historical 2026-09-08 check and must be refreshed when scaffolding |
| Security Boundary | PASS | Loopback-only P0, backend-only secrets, strict validation, and safe errors are defined |

### Coverage Report

**Systems Covered:** 21/21
**P0 Systems Covered:** 12/12
**Conditional Systems Mapped:** 9/9
**GDD Design Epics Mapped:** 11/11
**Current Implementation Epics:** revision pending
**Patterns Defined:** 7 original plus 6 staged-system contracts
**Decision Summary Entries:** 14; **ADRs:** 13
**Mandatory Sections Present:** 7/7

### Document Quality

- **Architecture completeness:** Complete for GDD 0.8 at the decision and boundary level
- **Version specificity:** Explicit but historically verified; refresh before scaffolding
- **Pattern clarity:** Clear, with deterministic ownership and cross-stage dependency rules
- **AI agent readiness:** Ready for implementation-epic revision; implementation itself remains gated by epic alignment and dependency verification

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
14. Added one-way stage dependencies and explicit idempotent ruleset migrations without introducing a speculative P0 capability framework.
15. Defined derived Health, Mana, and Stamina ownership plus the shared effect definition/instance kernel.
16. Defined deterministic same-second phase ordering across actions, ticks, thresholds, expiry, clamping, and death.
17. Separated physical access, possession, ownership claims, evidence, observations, and beliefs.
18. Defined need clocks, food batches, continuous sleep/work/crafting intervals, and causal off-screen livelihood execution.
19. Reused stable definition/instance and atomic reward patterns for alchemy, spells, recognition, daily quests, and hidden bonuses.
20. Defined combat as an encounter coordinator over existing world transactions rather than a separate rules engine.
21. Reconciled the 10,000-gold P0 fixture, isolated branch ledgers, browser-owned text sizing, and the P1–P9 evidence sequence.

### Readiness Boundary

GDD 0.8 is the approved staged-design baseline. P0 remains the only authorized initial implementation; P1–P9 are architecturally mapped but remain conditional on sequential evidence gates. Architecture 1.2 supplies the missing later-stage contracts and preserves the Session 0/P0 UX decisions from 1.1. The 2026-09-12 and 2026-09-15 readiness reports predate this finalized reconciliation or assess changing planning artifacts; they are not proof of current alignment. Complete the implementation-epics revision, update its Architecture 1.1 references, then rerun source/story readiness before implementation. Historical technology checks were not repeated; validate dependency availability and compatibility when scaffolding.

A separate implementation-readiness review should validate GDD, architecture, and story alignment before production work begins.

### Validation Date

Original validation: 2026-09-08. Session 0/UX reconciliation: 2026-09-12. GDD 0.8 staged-systems reconciliation: 2026-09-15. No runtime, performance, migration, or accessibility-conformance validation was executed for this revision.

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
