---
stepsCompleted: [1, 2, 3, 4]
inputDocuments:
  - _bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/gdd.md
  - _bmad-output/game-architecture.md
  - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/DESIGN.md
  - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md
scope: P0
excludedScope: Conditional P1, P2, and later proposals
---

# dmud - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for dmud, decomposing the requirements from the GDD, UX Design, and Architecture into implementable stories. This run is constrained to the approved P0 causal-world proof. Conditional P1, P2, and later proposals are source context only and are not implementation requirements.

## Requirements Inventory

### Functional Requirements

FR1: The application must open on a title surface that immediately offers New Game and Continue, with Continue reflecting whether durable saves are available.

FR2: New Game must run a Session 0 conversation in which Rowan asks for the player character's name, background, values, dislikes, desired cool elements, and campaign hopes without supplying choices unless the player explicitly asks for help.

FR3: Session 0 must let the player assign every value from the fixed standard array `8, 10, 12, 13, 14` exactly once across Body, Agility, Constitution, Mind, and Presence; report missing or duplicate assignments without losing prior input; and lock the starting assignments after explicit character confirmation.

FR4: Before starting the campaign, Rowan must reflect the character back while distinguishing character facts, agreed campaign premises, player preferences, and non-binding story hopes, accept corrections, and require explicit confirmation.

FR5: The primary game input must accept ordinary free text for Dungeon Master questions, character actions, and in-world speech, interpret ordinary synonyms without MUD syntax, and avoid visible action suggestions, recommended dialogue, generated replies, or strategy steering.

FR6: The system must classify a submitted intention without treating player assertions as authoritative state, and it must request neutral clarification before committing when the target, meaning, order, stakes, or stopping condition is materially ambiguous.

FR7: Routine feasible actions must succeed without a roll; impossible or mechanically unsupported intentions must be rejected factually without consuming time or state and without offering alternatives unless the player asks for help.

FR8: Before a consequential action commits, the player must be shown the reasonably knowable interpretation, stakes, costs, and stopping conditions; rare-resource spending or materially changed intent must require clarification.

FR9: Every state-changing intention must follow a propose, validate, resolve, atomic commit, then narrate lifecycle in which the rules engine owns feasibility, mechanics, randomness, time, and authoritative state, and narration describes committed facts only.

FR10: Each logical mutating request must commit at most once; duplicate submissions, retries, refreshes, reconnections, and post-commit narration failures must not duplicate purchases, transfers, elapsed time, rolls, XP, points, or other mutations.

FR11: An eligible uncertain check must resolve with one fair d20 where natural 1 automatically fails, natural 20 automatically succeeds at the admitted stakes, and other results succeed when `d20 + attribute + relevant basic-skill bonus >= difficulty`.

FR12: Before rolling, the system must fix and record the contextual difficulty, applicable modifiers and sources, calculated success probability, success and failure stakes, and random input; it must not change difficulty after observing the result.

FR13: The player must be able to inspect whether an action required no roll or, for a rolled action, the die, total, target, modifiers, pre-roll probability, result, committed consequence, rationale, and XP award.

FR14: P0 must support the controlled payment-extension check using Presence 14 with modifier `floor((14 - 10) / 2) = +2`, Persuasion +1, difficulty 12, total bonus +3, and 60% success probability; success grants a one-day extension, while failure leaves the deadline unchanged and consumes only the exchange's actual duration.

FR15: Successful meaningful checks must award player XP and the relevant skill XP as `floor(100 * (0.95 - p) / 0.90)`, where `p` is the actual pre-roll success probability; failures, routine actions, rejected actions, duplicate attempts, and checks that can fail only on natural 1 award zero check XP.

FR16: Player and skill tracks must start at level 1 with 0 XP, persist without a design cap, spend `100 * current level` XP for each next level while carrying excess, grant one allocatable attribute point per player level, grant +1 to the corresponding skill bonus per skill level, and award each resolved check no more than once.

FR17: The character sheet must display earned, spent, and unspent attribute points, allow the player to preview an allocation, require explicit confirmation, reject overspending without mutation, and display only persisted results after commit.

FR18: The world must use one integer-seconds campaign clock that advances only through committed fictional actions and pauses while the game is closed or waiting on browser activity, reading, menus, save operations, or LLM processing.

FR19: Travel must use authored route distance divided by the supported speed—walk 1.4, jog 2.8, sprint 5.6, or crawl 0.5 metres/second—round each completed segment up to a whole second, report the resulting place and time, and use the 7 m Market Square–Mara's Stall and 140 m Market Square–Common Room routes rather than one flat duration.

FR20: Conversation, object handling, purchases, transfers, and explicit or event-based waits must use validated contextual durations and count each duration once; conversation uses `15 * ceil(rendered spoken words / 30)` seconds excluding descriptive prose, the prepared known-value gift pouch takes 5 seconds to transfer, morning is 06:00, and a face-to-face silent wait returns control after 60 seconds.

FR21: Scheduled world events must execute in deterministic order by due game time, priority, and insertion sequence; a long action or wait must stop at the actual time of a development requiring player attention, and an estimated event must never be manufactured merely because the player waited for it.

FR22: P0 must provide exactly the authored Market Square, Mara's Stall, and Common Room locations with stable connections, readable factual exits, examinable context, and descriptions that reflect committed changes without procedural location generation.

FR23: P0 must instantiate Mara, Oren, Tessa, and Ivo with individual needs, competing desires, obligations, relationships, resources, current plans, locations, and limited knowledge as defined by the controlled scenario.

FR24: P0 must maintain authoritative ownership, quantities, location, stock, transferability, and money, including the one-gold drink purchase from stock of five and the controlled 10,000-gold known-value gift pouch.

FR25: A completed purchase or gift must reconcile payer funds, recipient funds or ownership, merchant stock, player inventory, elapsed handling time, and witness observations in one atomic mutation; an incomplete or rejected transfer must not partially change ownership.

FR26: Mara's feasible plan set and selected behavior must be recalculated after the witnessed gift using her resources, needs, obligations, relationships, knowledge, and available time rather than a fixed scripted retirement outcome.

FR27: The simulation must store historical facts, witness observations, spoken claims, and NPC beliefs as distinct records with stable identity, source, acquisition time, uncertainty or confidence, and provenance.

FR28: Information must spread only through plausible perception or contact: Tessa may observe the gift and transmit a claim to Ivo only when their scheduled Common Room meeting occurs 1,800 game seconds after the gift opportunity; before receipt, Ivo must not know the event.

FR29: The controlled rumor variant must allow Tessa's claim to be distorted or doubted and Ivo's distrust to affect confidence or prompt confirmation, while neither the claim nor the belief rewrites the original event or compels a predetermined response.

FR30: NPC knowledge and belief changes may trigger consequential replanning, and later player-observable dialogue, spending, schedules, fulfilled obligations, or choices must demonstrate the causal effect rather than relying on an internal memory flag alone.

FR31: The transcript, journal, reference views, and Rowan's recall answers must expose only information the player character perceived or legitimately learned; they must never reveal hidden actors, motives, omniscient state, or unreceived reports.

FR32: The journal must restate legitimately known facts, concerns, and explicit commitments without recommending an action, inventing a concern, or treating unresolved situations as completed quests.

FR33: Every submitted intention must be echoed exactly with a truthful lifecycle state, moving through acknowledged, clarification, resolved, interrupted, rejected, or failed states without presenting pending work as success.

FR34: If processing fails or is interrupted, the application must identify what did and did not commit, preserve entered material and any legitimate committed progress, and provide a safe retry, recovery, or resume path.

FR35: The application must provide three manual save slots that show enough branch context to choose safely, require overwrite confirmation, and preserve the prior durable state when saving or loading fails.

FR36: Loading a save must restore the complete branch state, including clock, transcript and known state, ownership, inventory, relationships, commitments, facts, observations, beliefs, NPC plans, scheduled events, XP, levels, bonuses, allocated and unspent points, request evidence, and applicable reward records.

FR37: Loading an older save must create or restore that branch without per-action undo or cross-branch state carryover, so progression, knowledge, and rewards from an abandoned branch do not appear in the loaded branch.

FR38: Given the same captured initial state, structured proposals, content versions, and seeded random inputs, replay must reproduce mechanical outcomes and resulting state evidence without requiring newly generated LLM prose to match verbatim.

FR39: Development diagnostics must make proposals, validation, rolls, state changes, operation lifecycle, facts and belief provenance, NPC replanning reasons, clock and event processing, revisions, state hashes, latency, token use, session cost, rejected proposals, duplicate attempts, and contradiction repairs inspectable without exposing hidden state in the normal player UI.

FR40: P0 must support controlled gift/no-gift, rumor, timing, progression-threshold, retry, save/load, and replay fixtures needed to demonstrate the documented P0 causal-world evidence gate.

### NonFunctional Requirements

NFR1: P0 scope must remain limited to one settlement, three authored locations, four named NPCs, one social conflict, one stocked drink, one uncertain-check situation, basic progression, three saves, and controlled causal variants; conditional P1, P2, multiplayer, combat, crafting, magic, titles, achievements, daily quests, and later proposals must not become P0 prerequisites.

NFR2: Authoritative mechanics must be deterministic, invariant-checked, and isolated from probabilistic LLM interpretation and narration.

NFR3: Persistent changes must be transactional, atomic, idempotent, revision-checked, and crash-recoverable, with no ambiguous window between world-state, action-record, request-result, and operation-state commits.

NFR4: Saves must be durable, complete, versioned, integrity-checkable, migratable, and reproducible across supported application and content versions.

NFR5: The implementation must preserve causal explainability: a developer must be able to trace a player-visible consequence through intent, proposal, validation, random resolution, committed changes, observations, claims, beliefs, and NPC replanning.

NFR6: The interface must meet WCAG 2.2 Level AA across complete pages and responsive variations, including semantic structure, keyboard operation, focus visibility, contrast, zoom, reflow, status announcements, reduced motion, and accessible overlays.

NFR7: The player experience must remain readable and usable for text-heavy 20–60-minute desktop-browser sessions, with selectable text, approximately 55–75-character narration lines, and no timed reading requirement.

NFR8: The provisional evaluation targets are visible input acknowledgement within 100 ms, local menu response within 200 ms, save/load within 2 seconds, 95% of completed LLM-mediated actions within 10 seconds, and a recoverable interruption state by 30 seconds; these targets must be measured on a documented test machine rather than treated as already validated commitments.

NFR9: The 60-minute, 100-action, four-NPC evaluation workload must record latency, model calls, tokens, session cost, retries, rejected proposals, contradiction repairs, and unexplained memory growth.

NFR10: The local packaged application must bind to loopback, keep provider credentials and unrestricted provider data on the backend, apply strict input validation, safe errors, conservative request limits, and security headers, and never store secrets in browser storage, saves, content, generated clients, or normal logs.

NFR11: Application and domain code must use strict TypeScript and Python typing; all external, persisted, configuration, API, and model-provider data must receive runtime validation before entering trusted logic.

NFR12: Code must follow cohesive vertical slices with inward dependency direction, explicit injected dependencies, separate command and query paths, thin HTTP adapters, and no domain dependency on FastAPI, SQLite, provider SDKs, environment access, or frontend code.

NFR13: First-party behavior must be verified integration-first through the real FastAPI application, real isolated SQLite persistence, and real browser journeys; only the external LLM provider may use deterministic contract fixtures.

NFR14: Formatting, linting, strict type checking, integration tests, contract drift, and browser tests must run as separate failing quality gates, and each eventual acceptance criterion must map to at least one behavior-focused test.

NFR15: Generated definitions, authored content, structured proposals, scheduled events, and reusable rulings must have stable identities and explicit schema or content versions so descriptions cannot silently change previously committed mechanics.

NFR16: Event processing must be bounded and loop-detected so one action cannot cause an unbounded cascade or hang an event-based wait.

NFR17: Player-facing failures must be plain, specific, recoverable, and free of stack traces, secrets, SQL, hidden objectives, or raw provider payloads; unexpected failures must carry a correlation ID for diagnosis.

NFR18: The browser must remain a presentation client and must not calculate authoritative outcomes, merge competing game states, or use browser storage as a second source of game truth.

### Additional Requirements

- **Starter requirement for Epic 1 Story 1:** scaffold the frontend from create-vite 9.2.0's minimal React/TypeScript template and initialize the FastAPI backend from scratch with uv 0.12.0; then add the exact architecture-selected runtime, validation, generated-client, test, lint, and type-check dependencies. Commit both lockfiles. The starter provides only the React/Vite entry and baseline configuration, not the game's feature architecture.
- Use the architecture-selected local-first stack: Node.js 24.20.0 LTS, React 19.2.8, React DOM 19.2.8, TypeScript 7.0.2, Vite 8.2.2, FastAPI 0.141.1, Python 3.14.7, Pydantic 2.13.5, Pydantic Settings 2.15.0, PyYAML 6.0.3, and SQLite 3.37.0 or newer, with exact resolved versions in committed lockfiles.
- Establish the feature-oriented monorepo and composition roots defined by the architecture, keeping frontend player-facing slices and backend game-system slices cohesive and preserving inward dependencies.
- Add startup SQLite-version validation, explicit ordered SQL migrations, SQLite STRICT application tables, canonical versioned JSON world snapshots, immutable action records, request results, persisted operations and events, three immutable save-slot snapshots, state hashes, and typed world-state migration fixtures.
- Implement stable typed IDs, world revisions, expected-revision conflicts, browser-generated request IDs, server resource IDs, and exactly-once request-result recovery.
- Isolate provider-specific behavior behind a provider-neutral `LlmGateway`; strictly validate versioned proposal and narration contracts, record provider/model/prompt/contract telemetry, and exclude unrestricted raw provider responses from normal saves and player surfaces.
- Implement persisted operation resources for long-running actions with `POST` acknowledgement, typed and versioned SSE progress, monotonically increasing event IDs, `Last-Event-ID` reconnection, polling recovery, cooperative pre-commit cancellation, one mutating operation per branch, and deterministic restart reconciliation.
- Make FastAPI OpenAPI the transport-contract source of truth; generate and commit the native fetch client, TypeScript types, Zod response schemas, and TanStack Query bindings, validate success and error payloads at runtime, and fail CI on generated-contract drift.
- Use resource-specific JSON success responses and RFC 9457 problem details extended with stable error classification, code, correlation ID, operation ID, and world revision; use camelCase JSON fields, lowercase snake_case wire enums, RFC 3339 UTC wall timestamps, integer game seconds, and integer duration milliseconds.
- Restrict TanStack Query to authoritative server state and React state to presentation concerns; browser storage may contain validated presentation preferences only.
- Load the complete P0 authored-content set at startup from version-controlled YAML via `yaml.safe_load` and strict Pydantic schemas, reject unknown fields and duplicate IDs, resolve cross-references, and expose an immutable registry with stable content IDs and versions.
- Keep controlled test starting states separate from production authored content; runtime-generated values belong to versioned world state and must never rewrite authored source files.
- Use typed domain events as returned data with explicit deterministic authoritative dispatch inside the transaction; post-commit SSE and telemetry handlers must not mutate mechanics, and P0 must not introduce a global mutable event bus or external message queue.
- Use typed expected-result variants for rejection, clarification, conflict, and successful resolution; handle unexpected exceptions at HTTP or operation-worker boundaries and roll back failed writes.
- Provide structured JSON logs, a rotating local JSONL destination, a human-readable development console, consistent correlation fields, and redaction of secrets, hidden objectives, complete saves, and unrestricted provider payloads.
- Provide player-safe diagnostics in all builds and read-only development diagnostics only when the backend is loopback-bound and `DMUD_DEVTOOLS=true`; state-changing fixture controls must exist only in automated test infrastructure.
- Package production as one loopback FastAPI process serving the built SPA and API from one origin; use separate proxied Vite and FastAPI servers in development.
- Create and run the architecture-defined quality baseline: Ruff format/check, Pyright strict, pytest integration tests, ESLint with type-aware rules, `tsc --noEmit`, Vitest/Testing Library, Playwright against the real SPA and API, and OpenAPI generation drift checks.
- Apply the project code architecture standard: small single-purpose functions, separate reads and writes, explicit dependency injection, precise boundary validation, cohesive vertical slices, accessible behavior-based tests in AAA form, and no speculative abstractions for conditional P1/P2 systems.
- Use the confirmed P0 tuning: attribute modifier `floor((score - 10) / 2)`; Presence 14 (+2), Persuasion +1, difficulty 12, and 60% success for the payment-extension fixture; walk/jog/sprint/crawl speeds of 1.4/2.8/5.6/0.5 metres per second; routes of 7 m and 140 m; conversation duration `15 * ceil(rendered spoken words / 30)` seconds; 5-second prepared-pouch transfer; 06:00 morning; 60-second face-to-face silence interval; success XP `floor(100 * (0.95 - p) / 0.90)` with zero failure and 95%-check XP; level thresholds of `100 * current level` with carryover; one attribute point or +1 skill bonus per applicable level; and no caps.

### UX Design Requirements

UX-DR1: Implement the complete P0 color-token set from DESIGN.md (`paper`, `paper-light`, `canvas`, `ink`, `ink-muted`, `forest`, `forest-deep`, `red-pencil`, `rule`, `note`, `player-note`, and `focus`) as reusable semantic tokens rather than scattered literal values.

UX-DR2: Implement the documented story, scene-title, overlay-title, interface, interface-strong, label, and caption typography tokens using the specified system-safe font stacks, sizes, weights, line heights, and label spacing; Comic Sans, faux handwriting, and dense medieval display faces are prohibited.

UX-DR3: Implement the documented 4px spacing scale and small, medium, large, extra-large, and full radius tokens, using lightly softened rectangular controls and reserving pill shapes for cases explicitly designed for them.

UX-DR4: Present the application as a warm, accumulated tabletop notebook shared with Rowan, using restrained paper layers and shadows while keeping the transcript visually dominant and avoiding a command-terminal or generic-chat appearance.

UX-DR5: Implement the `action-button` with an explicit text label, pointer and keyboard activation, forest/paper-light styling, visible external focus ring, and a stated reason for disabled states when the reason is not obvious.

UX-DR6: Implement `notebook-navigation` with stable, labeled factual destinations and campaign controls, a programmatically indicated current location, and a selected treatment that does not rely on color alone.

UX-DR7: Implement selectable `story-entry` content that appends only after its status is known, keeps prior consequences visible, uses long-form story typography, and exposes the speaker or message type before the content.

UX-DR8: Implement `player-intention` as a clearly labeled, selectable echo of the exact submitted text with its status and player-note treatment; any decorative tilt must not harm motion preferences or responsive reflow.

UX-DR9: Implement one visibly labeled `message-composer` for Rowan questions, character actions, and in-world speech, where Enter submits and Shift+Enter inserts a line; it must contain no mode selector, prefix requirement, suggestion chips, generated replies, or action recommendations.

UX-DR10: Implement `response-status` so submission receives immediate visible acknowledgement attributed to Rowan and transitions truthfully through pending, clarification, resolved, interrupted, or failed states without stealing focus.

UX-DR11: Implement `character-card` as a compact James-only identity and progression reference that opens the character sheet and never derives or implies an omniscient nearby-character roster.

UX-DR12: Implement one reusable `reference-overlay` shell for inventory, character sheet, roll details, and save/load with an accessible dialog name and role, explicit close control, Escape dismissal, contained focus, focus return, viewport bounds, internal scrolling, subdued backdrop, and a strict no-stacking rule.

UX-DR13: Implement `mechanical-result` as an inline control attached to its transcript result that states the skill/result and whether a roll occurred before its Details action, and supports both rolled and routine/no-roll explanations.

UX-DR14: Implement `journal-entry` as a text-first known-information row with written status, clear dividers, and no color-only state, hidden information, invented concerns, or recommended next action.

UX-DR15: Implement `stat-assignment` with explicit attribute/value pairing and text-plus-boundary treatments for available, assigned, invalid, and locked states, including precise inline reporting of missing or duplicate values.

UX-DR16: Implement `attribute-allocation` with explicit earned/spent/unspent counts and text-plus-boundary treatments for unspent, previewed, confirmation-pending, confirmed, invalid-overspend, persisted, loading, and error states.

UX-DR17: Implement `save-slot` rows that show slot identity, campaign, place, in-world time, and saved-at context; selection must use text and boundary changes in addition to color.

UX-DR18: Implement Title states for cold save-index loading, no saves with an explained unavailable Continue control, saves available, and save-index failure with retry while New Game remains available.

UX-DR19: Implement Session 0 states for the first question, incomplete concept, unassigned/invalid/valid stats, Rowan pending, reflection awaiting correction or confirmation, and response failure with all entered content preserved.

UX-DR20: Implement Main Notebook states for cold load, restored scene, composer ready, pending, clarification, resolved, interrupted, failed, model unavailable, and unsupported intention; pending must never masquerade as committed success.

UX-DR21: Implement Journal empty, known-entry, loading, and failed-read states; empty and failure copy must not invent hints, concerns, or omniscient knowledge.

UX-DR22: Implement Inventory empty, populated, loading, and failed-read states; an empty result must mean no owned items rather than exposing or guessing unknown simulation content.

UX-DR23: Implement Character Sheet states for editable Session 0 stats, P0 progression summary, no/unspent points, allocation preview, invalid overspend, confirmation pending, allocation persisted, loading, and error; conditional-P1 titles and achievements must remain absent.

UX-DR24: Implement Roll Details states for routine/no-roll, rolled resolution, and missing/corrupt evidence; missing evidence must be reported rather than synthesized.

UX-DR25: Implement Save Selection states for empty and occupied slots, saving/loading, overwrite confirmation, failed operation, and recovered prior state.

UX-DR26: Label and semantically expose every active voice—Rowan, narration, each NPC, player intention, and mechanics—without relying on color; conditional-P1 System and award voices must not be implemented in P0.

UX-DR27: Use a warm, direct Rowan voice; grounded narration tied to committed facts; individually attributed, knowledge-limited NPC voices; factual mechanics; neutral intent-preserving clarifications; and plain recovery language that states the commit boundary.

UX-DR28: Allow brief absurd backstage waiting copy only while still truthfully stating that Rowan is working; decorative copy or animation must not imply measured progress, reset screen-reader announcements, obscure status, or claim success.

UX-DR29: Make the complete P0 experience operable by keyboard, including title choices, composer, navigation, overlays, stat assignment, attribute allocation, save slots, and inline mechanics; Tab and Shift+Tab must follow visible reading order.

UX-DR30: Provide pointer parity with keyboard actions, preserve text selection, and ensure hover never contains unique information.

UX-DR31: Provide semantic landmarks, headings, explicit control names/roles/states, speaker/type labels, logical reading order, dialog behavior, and polite live announcements for screen-reader operation.

UX-DR32: Meet minimum contrast of 4.5:1 for normal text, 3:1 for large text and essential focus/component boundaries, and at least 7:1 for primary ink on the main paper surface; never use color as the sole carrier of meaning.

UX-DR33: Preserve all content and functionality at 200% browser zoom and at the WCAG reflow target equivalent to 320 CSS px without two-dimensional page scrolling except for intrinsically two-dimensional content.

UX-DR34: On ordinary desktop widths, allow navigation, dominant story page, and compact character reference as three regions while keeping transcript and composer central; at narrow or zoomed widths, collapse them into one reading column with labeled top navigation and a compact character block.

UX-DR35: Keep overlays within the visible viewport with internal scrolling and identical close/focus-return behavior at all supported widths; do not preserve the mockup's fixed minimum width.

UX-DR36: Honor `prefers-reduced-motion` by replacing looping activity movement with a static mark and stable or changing status text; require no audio, illustration, screen shake, confetti, portrait, timed narrative, auto-dismiss, or interaction timeout.

UX-DR37: Announce pending, clarification, resolved, interrupted, failed, and attribute-allocation changes programmatically without moving focus, while suppressing repetitive announcements for decorative waiting-copy rotations.

UX-DR38: Opening navigation, inventory, journal, character sheet, roll details, save UI, or any reference overlay must advance no fictional time.

UX-DR39: The Main Notebook information hierarchy must prioritize transcript and scene context, then composer and truthful request status, then James's character card, followed by factual navigation and reference controls.

UX-DR40: P0 must exclude the deferred `system-notice` and `award-notice` components and all conditional-P1 alchemy, daily-objective, gacha, affinity, title, achievement, and upgrade flows until a later phase-specific UX update promotes them.

### FR Coverage Map

FR1: Epic 1 - Open with New Game and save-aware Continue choices.
FR2: Epic 1 - Define the player character through Rowan's Session 0 conversation.
FR3: Epic 1 - Assign and validate the fixed starting-stat array.
FR4: Epic 1 - Review, correct, and confirm Rowan's understanding before play.
FR5: Epic 2 - Use one ordinary-language input without strategy-steering suggestions.
FR6: Epic 2 - Classify intentions and clarify ambiguity before commitment.
FR7: Epic 2 - Resolve routine actions directly and reject unsupported actions safely.
FR8: Epic 2 - Expose knowable interpretation, stakes, costs, and stopping conditions.
FR9: Epic 2 - Process changes through the authoritative action lifecycle.
FR10: Epic 2 - Guarantee at-most-once mutations across retries and recovery.
FR11: Epic 3 - Resolve eligible checks with the specified d20 rules.
FR12: Epic 3 - Fix and record difficulty, modifiers, probability, stakes, and randomness.
FR13: Epic 3 - Provide inspectable rolled and no-roll mechanical results.
FR14: Epic 3 - Support the controlled payment-extension check.
FR15: Epic 3 - Award probability-based player and skill XP under confirmed tuning.
FR16: Epic 3 - Persist uncapped player and skill progression.
FR17: Epic 3 - Preview, validate, confirm, and persist attribute allocation.
FR18: Epic 3 - Advance one authoritative seconds-based campaign clock.
FR19: Epic 3 - Calculate travel from authored distance and supported speed.
FR20: Epic 3 - Apply validated contextual durations to timed actions.
FR21: Epic 3 - Process scheduled events deterministically and interrupt long actions.
FR22: Epic 3 - Explore the three stable authored P0 locations.
FR23: Epic 3 - Instantiate the four named NPCs with grounded state and constraints.
FR24: Epic 3 - Maintain authoritative money, item, stock, and ownership state.
FR25: Epic 3 - Commit purchases and transfers atomically.
FR26: Epic 4 - Recalculate Mara's feasible plans after the gift.
FR27: Epic 4 - Store facts, observations, claims, and beliefs with provenance.
FR28: Epic 4 - Transmit Tessa's report to Ivo only through scheduled contact.
FR29: Epic 4 - Support distorted or doubted rumor beliefs without rewriting truth.
FR30: Epic 4 - Make knowledge-driven NPC replanning observable in later behavior.
FR31: Epic 2 - Restrict player surfaces and recall to legitimately known information.
FR32: Epic 2 - Present a factual, non-steering known-information journal.
FR33: Epic 2 - Echo intentions with truthful lifecycle states.
FR34: Epic 2 - Preserve the commit boundary and offer safe failure recovery.
FR35: Epic 5 - Provide three contextual manual save slots with safe overwrite behavior.
FR36: Epic 5 - Restore every causal dependency in a saved branch.
FR37: Epic 5 - Preserve branch isolation without undo or cross-branch carryover.
FR38: Epic 5 - Reproduce mechanical outcomes from captured state and random inputs.
FR39: Epic 5 - Expose read-only causal diagnostics for development evidence.
FR40: Epic 5 - Supply controlled P0 causal-world evidence fixtures.

## Epic List

### Epic 1: Create a Personal Campaign

The player can begin a new campaign, define a character in conversation with Rowan, assign starting attributes, confirm how Rowan understands the character, and enter a personally relevant opening scene.

**FRs covered:** FR1, FR2, FR3, FR4

### Epic 2: Speak and Act Through a Trustworthy Rowan

The player can use ordinary language to ask questions and express intentions, receiving neutral clarification, truthful request states, knowledge-bounded answers, safe rejection, and recoverable outcomes through the authoritative action lifecycle.

**FRs covered:** FR5-FR10, FR31-FR34

### Epic 3: Explore, Transact, and Grow in Brackenford

The player can navigate authored locations, advance deterministic time, buy and transfer items, resolve the controlled check, inspect mechanics, earn progression, and allocate attributes within the grounded P0 world.

**FRs covered:** FR11-FR25

### Epic 4: See Consequences Travel Through People

The player can change Mara's opportunities through a gift, observe NPC plans respond to grounded constraints, and experience information passing from Tessa to Ivo as a fallible, provenance-tracked belief that affects later behavior.

**FRs covered:** FR26-FR30

### Epic 5: Preserve and Verify a World That Remembers

The player can save, resume, branch, and replay the complete causal world, including facts, beliefs, plans, events, and progression. The prototype owner can then demonstrate the P0 evidence gate through inspectable diagnostics and controlled fixtures.

**FRs covered:** FR35-FR40

### Cross-Epic Delivery Guardrails

- The P0 attribute array, vocabulary, modifier rule, controlled check, action-duration values, XP curve, level thresholds, and level rewards are confirmed and must be used consistently by dependent stories.
- Epic 1 must establish the smallest reusable end-to-end Rowan operation path. Later epics extend that path rather than replacing a disposable Session 0 implementation.
- Authoritative state, transactional SQLite persistence, schema versioning, and migrations begin with the first stateful story. Epic 5 adds player-controlled save slots, branching, complete restoration, and replay; it is not the first persistence implementation.
- Correlation IDs, immutable action evidence, and structured diagnostics grow with every state-changing story. Epic 5 completes the read-only causal inspector and evidence suite.
- Every epic must finish as a runnable vertical slice through the real browser, FastAPI application, and isolated SQLite store, using deterministic fixtures only at the external LLM boundary.
- Epic 2 and Epic 3 stories must be ordered as playable vertical capabilities rather than frontend, backend, database, or test layers.
- Epic 4 cannot complete based on convincing narration alone. Its tests must demonstrate distinct facts, observations, claims, beliefs, provenance, feasible-plan changes, and later observable behavior.
- Conditional P1, P2, and later content remains prohibited until the P0 evidence gate passes and a later scope decision promotes it.

### Epic-to-Reality Trace

- Epic boundaries identify user-value completion points. They do not assign exclusive ownership of modules, schemas, or shared infrastructure.
- The UX Session 0 flow maps to Epic 1.
- Source E1, “Act in a small persistent world,” is delivered incrementally through Epics 2, 3, and 5.
- Source E2, “Make consequences travel through people,” is delivered through Epic 4 and receives its durability and evidence completion in Epic 5.
- Epic 1 must create a real versioned campaign state using the immutable authored-content registry and enough Brackenford content to open the confirmed campaign.
- Epic 2 must prove the reusable Rowan lifecycle with a concrete zero-time known-information or inspection action, not placeholder infrastructure, plus clarification, rejection, interruption, and recovery.
- Epic 3 must atomically produce the transaction fact and any witness-observation evidence needed by Epic 4. Epic 4 then completes claims, beliefs, transmission, and knowledge-driven replanning.
- Epic 5 adds manual save controls and complete causal verification over persistence and diagnostics that have evolved continuously since the first stateful story.
- Development-only causal inspection remains capability-gated and must never leak hidden state into the normal player experience.

## Epic 1: Create a Personal Campaign

The player can begin a new campaign, define a character in conversation with Rowan, assign starting attributes, confirm how Rowan understands the character, and enter a personally relevant opening scene.

### Story 1.1: Set Up the Initial Project and Begin a New Campaign

As a player,
I want to open dmud and begin a new campaign,
So that I can immediately start creating a character with Rowan.

**Implements:** FR1

**Acceptance Criteria:**

**Given** a clean checkout with the documented Node.js, Python, uv, and SQLite prerequisites
**When** the project is installed and started using its documented commands
**Then** the create-vite React/TypeScript frontend and uv-managed FastAPI backend run locally
**And** the architecture-selected dependencies and exact resolved versions are captured in committed frontend and backend lockfiles.

**Given** the application starts with a supported SQLite runtime
**When** the backend initializes
**Then** it applies only the ordered strict-table migrations needed for the title, save index, and initial campaign state
**And** startup fails with a specific configuration error before opening application data when SQLite is older than 3.37.0.

**Given** the browser opens dmud
**When** the save index is still loading
**Then** the Title surface immediately displays New Game and Continue
**And** Continue is unavailable with an accessible explanation while availability is unknown.

**Given** no manual saves exist
**When** the save-index request completes
**Then** New Game remains available
**And** Continue remains unavailable with text explaining that there is no campaign to continue.

**Given** the save-index request fails
**When** the Title surface presents the failure
**Then** it provides a retry control and a safe correlation identifier without exposing internal details
**And** New Game remains available.

**Given** the player activates New Game by keyboard or pointer
**When** the initial-campaign request is accepted
**Then** the backend creates one versioned campaign branch through an idempotent, runtime-validated API contract
**And** the browser displays Rowan's first Session 0 question asking for the character's name.

**Given** the same New Game request is submitted again because of a retry, refresh, or lost response
**When** the backend receives the same request identity
**Then** it recovers the original campaign branch and result
**And** it does not create a duplicate branch or advance fictional time.

**Given** the Title or first Session 0 question is visible
**When** the player navigates by keyboard, pointer, screen reader, 200% zoom, or a 320-CSS-pixel reflow viewport
**Then** the content, controls, labels, focus indicator, reading order, and functionality remain available without two-dimensional scrolling
**And** color is not the sole means of communicating control state.

**Given** the application shell renders
**When** its visual styles are inspected
**Then** it uses the complete semantic color, typography, spacing, and radius token foundations from DESIGN.md
**And** it presents the warm notebook identity without Comic Sans, faux handwriting, a terminal appearance, or conditional-P1/P2 interface elements.

**Given** the repository quality gates run
**When** frontend and backend formatting, linting, strict type checking, contract generation drift, integration tests, and the browser journey execute
**Then** every gate passes independently
**And** the browser journey uses the real FastAPI application and isolated SQLite store rather than mocked first-party boundaries.

### Story 1.2: Describe a Character to Rowan

As a player,
I want to describe my character and campaign interests to Rowan in my own words,
So that the campaign can reflect what I want to inhabit without choosing from a prescribed menu.

**Implements:** FR2

**Acceptance Criteria:**

**Given** Rowan is asking for the character's name
**When** the player submits a name
**Then** Rowan records it in the Session 0 draft and proceeds to the character-background questions
**And** no campaign fact or fictional time is committed before final character confirmation.

**Given** Session 0 is in progress
**When** Rowan gathers character information
**Then** Rowan asks where the character came from, what the character cares about, and what the character hates
**And** Rowan subsequently asks what the player thinks would be especially cool and what the player hopes to experience in the campaign.

**Given** the player answers a Session 0 question
**When** the answer is submitted
**Then** the interface immediately echoes the exact text as a labeled player intention and shows a truthful Rowan-working status
**And** the answer is processed through the persisted, reusable Rowan operation lifecycle rather than a Session 0-only shortcut.

**Given** the player uses the Session 0 composer
**When** Enter is pressed
**Then** the current text is submitted once
**And** Shift+Enter inserts a new line without submission.

**Given** the player has not asked Rowan for help generating a background or concept
**When** Rowan asks or responds to Session 0 questions
**Then** Rowan provides no background choices, suggestion chips, generated replies, recommended answers, or preferred campaign direction
**And** the player remains free to describe the character in ordinary language.

**Given** the player explicitly asks for help developing a background
**When** Rowan responds
**Then** Rowan may provide clearly labeled suggestions in conversational text
**And** no suggestion is treated as accepted character information until the player states or confirms it.

**Given** the Rowan operation requires external model work
**When** the request progresses
**Then** its validated operation states are available through typed SSE events with polling recovery
**And** refreshing or reconnecting recovers the existing operation without creating a duplicate submission.

**Given** a provider response is malformed, unavailable, cancelled before commitment, or interrupted
**When** the operation cannot complete
**Then** the interface reports a plain failed or interrupted state with a safe correlation identifier and retry path
**And** all previously entered Session 0 answers and the current submitted text remain available without duplicate draft entries.

**Given** an operation completes or fails after Session 0 draft data was legitimately persisted
**When** the player retries using the same request identity
**Then** the backend returns the existing result or resumes only permitted pending work
**And** it does not duplicate answers, operations, elapsed fictional time, or authoritative mutations.

**Given** Rowan, player content, and operation status are presented
**When** the interface is read visually or with assistive technology
**Then** Rowan and player entries are explicitly labeled, selectable, and distinguishable without color alone
**And** status announcements do not move focus or repeatedly announce decorative waiting-copy changes.

**Given** waiting feedback uses playful backstage copy or animation
**When** the operation remains pending or reduced motion is requested
**Then** the copy still states truthfully that Rowan is working and never implies measured progress or success
**And** reduced-motion presentation uses a static mark rather than looping movement.

**Given** automated tests exercise the conversation
**When** the full browser-to-API flow runs
**Then** it uses the real FastAPI application, operation store, and isolated SQLite database
**And** only the external LLM provider is replaced by a deterministic, strictly validated contract fixture.

### Story 1.3: Assign Starting Attributes

As a player,
I want to assign the standard array across my character's attributes,
So that I can define the character's initial strengths before confirming the campaign.

**Implements:** FR3

**Acceptance Criteria:**

**Given** the player reaches starting-stat assignment
**When** the Character Sheet is presented
**Then** it displays Body, Agility, Constitution, Mind, and Presence exactly once
**And** it displays the available values 8, 10, 12, 13, and 14 without inventing derived attributes or additional values.

**Given** one or more values remain unassigned
**When** the player attempts to complete stat assignment
**Then** the interface identifies every attribute missing a value and every unused array value
**And** it blocks completion without discarding any valid assignments or Session 0 answers.

**Given** the same array value is assigned more than once through malformed client state or a direct API request
**When** the assignment is validated
**Then** the interface identifies each duplicate value and the affected attributes
**And** the backend rejects the invalid mapping without changing the persisted Session 0 draft.

**Given** the player assigns 8, 10, 12, 13, and 14 exactly once across the five attributes
**When** the mapping is validated
**Then** the assignment enters a valid state and can proceed to character review
**And** the values remain editable until the player explicitly confirms the complete character.

**Given** the player changes a valid or incomplete assignment before character confirmation
**When** a different available value is selected for an attribute
**Then** the previous value returns to the available pool and the new one becomes assigned
**And** the persisted Session 0 draft contains exactly the latest one-to-one mapping.

**Given** a stat-assignment request is repeated because of retry, refresh, or reconnection
**When** the backend receives the same request identity
**Then** it recovers the existing result rather than applying a second mutation
**And** the displayed mapping agrees with the authoritative persisted draft.

**Given** the player refreshes or resumes an unfinished Session 0
**When** the character draft reloads successfully
**Then** every assigned and unassigned value is restored exactly
**And** no stat, Session 0 answer, or fictional-time change is lost or duplicated.

**Given** the character draft fails to load or an assignment fails to persist
**When** the error state is shown
**Then** the player receives a specific, recoverable message with a safe correlation identifier
**And** the last confirmed authoritative mapping is preserved rather than replaced by optimistic browser state.

**Given** the player opens or operates stat assignment
**When** they use keyboard, pointer, or screen reader controls
**Then** every attribute and value can be paired without drag-only interaction
**And** labels, available/assigned/invalid states, error associations, focus order, and focus visibility are programmatically available.

**Given** stat assignment is viewed at 200% zoom or the 320-CSS-pixel reflow target
**When** the player reviews or changes values
**Then** all attributes, values, validation messages, and controls remain operable without two-dimensional page scrolling
**And** selected or invalid states use explicit text and boundary changes rather than color alone.

**Given** the Character Sheet is opened, inspected, or edited during Session 0
**When** no in-world action occurs
**Then** the campaign clock advances by zero seconds
**And** conditional-P1 titles, achievements, affinities, and reward controls are absent.

### Story 1.4: Confirm the Campaign Understanding

As a player,
I want to review and correct Rowan's understanding before confirming my character,
So that the campaign begins from an accurate shared foundation without predetermining my story.

**Implements:** FR4

**Acceptance Criteria:**

**Given** the player has supplied the required Session 0 answers and a valid stat assignment
**When** Rowan presents the character reflection
**Then** it separately labels character facts, agreed campaign premises, player preferences, and non-binding story hopes
**And** it does not present preferences or hopes as established world facts or promised outcomes.

**Given** required Session 0 information is missing or the stat assignment is invalid
**When** the player attempts to enter character review or confirm the campaign
**Then** the interface identifies each unresolved requirement and blocks confirmation
**And** all valid answers and assignments remain available for correction.

**Given** Rowan's reflection contains an inaccurate or misclassified statement
**When** the player corrects it in ordinary language
**Then** Rowan updates the Session 0 draft and presents a revised reflection for review
**And** no fictional time, campaign event, or confirmed world fact is created by the correction.

**Given** a player preference or non-binding hope conflicts with an established P0 premise
**When** Rowan reflects the conflict
**Then** Rowan distinguishes the established premise from the preference or hope and asks for neutral clarification
**And** Rowan does not silently rewrite Brackenford, promise an outcome, or recommend a strategy.

**Given** the reflection and stat assignment are valid
**When** the player reaches final review
**Then** the interface presents an explicit confirmation action and the complete information that will become authoritative
**And** no campaign state is confirmed merely by viewing the reflection or continuing the conversation.

**Given** the player explicitly confirms the complete character
**When** the confirmation operation commits
**Then** the backend atomically records the categorized character information, Body, Agility, Constitution, Mind, and Presence assignments, content and schema versions, world revision, state hash, and operation evidence
**And** the confirmed campaign begins at its defined starting game second without charging time for Session 0.

**Given** the campaign confirmation commits successfully
**When** the Character Sheet is shown afterward
**Then** the starting-array assignments are read-only in ordinary use
**And** later earned attribute allocation remains a separate capability rather than altering the starting-array record.

**Given** the confirmed campaign opens
**When** Rowan presents the first Brackenford scene
**Then** the application uses stable authored content and opens at the authored P0 starting location in Market Square
**And** the scene is personally relevant to the confirmed character facts and hopes without predetermining NPC decisions, quest order, success, or campaign outcome.

**Given** the opening scene contains narration, Rowan text, NPC speech, player information, or mechanics
**When** it is presented in the notebook
**Then** each active voice or message type is explicitly labeled and exposed semantically rather than distinguished by color alone
**And** only information the character may legitimately perceive or know is shown.

**Given** the confirmation request is retried, refreshed, or reconnected with the same request identity
**When** the backend processes it again
**Then** it recovers the existing confirmed campaign and result
**And** it does not create another campaign, relock stats, duplicate the opening event, or advance fictional time.

**Given** confirmation fails before the atomic commit
**When** the failure is presented
**Then** the Session 0 draft remains editable and no campaign fact has committed
**And** the player receives a specific recovery path with a safe correlation identifier.

**Given** mechanics commit but opening narration fails afterward
**When** the player recovers or retries presentation
**Then** the confirmed character and initial world state remain authoritative
**And** only narration is retried from committed, player-perceptible facts.

**Given** the confirmed campaign is viewed by keyboard, pointer, screen reader, 200% zoom, or a reflow viewport
**When** the player reviews the opening and Character Sheet
**Then** focus, labels, reading order, transcript text, and controls remain accessible and selectable
**And** conditional-P1/P2 systems, rewards, suggestions, and hidden simulation state remain absent.

## Epic 2: Speak and Act Through a Trustworthy Rowan

The player can use ordinary language to ask questions and express intentions, receiving neutral clarification, truthful request states, knowledge-bounded answers, safe rejection, and recoverable outcomes through the authoritative action lifecycle.

### Story 2.1: Ask Rowan What I Know

As a player,
I want to ask Rowan what my character legitimately knows and review it in my journal,
So that I can reason about the world without receiving hidden information or strategic direction.

**Implements:** FR5, FR31, FR32

**Acceptance Criteria:**

**Given** a confirmed campaign is active
**When** the Main Notebook loads
**Then** it presents the current scene and transcript as the dominant reading surface, followed by the composer and truthful response status, James's character card, and factual navigation controls
**And** it does not display an omniscient nearby-character roster, suggested actions, generated replies, or conditional-P1/P2 controls.

**Given** the player enters "What do I know about Mara's debt?" or an ordinary-language equivalent
**When** the intention is submitted
**Then** Rowan classifies it as a Dungeon Master knowledge question rather than in-world speech or an action
**And** the exact submitted text is echoed as a labeled player intention with immediate truthful status.

**Given** Rowan resolves a knowledge question
**When** the answer is returned
**Then** it is derived only from authoritative facts the character observed, received, or was explicitly given as starting knowledge
**And** it does not reveal hidden motives, concealed actors, unreceived reports, private NPC state, or omniscient causal chains.

**Given** the character lacks evidence for some or all of the requested information
**When** Rowan answers
**Then** Rowan plainly identifies what the character does not know
**And** Rowan does not synthesize an answer from hidden state, invent a concern, or suggest how to discover it.

**Given** a knowledge question is processed successfully
**When** the authoritative result is recorded
**Then** the campaign clock advances by zero seconds and no world mutation or revision increment occurs
**And** operational evidence may be recorded without treating the query as a fictional event.

**Given** the player opens the Journal
**When** known information is available
**Then** it presents text-first entries for legitimately known facts, concerns, and explicit commitments with their statuses written in words
**And** each entry preserves its player-visible source or context without exposing hidden provenance details.

**Given** a concern has no explicit accepted commitment or completion evidence
**When** it appears in the Journal
**Then** it remains an unresolved concern rather than a completed quest
**And** the Journal does not recommend a next action or imply a preferred resolution.

**Given** the Journal has no known entries, is loading, or fails to load
**When** that state is presented
**Then** it shows a distinct empty, loading, or recoverable failure treatment
**And** empty or failure copy does not invent hints, concerns, commitments, or world information.

**Given** the player opens or closes the Journal or Character Sheet
**When** the reference interaction completes
**Then** no fictional time advances
**And** current navigation, accessible name, focus location, and return behavior remain predictable.

**Given** the player operates the Main Notebook and Journal with keyboard, pointer, or screen reader
**When** they navigate, submit, read, or return to the transcript
**Then** landmarks, headings, labels, current navigation state, speaker types, controls, focus order, and status changes are programmatically available
**And** text remains selectable and hover contains no unique information.

**Given** the Main Notebook is viewed on an ordinary desktop
**When** sufficient width is available
**Then** navigation, the dominant story page, and James's compact character reference may use three regions while transcript and composer remain central
**And** the layout does not expose other characters merely because they exist in simulation state.

**Given** the Main Notebook reflows at 200% zoom or the 320-CSS-pixel target
**When** the player uses the same features
**Then** the regions collapse into one logical reading column with labeled top navigation and a compact character block
**And** all content and controls remain available without two-dimensional page scrolling.

**Given** the knowledge request or Journal query fails
**When** the failure is presented
**Then** the prior transcript and legitimately known information remain intact with a safe retry and correlation identifier
**And** the interface does not imply that an answer or state change succeeded.

**Given** automated coverage exercises the knowledge flow
**When** the tests run through the browser and API
**Then** they verify permitted, unknown, and hidden-information fixtures against the real application and isolated SQLite store
**And** they verify that the same player-facing answer cannot be expanded merely because additional hidden simulation state exists.

### Story 2.2: Resolve a Routine Intention

As a player,
I want Rowan to understand an ordinary-language inspection and resolve it consistently,
So that I can interact naturally without learning a rigid command syntax.

**Implements:** FR5, FR7, FR9, FR33

**Acceptance Criteria:**

**Given** the player is in Market Square
**When** they submit "look around," "inspect the square," "survey the plaza," or another supported ordinary-language equivalent
**Then** Rowan classifies the intention as an inspection of the current location
**And** the player is not required to use one exact verb, command prefix, or interaction mode.

**Given** the player submits an inspection intention
**When** processing begins
**Then** the exact text is echoed immediately with a labeled pending status
**And** the composer provides no suggested actions, generated replies, recommendation chips, or preferred follow-up.

**Given** the external interpreter proposes an action
**When** its response crosses the provider boundary
**Then** the proposal is strictly validated against its versioned contract before application or domain code reads it
**And** malformed, unknown, or unsupported proposal fields cannot mutate state or reach narration as accepted facts.

**Given** a validated inspection targets the current authored location
**When** the rules evaluate feasibility
**Then** the inspection succeeds as a routine action without rolling
**And** the authoritative result records that no roll was needed and awards no check XP.

**Given** the inspection resolves successfully
**When** time and state effects are calculated
**Then** the campaign clock advances by zero seconds and no ownership, plan, relationship, knowledge, or location state changes
**And** the action evidence records the validated interpretation and authoritative no-change result without incrementing the world revision.

**Given** the authoritative inspection result is available
**When** Rowan narrates it
**Then** narration is generated only from authored current-location details, committed changes, and information the character may perceive
**And** it does not invent hidden actors, motives, exits, items, events, or successful state changes.

**Given** the inspection result appears in the transcript
**When** the player activates its inline mechanical result
**Then** the interface identifies the action as routine and states "No roll needed" with its feasibility rationale
**And** the details use the accessible reference-overlay behavior without advancing fictional time.

**Given** the player submits a statement framed as an authoritative claim, such as "I own this market"
**When** Rowan interprets it
**Then** the statement remains a player assertion rather than a direct state edit
**And** ownership or other world facts change only through a separately supported and validated action.

**Given** the same inspection is submitted more than once as genuinely separate requests
**When** each request resolves
**Then** each may produce a new presentation of the current perceptible state
**And** none creates fictional time, XP, ownership changes, or other mechanical rewards.

**Given** narration fails after the authoritative inspection result is recorded
**When** the operation reports the failure
**Then** the no-change mechanical result remains authoritative and inspectable
**And** narration can be retried without reinterpreting the action or introducing a state mutation.

**Given** the transcript presents the player intention, Rowan status, narration, and mechanics
**When** it is read visually or with assistive technology
**Then** every message exposes its speaker or type before its selectable content
**And** resolution replaces the pending state in context without stealing focus or collapsing prior entries.

**Given** automated tests exercise routine inspection synonyms
**When** the browser-to-API tests run
**Then** supported phrasings reach the same observable inspection behavior through the real application and isolated SQLite store
**And** deterministic provider fixtures replace only the external LLM while strict boundary validation and the complete proposal-to-narration flow remain active.

### Story 2.3: Clarify Consequential Intent

As a player,
I want Rowan to clarify ambiguous or consequential intentions before acting,
So that the game commits what I actually meant with understood stakes and costs.

**Implements:** FR6, FR8, FR33, FR34

**Acceptance Criteria:**

**Given** the player submits "I'll talk to Mara about the debt"
**When** the interpreter cannot determine whether this means asking Rowan for known information or beginning a specific in-world conversation
**Then** the operation enters `needs_clarification`
**And** Rowan asks which meaning the player intended without recommending an argument, tactic, or preferred choice.

**Given** an operation needs clarification
**When** the clarification is presented
**Then** the transcript preserves and labels the exact original intention and its unresolved status
**And** no fictional time, random result, authoritative state mutation, or world-revision increment occurs.

**Given** clarification is required because information is missing
**When** Rowan asks the follow-up question
**Then** it identifies the specific missing target, meaning, amount, order, stakes, or stopping condition
**And** it does not replace the player's wording with a materially different intention.

**Given** the player clarifies that the Mara request is a question about existing knowledge
**When** the operation resumes
**Then** it resolves through the established knowledge-query behavior using the original intention plus the clarification
**And** the answer remains limited to legitimate player-character knowledge at zero fictional-time cost.

**Given** the player clarifies that the request is an in-world action not yet supported by the current P0 capability slice
**When** the clarified proposal is validated
**Then** the game reports the current mechanical limitation factually without committing the action
**And** it does not provide unsolicited alternatives or imply that capabilities outside the implemented slice already exist.

**Given** a supported consequential action has a reasonably knowable interpretation, cost, stakes, sequence, and stopping condition
**When** the action reaches pre-commit validation
**Then** those details are displayed before commitment in factual language
**And** hidden NPC motives, secret information, and unknowable consequences remain undisclosed.

**Given** a proposed action spends a rare resource or materially changes the player's apparent intent
**When** the proposal differs from what was explicitly authorized
**Then** the operation requires clarification or confirmation before commitment
**And** silence, latency, or an unrelated reply cannot be treated as consent.

**Given** the player submits a multi-action request whose order or stopping conditions affect the outcome
**When** the interpreter cannot represent it safely as one bounded operation
**Then** Rowan identifies the ambiguity and may ask the player to submit the actions individually
**And** Rowan does not choose an order or execute a partial sequence without explicit agreement.

**Given** the player answers a clarification
**When** the operation resumes
**Then** it retains the same operation and request identity while recording the validated clarification contract
**And** retrying or reconnecting does not create a second action or duplicate the clarification response.

**Given** the world revision changes while an operation awaits clarification
**When** the player submits the clarification against the stale revision
**Then** the backend returns a typed conflict without committing the proposal
**And** the interface refreshes authoritative context and explains that the intention must be reviewed again.

**Given** the player cancels while an operation is awaiting clarification or otherwise remains pre-commit
**When** cancellation succeeds
**Then** the operation becomes terminal without changing game state or fictional time
**And** the original transcript entry remains available as an unresolved or cancelled intention rather than disappearing.

**Given** clarification status is announced or displayed
**When** the player uses keyboard, pointer, screen reader, reduced motion, zoom, or reflow
**Then** the missing distinction and available response control remain perceivable and operable without forced focus movement
**And** color, animation, or decorative waiting copy is never the sole indicator that input is required.

**Given** automated tests exercise ambiguous, consequential, rare-resource, multi-action, stale-revision, and cancellation cases
**When** the tests run through the real API and isolated SQLite operation store
**Then** every pre-commit path proves zero world mutation and zero fictional-time advancement
**And** deterministic provider fixtures remain confined to the external LLM boundary.

### Story 2.4: Reject and Recover Safely

As a player,
I want unsupported or interrupted intentions to fail honestly and recover safely,
So that I can trust what changed and continue without duplicated consequences.

**Implements:** FR7, FR9, FR10, FR33, FR34

**Acceptance Criteria:**

**Given** the player submits an impossible or unsupported P0 intention, such as using an unimplemented combat or magic system
**When** the rules validate the proposal
**Then** the operation is rejected with a factual explanation of the current limitation
**And** no fictional time, roll, XP, resource, world state, or world revision changes.

**Given** an intention is rejected
**When** Rowan presents the result
**Then** Rowan does not narrate attempted effects as successful or partially committed
**And** Rowan offers no alternative action, tactic, or recommended choice unless the player explicitly asks for help.

**Given** an action operation is in progress
**When** its state changes
**Then** the persisted operation and typed SSE event report the actual applicable lifecycle state, such as accepted, interpreting, needs clarification, validating, resolving, committed, narrating, complete, failed, or interrupted
**And** the interface never presents pending, failed, interrupted, or rejected work as success.

**Given** operation events are delivered over SSE
**When** the browser reconnects after missing events
**Then** it resumes from the last monotonically increasing event identifier when possible
**And** status polling recovers the authoritative operation state when streaming is unavailable.

**Given** one mutating operation is already executing for a branch
**When** another mutating request targets that branch
**Then** the backend does not execute the second mutation concurrently against the same world revision
**And** read-only queries remain available without changing authoritative state.

**Given** the browser repeats a request because of refresh, reconnection, timeout, or lost response
**When** the backend receives the same request identity
**Then** it returns or resumes the existing operation and authoritative result
**And** it does not reinterpret, reroll, recommit, duplicate transcript consequences, or advance time again.

**Given** provider, validation, or infrastructure work fails before commit
**When** the operation becomes failed or interrupted
**Then** authoritative world state remains unchanged and the interface explicitly says that nothing committed
**And** the original intention remains available for a safe retry or revision.

**Given** mechanics have committed but narration or presentation subsequently fails
**When** the operation becomes recoverable
**Then** the interface explicitly identifies the committed boundary and preserves the authoritative result
**And** recovery retries only narration or delivery from committed facts rather than rerunning mechanics.

**Given** the player requests cancellation before commit
**When** provider or validation work cooperatively stops
**Then** cancellation produces no authoritative state change
**And** once commit has occurred, cancellation cannot roll back mechanics and may stop only remaining narration or delivery.

**Given** the application restarts with a nonterminal operation
**When** startup reconciles persisted operations against atomic request results
**Then** an operation with a committed result resumes only narration or presentation, while an operation without one becomes safely interrupted
**And** a validated `needs_clarification` operation remains paused rather than being executed automatically.

**Given** a rejected, failed, interrupted, conflicted, or fatal result is presented
**When** the player reads the message
**Then** it uses the documented typed problem format and plain recovery language with a correlation identifier and applicable operation or world-revision context
**And** it exposes no stack trace, SQL, secret, hidden objective, unrestricted provider payload, or concealed world state.

**Given** response status changes while the player is reading or composing
**When** the interface announces the update
**Then** it preserves focus and the unsent composer draft while updating the relevant transcript entry in context
**And** it avoids repeatedly announcing decorative waiting-copy rotations.

**Given** automated tests inject pre-commit failure, post-commit narration failure, duplicate delivery, stale revision, cancellation, stream loss, and process restart
**When** the real FastAPI application and isolated SQLite store recover each scenario
**Then** persisted state and action evidence prove at-most-once authoritative behavior
**And** only external provider behavior is substituted by deterministic fixtures with a documented justification.

## Epic 3: Explore, Transact, and Grow in Brackenford

The player can navigate authored locations, advance deterministic time, buy and transfer items, resolve the controlled check, inspect mechanics, earn progression, and allocate attributes within the grounded P0 world.

### Story 3.1: Explore the Authored Brackenford Hub

As a player,
I want to move naturally among Brackenford's authored locations,
So that distance, movement choice, and persistent place give the world a trustworthy physical shape.

**Implements:** FR18, FR19, FR22, FR23

**Acceptance Criteria:**

**Given** the P0 content package loads at startup
**When** authored content is validated
**Then** it defines exactly Market Square, Mara's Stall, and the Common Room with stable IDs, schema and content versions, and authored connections
**And** strict validation rejects unknown fields, duplicate IDs, invalid references, or unsupported content versions before a campaign opens.

**Given** the Brackenford P0 world is instantiated
**When** its NPC foundations are loaded
**Then** Mara, Oren, Tessa, and Ivo each have authored needs, competing desires, obligations, relationships, resources, current plans, locations, and limited starting knowledge
**And** those definitions do not add conditional-P1/P2 characters, procedural locations, combat state, or speculative systems.

**Given** a newly confirmed campaign opens in Market Square
**When** the current-location view is presented
**Then** it exposes factual authored exits to Mara's Stall and the Common Room with their distances
**And** it shows only people and details the character may currently perceive rather than every actor in simulation state.

**Given** the player first enters an authored location
**When** Rowan narrates the place
**Then** the introduction uses 60–120 words based on authored geography and current perceptible state
**And** narration does not invent exits, hidden actors, uncommitted events, or procedurally generated geography.

**Given** the player revisits an authored location
**When** Rowan describes it again
**Then** the description uses 20–60 words and emphasizes actual committed changes
**And** unchanged authored geography and connections remain stable.

**Given** the player requests travel through ordinary language or activates a factual linked exit
**When** the destination is connected and the movement mode is supported
**Then** travel duration is calculated as authored distance divided by speed and rounded up to a whole second
**And** linked exits remain factual navigation controls rather than suggested strategies.

**Given** no character or context modifier applies
**When** the player travels the 7 m Market Square–Mara's Stall route
**Then** walking takes 5 seconds, jogging 3 seconds, sprinting 2 seconds, and crawling 14 seconds
**And** the selected mode and computed duration are recorded before commitment.

**Given** no character or context modifier applies
**When** the player travels the 140 m Market Square–Common Room route
**Then** walking takes 100 seconds, jogging 50 seconds, sprinting 25 seconds, and crawling 280 seconds
**And** the longer route never receives the shorter route's flat duration.

**Given** a travel request names no movement mode and context does not establish one
**When** the missing mode changes the duration materially
**Then** Rowan asks a neutral clarification before committing travel
**And** no location, time, event, or world revision changes while clarification is pending.

**Given** the player requests an unknown route, disconnected destination, or unsupported movement mode
**When** the rules validate the request
**Then** the operation is rejected with a factual explanation or asks for required supported information
**And** no travel, fictional time, roll, XP, or state mutation occurs.

**Given** valid travel completes without an interrupting event
**When** the action commits
**Then** location, campaign clock, world revision, action record, and resulting state hash update atomically exactly once
**And** the transcript reports the new place, selected movement mode, elapsed seconds, and current world time.

**Given** travel is a routine feasible action
**When** its mechanical result is inspected
**Then** it reports the distance, speed, rounding, elapsed time, and "No roll needed" rationale
**And** it awards no player or skill XP.

**Given** the same travel request is redelivered with the same request identity
**When** the backend recovers it
**Then** it returns the original committed destination and elapsed time
**And** it does not move the player again, process the segment twice, or advance the clock again.

**Given** location content or travel results appear in the Main Notebook
**When** the player uses keyboard, pointer, screen reader, zoom, or reflow
**Then** current location, factual exits, selected mode, world time, narration, and mechanical details remain labeled and operable
**And** text remains selectable and no information or control relies on hover or color alone.

**Given** automated tests exercise authored-content loading and every route/mode combination
**When** the tests run through the real API and isolated SQLite store
**Then** they verify exact durations, atomic location/time commits, content validation failures, and idempotent retry behavior
**And** Playwright verifies equivalent free-text and linked-exit outcomes through the real browser interface.

### Story 3.2: Advance Time and Wait for World Events

As a player,
I want conversations and waits to advance one consistent world clock,
So that nearby and distant events happen at believable, reproducible times.

**Implements:** FR18, FR20, FR21

**Acceptance Criteria:**

**Given** the player and an NPC complete an in-world spoken exchange
**When** its duration is calculated
**Then** the rules total only rendered spoken words from the player and NPC and apply `15 × ceil(words / 30)` seconds
**And** descriptive prose, player instructions, interface text, and model reasoning are excluded.

**Given** completed spoken exchanges contain 2, 30, or 31 counted words
**When** their durations are resolved
**Then** they advance time by 15, 15, and 30 seconds respectively
**And** the counted words, formula, and result are recorded before commitment.

**Given** an exchange contains zero spoken words
**When** its speech duration is calculated
**Then** speech contributes zero seconds
**And** any meaningful hesitation, silence, handling, or other action receives its own separately validated duration rather than being hidden in the speech count.

**Given** an LLM proposes a conversation or action duration
**When** the rules validate it
**Then** the value must agree with actual rendered speech, supported handling, travel, or event phases
**And** an unsupported estimate cannot advance the authoritative clock.

**Given** a conversation is interrupted before all planned speech occurs
**When** the action resolution commits
**Then** only completed spoken or action phases contribute elapsed time and effects
**And** unspoken future dialogue is neither charged nor narrated as completed.

**Given** the player requests a wait for an explicit duration
**When** no response-worthy event intervenes
**Then** the campaign clock advances by exactly that duration through the deterministic scheduler
**And** the operation records processed events and the final game second.

**Given** the player waits from 22:00 until morning
**When** morning is resolved as the next 06:00
**Then** the intended wait is 28,800 seconds
**And** the scheduler may still interrupt earlier at the actual time of a response-worthy event.

**Given** the player waits face-to-face without speaking or naming another stopping condition
**When** no earlier response-worthy development occurs
**Then** control returns after 60 seconds with a factual observation that one minute passed
**And** the player may speak or continue waiting without the game assuming an NPC decision.

**Given** the player waits for an NPC to perform an action, such as placing an order
**When** the NPC's deterministic plan or validated replanning schedules that action
**Then** the wait stops when the action actually occurs or an earlier attention event intervenes
**And** Rowan's estimated timing cannot manufacture the requested action.

**Given** no qualifying event is scheduled or the requested event becomes impossible
**When** the event-based wait is evaluated
**Then** the game reports that state and returns control rather than waiting indefinitely
**And** no fictional event is invented to satisfy the request.

**Given** multiple scheduled events share or cross the same time interval
**When** the scheduler processes them
**Then** it orders them by due game second, event priority, and insertion sequence
**And** the same starting state and recorded random inputs produce the same processing order.

**Given** a long action crosses an event that requires player attention
**When** the scheduler reaches the event's actual game second
**Then** the action stops at that point and commits only completed phases and processed events
**And** the transcript identifies what completed, what remains unfinished, and why control returned.

**Given** event processing schedules recursive or same-time follow-up work
**When** the configured processing budget or loop detector is reached
**Then** the operation stops safely with a recoverable diagnostic result
**And** it does not hang, skip the commit boundary, or continue an unbounded event cascade.

**Given** the player reads, types, opens menus or reference views, waits for the LLM, closes the application, or saves presentation preferences
**When** no fictional action commits
**Then** the campaign clock advances by zero seconds
**And** distant NPC plans do not progress during application downtime or model latency.

**Given** a timed action or wait is redelivered with the same request identity
**When** the backend recovers the operation
**Then** it returns the original clock, completed phases, processed events, and interruption result
**And** it does not repeat elapsed time or event effects.

**Given** time advancement and interruption are presented in the Main Notebook
**When** the player inspects the result
**Then** elapsed seconds, final world time, stopping condition, and completed boundary are available in factual text
**And** the update remains keyboard-accessible, screen-reader announced without forced focus, and distinguishable without color alone.

**Given** automated tests exercise speech lengths, explicit waits, clock-target waits, face-to-face silence, impossible event waits, simultaneous events, interruptions, loops, downtime, and retries
**When** they run against the real scheduler and isolated SQLite store
**Then** exact clock and event outcomes are reproducible from the same state and recorded random inputs
**And** no test relies on fresh LLM prose to reproduce mechanics.

### Story 3.3: Purchase and Transfer Owned Items

As a player,
I want purchases and gifts to reconcile ownership, stock, money, witnesses, and time exactly once,
So that material actions have trustworthy persistent consequences.

**Implements:** FR20, FR24, FR25

**Acceptance Criteria:**

**Given** the controlled P0 starting fixture is created
**When** inventory and merchant state load
**Then** the player owns 10,000 test gold, Mara stocks five drinks priced at one gold each, and the prepared gift pouch has a known value of 10,000 gold
**And** the test funding is identified as controlled fixture state rather than the normal campaign's assumed starting balance.

**Given** the player opens Inventory
**When** owned assets load successfully
**Then** the overlay displays authoritative money, item identity, quantity, location, and relevant transferability information
**And** opening, reading, or closing Inventory advances zero fictional seconds.

**Given** Inventory is empty, loading, or fails to load
**When** that state is presented
**Then** the overlay distinguishes empty, loading, and recoverable failure states
**And** it never exposes scenery, NPC property, hidden simulation assets, or unknown content as player-owned inventory.

**Given** the player intends to buy one stocked drink from Mara
**When** the purchase reaches pre-commit review
**Then** the known item, quantity, one-gold price, available funds, stock, intended recipient, and validated speech and handling durations are available
**And** speech and handling time are each counted once rather than duplicated in a combined narrative duration.

**Given** the player has sufficient funds and Mara has stock and consents to the sale
**When** the one-drink purchase commits
**Then** the player loses one gold and gains one drink, Mara gains one gold and retains four drinks, and the validated handling time advances once
**And** all ownership, quantity, funds, time, action evidence, world revision, and state-hash changes commit atomically.

**Given** the purchase is routine and feasible
**When** its mechanical result is inspected
**Then** it reports the price, quantity, ownership changes, and elapsed handling time with "No roll needed"
**And** no player or skill XP is awarded.

**Given** the player lacks funds, Mara lacks stock, the item is not transferable, the owner does not consent, or the requested quantity is unavailable
**When** the rules validate the transaction
**Then** the purchase or transfer is rejected with the applicable factual reason
**And** no money, item, stock, ownership, time, witness observation, or world revision changes.

**Given** the controlled gift branch begins from its unchanged starting fixture
**When** the player gives Mara the prepared known-value pouch
**Then** the proposed handling duration is five seconds and the pouch value is treated as a prepared total rather than 10,000 individually counted loose coins
**And** no general container, weight, or equipment subsystem is introduced.

**Given** the five-second gift handover completes without interruption
**When** the action commits
**Then** the player loses ownership of the 10,000 gold value, Mara gains it, and the clock advances five seconds exactly once
**And** the gift fact and Tessa's witness observation are committed atomically as complete authoritative evidence without requiring downstream belief or planning behavior to complete the transaction.

**Given** Tessa witnesses the committed gift
**When** the player-facing result is presented
**Then** Rowan may describe only perceptible evidence that Tessa observed the handover
**And** the interface does not expose her hidden interpretation, future claim, or resulting NPC plan.

**Given** the five-second pouch transfer is interrupted after three completed seconds
**When** the interrupted action commits its completed boundary
**Then** the clock may advance three seconds and the interrupting event may commit, but ownership of the gold remains with the player
**And** retrying cannot treat the incomplete handover as an already completed transfer.

**Given** the player instead transfers 100 individually counted loose coins
**When** handling duration is validated
**Then** counting contributes at least 100 seconds before any additional supported speech or handover duration
**And** the value is not incorrectly treated as the five-second prepared-pouch case.

**Given** the same completed purchase or gift request is redelivered with the same request identity
**When** the backend recovers the operation
**Then** it returns the original authoritative transaction and result
**And** funds, stock, ownership, time, facts, and witness observations are not applied again.

**Given** persistence or narration fails before or after the transaction boundary
**When** recovery is presented
**Then** a pre-commit failure preserves all prior authoritative state, while a post-commit narration failure preserves the complete committed transaction
**And** the player is told exactly what did and did not transfer before retrying.

**Given** the Inventory overlay is operated by keyboard, pointer, screen reader, zoom, or reflow
**When** the player opens, reads, and closes it
**Then** it uses the shared accessible reference-overlay with an accessible name, contained focus, Escape and explicit close behavior, focus return, viewport bounds, and internal scrolling
**And** no overlay stacks or communicates ownership and error state through color alone.

**Given** automated tests exercise successful and rejected purchases, completed and interrupted gifts, loose-coin handling, witness creation, duplicate delivery, and commit-boundary failures
**When** they run through the real API and isolated SQLite store
**Then** conservation assertions reconcile every quantity and monetary change with exact elapsed time
**And** the browser tests verify the same authoritative outcomes without mocking first-party rules or persistence.

### Story 3.4: Resolve a Transparent Persuasion Check

As a player,
I want uncertain social actions resolved from declared rules and recorded randomness,
So that success and failure feel fair, inspectable, and consistent with my character.

**Implements:** FR11, FR12, FR13, FR14, FR20

**Acceptance Criteria:**

**Given** the controlled payment-extension situation is available
**When** the player asks Oren to grant Mara a one-day payment extension
**Then** the rules identify the request as an eligible Presence plus Persuasion check rather than a routine success
**And** impossible demands or outcomes beyond the admitted stakes are screened out before any roll.

**Given** the fixture character has Presence 14 and Persuasion +1
**When** modifiers are calculated
**Then** Presence contributes `floor((14 - 10) / 2) = +2`, Persuasion contributes +1, and the total bonus is +3
**And** the raw attribute score, modifier rule, skill bonus, sources, and total are recorded separately.

**Given** the check is ready for resolution
**When** its pre-roll information is established
**Then** the difficulty is fixed at 12 and the actual success probability is fixed at 60%
**And** the knowable interpretation, actual conversation-time cost, one-day-extension success stake, and unchanged-deadline failure stake are recorded before randomness is sampled.

**Given** the pre-roll result is available to the player
**When** the check proceeds
**Then** the declared difficulty, modifiers, probability, costs, and stakes are inspectable before the outcome appears
**And** hidden NPC motives or unknowable contextual consequences remain undisclosed.

**Given** one fair d20 is rolled with a +3 total bonus against difficulty 12
**When** the die is 1
**Then** the check automatically fails
**And** no modifier can turn the natural 1 into success.

**Given** one fair d20 is rolled with a +3 total bonus against difficulty 12
**When** the die is 20
**Then** the check automatically succeeds at the admitted one-day-extension stakes
**And** the natural 20 does not compel obedience or authorize an otherwise impossible outcome.

**Given** the die result is between 2 and 19
**When** the total is calculated
**Then** the check succeeds exactly when `die + 3 >= 12`
**And** faces 9–19 succeed while faces 2–8 fail, producing twelve successful faces including natural 20 out of twenty.

**Given** the check resolves
**When** randomness is consumed
**Then** exactly one die result and its recorded random input are associated with the operation
**And** the difficulty, modifiers, probability, and stakes cannot change after the die is known.

**Given** the check succeeds
**When** the action commits
**Then** Oren's recorded payment deadline is extended by one day and the actual completed conversation duration advances once
**And** no broader obedience, relationship rewrite, gift reversal, or unstated concession is committed.

**Given** the check fails
**When** the action commits
**Then** Oren's payment deadline remains unchanged and only the actual completed conversation duration advances
**And** any prior gift, ownership change, observation, or unrelated commitment remains intact.

**Given** the same resolved check request is redelivered with the same request identity
**When** the backend recovers the result
**Then** it returns the original die, total, consequence, elapsed time, revision, and state hash
**And** it does not reroll, reapply the extension, or advance conversation time again.

**Given** the player repeats the same failed request without a materially changed approach or circumstance
**When** check eligibility is evaluated
**Then** the game does not grant an unlimited new roll
**And** it explains the grounded reason without changing state or awarding another resolution opportunity.

**Given** the result appears in the transcript
**When** the player opens Roll Details
**Then** the overlay displays the attribute score and modifier, skill bonus, difficulty, probability, die, total, result, declared stakes, committed consequence, elapsed time, and rationale
**And** the details remain attached to this transcript result rather than becoming an unexplained global roll entry.

**Given** roll evidence is missing or corrupt
**When** Roll Details is opened
**Then** the interface reports that the explanation is unavailable or invalid
**And** it does not synthesize a replacement roll, modifier, probability, or consequence.

**Given** Rowan narrates the resolved exchange
**When** narration is validated for presentation
**Then** it agrees with the recorded die and committed deadline consequence
**And** narration failure cannot alter, rerun, or roll back the mechanical result.

**Given** Roll Details is used by keyboard, pointer, screen reader, zoom, or reflow
**When** the overlay opens and closes
**Then** it uses the shared accessible overlay behavior with contained focus, Escape and explicit close controls, focus return, and no stacking
**And** opening or reading it advances zero fictional seconds.

**Given** automated tests exercise every natural and ordinary roll boundary
**When** deterministic random inputs produce faces 1, 2, 8, 9, 19, and 20
**Then** the real rules engine and SQLite transaction produce the specified results, consequences, and exact-once recovery behavior
**And** the browser journey verifies pre-roll and post-roll evidence without mocking first-party mechanics.

### Story 3.5: Earn and Allocate Progression

As a player,
I want difficult successful checks to improve my character and relevant skills,
So that earned competence persists and familiar challenges become easier over time.

**Implements:** FR15, FR16, FR17

**Acceptance Criteria:**

**Given** a meaningful eligible check has actual pre-roll success probability `p`
**When** it succeeds
**Then** player XP and the relevant skill XP each receive `floor(100 × (0.95 - p) / 0.90)`
**And** the calculation uses all applicable bonuses and the recorded pre-roll probability rather than nominal difficulty or the observed die.

**Given** the controlled 60% Presence plus Persuasion check succeeds
**When** progression is awarded
**Then** the player track receives 38 XP and the Persuasion track receives 38 XP
**And** the XP award is committed atomically with the check result, consequence, elapsed time, action record, and world revision.

**Given** an eligible check has a 5% success probability
**When** it succeeds on the only successful face
**Then** the player and relevant skill tracks each receive 100 XP
**And** natural-roll handling remains part of the probability calculation.

**Given** a check has a 95% success probability
**When** it succeeds or fails only on natural 1
**Then** it awards zero player XP and zero skill XP
**And** no negative, rounded-up, consolation, or minimum award is created.

**Given** a check fails at any success probability
**When** progression is resolved
**Then** it awards zero player XP and zero skill XP
**And** the failure consequence and completed action time still commit according to the check's declared stakes.

**Given** an action is routine, rejected, unsupported, duplicated, or a retry of an already resolved request
**When** progression eligibility is evaluated
**Then** it awards zero check XP
**And** it does not create a new advancement opportunity merely because the request was phrased again.

**Given** a player or skill track starts at level 1 with 0 XP
**When** its stored XP reaches at least `100 × current level`
**Then** that threshold is consumed, the track gains one level, and excess XP carries forward
**And** the calculation repeats while enough carried XP remains for another level.

**Given** a level-1 player and level-1 Persuasion track each have 90 XP
**When** the controlled 60% check succeeds for 38 XP
**Then** each becomes level 2 with 28 XP remaining toward its next 200-XP threshold
**And** the player gains one unspent attribute point while Persuasion increases from +1 to +2.

**Given** a player level is gained
**When** rewards are committed
**Then** exactly one unspent attribute point is added for that level
**And** the point does not automatically change an attribute, starting-array assignment, affinity slot, title, achievement, or ability.

**Given** a skill level is gained
**When** rewards are committed
**Then** the corresponding skill bonus increases by exactly +1 for that level
**And** no unrelated skill, attribute, or affinity value changes.

**Given** progression crosses several thresholds in one valid award
**When** levels are calculated
**Then** every earned player level grants one attribute point and every earned skill level grants +1 to that skill
**And** level, attribute, skill bonus, and XP values are not clamped to former proposed caps.

**Given** the player returns to the difficulty-12 Persuasion task after Persuasion increases to +2 while Presence remains 14 (+2)
**When** the check is previewed again under otherwise unchanged circumstances
**Then** the total bonus is +4 and the success probability is 65%
**And** the difficulty is not raised merely to cancel earned mastery.

**Given** committed progression creates an unspent attribute point
**When** the player opens the Character Sheet
**Then** it displays player and skill levels, current XP, next thresholds, bonuses, and earned, spent, and unspent attribute-point counts
**And** the original standard-array record remains separately visible and unchanged.

**Given** the player selects an attribute increase
**When** the allocation is previewed
**Then** the Character Sheet shows the proposed score, derived modifier, and resulting earned, spent, and unspent counts before commitment
**And** inspecting or previewing the allocation advances zero fictional seconds.

**Given** the player confirms a valid one-point allocation
**When** the allocation operation commits
**Then** the chosen attribute increases by one, one unspent point becomes spent, and the persisted Character Sheet reflects the new values
**And** the allocation uses a new world revision and can be applied at most once for its request identity.

**Given** the player attempts to spend more points than are available or submits an invalid attribute
**When** the allocation is validated
**Then** the operation identifies the exact overspend or invalid target and changes nothing
**And** previously committed progression and the player's current preview remain available for correction.

**Given** an XP, level, or allocation operation is retried after commit
**When** the backend recovers the request result
**Then** the original progression and allocation outcome is returned
**And** XP, levels, skill bonuses, attribute points, and attribute increases are not duplicated.

**Given** the Character Sheet presents progression and allocation states
**When** it is used by keyboard, pointer, screen reader, zoom, or reflow
**Then** no-unspent, unspent, preview, invalid, confirmation-pending, persisted, loading, and error states are perceivable and operable
**And** changes are announced without forced focus and never communicated through color alone.

**Given** automated tests exercise 5%, 60%, 65%, and 95% checks, failures, near-threshold leveling, multiple levels, high uncapped bonuses, duplicate awards, valid allocation, and overspending
**When** they run through the real rules engine, API, and isolated SQLite store
**Then** exact XP, level, bonus, point, probability, and persistence outcomes match the confirmed formulas
**And** first-party progression and persistence are not mocked.

## Epic 4: See Consequences Travel Through People

The player can change Mara's opportunities through a gift, observe NPC plans respond to grounded constraints, and experience information passing from Tessa to Ivo as a fallible, provenance-tracked belief that affects later behavior.

### Story 4.1: Witness a Gift Without Sharing Omniscience

As a player,
I want each character to know only what they could actually perceive,
So that the world's reactions arise from situated knowledge rather than invisible omniscience.

**Implements:** FR27

**Acceptance Criteria:**

**Given** the prepared gift pouch is successfully transferred to Mara
**When** the gift transaction commits
**Then** the engine records an immutable historical fact with stable identity, event type, actors, amount, place, game time, source action, and resulting ownership
**And** the fact is distinct from every character's observation, claim, belief, and player-facing narration.

**Given** Mara directly receives the committed gift
**When** witness observations are constructed
**Then** Mara receives a separate observation linked to the gift fact and containing only details perceptible to her
**And** the observation records Mara as witness, the location, acquisition time, perceptible meaning, and applicable uncertainty.

**Given** Tessa is present and can perceive the committed handover
**When** witness observations are constructed
**Then** Tessa receives her own observation linked to the same historical fact
**And** her observation is not automatically copied to Ivo, Oren, absent NPCs, or a global shared-memory record.

**Given** the player character perceives the completed handover
**When** the result enters the transcript or known-information projection
**Then** the player receives only the perceptible gift outcome and visible witness behavior
**And** hidden interpretations, confidence values, private NPC knowledge, future claims, and planned reactions remain absent.

**Given** Ivo did not witness the gift and has received no claim about it
**When** his knowledge is queried before contact with Tessa
**Then** no observation or belief about the gift exists for Ivo
**And** his other knowledge, distrust, and relationships do not manufacture awareness of the event.

**Given** Oren or another non-witness has no supported information source
**When** consequential planning or dialogue is evaluated
**Then** the gift cannot be used as that NPC's known premise
**And** the planner cannot read historical truth directly as personal knowledge.

**Given** a witness forms an interpretation from an observation
**When** that interpretation is stored
**Then** it becomes a separate belief with its own proposition, confidence, provenance, acquisition time, and status
**And** the belief cannot alter the historical gift fact or another character's knowledge.

**Given** the gift transfer is rejected or interrupted before ownership changes
**When** causal records are committed
**Then** no completed-gift fact or completed-handover observation is created
**And** any legitimately completed time or interrupting event is recorded separately from the uncompleted transfer.

**Given** the committed gift request is redelivered with the same request identity
**When** the backend recovers the original result
**Then** it returns the existing fact and observation identities
**And** it does not create duplicate facts, witness observations, ownership changes, or elapsed time.

**Given** a knowledge record is loaded from persistence or crosses an application boundary
**When** it is validated
**Then** its stable ID, schema version, record kind, immediate source, subject, owner or witness, and game time must satisfy the correct strict typed contract
**And** invalid cross-kind references or unknown fields are rejected before domain planning receives them.

**Given** Rowan answers a player knowledge question after the gift
**When** the player asks what they know about the event or witnesses
**Then** the response is generated from the player-character knowledge projection rather than the full fact and provenance ledger
**And** Rowan plainly withholds anything the player did not perceive or subsequently learn.

**Given** operational logs and ordinary diagnostic identifiers are recorded
**When** the gift operation completes
**Then** they preserve correlation and causal record identities needed for later inspection
**And** normal logs exclude complete hidden knowledge state, private beliefs, secrets, and unrestricted provider payloads.

**Given** gift and no-gift fixtures begin from the same controlled initial state
**When** tests compare their immediate knowledge records
**Then** only the committed gift branch contains the gift fact and supported witness observations
**And** neither branch gives Ivo knowledge before a valid later transmission event.

**Given** automated tests add extra hidden NPC state without changing the player's legitimate evidence
**When** the same player-facing query and scene projection run
**Then** the visible response remains unchanged
**And** the real API and isolated SQLite store prove that player presentation is separated from authoritative hidden records.

### Story 4.2: See Mara Reconsider Her Plans

As a player,
I want Mara's choices to respond to her changed circumstances and personal obligations,
So that the gift affects a believable life rather than triggering a scripted reaction.

**Implements:** FR26, FR27, FR30

**Acceptance Criteria:**

**Given** the controlled starting state before any gift
**When** Mara's feasible plans are evaluated
**Then** they reflect her 20-gold debt to Oren, desire to clear it, desire to visit her ill sister, available resources, relationships, knowledge, location, and available time
**And** no plan may spend resources she does not own or ignore a binding obligation without a supported reason.

**Given** gift and no-gift branches begin from the same controlled initial state
**When** their feasible opportunity sets are compared
**Then** the committed 10,000-gold gift changes Mara's supported options in the gift branch
**And** the no-gift branch cannot use the gift, its observation, or resources derived from it.

**Given** Mara receives and observes the committed gift
**When** consequential replanning begins
**Then** the planner receives only Mara's actual resources, obligations, relationships, knowledge, current plan, and available time
**And** it does not receive another NPC's private beliefs or unrestricted historical truth as Mara's knowledge.

**Given** consequential replanning uses the LLM boundary
**When** a candidate plan is proposed
**Then** the proposal is strictly validated against a versioned contract before domain evaluation
**And** the LLM cannot directly change resources, obligations, schedules, relationships, facts, or authoritative plan state.

**Given** a candidate plan requires spending, travel, contact, or fulfillment of an obligation
**When** feasibility is validated
**Then** required resources, ownership, timing, route, participants, and prerequisites must be supported by current state
**And** invalid portions are rejected rather than made true through narration.

**Given** several plans are feasible after the gift
**When** Mara selects a plan
**Then** the decision may weigh clearing the debt, visiting her sister, maintaining dependable trade, retaining resources, or another supported response according to her situation
**And** the system does not require retirement, gratitude, obedience, or any single scripted outcome.

**Given** a plan is validly selected
**When** the replan commits
**Then** it records a stable plan identity, status, goals, required resources, scheduled steps, motivating knowledge, and feasibility rationale
**And** the previous plan remains available as historical evidence rather than being silently overwritten.

**Given** Mara's chosen plan includes repaying Oren or changing a trade commitment
**When** its scheduled step occurs
**Then** Oren is affected only by the actual payment, contact, or commitment he perceives
**And** Mara's private intention alone does not change Oren's resources, knowledge, or behavior.

**Given** Mara's chosen plan includes visiting her sister or changing her routine
**When** the plan advances on the shared campaign clock
**Then** the relevant schedule and location changes occur through deterministic events at supported times
**And** application downtime, LLM latency, or player reading does not advance those steps.

**Given** the player later encounters Mara or a consequence of her plan
**When** Rowan presents the scene
**Then** changed spending, fulfilled obligations, dialogue, location, or schedule provides observable evidence that her feasible life changed
**And** the interface does not expose her complete private plan, hidden motivation, or diagnostic rationale unless the player legitimately learned it.

**Given** a valid candidate cannot be produced or persistence fails before commit
**When** replanning ends unsuccessfully
**Then** Mara retains her prior authoritative plan and resources
**And** the operation records a recoverable failure without narrating a new plan as true.

**Given** a replan commits but its narration fails
**When** presentation is retried
**Then** Mara's committed plan and scheduled consequences remain authoritative
**And** only player-perceptible narration is regenerated from the committed result.

**Given** the same replanning trigger is redelivered with the same causal or request identity
**When** the engine processes it again
**Then** it recovers the existing plan decision and scheduled events
**And** it does not spend resources, replace the plan, or schedule consequences twice.

**Given** routine plan steps require no new interpretation
**When** their scheduled time arrives
**Then** deterministic rules execute them without continuously running an autonomous agent
**And** the LLM is consulted only when a consequential situation genuinely requires interpretation or replanning.

**Given** controlled provider fixtures propose retirement, debt repayment plus a sister visit, investment, or an infeasible plan
**When** integration tests evaluate each proposal
**Then** every accepted outcome is grounded in Mara's actual state and every infeasible outcome is rejected without mutation
**And** success is measured by changed feasible options and observable motivated behavior rather than a required narrative script.

### Story 4.3: Let News Travel Through Contact

As a player,
I want news to reach NPCs only through actual encounters and communicated claims,
So that reputation travels through people rather than appearing everywhere automatically.

**Implements:** FR27, FR28

**Acceptance Criteria:**

**Given** the controlled scenario records the gift-opportunity game second
**When** the scenario initializes its schedule
**Then** Tessa and Ivo's Common Room meeting is due exactly 1,800 seconds after that opportunity
**And** the meeting remains scheduled whether or not the player ultimately gives Mara the gift.

**Given** the campaign clock reaches the scheduled meeting time
**When** routine NPC movement and schedules are processed
**Then** the encounter exists only if Tessa and Ivo are actually present in the Common Room under the resolved world state
**And** an LLM estimate cannot manufacture their contact or move either NPC outside validated plans and travel time.

**Given** the gift was committed and Tessa observed it
**When** Tessa and Ivo meet and Tessa has a supported motive to report it
**Then** she may communicate a claim derived from her own observation
**And** the claim cannot contain gift details that she did not perceive or legitimately learn.

**Given** Tessa communicates the baseline gift report
**When** the claim commits
**Then** it records a stable claim identity, speaker, listener, encounter, communicated proposition, immediate observation source, disclosed source, game time, and truth relationship
**And** it remains distinct from the historical gift fact and Tessa's observation.

**Given** Ivo has not yet received the claim
**When** his knowledge is inspected immediately before the encounter
**Then** he has no observation, claim receipt, or belief about the gift
**And** his friendship with Tessa or distrust of the player does not create knowledge without transmission.

**Given** Ivo is present and receives Tessa's committed claim
**When** belief updating runs
**Then** Ivo receives a separate belief linked to the claim and encounter with its proposition, confidence, provenance, acquisition time, and status
**And** the new belief does not rewrite the original fact, Tessa's observation, or Ivo's prior belief history.

**Given** the gift did not occur in the matched no-gift branch
**When** Tessa and Ivo's scheduled meeting occurs
**Then** the encounter still commits at its actual time
**And** no firsthand gift report may be derived from a nonexistent gift fact or observation.

**Given** Tessa or Ivo is absent, the encounter is interrupted, Tessa lacks the observation, or no supported claim is communicated
**When** transmission is evaluated
**Then** Ivo receives no gift belief from that attempted delivery
**And** the historical gift and any existing witness observations remain unchanged.

**Given** a claim transmission fails after the encounter but before the belief update commits
**When** recovery occurs
**Then** the transaction preserves only records that reached their documented atomic boundary
**And** it does not erase the gift, fabricate receipt, or leave an unproven belief attached to Ivo.

**Given** the same transmission is redelivered with the same transmission or request identity
**When** the engine recovers it
**Then** it returns the existing claim and belief-update result
**And** it does not duplicate the encounter, claim, belief history, elapsed time, or replanning trigger.

**Given** Tessa genuinely repeats the report during a later distinct encounter
**When** that communication is supported
**Then** it may create a new claim event with its own time and provenance
**And** retry deduplication does not erase legitimate repeated social contact.

**Given** the player is not present and has not learned about the Common Room conversation
**When** the off-screen meeting and transmission occur
**Then** the event advances NPC knowledge without adding its private contents to the player transcript or Journal
**And** Rowan continues to answer player questions only from the player-character knowledge projection.

**Given** the player legitimately witnesses or later receives evidence of the encounter
**When** the event becomes player-facing
**Then** Rowan may present only the perceptible or transmitted information the player learned
**And** hidden confidence calculations, private beliefs, and future actions remain concealed.

**Given** the scheduler processes the contact and transmission
**When** causal evidence is recorded
**Then** the encounter, claim, belief update, processed scheduled event, world revision, and state hash remain traceable through stable identifiers
**And** ordinary logs preserve correlation without exposing complete hidden knowledge content.

**Given** gift and no-gift branches start from matching fixtures and advance to the meeting
**When** integration tests compare them before and after 1,800 seconds
**Then** both contain the scheduled encounter when attendance conditions hold, only the gift branch can contain the supported firsthand gift claim, and Ivo knows nothing before receipt
**And** the real scheduler, API, and isolated SQLite store prove contact-dependent propagation without mocked first-party behavior.

### Story 4.4: Experience a Doubted or Distorted Rumor

As a player,
I want NPCs to interpret reports through their own trust and prior beliefs,
So that reputation can distort and influence behavior without replacing historical truth.

**Implements:** FR27, FR29, FR30

**Acceptance Criteria:**

**Given** the controlled rumor variant is enabled and Tessa witnessed the gift
**When** she reports it to Ivo during their valid Common Room encounter
**Then** her claim may state that the gift occurred and suggest that it bought influence
**And** the suggestion is represented as Tessa's communicated interpretation rather than an established historical fact.

**Given** the ordinary baseline scenario is running instead of the rumor variant
**When** Tessa reports the gift
**Then** the claim is not automatically changed into an influence allegation
**And** the game does not produce the same slander or distortion on every playthrough.

**Given** Tessa communicates the influence claim
**When** the claim record commits
**Then** it preserves the observed gift details separately from the inferred motive or social meaning
**And** its source observation, speaker, listener, encounter, disclosed source, time, and uncertainty remain traceable.

**Given** Ivo receives the influence claim
**When** his belief update is evaluated
**Then** his existing distrust of the player, relationship with Tessa, prior beliefs, disclosed source, and claim uncertainty affect his confidence
**And** the engine does not copy Tessa's interpretation into Ivo as certain knowledge.

**Given** Ivo doubts the influence claim
**When** his next feasible plan is selected
**Then** he seeks supported confirmation before favoring the player on the basis of that claim
**And** doubt does not erase his memory that Tessa made the report.

**Given** Ivo's belief triggers consequential replanning
**When** an LLM proposes a response
**Then** the rules validate the proposal against Ivo's own knowledge, resources, relationships, obligations, location, and available time
**And** the LLM cannot compel favor, hostility, confirmation, or any unsupported action.

**Given** Ivo later encounters the player or another valid source of evidence
**When** he acts on the uncertain belief
**Then** an observable question, verification attempt, withheld favor, or other supported choice demonstrates that the report affected behavior
**And** the player-facing scene does not reveal Ivo's numeric confidence, complete hidden plan, or facts the player has not learned.

**Given** Ivo receives confirming, contradicting, or incomplete evidence later
**When** his belief is updated
**Then** the new belief state records the evidence and immediate provenance while preserving the prior claim and belief history
**And** neither correction nor continued doubt rewrites the original gift fact.

**Given** Ivo believes an inaccurate interpretation
**When** planning or dialogue uses that belief
**Then** the belief may influence his supported choices without making the interpretation historically true
**And** authoritative ownership, events, and other characters' knowledge remain unchanged.

**Given** Ivo receives a truthful claim but disbelieves it
**When** his confidence remains insufficient for action
**Then** the historical truth remains committed and his belief accurately records doubt
**And** the game does not force belief merely because the source claim is true.

**Given** Tessa conceals uncertainty, exaggerates, or communicates incompletely within the controlled variant
**When** the claim is validated
**Then** the record preserves what she communicated and its relationship to her actual observation
**And** her speech cannot introduce event details or mechanics unsupported by her knowledge.

**Given** the rumor delivery, belief update, or replan fails before commit
**When** recovery occurs
**Then** earlier committed facts, observations, encounters, and claims remain intact at their documented boundaries
**And** the game does not fabricate Ivo's belief or later action.

**Given** the same claim, belief update, or replan is redelivered with the same identity
**When** the engine recovers it
**Then** the existing causal result is returned
**And** no duplicate belief history, verification plan, schedule, elapsed time, or observable consequence is created.

**Given** the player has no evidence of the rumor or Ivo's reaction
**When** the transcript, Journal, Character Sheet, Inventory, or Rowan knowledge answer is projected
**Then** those surfaces omit the private claim, belief, confidence, and plan
**And** development-only access remains unavailable unless capability-gated diagnostics are enabled later.

**Given** the player legitimately observes Ivo's later behavior
**When** Rowan narrates the consequence
**Then** narration describes only the visible words and actions backed by the committed plan and current scene
**And** it does not state hidden motives as known facts or claim that narration itself caused the behavior.

**Given** controlled tests compare baseline, rumor, no-contact, no-gift, confirming-evidence, and contradicting-evidence variants
**When** the real scheduler, belief updater, planner, API, and isolated SQLite store execute them
**Then** each resulting action is traceable through fact, observation, claim, belief, and plan records without any record type rewriting another
**And** the rumor variant demonstrates changed later behavior while preserving the original event and player-information boundary.

## Epic 5: Preserve and Verify a World That Remembers

The player can save, resume, branch, and replay the complete causal world, including facts, beliefs, plans, events, and progression. The prototype owner can then demonstrate the P0 evidence gate through inspectable diagnostics and controlled fixtures.

### Story 5.1: Save a Complete Campaign

As a player,
I want to save my complete campaign into one of three clear manual slots,
So that I can preserve the exact world branch and return to it safely.

**Implements:** FR35, FR36

**Acceptance Criteria:**

**Given** a confirmed campaign is active
**When** the player opens Save Selection
**Then** exactly three manual save slots are displayed
**And** opening, reading, or closing the overlay advances zero fictional seconds and changes no game state.

**Given** a save slot is empty
**When** it is displayed
**Then** its empty status and slot identity are explicit
**And** the interface does not invent campaign, character, place, time, or progress metadata.

**Given** a save slot is occupied
**When** it is displayed
**Then** it shows slot identity, campaign or character context, current place, in-world time, and saved-at wall-clock time
**And** selection is communicated through text and boundary changes rather than color alone.

**Given** the player chooses an empty slot
**When** the save operation begins
**Then** the interface shows a truthful saving state associated with that slot
**And** the composer, transcript, and authoritative campaign remain intact while the snapshot is written.

**Given** the player chooses an occupied slot
**When** they request a save
**Then** the interface shows the existing slot context and requires explicit overwrite confirmation
**And** cancelling confirmation preserves the existing slot without creating a snapshot or advancing fictional time.

**Given** a save captures the complete committed branch
**When** the snapshot is constructed
**Then** it includes the campaign clock, transcript and known state, character facts and confirmed premises, ownership, money, inventory, locations, relationships, obligations, commitments, historical facts, observations, claims, beliefs, NPC plans, scheduled events and insertion order, XP, levels, skill bonuses, starting attributes, allocated and unspent points, request and action evidence, and applicable reward records
**And** it excludes uncommitted proposals, browser-only presentation state, secrets, unrestricted provider payloads, and abandoned-branch state.

**Given** a mutating operation is still in flight
**When** the player saves
**Then** the snapshot represents one identified, fully committed world revision rather than partial pending effects
**And** pending operation state remains recoverable through the operation store without masquerading as committed world state.

**Given** a complete snapshot is ready
**When** it is persisted
**Then** canonical versioned state, branch ID, schema version, content version, world revision, state hash, and timestamps are written transactionally as an immutable snapshot
**And** the slot pointer changes only after the new snapshot and integrity metadata have committed successfully.

**Given** a save completes successfully
**When** the slot refreshes
**Then** its displayed metadata matches the saved authoritative revision and snapshot
**And** saving does not heal the character, restore items, change NPC state, advance time, or increment the campaign's world revision.

**Given** an overwrite operation fails before the new snapshot commits
**When** the failure is presented
**Then** the previous slot snapshot and pointer remain durable and loadable
**And** the player receives a specific retry path and safe correlation identifier.

**Given** snapshot validation detects a missing causal dependency, incompatible schema, content mismatch, or hash failure
**When** saving is attempted
**Then** the save is rejected without replacing the occupied slot
**And** the error identifies the affected compatibility or integrity category without exposing complete hidden state.

**Given** the same save request is redelivered with the same request identity
**When** the backend recovers it
**Then** it returns the existing snapshot and slot result
**And** it does not create duplicate snapshots, change the slot twice, or alter campaign state.

**Given** save metadata or state crosses a persistence or API boundary
**When** it is loaded or returned
**Then** strict versioned validation occurs before application or frontend logic accepts it
**And** invalid JSON fields, identifiers, enum values, or timestamps produce a typed safe failure.

**Given** Save Selection is loading, saving, confirming overwrite, complete, or failed
**When** its state changes
**Then** the update is visible and politely announced without moving focus
**And** the overlay preserves its accessible name, contained focus, Escape and explicit close behavior, focus return, viewport bounds, internal scrolling, and no-stacking rule.

**Given** save performance is measured on the documented P0 test machine
**When** representative complete branch snapshots are written
**Then** elapsed time and snapshot size are recorded against the provisional two-second target
**And** a missed target is reported as measurement evidence rather than hidden or declared successful.

**Given** automated tests exercise every slot, overwrite confirmation, cancellation, in-flight operation state, complete snapshots, validation failure, write failure, duplicate delivery, and integrity metadata
**When** they run against the real API and isolated SQLite store
**Then** each successful snapshot contains every required causal dependency and each failure preserves the prior durable slot
**And** browser tests verify the complete accessible manual-save flow without mocked first-party persistence.

### Story 5.2: Load and Continue an Isolated Branch

As a player,
I want to load a saved campaign branch with its complete history intact,
So that I can continue from that exact world without state leaking from another path.

**Implements:** FR36, FR37

**Acceptance Criteria:**

**Given** at least one valid manual save exists
**When** the Title save-index request succeeds
**Then** Continue becomes available and communicates that saves can be selected
**And** no save is loaded automatically merely because it exists.

**Given** the player activates Continue
**When** Save Selection opens
**Then** each occupied slot displays its campaign or character, place, in-world time, and saved-at context
**And** the player can distinguish branches without seeing hidden simulation details.

**Given** the player chooses an occupied slot
**When** loading begins
**Then** the interface identifies the selected slot and shows a truthful loading state
**And** the currently active campaign remains available until the target snapshot has been validated and restored successfully.

**Given** a snapshot belongs to the current supported schema and content versions
**When** the backend loads it
**Then** canonical state validation, content-reference validation, and state-hash verification complete before it becomes active
**And** invalid or incomplete state cannot reach domain logic or the browser as a successful load.

**Given** a snapshot uses a supported historical world-state version
**When** it is loaded
**Then** explicit ordered typed migration functions transform it to the current version and validate the result
**And** fixtures for that historical version prove no required causal dependency is silently dropped or invented.

**Given** a snapshot uses an unsupported schema or content version, contains an invalid reference, or fails its integrity hash
**When** loading is attempted
**Then** the operation fails safely with the precise compatibility or integrity category
**And** the prior active campaign and saved slot remain unchanged and usable.

**Given** a valid snapshot is restored
**When** the loaded branch becomes active
**Then** its clock, transcript, player-known state, character facts and premises, ownership, money, inventory, locations, relationships, obligations, commitments, facts, observations, claims, beliefs, NPC plans, scheduled events and insertion order, XP, levels, bonuses, starting attributes, allocated and unspent points, action evidence, request results, and applicable reward records match the saved revision
**And** the resulting authoritative state hash matches the validated restored state.

**Given** the loaded branch contains hidden NPC knowledge, beliefs, plans, or scheduled events
**When** the Main Notebook renders after restoration
**Then** those records influence simulation but remain excluded from player-facing projections unless the character legitimately knows them
**And** the transcript, Journal, Character Sheet, and Inventory show only their authorized views.

**Given** the player loads an older save from before a gift, check, level, allocation, report, or NPC replan
**When** that branch becomes active
**Then** none of the later branch's money changes, knowledge, rewards, rolls, progression, elapsed time, or social consequences carry into it
**And** the abandoned branch's records remain associated only with that branch or its own saves.

**Given** the player continues from a loaded older snapshot
**When** new actions commit
**Then** they advance an isolated branch from the loaded revision without modifying the immutable source snapshot
**And** the player can later return to another saved branch without merging their histories.

**Given** a save is loaded
**When** its campaign view replaces the prior active view
**Then** TanStack Query replaces or invalidates affected authoritative server-state caches rather than merging world objects in the browser
**And** presentation-only preferences may remain without carrying authoritative campaign state.

**Given** a load succeeds
**When** the restored Main Notebook becomes ready
**Then** it reports the restored place and in-world time and preserves the branch's transcript context
**And** loading itself advances zero fictional seconds, creates no roll or XP, restores no consumed resources beyond the snapshot, and performs no per-action undo.

**Given** the same load request is redelivered with the same request identity
**When** the backend recovers it
**Then** it returns the existing loaded-branch result
**And** it does not create duplicate branches, replay actions, process scheduled events, or change the clock again.

**Given** persistence or presentation fails after the target snapshot validates but before activation completes
**When** recovery occurs
**Then** activation is atomic and leaves either the prior branch or the fully restored target branch authoritative
**And** the interface states which branch remains active with a safe retry and correlation identifier.

**Given** Save Selection or the restored Main Notebook is operated by keyboard, pointer, screen reader, zoom, or reflow
**When** the player selects, loads, closes, or resumes
**Then** selection, progress, failure, active branch context, focus, and status announcements remain perceivable and operable
**And** no information relies on hover or color alone.

**Given** load performance is measured on the documented P0 test machine
**When** representative complete branch snapshots are restored
**Then** validation, migration, activation, and render timing are recorded against the provisional two-second target
**And** a missed target remains visible measurement evidence rather than being omitted.

**Given** controlled branches diverge through gift/no-gift, rumor, progression, and time changes
**When** automated tests alternate saving and loading them
**Then** every loaded state matches its own snapshot with no cross-branch carryover and no lost causal records
**And** the tests use the real API, migration path, SQLite store, and browser flow without mocked first-party persistence.

### Story 5.3: Replay Reproducible Mechanical Outcomes

As a prototype owner,
I want to replay captured actions from recorded state and inputs,
So that I can reproduce mechanical outcomes and diagnose contradictions without relying on identical LLM prose.

**Implements:** FR38

**Acceptance Criteria:**

**Given** an action reaches authoritative resolution
**When** replay evidence is captured
**Then** it records the initial state identity and hash, schema and content versions, expected world revision, validated structured proposal, clarification contract when applicable, recorded identifiers, random inputs, timed phases, and relevant scheduler state
**And** it excludes secrets and does not require unrestricted raw provider output to reproduce mechanics.

**Given** a compatible replay bundle is selected
**When** replay begins
**Then** the bundle and initial state are strictly validated before any rule executes
**And** missing inputs, unknown fields, invalid references, incompatible versions, or a mismatched initial hash stop replay with a typed diagnostic failure.

**Given** replay inputs are valid
**When** the action is executed
**Then** it runs in an isolated replay context rather than mutating an active campaign, manual save, or immutable source snapshot
**And** no player-visible branch, operation, time, resource, XP, or knowledge state changes.

**Given** a captured movement action is replayed
**When** the same route, movement mode, starting clock, and proposal are applied
**Then** destination, elapsed seconds, processed events, resulting revision, and canonical state hash match the original mechanics
**And** fresh narration is not part of the equality requirement.

**Given** a captured purchase or gift action is replayed
**When** the same initial ownership, stock, duration, witness state, and proposal are applied
**Then** funds, quantities, ownership, time, gift fact, and supported observations match the original committed result
**And** recorded identifiers are reused or deterministically mapped so identity generation cannot create a false divergence.

**Given** a captured uncertain check is replayed
**When** the recorded difficulty, modifiers, probability, stakes, and random input are applied
**Then** the die, total, success or failure, committed consequence, and elapsed time match the original result
**And** no new random sample or post-roll difficulty change occurs.

**Given** a captured successful check includes progression
**When** replay resolves its XP and level effects
**Then** XP awards, carried XP, levels, skill bonuses, unspent points, allocations, revision, and state hash match the original result
**And** the award is computed from the recorded pre-roll probability rather than regenerated narration.

**Given** a captured timed action crosses scheduled events
**When** replay processes the event queue
**Then** due time, priority, insertion sequence, interruptions, completed phases, and emitted causal records match the original
**And** event handlers use the same recorded random inputs and bounded processing rules.

**Given** an NPC replan or belief update originally used a validated LLM proposal
**When** its mechanics are replayed
**Then** the recorded validated proposal is supplied directly to deterministic validation and commit logic
**And** replay does not call the provider again or ask a new model to recreate the decision.

**Given** narration is requested after mechanical replay
**When** a narrator produces new text from the reproduced committed facts
**Then** the prose may differ from the original while remaining constrained to the same player-perceptible result
**And** narration cannot change the replayed mechanics, equality result, or state hash.

**Given** the replayed result matches the original
**When** comparison completes
**Then** the report confirms matching authoritative state, domain events, action outcome, causal record identities, revisions, and canonical state hash
**And** it distinguishes mechanically relevant equality from wall-clock, transport, logging, or prose differences.

**Given** replay diverges from the original
**When** comparison detects the first mismatch
**Then** the report identifies the earliest differing rule input, validation decision, event, mutation, revision, or hash path
**And** it does not mask the divergence by accepting a later coincidental final value.

**Given** a historical replay bundle requires a supported migration
**When** replay prepares the initial state
**Then** the same explicit typed migration path used by save loading is applied and recorded
**And** the report distinguishes migration effects from rule-execution differences.

**Given** a replay request is repeated or interrupted
**When** it resumes or runs again
**Then** each isolated execution starts from the same validated initial state and produces an independent report
**And** it never appends duplicate evidence to the original action or changes live state.

**Given** replay data contains hidden NPC knowledge or private provider-derived proposals
**When** results are presented outside capability-gated development diagnostics
**Then** only player-safe identifiers and permitted summary information are exposed
**And** hidden facts, beliefs, plans, prompts, and unrestricted provider data remain protected.

**Given** automated tests replay movement, waiting, purchase, gift, check success and failure, progression, attribute allocation, report transmission, belief change, and NPC replanning
**When** they run against the real deterministic rules and isolated SQLite replay store
**Then** all mechanical outcomes and hashes reproduce from captured inputs without first-party mocks
**And** a changed rule fixture deliberately produces a precise, test-verified divergence report.

### Story 5.4: Inspect Causal Evidence Safely

As a prototype owner,
I want read-only causal diagnostics and redacted evidence exports,
So that I can explain surprising outcomes without exposing hidden information or changing the game.

**Implements:** FR39

**Acceptance Criteria:**

**Given** a player-facing action is pending, completed, rejected, or interrupted
**When** its status is displayed
**Then** the player can see a truthful state, appropriate recovery guidance, and a safe correlation identifier
**And** uncertain checks expose their declared difficulty, modifiers, probability, roll, total, and outcome without revealing hidden NPC state.

**Given** a campaign is active
**When** the player opens permitted system information
**Then** they can inspect save-integrity status, application and schema versions, and player-safe diagnostic summaries
**And** these views do not expose secrets, hidden objectives, private beliefs, unrevealed events, or complete authoritative state.

**Given** development diagnostics are requested
**When** the backend is bound only to a loopback interface and `DMUD_DEVTOOLS=true`
**Then** the backend exposes a typed development-capability response and read-only diagnostic routes
**And** the frontend enables its development inspector only from that authoritative capability response.

**Given** the backend is remotely accessible or `DMUD_DEVTOOLS` is absent or false
**When** diagnostic capabilities are evaluated
**Then** development-only routes are unavailable or forbidden and their interface controls are absent
**And** frontend build mode alone cannot enable them.

**Given** an authorized developer inspects an action
**When** its causal record is available
**Then** the inspector shows its submitted intent, validated proposal, clarification contract, rules decisions, rejected alternatives, random input and result, committed change set, revisions, state hashes, narration status, and correlated logs
**And** every displayed relationship uses stable causal identifiers.

**Given** facts, observations, claims, beliefs, plans, commitments, or scheduled events contributed to an outcome
**When** the developer follows its causal chain
**Then** the inspector shows each record's source, subject, observer or holder, creation time, confidence or status, and downstream effects
**And** it distinguishes direct observation, reported information, inference, and private planning.

**Given** an NPC changes a belief or plan
**When** the developer inspects that transition
**Then** the view identifies the relevant knowledge, resources, commitments, opportunities, constraints, prior plan, validated proposal, and resulting plan
**And** absent evidence is reported as unavailable rather than replaced with a fabricated explanation.

**Given** a timed action or wait processes scheduled work
**When** its timeline is inspected
**Then** the world clock, action phases, event due times, priorities, insertion order, interruptions, resumptions, and resulting mutations are visible
**And** the ordering matches the authoritative event and action records.

**Given** two branches or revisions are compared
**When** the developer requests a diagnostic difference
**Then** the inspector reports changes in canonical state hashes, authoritative records, causal identities, and operation timelines
**And** it does not treat narration, transport metadata, or incidental log formatting as mechanical state differences.

**Given** an LLM-assisted operation is inspected
**When** provider evidence exists
**Then** diagnostics report the model, provider, prompt and contract versions, latency, token usage, estimated session cost, retries, validation rejections, and contradiction repairs
**And** unrestricted prompts and raw provider payloads remain confined to authorized local development diagnostics.

**Given** diagnostic data is queried
**When** the request executes
**Then** it uses read-only application paths and database transactions
**And** no inspector control can mutate state, inject random seeds, alter evidence, execute replay into a live branch, or bypass game rules.

**Given** a player-safe evidence bundle is exported
**When** export validation succeeds
**Then** the versioned bundle contains permitted action summaries, roll evidence, integrity metadata, causal identifiers, and redacted structured logs
**And** it excludes credentials, secrets, unrestricted provider content, hidden NPC state, unrevealed events, and complete save snapshots.

**Given** an export contains a forbidden field or fails versioned validation
**When** download is requested
**Then** the export is rejected with a typed safe error
**And** no partial unredacted artifact is produced.

**Given** structured operational logs are written
**When** an action crosses browser, API, domain, persistence, scheduler, or provider boundaries
**Then** rotating JSONL logs and the local development console preserve correlation, operation, campaign, branch, action, revision, and causal identifiers
**And** logs remain supporting evidence rather than replacing the authoritative action record.

**Given** diagnostic evidence is missing, corrupt, incompatible, or inaccessible
**When** a view or export requests it
**Then** the interface identifies the unavailable evidence category and offers a safe recovery path where possible
**And** it never synthesizes a causal chain or exposes unrelated records.

**Given** diagnostics are used with keyboard navigation, screen readers, zoom, or reflow
**When** the user explores filters, timelines, details, and exports
**Then** controls, relationships, status changes, and errors remain perceivable and operable without hover or color alone
**And** focus order and announcements remain stable.

**Given** automated tests exercise every capability combination, causal view, branch comparison, export, redaction rule, and failure path
**When** they run against the real API and isolated SQLite store
**Then** diagnostics remain read-only, hidden state remains protected, and displayed chains match authoritative evidence
**And** attempts to enable remote development diagnostics or export forbidden data fail safely.

### Story 5.5: Demonstrate the P0 Causal-World Proof

As a prototype owner,
I want a controlled end-to-end proof of the P0 experience,
So that I can determine whether the world is mechanically coherent, causally explainable, and believable enough to continue development.

**Implements:** FR40

**Acceptance Criteria:**

**Given** the documented P0 content, rules, versions, and test environment
**When** an evaluation run begins
**Then** the system records the build, schema and content versions, initial snapshot identity and hash, provider configuration, machine profile, and scenario fixtures
**And** P1, P2, and other future proposals are excluded from the proof.

**Given** two branches begin from the same validated initial snapshot
**When** one branch gives Mara the coin pouch and the other does not
**Then** only the gift branch transfers the prepared pouch, deducts exactly 100 coins, advances five seconds, creates the gift fact and witness observations, and permits Mara's later opportunity-driven reconsideration
**And** both branches preserve money and item conservation without duplicate ownership.

**Given** Mara later changes a plan in the gift branch
**When** the causal evidence is reviewed
**Then** the explanation traces from Rowan's action through Mara's observation, belief or disposition, available resources and opportunity, validated proposal, and committed plan
**And** the comparison branch shows no equivalent unsupported change.

**Given** Rowan attempts the controlled persuasion scenario with Presence 14, Persuasion +1, and DC 12
**When** the check is declared
**Then** the interface shows a +3 total modifier and 60% success probability before the roll
**And** the target, modifiers, probability, stakes, and reward basis cannot change after randomness is sampled.

**Given** controlled check fixtures cover ordinary results and natural 1 and natural 20
**When** they resolve
**Then** the recorded die, total, success or failure, consequence, elapsed time, and any successful-check XP match the approved rules
**And** failure, duplicate delivery, and a pre-roll probability of 95% award zero XP.

**Given** successful checks cross or approach progression thresholds
**When** rewards are applied
**Then** XP carries across levels, each skill level grants +1 to that skill, each player level grants one allocatable attribute point, and the next threshold is `100 × current level`
**And** bonuses remain uncapped and make the same unchanged task mechanically easier in later checks.

**Given** Tessa directly receives or witnesses information that Ivo does not know
**When** the controlled social chain begins
**Then** Tessa's knowledge has direct provenance and Ivo has no omniscient copy
**And** Ivo can learn only through a supported contact or report event.

**Given** Tessa reports the information to Ivo
**When** transmission resolves
**Then** the claim records its source, content, time, participants, and causal relationship to Tessa's knowledge
**And** Ivo may believe, doubt, or distort it according to his supported evidence and state rather than automatically accepting a world fact.

**Given** Ivo later acts on, questions, or repeats the report
**When** his behavior is inspected
**Then** the resulting belief and plan are traceable to the transmitted claim and his own context
**And** the player-facing narration reveals only what Rowan could legitimately perceive.

**Given** timing variants are exercised
**When** Rowan walks, jogs, sprints, or crawls on the authored routes; speaks 2 versus 31 rendered words; transfers a prepared pouch versus counting 100 loose coins; or waits one minute versus through an overnight scheduled event
**Then** elapsed time follows the approved movement, conversation, handling, and scheduler rules with segment rounding
**And** rejected commands, clarification, retries, and duplicate deliveries advance zero fictional time.

**Given** scheduled events fall before, during, or at the end of a timed action
**When** the action resolves
**Then** event ordering, priority, insertion sequence, interruptions, phase completion, and resumptions remain deterministic and causally recorded
**And** no due event is silently skipped or processed twice.

**Given** representative branches have accumulated gifts, purchases, checks, progression, beliefs, plans, reports, and scheduled events
**When** they are saved, loaded, continued, and replayed
**Then** each restored branch preserves its complete isolated authoritative state and hidden causal history
**And** replay reproduces its mechanical outcomes and canonical hashes without requiring identical narration.

**Given** any exercised scenario violates conservation, isolation, timing, declared-roll integrity, information provenance, save integrity, or replay equality
**When** evaluation results are calculated
**Then** the affected scenario fails and links to the earliest available divergence or causal evidence
**And** the contradiction cannot be waived merely because the narration sounds plausible.

**Given** the P0 endurance profile is run for 60 in-world or evaluation minutes as documented, approximately 100 representative actions, and four active NPCs
**When** measurement completes on the documented test machine
**Then** the report records latency distributions, provider tokens and estimated cost, memory behavior, retries, validation failures, contradiction repairs, save and load timing, and action throughput
**And** provisional targets are reported as measured evidence rather than silently converted into release guarantees.

**Given** the causal scenarios are demonstrated to the designated prototype evaluator
**When** qualitative feedback is recorded
**Then** mechanical causality and subjective believability are assessed separately
**And** the evaluator can identify why Mara reconsidered, why Ivo did or did not know something, and what produced each check and progression result.

**Given** the evaluation interface is used by keyboard, pointer, screen reader, zoom, or reflow
**When** the evaluator runs scenarios and reads their results
**Then** controls, progress, outcomes, failures, comparisons, and evidence links remain perceivable and operable
**And** no required conclusion depends on hover, color alone, or access to hidden player-forbidden information.

**Given** the proof suite completes
**When** its final artifact is generated
**Then** it contains scenario results, deterministic assertions, branch and replay hashes, performance measurements, qualitative observations, known limitations, failures, and evidence links
**And** it makes a clear P0 proceed, revise, or stop recommendation without claiming evidence for excluded future scope.

**Given** automated verification executes the proof suite
**When** deterministic scenarios run
**Then** they use the real browser, API, domain rules, scheduler, migrations, and isolated SQLite persistence with controlled LLM fixtures
**And** an optional separately labeled real-provider evaluation may assess prose and proposal quality without replacing deterministic acceptance results.
