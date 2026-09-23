---
stepsCompleted: [1, 2, 3, 4]
inputDocuments:
  - _bmad-output/planning-artifacts/briefs/brief-dmud-2026-09-05/brief.md
  - _bmad-output/planning-artifacts/briefs/brief-dmud-2026-09-05/addendum.md
  - _bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/gdd.md
  - _bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/decision-log.md
  - _bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/epics.md
  - _bmad-output/game-architecture.md
  - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/DESIGN.md
  - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md
  - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/reconcile-brief.md
  - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/reconcile-gdd.md
  - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/review-rubric.md
  - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/review-accessibility-text-resizing.md
  - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/validation-report.md
reviewEvidence:
  - _bmad-output/planning-artifacts/implementation-readiness-report-2026-09-22.md
  - _bmad-output/planning-artifacts/implementation-readiness-report-2026-09-23.md
  - _bmad-output/planning-artifacts/implementation-readiness-report-2026-09-23-p0.md
  - _bmad-output/planning-artifacts/p0-story-dependency-review-2026-09-23.md
---

# dmud - Epic Breakdown

## Overview

The September 22 readiness review prompted a P0 story-scope revision; the [September 23 readiness report](./implementation-readiness-report-2026-09-23.md) identified sequencing and sizing defects in that revision. The [focused P0 readiness report](./implementation-readiness-report-2026-09-23-p0.md) then found an incomplete early action path and two ownership gaps. Epics 1–2 below put a completed authored walk before action extensions, assign the shared Session 0 input when answers first need it, and give the payment obligation and gift opportunity explicit fixture ownership. Their stage-wide evidence lives in [P0 Verification and Exit Plan](./p0-verification-and-exit-plan.md). Epics 3–11 remain conditional design backlog and require their phase-specific UX contract, prior evidence gate, and another story-scope review before implementation. The reports are review evidence, not governing requirement sources. The architecture's canonical file remains `_bmad-output/game-architecture.md`; `planning-artifacts/game-architecture.md` is a discovery symlink to that same file.

This document tracks the GDD, UX Design, and Architecture requirements through P0 implementation stories and conditional later-stage design stories.

The September 23 findings are addressed at these story boundaries:

| Finding | Revised location |
| --- | --- |
| Q1 — Session 0 operation dependency | 1.3 precedes 1.5–1.10; 1.14–1.18 extend the same operation contract for world actions. |
| Q2 — starting-world content dependency | 1.4 validates the authored fixture before 1.9 confirms it; 1.19 adds exploration. |
| Q3 — gift observation dependency | 2.3 owns fact and witness capture before gift Story 2.4; 2.6–2.9 add contact, claims, beliefs, and downstream choices. |
| Q4 — Title load dependency | 1.2 owns Title/New Game and empty/error states; 1.31 adds occupied-slot selection and load. |
| Q5 — action lifecycle dependency | 1.14 completes an authored walk end to end; 1.15–1.18 extend that working action with interruption, clarification, declared costs, and narration replay. |
| Q6 — foundation and recovery size | 1.1 is the runnable shell, 1.35 owns production packaging and full quality gates; 1.3, 1.15, 1.18, and 1.31 split recovery by subject and commit boundary. |
| P0 Q2 — early input ownership | 1.5 owns the one shared composer, submission keys, and truthful Session 0 status; 1.12 carries it into the Main Notebook and adds overlays. |
| P0 Q3 — payment obligation | 1.4 seeds the minimal Mara-to-Oren debt and deadline; 1.24 changes that same record; 2.1 enriches the people around it. |
| P0 minor — gift-opportunity clock | 2.4 records the same authored opportunity marker after the shared route in both branches; 2.6 schedules contact from that marker. |

## Requirements Inventory

### Functional Requirements

#### P0 — Causal-world proof (authorized initial implementation)

FR1: The application shall present New Game and Continue immediately on startup, keep New Game usable during save-index failure, and make Continue open a three-slot selector only when compatible saves exist.

FR2: New Game shall create a durable, zero-fictional-time Session 0 draft in which Rowan asks for the character's name, origin, cares, hates, especially cool ideas, and campaign hopes, while offering creative suggestions only when explicitly requested.

FR3: Session 0 shall preserve exact submitted answers and distinguish player-authored character facts, agreed campaign premises, player preferences, and non-binding story hopes.

FR4: Session 0 shall let the player assign 8, 10, 12, 13, and 14 exactly once across Body, Agility, Constitution, Mind, and Presence, with precise validation for missing, duplicate, unknown, or out-of-array assignments.

FR5: Rowan shall reflect the current character draft for correction, and any edit shall invalidate a stale reflection until a new review is produced.

FR6: Explicit confirmation shall atomically create one immutable character origin and one initial branch at Market Square at day 1, 08:00, without advancing time or predetermining any NPC decision, route, success, or campaign outcome.

FR7: The player shall submit ordinary free-text intentions through one composer for Rowan questions, in-world speech, and actions, with synonyms supported and no required MUD command syntax.

FR8: The system shall neutrally clarify ambiguity, rare-resource spending, or materially changed intent before commitment, preserving the player's intent without suggesting a tactic or preferred action.

FR9: Every consequential action shall follow an interpret/propose → validate → resolve → commit → narrate lifecycle in which the rules, not the LLM or client, own authoritative state.

FR10: Routine feasible actions shall succeed without a roll, impossible or unsupported intentions shall be factually rejected without time or mutation, and eligible uncertain actions shall declare knowable interpretation, stakes, costs, difficulty, and consequences before resolution.

FR11: Eligible checks shall use natural 1 automatic failure, natural 20 automatic success, and otherwise `d20 + attribute modifier + relevant skill bonus >= difficulty`, with difficulty fixed before rolling and probability calculated from actual successful faces.

FR12: The controlled payment-extension fixture shall support Presence 14 (+2), Persuasion +1, difficulty 12, 60% success, a one-day extension on success, and no gift reversal on failure.

FR13: Successful meaningful checks shall award the G18 probability-based XP once to the player and relevant-skill tracks; failures, routine actions, duplicate resolutions, unchanged retries, and 95%-success checks shall award no XP.

FR14: Player and skill tracks shall start at level 1 with 0 XP, consume `100 × current level` XP per level while carrying excess, award one allocatable attribute point or one skill bonus per applicable level, and impose no design cap.

FR15: The character sheet shall preserve immutable starting scores separately from current scores and shall support previewed, explicitly confirmed, idempotent allocation of earned attribute points without overspending.

FR16: The authoritative world clock shall use integer seconds, pause while the application is closed or awaiting non-fictional UI/model work, and advance only through committed in-world actions.

FR17: Travel shall use authored distance divided by supported speed and round completed segments up to whole seconds; dialogue, item handling, transactions, and waits shall use their approved contextual duration rules.

FR18: Event-based waits shall depend on actual simulated events, interrupt for response-worthy developments, return control after the face-to-face silence interval, and report impossible or unscheduled targets rather than manufacturing an event.

FR19: P0 shall provide exactly the authored Market Square, Mara's Stall, and Common Room locations with stable connections, readable exits, present people, and examinable context.

FR20: P0 shall support the approved ordinary purchase with authoritative stock, funds, possession, ownership, speech time, and handling time committed exactly once.

FR21: The controlled P0 starting fixture shall contain one prepared pouch holding exactly 10,000 gold and no other player gold, with purchase, full-pouch gift, and no-gift tests restored from isolated copies that never merge.

FR22: Mara, Oren, Tessa, and Ivo shall each have explicit needs, desires, obligations, relationships, resources, plans, and limited knowledge sufficient for the controlled social scenario.

FR23: A committed gift shall change Mara's feasible opportunity set, and any resulting plan or behavior shall be explainable from her recorded situation rather than forced to a scripted outcome.

FR24: Historical facts, witness observations, spoken claims, and character beliefs shall remain distinct; beliefs shall retain source, time, confidence/uncertainty, and possible distortion without rewriting history.

FR25: Information shall spread only through plausible observation or contact; Tessa's later meeting with Ivo shall support the controlled rumor and doubt variants, while a non-witness knows nothing before receipt.

FR26: Consequential NPC replanning shall be validated against the NPC's actual knowledge, resources, obligations, relationships, feasible actions, and time; routine behavior may use deterministic rules.

FR27: The Main Notebook shall expose the current scene and transcript, exact submitted player intention, truthful request lifecycle, factual exits, current player character reference, and access to known-information surfaces.

FR28: The journal shall show only legitimately known facts, open concerns, and explicit commitments; inventory shall show authoritative owned items; result details shall explain both rolled and no-roll resolutions.

FR29: The application shall provide three manual save slots whose snapshots restore the complete branch state, including clock, inventory, ownership, relationships, commitments, beliefs, plans, progression, and Session 0 origin.

FR30: Save loading shall create or activate the restored branch only after successful validation, preserve the previous durable state on failure, and prohibit abandoned-branch knowledge or rewards from carrying over.

FR31: Long-running Rowan and action requests shall be durable operations with accepted, interpreting, needs-clarification, validating, resolving, committed, narrating, complete, failed, and interrupted lifecycle states.

FR32: Operations shall support typed progress, reconnect/recovery, polling fallback, cooperative pre-commit cancellation, and safe restart reconciliation without re-executing a committed action.

FR33: Every logical mutation shall be revision-checked and idempotent so retries cannot duplicate elapsed time, purchases, transfers, rolls, XP, allocations, rewards, or narration-triggered mechanics.

FR34: Development diagnostics shall expose read-only causal evidence for proposals, validation, random inputs, mutations, facts/observations/beliefs, plans, clock/events, revisions/hashes, latency, tokens, cost, and contradiction repairs without bypassing invariants.

FR35: The P0 evidence workflow shall support controlled repetitions of gift/no-gift branches, at least one rumor variant, timing/input/growth fixtures, save/load, failure/recovery, and an unplanned supported approach with conservation and contradiction checks.

#### P1 — Resources and shared effects (conditional on P0 evidence)

FR36: Every character shall have integer current and Base Maximum Health, Mana, and Stamina derived from the approved raw-attribute formulas, with P1 migration initializing existing characters at maximum.

FR37: Permanent attribute changes shall recalculate affected Base Maxima while preserving absolute deficits on increases and clamping to Effective Maxima on decreases; current pools shall remain within zero and Effective Maximum.

FR38: Mana, Stamina, Health, wounds, rest, sleep recovery, insufficient-resource rejection, zero-Stamina restrictions, immediate death at zero Health, and supported timed revival shall follow the approved rules.

FR39: Conditions, buffs, debuffs, and item treatments shall use one versioned effect definition/instance model containing source, category, polarity, tier, magnitude, target/shape, duration or uses, duplicate behavior, removal, and knowledge visibility.

FR40: The engine shall enforce source-bounded Subtle, Standard, and Major budgets; Stack, Refresh, and Replace duplicate policies; percentage-then-flat arithmetic; stable identity; cause-compatible removal; and independent persistence/expiry of cancelling effects.

FR41: Completed actions, scheduled ticks and need thresholds, expirations/environment changes, derived-value recalculation/clamping, and terminal states shall resolve in the approved deterministic same-second order.

FR42: P1 shall implement and verify the Sharpened, Bleeding, opposed-modifier, Star-metal Edge, tier/shape boundary, recovery, inspection, expiry, and save/load fixtures without importing later-stage needs, crafting, spell, or combat scope.

#### P2 — Places, access, ownership, and evidence (conditional on P1 evidence)

FR43: Resources shall be usable only where physically located and reachable; access shall resolve from location, entrance state, permission, relationship, compatible keys, tools, capacity, method, and payable time/Stamina costs rather than ownership alone.

FR44: Places shall persist entrances in open, closed, locked, and broken states; keys, permissions, local facilities, bed capacity, and environmental protection shall be authoritative.

FR45: Ivo's Home shall support the approved key entry, difficulty-12 lockpicking with consumed picks and paid retries, difficulty-14 forced entry with noise and Stamina costs, door damage, and capacity-two bed fixtures.

FR46: Distinctive items shall retain individual identity, claim, provenance, possessor, and recognizable marks, while fungible goods shall retain quantity and transfer history without magical traceability after mixing.

FR47: Witnessed and unwitnessed access, theft, damage, tampering, absence discovery, evidence, suspicion, and mistaken accusation shall update physical truth and character knowledge through separate causal paths.

#### P3 — Needs, food, and shelter (conditional on P2 evidence)

FR48: Every character shall persist last completed meal and adequate sleep, need-priority bands, next thresholds, and `Starved`/`Exhausted` stack schedules without forcing player intentions.

FR49: Crossing each 24-hour threshold shall apply the approved multiplicative Effective Maximum reduction; eating or adequate sleep shall reset the relevant timer and remove one stack with only the explicitly defined pool recovery.

FR50: Adequate sleep shall require a continuous eight-hour interval with a usable bed and valid protection throughout; interruption, bed loss, capacity loss, or protection lapse shall make it inadequate.

FR51: `Exposed` shall describe an unprotected sleeping place, block safe qualifying sleep and community stability, and cause no automatic damage or food loss.

FR52: P3 shall implement the six authored food fixtures with recipe inputs, facilities, occupied/unoccupied work, Stamina, yield, servings, batch shelf life, fresh-output expiry, raw edibility, and persistent scheduled processing.

FR53: Expired food shall remain edible and satisfy hunger, then resolve the approved spoilage risk, nearest-achievable Constitution check, success-only XP, and tiered physiological food-poisoning effect.

#### P4 — Autonomous livelihoods (conditional on P3 evidence)

FR54: NPC wants shall be selected from physiological pressure, personality, obligations, knowledge, relationships, resources, risk, time, and feasible known plans rather than direct need-to-resource mutation.

FR55: NPC plans shall execute through the ordinary travel, access, work, purchase, craft, eat, sleep, and transaction commands with the same costs, timing, failure, consequences, and death rules on-screen and off-screen.

FR56: Jobs, wages, shops, food, lodging, and trade shall use finite opportunities, counterparties, stock, budgets, tools, inputs, facilities, and completed actions; failures shall cause recorded replanning rather than invented resources.

FR57: The Ivo/Tessa fixture shall exercise the approved starting need state, finite courier wage, cabbage purchase, cooking/raw-food choice, protected bed, adequate sleep, and every declared failure/replanning branch.

#### P5 — Community viability and alchemy (conditional on P4 evidence)

FR58: P5 shall represent four one-resident households with concrete homes, local resources, beds, and protection, and shall track each household's independent consecutive lived-stability streak.

FR59: Community victory shall require every household to complete three consecutive qualifying days using recorded meals, adequate protected sleep, and non-Exposed housing funded or supplied by actual resources and commitments; only the failing household resets.

FR60: The seven-day ward, three-day/one-day warnings, expiry, 30-day repair, patrol contract, named-destination relocation, mixed solutions, and continued post-victory play shall follow the approved costs and causal rules.

FR61: Concerns and commitments shall use proposed, accepted, fulfilled, failed, expired, abandoned, and renegotiated states with explicit outcome, parties, deadline, evaluator, and reward or lack of reward.

FR62: Alchemy and Brewing shall support declared recipes or approaches, validated ingredients/workspace/tools/skills, routine known crafts, contextual uncertain substitutions, atomic input/time/output/XP commitment, and consumed ingredients on failed craft.

FR63: P5 shall provide the Field Alchemy Kit, Brewer's Crock, four base recipes, twelve total authored recipes across healing, mana, poison, and brewing tracks, and persistent recipe adoption/decline and 10/25-success production thresholds.

FR64: Crafted consumables and applied poisons shall produce stable persistent items/effects, respect delivery and use limits, survive save/load, and never reparse presentation text as mechanics.

FR65: The independent 30-gold P5 economy shall implement bounded supplier stock/restock, authored prices and values, finite need-driven NPC demand, and conservation across purchase, craft, use, gift, failure, and sale.

#### P6 — Spells and recognition (conditional on P5 evidence)

FR66: P6 shall offer exactly the two approved affinity packages, affinity-owned two-slot capacity, package skill bonuses, fixed starting spells, declared spell contracts, and Mana payment at commitment.

FR67: The Rest-concept stone shall retain an 80/20 rarity, disclose uniform choice between eligible package candidates, require capacity for either result, consume only on valid use, and permanently award the selected fixed mechanic.

FR68: Generated spell names and manifestations may use concept, affinity set, Session 0 concept, and committed history, but shall receive stable identities and shall never change the fixed accepted mechanics.

FR69: Titles, achievements, item prizes, and spell evolution shall remain distinct records; G01 completion shall award Brackenford's Anchor and the approved achievement trigger shall award the Copper Sandglass independently of later sale or loss.

FR70: Three distinct consequential Rest-spell uses plus the achievement shall reveal the exact approved Deepened replacement after the first-use clue, and replacement shall occur only after explicit confirmation.

#### P7 — Daily quests and gacha (conditional on P6 evidence)

FR71: The System shall maintain three daily quest slots refreshed together at 06:00 with exactly one crafting, one social, and one observation quest, each exposing an explicit success contract and expiring without penalty.

FR72: Daily quest completion shall be evaluated from committed fulfillment, award 25 player XP and 25 relevant-skill XP plus one draw exactly once, and award nothing for partial, expired, or duplicate resolution.

FR73: Gacha shall select the approved 70/25/5 tier and then uniformly select from the visible nine-item pool, recording pool version, random evidence, accepted rerolls, and awarded item for idempotent replay.

FR74: System presentation shall remain distinct from Rowan, NPCs, narration, mechanics, and award narration and shall never claim an uncommitted objective or reward.

#### P8 — Hidden quest bonuses (conditional on P7 evidence)

FR75: Each supported P8 quest shall receive exactly one stable private hidden-condition record specifying unusual approach, qualifying evidence, evaluation point, evaluator version, and one seeded bounded reward.

FR76: At the evaluation point, bounded LLM judgment shall be validated against committed evidence and deterministic reward limits; at most one XP, extra-draw, or Common-item bonus shall commit atomically.

FR77: Hidden conditions and evaluator reasoning shall never enter player projections or ordinary narration; success shall use the exact approved notification followed by the committed reward.

#### P9 — Bounded combat (conditional on P8 evidence)

FR78: P9 shall provide one authored one-on-one encounter with the approved initiative, tie-break, six-second rounds, turn actions, movement, sprint, escape, surrender, positions, legal exits, and action economy.

FR79: Combat shall reuse ordinary checks, Defense, Stamina/Mana payment, attacks, damage, spells, items, effects, time, immediate death, and transaction semantics rather than creating a second rules engine.

FR80: The controlled player and road-robber fixtures shall implement the approved statistics, equipment, Cinder Lance, surrender thresholds, accepted surrender behavior, escape distance, purse transfers, and outcome-specific rewards.

FR81: Combat XP, loot, initiative, attacks, effects, current pools, positions, turns, and terminal outcome shall persist through mid-combat save/load and shall never reroll or reward twice.

#### Cross-stage scope and content

FR82: Implementation shall follow P0 → P1 → ... → P9 sequential evidence gates; design approval for a later stage shall not authorize its implementation or introduce its state, UI, folders, abstractions, or migrations early.

FR83: Locations and geography shall be deliberately authored and stable; procedurally generated locations are permanently excluded.

FR84: Each stage shall stay within its approved cast, location, system, item, recipe, spell, quest, reward, and encounter content budgets and shall treat unsupported proposals as expansion candidates rather than invented successful consequences.

### NonFunctional Requirements

NFR1: The game shall run locally in a desktop browser as a solo experience, with a packaged loopback-only FastAPI process serving the React SPA and API from one origin.

NFR2: Visible input acknowledgement shall occur within 100 ms, local menu responses within 200 ms, save/load within 2 seconds, and 95% of completed LLM-mediated actions within 10 seconds, with a recoverable interruption state by 30 seconds.

NFR3: A 60-minute, approximately 100-action, four-NPC endurance run shall remain no more than 100 MB resident memory above the post-initial-scene baseline and shall show no monotonic per-action growth.

NFR4: Authoritative mutations shall be atomic, revision-checked, transactional, and idempotent; pre-commit failure shall leave state unchanged and post-commit presentation failure shall preserve mechanics.

NFR5: For the same captured state, structured proposal, content/rules versions, and recorded random inputs, the engine shall reproduce mechanical outcomes without requiring identical newly generated prose.

NFR6: Persistence shall preserve complete causal state, stable IDs, schema/content/ruleset versions, state hashes, operation evidence, and branch isolation without save drift.

NFR7: The application shall meet WCAG 2.2 Level AA across complete pages and responsive variants, including generated and dynamic content.

NFR8: All functionality shall be keyboard operable with visible unobscured focus, screen-reader semantics, explicit labels/states, polite deduplicated announcements, and pointer targets of at least 24×24 CSS px or the WCAG spacing exception.

NFR9: Browser-root text sizing and at least 200% page zoom shall preserve all content and functionality; at the 320 CSS px-equivalent reflow target, ordinary operation shall require no horizontal page scrolling.

NFR10: Normal text and labels shall meet 4.5:1 contrast, large text 3:1, and essential focus/component boundaries 3:1; meaning shall never depend on color alone.

NFR11: The interface shall honor `prefers-reduced-motion` and shall have no timed reading, auto-dismissed narrative, interaction timeout, or required audio cue.

NFR12: LLM provider credentials and secrets shall remain backend-only and shall never enter browser storage, saves, authored content, generated clients, player-visible errors, or ordinary logs.

NFR13: All external, persisted, API, and provider-boundary data shall receive strict runtime validation; incompatible SQLite, configuration, content, schema, or ruleset versions shall fail safely before mutation.

NFR14: Player-facing projections and LLM recall context shall enforce the character's legitimate knowledge and shall not leak hidden actors, private plans, beliefs, hidden objectives, provider payloads, or diagnostic-only state.

NFR15: Application code shall maintain strict dependency direction, precise static typing, thin transport adapters, explicit dependency injection, immutable authored content, and feature-oriented vertical slices without generic managers or speculative abstractions.

NFR16: Quality gates shall separately enforce formatting, linting, strict type checking, integration tests against real FastAPI/SQLite, component tests through accessible interactions, contract drift, and Playwright browser journeys; only the external LLM boundary may use deterministic fixtures.

NFR17: Structured diagnostics shall record latency, model/provider and contract versions, token/cost usage, rejected/duplicate attempts, contradiction repairs, revisions, state hashes, and correlation IDs while excluding secrets, hidden objectives, complete saves, and unrestricted provider payloads.

NFR18: Generated definitions and reusable rulings shall retain stable identity, immutable accepted mechanics, and explicit version history across sessions; intentional changes require migration rather than silent reinterpretation.

NFR19: The application shall support recoverable operation interruption, refresh/reconnect, status polling when streaming is unavailable, crash reconciliation, and safe retry without ambiguous commit state.

NFR20: Each stage migration shall be explicit, ordered, typed, idempotent, covered against real SQLite, and atomic; failure shall preserve the previous readable save and skipping an intermediate stage shall be rejected.

### Additional Requirements

- Use the specified starter approach for initial scaffolding: create-vite 9.2.0's minimal React/TypeScript scaffold for `frontend/` and a small uv-managed FastAPI application initialized from scratch for `backend/`. This is the required Epic 1 Story 1 foundation.
- Use the documented exact dependency versions and commit frontend/backend lockfiles; refresh dependency availability and compatibility when scaffolding because the architecture's currency check is historical.
- Organize the repository as a feature-oriented monorepo with cohesive frontend player-facing slices and backend domain/application slices; do not introduce distributed services for P0.
- Preserve inward dependency direction: domain code cannot import FastAPI, SQLite, provider SDKs, process environment access, or frontend code.
- Construct dependencies in composition roots and inject them explicitly; prohibit global mutable service registries, feature-owned containers, and hidden environment reads.
- Use React for presentation and accessible interaction only; FastAPI and the Python domain engine own mechanics, world state, time, randomness, persistence, NPC decisions, and LLM orchestration.
- Use strict Pydantic models for Python boundaries, strict TypeScript plus generated Zod schemas for browser boundaries, and reject unknown fields unless a contract explicitly permits extensibility.
- Make FastAPI OpenAPI 3.1 the transport source of truth; generate and commit the native fetch client, TypeScript types, Zod schemas, and TanStack Query bindings, and fail CI on contract drift.
- Use resource-specific JSON success models and RFC 9457 `application/problem+json` failures extended with stable code, classification, correlation ID, and applicable operation/revision metadata.
- Use camelCase JSON fields, lowercase snake_case wire enums, RFC 3339 UTC wall-clock timestamps, integer game seconds, and integer measured milliseconds.
- Require `requestId` and the applicable expected world, draft, or slot revision for every mutation; stale revisions return typed conflicts and duplicate logical requests recover the original result.
- Represent slow mutations as durable operation resources returning `202 Accepted`, with typed versioned SSE events, monotonic event IDs, `Last-Event-ID` reconnection, status polling, and cooperative cancellation.
- Allow one mutating operation at a time per branch while preserving read access; prevent save/load from racing an unresolved branch mutation.
- Atomically write subject state, immutable action record, request result, and committed operation status so restart recovery has no ambiguous commit window.
- Persist authoritative state in SQLite `STRICT` tables through typed adapters, canonical versioned JSON snapshots, relational lifecycle/audit records, explicit ordered SQL migrations, and typed world-state migrations.
- Reject SQLite runtimes older than 3.37.0 before opening application data; store application data in an explicit directory with backup/export support.
- Use authoritative current state plus an append-only action log rather than full event sourcing; increment world revision and record a state hash on each committed mutation.
- Store authored locations, NPC templates, items, encounters, and rules as version-controlled YAML with stable namespaced IDs and explicit schema/content versions.
- Load P0 authored content at startup using `yaml.safe_load`, strict Pydantic validation, duplicate/reference checks, and an immutable in-memory registry; do not hot-reload production content during an active session.
- Keep production authored content separate from controlled test starting states; runtime-generated content persists in game state and never rewrites authored files.
- Implement the provider-neutral `LlmGateway`; provider-specific formats and credentials remain confined to the adapter, and model/provider selection remains deferred until compatibility and measured cost are evaluated.
- Validate unknown model output through versioned contracts before application code uses it; narration receives only committed facts and presentation context and cannot request mutations.
- Record provider, model, prompt/contract version, latency, usage, validated proposal, and outcome for diagnostics; restrict raw provider responses to local diagnostics.
- Implement the deterministic persisted scheduler with stable event IDs, due-second/priority/insertion ordering, the GDD same-second phase reducer, event budgets, and loop detection.
- Compile both player and NPC work into ordinary typed commands that reserve inputs, pay costs, advance the shared clock, and commit through one coordinator.
- Keep TanStack Query as the browser's server-state owner and React state limited to presentation concerns such as unsent draft input, panels, selection, roll-detail selection, and focus.
- Do not store authoritative game state or text-size preferences in browser storage; validate any other non-authoritative browser preference with Zod and safe defaults.
- Use stable slice-owned factories, discriminated lifecycle states, typed result variants, slice-specific stores, explicit commands/queries/events, and exhaustive transitions.
- Route multi-slice mutations through one commit coordinator; domain functions return validated change sets/events and do not open transactions, publish through a global bus, or perform external side effects before commit.
- Execute authoritative event handlers synchronously and deterministically before commit; post-commit SSE/telemetry handlers cannot alter mechanics.
- Use structured JSON logs to rotating local JSONL plus readable development output, with consistent correlation fields and safe severity policy.
- Provide capability-gated, read-only development diagnostics only when loopback-bound with `DMUD_DEVTOOLS=true`; never register state-changing cheats or fixture controls as release routes.
- Serve the packaged SPA and API from FastAPI on loopback only; development may use split Vite/FastAPI servers with a Vite `/api` proxy.
- Apply conservative local security headers and request-size limits; require a separate threat model before remote binding, accounts, TLS termination, hosting, or multi-user access.
- Keep P0 free of WebSockets, Redis, Celery, external brokers, remote configuration, authentication, cloud saves, audio infrastructure, client routing without user value, and speculative P1–P9 modules.
- Add conditional-system slices only after authorization, using the documented one-way dependency map; lower-stage modules cannot import later-stage rules.
- Starting with P1, record ruleset stage/version and enabled content packages through typed migrations; composition registers only the highest implemented stage and all proven stages beneath it.
- Reuse stable definition/instance conventions and the common transaction, scheduler, item, effect, progression, and reward contracts for all later-stage mechanics.
- Treat P9 combat as an encounter coordinator over lower-stage contracts, not a second engine or alternate persistence path.
- Use Python `snake_case`, React `PascalCase`, feature/YAML `kebab-case`, plural kebab-case API nouns, past-tense PascalCase domain events, dotted lowercase telemetry events, and the documented ID conventions.
- Keep generated OpenAPI/client files committed but never manually edited; runtime databases, saves, logs, provider responses, secrets, build output, and test artifacts remain outside source control.

### UX Design Requirements

UX-DR1: Implement the warm “DM's Notebook” visual system using the authoritative paper, ink, forest, red-pencil, rule, note, player-note, and focus tokens from DESIGN.md rather than a terminal or generic chat shell.

UX-DR2: Translate DESIGN.md typography into relative `rem`-based story, scene-title, overlay-title, interface, strong-interface, label, and caption styles while inheriting the browser's root size and prohibiting Comic Sans, faux handwriting, and dense medieval display faces.

UX-DR3: Keep sustained narration at approximately 55–75 characters per line and make the transcript and composer the dominant visual surface.

UX-DR4: Implement the 4px spacing scale, lightly softened corner scale, restrained stacked-paper depth, and tokenized component styling in `frontend/src/app/styles.css`.

UX-DR5: Implement `action-button` with explicit text, keyboard and pointer activation, a visible external focus ring, a non-obvious-disabled reason, and the target-size rule.

UX-DR6: Implement `notebook-navigation` with stable reading order, explicit labels, programmatic current-location state, and a non-color selected marker.

UX-DR7: Implement `story-entry` with selectable content and a semantic speaker/message-type label before narration, NPC speech, Rowan text, or mechanics; never silently collapse prior consequences.

UX-DR8: Implement `player-intention` as a labeled, selectable echo of the exact submitted text plus its current status.

UX-DR9: Implement one labeled `message-composer` for Rowan questions, in-world speech, and actions; Enter submits, Shift+Enter inserts a line, and no modes, prefixes, suggestions, generated replies, or action chips appear.

UX-DR10: Implement `response-status` with immediate acknowledgement and truthful pending, clarification, resolved, interrupted, failed, and committed-but-narrating states; announce changes politely without stealing focus or repeatedly announcing decorative copy.

UX-DR11: Implement one current-player `character-card` using text identity or a monogram, opening the character sheet without implying an omniscient nearby-character roster or requiring portrait assets.

UX-DR12: Implement one reusable `reference-overlay` for inventory, character sheet, roll details, and save/load, with an accessible dialog name/role, contained focus, Escape/close behavior, focus return, viewport bounds, internal scrolling, and no stacked overlays.

UX-DR13: Implement `mechanical-result` as an inline control attached to one transcript result, stating the skill/result and whether a roll occurred before Details and supporting inspectable no-roll outcomes.

UX-DR14: Implement `journal-entry` as text-first known information with status written in words, no hidden state, and no recommended next action.

UX-DR15: Implement `stat-assignment` for the exact five attributes and fixed array with available, assigned, incomplete, duplicate, invalid, valid, and locked states conveyed by text plus boundaries.

UX-DR16: Implement `attribute-allocation` with earned/spent/unspent counts, local preview, explicit confirmation, overspend error, pending state, and persisted result while keeping the starting array immutable.

UX-DR17: Implement `save-slot` rows showing slot identity, campaign, known place, in-world time, saved-at metadata, compatibility, selection, progress, overwrite confirmation, failure, and recovered prior state.

UX-DR18: Implement Title states for cold save-index loading, no saves with explained unavailable Continue, compatible saves, and save-index failure with retry while New Game remains usable.

UX-DR19: Implement Session 0 states for the first question, incomplete concept, stat-assignment errors, all-valid assignment, Rowan pending, reflection correction/confirmation, and provider failure with all acknowledged material preserved.

UX-DR20: Implement Main Notebook states for cold load, restored scene, ready composer, each request lifecycle state, model unavailable, and unsupported intention; pending must never look resolved.

UX-DR21: Implement separate empty, populated, loading, and failed-read states for Journal and Inventory; an empty view must mean known-empty rather than silently masking a failed or unknown read.

UX-DR22: Implement Character Sheet states for Session 0 editing, confirmed locked starting scores, P0 progression summary, no/unspent points, preview, invalid overspend, pending confirmation, persisted allocation, loading, and error.

UX-DR23: Implement Roll Details states for routine/no-roll, rolled resolution, missing evidence, and corrupt/unreadable evidence; missing mechanics must be reported rather than reconstructed by the LLM.

UX-DR24: Preserve the information hierarchy of transcript/scene, composer/request status, current-character reference, and factual navigation/reference controls.

UX-DR25: Make Rowan, narration, NPC speech, player intention, mechanics, clarification, waiting, and failure semantically and textually distinct rather than relying on color.

UX-DR26: Keep clarification neutral and intent-preserving, failure plain and specific about the commit boundary, and waiting copy truthful even when it includes brief absurd backstage humor.

UX-DR27: Enforce character-knowledge boundaries before serialization so transcript, journal, inventory, character sheet, result details, save labels, Rowan recall, and visible actors cannot leak concealed or private simulation state.

UX-DR28: Provide complete keyboard, pointer, and screen-reader parity across title choices, Session 0, composer, navigation, overlays, stat assignment, attribute allocation, save slots, and inline mechanics; hover must never carry unique information.

UX-DR29: Use semantic HTML, landmarks, headings, explicit control labels/names/roles/states, explicit speaker/type labels, logical focus order, and visible unobscured focus for authored and generated content.

UX-DR30: Reflow the ordinary desktop navigation/story/character-reference layout into one reading column at 200% zoom or narrow width, moving navigation to a labeled top region and compacting the character reference without lost controls or horizontal page scrolling.

UX-DR31: Ensure pointer target size/spacing, overlay bounds, focus behavior, keyboard semantics, and screen-reader semantics remain intact under browser-root text enlargement, 200% zoom, and 320 CSS px-equivalent reflow.

UX-DR32: Honor reduced motion by replacing looping waiting movement with a static mark; never use animation, decorative rotation, or copy changes in ways that obstruct reading, focus, reflow, or status truth.

UX-DR33: Provide no Settings surface or in-game text-size control; preserve browser zoom, browser text sizing, text selection, and OS motion preferences.

UX-DR34: Require no audio, illustration, portrait, sprite, screen shake, confetti, or generated-image pipeline for P0; every meaningful cue must be available textually.

UX-DR35: Keep `system-notice` and `award-notice` as distinct deferred token/component contracts only; do not render them in P0, and require a phase-specific UX update before implementing E3–E11 interfaces.

UX-DR36: When later authorized, `system-notice` shall remain visually and semantically separate from Rowan, NPCs, ordinary mechanics, and award narration, while `award-notice` shall appear only after its underlying title, achievement, prize, or variant commits.

### FR Coverage Map

FR1: Epic 1 - Title entry and save-index behavior
FR2: Epic 1 - Durable Session 0 discovery
FR3: Epic 1 - Categorized character and campaign information
FR4: Epic 1 - Fixed-array attribute assignment
FR5: Epic 1 - Correctable Rowan reflection
FR6: Epic 1 - Atomic campaign confirmation
FR7: Epic 1 - Unified free-text intent input
FR8: Epic 1 - Neutral pre-commit clarification
FR9: Epic 1 - Authoritative action lifecycle
FR10: Epic 1 - Routine, impossible, and uncertain action handling
FR11: Epic 1 - Core check resolution
FR12: Epic 1 - Controlled payment-extension fixture
FR13: Epic 1 - Probability-based XP awards
FR14: Epic 1 - Uncapped player and skill progression
FR15: Epic 1 - Earned attribute allocation
FR16: Epic 1 - Authoritative seconds-based clock
FR17: Epic 1 - Contextual action durations
FR18: Epic 1 - Event-based and interruptible waits
FR19: Epic 1 - Authored P0 locations and navigation
FR20: Epic 1 - Authoritative ordinary purchase
FR21: Epic 1 - Isolated P0 funding fixtures
FR22: Epic 2 - Grounded NPC state
FR23: Epic 2 - Gift-driven opportunity and replanning
FR24: Epic 2 - Separate facts, observations, claims, and beliefs
FR25: Epic 2 - Contact-based information transmission
FR26: Epic 2 - Knowledge-constrained NPC replanning
FR27: Epic 1 - Main Notebook gameplay surface
FR28: Epic 1 - Journal, inventory, and result details
FR29: Epic 1 - Complete three-slot saving
FR30: Epic 1 - Safe branch loading and isolation
FR31: Epic 1 - Durable operation lifecycle
FR32: Epic 1 - Operation progress, cancellation, and recovery
FR33: Epic 1 - Revision checks and idempotency
FR34: Epic 1 - Read-only causal diagnostics
FR35: Epic 1 - P0 controlled evidence workflow
FR36: Epic 3 - Derived character resource pools
FR37: Epic 3 - Maximum recalculation and clamping
FR38: Epic 3 - Resource costs, recovery, restrictions, and death
FR39: Epic 3 - Shared effect definitions and instances
FR40: Epic 3 - Effect budgets, duplication, arithmetic, and removal
FR41: Epic 3 - Deterministic same-second ordering
FR42: Epic 3 - P1 controlled fixtures and evidence
FR43: Epic 4 - Physical access resolution
FR44: Epic 4 - Entrances, keys, permissions, beds, and protection
FR45: Epic 4 - Ivo's Home access fixture
FR46: Epic 4 - Distinctive and fungible item identity
FR47: Epic 4 - Theft, evidence, suspicion, and knowledge separation
FR48: Epic 5 - Hunger and sleep need clocks
FR49: Epic 5 - Starved and Exhausted stacking and recovery
FR50: Epic 5 - Adequate sleep requirements
FR51: Epic 5 - Exposed sleeping places
FR52: Epic 5 - Authored food preparation and batches
FR53: Epic 5 - Expired-food risk and poisoning
FR54: Epic 6 - Wants-driven NPC goal selection
FR55: Epic 6 - Ordinary-command plan execution
FR56: Epic 6 - Finite jobs, trade, and failure replanning
FR57: Epic 6 - Ivo/Tessa livelihood proof
FR58: Epic 7 - Household stability tracking
FR59: Epic 7 - Causal community victory
FR60: Epic 7 - Ward, patrol, relocation, and mixed solutions
FR61: Epic 7 - Explicit concerns and commitments
FR62: Epic 7 - Alchemy and Brewing action lifecycle
FR63: Epic 7 - Recipe tracks and unlock progression
FR64: Epic 7 - Persistent crafted items and applied poisons
FR65: Epic 7 - Bounded P5 ingredient economy and demand
FR66: Epic 8 - Affinity packages, slots, and starting spells
FR67: Epic 8 - Rest-stone awakening
FR68: Epic 8 - Stable generated spell presentation
FR69: Epic 8 - Titles, achievements, and prizes
FR70: Epic 8 - Deepened spell evolution
FR71: Epic 9 - Three daily quest categories and refresh
FR72: Epic 9 - One-time daily quest rewards
FR73: Epic 9 - Declared-pool gacha draws
FR74: Epic 9 - Distinct System presentation
FR75: Epic 10 - Private hidden-condition records
FR76: Epic 10 - Bounded hidden-condition evaluation and rewards
FR77: Epic 10 - Hidden-condition secrecy and notification
FR78: Epic 11 - Authored combat encounter and action economy
FR79: Epic 11 - Lower-stage combat mechanics reuse
FR80: Epic 11 - Player and road-robber combat fixtures
FR81: Epic 11 - Persistent, idempotent combat outcomes
FR82: Epic 1 - Sequential stage and implementation gates
FR83: Epic 1 - Authored, nonprocedural geography
FR84: Epic 1 - Approved content and scope budgets

## Shared Delivery Definition of Done

Every implementation story inherits the applicable NFR and architecture contracts in this document. Feature-local criteria state the observable behavior and any exceptional boundary. Verification records must use real FastAPI and isolated SQLite for first-party integration, accessible browser/component interaction for UI, strict type/lint/format/contract gates, and deterministic fixtures only at the external LLM boundary. Each mutation is atomic, revision-checked, idempotent, and safe across retry and failure. Once save/load is introduced, every owned state change must survive restoration without branch leakage. Player-facing projections respect legitimate knowledge. All applicable P0 UI states meet DESIGN/EXPERIENCE accessibility, zoom, reflow, focus, status, and reduced-motion requirements. Evidence includes reproducible commands and failures; a skipped, flaky, or failing required check does not pass a stage gate.

For P0, [P0 Verification and Exit Plan](./p0-verification-and-exit-plan.md) owns stage-wide fixture matrices, endurance, accessibility, contradiction review, and P0 promotion evidence. Completion of Epic 1 is foundation evidence only; P0 passes only after Epic 2 and that plan pass. The shared contract does not replace feature-specific ACs such as a stale save-slot conflict or a particular knowledge leak.

### P0 Story-Level FR Traceability

| Native FR | Current story or exit evidence |
| --- | --- |
| FR1 | 1.2, 1.31 |
| FR2–FR3 | 1.3, 1.5–1.6, 1.8 |
| FR4–FR5 | 1.7–1.8 |
| FR6 | 1.4, 1.9–1.10 |
| FR7–FR9 | 1.14–1.18, 1.21 |
| FR10–FR12 | 1.14, 1.16–1.17, 1.24 |
| FR13–FR14 | 1.25 |
| FR15 | 1.26 |
| FR16–FR18 | 1.14, 1.17, 1.20–1.23 |
| FR19 | 1.4, 1.14, 1.19–1.20 |
| FR20 | 1.21 |
| FR21 | 1.4, 1.22, 2.4 |
| FR22 | 1.4, 2.1–2.2 |
| FR23 | 2.4–2.5 |
| FR24–FR26 | 2.2–2.3, 2.5–2.9 |
| FR27 | 1.5, 1.11–1.13 |
| FR28 | 1.27–1.29 |
| FR29–FR30 | 1.30–1.32 |
| FR31–FR33 | 1.3, 1.14–1.18 |
| FR34 | 1.33–1.34 |
| FR35 | P0 Verification and Exit Plan |
| FR82 | 1.1, 1.35 and P0 Verification and Exit Plan |
| FR83 | 1.4, 1.19 |
| FR84 | 1.4, 1.19 and P0 Verification and Exit Plan |

## Conditional Stage Backlog Status

Epics 3–11 describe approved design intent and requirement coverage, not currently executable sprint stories. Each must first receive its phase-specific UX update and preceding stage evidence. The September 22 report identified Stories 3.2, 3.4, 5.3, 5.4, and 11.5 as multi-capability work packages and Stories 3.6, 4.6, 5.6, 6.6, 7.19, 8.12, 9.10, 10.7, and 11.11 as mixed feature/gate work. Those and the other ten-plus-scenario stories require decomposition at the corresponding stage planning gate. Their present criteria retain design coverage but are not sprint-sized commitments. Stage-wide evidence will move to exit plans, while player-visible inspection remains in feature stories. The revised P0 order has a [focused dependency review](./p0-story-dependency-review-2026-09-23.md); executable P0 gate evidence remains outstanding until implementation.

## Epic List

### Epic 1: Enter and Act in a Small Persistent World
Players can create a character, enter Brackenford, express intentions in ordinary language, resolve actions and uncertainty, develop competence, inspect known information, and safely save and resume a complete persistent branch.

**FRs covered:** FR1–FR21, FR27–FR35, FR82–FR84

**Implementation notes:** This epic is the complete P0 application foundation and intentionally consolidates the heavily overlapping Session 0, Main Notebook, action pipeline, time, progression, persistence, request recovery, diagnostics, architecture, and P0 UX work. It must satisfy the current DESIGN and EXPERIENCE contracts and establish the controlled P0 evidence harness without implementing later stages.

### Epic 2: Make Consequences Travel Through People
Players can change an NPC's feasible opportunities and later observe information travel through witnesses, fallible reports, beliefs, and motive-based NPC choices without omniscience or scripted outcomes.

**FRs covered:** FR22–FR26

**Implementation notes:** Completes the second half of the P0 causal-world proof using Epic 1's action, time, persistence, knowledge-safe presentation, and diagnostics contracts. P0 evidence must pass before Epic 3 is authorized.

### Epic 3: Make Resources and Effects Authoritative
Players can spend and recover Health, Mana, and Stamina and can apply, inspect, stack, remove, expire, and persist bounded effects whose mechanics remain stable.

**FRs covered:** FR36–FR42

**Implementation notes:** Conditional P1. Introduces the shared resource/effect kernel through an explicit migration and deterministic scheduler ordering without importing survival, crafting, spells, or combat.

### Epic 4: Make Places Physically Accessible
Players can reach and use local resources through permission, keys, locks, force, and other physical methods while ownership, evidence, observation, and belief remain causally separate.

**FRs covered:** FR43–FR47

**Implementation notes:** Conditional P2. Builds on P1 costs/effects and P0 knowledge/inventory contracts; it does not add formal policing or universal crime reputation.

### Epic 5: Live With Hunger and Fatigue
Players can eat, prepare food, sleep, accept deprivation, recover, and experience causal Starved, Exhausted, Exposed, spoilage, and food-poisoning outcomes.

**FRs covered:** FR48–FR53

**Implementation notes:** Conditional P3. Adds need clocks, continuous rest, authored food recipes, persistent batches, and scheduled processing on the existing access, effect, check, and time contracts.

### Epic 6: Let Needs Become Plans
Players can observe NPCs pursue food, work, trade, cooking, shelter, and sleep through finite physical actions, then replan honestly when resources, access, or opportunities fail.

**FRs covered:** FR54–FR57

**Implementation notes:** Conditional P4. Proves the complete need → plan → action → consequence → replan loop with Ivo and Tessa and requires mechanical equivalence between observed and off-screen execution.

### Epic 7: Secure Brackenford's Future Through Play
Players can sustain four households through protection, relocation, work, trade, food, commitments, and personal alchemy while supported mixed solutions remain valid.

**FRs covered:** FR58–FR65

**Implementation notes:** Conditional P5. Combines community viability and alchemy because both operate on the same needs, crafting, inventory, economy, commitment, and effect contracts in this approved stage.

### Epic 8: Earn a Distinctive Affinity Spell
Players can choose an affinity package, awaken a bounded Rest-concept spell, receive stable history-shaped presentation and distinct recognition, and optionally deepen the earned spell.

**FRs covered:** FR66–FR70

**Implementation notes:** Conditional P6. Fixed mechanics remain separate from generated names and manifestations; affinities, spell slots, titles, achievements, prizes, and variants retain distinct identities. A phase-specific UX update is required before implementation.

### Epic 9: Complete Daily Quests for Explicit Rewards
Players can complete three clearly stated daily objectives for one-time XP and item draws from a visible declared pool without penalties for expiry or partial completion.

**FRs covered:** FR71–FR74

**Implementation notes:** Conditional P7. Adds scheduled refresh, explicit contracts, a distinct System voice, and idempotent rewards using proven action, quest, progression, inventory, and random-evidence contracts. A phase-specific UX update is required.

### Epic 10: Discover Hidden Quest Bonuses
Players can receive bounded surprise rewards when committed evidence satisfies a private unusual-approach condition without revealing the trigger or routinely over-awarding normal play.

**FRs covered:** FR75–FR77

**Implementation notes:** Conditional P8. Extends the P7 quest lifecycle with one private condition and at most one atomic bonus claim per quest. A phase-specific UX update is required.

### Epic 11: Resolve a Bounded Combat Encounter
Players can fight, flee, surrender, or accept surrender in one readable authored encounter while established resources, effects, positioning, items, time, death, rewards, and persistence remain authoritative.

**FRs covered:** FR78–FR81

**Implementation notes:** Conditional P9. Combat is an encounter coordinator over proven lower-stage rules, not a second engine. It requires four outcome paths, mid-combat save/load, and idempotent XP/loot evidence. A phase-specific UX update is required.


## Epic 1: Enter and Act in a Small Persistent World

Players can create a character, enter Brackenford, express intentions in ordinary language, resolve actions and uncertainty, develop competence, inspect known information, and safely save and resume a complete persistent branch.

### Story 1.1: Run the Local dmud Application Foundation

As a player,
I want to start the local application with a validated foundation,
So that I can begin a campaign on a stable local system.

**Acceptance Criteria:**

**Given** the documented Node, Python, uv, and SQLite prerequisites are available
**When** dependencies are installed from the committed lockfiles
**Then** the create-vite 9.2.0 React/TypeScript starter and the uv-managed FastAPI backend initialized from scratch build successfully
**And** dependency availability has been revalidated against the versions selected by Architecture 1.2.

**Given** the development environment is started
**When** the player opens the frontend
**Then** the browser receives a working application shell
**And** frontend `/api` requests are proxied to the loopback FastAPI server without development CORS configuration.

**Given** backend configuration includes an LLM credential or other secret
**When** the frontend, logs, authored content, generated API client, or browser storage is inspected
**Then** the secret is absent
**And** configuration is constructed and validated only at the backend composition root.

**Given** the initial repository structure
**When** its dependencies and directories are reviewed
**Then** it follows the approved feature-oriented monorepo and inward dependency direction
**And** it contains no speculative P1–P9 modules, distributed infrastructure, audio pipeline, or unused asset directories.

**Given** the runnable shell is checked in
**When** its baseline checks run
**Then** formatting, linting, strict type checking, and an isolated real-browser startup journey pass
**And** the checks exercise the frontend and backend through their real local boundary.

### Story 1.2: Open the Title and Start a New Game

As a player,
I want to start a new campaign from a clear Title surface,
So that I can enter Session 0 even if save discovery fails.

**Acceptance Criteria:**

**Given** the application has opened and the save index is still loading
**When** the Title surface renders
**Then** New Game and Continue are shown immediately
**And** Continue is unavailable with truthful loading context while New Game remains keyboard and pointer accessible.

**Given** all three save slots are empty
**When** the save-index request succeeds
**Then** Continue remains visible but unavailable
**And** its accessible explanation states that no saved campaign exists.

**Given** the save index cannot be read or fails runtime validation
**When** the Title surface reports the failure
**Then** it offers a safe retry and keeps New Game available
**And** malformed data is not presented as an empty save list.

**Given** the player activates New Game
**When** the entry action succeeds
**Then** the application enters the Session 0 route/surface without deleting saves or selecting an occupied slot
**And** the transition advances no fictional time.

**Given** the Title surface is used with keyboard navigation, a screen reader, enlarged browser text, 200% zoom, reduced motion, or the 320 CSS px-equivalent layout
**When** the player operates every control
**Then** labels, focus, status, target size, reading order, and functionality remain available
**And** the layout reflows without horizontal page scrolling.

### Story 1.3: Track a Recoverable Session 0 Operation

As a player,
I want the start of Session 0 to have a durable request and status,
So that refresh or interruption cannot leave me unsure whether it started.

**Acceptance Criteria:**

**Given** the first durable Session 0 operation needs local storage
**When** the backend initializes application data
**Then** its first ordered migration creates only the draft and operation records needed by this story in SQLite `STRICT` tables through typed infrastructure adapters
**And** a SQLite runtime older than 3.37.0 fails before application data opens or mutates with a clear, secret-free error.

**Given** New Game starts a Session 0 draft subject
**When** the first zero-time operation is accepted
**Then** the server creates one idempotent, revisioned `SessionZeroDraft` and durably records its subject, request ID, payload digest, revision, and ordered status events before returning its operation ID
**And** duplicate IDs with identical payloads return the same operation while changed payloads receive a typed conflict.

**Given** a draft-subject operation is accepted, running, complete, failed, or interrupted
**When** its status is queried
**Then** the typed response reports the authoritative state and last event ID
**And** the Session 0 surface never treats an unacknowledged request as committed.

**Given** the event connection drops or the browser refreshes
**When** the client reconnects with its last event ID or polls the status endpoint
**Then** it recovers the same ordered operation and draft subject without rerunning the request
**And** the pending or terminal state remains visible and accessible.

**Given** the backend restarts with a nonterminal draft operation
**When** startup reconciliation reads its durable operation record
**Then** an uncommitted request becomes explicitly interrupted and a committed draft result remains available
**And** recovery never fabricates a campaign or advances fictional time.

**Given** a failed or interrupted draft operation is retried
**When** its recovery action runs
**Then** only the supported uncommitted work is retried under the same draft subject
**And** later answer, reflection, and confirmation operations can use this same contract without a second operation store.

### Story 1.4: Validate the Authored P0 Starting World

As a player,
I want character confirmation to use a validated starting world,
So that I enter the same coherent Brackenford fixture every time.

**Acceptance Criteria:**

**Given** the application starts with the P0 content package
**When** authored YAML is loaded
**Then** strict validation accepts exactly the approved three locations, four named NPCs, social conflict, five one-gold drinks, routes, movement rules, and controlled check content
**And** duplicate IDs, invalid references, unknown fields, or incompatible content versions fail before campaign mutation.

**Given** the validated starting package
**When** its deterministic fixture factory produces a pre-confirmation seed
**Then** the seed provides Market Square, Mara's Stall, the Common Room, Mara, Oren, Tessa, Ivo, Mara's initial drink stock and transaction funds, and one prepared 10,000-gold pouch with no other player gold
**And** Mara and Tessa have authored starting positions that make the handover at Mara's Stall perceptible to Tessa but not to Oren or Ivo; the seed has a stable content version and immutable fixture origin suitable for later isolated branch creation without itself creating a campaign.

**Given** the authored payment-extension situation
**When** the P0 seed is validated and instantiated
**Then** it contains one authoritative obligation record linking debtor Mara and creditor Oren, with 20 gold outstanding and an authored due second of 115,200 (day 2 at 08:00)
**And** that stable record ID, balance, and deadline are part of the same branch state later extended by Story 1.24 and enriched with NPC motives by Story 2.1; neither story creates a replacement debt model.

**Given** authored content fails validation
**When** New Game or confirmation needs that content
**Then** the player receives a recoverable, factual content-unavailable state
**And** no partial campaign, fixture funding, or world clock is created.

### Story 1.5: Create a Correctable Session 0 Draft

As a player,
I want to answer Rowan and correct my draft,
So that my authored character and hopes stay accurate.

**Acceptance Criteria:**

**Given** the player enters Session 0 through New Game
**When** the common draft-start operation completes
**Then** the existing idempotent, revisioned `SessionZeroDraft` is available without a campaign branch
**And** Rowan's first question asks for the character's name.

**Given** an active Session 0 draft
**When** Rowan collects the character's name, origin, cares, hates, especially cool ideas, and campaign hopes
**Then** each exact submitted answer is durably associated with its source question
**And** an explicit “none” is accepted where applicable while an unanswered field remains incomplete.

**Given** Rowan asks a Session 0 question
**When** the player uses the shared `message-composer`
**Then** it has a visible programmatic label, Enter submits the exact answer, and Shift+Enter inserts a newline
**And** the same component and submission semantics are reused for later speech and actions, without modes, prefixes, suggested replies, action chips, or unsolicited ideas.

**Given** the player authors a character concept
**When** Rowan responds
**Then** Rowan preserves the player's authorship and asks attentive follow-up questions
**And** Rowan suggests backgrounds or ideas only after the player explicitly asks for help.

**Given** a submitted answer contradicts the authored P0 fixture or asserts unsupported authority over geography, resources, rewards, secrets, or NPC decisions
**When** the answer is validated
**Then** the draft remains unchanged for the conflicting portion and Rowan asks a neutral clarification
**And** no fictional fact, campaign event, resource, or elapsed time is created.

**Given** a valid answer submission
**When** the durable Rowan operation is pending, succeeds, fails, or is interrupted
**Then** the Session 0 surface shows the truthful operation state without presenting unacknowledged input as saved
**And** the shared `response-status` presents text and polite, deduplicated announcements without stealing focus; acknowledged answers remain available after failure or interruption.

### Story 1.6: Resume a Durable Session 0 Draft

As a player,
I want to return to an unfinished draft safely,
So that refreshes and retries do not lose or duplicate my answers.

**Acceptance Criteria:**

**Given** the same answer request is submitted again with the same request ID and payload
**When** the backend processes it
**Then** it returns the existing operation or result without creating a duplicate answer
**And** using the same request ID with different payload returns a typed conflict.

**Given** two edits target the same draft revision
**When** one commits before the other
**Then** the later stale edit is rejected with the current revision
**And** the player can recover the authoritative draft without losing unsent local text.

**Given** the browser refreshes during Session 0 or an operation reconnects
**When** the draft is requested again
**Then** saved answers, draft revision, completion state, and any active operation are restored
**And** status polling provides recovery when streaming is unavailable.

**Given** an unfinished draft is known locally
**When** the player resumes it
**Then** only a validated non-authoritative draft pointer is read from browser storage
**And** all authoritative draft content comes from the backend.

**Given** the player chooses New Game while another draft or saved campaign exists
**When** creation is confirmed
**Then** a distinct draft is created without deleting or mutating the prior draft or saves
**And** Continue remains reserved for saved campaigns rather than unfinished drafts.

**Given** Session 0 is operated with keyboard, pointer, or screen reader across supported zoom and reflow states
**When** answers are entered, submitted, retried, or restored
**Then** labels, focus order, exact submitted text, response status, and errors remain perceivable and operable
**And** typing, reading, Rowan processing, and draft correction advance zero fictional seconds.

### Story 1.7: Assign the Fixed Starting Attributes

As a player,
I want to assign the five starting scores,
So that invalid or conflicting assignments cannot become my character.

**Acceptance Criteria:**

**Given** an active Session 0 draft
**When** the player opens starting-attribute assignment
**Then** Body, Agility, Constitution, Mind, and Presence are presented with the values 8, 10, 12, 13, and 14
**And** the interface explains that every value must be used exactly once.

**Given** a partial valid assignment
**When** the player saves it
**Then** the assigned values persist with a new draft revision
**And** the draft remains incomplete until all five attributes have unique allowed values.

**Given** an assignment contains a duplicate, missing, unknown, or out-of-array value
**When** it is submitted
**Then** precise inline field errors identify the problem
**And** the last valid persisted assignment remains unchanged.

**Given** two assignment updates target the same draft revision
**When** one commits first
**Then** the stale update is rejected as a typed revision conflict
**And** the authoritative assignment can be recovered without applying a partial merge.

**Given** one or more required answers are missing or the attribute assignment is incomplete
**When** the player requests Rowan's review
**Then** review readiness is rejected with the missing requirements identified
**And** no reflection is generated from an incomplete character.

### Story 1.8: Review and Correct Rowan’s Reflection

As a player,
I want to review and correct Rowan’s reflection,
So that confirmation uses the latest agreed draft.

**Acceptance Criteria:**

**Given** all required answers and the full assignment are valid
**When** Rowan's reflection completes
**Then** it separately labels `character_fact`, `campaign_premise`, `player_preference`, and `story_hope` statements
**And** every statement retains its source-answer identity.

**Given** Rowan reflects preferences or story hopes
**When** the review is displayed
**Then** they are explicitly described as non-binding
**And** they do not enter historical truth or promise a campaign outcome.

**Given** the player changes an answer or starting assignment after a reflection exists
**When** the edit commits
**Then** the old reflection and digest become stale and confirmation is unavailable
**And** a new reflection must match the current draft revision before confirmation can proceed.

**Given** Rowan's reflection is incorrect or incomplete
**When** the player returns to edit the draft and requests another review
**Then** the corrected answers and assignments remain editable
**And** the new review replaces the prior review without creating campaign time or events.

**Given** reflection generation fails or is interrupted
**When** the player recovers Session 0
**Then** all acknowledged answers and the last valid assignment remain intact
**And** the operation can safely resume or retry without duplicating reflection records.

**Given** the assignment and review interfaces are used with keyboard, pointer, or screen reader at supported zoom and reflow states
**When** the player moves values, corrects errors, reads categories, or requests review
**Then** available, assigned, invalid, complete, pending, and ready states are conveyed in text and semantics rather than color alone
**And** focus and status announcements remain predictable.

### Story 1.9: Confirm a Character Into the Authored Starting World

As a player,
I want to confirm my reviewed character,
So that one character enters the authored world with the agreed origin.

**Acceptance Criteria:**

**Given** a complete draft with a current Rowan reflection
**When** the player explicitly confirms using the reviewed draft revision and reflection digest
**Then** the server revalidates completeness, assignment integrity, content compatibility, and reflection freshness inside one transaction
**And** no campaign is created before that explicit confirmation.

**Given** confirmation succeeds
**When** the transaction commits
**Then** it creates the immutable character origin, categorized confirmed information, initial branch, initial world revision and state hash, operation evidence, request result, and draft-to-campaign link atomically
**And** the confirmed starting-array assignment remains separately identifiable from future earned increases.

**Given** the initial branch is created
**When** its authoritative state is inspected
**Then** the player is at Market Square at game second 28,800—day 1 at 08:00
**And** Session 0 has consumed zero fictional seconds.

**Given** the approved P0 starting fixture is used
**When** the initial inventory and world content are inspected
**Then** the player owns one prepared known-value pouch containing exactly 10,000 gold and no other gold
**And** the world contains only the approved three locations, four named NPCs, and social conflict.

**Given** the player selected a character name
**When** the campaign and opening presentation are created
**Then** that selected name identifies the character
**And** “James” is never substituted as a fixed protagonist.

**Given** campaign confirmation has committed
**When** opening narration is generated
**Then** it receives only committed player-perceptible facts plus separately labeled personalization context
**And** it may make the opening tension relevant without promising a hoped-for outcome or predetermining an NPC decision.

### Story 1.10: Recover Character Confirmation Safely

As a player,
I want to recover a failed or interrupted confirmation,
So that the campaign is created once and its state stays truthful.

**Acceptance Criteria:**

**Given** confirmation fails before the authoritative transaction commits
**When** the player recovers
**Then** no campaign, branch, origin, fixture funding, or fictional time exists
**And** the draft remains editable and retryable.

**Given** confirmation commits but opening narration fails or is interrupted
**When** the operation is recovered
**Then** the campaign and branch remain authoritative
**And** only narration delivery is retried.

**Given** confirmation is repeated with the same request ID
**When** the server processes it
**Then** the existing campaign result is returned
**And** no second campaign or initial inventory is created.

**Given** concurrent confirmations use different request IDs for the same draft
**When** both reach the commit boundary
**Then** the draft uniqueness constraint permits exactly one campaign
**And** the other request recovers that campaign or receives a typed conflict without duplicate state.

**Given** the draft or reflection changed after the displayed review
**When** the player attempts confirmation with stale revision or digest data
**Then** confirmation is rejected without mutation
**And** the player must review the current draft again.

**Given** confirmation and opening narration complete
**When** the campaign route becomes active
**Then** the confirmed starting values remain immutable in authoritative state
**And** the player enters the campaign with no predetermined route, success, or ending.

### Story 1.11: Read the Main Notebook Transcript

As a player,
I want to read the current scene and transcript,
So that I can follow what happened and what I submitted.

**Acceptance Criteria:**

**Given** a confirmed campaign
**When** the Main Notebook renders
**Then** the current transcript and scene are the dominant visual surface, followed by the composer/status, current-character reference, and factual navigation
**And** the presentation uses the authoritative DESIGN color, typography, spacing, shape, and component tokens.

**Given** narration, Rowan text, NPC speech, a player intention, or a mechanical result appears
**When** it is rendered in the transcript
**Then** its speaker or message type is identified in visible text and accessible semantics before its content
**And** voice or state never depends on color alone.

**Given** prior transcript entries exist
**When** new content is appended
**Then** earlier consequences remain selectable and available in reading order
**And** the interface does not silently collapse or replace them.

**Given** the player views their persistent character reference
**When** the `character-card` renders
**Then** it shows only the current player character using text identity or a monogram
**And** it does not expose a nearby-character roster, concealed actor, or required portrait.

**Given** a newly confirmed campaign opens in the Main Notebook
**When** the character reference and opening scene render
**Then** the confirmed starting values are read-only in ordinary character-sheet use
**And** the opening uses the committed world state rather than a predetermined route or outcome.

### Story 1.12: Use Notebook Controls and Request States

As a player,
I want to use the notebook controls and see truthful request states,
So that I can navigate and understand pending work.

**Acceptance Criteria:**

**Given** the player opens a reference view available in the current story slice, such as the confirmed Character Sheet
**When** reference content is displayed
**Then** it uses the shared, accessible `reference-overlay` shell
**And** only one overlay can be open at a time; later Inventory, Roll Details, and Save/Load views reuse this shell when their content is introduced.

**Given** a reference overlay is open
**When** the player uses Tab, Shift+Tab, Escape, Close, or completes the overlay task
**Then** focus remains contained while open and returns to the invoker or stable logical target afterward
**And** opening or closing the overlay advances no fictional time.

**Given** the player reaches the Main Notebook composer after Session 0
**When** it is inspected or operated
**Then** the existing `message-composer` keeps its label, Enter/Shift+Enter semantics, exact submitted text, and accessible status treatment while routing speech and actions
**And** it adds no modes, prefixes, action suggestions, dialogue replies, recommendation chips, or generated tactical choices.

**Given** a request state is shown
**When** `response-status` updates
**Then** the Session 0 status component is reused to express the state truthfully in text and announce it politely without moving focus
**And** decorative waiting copy never claims measured progress or committed success.

### Story 1.13: Read the Notebook Accessibly at Different Sizes

As a player,
I want to read and operate the notebook with my input and display settings,
So that the same information stays available to me.

**Acceptance Criteria:**

**Given** the player uses the notebook with keyboard, pointer, or screen reader
**When** they traverse navigation, composer, transcript controls, character card, or overlays
**Then** semantic landmarks, headings, labels, reading order, visible unobscured focus, hover parity, and minimum target sizing remain correct
**And** all functionality is available without a pointer.

**Given** browser-root text enlargement, 200% zoom, or the 320 CSS px-equivalent reflow layout
**When** the notebook is displayed
**Then** navigation becomes a labeled top region and the character reference becomes a compact block in one reading column
**And** no control or content is lost and no horizontal page scrolling is required.

**Given** the player prefers reduced motion
**When** a pending-state activity mark is shown
**Then** looping motion is replaced by a static mark
**And** no narrative or status content auto-dismisses or requires timed reading.

**Given** the notebook's rendered colors and typography
**When** accessibility checks are performed
**Then** normal text meets 4.5:1, large text 3:1, essential boundaries and focus 3:1, and primary ink on paper-light targets 7:1
**And** all font sizing uses relative units that inherit the browser's root size.

**Given** the P0 notebook navigation
**When** its surfaces and settings are reviewed
**Then** no text-size setting, System notice, award notice, global roll-log tab, audio dependency, illustration pipeline, or stacked modal flow is present
**And** browser text sizing, zoom, text selection, and OS motion preferences remain authoritative.

### Story 1.14: Walk to Mara's Stall Through a Complete Action

As a player,
I want to tell Rowan I walk to Mara's Stall and arrive there,
So that my first in-world intention produces a truthful, persistent result.

**Acceptance Criteria:**

**Given** a confirmed branch at Market Square and a ready Main Notebook
**When** the player submits “I walk to Mara's Stall” or an ordinary equivalent through the established composer
**Then** the browser appends the exact `player-intention`, creates one unique request ID, and visibly acknowledges submission within the 100 ms target without claiming arrival
**And** the existing durable operation contract records the branch, expected world revision, payload digest, and truthful status.

**Given** that submitted walk
**When** `POST /api/branches/{branchId}/actions` accepts and interprets it
**Then** acceptance returns `202 Accepted` with operation, status, and event URLs, and the provider-neutral proposal identifies the player, Mara's Stall, the authored 7 m route, and walking mode without treating the player's words as a direct state edit
**And** invalid proposal data, an unknown route, or a stale revision yields a typed factual failure with no travel or elapsed time.

**Given** the proposed walk passes route and current-location validation
**When** its known destination and five-second cost are shown and the action resolves
**Then** one atomic world commit moves the player to Mara's Stall, advances the shared clock from 28,800 to 28,805, and records a no-roll result, action evidence, operation result, new revision, and state hash
**And** no die, resource charge, or second movement is introduced.

**Given** the walk has committed
**When** the operation completes or the browser refreshes
**Then** the player can read a factual arrival result and the current location and clock from authoritative state
**And** any failed generated prose is replaced with a truthful committed-result fallback without rerunning the walk.

**Given** the walk request is repeated with the same ID and payload or the connection drops before the result is seen
**When** its durable status or result is recovered through event replay or polling
**Then** the original committed arrival or explicit pre-commit failure is shown with its commit boundary
**And** time, location, action record, and narration fallback are not duplicated; a changed payload under that ID is a conflict.

**Given** one mutating operation is unresolved on a branch
**When** another mutation is submitted
**Then** the second request receives a typed busy conflict or waits only through an explicitly defined recovery path
**And** read-only game queries remain available.

### Story 1.15: Recover an Interrupted Walk

As a player,
I want to recover my walk after a connection loss or interruption,
So that I can tell whether I arrived without moving twice.

**Acceptance Criteria:**

**Given** the player has submitted the supported walk and the event stream disconnects
**When** the browser reconnects with the last received event ID
**Then** monotonically identified events resume without duplication
**And** status polling recovers the committed arrival or the explicit uncommitted state if streaming remains unavailable.

**Given** the browser refreshes while that walk is active
**When** the operation status is fetched
**Then** the existing operation and exact submitted intention are restored
**And** the player can continue to the same completed arrival or safely retry only uncommitted work without creating a second walk.

**Given** the player cancels an accepted but unresolved walk
**When** cancellation succeeds before interpretation or action work begins
**Then** queued work stops and the operation becomes recoverably interrupted
**And** no world state, time, roll, cost, or result is committed.

**Given** the walk is retried with the same request ID and identical payload
**When** the operation endpoint receives it
**Then** the existing operation or final result is returned
**And** a different payload under that request ID is rejected as a conflict.

**Given** the walk returns an accepted operation, completed arrival, or typed rejection
**When** the browser reads the response
**Then** success and RFC 9457 problem payloads pass generated Zod validation before use
**And** malformed transport data cannot be mistaken for an accepted action.

### Story 1.16: Clarify and Reject Ambiguous World Intentions

As a player,
I want Rowan to clarify an unclear destination or explain an unsupported request,
So that I can complete or abandon the intention without a false world change.

**Acceptance Criteria:**

**Given** the player submits an ordinary synonym for walking to Mara's Stall
**When** the provider-neutral interpreter processes it
**Then** strict versioned contracts separate proposed action, actor, targets, player speech, asserted claims, duration, clarification needs, stakes, and candidate consequences
**And** provider-specific data remains confined to the LLM adapter while a valid synonym completes the same five-second arrival from Story 1.14.

**Given** model output is malformed, contains unknown fields, or violates its contract
**When** boundary validation runs
**Then** the proposal is rejected before application code uses it
**And** no world state, time, random result, resource, or player-facing success is committed.

**Given** the player asserts an authoritative fact such as owning a shop
**When** the proposal is validated
**Then** the assertion is treated as speech or intent rather than direct state mutation
**And** ownership changes only through a supported validated action.

**Given** an intention is impossible or unsupported in P0
**When** validation rejects it
**Then** the player receives a factual explanation with no mutation or fictional-time cost
**And** the request reaches a visible terminal result without an unsolicited alternative action or strategy.

**Given** an intention is materially ambiguous
**When** required actor, target, meaning, order, or commitment information is missing
**Then** the operation enters `needs_clarification` with a neutral, intent-preserving question
**And** clarification commits no fictional time, world change, or recommended tactic; answering with Mara's Stall resumes the same request and completes the authored walk once.

**Given** a clarification operation is interrupted or the backend restarts
**When** its status is recovered
**Then** the validated question and draft proposal remain paused under the same operation identity
**And** the player can answer to complete the walk or abandon it with a terminal no-change result without creating a second world action.

**Given** an LLM-mediated interpretation has not completed by 30 seconds
**When** the interruption target is reached
**Then** the player receives a recoverable pending or interrupted state based on the durable status query
**And** recovery resolves to the same arrival or an explicit uncommitted outcome without claiming a world commitment before that boundary exists.

### Story 1.17: Choose a Faster Route With Declared Cost

As a player,
I want to choose to jog to Mara's Stall after seeing the time cost,
So that the committed movement matches the route and mode I intended.

**Acceptance Criteria:**

**Given** the player is at Market Square and asks to jog to Mara's Stall
**When** rules validate the actor, current place, authored route, mode, and duration
**Then** the player sees the destination and three-second cost before commitment and may confirm or decline
**And** confirmation completes one no-roll move to Mara's Stall, advances the clock by exactly three seconds, and presents an inspectable result; declining changes nothing.

**Given** a consequential action has reasonably knowable stakes, costs, or interpretation
**When** it is ready for commitment
**Then** those details are exposed before resolution
**And** the same pre-commit contract is reused by later purchase, pouch gift, and uncertain-check stories; rare-resource spending or a materially changed interpretation requires explicit clarification when those actions are introduced.

**Given** a request contains multiple consequential actions
**When** order or stopping conditions affect the outcome
**Then** the proposed order, stakes, and stopping conditions are exposed before commitment
**And** the player receives a complete no-change result asking for separate submissions if a safe composite cannot be supported.

**Given** the jog proposal passes validation and the player confirms
**When** it resolves
**Then** no random input is sampled, the completed three-second segment is accumulated, and one complete change set is built
**And** expected world revision is checked again inside the write transaction.

**Given** the authoritative transaction succeeds
**When** the action commits
**Then** subject state, immutable action record, request result, committed operation status, new world revision, state hash, and domain-event evidence are written atomically
**And** the player sees the committed jog result; external side effects occur only after commit.

**Given** an operation moves from interpretation through validation and resolution
**When** its durable status is read
**Then** only the transitions reached by completed work are shown as interpreting, needs-clarification, validating, resolving, or committed
**And** committed status identifies the authoritative world revision and `world` commit boundary.

### Story 1.18: Revisit a Committed Arrival Safely

As a player,
I want to revisit a completed walk or jog and hear what happened,
So that presentation failures and retries cannot rewrite my arrival.

**Acceptance Criteria:**

**Given** the walk or jog to Mara's Stall has committed
**When** Rowan describes or re-describes the arrival
**Then** narration receives committed player-perceptible facts and presentation context only
**And** the player sees the arrival and elapsed time even if generated prose fails; narration cannot request a mutation, reorder committed events, reveal hidden facts, or contradict the mechanical outcome.

**Given** arrival narration fails after movement commits
**When** the operation is recovered
**Then** committed mechanics remain unchanged
**And** narration can be retried independently while the player can still inspect the committed location and clock, without repeating interpretation, resolution, random sampling, time, or costs.

**Given** a reusable route or movement ruling is accepted
**When** it is referenced later or after save/load
**Then** it retains a stable identity and recorded version
**And** regenerated prose cannot silently change its mechanics.

**Given** a stale expected world revision or duplicate walk or jog request reaches resolution
**When** the commit coordinator checks it
**Then** stale work returns a typed conflict and duplicate work returns the prior result
**And** neither path creates a second mutation.

**Given** narration is pending after authoritative commit
**When** the operation is queried, cancelled, or recovered after a restart
**Then** it reports committed-but-narrating truthfully and may stop or retry only narration delivery
**And** the atomic request result prevents any repeated mechanics, time, roll, cost, or XP award.

**Given** an operation completes or fails after action resolution
**When** its typed result is returned
**Then** it identifies the subject, commit boundary (`none`, `draft`, or `world`), committed revision when present, and safe recovery capability
**And** unknown, uncommitted, and already-committed work remain distinguishable after interruption.

### Story 1.19: Explore the Three Authored P0 Locations

As a player,
I want to explore the stable authored P0 places,
So that exits and descriptions reflect the world.

**Acceptance Criteria:**

**Given** authored P0 geography
**When** the player inspects navigation
**Then** Market Square connects to Mara's Stall and the Common Room using stable authored routes
**And** no location or connection is procedurally generated.

**Given** the player follows a factual linked exit or states a supported walking intention toward the Common Room
**When** the authored 140 m segment completes from Market Square
**Then** the player arrives at the Common Room through the same validated, committed, recoverable action path as Story 1.14 and the clock advances 100 seconds
**And** returning through an authored exit also completes with a truthful location and clock result.

**Given** the player enters a location for the first time or revisits it
**When** its description is rendered
**Then** first introductions use 60–120 words and repeat descriptions use 20–60 words emphasizing actual changes
**And** exits, perceptible people, and examinable context remain factual controls rather than action recommendations.

### Story 1.20: Travel on the Shared World Clock

As a player,
I want to move through authored routes at a chosen supported speed,
So that completed travel consumes the correct game time.

**Acceptance Criteria:**

**Given** an action is reading, typing, opening a menu, inspecting known information, viewing inventory or journal, or saving
**When** it completes
**Then** zero fictional seconds advance
**And** closing the game or waiting for a model also leaves the game clock paused.

**Given** the player moves along the established 7 m Market Square–Mara's Stall route or 140 m Market Square–Common Room route
**When** walking at 1.4 m/s
**Then** the completed segment advances 5 seconds or 100 seconds respectively
**And** travel uses `distance / speed`, rounds each segment up to a whole second, and records the chosen movement mode.

**Given** the player chooses a supported ordinary-ground mode
**When** travel is calculated
**Then** walk 1.4, jog 2.8, sprint 5.6, and crawl 0.5 m/s are applied
**And** an unknown route or mode requires a supported distance/speed ruling before time advances.

### Story 1.21: Converse and Purchase With Actual Handling Time

As a player,
I want to speak and purchase goods with actual time and stock,
So that ordinary transactions reconcile with the shared clock.

**Acceptance Criteria:**

**Given** a completed dialogue exchange contains rendered spoken words
**When** its duration is committed
**Then** time advances by `15 × ceil(total spoken words / 30)` seconds with a 15-second minimum for nonempty speech
**And** descriptive prose, player instructions, model reasoning, and unspoken interrupted dialogue are excluded.

**Given** the player purchases one of Mara's five drinks for 1 gold
**When** known price, stock, funds, consent, and intended purchase validate
**Then** the actual speech and handling durations, player funds, Mara's funds/stock, possession, and ownership reconcile atomically
**And** a retry cannot charge time or gold or transfer stock twice.

### Story 1.22: Transfer a Prepared Pouch Without Duplicate Ownership

As a player,
I want to transfer counted containers or loose coins,
So that handling and handover reflect what physically completed.

**Acceptance Criteria:**

**Given** the controlled handling fixtures
**When** the prepared 10,000-gold pouch is transferred or 100 loose coins are individually counted
**Then** the pouch handover uses the approved 5 seconds while loose counting takes at least 100 seconds
**And** the 100 loose coins never enter the player's wealth or purchase/gift branches.

**Given** a transfer is interrupted before its completion boundary
**When** elapsed phases commit
**Then** completed elapsed time and the interrupting event may persist
**And** funds, possession, and ownership remain unchanged until the handover completes.

**Given** the captured P0 starting state
**When** independent purchase, gift-test, and no-gift-test fixture copies are created
**Then** each copy begins with the same untouched prepared pouch and distinct branch identity
**And** spending 1 gold in the purchase copy cannot reduce or otherwise alter either comparison copy.

### Story 1.23: Wait for Time or Real Events

As a player,
I want to wait for a clock target or an actual event,
So that silence and scheduled events advance without invented outcomes.

**Acceptance Criteria:**

**Given** the player waits until the next morning from 22:00
**When** “morning” resolves to the next 06:00
**Then** 28,800 seconds are eligible to advance unless a response-worthy event interrupts
**And** an uneventful overnight wait is not interrupted every minute.

**Given** the player waits face-to-face for an NPC action
**When** the requested event has not occurred after 60 silent seconds
**Then** control returns with the observation that one minute passed
**And** continuing the wait does not manufacture the requested NPC decision.

**Given** a wait targets an actual scheduled event
**When** the deterministic scheduler reaches it
**Then** the world advances to the event's real game second and interrupts if player attention is required
**And** an impossible or unscheduled target is reported rather than allowed to wait forever.

**Given** a timed action crosses one or more scheduled events
**When** time advances
**Then** events are processed by due game second, priority, and stable insertion sequence within a bounded work budget
**And** identical recorded state and random inputs reproduce the same mechanical timing and outcome.

### Story 1.24: Resolve an Uncertain Check With Declared Odds

As a player,
I want to understand and resolve an uncertain action,
So that the die, difficulty, and admitted consequence remain fair.

**Acceptance Criteria:**

**Given** a character with Body, Agility, Constitution, Mind, and Presence scores
**When** an attribute modifier is required
**Then** it is calculated as `floor((score - 10) / 2)`
**And** the confirmed starting assignment remains immutable while current scores may later increase.

**Given** an eligible uncertain intention
**When** the action is prepared
**Then** its contextual difficulty, attribute modifier, relevant skill bonus, knowable stakes, and pre-roll success probability are fixed and recorded before rolling
**And** impossible or unsupported intentions are rejected before any roll.

**Given** one fair d20 is rolled
**When** the result resolves
**Then** natural 1 automatically fails, natural 20 automatically succeeds, and faces 2–19 use `d20 + attribute modifier + skill bonus >= difficulty`
**And** the natural-roll overrides do not make an otherwise impossible action possible.

**Given** the controlled payment-extension fixture uses Presence 14, Persuasion +1, and difficulty 12
**When** the probability is calculated
**Then** the total bonus is +3 and the pre-roll success probability is 60%
**And** the target is the existing Story 1.4 Mara-to-Oren obligation record, whose original due second is 115,200; success sets that record's due second to 201,600, while failure leaves it at 115,200 without reversing any earlier committed transaction or creating a second obligation.

**Given** an uncertain social action succeeds
**When** its consequence is committed
**Then** only the admitted and validated check outcome is committed
**And** success cannot imply obedience, remove an obligation, or impose an unsupported NPC plan.

**Given** the same unchanged task is attempted after competence increases
**When** contextual difficulty is chosen
**Then** the difficulty is not raised merely to cancel the earned bonus
**And** genuinely harder chosen feats may still receive appropriately higher declared targets.

### Story 1.25: Earn Player and Skill Progression

As a player,
I want to earn persistent growth from meaningful success,
So that competence improves without duplicate or artificial caps.

**Acceptance Criteria:**

**Given** a meaningful check succeeds with pre-roll probability `p`
**When** XP is awarded
**Then** both the player track and relevant-skill track receive `floor(100 × (0.95 - p) / 0.90)` XP exactly once
**And** 95%, 60%, and 5% success probabilities award 0, 38, and 100 XP respectively.

**Given** a check fails, requires no roll, is rejected, repeats an unchanged failed approach, or replays an already resolved request
**When** progression is evaluated
**Then** it awards zero XP
**And** no duplicate opportunity is created by retry, bonus suppression, or narration replay.

**Given** a player or skill track starts at level 1 with 0 XP
**When** accumulated XP reaches `100 × current level`
**Then** that threshold is consumed, excess carries forward, and additional crossed levels resolve in the same commit
**And** a player level grants one attribute point while a skill level grants +1 to that skill bonus.

**Given** a controlled high-bonus fixture exceeds earlier proposed attribute or skill limits
**When** progression and checks resolve
**Then** no maximum level, attribute, or skill bonus clamps the character
**And** the resulting actual probability still remains bounded by natural 1 and 20.

### Story 1.26: Allocate Earned Attributes

As a player,
I want to allocate earned points,
So that my current scores change only after valid confirmation.

**Acceptance Criteria:**

**Given** progression produces an unspent attribute point
**When** the player opens `attribute-allocation`
**Then** earned, spent, and unspent counts plus current and immutable starting scores are shown
**And** the player can preview one or more positive integer increases without changing authoritative state.

**Given** a valid allocation preview within the available balance
**When** the player explicitly confirms it
**Then** current attributes and point balances commit atomically, idempotently, and at zero fictional-time cost
**And** the immutable starting-array record remains unchanged.

**Given** an allocation overspends, uses an invalid attribute, uses a nonpositive increase, or targets a stale revision
**When** confirmation is attempted
**Then** precise field or conflict errors are returned without mutation
**And** the last persisted scores and point balance remain authoritative.

### Story 1.27: Recall Known Facts in Rowan and Journal

As a player,
I want to inspect only what my character knows,
So that the journal and Rowan do not reveal hidden state.

**Acceptance Criteria:**

**Given** the player asks Rowan a known-information question such as “What do I know about Mara's debt?”
**When** the composer classifies the request
**Then** Rowan answers from the character's legitimately known evidence
**And** the question, response, and transcript evidence persist without advancing fictional time.

**Given** the requested information is unknown to the character
**When** Rowan answers
**Then** Rowan plainly states that the character does not know
**And** no concealed actor, private plan, hidden belief, or diagnostic provenance is revealed.

**Given** the Journal query succeeds with no known entries
**When** the Journal opens
**Then** it displays an explicit known-empty state
**And** it does not invent concerns, commitments, secrets, or suggested next actions.

**Given** the character knows facts, concerns, evidence, or explicit commitments
**When** the Journal opens
**Then** entries restate only that known information in text-first rows with worded statuses
**And** uncertainty, source, and commitment state are shown when legitimately known.

### Story 1.28: Inspect Inventory and Character State

As a player,
I want to inspect my inventory and character sheet,
So that owned items and progression remain clear.

**Acceptance Criteria:**

**Given** the Inventory query succeeds with no owned items or with populated contents
**When** the Inventory overlay opens
**Then** it distinguishes empty from populated state and shows authoritative known possession, quantities, and money
**And** scenery, hidden simulation content, and unowned items do not appear as takeable inventory.

**Given** the Character Sheet opens during P0 play
**When** progression data is displayed
**Then** immutable starting scores, current scores, player and skill XP/levels, skill bonuses, and earned/spent/unspent attribute points are distinct
**And** P6 titles, achievements, affinities, and spells are absent.

**Given** Journal, Inventory, Character Sheet, or Result Details is loading or fails
**When** the overlay renders
**Then** loading, successful empty/populated, stale prior content, and error states remain distinguishable
**And** failed or schema-invalid reads never masquerade as empty data or enable mutation from an unknown revision.

**Given** any player-facing query is projected
**When** backend authorization and knowledge filtering run
**Then** concealed actors, private NPC plans, unknown beliefs, hidden objectives, unrestricted provider content, and diagnostic-only state are removed before serialization
**And** the browser validates the resulting success or problem response before rendering it.

**Given** the information overlays are opened, read, and closed
**When** the player uses keyboard, pointer, or screen reader at supported zoom and reflow states
**Then** focus containment/return, accessible names, reading order, target sizing, internal scrolling, and status announcements remain correct
**And** no inspection action advances fictional time.

**Given** a local information view has already loaded
**When** the player opens it or switches its local section
**Then** the interaction meets the approved 200 ms local-menu target under the evaluation setup
**And** there is no global roll-log tab or omniscient roster.

### Story 1.29: Inspect Mechanical Results

As a player,
I want to inspect how an action resolved,
So that rolled and routine results are explained from recorded evidence.

**Acceptance Criteria:**

**Given** a check result is displayed
**When** the player inspects its inline mechanical summary
**Then** it identifies the skill, rolled or no-roll status, result, and whether XP was awarded
**And** narration agrees with the committed die, total, consequence, and progression.

**Given** a transcript result resolved without a roll
**When** its `mechanical-result` control opens Roll Details
**Then** the overlay states that no roll was needed and explains the validated rationale, time, cost, and committed consequence
**And** it does not fabricate a die result or hidden reasoning.

**Given** a transcript result used a roll
**When** its Roll Details open
**Then** the view shows the declared difficulty, applicable modifiers and sources, successful-face probability, die, total, success/failure, committed consequence, and XP outcome
**And** all values match the immutable result evidence.

**Given** result evidence is missing, corrupt, or unreadable
**When** Roll Details is requested
**Then** the interface reports that exact failure state
**And** neither Rowan nor the client reconstructs an explanation from guesses.

### Story 1.30: Save a Complete Branch in a Manual Slot

As a player,
I want to save the complete branch in one of three slots,
So that the previous durable save survives conflicts and failures.

**Acceptance Criteria:**

**Given** a campaign branch and one of three numbered save slots
**When** the player opens Save/Load
**Then** every slot is explicitly identified as empty, occupied, or unavailable
**And** occupied slots show campaign identity, known place, game second, saved-at time, compatibility, and slot revision.

**Given** the player saves into an empty slot
**When** the request includes the current branch revision, expected slot revision, and request ID
**Then** one immutable complete snapshot is committed and the slot revision advances
**And** saving consumes zero fictional seconds and restores no resources or items.

**Given** the player selects an occupied slot for saving
**When** overwrite confirmation opens
**Then** it names the existing save and requires explicit confirmation against that slot revision
**And** cancelling returns focus without changing the slot.

**Given** an occupied slot changes after overwrite confirmation is displayed
**When** the stale overwrite is submitted
**Then** a typed slot-revision conflict is returned
**And** the newer save remains intact.

**Given** a save write, validation, or storage operation fails
**When** the operation terminates
**Then** the previously durable slot remains unchanged and readable
**And** the UI reports failure and a safe recovery path without claiming success.

**Given** a save commits successfully
**When** its snapshot is inspected
**Then** it includes every authoritative state type introduced through Epic 1: clock, authored-content/schema versions, fixture and branch origin, inventory, money, possession, ownership, scheduled events, operation-safe state, character origin, starting and current attributes, player/skill XP and levels, bonuses, allocations, and unspent points
**And** its versioned snapshot contract preserves causal identifiers and state hashes so later Epic 2 state types must extend the same complete save/load path when introduced.

### Story 1.31: Load a Compatible Branch Without State Leakage

As a player,
I want to restore a compatible saved branch,
So that old or incompatible state cannot corrupt my current campaign.

**Acceptance Criteria:**

**Given** at least one compatible occupied save slot exists
**When** the save index loads and the player activates Continue from Title
**Then** one accessible save-selection overlay opens with no slot preselected or silently loaded
**And** each empty, occupied, or unavailable row identifies its slot and state in text, including campaign identity, known place, in-world time, saved-at time, compatibility, and selection state where available.

**Given** save selection is open
**When** the player presses Escape, activates Close, or completes a successful selection
**Then** focus is contained while open and returns predictably afterward
**And** no second overlay is stacked.

**Given** the player confirms an occupied compatible Title slot
**When** load begins
**Then** the selected slot identity and revision reach the typed load boundary and the UI shows loading, success, or failure
**And** the active campaign changes only after successful validation and commit.

**Given** the player chooses a compatible occupied slot
**When** load is submitted with the selected slot revision and request ID
**Then** the snapshot is validated and a recovered branch is activated only after the load transaction succeeds
**And** the previously active branch remains active if validation or commit fails.

**Given** a save uses an unsupported schema, content version, or corrupted state
**When** load validation runs
**Then** the application rejects it before mutation with a safe compatibility or integrity error
**And** it does not silently drop, default, or regenerate missing causal state.

**Given** an unresolved branch mutation exists
**When** the player attempts save or load
**Then** the application requires that operation to settle or be recovered first and returns a typed busy conflict while its commit state is unknown
**And** save/load never races the mutation.

**Given** a saved branch is loaded
**When** the Main Notebook and reference views refresh
**Then** time, location, money, inventory, ownership, confirmed starting attributes, current attributes, XP, levels, bonuses, and allocated/unspent points match the snapshot
**And** late responses from the previously active branch cannot alter the restored transcript or state.

**Given** the active branch changes after a successful load
**When** a late event or query response arrives for the prior branch
**Then** it remains attached only to its original operation subject
**And** it cannot append to or replace the loaded branch's transcript or state.

**Given** two branches diverged from the same captured state
**When** either is loaded
**Then** it restores only its own clock, knowledge, progression, inventory, rewards, and consequences
**And** abandoned-branch state never carries across.

### Story 1.32: Replay and Revisit a Saved Choice

As a player,
I want to revisit a saved choice and inspect reproducible outcomes,
So that branch comparison remains isolated and timely.

**Acceptance Criteria:**

**Given** the same captured initial state, structured proposals, and recorded random inputs
**When** a branch is replayed for evidence
**Then** its mechanical results are reproducible
**And** fresh LLM prose is not required to match word-for-word.

**Given** a player wants to revisit an earlier choice
**When** they load an older manual save
**Then** the load is allowed as the supported branch-comparison mechanism
**And** no per-action undo or cross-save progression system is introduced.

**Given** the evaluation environment and a valid ordinary-size save
**When** saving or loading completes
**Then** it meets the approved 2-second target
**And** progress, overwrite, failure, success, and recovered-prior-state changes are announced without stealing focus.

### Story 1.33: Inspect Read-Only Causal Diagnostics

As a playtester,
I want to inspect read-only causal evidence during local playtesting,
So that I can trace an outcome without changing the live branch.

**Acceptance Criteria:**

**Given** the backend is loopback-bound and starts with `DMUD_DEVTOOLS=true`
**When** the frontend requests diagnostic capabilities
**Then** a typed capability response enables read-only development tools
**And** build mode alone cannot enable them.

**Given** dev tools are disabled or the application is not loopback-bound
**When** a diagnostic route is requested
**Then** privileged diagnostic state is unavailable
**And** test-only cheats, seed injection, fixture mutation, and state-changing controls are not registered as release routes.

**Given** a committed or rejected action
**When** its diagnostic timeline is opened
**Then** it can show the submitted intention, validated proposal, validation decisions, recorded random inputs, completed phases, committed change set, domain events, resulting revision/hash, narration status, and correlated logs
**And** the view cannot mutate or replay the live branch.

**Given** the playtester inspects social and simulation state
**When** diagnostic projections load
**Then** the already implemented causal records, clock, and scheduled-event queue remain separately identifiable, and later social facts, observations, claims, beliefs, NPC plans, and reasons extend this read-only projection when their stories add them
**And** operational logs are never treated as authoritative game truth.

### Story 1.34: Export Redacted Operation Diagnostics

As a playtester,
I want to read and export correlated diagnostic evidence,
So that I can investigate failures without disclosing secrets.

**Acceptance Criteria:**

**Given** structured application logging is active
**When** operations, commits, saves, loads, failures, retries, or repairs occur
**Then** rotating local JSONL and readable development logs include applicable correlation, operation, branch, revision, duration, and outcome fields
**And** credentials, hidden objectives, complete saves, and unrestricted provider payloads are excluded.

**Given** a player or developer exports a diagnostic bundle
**When** the export is created
**Then** it contains the evidence needed to investigate the selected operations, versions, hashes, latency, token usage, cost, duplicate attempts, rejected proposals, and contradiction repairs
**And** secret and hidden-state redaction is applied consistently.

### Story 1.35: Run a Packaged Local Campaign

As a player,
I want to launch the finished local build,
So that a campaign works without a development server.

**Acceptance Criteria:**

**Given** a packaged production build
**When** the application starts
**Then** FastAPI serves the SPA and API from one loopback-only origin
**And** no remote binding, account system, cloud service, or external broker is required.

**Given** the completed P0 application is checked in
**When** its baseline quality commands run independently
**Then** formatting, linting, strict type checking, backend integration tests, frontend tests, OpenAPI drift checks, and a real-browser startup journey pass
**And** only the external LLM boundary is eligible for a deterministic test substitute.


## Epic 2: Make Consequences Travel Through People

Players can change an NPC's feasible opportunities and later observe information travel through witnesses, fallible reports, beliefs, and motive-based NPC choices without omniscience or scripted outcomes.

### Story 2.1: Give the Four P0 NPCs Grounded State

As a player,
I want to meet residents with distinct needs and obligations,
So that their choices begin from authored circumstances.

**Acceptance Criteria:**

**Given** a new P0 branch
**When** Mara, Oren, Tessa, and Ivo are instantiated from authored content
**Then** each has explicit resources, needs, competing desires, obligations, relationships, current plan, location, and limited knowledge
**And** their richer NPC state references and extends the same Mara-to-Oren obligation ID and current deadline seeded in Story 1.4, preserving any Story 1.24 extension; no fifth named NPC, broader merchant network, or duplicate debt model is added.

**Given** Mara's initial authored state
**When** it is inspected through development diagnostics
**Then** she owes Oren 20 gold, wants to clear the debt, and also wants to visit her ill sister
**And** neither desire predetermines what she must choose after circumstances change.

**Given** Oren's initial authored state
**When** it is inspected
**Then** he is Mara's creditor and values repayment and dependable trade
**And** his obligation and relationship context constrain supported responses.

**Given** Tessa and Ivo's initial authored states
**When** they are inspected
**Then** Tessa is a neighboring trader and Ivo is a courier and Tessa's friend
**And** the controlled rumor variant can use Ivo's recorded distrust without making distrust universal in every branch.

### Story 2.2: Let NPCs Choose Feasible Plans

As a player,
I want to observe residents choosing feasible plans,
So that their behavior changes with knowledge and resources.

**Acceptance Criteria:**

**Given** an NPC considers a plan
**When** feasible options are generated
**Then** resources, needs, desires, obligations, relationships, individual knowledge, location, risk, and available time constrain those options
**And** unavailable resources, unknown facts, or unsupported actions cannot appear in the plan.

**Given** an NPC performs routine scheduled behavior
**When** no consequential interpretation or replanning is required
**Then** deterministic rules select and execute the supported plan
**And** the action uses the same authoritative time, transaction, and event contracts as player actions.

**Given** circumstances require consequential dialogue or replanning
**When** the LLM proposes an NPC response or plan
**Then** the proposal is validated against that NPC's actual state and feasible actions before commitment
**And** the LLM cannot invent money, knowledge, permission, obligations, or a guaranteed outcome.

**Given** multiple feasible plans remain after validation
**When** one is selected
**Then** the committed plan records its motive-based reasons and relevant constraints for diagnostics
**And** the player-facing presentation reveals only what the character can legitimately perceive.

**Given** NPC state is saved and loaded
**When** the branch resumes
**Then** resources, needs, desires, obligations, relationships, knowledge, current plan, plan status, and recorded reasons are restored together
**And** loading does not trigger an unrecorded replan.

### Story 2.3: Record Facts and Actual Witness Observations

As a player,
I want nearby people to remember only what they could perceive,
So that a later gift or report has a trustworthy causal source.

**Acceptance Criteria:**

**Given** a supported world event commits
**When** its historical fact is recorded
**Then** the fact has a stable typed identity, event source, place, game time, and authoritative details
**And** it is distinct from every participant or witness observation.

**Given** an NPC actually perceives a completed event
**When** observation capture runs in the same authoritative commit
**Then** the typed observation records witness, source fact, place, time, perceptible details, and uncertainty
**And** it excludes hidden motives, unobservable mechanics, and facts beyond that witness's perception.

**Given** an NPC is absent, blocked from perceiving the event, or the action never completes
**When** witness capture evaluates the event
**Then** that NPC receives no observation
**And** historical truth is never copied into non-witness knowledge by default.

**Given** the supported event or its operation is retried or a branch is saved and loaded
**When** causal records are inspected
**Then** each fact and observation keeps its stable ID, source link, and insertion order without duplication
**And** the player-facing projection reveals only information legitimately learned by the player character.

### Story 2.4: Complete a Witnessed Full-Pouch Gift

As a player,
I want to give Mara the prepared pouch in view of Tessa,
So that the transfer and witnesses reflect a completed action.

**Acceptance Criteria:**

**Given** the captured P0 starting state for the gift comparison
**When** the gift or no-gift branch begins
**Then** it receives an isolated copy containing the untouched prepared pouch with exactly 10,000 gold and no other player gold
**And** no purchase-branch or sibling-branch mutation is present.

**Given** either isolated comparison branch leaves the day-1 08:00 Market Square capture
**When** the same five-second authored walk reaches Mara's Stall with Mara and Tessa present
**Then** the branch records one `p0-gift-opportunity` event with a branch-local stable ID and game second 28,805 before the gift/no-gift decision
**And** both branches retain the same opportunity timestamp and fixture marker even if no gift occurs; retries cannot record it twice.

**Given** the player offers Mara the full prepared pouch
**When** the intention is interpreted
**Then** the known recipient, entire 10,000-gold amount, five-second handover, and loss of the player's only gold are exposed before commitment
**And** materially different or ambiguous gift intent requires clarification.

**Given** Mara can receive the pouch and the handover completes
**When** the gift transaction commits
**Then** possession, ownership, player wealth, Mara's resources, elapsed time, historical fact, and action evidence change atomically exactly once
**And** the player no longer owns any gold in that branch.

**Given** the handover is rejected, cancelled, or interrupted before completion
**When** the operation terminates
**Then** no pouch, ownership, or wealth transfer occurs
**And** only legitimately completed elapsed phases or interrupting events may persist.

**Given** the gift occurs where Mara and Tessa can perceive it
**When** the transaction commits
**Then** Mara receives a recipient observation and Tessa receives a witness observation containing only perceptible details
**And** Oren, Ivo, and other non-witness knowledge remain unchanged.

### Story 2.5: Compare Mara’s Gift and No-Gift Opportunities

As a player,
I want to see how the gift changes Mara’s feasible choices,
So that both branches stay causal and independent.

**Acceptance Criteria:**

**Given** the player gives Mara substantial resources
**When** future plan selection occurs
**Then** retirement, investment, debt payment, travel, refusal, or another supported option remains contingent on her situation
**And** no universal “gift enough money = obedience” rule exists.

**Given** Mara's resources increase by 10,000 gold
**When** her feasible opportunity set is recalculated
**Then** plans that were previously unaffordable may become feasible while existing needs, desires, debt, relationships, obligations, knowledge, risk, and time still constrain selection
**And** no fixed retirement, repayment, travel, investment, or refusal script is imposed.

**Given** Mara selects a post-gift plan
**When** it commits
**Then** the selected plan records the state and motive-based reasons that made it eligible and preferable
**And** any effect on Oren occurs through supported actions, obligations, contact, or resource changes rather than instant omniscience.

**Given** the corresponding no-gift branch advances through the same opportunity
**When** Mara replans or continues her prior plan
**Then** her feasible choices reflect the absence of the transferred resources
**And** the comparison does not require her to choose a single predetermined no-gift behavior.

**Given** the player observes Mara after either branch
**When** Rowan narrates changed schedules, spending, fulfilled obligations, refusal, or another visible consequence
**Then** narration is derived from committed behavior and player-perceptible facts
**And** an internal plan flag alone is not presented as proof that the world remembered.

**Given** the gift request is retried, reconnected, or narrated again
**When** idempotency is evaluated
**Then** the original transfer result is returned
**And** the pouch, time, observations, and replanning trigger are not duplicated.

**Given** either branch is saved and loaded
**When** play resumes
**Then** its resources, ownership, fact, witness observations, Mara's opportunity set, selected plan, reasons, and resulting schedule are restored
**And** no state crosses into the other branch.

### Story 2.6: Schedule Contact and Record a Spoken Claim

As a player,
I want Tessa's report to require a real meeting with Ivo,
So that a claim has a supported path through the world.

**Acceptance Criteria:**

**Given** the branch-local `p0-gift-opportunity` event from Story 2.4 is recorded at second 28,805
**When** the scheduler reaches 1,800 seconds after that event
**Then** Tessa and Ivo meet in the Common Room at second 30,605 in both gift and no-gift branches unless a committed interruption changes their ability to meet
**And** the meeting follows the shared clock rather than an out-of-band timer.

**Given** Ivo has not witnessed the gift and has received no claim
**When** his knowledge is queried before the meeting
**Then** he knows nothing about the gift
**And** authoritative event or ownership records do not leak into his beliefs.

**Given** Tessa and Ivo are not participants in the same valid encounter
**When** a transmission is proposed
**Then** the claim is rejected as unsupported
**And** no listener belief or implied off-screen conversation is created.

**Given** Tessa witnessed the gift and meets Ivo
**When** she communicates a supported report
**Then** the claim records speaker, listener, encounter, communicated meaning, acquisition time, and disclosed or undisclosed source
**And** the claim may be truthful, mistaken, incomplete, distorted, or deceptive without changing the original fact.

### Story 2.7: Let Ivo Form a Belief From Tessa’s Claim

As a player,
I want to see Tessa’s report reach Ivo through a real meeting,
So that claims and beliefs have a traceable source.

**Acceptance Criteria:**

**Given** Ivo receives a valid claim
**When** his belief is updated
**Then** the belief records subject, proposition, source, confidence, provenance, acquisition time, uncertainty, and its relationship to known truth where appropriate
**And** prior beliefs remain in history rather than being overwritten.

**Given** the no-gift branch reaches the same meeting
**When** Tessa has no witnessed gift to report
**Then** no gift claim is created merely because the scheduled contact occurred
**And** Ivo does not acquire knowledge from the corresponding gift branch.

**Given** a claim transmission is retried with the same logical request identity
**When** it is processed
**Then** the original transmission result is returned without duplicating the claim or belief update
**And** a genuinely repeated report at a later encounter may be recorded as a new event.

**Given** a scheduled meeting or claim delivery fails or is interrupted
**When** the branch continues
**Then** the original gift fact and existing observations remain intact
**And** Ivo receives no report until a later supported contact actually occurs.

**Given** the player is not present for the meeting
**When** Tessa's claim and Ivo's belief commit
**Then** the transcript and ordinary player views do not expose that private exchange
**And** the player may learn about it only through later perception, dialogue, behavior, or another supported report.

**Given** the branch is saved before or after contact
**When** it is loaded and advanced
**Then** the meeting event, participants, observations, claims, beliefs, provenance, and insertion order restore exactly
**And** loading cannot deliver the report twice or skip an already committed transmission.

### Story 2.8: Let Fallible Beliefs Shape Choices

As a player,
I want to see Ivo respond to a fallible report,
So that beliefs influence choices without rewriting history.

**Acceptance Criteria:**

**Given** a belief changes while physical circumstances remain the same
**When** the NPC replans
**Then** the belief may affect option evaluation without rewriting historical facts or compelling a fixed action
**And** the prior plan and reason history remain available for causal inspection.

**Given** the controlled rumor branch and Tessa's gift observation
**When** Tessa reports that the gift may have bought influence
**Then** the claim records that interpretation as Tessa's communicated meaning rather than historical fact
**And** the original gift event remains an unchanged witnessed transfer.

**Given** Ivo's recorded distrust and his relationship with Tessa
**When** he receives the influence claim
**Then** confidence is evaluated from his prior beliefs, source, relationship, disclosed provenance, and circumstances
**And** distrust may cause him to doubt the report or seek confirmation rather than automatically favoring or opposing the player.

**Given** Ivo now holds a received belief about the player
**When** he considers a later plan or social choice
**Then** that belief may change the ranking or eligibility of supported options
**And** the selected action still respects his resources, obligations, relationships, knowledge, risk, and time.

**Given** a belief influences a later choice
**When** the choice commits
**Then** diagnostics record the belief and other state that contributed to the decision
**And** no single belief acts as a universal command or predetermined response.

**Given** Ivo doubts or distorts a truthful report
**When** his belief is stored
**Then** the belief may differ from the historical fact without changing it
**And** truth, claim content, confidence, and belief status remain independently inspectable.

**Given** an NPC lies, conceals a motive, or communicates an incomplete account
**When** the communication is validated
**Then** it must be consistent with what the speaker knows and the supported encounter
**And** the listener receives only the communicated claim, not the speaker's hidden knowledge or intent.

### Story 2.9: Correct and Inspect a Belief-Driven Choice

As a player,
I want to observe how later evidence changes a belief-driven choice,
So that my knowledge and saved branch remain honest.

**Acceptance Criteria:**

**Given** Ivo later receives corroboration, contradiction, or correction through a supported observation or contact
**When** his belief updates
**Then** the new evidence and resulting confidence are appended to belief history
**And** prior beliefs and the actions taken under them remain causally preserved.

**Given** the player later observes Ivo's changed behavior or speaks with him
**When** Rowan presents the consequence
**Then** only perceptible behavior, dialogue, and legitimately learned information are shown
**And** the internal rumor chain or private motive is not exposed merely to explain the simulation.

**Given** the player asks Rowan why Ivo behaved differently without possessing the relevant evidence
**When** the known-information query resolves
**Then** Rowan states only what the character can support or that the reason is unknown
**And** development diagnostics remain the separate place for full causal inspection.

**Given** the same physical event occurs in branches with different transmitted claims or belief confidence
**When** later plans resolve
**Then** choices may differ because of recorded belief state without changing shared historical truth
**And** deterministic replay reproduces the same mechanical choice inputs and committed outcome for each captured branch.

**Given** the branch is saved and loaded after belief-driven replanning
**When** play resumes
**Then** the fact, observations, claims, belief history, confidence, selected plan, decision reasons, and observable consequences persist
**And** no universal crime, gift, or reputation score is inferred.


## Epic 3: Make Resources and Effects Authoritative

Players can spend and recover Health, Mana, and Stamina and can apply, inspect, stack, remove, expire, and persist bounded effects whose mechanics remain stable.

### Story 3.1: Upgrade a P0 Campaign to the P1 Ruleset

As a returning player,
I want my proven P0 campaign upgraded safely to include character resources,
So that I can continue playing without losing or fabricating prior world history.

**Acceptance Criteria:**

**Given** the P0 evidence gate has not passed, P1 lacks explicit authorization, or no P1 UX contract has been approved
**When** a P1 build or migration is requested
**Then** the upgrade is unavailable
**And** no P1 module, state, content, or interface is activated.

**Given** P1 is authorized
**When** the P1 release is composed
**Then** it registers only the P0 foundation plus the P1 character-resource and effect slices
**And** it introduces no P2–P9 modules, state, migrations, UI, or content.

**Given** a valid immediately preceding P0 save
**When** the P1 ruleset migration begins
**Then** it validates the source schema/content versions and records `rulesetStage: p1`, a P1 ruleset version, and enabled content-package versions
**And** skipping an intermediate stage or migrating an unsupported source is rejected before mutation.

**Given** an existing P0 character with current raw attributes
**When** migration initializes P1 resources
**Then** Base Maximum Health is `Body × Constitution`, Base Maximum Mana is `Body × Mind`, and Base Maximum Stamina is `Agility × Constitution`
**And** current Health, Mana, and Stamina each begin at their calculated maximum.

**Given** the four approved NPC fixtures
**When** their P1 maxima are calculated
**Then** Mara receives 80 Health, 130 Mana, and 96 Stamina; Oren 182, 130, and 112; Tessa 80, 112, and 130; and Ivo 156, 120, and 182
**And** the values derive from their saved attributes rather than duplicated mutable constants.

**Given** a P0 branch containing clock, inventory, ownership, relationships, knowledge, plans, progression, operations, and action history
**When** migration succeeds
**Then** every existing P0 causal record and branch identity remains unchanged
**And** only the new P1-owned ruleset metadata and resource state are initialized.

**Given** migration is retried for the same save
**When** the destination ruleset is already recorded
**Then** the existing migrated result is returned or recognized as complete
**And** resource pools and migration evidence are not created twice.

**Given** resource derivation, validation, or database writing fails
**When** the migration transaction rolls back
**Then** the original P0 save remains readable and unchanged
**And** no partially initialized pools or P1 ruleset marker are visible.

**Given** a P1 save is loaded by a release that supports only P0 or incompatible P1 versions
**When** compatibility validation runs
**Then** loading is rejected before branch mutation
**And** the application reports the unsupported ruleset safely rather than dropping P1 state.

**Given** a migrated P1 snapshot
**When** it is saved and restored
**Then** ruleset stage/version, content packages, raw attributes, Base Maxima, current pools, and migration provenance persist
**And** Base Maxima are verified against the restored attributes.

**Given** the migration implementation is verified
**When** quality tests run against real isolated SQLite databases
**Then** success, retry, rollback, incompatible source, skipped-stage, save/load, and all standard-array derivations are covered
**And** the external LLM is not involved in migration.

### Story 3.2: Spend, Recover, and Recalculate Character Resources

As a player,
I want Health, Mana, and Stamina to change through consistent rules,
So that costs, recovery, growth, incapacity, and death remain understandable and persistent.

**Acceptance Criteria:**

**Given** a character's raw attributes and active effects
**When** resource state is projected
**Then** current value, Base Maximum, and Effective Maximum are distinct for Health, Mana, and Stamina
**And** each current value is bounded from 0 through its Effective Maximum.

**Given** Body, Agility, Constitution, or Mind permanently increases
**When** affected Base Maxima are recalculated
**Then** each positive maximum difference is added to the corresponding current pool
**And** existing damage or expenditure remains the same absolute deficit.

**Given** a relevant raw attribute permanently decreases
**When** Base and Effective Maxima are recalculated
**Then** current values are clamped to their new Effective Maxima
**And** clamping is not recorded as damage, expenditure, or a damage-triggering event.

**Given** a temporary check modifier is applied
**When** resources are recalculated
**Then** Base Maxima remain unchanged
**And** only an effect that explicitly targets a maximum can change the Effective Maximum.

**Given** an action has a Routine, Exerting, Strenuous, or Extreme Stamina classification
**When** it begins
**Then** the full approved cost of 0, 5, 10, or 20 Stamina is validated and reserved before execution
**And** rejection commits no partial Stamina or fictional time.

**Given** a Mana- or Stamina-costing action exceeds the character's current pool
**When** validation runs
**Then** the action is rejected before commitment
**And** no effect, resource cost, random roll, or elapsed time occurs.

**Given** a valid ten-minute uninterrupted non-strenuous rest
**When** it completes
**Then** Stamina restores by 25% of Effective Maximum, rounded up and capped at that maximum
**And** an interruption before completion grants no completed-rest restoration.

**Given** a qualifying adequate-sleep recovery event is supplied by a controlled P1 fixture or a later proven sleep system
**When** eight hours complete
**Then** all Mana and 25% of Effective Maximum Health, rounded up, are restored
**And** P1 does not introduce hunger, sleep-pressure clocks, beds, protection, `Exhausted`, or `Exposed`.

**Given** ordinary time passes or a character eats without an explicit restoration effect
**When** resource recovery is evaluated
**Then** Health, Mana, and Stamina do not recover merely from that passage or meal
**And** future consumables may restore only what their accepted definitions declare.

**Given** a character reaches 0 Stamina
**When** they attempt movement or a Stamina-costing action
**Then** the action is rejected even if ordinary walking would normally cost zero
**And** the character may still talk, inspect, eat, use a suitable item, or attempt supported rest.

**Given** damage is committed
**When** current Health decreases
**Then** the loss is recorded separately from any declared Minor or Severe Wound
**And** wounds apply only through their own accepted effect definitions.

**Given** current Health reaches 0 after the authoritative same-second resolution phase
**When** terminal states are applied
**Then** the character dies immediately
**And** no Downed or stabilization interval is introduced.

**Given** a player character dies
**When** the outcome is presented
**Then** recovery from a manual save remains available and no forced permanent-death deletion occurs
**And** revival is possible only through an explicitly supported effect within its declared window.

**Given** an NPC dies
**When** the transaction commits
**Then** the death persists in the branch
**And** it can be reversed only by a supported effect rather than narration or reload-free fiat.

**Given** the player inspects known resource state
**When** the P1 character projection renders under the approved P1 UX contract
**Then** current and Effective Maximum values, paid costs, recovery, clamping, restrictions, and terminal results are understandable without client-side calculation
**And** the browser treats the server projection as authoritative.

### Story 3.3: Create Stable Source-Bounded Effects

As a player,
I want conditions and item treatments constrained by their actual source,
So that improvised effects can be creative without becoming arbitrary or changing later.

**Acceptance Criteria:**

**Given** an authored or proposed mechanical effect
**When** its definition is validated
**Then** it declares a stable ID, schema version, source event/entity, source category, polarity, tier, eligible target, mechanical shape, magnitude, duration/use limit or terminating condition, duplicate policy, removal contract, and knowledge visibility
**And** incomplete definitions cannot commit.

**Given** an effect is applied to a target
**When** its instance is created
**Then** it records a stable instance ID, exact definition/version, source, target, creation sequence, start/expiry data, remaining uses or ticks, stack linkage, and visibility state
**And** mechanical resolution never reparses player-facing prose.

**Given** a fictional source is evaluated before an uncertain check
**When** its effect budget is established
**Then** the maximum tier, eligible targets, and maximum duration, uses, or terminating condition are fixed before rolling
**And** difficulty determines success rather than effect magnitude.

**Given** a source provides no explicit maximum duration, use limit, or terminating condition
**When** a generated effect is proposed
**Then** the proposal is rejected rather than made indefinite
**And** the LLM may propose only a shorter duration within a supplied limit.

**Given** a Subtle source
**When** magnitude is validated
**Then** flat magnitude is limited to ±1, proportional magnitude to ±10%, and total periodic damage to 10
**And** values above those limits are rejected or reduced before commitment.

**Given** a Standard source
**When** magnitude is validated
**Then** flat magnitude is limited to ±4, proportional magnitude to ±25%, and total periodic damage to 30
**And** values above those limits are rejected or reduced before commitment.

**Given** a Major source
**When** magnitude is validated
**Then** flat magnitude is limited to ±20, proportional magnitude to ±50%, and total periodic damage to 100
**And** only rare materials/artifacts, major achievements/sacrifices, or extreme hazards can establish that tier.

**Given** an effect targets Health, Mana, Stamina, an Effective Maximum, a check, Defense, movement, damage, healing, or an action/spell cost
**When** the target and shape are eligible for the source
**Then** the proposal may be accepted within budget
**And** unsupported targets or shapes are rejected before state changes.

**Given** the LLM proposes a generated effect
**When** strict validation runs
**Then** the proposal contains one primary mechanical shape and stays within the pre-established source budget
**And** the engine, not the LLM, decides whether to accept, reduce, or reject it.

**Given** an explicitly authored effect contains multiple components
**When** content validation runs
**Then** every component is separately balanced and versioned
**And** the exception does not allow generated effects to bypass the one-primary-shape rule.

**Given** an uncertain effect-creating action rolls a natural 20 or natural 1
**When** its outcome resolves
**Then** natural 20 succeeds only at the admitted source budget and natural 1 creates no effect
**And** neither the die nor repeated mundane actions can manufacture a higher tier.

**Given** a complete effect definition is accepted
**When** its player-facing name or description is generated or later displayed
**Then** presentation may express the causal source while mechanics remain immutable under the accepted version
**And** intentional mechanical revision requires a new explicit version or migration.

**Given** the tier/shape calibration matrix proposes every exact boundary and one-unit or one-percentage-point excess
**When** validation runs
**Then** every exact-limit proposal validates and every over-limit proposal is rejected or reduced before commitment
**And** all decisions are available as diagnostic evidence.

### Story 3.4: Stack, Replace, Refresh, and Remove Effects

As a player,
I want active effects to combine and end through explicit rules,
So that their consequences remain predictable even when several effects interact.

**Acceptance Criteria:**

**Given** differently named valid effects target the same character or item
**When** they are applied
**Then** their instances coexist and contribute independently
**And** similarity of outcome does not make one silently replace another.

**Given** an effect definition uses `stack`
**When** the same definition is applied again
**Then** a new independent instance is created with its own source, sequence, duration, ticks, and removal linkage
**And** removing or expiring one instance leaves the others active.

**Given** an effect definition uses `refresh`
**When** it is reapplied to the same eligible target
**Then** the existing magnitude is retained while its duration or uses reset to the accepted definition
**And** no additional magnitude stack is created.

**Given** an effect definition uses `replace`
**When** another eligible application is committed
**Then** the stronger accepted magnitude remains active with deterministic tie handling
**And** a weaker application cannot shorten or downgrade the retained effect.

**Given** ordinary percentage and flat modifiers target the same value
**When** the effective value is calculated
**Then** it uses `round(Base × (1 + sum of percentage modifiers)) + sum of flat modifiers`
**And** percentages add rather than compound while flats apply after the single rounding step.

**Given** simultaneous +25% and −25% effects
**When** the modifier reducer runs
**Then** their numeric percentage contribution cancels to zero
**And** both instances remain present, inspectable, removable, and independently expiring.

**Given** effects reduce Health, Mana, Stamina, damage, or healing
**When** the final value is calculated
**Then** the result cannot fall below zero
**And** action or spell costs cannot fall below one unless an authored effect explicitly permits zero.

**Given** effects change an Effective Maximum below the current value
**When** recalculation runs
**Then** the current pool clamps to the new maximum
**And** the clamp does not fire damage, spending, or wound triggers.

**Given** an effect records a physiological, wound, poison, disease, magical, environmental, social, or item-treatment category
**When** removal is attempted
**Then** only its declared cause, a compatible category, or an exact-effect remedy can remove it
**And** a narratively convenient but incompatible remedy is rejected without mutation.

**Given** one wound has one linked `Bleeding` instance
**When** compatible wound treatment completes
**Then** that one linked instance is removed
**And** other independently stacked wounds and Bleeding instances remain active.

**Given** `Sharpened` is applied with a whetstone
**When** ten minutes and 5 Stamina commit
**Then** the weapon gains +1 damage for its next ten successful hits under `refresh` behavior
**And** misses do not consume a successful-hit charge.

**Given** Sharpened is reapplied before its charges are exhausted
**When** the maintenance action completes
**Then** its magnitude remains +1 and successful-hit charges reset to ten
**And** time and Stamina are paid exactly once.

**Given** separate Bleeding wounds are created
**When** their effects apply
**Then** each instance is scheduled to deal 2 Health every six seconds for five ticks
**And** their periodic-damage total remains within the accepted Standard budget.

**Given** diagnostic-only `Star-metal Edge` is applied from its rare artifact-grade oil
**When** the accepted Major treatment commits
**Then** the weapon gains +20 damage on the next successful hit within ten minutes under `replace` behavior
**And** a weaker duplicate cannot displace it.

**Given** an application, refresh, replacement, charge consumption, or removal action is retried
**When** idempotency is checked
**Then** the original result is returned
**And** instances, costs, uses, time, and linked removals are not duplicated.

### Story 3.5: Resolve Effect Ticks and Same-Second Outcomes

As a player,
I want simultaneous actions and effects resolved in one stable order,
So that timing edge cases have reproducible outcomes.

**Acceptance Criteria:**

**Given** scheduled effect work
**When** it is persisted
**Then** every event has a stable ID, due game second, event phase/priority, and insertion sequence
**And** equal-time events do not depend on database row order or narration order.

**Given** multiple changes share one game second
**When** the domain reducer resolves them
**Then** it applies completed actions and continuous intervals first, scheduled effect ticks second, expirations and environmental transitions third, and Base/Effective recalculation, current-pool clamping, and terminal states last
**And** later stages can add need-threshold events to the established second phase without changing the ordering contract.

**Given** several completed actions or intervals share a timestamp
**When** phase one runs
**Then** they resolve in recorded commitment order
**And** only completed phases apply their completion effects.

**Given** multiple effect ticks share a timestamp
**When** phase two runs
**Then** they resolve in stable effect-creation order
**And** each tick records the exact definition/version and instance that caused it.

**Given** an effect's final scheduled tick and ordinary duration expiry share a timestamp
**When** phase two and phase three run
**Then** the final tick resolves before expiry
**And** expiry cannot erase an already due final tick.

**Given** a compatible treatment completes at the exact second of a linked Bleeding tick
**When** the reducer runs
**Then** the completed treatment removes that linked instance during phase one
**And** the removed instance does not deal its same-second phase-two tick.

**Given** Health reaches or passes zero during one or more same-second ticks
**When** phase four applies bounds and terminal state
**Then** all earlier ordered changes for that second are accounted for before death is determined
**And** narration cannot insert recovery or reorder the ticks afterward.

**Given** an Effective Maximum falls below the current pool because an effect begins, ends, or is replaced
**When** phase four recalculates and clamps
**Then** the final current value reflects all same-second modifier changes
**And** the clamp is recorded separately from damage or expenditure.

**Given** equal and opposite modifiers expire at different times
**When** each expiry phase is reached
**Then** only the expiring instance is removed and the effective value is recalculated
**And** the other effect remains active even if their prior net modifier was zero.

**Given** a timed action is interrupted before its completion boundary
**When** the accumulated resolution commits
**Then** due scheduled events and legitimately completed phases persist
**And** the unfinished action's completion effect does not occur.

**Given** an action advances across many scheduled events
**When** the per-action event budget is exhausted or a same-time loop is detected
**Then** the operation stops safely with a typed recoverable failure or interruption
**And** no unbounded event cascade or partially ambiguous commit is allowed.

**Given** an identical snapshot, event queue, insertion counter, action phases, and recorded random inputs
**When** time advances again in replay
**Then** effect ticks, expiry, resource values, clamping, and death reproduce in the same order
**And** fresh narration cannot change the mechanical result.

**Given** later narration describes an equal-time outcome
**When** it receives the committed event evidence
**Then** it reflects the authoritative ordering and terminal state
**And** it cannot claim an expired effect acted late or a treatment acted after the tick when the inverse committed.

### Story 3.6: Inspect, Persist, and Verify the P1 Effect System

As a player,
I want resource and effect state to remain understandable and stable across sessions,
So that I can trust what is affecting each character and why.

**Acceptance Criteria:**

**Given** the player inspects a character under the approved P1 UX contract
**When** the resource/effect view opens
**Then** it shows current and Effective Maximum Health, Mana, and Stamina plus every known effect's name, stacks, mechanics, source, category, remaining uses or known duration, and removal condition
**And** values are projected by the server rather than recalculated in the browser.

**Given** an effect exists but its mechanics are not known to the viewing character
**When** the player projection is built
**Then** it exposes only legitimately observed symptoms and known source information
**And** hidden definition fields, exact timers, private causes, and removal knowledge remain concealed.

**Given** an exact effect duration is unknown
**When** the effect is inspected
**Then** no exact remaining time is displayed
**And** later abilities may reveal it only through their explicit mechanics.

**Given** effect or resource state changes
**When** the accessible P1 interface updates
**Then** stacks, costs, recovery, clamping, expiry, removal, restrictions, and death are announced and labeled without relying on color or stealing focus
**And** keyboard, pointer, screen-reader, zoom, reflow, contrast, and reduced-motion requirements remain satisfied.

**Given** a P1 branch is saved
**When** the snapshot is written
**Then** it includes ruleset metadata, current pools, verified Base Maxima, effect definitions and exact versions, effect instances, sources, visibility, stacks, remaining uses, scheduled ticks, expiry data, insertion counters, and removal linkage
**And** the existing P0 causal state remains present.

**Given** the P1 snapshot is loaded
**When** restoration and compatibility validation complete
**Then** every pool, effect, tick, use, modifier, and known/unknown projection matches the saved branch
**And** loading does not reapply an effect, repeat a tick, consume a use, reroll a proposal, or regenerate its mechanics.

**Given** all standard-array assignments and later permanent attribute growth
**When** the resource formula suite runs
**Then** Base Maxima, positive-difference current increases, absolute deficits, reductions, Effective Maximum changes, and clamps match the approved rules
**And** clamping never fires damage triggers.

**Given** the P1 calibration matrix
**When** every supported target/shape is proposed at each tier's exact limit and one unit or percentage point above it
**Then** exact-limit definitions validate and over-limit definitions are rejected or reduced before commitment
**And** source eligibility, termination, identity, and accepted version are recorded.

**Given** Stack, Refresh, Replace, differently named effects, opposed percentages, flat modifiers, and authored multiplicative-exception reducer fixtures
**When** interaction tests run
**Then** every policy and arithmetic result matches the approved contract
**And** the reducer can later host `Starved` and `Exhausted` without activating P3 conditions in P1.

**Given** Sharpened, separate Bleeding wounds, opposed modifiers, and Star-metal Edge fixtures
**When** application, use, refresh, replacement, ticking, treatment, expiry, and save/load are exercised
**Then** magnitudes, costs, charges, ticks, removals, ordering, and persistence match their definitions
**And** duplicate or retried requests do not repeat any change.

**Given** Stamina spending and recovery fixtures
**When** full-cost, insufficient-cost, zero-Stamina, completed-rest, interrupted-rest, and qualifying sleep-recovery cases run
**Then** payment, rejection, restrictions, rounding, caps, time, and recovery match the resource rules
**And** no P3 need clock, bed, hunger, or shelter state is created.

**Given** the P1 controlled evidence run
**When** it exercises its fixtures, one failure/recovery path, save/load, and one unplanned but supported effect approach
**Then** all resource conservation, effect bounds, ordering, knowledge, and persistence checks produce inspectable evidence
**And** actual player feedback records what changed, what felt unfair, and what should happen next.

**Given** an unexplained contradiction, ordering divergence, resource-conservation error, hidden-state leak, unstable definition, or save failure occurs
**When** the P1 gate is evaluated
**Then** the affected case fails and must be corrected and repeated
**And** P2 remains unauthorized until the P1 evidence gate passes with zero unexplained failures.

**Given** all P1 evidence passes
**When** the epic is closed
**Then** P1 is recorded as eligible for a separate P2 authorization decision
**And** P2 access, ownership, theft, beds, and shelter mechanics remain absent until explicitly authorized.

## Epic 4: Make Places Physically Accessible

Players can reach and use local resources through permission, keys, locks, force, and other physical methods while ownership, evidence, observation, and belief remain causally separate.

### Story 4.1: Upgrade the World to Authored Physical Places

As a returning player,
I want homes, entrances, and local resources added without rewriting my campaign,
So that physical access becomes meaningful while prior consequences remain intact.

**Acceptance Criteria:**

**Given** the P1 evidence gate has not passed, P2 lacks explicit authorization, or no P2 UX contract has been approved
**When** a P2 build or migration is requested
**Then** the upgrade is unavailable
**And** no P2 place, entrance, permission, key, property, evidence, or interface state is activated.

**Given** P2 is authorized
**When** the P2 release is composed
**Then** it registers the P0–P1 slices plus P2 `places` and required inventory identity behavior
**And** it introduces no P3–P9 modules, need clocks, food systems, autonomous livelihoods, guards, courts, or universal crime reputation.

**Given** a valid immediately preceding P1 save
**When** the P2 ruleset migration runs
**Then** it validates the source ruleset and records the P2 stage/version and compatible content-package versions
**And** it initializes only P2-owned place, entrance, access, permission, key, capacity, property, and evidence fixture state.

**Given** Ivo's Home is loaded from authored content
**When** its physical state is inspected
**Then** it has a stable authored location ID, local resources and facilities, one entrance/door, a difficulty-12 lock, and one capacity-two bed
**And** geography and connections are stable rather than procedurally generated.

**Given** the Ivo's Home fixture is initialized
**When** actors and access credentials are inspected
**Then** Ivo and permitted guest Mara have compatible keys and explicit access context
**And** possession of a key, ownership, permission, relationship, and physical reachability remain separate facts.

**Given** the door is initialized
**When** its state is queried
**Then** open, closed, locked, and broken are represented as explicit valid states with constrained transitions
**And** a broken-open door cannot simultaneously behave as intact and locked.

**Given** resources or facilities exist at Ivo's Home
**When** world state is projected
**Then** each records its actual location, current possessor where applicable, capacity or availability, and stable content identity
**And** ownership alone does not permit remote use or teleport the resource.

**Given** the P2 theft fixtures are initialized
**When** their item models are inspected
**Then** one fungible food serving and one distinctive marked object use their appropriate identity models
**And** no physiological need, food-preparation, or spoilage behavior is introduced before P3.

**Given** a P1 branch already contains characters, pools, effects, knowledge, plans, inventory, clock, and history
**When** migration succeeds
**Then** all prior causal state, revisions, identifiers, and scheduled events remain unchanged
**And** only the authored P2 fixture state and ruleset metadata are added.

**Given** migration is retried
**When** the save already records the P2 destination version
**Then** the existing migrated result is recovered or recognized as complete
**And** places, doors, keys, permissions, beds, resources, and fixture items are not duplicated.

**Given** content validation or migration fails
**When** the transaction rolls back
**Then** the original P1 save remains readable and unchanged
**And** no partial P2 ruleset marker or physical state becomes visible.

**Given** a migrated P2 branch is saved and loaded
**When** compatibility checks complete
**Then** its ruleset metadata, locations, entrance states, permissions, keys, capacities, resource placement, possession, ownership claims, and item identity restore together
**And** Base P0–P1 state remains intact.

**Given** migration quality tests run against real isolated SQLite databases
**When** success, retry, rollback, incompatible source, skipped stage, content failure, and save/load cases execute
**Then** every outcome matches the typed migration contract
**And** no LLM call is required to establish authored physical truth.

### Story 4.2: Enter Through Permission, Keys, and Door State

As a player,
I want lawful physical access to depend on where I am and what access I actually have,
So that doors, keys, permission, and shared facilities matter consistently.

**Acceptance Criteria:**

**Given** an actor attempts to reach a place or resource
**When** access is evaluated
**Then** the decision uses actor location, target location, route, entrance state, permission, relationship, compatible key, required tools, capacity, proposed method, and payable costs
**And** ownership is neither remote access nor an automatic prohibition on physical use.

**Given** an actor is not at the relevant entrance and has no supported route to it
**When** they attempt to use a local resource
**Then** access is rejected without moving or using the resource
**And** the explanation identifies physical unreachability without suggesting a strategy.

**Given** Ivo or permitted guest Mara is at Ivo's intact locked door with a matching key
**When** they unlock and open it
**Then** five fictional seconds advance and the door becomes open without a roll
**And** key compatibility, permission, elapsed time, and door transitions commit atomically.

**Given** an actor holds a nonmatching key
**When** they attempt to unlock the door
**Then** the attempt is rejected without changing the door
**And** possession of an arbitrary key does not satisfy compatibility.

**Given** the intact door is unlocked and closed
**When** an actor physically opens it
**Then** the door becomes open through a supported state transition
**And** no lockpick, force check, or ownership inference is required.

**Given** the door is open
**When** an actor closes and locks it with a compatible key
**Then** the door becomes closed and locked through the declared action durations
**And** no character outside perceptual range learns that state automatically.

**Given** the door is broken and open
**When** an actor attempts to lock it as though intact
**Then** the transition is rejected
**And** repair remains outside P2 unless explicitly supported later.

**Given** an actor has ownership or permission but is physically elsewhere
**When** they attempt to use the bed or local resource remotely
**Then** the attempt is rejected for lack of physical access
**And** the ownership or permission record remains unchanged.

**Given** an actor lacks ownership but reaches a usable resource through a supported entrance
**When** they attempt physical use
**Then** access rules may permit the physical action
**And** unauthorized use can still create trespass, theft, observation, evidence, and relationship consequences.

**Given** Ivo's capacity-two bed is physically reachable
**When** one or two permitted occupants use it
**Then** capacity reservations allow both occupants
**And** a third simultaneous occupant is rejected without displacing a committed occupant.

**Given** a character uses the bed during P2
**When** the action completes
**Then** physical occupancy and elapsed action state may be recorded
**And** no adequate-sleep, hunger, `Exhausted`, `Exposed`, or recovery qualification is introduced before P3.

**Given** a door, key, permission, resource, or capacity fact is projected to the player
**When** the P2 interface renders it
**Then** only states legitimately known through perception or communication are shown
**And** hidden lock state, private permission, ownership claims, or occupants are not inferred from authoritative data.

**Given** an access command is retried, reconnected, or submitted against a stale revision
**When** the commit boundary is checked
**Then** duplicate requests return the original result and stale requests conflict without mutation
**And** door state, time, key state, occupancy, and access history cannot commit twice.

### Story 4.3: Pick Locks or Force Entry at a Real Cost

As a player,
I want unauthorized entry attempts to consume real tools, effort, and time,
So that bypassing access controls produces persistent risk and evidence.

**Acceptance Criteria:**

**Given** an actor is physically at Ivo's intact locked door with a lockpick
**When** they propose lockpicking
**Then** the action declares 60 seconds, consumption rules for the pick, and an `Agility + Sleight of Hand` check at difficulty 12 before rolling
**And** the attempt uses the ordinary natural-roll and success-only XP rules.

**Given** the lockpicking check succeeds
**When** the completed attempt commits
**Then** the lock becomes unlocked through one atomic action record
**And** opening the door occurs only if included in the accepted action and its required time is paid.

**Given** the lockpicking check fails
**When** the completed attempt commits
**Then** 60 seconds advance and the used pick is consumed
**And** the door remains locked.

**Given** a failed lockpicking attempt and another available pick
**When** the actor tries again
**Then** the retry is a new declared check and may proceed
**And** it must independently pay its tool, time, and uncertainty costs.

**Given** no lockpick is available or the door is already broken/open
**When** lockpicking is attempted
**Then** the action is rejected before rolling or advancing time
**And** the system does not invent a tool or meaningful lock state.

**Given** an actor is physically at the intact door with at least 10 Stamina
**When** they attempt forced entry
**Then** the action declares 30 seconds, 10 Stamina, unavoidable loud noise, and a `Body + Athletics` check at difficulty 14 before rolling
**And** full cost is reserved before resolution.

**Given** forced entry succeeds
**When** the attempt commits
**Then** the door becomes broken and open
**And** the elapsed time, Stamina cost, noise event, property damage, and successful check/XP commit exactly once.

**Given** forced entry fails
**When** the attempt commits
**Then** the door remains in its prior intact state while 30 seconds, 10 Stamina, and the loud noise event still commit
**And** failed-check XP remains zero.

**Given** an actor has fewer than 10 Stamina
**When** forced entry is proposed
**Then** it is rejected before a roll, noise, damage, time, or partial Stamina cost
**And** the player receives the factual insufficiency reason without a suggested alternative.

**Given** another fully funded forced-entry attempt follows a failure
**When** it is submitted
**Then** it is allowed as a new request with a new recorded roll
**And** previous failure does not waive time, Stamina, noise, or other costs.

**Given** lockpicking or forced entry is interrupted before its resolution boundary
**When** interruption handling commits completed phases
**Then** the action follows its declared reservation/consumption policy without inventing success or failure
**And** any elapsed time and perceivable noise that actually occurred remain causal evidence.

**Given** a loud attempt occurs within an NPC's perceptual range
**When** the action commits
**Then** the historical noise event may produce a witness-specific observation containing only perceptible details
**And** characters outside perceptual range gain no automatic knowledge.

**Given** an NPC later encounters damage, tampering, or an unexpectedly unlocked door
**When** they inspect it
**Then** a new observation and possible belief may be created from that evidence
**And** the actor's identity remains unknown unless supported by observation, claim, or inference.

**Given** an access attempt is retried with the same logical request ID or restored after save/load
**When** it resolves
**Then** the prior result is recovered without repeating tool consumption, time, Stamina, noise, damage, roll, or XP
**And** the current door state remains authoritative.

### Story 4.4: Distinguish Possession, Ownership, and Item Identity

As a player,
I want items to retain the right kind of identity and ownership history,
So that transfers, use, loss, and restitution have consistent physical meaning.

**Acceptance Criteria:**

**Given** any portable item or quantity
**When** authoritative state is inspected
**Then** physical location or current possessor is distinct from the legitimate ownership claim
**And** changing possession does not silently rewrite ownership.

**Given** a distinctive marked object
**When** it is instantiated
**Then** it has a stable item ID, current possessor, legitimate claimant, provenance, and observable identifying marks
**And** those properties survive transfer without being regenerated from prose.

**Given** a fungible food serving or other fungible good
**When** it is instantiated
**Then** state records its item type, quantity, location or possessor, and causal transfer events
**And** it does not claim a permanently recognizable individual identity after mixing.

**Given** fungible quantities are split, transferred, or merged with equivalent goods
**When** the transaction commits
**Then** total quantity is conserved across source and destination
**And** causal transfer history remains available without pretending the mixed units can be individually identified.

**Given** a fungible stolen serving has been mixed with equivalent servings
**When** someone later inspects the combined stock
**Then** authoritative state cannot identify which physical serving was stolen
**And** equivalent restitution remains possible through quantity transfer.

**Given** a distinctive marked object changes possessors without the owner's consent
**When** the transfer commits
**Then** the new possessor and location change while the legitimate ownership claim and provenance remain
**And** the item's marks can later support recognition if actually perceived.

**Given** an ordinary consensual transfer
**When** both parties, item, physical reachability, consent, time, and transferability validate
**Then** possession and any explicitly transferred ownership claim commit atomically
**And** a retry cannot duplicate the item or quantity.

**Given** an actor physically reaches a usable resource they do not own
**When** they use or consume it
**Then** the physical result may commit if all non-ownership requirements are met
**And** unauthorized use does not erase theft, trespass, observation, relationship, or restitution consequences.

**Given** an actor owns an item located elsewhere
**When** they attempt to use or transfer it remotely
**Then** the request is rejected for physical unreachability
**And** the item remains at its actual location with its current possessor.

**Given** authored scenery is examinable but not defined as portable
**When** the player attempts to take it
**Then** the action is rejected without creating an inventory item
**And** the system does not convert descriptive nouns into resources automatically.

**Given** a distinctive or fungible item is shown in Inventory or a place view
**When** the player projection is built
**Then** it exposes only known possession, location, quantity, marks, provenance, or ownership information
**And** authoritative ownership or hidden transfer history does not leak merely because the backend stores it.

**Given** item state is saved and loaded
**When** restoration completes
**Then** stable IDs, batches or quantities, possessor, location, ownership claim, provenance, marks, and transfer history restore exactly
**And** loading cannot duplicate, merge, identify, or erase goods beyond the saved state.

### Story 4.5: Create Theft Evidence Without Omniscience

As a player,
I want theft and trespass to produce only the evidence people can actually perceive,
So that discovery and suspicion remain causal and can sometimes be wrong.

**Acceptance Criteria:**

**Given** an actor physically reaches the fungible serving or distinctive marked object without consent
**When** they take it
**Then** possession and location change while the legitimate ownership claim remains unchanged
**And** the theft action, time, access path, and transfer commit atomically.

**Given** no character perceives the removal
**When** the theft commits
**Then** no owner or other NPC observation, belief, or thief identity is created
**And** authoritative property state remains separate from character knowledge.

**Given** a character directly witnesses the taking
**When** the theft commits
**Then** that witness receives an observation limited to perceptible actor, object or quantity, place, time, access, and behavior
**And** non-witnesses gain no knowledge until supported contact occurs.

**Given** the owner later inspects the expected storage location
**When** an item or quantity is absent
**Then** the inspection creates an absence observation
**And** comparison with remembered state may create a belief that property is missing without identifying the thief automatically.

**Given** a witness sees a newly possessed distinctive marked object
**When** its recognizable marks and prior knowledge support comparison
**Then** the observation may contribute to a belief about provenance or theft
**And** ownership truth is not copied directly into the belief.

**Given** a stolen fungible serving has been mixed with equivalent goods
**When** an NPC inspects the mixed stock or another character's inventory
**Then** the specific stolen unit cannot be recognized from identity alone
**And** suspicion requires other observations, testimony, opportunity, motive, or inconsistent statements.

**Given** witnessed access, forced-entry damage, lock tampering, noise, opportunity, motive, possession of a marked object, or inconsistent statements exist
**When** an NPC evaluates evidence
**Then** one or more supported suspicions may be recorded with provenance and confidence
**And** the evidence may support an incorrect accusation without changing historical truth.

**Given** evidence is incomplete or conflicting
**When** an NPC considers accusation or relationship consequences
**Then** personality, relationships, existing beliefs, confidence, and alternatives affect the decision
**And** no universal crime score or mandatory accusation is applied.

**Given** an accusation is made
**When** another character hears it
**Then** the accusation becomes a claim with its own speaker, listener, encounter, content, and provenance
**And** it does not become proof merely because it was spoken.

**Given** a later observation or report contradicts the suspicion
**When** belief updates occur
**Then** confidence may decrease, change, or remain contested according to supported evidence
**And** the earlier belief and actions taken under it remain in causal history.

**Given** an unauthorized actor eats the serving or uses the bed while physically able
**When** the action completes
**Then** the physical use is not undone merely because it was unauthorized
**And** P2 records access, possession/use, evidence, and relationship consequences without adding P3 physiological benefit.

**Given** the player lacks legitimate knowledge of a private theft, suspicion, or accusation
**When** transcript, Journal, Inventory, or place views are projected
**Then** the hidden event and beliefs remain concealed
**And** the player may learn them only through later perception or communication.

**Given** theft, inspection, suspicion, or accusation requests are retried
**When** idempotency is checked
**Then** the existing result is recovered
**And** possession, quantities, observations, beliefs, time, damage, and relationship changes are not duplicated.

**Given** P2 scope is audited
**When** theft consequences are reviewed
**Then** they use only access, evidence, belief, relationship, possession, ownership, and resource rules
**And** guards, arrest, courts, and universal crime reputation remain outside P0–P9.

### Story 4.6: Inspect, Persist, and Verify Physical Access

As a player,
I want access, property, and evidence to remain understandable and persistent,
So that entering, using, damaging, or taking something has reliable consequences.

**Acceptance Criteria:**

**Given** the player inspects a known place under the approved P2 UX contract
**When** the access/property view renders
**Then** it may show legitimately known entrance state, route, permissions, compatible keys, capacity, reachable facilities, item location or possession, and observed evidence
**And** it does not reveal hidden ownership claims, occupants, permissions, access attempts, or NPC beliefs.

**Given** access, item, or evidence state changes
**When** the P2 interface updates
**Then** state, cost, result, damage, noise, observation, and known consequences are labeled and announced without relying on color or stealing focus
**And** keyboard, pointer, screen-reader, zoom, reflow, contrast, target-size, and reduced-motion requirements remain satisfied.

**Given** a P2 branch is saved
**When** the snapshot is written
**Then** it includes ruleset metadata, places, resource locations, door/lock state, keys, permissions, relationships relevant to access, bed capacity/occupancy, tools, possession, ownership claims, distinctive provenance/marks, fungible quantities/transfers, damage, noise, event history, observations, claims, beliefs, suspicion, and scheduled work
**And** all P0–P1 causal state remains present.

**Given** the snapshot is loaded
**When** compatibility and integrity validation complete
**Then** every entrance, credential, permission, capacity, item, claim, observation, belief, and access consequence matches the saved branch
**And** loading does not repeat an attempt, consume another tool, charge time/Stamina, create evidence, or deliver knowledge twice.

**Given** the Ivo's Home lawful-access matrix
**When** owner, permitted guest, matching key, nonmatching key, unlocked door, locked door, broken door, remote owner, and over-capacity cases run
**Then** every access decision, transition, duration, and capacity result matches the approved rules
**And** ownership never acts as remote access or automatic physical prohibition.

**Given** the lockpicking matrix
**When** success, failed pick consumption, missing tool, retry with another pick, stale revision, duplicate request, and interruption cases run
**Then** door state, tool quantity, time, roll, XP, observations, and recovery remain correct
**And** each genuine retry pays its own requirements.

**Given** the forced-entry matrix
**When** success, failure, insufficient Stamina, paid retry, witnessed noise, unwitnessed noise, damage discovery, and interruption cases run
**Then** Stamina, time, rolls, door state, noise, damage, observations, and beliefs reconcile
**And** no actor identity becomes known without evidence.

**Given** the property matrix
**When** consensual transfer, remote-use rejection, unauthorized use, distinctive theft, fungible theft, splitting, mixing, restitution, and scenery-taking cases run
**Then** quantities, identity, possession, ownership, provenance, location, and transfer events remain conserved and correctly distinct
**And** mixed fungible goods never become magically traceable.

**Given** witnessed and unwitnessed theft variants
**When** immediate observation, later absence discovery, marked-object recognition, conflicting evidence, and mistaken suspicion are exercised
**Then** property truth persists while knowledge arises only through observation, claim, or supported inference
**And** accusations remain fallible beliefs rather than authoritative truth.

**Given** the P2 controlled evidence run
**When** it exercises lawful entry, bed capacity, every door state, keys, lockpicking, force, local-resource use, both item identities, one failure/recovery path, save/load, and one unplanned supported access approach
**Then** all costs, access, conservation, evidence, knowledge, and persistence results are recorded
**And** player feedback records what changed, what felt unfair, and what should happen next.

**Given** an unexplained access contradiction, conservation error, property omniscience, evidence leak, duplicate cost, nonreproducible result, or save failure occurs
**When** the P2 gate is evaluated
**Then** the affected case fails and must be corrected and repeated
**And** P3 remains unauthorized until the P2 evidence gate passes with zero unexplained failures.

**Given** all P2 evidence passes
**When** the epic is closed
**Then** P2 is recorded as eligible for a separate P3 authorization decision
**And** hunger, sleep pressure, food preparation, spoilage, `Starved`, `Exhausted`, and `Exposed` remain absent until P3 is explicitly authorized.

## Epic 5: Live With Hunger and Fatigue

Players can eat, prepare food, sleep, accept deprivation, recover, and experience causal `Starved`, `Exhausted`, `Exposed`, spoilage, and food-poisoning outcomes.

### Story 5.1: Upgrade Characters With Need Clocks and Food Fixtures

As a returning player,
I want hunger, fatigue, food, and shelter state added without inventing past deprivation,
So that survival begins from a clear and trustworthy campaign baseline.

**Acceptance Criteria:**

**Given** the P2 evidence gate has not passed, P3 lacks explicit authorization, or no P3 UX contract has been approved
**When** a P3 build or migration is requested
**Then** the upgrade is unavailable
**And** no need clock, survival condition, food recipe, batch, protection, or P3 interface state is activated.

**Given** P3 is authorized
**When** the P3 release is composed
**Then** it registers the P0–P2 slices plus P3 `needs` and `crafting/food` behavior
**And** it introduces no P4 autonomous-livelihood planner, passive sustenance, wage loop, restaurant simulation, or later-stage content.

**Given** a valid immediately preceding P2 save
**When** the P3 ruleset migration runs
**Then** it validates the source ruleset and records the P3 stage/version and compatible content-package versions
**And** it initializes only P3-owned need timers, threshold schedules, shelter/protection state, food definitions, batches, ingredients, and crafting fixtures.

**Given** an existing character has no prior hunger or sleep-pressure history because P3 did not exist
**When** need state is initialized
**Then** the migration records a `p3_activation_baseline` at the current game second for meal and adequate-sleep timing
**And** it does not fabricate a past meal, sleep event, deprivation interval, condition, or retroactive elapsed need.

**Given** a character's P3 need state
**When** it is inspected
**Then** last qualifying baseline/event, elapsed time, next threshold, priority band, and `Starved` or `Exhausted` stack count are distinct persisted values
**And** the player and NPC characters use the same need and condition rules.

**Given** authored household and shelter fixtures required by P3
**When** content loads
**Then** beds, usable food facilities, and current protection state have stable IDs and physical locations
**And** a bed and protection remain separate requirements.

**Given** the six P3 food fixtures are loaded
**When** recipe content is validated
**Then** Raw Cabbage, Cabbage Stew, Pound Cake, Sauerkraut, Cooked Meat, and Cured Meat each declare exact ingredients, tools/facilities, occupied and unoccupied work, Stamina, yield, servings, raw-edibility, and shelf life
**And** duplicate IDs, invalid references, or incomplete recipes fail before migration.

**Given** P3 ingredients or existing food are initialized
**When** authoritative state is inspected
**Then** every quantity has a physical location or possessor and follows the proven P2 ownership and access rules
**And** migration does not grant remote use or unexplained inventory.

**Given** a food batch model is introduced
**When** its schema is validated
**Then** it supports a stable batch ID, exact recipe/version, quantity or servings, completion time, and one expiration timestamp
**And** no nutrition, macronutrient, storage-quality, or ingredient-age-inheritance simulation is added.

**Given** the P2 branch already contains places, access, resources, effects, knowledge, plans, and history
**When** migration succeeds
**Then** all prior causal state, IDs, revisions, door/property state, pools, and scheduled events remain unchanged
**And** only P3-owned baseline and fixture state is added.

**Given** migration is retried
**When** the destination ruleset is already P3
**Then** the existing result is recovered or recognized as complete
**And** need clocks, thresholds, ingredients, recipes, batches, protection, and fixtures are not duplicated.

**Given** migration or content validation fails
**When** the transaction rolls back
**Then** the original P2 save remains readable and unchanged
**And** no partial P3 ruleset marker or survival state becomes visible.

**Given** a migrated P3 branch is saved and loaded
**When** compatibility validation completes
**Then** ruleset metadata, activation baselines, need clocks, scheduled thresholds, food state, facilities, beds, and protection restore exactly
**And** loading does not advance a need timer while the game is closed.

**Given** migration tests run against real isolated SQLite databases
**When** success, retry, rollback, incompatible source, skipped stage, malformed content, and save/load cases execute
**Then** every outcome matches the typed migration contract
**And** no LLM call is required to establish survival truth.

### Story 5.2: Become Starved and Recover by Eating

As a player,
I want hunger to create visible pressure without taking control of my choices,
So that eating—or deliberately postponing it—has consistent consequences.

**Acceptance Criteria:**

**Given** a character is 0–8 hours from the last completed meal or P3 activation baseline
**When** hunger priority is evaluated
**Then** the character is satisfied
**And** no `Starved` stack is scheduled before the 24-hour threshold.

**Given** elapsed time since the last completed meal reaches 8, 16, or 20 hours
**When** hunger priority is evaluated
**Then** it becomes low, competing with ordinary work/leisure, or urgent enough to interrupt noncritical plans respectively
**And** the player receives information and consequences rather than a forced intention.

**Given** 24 consecutive hours pass without a completed meal
**When** the need-threshold phase resolves
**Then** one `Starved` stack is applied and another threshold is scheduled every additional 24 hours
**And** each threshold uses the shared scheduler's stable phase-two ordering.

**Given** one or more `Starved` stacks are active
**When** Effective Maximum Health is calculated
**Then** it equals `round(Base Maximum Health × 0.75^stacks)`
**And** the authored multiplicative exception is not merged into ordinary additive percentage stacking.

**Given** a new `Starved` stack lowers Effective Maximum Health below current Health
**When** same-second recalculation occurs
**Then** current Health clamps to the new maximum
**And** the clamp is not damage and fires no damage or wound trigger.

**Given** repeated `Starved` stacks cause Effective Maximum Health to round to zero
**When** terminal state resolves
**Then** current Health becomes zero and the character dies
**And** death follows the proven resource rules without a separate starvation-death shortcut.

**Given** a character has physical access to one complete edible serving
**When** the eating action completes
**Then** exactly one serving leaves inventory through a recorded consumption event, the hunger timer resets, and one `Starved` stack is removed
**And** restored Effective Maximum Health does not heal current Health.

**Given** a character has several `Starved` stacks
**When** one complete serving is eaten
**Then** exactly one stack is removed
**And** additional servings or qualifying meals are required to remove additional stacks.

**Given** a meal action completes at the exact 24-hour threshold
**When** same-second phases resolve
**Then** eating completes during phase one and prevents that threshold's phase-two `Starved` stack
**And** narration cannot reverse the committed ordering.

**Given** an eating action is interrupted before the serving is consumed
**When** completed phases commit
**Then** the serving remains in inventory and the hunger timer does not reset
**And** elapsed time may still cause the scheduled threshold to resolve.

**Given** a serving is expired, disliked, or poor tasting but remains edible
**When** it is completely eaten
**Then** it still resets hunger and removes one `Starved` stack
**And** taste affects choice or willingness to pay rather than physiological qualification.

**Given** a quantity is less than one complete serving or the item is not edible
**When** consumption is attempted
**Then** it does not qualify as a meal
**And** the action cannot silently reset hunger or remove `Starved`.

**Given** ward protection expires or another non-consumption event occurs
**When** hunger state is evaluated
**Then** no food is removed automatically
**And** inventory changes only through recorded eating, transfer, theft, spoilage use, or destruction events.

**Given** an NPC's hunger priority changes during P3
**When** state updates
**Then** thresholds and conditions apply through the same rules as the player
**And** no autonomous food-seeking plan is selected before P4.

### Story 5.3: Become Exhausted and Complete Adequate Sleep

As a player,
I want fatigue and safe sleep governed by physical conditions,
So that resting, staying awake, or losing shelter produces consistent consequences.

**Acceptance Criteria:**

**Given** a character is 0–12 hours from the last completed adequate sleep or P3 activation baseline
**When** sleep priority is evaluated
**Then** the character is rested
**And** no `Exhausted` stack is scheduled before the 24-hour threshold.

**Given** elapsed time since adequate sleep reaches 12, 16, or 20 hours
**When** sleep priority is evaluated
**Then** it becomes low priority to secure a bed/safe place, high priority to begin adequate sleep, or critical enough to interrupt nonessential activity respectively
**And** the player receives pressure and information rather than a forced sleep action.

**Given** 24 consecutive hours pass without completing adequate sleep
**When** the need-threshold phase resolves
**Then** one `Exhausted` stack is applied and another threshold is scheduled every additional 24 hours
**And** each threshold uses the shared scheduler's stable phase-two ordering.

**Given** one or more `Exhausted` stacks are active
**When** Effective Maximum Stamina is calculated
**Then** it equals `round(Base Maximum Stamina × 0.75^stacks)`
**And** the authored multiplicative exception remains separate from ordinary additive percentage modifiers.

**Given** a new `Exhausted` stack lowers Effective Maximum Stamina below current Stamina
**When** same-second recalculation occurs
**Then** current Stamina clamps to the new maximum
**And** the clamp is not expenditure and fires no spending trigger.

**Given** a character begins an adequate-sleep attempt
**When** the interval is validated
**Then** it requires one continuous eight-hour interval, one usable bed within capacity, and valid protection for the whole interval
**And** all reservations, start time, planned completion, and interruption policy are persisted.

**Given** the character leaves the bed, a disruptive event wakes them, bed capacity is lost, or protection lapses before completion
**When** the sleep interval resolves
**Then** it is inadequate and neither resets the timer nor removes `Exhausted`
**And** only completed ten-minute non-strenuous-rest intervals restore ordinary Stamina.

**Given** a full eight-hour adequate-sleep interval completes
**When** phase-one completion effects resolve
**Then** the sleep timer resets, exactly one `Exhausted` stack is removed, and Stamina restores to the newly available Effective Maximum
**And** all Mana plus 25% of Effective Maximum Health, rounded up, restore under the proven resource rules.

**Given** several `Exhausted` stacks exist
**When** one adequate sleep completes
**Then** exactly one stack is removed
**And** additional adequate sleeps are required to remove additional stacks.

**Given** adequate sleep completes at the exact 24-hour threshold
**When** same-second phases resolve
**Then** phase-one sleep completion prevents that threshold's phase-two `Exhausted` stack
**And** narration cannot reverse the ordering.

**Given** protection ends at the exact second an eight-hour sleep interval completes
**When** same-second phases resolve
**Then** protection counts as valid for the completed interval
**And** its phase-three expiry applies only after sleep completion.

**Given** hunger thresholds or scheduled effects become due during sleep
**When** the scheduler reaches them
**Then** they resolve in their normal phase without automatically waking the character
**And** only an effect or event explicitly marked disruptive interrupts sleep.

**Given** a sleeping place lacks valid protection
**When** shelter state is evaluated
**Then** the place or household is `Exposed`, safe adequate sleep is blocked, and later community stability cannot qualify there
**And** `Exposed` causes no direct damage, character effect, or food loss.

**Given** a protected place lacks a usable bed
**When** sleep is attempted
**Then** adequate sleep is blocked for missing bed capacity
**And** the protected place does not become `Exposed` merely because it lacks a bed.

**Given** valid protection is restored through an approved source
**When** shelter state recalculates
**Then** the cause of `Exposed` is removed
**And** no arbitrary Health, inventory, or food restoration occurs.

**Given** an NPC becomes tired during P3
**When** sleep priority changes
**Then** timers and conditions apply through the same rules as the player
**And** autonomous shelter-seeking plans remain disabled until P4.

### Story 5.4: Prepare and Persist Authored Food Batches

As a player,
I want to prepare varied food through physical ingredients, facilities, effort, and time,
So that meals are produced through consistent world actions rather than appearing from narration.

**Acceptance Criteria:**

**Given** the player declares a known food recipe
**When** preparation is validated
**Then** required ingredients, quantities, tools/facilities, physical access, occupied work, unattended processing, Stamina, yield, and shelf life are fixed before commitment
**And** all inputs and outputs reference stable content versions.

**Given** an ingredient, required facility, tool, access right, or full Stamina cost is missing
**When** preparation is attempted
**Then** the action is rejected before any input, time, Stamina, job, or output commits
**And** no substitute is invented automatically.

**Given** exact inputs for a known recipe are available
**When** preparation begins
**Then** the known recipe is routine and requires no roll
**And** a substitution or novel method uses the ordinary declared contextual-difficulty rules.

**Given** raw cabbage is available and edible
**When** one serving is eaten over ten minutes
**Then** one serving is consumed and qualifies as a meal
**And** its authored shelf life is seven days.

**Given** cabbage, water, a hearth, and a pot are available
**When** Cabbage Stew completes after 30 occupied minutes and 5 Stamina
**Then** one input set produces a batch of two servings
**And** the batch expires two days after completion.

**Given** flour, sugar, butter, and an oven are available
**When** Pound Cake completes after 60 occupied minutes and 10 Stamina
**Then** one input set produces a batch of four servings
**And** the batch expires five days after completion.

**Given** cabbage, salt, and a crock are available
**When** Sauerkraut setup completes after 15 occupied minutes and 5 Stamina
**Then** one 72-hour unattended fermentation job is scheduled with its inputs reserved
**And** successful completion produces four servings with a 30-day shelf life.

**Given** raw meat, a hearth, and a pan are available
**When** Cooked Meat completes after 20 occupied minutes and 5 Stamina
**Then** one input set produces a batch of two servings
**And** the batch expires two days after completion.

**Given** raw meat, salt, and a curing rack are available
**When** Cured Meat setup completes after 30 occupied minutes and 5 Stamina
**Then** one 48-hour unattended curing job is scheduled with its inputs reserved
**And** successful completion produces two servings with a 14-day shelf life.

**Given** occupied preparation work is interrupted before completion
**When** completed phases commit
**Then** no finished batch is created
**And** input reservation/consumption, elapsed time, and Stamina follow the recipe's declared interruption policy without duplication.

**Given** fermentation or curing is in unattended processing
**When** game time advances
**Then** the actor may perform other supported actions while the scheduled job progresses
**And** closing the game pauses the shared clock rather than advancing the job offline.

**Given** an unattended job reaches completion
**When** its scheduled event commits
**Then** reserved inputs are consumed and one output batch is created atomically
**And** retry, replay, or load cannot complete the same job twice.

**Given** ingredients have different ages
**When** a recipe finishes
**Then** the output batch receives `completion time + recipe shelf life` as its expiration timestamp
**And** ingredient age and storage quality do not shorten or lengthen it in P3.

**Given** a batch contains multiple servings
**When** servings are transferred, eaten, or destroyed
**Then** batch quantity decreases through recorded events while the remaining servings retain the same expiration timestamp
**And** quantity is conserved.

**Given** a recipe defines taste, preference, price, or optional effects
**When** the food is evaluated
**Then** those authored properties may affect choice, willingness to pay, or declared effects
**And** taste does not change whether one complete serving resets hunger.

### Story 5.5: Eat Expired Food and Resolve Poisoning

As a player,
I want expired food to remain usable but increasingly risky,
So that scarcity creates a deliberate tradeoff rather than arbitrary food deletion.

**Acceptance Criteria:**

**Given** a food batch has not reached its expiration timestamp
**When** a serving is eaten
**Then** no food-poisoning check occurs
**And** normal meal consumption and any explicitly authored food effects resolve.

**Given** a food batch is past expiration
**When** spoilage risk is calculated
**Then** risk equals `min(100%, 5% + 95% × time past expiration / declared shelf life)` rounded to the nearest whole percent
**And** all time values use the authoritative game clock.

**Given** a calculated spoilage risk
**When** a Constitution-check difficulty is selected
**Then** the engine chooses the difficulty whose achievable failure chance is nearest that risk for the eater's actual modifier
**And** natural 1 and 20 bound the realized failure probability to 5%–95%.

**Given** an expired serving is about to be eaten
**When** the action is prepared
**Then** known expiration, consumption time, calculated risk, Constitution modifier, selected difficulty, actual probability, and success/failure consequences are fixed before rolling
**And** unknown spoilage details remain knowledge-filtered under the P3 UX contract.

**Given** the eating action completes
**When** its transaction commits
**Then** one serving is consumed, hunger resets, one `Starved` stack is removed, and the recorded Constitution result resolves atomically
**And** the food qualifies as a meal on both success and failure.

**Given** the Constitution check succeeds
**When** the expired serving is consumed
**Then** no food-poisoning effect is created
**And** success-only XP uses the ordinary probability-based formula, including zero XP for near-certain 95% success.

**Given** the Constitution check fails while the food is no more than 25% of one shelf life overdue
**When** consumption commits
**Then** one generated Subtle physiological food-poisoning effect is applied within its accepted source budget
**And** failed-check XP remains zero.

**Given** the food is more than 25% and no more than 75% of one shelf life overdue
**When** the Constitution check fails
**Then** one generated Standard physiological food-poisoning effect is applied within its accepted source budget
**And** its definition includes stable mechanics, duration, removal, and knowledge visibility.

**Given** the food is more than 75% of one shelf life overdue
**When** the Constitution check fails
**Then** one generated Major physiological food-poisoning effect is applied within its accepted source budget
**And** the fictional source cannot exceed the Major effect limits.

**Given** spoilage risk reaches 100% by formula
**When** the bounded d20 check resolves
**Then** a natural 20 can still succeed under the universal check rule
**And** the displayed actual failure probability is 95%, not a false guaranteed failure.

**Given** a food-poisoning effect is active
**When** removal is attempted
**Then** it requires its declared cause, a compatible physiological/disease remedy, or an exact-effect remedy
**And** a magical dispel or unrelated wound treatment cannot remove it.

**Given** an expired-food action is retried, reconnected, replayed, or narrated again
**When** idempotency is checked
**Then** the existing result is returned
**And** the serving, hunger reset, `Starved` removal, roll, XP, effect, and elapsed time are not duplicated.

**Given** the batch and resulting poisoning state are saved and loaded
**When** play resumes
**Then** expiration, remaining servings, risk inputs, committed roll evidence, effect definition/version, instance, duration, and removal contract persist
**And** loading cannot reroll the check or regenerate different mechanics.

### Story 5.6: Inspect, Persist, and Verify Survival State

As a player,
I want hunger, fatigue, shelter, food, and recovery state to remain visible and persistent,
So that survival consequences are understandable rather than surprising or arbitrary.

**Acceptance Criteria:**

**Given** the player opens the P3 status view
**When** the survival projection renders
**Then** it shows current and Effective Maximum resources, known active effects/stacks, time since the last meal and adequate sleep, and exact time to the next `Starved` and `Exhausted` stack
**And** the facts are stated without recommending an action.

**Given** the player inspects shelter, food, or crafting state
**When** the P3 interface renders
**Then** it shows legitimately known bed usability/capacity, protection or `Exposed` state, servings, batch expiration when known, required inputs/facilities, and occupied or unattended job progress
**And** it does not reveal hidden resources, private ownership, unknown effects, or NPC plans.

**Given** survival state changes
**When** thresholds, meals, sleep, crafting, expiry, poisoning, recovery, interruption, or death resolve
**Then** the accessible P3 UX labels and announces the committed state without relying on color or stealing focus
**And** keyboard, pointer, screen-reader, zoom, reflow, contrast, target-size, and reduced-motion requirements remain satisfied.

**Given** a P3 branch is saved
**When** the snapshot is written
**Then** it includes ruleset metadata, activation baselines, last-meal/adequate-sleep times, priority bands, next thresholds, `Starved`/`Exhausted` stacks, `Exposed` causes, sleep intervals/reservations, food definitions/batches, servings, expiration, crafting jobs, reserved inputs, facilities, poisoning evidence/effects, and scheduled events
**And** all P0–P2 state remains present.

**Given** the snapshot is loaded
**When** compatibility and integrity validation complete
**Then** every need clock, threshold, stack, sleep interval, protection state, batch, job, serving, expiry, roll, effect, and resource value matches the saved branch
**And** closing or loading the game advances no offline need, sleep, spoilage, or crafting time.

**Given** the hunger boundary matrix
**When** satisfied, low, competing, urgent, critical, repeated 24-hour, exact-threshold meal, interrupted meal, several-stack, and death cases run
**Then** priorities, schedules, `Starved`, Health maxima/clamps, eating, stack removal, and death match the approved rules
**And** food never disappears without a recorded event.

**Given** the sleep boundary matrix
**When** rested, low, high, critical, repeated 24-hour, adequate, interrupted, capacity loss, bed loss, protection loss, exact-threshold completion, and exact-expiry cases run
**Then** priorities, `Exhausted`, Stamina maxima/clamps, recovery, `Exposed`, and same-second ordering match the approved rules
**And** a missing bed and missing protection remain distinct failures.

**Given** all six authored food fixtures
**When** exact preparation, missing-input/facility, substitution, occupied interruption, unattended processing, completion, serving transfer, consumption, and batch depletion cases run
**Then** inputs, Stamina, work, schedules, yield, expiration, quantity, hunger, and atomicity match each recipe
**And** fresh output expiration is independent of ingredient age.

**Given** unexpired and expired servings across the spoilage boundaries
**When** risk, nearest-achievable Constitution difficulty, natural-roll limits, success-only XP, and failure effects are exercised
**Then** risk rounding, actual probability, meal qualification, Subtle/Standard/Major selection, and effect persistence match the approved rules
**And** even maximally overdue food remains edible rather than being deleted.

**Given** the P3 controlled evidence run
**When** it exercises every threshold, condition, recipe, spoilage tier, one failure/recovery path, save/load, and one unplanned but supported survival approach
**Then** resource, time, quantity, access, condition, effect, and persistence evidence is complete
**And** player feedback records what changed, what felt unfair, and what should happen next.

**Given** an unexplained threshold-order error, resource or serving conservation failure, automatic food loss, hidden-state leak, duplicate job, nonreproducible check, or save failure occurs
**When** the P3 gate is evaluated
**Then** the affected case fails and must be corrected and repeated
**And** P4 remains unauthorized until the P3 evidence gate passes with zero unexplained failures.

**Given** all P3 evidence passes
**When** the epic is closed
**Then** P3 is recorded as eligible for a separate P4 authorization decision
**And** needs do not yet create autonomous jobs, purchases, cooking, theft, shelter-seeking, or other NPC plans until P4 is explicitly authorized.

## Epic 6: Let Needs Become Plans

Players can observe NPCs pursue food, work, trade, cooking, shelter, and sleep through finite physical actions, then replan honestly when resources, access, or opportunities fail.

### Story 6.1: Upgrade NPC Needs Into Executable Plans

As a returning player,
I want NPC needs to become real plans without inventing resources or past activity,
So that residents begin living through the same world rules I use.

**Acceptance Criteria:**

**Given** the P3 evidence gate has not passed, P4 lacks explicit authorization, or no P4 UX contract has been approved
**When** a P4 build or migration is requested
**Then** the upgrade is unavailable
**And** no autonomous livelihood planning, wage, purchase, cooking, or off-screen execution is activated.

**Given** P4 is authorized
**When** the P4 release is composed
**Then** it extends the existing NPC-planning slice to compile need-driven plans into proven actions
**And** it introduces no P5 community-victory, alchemy, ward-pressure, additional cast, or later-stage systems.

**Given** a valid immediately preceding P3 save
**When** the P4 ruleset migration runs
**Then** it validates the source ruleset and records the P4 stage/version and compatible content-package versions
**And** it initializes only P4-owned wants, plan state, livelihood opportunities, finite ledgers, and controlled fixture data.

**Given** the controlled Ivo fixture is initialized
**When** its starting state is inspected
**Then** Ivo has 0 discretionary gold, is 12 hours since food and 12 hours since adequate sleep, and knows the authored courier opportunity and relevant local resources
**And** no unexplained prior wage, meal, work, or passive income is created.

**Given** the controlled Tessa fixture is initialized
**When** her business state is inspected
**Then** it has exactly 12 gold and six cabbages priced at 1 gold each
**And** its budget and stock can change only through completed recorded transactions.

**Given** Ivo's home fixture is initialized for P4
**When** its relevant state is inspected
**Then** the protected home has the proven access state, hearth, pot, and bed required by supported plans
**And** no resource is available unless it physically exists and Ivo can reach it.

**Given** an NPC plan is created
**When** its model is validated
**Then** it records the motivating want, known goal, candidate plan, ordered typed steps, requirements, reservations, status, expected time/cost, failure cause, and decision reasons
**And** it contains no direct inventory, gold, need, or world mutation.

**Given** a candidate plan is selected
**When** it becomes executable
**Then** each step compiles into ordinary travel, access, work, transaction, craft, eat, rest, or sleep commands
**And** those commands use the same validation, scheduler, random source, commit coordinator, and idempotency rules as player actions.

**Given** a plan runs while the player is elsewhere
**When** game time advances
**Then** off-screen steps pay the same inventory, gold, access, Stamina, work-time, and uncertainty costs as observed steps
**And** no continuously running autonomous agent or offline progression process is created.

**Given** game time is paused because the application is closed or awaiting non-fictional interaction
**When** NPC planning is evaluated
**Then** no plan step, need clock, job, purchase, meal, sleep interval, condition, or death advances
**And** reopening resumes only from persisted state.

**Given** a prior P3 branch already contains needs, effects, food, access, knowledge, resources, and history
**When** migration succeeds
**Then** every existing causal record, timer, batch, condition, door, belief, and branch identifier remains unchanged
**And** only the declared P4 fixture and plan state is added.

**Given** migration is retried or fails
**When** idempotency or rollback is evaluated
**Then** a completed migration is not duplicated and a failed migration leaves the original P3 save readable and unchanged
**And** no partial plan, wage, stock, gold, or P4 marker becomes visible.

**Given** a migrated P4 branch is saved and loaded
**When** compatibility validation completes
**Then** wants, candidate/selected plans, step status, reservations, finite business ledgers, failure causes, and decision reasons restore exactly
**And** loading does not execute or reselect a plan step.

**Given** migration quality tests run against real isolated SQLite databases
**When** success, retry, rollback, incompatible source, skipped stage, fixture validation, and save/load cases execute
**Then** every outcome matches the typed migration contract
**And** the LLM cannot create authoritative fixture state.

### Story 6.2: Choose Feasible Hunger and Shelter Goals

As a player,
I want NPC needs to influence priorities without erasing personality or obligations,
So that residents pursue believable solutions rather than following a survival script.

**Acceptance Criteria:**

**Given** an NPC's current need state
**When** goal priority is evaluated
**Then** physiological pressure is considered alongside personality, taste, obligations, knowledge, relationships, resources, risk, time, and current circumstances
**And** need level does not directly mutate inventory, money, access, or plan outcome.

**Given** an NPC is normally hungry
**When** hunger candidates are generated
**Then** supported options may include accessible prepared food, preparation of owned ingredients, purchase, restaurant use, hospitality, borrowing, trade, sale, help-seeking, or work for gold
**And** only options the NPC knows and can feasibly attempt are retained.

**Given** an NPC's hunger becomes urgent
**When** candidates are ranked
**Then** socially costly but supported options may receive greater weight
**And** owned, lawful, relationship-preserving alternatives remain eligible when feasible.

**Given** an NPC is `Starved` or near death
**When** risky hunger candidates are considered
**Then** trespass, theft, lockpicking, or forced entry become eligible only if personality, knowledge, fear, relationships, risks, and remaining alternatives support them
**And** severe need never makes every NPC criminal or violent.

**Given** an NPC needs adequate sleep
**When** shelter candidates are generated
**Then** supported options may include returning home, renting lodging, requesting hospitality, sharing or obtaining a bed, repairing shelter, securing protection, relocating, or first obtaining required resources
**And** every candidate obeys access, capacity, time, budget, relationship, and knowledge constraints.

**Given** a candidate requires an unknown job, seller, bed, route, facility, price, or permission
**When** feasibility is checked
**Then** the candidate is excluded or begins with a supported information-seeking step
**And** the planner cannot use authoritative hidden state as NPC knowledge.

**Given** two feasible candidates differ in duration or resource cost
**When** the NPC chooses between them
**Then** time and cost influence ranking
**And** they do not automatically override personality, taste, relationships, obligations, safety, or preference.

**Given** routine state and authored rules determine one ordinary choice
**When** goal selection runs
**Then** deterministic planning may select it without an LLM call
**And** the reasons remain recorded.

**Given** consequential ambiguity or replanning requires LLM judgment
**When** a candidate plan is proposed
**Then** strict contracts bound the goal and steps to the NPC's actual knowledge and feasible actions
**And** deterministic validation rejects invented resources, access, relationships, jobs, or outcomes.

**Given** a selected plan has multiple steps
**When** it is accepted
**Then** the order, stopping conditions, reservations, expected costs, and failure branches are recorded before execution
**And** later failure triggers replanning rather than silent substitution or direct goal completion.

**Given** hunger or fatigue priority changes while a noncritical plan is active
**When** the next decision boundary occurs
**Then** the NPC may continue, pause, interrupt, or replace the plan according to the approved priority bands and recorded context
**And** a critical need does not retroactively undo completed work.

**Given** the player is not present for goal selection
**When** the NPC chooses a plan
**Then** no private plan or decision reason appears in ordinary player views
**And** the player is interrupted only by events they can reasonably perceive.

**Given** the player later observes absence, movement, work, purchase, preparation, eating, sleeping, or a consequence
**When** presentation is generated
**Then** it derives from completed plan steps and perceptible state
**And** it does not reveal unobserved alternatives or internal ranking.

### Story 6.3: Work for a Finite Wage and Buy Food

As a player,
I want NPC work and purchases to move real time, money, and stock,
So that livelihoods cannot create resources from nowhere.

**Acceptance Criteria:**

**Given** the controlled P4 starting state
**When** Ivo evaluates his resources
**Then** he has 0 discretionary gold and cannot purchase a 1-gold cabbage
**And** no unexplained 3-gold balance or passive income exists.

**Given** Ivo knows Tessa's four-hour courier opportunity
**When** the job plan is validated
**Then** the work place, duration, required access/tools, 3-gold wage, employer, and completion condition are fixed
**And** payment cannot occur merely because the plan was selected.

**Given** Tessa has at least 3 uncommitted gold and the job is accepted
**When** the shift begins
**Then** 3 gold is reserved against Tessa's finite 12-gold business ledger
**And** it is not yet owned by Ivo.

**Given** Ivo completes the full four-hour courier shift
**When** the completion transaction commits
**Then** the reserved 3 gold transfers from Tessa to Ivo exactly once
**And** completed work, elapsed time, employer expense, worker income, and plan progress reconcile atomically.

**Given** the shift is interrupted, abandoned, invalidated, or fails before completion
**When** completed phases commit
**Then** Ivo receives no wage under the controlled contract and the reservation is released according to its recorded policy
**And** any elapsed time, need thresholds, effects, or perceivable events that actually occurred remain.

**Given** Tessa lacks 3 available gold when the job is proposed
**When** feasibility is checked
**Then** the shift cannot begin under the controlled contract
**And** no wage, debt, or replacement employer is invented.

**Given** the courier opportunity is unavailable, its required place is inaccessible, or required tools are missing
**When** Ivo reaches that step
**Then** the failure cause is recorded and the plan stops at that boundary
**And** Ivo replans from his new time, hunger, fatigue, knowledge, and resources.

**Given** Ivo owns the completed 3-gold wage and knows Tessa sells cabbage for 1 gold
**When** he physically reaches the business and purchases one cabbage
**Then** 1 gold transfers from Ivo to Tessa and one cabbage transfers from Tessa's stock to Ivo atomically
**And** Ivo ends with 2 gold while Tessa's business ends with the reconciled wage expense, sale income, and five cabbages.

**Given** Tessa's cabbage stock is sold out or the known price exceeds Ivo's owned funds
**When** purchase validation runs
**Then** the purchase is rejected without partial money, stock, or time mutation
**And** Ivo replans rather than receiving food or credit automatically.

**Given** business demand, closure, access, or the counterparty changes before purchase
**When** Ivo attempts the transaction
**Then** current authoritative state is revalidated at commitment
**And** a stale expectation cannot overdraw money or stock.

**Given** Ivo's hunger priority changes during the shift or travel
**When** a decision boundary occurs
**Then** he may continue, interrupt, or replace the plan according to the approved priority and context
**And** completed work or transactions are not retroactively erased.

**Given** the player observes the shift and purchase or remains elsewhere
**When** the plan executes
**Then** both paths use identical work, scheduler, ledger, access, and transaction handlers
**And** only the presentation and legitimately perceived evidence differ.

**Given** a work or purchase operation is retried, reconnected, or restored
**When** idempotency is checked
**Then** the prior result is recovered
**And** wage, gold, cabbage, work completion, time, observations, and plan progress cannot commit twice.

### Story 6.4: Cook, Eat, Sleep, and Replan After Failure

As a player,
I want Ivo to turn earned food into a meal and pursue rest through real actions,
So that his needs improve only when his plan actually succeeds.

**Acceptance Criteria:**

**Given** Ivo has bought a cabbage and knows his protected home is accessible
**When** he evaluates how to eat
**Then** stew is eligible when the hearth, pot, water, time, and Stamina are available
**And** raw cabbage remains a supported alternative.

**Given** Ivo chooses stew and reaches his home
**When** preparation completes
**Then** the P3 recipe consumes its inputs and 5 Stamina over 30 minutes and produces two servings with the approved expiration
**And** selecting the plan alone creates no food or hunger relief.

**Given** the hearth is unusable or another stew requirement fails before preparation
**When** Ivo reaches that step
**Then** the failed requirement and any completed travel or other costs remain recorded
**And** he replans from current state, which may include eating the cabbage raw.

**Given** Ivo has physical access to a complete edible serving
**When** he finishes eating it
**Then** one serving is consumed, his meal timer resets, and one `Starved` stack is removed if present
**And** neither an intended meal nor an unfinished eating action satisfies hunger.

**Given** Ivo has eaten and needs sleep
**When** he chooses a shelter plan
**Then** he considers his known home, bed capacity, protection, access, time, and other feasible options
**And** eating does not automatically complete sleep or refill resource pools.

**Given** Ivo occupies an available bed in his protected home for eight uninterrupted hours
**When** adequate sleep completes
**Then** his sleep timer resets, one `Exhausted` stack is removed if present, and the approved Stamina, Mana, and Health recovery occurs
**And** the bed and protection must remain valid throughout the interval.

**Given** protection is lost, the bed becomes unavailable, or sleep is disrupted before completion
**When** the interval ends
**Then** it does not qualify as adequate sleep
**And** Ivo records the failure and replans using only known, reachable, affordable shelter options.

**Given** work, purchase, preparation, eating, or sleep fails
**When** Ivo replans
**Then** he retains every completed wage, purchase, item transfer, cost, elapsed second, need threshold, effect, and observation
**And** no step is silently undone or replaced with an invented resource.

**Given** Ivo's hunger or fatigue becomes critical during the sequence
**When** he reaches the next decision boundary
**Then** priorities may change according to the proven need bands and his recorded circumstances
**And** neither condition guarantees one scripted choice.

**Given** the player is present for some steps but absent for others
**When** Ivo completes the sequence
**Then** every step uses the same authoritative commands and scheduler
**And** the player sees only actions and consequences they could perceive or later learn.

**Given** the sequence is saved, loaded, retried, or interrupted
**When** execution resumes
**Then** current plan step, reservations, food batches, need clocks, bed interval, costs, and completed results restore exactly
**And** no wage, purchase, craft, meal, or sleep completion occurs twice.

### Story 6.5: Consider Risky Options Under Severe Need

As a player,
I want desperate NPCs to consider risky choices in character,
So that survival pressure creates believable possibilities without making theft or violence automatic.

**Acceptance Criteria:**

**Given** an NPC is hungry but has a feasible owned or lawful way to eat
**When** hunger plans are ranked
**Then** that option remains eligible and its cost, time, taste, obligations, and relationships are considered
**And** hunger alone does not select trespass, theft, lockpicking, or force.

**Given** an NPC is `Starved` or near death and lawful options have failed or become infeasible
**When** risky candidates are considered
**Then** the planner checks personality, fear, relationships, known opportunities, likely witnesses, access, tools, Stamina, and remaining alternatives
**And** it records why each candidate is eligible or excluded.

**Given** a risky candidate relies on a location, item, or permission the NPC does not know about
**When** feasibility is checked
**Then** the candidate is excluded or begins with supported information gathering
**And** the planner cannot use hidden world truth as the NPC's knowledge.

**Given** trespass, theft, lockpicking, or forced entry is selected
**When** the plan executes
**Then** it uses the proven P2 access and evidence commands with their full time, tool, Stamina, check, and ownership consequences
**And** need pressure grants no automatic success or waived cost.

**Given** an unauthorized NPC physically reaches and eats a serving
**When** the meal completes
**Then** the ordinary P3 hunger benefit applies
**And** theft, trespass, observations, suspicion, and relationship consequences remain intact.

**Given** a risky access attempt fails
**When** the result commits
**Then** its actual costs, noise, damage, observations, and failed-check outcome persist
**And** the NPC replans from that changed state rather than trying indefinitely for free.

**Given** evidence of risky behavior reaches another character
**When** that character forms a belief or responds
**Then** observation, contact, confidence, personality, and relationship state govern the response
**And** no universal crime score, guard response, arrest, court, or guaranteed accusation is created.

**Given** an NPC's condition worsens while no feasible food or shelter plan exists
**When** time advances
**Then** `Starved`, `Exhausted`, immobility, and potentially death follow the ordinary resource and need rules
**And** the planner does not fabricate rescue, food, money, or protection to avoid the outcome.

**Given** identical severe-need fixtures differ in personality, knowledge, relationships, or available lawful options
**When** plans are selected
**Then** risky actions may be eligible in one fixture and excluded in another for recorded reasons
**And** no “all desperate NPCs steal” rule is encoded.

**Given** risky behavior occurs outside the player's perception
**When** the player-facing state updates
**Then** it reveals only later observable absence, damage, behavior, dialogue, or reports
**And** private plan reasons and unseen acts remain available only to diagnostics until learned.

### Story 6.6: Persist and Verify Observed and Off-Screen Livelihoods

As a playtester,
I want NPC plans to execute consistently whether or not I watch them,
So that their livelihoods are causal world activity rather than presentation tricks.

**Acceptance Criteria:**

**Given** Ivo's controlled P4 starting state
**When** his feasible work → buy → cook or eat raw → eat → sleep sequence completes
**Then** every wage, purchase, ingredient, serving, action duration, Stamina cost, access check, meal, and sleep interval reconciles
**And** no step succeeds solely because a plan or narration says it happened.

**Given** identical captured saves and recorded decision/random inputs
**When** one run is observed and the other occurs off-screen
**Then** both use the same commands, scheduler, costs, transactions, need thresholds, and resulting mechanical state
**And** only player perception and presentation differ.

**Given** work is unavailable or Tessa lacks the wage funds
**When** Ivo reaches the work step
**Then** no wage is created and the failure cause is recorded
**And** he replans from his actual resources and need state.

**Given** cabbage stock is sold out
**When** Ivo reaches the purchase step
**Then** no gold or food transfers
**And** his next plan uses only known, feasible alternatives.

**Given** the home hearth becomes unusable after purchase
**When** Ivo reaches the cooking step
**Then** no stew is produced or ingredient silently consumed
**And** eating the cabbage raw remains eligible if it is still reachable and edible.

**Given** protection is lost before adequate sleep completes
**When** the sleep interval resolves
**Then** it does not qualify as safe adequate sleep
**And** Ivo replans for protection or another known shelter without inventing one.

**Given** hunger becomes severe during a failed livelihood route
**When** Ivo considers riskier options
**Then** their eligibility follows his personality, knowledge, relationships, risks, and remaining lawful alternatives
**And** any chosen trespass, theft, lockpicking, or force uses full P2 costs and evidence rules.

**Given** an off-screen plan produces injury, zero Stamina, or death
**When** its causal steps are inspected
**Then** each cost, effect, threshold, and terminal result is recorded in order
**And** no persistent off-screen death exists without a complete causal chain.

**Given** an NPC acts while the player is elsewhere
**When** a scheduled event occurs
**Then** the player is interrupted only if they could reasonably perceive it
**And** other outcomes become knowable through later observation, absence, conversation, or rumor.

**Given** a P4 branch is saved during work, travel, purchase, preparation, eating, or sleep
**When** it is loaded
**Then** the current plan step, reservations, finite ledgers, inventory, need clocks, work and sleep intervals, event queue, failure history, and decision reasons restore exactly
**And** no step executes, pays, or replans twice on load.

**Given** the P4 UX shows a known livelihood consequence
**When** it renders
**Then** it distinguishes observed action, received report, and player inference without exposing private plans or hidden state
**And** the interface remains keyboard-, pointer-, and screen-reader-operable at required zoom and reflow sizes.

**Given** the controlled P4 evidence run
**When** it exercises the successful Ivo/Tessa chain, every declared failure branch, one failure/recovery path, save/load, off-screen equivalence, and one unplanned supported approach
**Then** conservation, timing, access, needs, plan changes, knowledge, and persistence evidence is recorded
**And** player feedback captures what changed, why Ivo acted, what felt unfair, and what should happen next.

**Given** an unexplained fabricated resource, divergent off-screen outcome, knowledge leak, duplicate wage or meal, missing failure replan, or save failure occurs
**When** the P4 gate is evaluated
**Then** the affected case fails and must be corrected and repeated
**And** P5 remains unauthorized until the P4 evidence gate passes with zero unexplained failures.

**Given** all P4 evidence passes
**When** the epic closes
**Then** P4 is recorded as eligible for a separate P5 authorization decision
**And** household victory, ward pressure, and alchemy remain absent until P5 is explicitly authorized.

## Epic 7: Secure Brackenford's Future Through Play

Players can sustain four households through protection, relocation, work, trade, food, commitments, and personal alchemy while supported mixed solutions remain valid.

### Story 7.1: Upgrade to Four Households and the P5 Starting State

As a returning player,
I want Brackenford's households and ward to become concrete world state,
So that I can understand what each resident needs before choosing how to help.

**Acceptance Criteria:**

**Given** P4 evidence has not passed, P5 lacks explicit authorization, or no P5 UX contract has been approved
**When** a P5 build or migration is requested
**Then** the upgrade is unavailable
**And** no household-stability, ward, commitment, or alchemy state is activated.

**Given** P5 is authorized
**When** the release is composed
**Then** it adds only the P5 community-viability and alchemy slices to the proven P0–P4 rules
**And** P6–P9 spells, quests, bonuses, and combat remain absent.

**Given** a valid immediately preceding P4 save
**When** its P5 migration runs
**Then** the source ruleset and content versions are validated and the P5 stage/version is recorded atomically
**And** existing time, money, resources, relationships, needs, plans, knowledge, and history remain unchanged.

**Given** the four P5 household definitions load
**When** their authored content is validated
**Then** Mara, Oren, Tessa, and Ivo each belong to one one-resident household with a concrete home, local resources, bed, and protection state
**And** no fifth named resident or procedurally generated location is introduced.

**Given** a household is inspected
**When** its authoritative state is read
**Then** resident, home, bed, local food and funds, current protection source, and separate stability record have stable identities
**And** promises or expected future income are not counted as resources already delivered.

**Given** the independent controlled P5 starting fixture
**When** it is created
**Then** the player starts that fixture with 30 gold, a Field Alchemy Kit, a Brewer's Crock, and knowledge of Healing Draft, Mana Draft, Weak Toxin, and Common Ale
**And** the P0 test pouch and all P0 branch outcomes are discarded rather than carried into the P5 economy.

**Given** the controlled P5 ward baseline
**When** the fixture begins
**Then** the ward provides seven simulated days of protection with an inspectable remaining duration
**And** its timer advances only on the shared game clock.

**Given** P5 content is loaded
**When** households, protection routes, tools, ingredients, and base recipes are validated
**Then** each has a stable authored ID and compatible content version
**And** missing references, duplicate IDs, or malformed definitions fail before campaign mutation.

**Given** a live P4 campaign is migrated rather than the independent P5 fixture being created
**When** initialization completes
**Then** it receives only the P5 state justified by its authored current world and activation time
**And** it is not granted the fixture's 30 gold or retroactive meals, sleep, wages, protection work, or alchemy crafts.

**Given** migration or fixture creation is retried
**When** idempotency is checked
**Then** the prior result is returned or recognized as complete
**And** households, ward time, tools, recipes, gold, or ruleset markers are not duplicated.

**Given** validation or persistence fails
**When** the transaction rolls back
**Then** the original P4 save remains readable and unchanged
**And** no partial household, ward, alchemy, or P5 ruleset state becomes visible.

**Given** the P5 starting state is saved and loaded
**When** compatibility checks complete
**Then** households, homes, resources, beds, protection, ward time, tools, known recipes, fixture origin, and all earlier-stage state restore exactly
**And** no ward time advances while the game is closed.

### Story 7.2: Track Three Days of Lived Stability

As a player,
I want each household's stability measured from what its resident actually does,
So that securing Brackenford is a lived outcome rather than a quest flag.

**Acceptance Criteria:**

**Given** P5 begins for a branch
**When** household evaluation is initialized
**Then** each of Mara, Oren, Tessa, and Ivo has a separate streak starting at zero
**And** no earlier P4 activity is counted retroactively.

**Given** a completed 86,400-second evaluation window anchored at P5 activation
**When** one household is evaluated
**Then** it qualifies only if its resident ate through a recorded action before the next `Starved` threshold, completed eight hours of adequate sleep in a bed protected for that interval, and remained in a household that was not `Exposed`
**And** all three conditions must be supported by committed events; partial pre-P5 days do not count.

**Given** a meal was promised, planned, purchased, or prepared but not eaten
**When** the day is evaluated
**Then** it does not satisfy the meal condition
**And** no food is consumed merely to make the household qualify.

**Given** sleep was attempted but interrupted, lacked a usable bed, or lost protection before completion
**When** the day is evaluated
**Then** it does not satisfy the adequate-sleep condition
**And** ordinary rest recovery does not make inadequate sleep qualify.

**Given** a household has a valid bed and food but its sleeping place is `Exposed`
**When** the day is evaluated
**Then** it does not qualify
**And** `Exposed` causes no automatic damage, inventory loss, or food deletion.

**Given** food, lodging, or protection depends on a wage, transfer, crop, service, or agreement
**When** qualification is checked
**Then** only resources actually earned, transferred, produced, or contractually guaranteed by a committed enforceable agreement count
**And** an unaccepted promise or hoped-for future income does not count.

**Given** a household qualifies for a completed day
**When** its evaluation commits
**Then** its streak increases by one exactly once with the supporting meal, sleep, protection, and resource evidence recorded
**And** other households' streaks are unchanged.

**Given** a household fails a completed day
**When** its evaluation commits
**Then** only that household's streak resets to zero
**And** the failure itself causes no arbitrary loss of food, gold, Health, or relationships.

**Given** a supported relocation has changed a resident's accepted home
**When** later days are evaluated
**Then** the resident's actual destination bed, food, and protection are used
**And** changing an address alone does not satisfy stability.

**Given** all four households reach three consecutive qualifying days
**When** the evaluator commits the result
**Then** community victory is recorded once from the underlying evidence
**And** no quest flag or narration can grant victory independently.

**Given** community victory is recorded
**When** play continues
**Then** agreements, trade, departures, needs, and protection still evolve under ordinary rules
**And** the world is not reset or ended.

**Given** the evaluator is retried or the branch is saved and loaded near a day boundary
**When** evaluation resumes
**Then** each household's streak and supporting evidence restore exactly
**And** a day is not counted or reset twice.

### Story 7.3: Repair the Ward or Arrange Protection

As a player,
I want ward repair and patrol agreements to provide real, paid protection,
So that safeguarding households depends on completed work and commitments.

**Acceptance Criteria:**

**Given** the controlled P5 ward starts with seven days of protection
**When** the player inspects it
**Then** the remaining duration is shown from the authoritative game clock
**And** no wall-clock time passes while the application is closed.

**Given** the ward reaches three days or one day of remaining protection
**When** a long wait crosses that threshold
**Then** the corresponding warning interrupts the wait at its actual game second
**And** each warning is recorded and delivered at most once.

**Given** the ward reaches expiry without replacement protection
**When** the environmental transition commits
**Then** its protection ends and affected sleeping places become `Exposed`
**And** no food disappears, automatic damage occurs, or irreversible lockout is imposed.

**Given** the player proposes ward repair
**When** its terms are presented
**Then** the required 12 gold in materials and two separate four-hour work actions are declared before commitment
**And** materials, workers, access, and available time must be real and feasible.

**Given** the required materials are not funded or obtainable from owned resources
**When** repair is attempted
**Then** the repair cannot begin or complete
**And** neither a future promise nor narration creates the missing materials.

**Given** one four-hour repair action completes
**When** its result commits
**Then** the completed work and any paid costs persist
**And** the ward is not repaired until the second required action also completes.

**Given** both four-hour work actions and the 12-gold material requirement are completed
**When** the final repair transaction commits
**Then** the ward provides 30 days of protection from that committed repair
**And** the effect, costs, work evidence, and expiry schedule are recorded exactly once.

**Given** repair work is interrupted or a worker cannot pay a required action cost
**When** the attempt resolves
**Then** only completed work and costs persist under their declared policies
**And** unfinished work cannot be counted toward the two completed actions.

**Given** the player proposes a settlement-wide patrol contract
**When** its terms are presented
**Then** the 18-gold contract cost plus 1 gold for each of its first three days is explicit
**And** the provider, covered households, start, payment schedule, and evaluating authority are recorded before acceptance.

**Given** the patrol agreement is accepted and required funds are paid or contractually guaranteed
**When** patrol coverage begins
**Then** covered households have a valid protection source for the funded interval
**And** neither an unaccepted promise nor an unpaid day grants protection.

**Given** a scheduled patrol payment fails or the agreement ends
**When** the coverage transition resolves
**Then** protection from that contract ends according to its terms
**And** households become `Exposed` only if no other valid protection source remains.

**Given** ward and patrol protection overlap
**When** one source expires
**Then** the other remains independently valid until its own expiry
**And** protection is not removed merely because one source ended.

**Given** repair, patrol acceptance, payment, warning, or expiry is retried or restored from a save
**When** the operation resumes
**Then** costs, work, warnings, protection, and scheduled transitions retain their committed state
**And** none is paid, delivered, or applied twice.

**Given** the player learns that ward protection expired
**When** the consequence is presented
**Then** the explanation identifies the resulting shelter state without recommending a route
**And** repair, a valid protection agreement, relocation, or another recorded equivalent remains possible.

### Story 7.4: Relocate Households and Support Mixed Solutions

As a player,
I want residents to be able to relocate or combine supported solutions,
So that Brackenford's future is shaped by their circumstances rather than one required route.

**Acceptance Criteria:**

**Given** relocation is proposed for one household
**When** its terms are presented
**Then** the 5-gold cost, named destination, resident, travel, required acceptance, bed, and protection expectations are explicit
**And** the cost is assessed separately for each household.

**Given** no named destination exists or the destination has not accepted the resident
**When** relocation is evaluated
**Then** the household does not move or gain destination protection
**And** a declaration of intent cannot substitute for acceptance.

**Given** the resident and destination agree, the route is supported, and 5 gold is available from owned funds
**When** the relocation completes
**Then** the cost and travel time commit, the resident's actual home changes, and the household retains its stable identity
**And** the destination's bed, local resources, and protection become the facts used for later need and stability evaluation.

**Given** relocation negotiation or travel fails before completion
**When** the attempt resolves
**Then** only explicitly completed time, payments, and other consequences persist under their declared terms
**And** neither the address change nor a qualifying stable day is invented.

**Given** a relocated resident reaches a destination without a usable bed, food, or valid protection
**When** the day is evaluated
**Then** the household fails whichever lived-stability condition is unmet
**And** relocation alone is not victory.

**Given** one household relocates while others remain in Brackenford
**When** protection and stability are evaluated
**Then** each household uses its own actual location, resources, bed, and protection source
**And** a settlement-wide route is not imposed on every resident.

**Given** ward repair, patrol coverage, relocation, stocked food, work, restaurant meals, hospitality, farming, or another supported plan provides a needed condition
**When** its committed actions are evaluated
**Then** the same meal, adequate-sleep, non-`Exposed`, and funding rules apply
**And** the evaluator does not privilege a named route or quest flag.

**Given** a proposed solution relies on farming, hospitality, or another activity beyond currently supported actions
**When** validation runs
**Then** it succeeds only if the necessary place, resources, time, agreement, and actions are actually supported and committed
**And** narration cannot invent the missing subsystem or output.

**Given** Tessa, Ivo, or Mara considers a community route
**When** their preferences are evaluated
**Then** Tessa's interest in dependable trade, Ivo's overdue pay, and Mara's wish to live nearer her ill sister may influence their starting positions
**And** later offers, relationships, needs, and evidence may change those positions without a fixed decision script.

**Given** two or more protection or supply routes overlap
**When** one ends or fails
**Then** the remaining valid resources and agreements continue to count on their own terms
**And** only households that fail a daily condition reset their streak.

**Given** relocation or a mixed route is saved, loaded, retried, or replayed
**When** its state is restored
**Then** destination acceptance, household identity, location, resources, costs, agreements, protection, and stability evidence remain consistent
**And** no travel, payment, transfer, or daily qualification is duplicated.

### Story 7.5: Record Concerns and Explicit Commitments

As a player,
I want to see which problems remain open and what people have actually agreed to do,
So that I can judge progress without mistaking a proposal or promise for a completed outcome.

**Acceptance Criteria:**

**Given** the player learns of a need or conflict without agreeing to an outcome
**When** the journal records it
**Then** it appears as an open concern with its known source and status
**And** it is not presented as an accepted commitment or quest.

**Given** a player or NPC proposes an agreement
**When** the proposal is recorded
**Then** its parties, required outcome, deadline if any, evaluating authority, and exact reward or lack of reward are stated in plain language
**And** it remains proposed until the relevant parties accept it.

**Given** a proposal is accepted
**When** acceptance commits
**Then** an accepted commitment with stable identity and version is recorded
**And** unowned resources, unperformed work, and hoped-for future income are not treated as already delivered.

**Given** an accepted commitment’s stated outcome is achieved
**When** its named evaluator checks committed evidence
**Then** it becomes fulfilled exactly once
**And** any NPC reward is transferred only from resources the rewarding party owns or has already validly committed.

**Given** the required outcome is not achieved under its agreed terms
**When** failure or deadline expiry is evaluated
**Then** the commitment moves to the applicable failed or expired state with a recorded reason
**And** neither fulfillment nor a reward is invented.

**Given** a party explicitly abandons an active commitment
**When** that decision commits
**Then** the commitment becomes abandoned with its history intact
**And** any resulting time, resource, or relationship consequence follows the stated agreement and ordinary rules.

**Given** the parties agree to change an accepted commitment
**When** renegotiation commits
**Then** the changed outcome, parties, deadline, evaluator, or reward is recorded as a new agreement version
**And** the prior terms and their status remain inspectable rather than being silently rewritten.

**Given** a concern or commitment contains information the player has not legitimately learned
**When** the journal is rendered
**Then** only the player-known terms and status are shown
**And** private motives, hidden resources, and evaluator-only evidence remain concealed.

**Given** household stability is evaluated
**When** a commitment is offered as support for food, lodging, or protection
**Then** only an enforceable accepted agreement or resources actually delivered under it may count
**And** the commitment’s status alone never grants a qualifying day or community victory.

**Given** a commitment transition is retried, interrupted, saved, or loaded
**When** its operation resumes
**Then** its identity, version, terms, evidence, status, and any committed reward restore consistently
**And** no acceptance, fulfillment, payment, or reward occurs twice.

**Given** the journal is used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the player inspects a concern or commitment
**Then** its type, parties, terms, deadline, status, and reward or lack of reward have readable labels
**And** status is not conveyed by color alone.

**Given** Story 7.5 automated evidence
**When** integration and browser tests run
**Then** concern/proposal separation, acceptance, each terminal state, renegotiation, evidence-based fulfillment, resource-backed rewards, knowledge filtering, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party commitment and persistence behavior is not mocked.

### Story 7.6: Buy Ingredients From a Finite Supplier

As a player,
I want to buy alchemy ingredients from a supplier with real prices and limited stock,
So that crafting uses resources I actually acquired.

**Acceptance Criteria:**

**Given** the authorized P5 ingredient supplier
**When** its authored content loads
**Then** basic ingredients cost 1 gold each and rare catalysts cost 4 gold each
**And** its stock cannot exceed 20 basic ingredients or 4 rare catalysts.

**Given** the player can legitimately inspect the supplier’s offer
**When** the offer is displayed
**Then** known prices and available quantities are shown as factual information
**And** private supplier state or a recommended purchase is not exposed.

**Given** the player requests ingredients
**When** the purchase is validated
**Then** physical access, requested quantities, current stock, owned funds, and applicable handling time are checked before commitment
**And** a statement that the player has funds or ingredients cannot substitute for authoritative state.

**Given** the supplier has stock and the player has sufficient owned gold
**When** the purchase completes
**Then** the correct gold moves from player to supplier, stock decreases, and purchased ingredients enter the player’s inventory in one transaction
**And** the clock advances only by the completed purchase’s validated speech and handling time.

**Given** stock or owned funds are insufficient
**When** the purchase is attempted
**Then** the specific shortage is explained
**And** no gold, stock, inventory, or fictional time changes.

**Given** the shared clock reaches 06:00
**When** the scheduled supplier restock resolves
**Then** basic and rare stock replenish only up to their respective limits of 20 and 4
**And** restocking never adds a full limit on top of remaining stock.

**Given** a wait or off-screen action crosses a 06:00 restock
**When** the scheduled event is processed
**Then** the restock occurs at its actual game second in the established deterministic event order
**And** it is recorded only once even if processing is interrupted or resumed.

**Given** a purchase or restock is retried, saved, or loaded
**When** its state is recovered
**Then** player funds, supplier funds and stock, owned ingredients, clock, and event evidence restore consistently
**And** no payment, ingredient transfer, or restock is duplicated.

**Given** the independent P5 economy fixture is used
**When** its ledgers are inspected
**Then** the player begins with the fixture’s 30 gold and can spend only that branch’s owned funds
**And** the P0 10,000-gold pouch and its isolated branch outcomes are absent.

**Given** Story 7.6 automated evidence
**When** integration and browser tests run
**Then** exact prices, stock caps, successful and rejected purchases, 06:00 restock, interruption recovery, conservation, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party inventory, clock, and persistence behavior is not mocked.

### Story 7.7: Craft Known Base Recipes

As a player,
I want to make the recipes my character already knows using real ingredients and tools,
So that crafting produces durable items at a predictable cost in materials and time.

**Acceptance Criteria:**

**Given** the authorized P5 starting state
**When** the character’s crafting knowledge is inspected
**Then** Healing Draft, Mana Draft, Weak Toxin, and Common Ale are known recipes
**And** Alchemy and Brewing are universal basic skills that begin with a +0 bonus.

**Given** the four base recipes load
**When** their authored definitions are validated
**Then** Healing Draft, Mana Draft, and Weak Toxin each require two basic ingredients and 30 minutes of work, while Common Ale requires one basic ingredient and 60 minutes
**And** each definition has a stable ID, version, product identity, value, and declared mechanics.

**Given** the player proposes a known base recipe with its exact inputs
**When** the required ingredients, accessible workspace, and tool are available
**Then** an Alchemy recipe requires the Field Alchemy Kit and Common Ale requires the Brewer’s Crock
**And** the player is shown the inputs, work duration, and expected product before commitment.

**Given** a known base recipe has valid exact inputs and prerequisites
**When** its work completes
**Then** it succeeds without a roll
**And** the specified ingredients are consumed, the exact product enters inventory, and only the completed work time advances the shared clock.

**Given** an ingredient, required tool, accessible workspace, or other prerequisite is missing
**When** the craft is validated
**Then** the specific missing prerequisite is explained before work begins
**And** no ingredient, time, product, roll, or XP is committed.

**Given** a proposed method changes a known recipe’s inputs or procedure
**When** it is interpreted
**Then** it is not silently treated as a routine exact-recipe craft
**And** no substitute ingredient is consumed or product created without a separately validated uncertain approach.

**Given** a craft is interrupted before completion
**When** its state is recorded
**Then** only work and costs completed under the terms disclosed before commitment persist
**And** no finished product appears until the required work completes.

**Given** a base craft succeeds
**When** its result is persisted
**Then** the product records its exact recipe and definition version and the action records one successful production event
**And** crafting alone does not apply the product’s effects or grant a recipe unlock.

**Given** a completed craft request is retried, recovered, or loaded
**When** its result already exists
**Then** the same product and production event are returned
**And** ingredients, elapsed time, output, and production evidence are not duplicated.

**Given** the player inspects a recipe or completed product with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** its information is displayed
**Then** recipe name, ingredients, tool, work time, product, and status have readable labels
**And** no essential information depends on color, hover, or horizontal page scrolling.

**Given** Story 7.7 automated evidence
**When** integration and browser tests run
**Then** all four exact base recipes, tool and access requirements, no-roll success, rejected prerequisites, interruption, product versioning, one-time production evidence, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party crafting and persistence behavior is not mocked.

### Story 7.8: Attempt an Uncertain Crafting Substitution

As a player,
I want to try a plausible change to a known recipe with disclosed risks,
So that experimentation can succeed or fail under the same trustworthy rules as other checks.

**Acceptance Criteria:**

**Given** the controlled substitution fixture
**When** the player proposes a Healing Draft using one basic ingredient and one bruised duskroot instead of the usual two basic ingredients
**Then** the attempt is classified as uncertain rather than routine
**And** it still requires the Field Alchemy Kit, an accessible workspace, and ownership of both ingredients.

**Given** the substitution is feasible
**When** its terms are presented before commitment
**Then** the player sees the 30-minute work period, that both ingredients will be consumed on either completed outcome, and that failure produces no draft
**And** the check uses the current Mind modifier plus Alchemy bonus against difficulty 12.

**Given** the check is admitted
**When** pre-roll evidence is recorded
**Then** the target, modifier sources, actual probability, success product, failure loss, and work time are fixed before rolling
**And** natural 1 fails and natural 20 succeeds at those admitted stakes.

**Given** the controlled check succeeds
**When** the completed craft commits
**Then** both ingredients are consumed, 30 minutes advance, and one normal Healing Draft with its existing definition version enters inventory
**And** one successful production event and any eligible G18 check XP commit with the result.

**Given** the controlled check fails
**When** the completed craft commits
**Then** both ingredients are consumed and 30 minutes advance, but no product is created
**And** no production success, recipe-track progress, or check XP is awarded.

**Given** the player lacks an ingredient, tool, accessible workspace, or another prerequisite
**When** validation occurs before work begins
**Then** the specific issue is reported without a roll
**And** no ingredient, time, product, XP, or production count changes.

**Given** another substitution or novel method is proposed
**When** it can be bounded to a supported product and feasible approach
**Then** its contextual difficulty and both outcomes are declared before commitment
**And** the method does not silently unlock a recipe or create an unvalidated product definition.

**Given** a proposed method has no supportable product, ingredients, procedure, or bounded outcome in the active P5 rules
**When** validation runs
**Then** it is neutrally clarified or factually rejected
**And** narration cannot fabricate a new recipe, product, effect, or success.

**Given** the same completed attempt is retried or an unchanged failed approach is resubmitted
**When** its prior resolution is found
**Then** the recorded roll and outcome govern the attempt
**And** the player receives no new roll, output, XP, or production opportunity.

**Given** the craft commits but narration fails, or the branch is saved and loaded
**When** the result is recovered
**Then** consumed inputs, elapsed time, roll evidence, output or failure, XP, and production event restore exactly
**And** narration cannot change the committed mechanics.

**Given** the player inspects the uncertain craft result
**When** its details open by keyboard, pointer, or screen reader
**Then** the target, modifiers, pre-roll probability, natural die, result, consumed inputs, elapsed time, and product or failure are readable
**And** the details remain usable at 200% zoom and 320-pixel reflow.

**Given** Story 7.8 automated evidence
**When** integration and browser tests run
**Then** the exact bruised-duskroot fixture, success and failure costs, natural-roll overrides, pre-roll disclosure, prerequisite rejection, unchanged-attempt protection, idempotency, and recovery are verified against the real application and SQLite store
**And** only interpretation and narration at the external LLM boundary may use deterministic contract fixtures.

### Story 7.9: Use Crafted Restoratives and Brewed Drinks

As a player,
I want crafted potions and drinks to have the effects their recipes promise,
So that making or acquiring them gives me useful, persistent choices.

**Acceptance Criteria:**

**Given** a finished Healing Draft, Mana Draft, or Common Ale
**When** its inventory entry is inspected
**Then** the product shows its known effect, use conditions, and exact definition version
**And** crafting or merely carrying it has not applied that effect.

**Given** the player proposes to use a product
**When** the action is validated
**Then** ownership or permitted access, the recipient, physical reach, consumption method, and handling time are checked
**And** an unsupported target or method is clarified or rejected before any item or time is consumed.

**Given** a living recipient consumes a Healing Draft
**When** the use commits
**Then** Health increases by 25% of Effective Maximum Health, rounded up but capped at that maximum, and one Minor Wound is removed if present
**And** the draft cannot remove a Severe Wound or revive a dead character.

**Given** a recipient consumes a Mana Draft
**When** the use commits
**Then** Mana increases by 25% of Effective Maximum Mana, rounded up but capped at that maximum
**And** no Health, wound, or unrelated resource changes.

**Given** a recipient consumes Common Ale
**When** the use commits
**Then** a versioned 60-second effect applies −2 to Perception and offers +1 to at most one eligible Presence-based check during that interval
**And** use of that one-check bonus is recorded so later checks cannot reuse it.

**Given** a valid product use completes
**When** the transaction commits
**Then** exactly one product is consumed, its resource or effect changes and validated handling time commit together, and the resulting state is inspectable
**And** no check XP is awarded merely for routine consumption.

**Given** the player gives a finished product to another character without using it
**When** the transfer completes
**Then** ownership or possession changes under the ordinary transaction rules
**And** the product’s restorative or drink effect is not applied by the transfer alone.

**Given** an active Common Ale effect expires or its one-check bonus is spent
**When** later checks are resolved
**Then** only still-active, unused modifiers apply
**And** the saved effect history remains visible without silently extending its duration or uses.

**Given** product use is retried, interrupted, saved, or loaded
**When** its operation or branch is recovered
**Then** the consumed item, pools, wounds, effect instance, remaining duration or uses, and elapsed time restore from committed state
**And** no item or effect is consumed or applied twice.

**Given** Rowan narrates a product use
**When** the committed result is presented
**Then** the description agrees with the actual resource and effect changes
**And** player-facing prose is never reparsed to determine mechanics.

**Given** the player inspects or uses a product with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the inventory and result views render
**Then** the product, recipient, effect, limits, remaining duration or use, and operation status have readable labels
**And** essential information is not conveyed by color alone.

**Given** Story 7.9 automated evidence
**When** integration and browser tests run
**Then** exact Healing Draft, Mana Draft, and Common Ale effects; caps and wound limits; transfer-versus-use; expiry and one-check use; invalid targets; idempotency; and save/load are verified against the real application and SQLite store
**And** first-party inventory, resources, effects, and persistence behavior is not mocked.

### Story 7.10: Apply and Trigger Crafted Poison

As a player,
I want a crafted toxin to remain on a real item until contact, consumption, cleaning, or expiry,
So that its effects follow what happened in the world rather than narration alone.

**Acceptance Criteria:**

**Given** a finished Weak Toxin
**When** its known properties are inspected
**Then** it declares weapon contact-on-hit and food consumption as supported delivery methods
**And** its damage, modifiers, duration, and definition version are stable.

**Given** the player proposes coating a weapon or food item
**When** the action is validated
**Then** the toxin and target item must physically exist and be reachable, and the method and handling time must be supported
**And** ownership or permission consequences follow the existing access and property rules.

**Given** a valid coating completes
**When** it commits
**Then** one Weak Toxin is consumed and a versioned coating instance is attached to the specific target item
**And** applying the coating alone deals no damage or condition effect.

**Given** a proposed coating lacks a reachable item, toxin, supported method, or other required condition
**When** validation rejects it
**Then** the specific limitation is reported
**And** no toxin, target property, fictional time, damage, or effect changes.

**Given** Weak Toxin coats a weapon
**When** a qualifying successful hit occurs within ten game minutes
**Then** the coating triggers on that one contact
**And** no later hit can trigger the same coating again.

**Given** ten game minutes pass without a qualifying hit
**When** the weapon coating expires
**Then** it can no longer trigger
**And** expiry deals no damage or condition effect.

**Given** Weak Toxin coats food
**When** the food remains unconsumed
**Then** the coating remains on that specific food item until consumption or a supported cleaning action
**And** the weapon’s ten-minute limit is not applied to food.

**Given** coated food is consumed, or a coated weapon records a qualifying hit
**When** exposure commits
**Then** the exposed character takes 10 Health damage and receives −2 to Perception and Athletics for 60 game seconds through the existing resource and effect rules
**And** any food-serving or terminal Health outcome is resolved by its own established rules in the same transaction.

**Given** a coating is cleaned off before exposure
**When** cleaning completes
**Then** that coating is removed from the item with its causal history retained
**And** no poison damage or condition effect is applied.

**Given** a coating, exposure, cleaning, or expiry is interrupted, retried, saved, or loaded
**When** its state is recovered
**Then** the exact item, coating version, remaining use or time, exposure evidence, Health change, and condition restore consistently
**And** neither a toxin nor its effect is consumed or applied twice.

**Given** a character has not observed a coating or exposure
**When** player-facing or NPC knowledge is projected
**Then** hidden item properties and inferred culprit identity are not revealed merely because authoritative state contains them
**And** later observation or communication may establish knowledge through recorded evidence.

**Given** a controlled P5 weapon-contact fixture is exercised
**When** it emits a qualifying hit into the existing action/effect transaction
**Then** the poison resolves without adding P9 encounter rounds, initiative, or a second combat engine
**And** non-qualifying contact does not trigger it.

**Given** Story 7.10 automated evidence
**When** integration and browser tests run
**Then** weapon and food coating, successful-hit and consumption triggers, exact damage and modifiers, expiry, cleaning, hidden-knowledge boundaries, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party item, resource, effect, and persistence behavior is not mocked.

### Story 7.11: Earn Mana-Restoration Recipes

As a player,
I want successful mana-draft crafting to offer stronger recipes I can choose to learn,
So that practice expands what I can make without replacing what I already know.

**Acceptance Criteria:**

**Given** a craft succeeds
**When** its production event commits
**Then** exactly one success is credited to its healing, mana-restoration, poison, or brewing track
**And** failures, rejected attempts, and replayed requests do not increase any track count.

**Given** the mana-restoration track has fewer than ten successful crafts
**When** its progress is inspected
**Then** Mana Draft remains available and no higher-tier mana recipe is offered
**And** successes in the other three tracks do not advance the mana count.

**Given** the tenth mana-restoration craft succeeds
**When** its result commits
**Then** Mana Elixir is offered for adoption exactly once for that threshold event
**And** the player can inspect its ingredients, work time, effect, and value before accepting or declining.

**Given** the player declines Mana Elixir
**When** that choice commits
**Then** the recipe remains unknown and the declined offer is recorded
**And** the next successful mana-restoration craft offers it again without replaying the tenth craft.

**Given** the player accepts Mana Elixir
**When** adoption commits
**Then** its stable definition version becomes known without consuming ingredients or fictional time
**And** Mana Draft remains known and craftable.

**Given** Mana Elixir is known and its exact prerequisites are available
**When** the player completes its routine craft
**Then** two basic ingredients and one rare catalyst are consumed over 60 minutes of work to produce one Mana Elixir valued at 10 gold
**And** using it restores 50% of Effective Maximum Mana, rounded up and capped at that maximum.

**Given** the twenty-fifth total mana-restoration craft succeeds
**When** its result commits
**Then** Deepwell Tonic is offered for adoption under the same inspect, accept, decline, and next-success re-offer rules
**And** the threshold counts successful Mana Draft and Mana Elixir crafts in that track without requiring prior adoption of Mana Elixir.

**Given** Deepwell Tonic is adopted and its exact prerequisites are available
**When** the player completes its routine craft
**Then** three basic ingredients and two rare catalysts are consumed over 120 minutes to produce one Deepwell Tonic valued at 18 gold
**And** using it restores Mana to Effective Maximum Mana without exceeding that maximum.

**Given** a tier recipe is not adopted or its ingredients, tool, workspace, or access are missing
**When** crafting is attempted
**Then** the exact prerequisite is reported before work begins
**And** no ingredients, time, item, roll, or production count changes.

**Given** an offer decision, craft, or product use is retried, interrupted, saved, or loaded
**When** its state is recovered
**Then** counts, offer history, known recipes, product definitions, ingredients, Mana, and time restore from committed evidence
**And** no threshold offer, adoption, craft, or effect is duplicated.

**Given** recipe progress and offers are displayed with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the player inspects or decides on an offer
**Then** the track count, threshold, recipe terms, choice, and persisted status have readable labels
**And** declining remains a real choice rather than an automatic adoption.

**Given** Story 7.11 automated evidence
**When** integration and browser tests run
**Then** independent track counting, 10/25 boundaries, decline/re-offer/adoption, both mana recipes, their exact costs and effects, unchanged base access, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party crafting, progression, inventory, and resource behavior is not mocked.

### Story 7.12: Learn and Use Restorative Elixir

As a player,
I want healing practice to unlock a remedy for serious injuries,
So that a severe wound can be treated through a recipe I earned and supplied.

**Acceptance Criteria:**

**Given** the healing track has fewer than ten successful crafts
**When** its progress is inspected
**Then** Healing Draft remains known and Restorative Elixir is not yet offered
**And** successes in mana, poison, or brewing do not advance the healing count.

**Given** the tenth healing-track craft succeeds
**When** its production event commits
**Then** Restorative Elixir is offered for adoption with its ingredients, work time, effect, and value visible
**And** the offer is recorded once for that threshold event.

**Given** the player declines the offer
**When** the next healing-track craft succeeds
**Then** Restorative Elixir is offered again
**And** the earlier decline remains in the offer history without changing the success count.

**Given** the player accepts the offer
**When** adoption commits
**Then** Restorative Elixir becomes a known, versioned recipe without consuming materials or fictional time
**And** Healing Draft remains known and craftable.

**Given** Restorative Elixir is known and the prerequisites are available
**When** its exact routine craft completes
**Then** two basic ingredients and one rare catalyst are consumed over 60 minutes using the Field Alchemy Kit and an accessible workspace
**And** one Restorative Elixir valued at 10 gold enters inventory with a successful healing-track production event and no roll.

**Given** a living recipient uses a Restorative Elixir
**When** the use commits
**Then** Health is restored by 50% of Effective Maximum Health, rounded up under the existing percentage-restoration convention and capped at that maximum
**And** one selected Severe Wound or crippling injury, including a lost-limb condition, is removed if present.

**Given** the recipient has more than one qualifying injury
**When** the elixir is used
**Then** the injury to be removed is identified before commitment
**And** no second injury is silently removed.

**Given** the recipient is dead
**When** Restorative Elixir use is proposed
**Then** it is rejected because this product cannot revive
**And** no elixir, fictional time, wound, or Health state changes.

**Given** an adopted recipe lacks ingredients, kit, accessible workspace, or another prerequisite
**When** crafting is validated
**Then** the specific missing prerequisite is reported before work begins
**And** no materials, time, output, or production count changes.

**Given** an offer decision, craft, or use is retried, interrupted, saved, or loaded
**When** its state is recovered
**Then** the offer history, known recipe, ingredients, product version, Health, injury state, and time restore from committed evidence
**And** no adoption, production event, item use, or healing effect is duplicated.

**Given** Story 7.12 automated evidence
**When** integration and browser tests run
**Then** the independent healing threshold, decline/re-offer/adoption, exact recipe, routine craft, Health cap, single-injury removal, no-revival restriction, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party crafting, wound, resource, and persistence behavior is not mocked.

### Story 7.13: Earn and Use a Draught of Revival

As a player,
I want an earned remedy to reverse a recent death under strict limits,
So that revival is possible without erasing the injury or history that led to it.

**Acceptance Criteria:**

**Given** the healing track reaches 25 total successful crafts
**When** that production event commits
**Then** Draught of Revival is offered for adoption with its costs, effect, and 120-second use window visible
**And** the offer uses the established accept, decline, and next-success re-offer rules independently of whether Restorative Elixir was adopted.

**Given** the player adopts Draught of Revival
**When** the choice commits
**Then** its versioned recipe becomes known without consuming materials or fictional time
**And** Healing Draft and any previously adopted healing recipe remain available.

**Given** the adopted recipe’s exact prerequisites are available
**When** its routine craft completes
**Then** three basic ingredients and two rare catalysts are consumed over 120 minutes using the Field Alchemy Kit and an accessible workspace
**And** one Draught of Revival valued at 24 gold enters inventory with one healing-track production event and no roll.

**Given** a character reaches 0 Health
**When** death commits
**Then** a stable death-event identity and game-second timestamp are recorded
**And** ordinary narration or item possession alone cannot reverse that state.

**Given** an accessible dead recipient has not been revived for that death event
**When** a Draught is administered at or before 120 game seconds after the recorded death
**Then** one Draught is consumed and the recipient returns to life at 25% of Effective Maximum Health, rounded up under the existing percentage-restoration convention
**And** Severe Wounds and other injuries remain unless a separate supported treatment removes them.

**Given** more than 120 game seconds have passed since death
**When** administration is attempted
**Then** the use is rejected with the expired-window reason
**And** the Draught, Health, injuries, and fictional time remain unchanged.

**Given** the application is closed or the player is reading a menu while a recipient is dead
**When** eligibility is checked
**Then** the window is calculated from authoritative game seconds, not wall-clock time
**And** no time passes merely because the application was closed or a view was open.

**Given** the same death event was already reversed by a Draught
**When** another administration is attempted for that event
**Then** it is rejected without consuming another item
**And** a later distinct death event has its own independently evaluated eligibility.

**Given** the target is alive, physically unreachable, or the actor lacks a usable Draught
**When** administration is validated
**Then** the specific prerequisite failure is reported before commitment
**And** no item, time, Health, wound, or death-event state changes.

**Given** revival commits
**When** its result is recorded
**Then** the death event, administered item, recipient, elapsed game seconds, restored Health, retained wounds, world revision, and request result are linked atomically
**And** prior consequences are not silently undone beyond the stated revival effect.

**Given** administration is retried, interrupted, saved, or loaded
**When** the operation or branch is recovered
**Then** the exact death event, eligibility window, item use, Health, and wounds restore from committed evidence
**And** neither the Draught nor its revival effect can apply twice.

**Given** the revival action is presented with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the player reviews its terms or result
**Then** the game clearly distinguishes a living target, eligible recent death, expired window, pending operation, and committed revival
**And** no narration claims revival before authoritative commitment.

**Given** Story 7.13 automated evidence
**When** integration and browser tests run
**Then** the 25-craft threshold, recipe adoption and costs, exact 120/121-second boundary, game-clock pause, once-per-death rule, retained wounds, invalid targets, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party death, resource, crafting, and persistence behavior is not mocked.

### Story 7.14: Learn and Use Potent Venom

As a player,
I want poison-crafting practice to unlock a stronger toxin,
So that its increased risk and effect come from a recipe I earned and real materials I spent.

**Acceptance Criteria:**

**Given** the poison track has fewer than ten successful crafts
**When** its progress is inspected
**Then** Weak Toxin remains known and Potent Venom is not yet offered
**And** successes in healing, mana, or brewing do not advance the poison count.

**Given** the tenth poison-track craft succeeds
**When** its production event commits
**Then** Potent Venom is offered with its ingredients, work time, delivery methods, effect, and value visible
**And** the offer uses the established accept, decline, and next-success re-offer rules.

**Given** the player accepts Potent Venom
**When** adoption commits
**Then** its stable definition version becomes known without consuming materials or fictional time
**And** Weak Toxin remains known and craftable.

**Given** Potent Venom is known and its exact prerequisites are available
**When** its routine craft completes
**Then** two basic ingredients and one rare catalyst are consumed over 60 minutes using the Field Alchemy Kit and an accessible workspace
**And** one Potent Venom valued at 10 gold enters inventory with one poison-track production event and no roll.

**Given** Potent Venom is applied to a reachable weapon or food item
**When** coating completes
**Then** one toxin item is consumed and a versioned coating is attached to that specific item
**And** application alone causes no damage or condition.

**Given** a coated weapon records one qualifying successful hit within ten game minutes
**When** exposure commits
**Then** the coating triggers once and cannot trigger on a later hit
**And** an untriggered weapon coating expires without effect after ten game minutes.

**Given** coated food is consumed
**When** exposure commits
**Then** its coating triggers once
**And** the weapon’s ten-minute expiry is not applied to food waiting to be consumed.

**Given** Potent Venom exposure triggers
**When** the existing resource and effect rules resolve it
**Then** the target takes 20 Health damage and receives −4 to Perception and Athletics for 120 game seconds
**And** no Weak Toxin definition, prior coating, or unrelated item is rewritten.

**Given** the recipe is unknown or its ingredients, tool, workspace, or delivery prerequisites are missing
**When** crafting or application is validated
**Then** the specific limitation is reported before commitment
**And** no inputs, time, coating, output, damage, or production count changes.

**Given** an offer, craft, coating, exposure, expiry, or item transfer is retried, interrupted, saved, or loaded
**When** its state is recovered
**Then** the chosen recipe version, item, coating, production count, damage, modifier duration, and causal evidence restore consistently
**And** no toxin or effect is duplicated.

**Given** Story 7.14 automated evidence
**When** integration and browser tests run
**Then** the independent ten-craft threshold, decline/re-offer/adoption, exact recipe, both delivery methods, 20-damage and 120-second effect, weapon expiry, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party crafting, inventory, resource, effect, and persistence behavior is not mocked.

### Story 7.15: Learn and Use Lingering Bane

As a player,
I want an earned poison whose damage unfolds on the shared clock,
So that delayed consequences remain predictable, persistent, and interruptible by valid treatment.

**Acceptance Criteria:**

**Given** the poison track reaches 25 total successful crafts
**When** that production event commits
**Then** Lingering Bane is offered with its ingredients, work time, immediate and delayed effects, delivery methods, and value visible
**And** the established accept, decline, and next-success re-offer rules apply whether or not Potent Venom was adopted.

**Given** the player adopts Lingering Bane
**When** adoption commits
**Then** its stable definition version becomes known without consuming materials or fictional time
**And** Weak Toxin and any previously adopted poison remain available.

**Given** its exact prerequisites are available
**When** a routine Lingering Bane craft completes
**Then** three basic ingredients and two rare catalysts are consumed over 120 minutes using the Field Alchemy Kit and an accessible workspace
**And** one Lingering Bane valued at 18 gold enters inventory with one poison-track production event and no roll.

**Given** Lingering Bane coats a weapon or food item
**When** application commits
**Then** one toxin item becomes a versioned coating on that specific reachable item
**And** application alone causes no damage or condition.

**Given** the coated weapon records a qualifying successful hit within ten game minutes, or coated food is consumed
**When** exposure commits
**Then** the coating triggers once and deals 10 Health damage immediately
**And** it applies −4 to Perception and Athletics for 180 game seconds.

**Given** exposure has committed and the poison remains active
**When** the shared clock reaches 60 and then 120 seconds after exposure
**Then** each scheduled tick deals 10 additional Health damage exactly once
**And** no third damage tick is generated.

**Given** an untriggered weapon coating reaches ten game minutes
**When** it expires
**Then** it can no longer cause exposure
**And** a food coating remains governed by consumption or cleaning rather than that weapon limit.

**Given** a compatible antidote or exact-effect remedy completes before a scheduled tick
**When** the shared same-second ordering is applied
**Then** the matching poison effect and its future ticks are removed according to that remedy’s declared terms
**And** damage already committed is not reversed merely by removing the effect.

**Given** scheduled damage reduces Health to zero
**When** the tick commits
**Then** the established death rule records the resulting death event
**And** narration, a later tick, or a retry cannot change the committed timestamp or apply that tick again.

**Given** the recipient is saved, loaded, or advanced through a long wait while Lingering Bane is active
**When** scheduled work resumes
**Then** the exposure time, pending tick identities, completed ticks, modifiers, and expiry restore in deterministic order
**And** game downtime adds no fictional seconds.

**Given** an offer, craft, coating, exposure, tick, remedy, or expiry is retried or interrupted
**When** the operation is recovered
**Then** only its committed costs and consequences remain
**And** no ingredient, item, production count, damage tick, or condition is duplicated.

**Given** the player can legitimately inspect an exposure or result
**When** its details are displayed by keyboard, pointer, or screen reader
**Then** the known immediate damage, delayed schedule, modifier duration, applied treatment, and current status are readable
**And** the view remains usable at 200% zoom and 320-pixel reflow without revealing unknown poison facts.

**Given** Story 7.15 automated evidence
**When** integration and browser tests run
**Then** the 25-craft threshold, adoption and exact recipe, both delivery methods, immediate and two delayed damage events, same-second remedy ordering, death, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party scheduling, resource, effect, and persistence behavior is not mocked.

### Story 7.16: Learn and Use Quality Ale

As a player,
I want brewing practice to unlock a better drink,
So that its benefits and drawbacks follow a recipe I chose to learn.

**Acceptance Criteria:**

**Given** the brewing track has fewer than ten successful crafts
**When** its progress is inspected
**Then** Common Ale remains known and Quality Ale is not yet offered
**And** successes in healing, mana, or poison do not advance the brewing count.

**Given** the tenth brewing-track craft succeeds
**When** its production event commits
**Then** Quality Ale is offered with its ingredients, work time, effect, and value visible
**And** the established accept, decline, and next-success re-offer rules apply.

**Given** the player accepts Quality Ale
**When** adoption commits
**Then** its stable definition version becomes known without consuming ingredients or fictional time
**And** Common Ale remains known and craftable.

**Given** Quality Ale is known and its exact prerequisites are available
**When** its routine craft completes
**Then** two basic ingredients are consumed over 120 minutes using the Brewer’s Crock and an accessible workspace
**And** one Quality Ale valued at 6 gold enters inventory with one brewing-track production event and no roll.

**Given** a recipient consumes Quality Ale
**When** use commits
**Then** one drink is consumed and a versioned 120-second effect applies −1 to Perception and +1 to all eligible Presence-based checks during that interval
**And** unlike Common Ale’s one-check bonus, the Quality Ale bonus is not spent after a single check.

**Given** an eligible check occurs while Quality Ale is active
**When** difficulty, probability, result, and any XP are calculated
**Then** the active +1 is included among the applicable modifiers and recorded with its source
**And** XP uses the actual pre-roll probability rather than a calculation that omits the drink.

**Given** the 120-second effect ends
**When** a later check is resolved
**Then** neither the Perception penalty nor Presence bonus applies
**And** elapsed wall-clock time while the game is closed does not shorten the game-time duration.

**Given** the recipe is unknown or its ingredients, crock, workspace, or use prerequisites are missing
**When** crafting or consumption is validated
**Then** the specific limitation is reported before commitment
**And** no materials, time, drink, production count, or effect changes.

**Given** an offer decision, craft, drink use, check, or expiry is retried, interrupted, saved, or loaded
**When** its state is recovered
**Then** the brewing count, recipe version, product, remaining effect duration, check modifiers, and time restore consistently
**And** no offer, product, check bonus, or effect is duplicated.

**Given** Story 7.16 automated evidence
**When** integration and browser tests run
**Then** the independent ten-craft threshold, decline/re-offer/adoption, exact recipe, 120-second effect, all-check bonus, probability accounting, expiry, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party crafting, checks, effects, and persistence behavior is not mocked.

### Story 7.17: Learn and Use Artisan Brew

As a player,
I want brewing mastery to unlock a drink tailored to one social skill I choose,
So that my practice creates a distinctive but temporary advantage.

**Acceptance Criteria:**

**Given** the brewing track reaches 25 total successful crafts
**When** that production event commits
**Then** Artisan Brew is offered with its ingredients, work time, effect, value, and skill choice visible
**And** the established accept, decline, and next-success re-offer rules apply whether or not Quality Ale was adopted.

**Given** the player accepts Artisan Brew
**When** the recipe-adoption choice is made
**Then** the player selects exactly one of Deception, Intimidation, Performance, or Persuasion
**And** no other skill is eligible.

**Given** no skill or an ineligible skill is submitted
**When** adoption is validated
**Then** the recipe remains unadopted with a specific error
**And** the prior offer and brewing count remain unchanged.

**Given** a valid skill is selected
**When** adoption commits
**Then** the chosen skill and recipe-definition version are saved together without consuming materials or fictional time
**And** the choice is not reselected for each batch or drink.

**Given** Artisan Brew is known and its exact prerequisites are available
**When** its routine craft completes
**Then** two basic ingredients and one rare catalyst are consumed over 240 minutes using the Brewer’s Crock and an accessible workspace
**And** one Artisan Brew valued at 12 gold enters inventory with one brewing-track production event and no roll.

**Given** a recipient consumes Artisan Brew
**When** use commits
**Then** one drink is consumed and a versioned effect grants +2 to checks using the skill chosen at recipe adoption for 120 game seconds
**And** Artisan Brew applies no Perception penalty.

**Given** a check uses a different social skill or occurs after the effect expires
**When** it resolves
**Then** Artisan Brew contributes no bonus
**And** the drink never changes the recipient’s permanent skill level or bonus.

**Given** an eligible check occurs during the active effect
**When** its probability, result, and any XP are calculated
**Then** the temporary +2 and its product source are recorded among applicable modifiers
**And** XP uses the actual pre-roll probability including that bonus.

**Given** adoption, crafting, use, expiry, or a check is retried, interrupted, saved, or loaded
**When** its state is recovered
**Then** the selected skill, recipe version, item, brewing count, remaining effect duration, and check evidence restore consistently
**And** no adoption, product, modifier, or result is duplicated.

**Given** the recipe offer and skill selector are used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the player reviews and makes the choice
**Then** all four eligible skills and the selected state have explicit labels
**And** the fixed-at-adoption consequence is explained before confirmation.

**Given** Story 7.17 automated evidence
**When** integration and browser tests run
**Then** the 25-craft threshold, each of the four eligible selections, invalid selections, exact recipe, 120-second selected-skill bonus, lack of Perception penalty, expiry, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party crafting, checks, effects, and persistence behavior is not mocked.

### Story 7.18: Sell to Finite, Need-Driven Buyers

As a player,
I want residents to buy crafted products only when those products meet a real need and they can pay,
So that selling feels like trade in Brackenford rather than an infinite cash outlet.

**Acceptance Criteria:**

**Given** the independent P5 starting fixture
**When** Mara’s state is inspected by authorized diagnostics
**Then** she has one Minor Wound and 4 owned gold reserved for at most one Healing Draft
**And** the player view exposes only what the character can legitimately know.

**Given** Mara knows of an available Healing Draft and still has a compatible wound
**When** she considers buying it
**Then** her decision uses her actual need, knowledge, relationship, obligations, and owned funds
**And** the fixture permits at most one 4-gold Healing Draft purchase without requiring a scripted yes.

**Given** Mara’s wound has been treated, the draft is unavailable, or her owned funds are insufficient
**When** demand is evaluated again
**Then** no further Healing Draft purchase is authorized from the fixture demand
**And** no daily budget refill or replacement wound is invented.

**Given** Ivo has not completed work that leaves him with at least 3 owned gold available
**When** he considers Common Ale
**Then** he cannot buy it
**And** an expected wage or an unexplained discretionary balance does not count as payment.

**Given** completed courier work and other actual spending leave Ivo with enough owned gold
**When** he learns of an available Common Ale
**Then** he may consider buying at most one based on his current needs and preferences
**And** the completed wage and any purchase have distinct, conserved ledger entries.

**Given** another resident considers a crafted product
**When** demand is evaluated
**Then** a recorded event must have created a compatible need and the resident must own sufficient funds
**And** mere product availability, a generated line of dialogue, or a hidden arbitrary budget does not create demand.

**Given** a buyer agrees to a sale
**When** the transaction completes
**Then** the declared price moves from the buyer’s owned funds to the seller, and the specific product changes possession or ownership exactly once
**And** applicable speech, handling time, and observations commit through the ordinary action rules.

**Given** a proposed sale is declined or cannot be funded or delivered
**When** the transaction is rejected
**Then** no item or purchase money transfers
**And** any separately completed conversation is timed only once under the existing speech rule.

**Given** the player gives a product rather than selling it
**When** the transfer completes
**Then** the recipient obtains it under the ordinary gift rules without paying a price
**And** the gift is not recorded as a sale or counted as sale income.

**Given** a sale, refusal, gift, or buyer plan is retried, executed off-screen, saved, or loaded
**When** its state is recovered
**Then** needs, knowledge, funds, product identity, ownership, time, and decision evidence remain consistent
**And** no buyer pays twice, buys beyond its finite demand, or receives an item that was never transferred.

**Given** the player reviews a known offer or completed trade with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** terms and status are displayed
**Then** buyer, product, price, agreed or declined status, and committed transfer have readable labels
**And** the interface does not expose private NPC budgets or recommend a sale.

**Given** Story 7.18 automated evidence
**When** integration and browser tests run
**Then** Mara’s bounded wound-driven purchase, Ivo’s earned-funds prerequisite, other buyers’ event-driven needs, refusal, gift-versus-sale, conservation, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party NPC planning, inventory, economy, and persistence behavior is not mocked.

### Story 7.19: Verify the P5 Community and Alchemy Gate

As a playtester,
I want to complete and inspect the full P5 community-and-alchemy loop,
So that later magic work builds on a world whose needs, resources, crafts, and outcomes remain causal.

**Acceptance Criteria:**

**Given** an authorized P5 build and controlled starting state
**When** its content is validated
**Then** exactly four one-resident households and twelve authored recipes across healing, mana, poison, and brewing are present with stable versions
**And** no P0 fixture wealth, procedural location, P6 spell, or later-stage reward system is activated.

**Given** two distinct, plausible supported approaches to household stability
**When** each is played through from an independent captured state
**Then** all four households earn three consecutive qualifying days from recorded meals, adequate protected sleep, and non-`Exposed` housing
**And** the evaluator does not require a particular ward, patrol, relocation, trade, or alchemy route.

**Given** one household fails a day while the other three qualify
**When** the daily evaluation commits
**Then** only the failing household’s streak resets
**And** no arbitrary food, gold, Health, or relationship loss is introduced.

**Given** a third, unplanned but supported player approach
**When** its proposals are validated and resolved
**Then** it can contribute to stability only through real places, resources, agreements, actions, and time
**And** unsupported parts receive factual limits rather than invented success.

**Given** the controlled P5 economy and crafting fixtures
**When** purchases, routine crafts, the bruised-duskroot uncertain craft, failed crafting, item uses, poison contact, recipe thresholds, and finite sales are exercised
**Then** ingredients, funds, output, work time, rolls, XP, effects, stock, demand, and ownership reconcile within each branch
**And** a failed craft consumes its declared inputs without producing an item or successful-craft count.

**Given** every authored recipe is exercised in an eligible controlled state
**When** its craft and use evidence is inspected
**Then** its exact ingredients, work duration, product identity, value, version, and bounded mechanics match the GDD
**And** generated presentation cannot change those mechanics.

**Given** a branch is saved during a household streak, craft, active poison, ward or patrol interval, or pending supplier restock
**When** it is loaded and continued
**Then** all clocks, scheduled events, resources, effects, agreements, recipe choices, counts, funds, and household evidence restore exactly
**And** no day, tick, payment, craft, restock, sale, or reward repeats.

**Given** the same captured initial state, structured proposals, content versions, and recorded random inputs
**When** mechanical replay is run
**Then** the same authoritative results and state hashes are produced
**And** newly generated prose need not be identical.

**Given** an operation fails before commitment or presentation fails after commitment
**When** recovery is exercised
**Then** the player can identify what committed and safely retry only unfinished work
**And** no resource, time, check, production count, agreement, or household qualification is duplicated.

**Given** P5 player-facing views and a phase-specific UX contract
**When** keyboard, pointer, screen-reader, 200% zoom, and 320-pixel reflow journeys are tested
**Then** household conditions, known commitments, recipe choices, product effects, and operation status are usable and appropriately knowledge-filtered
**And** private NPC plans, hidden funds, and unobserved poison facts do not leak.

**Given** the P5 playtest sessions
**When** feedback is recorded
**Then** the evidence separately captures what changed, why residents acted, what felt unfair, and what the player wants next
**And** mechanical consistency is not treated as proof that the outcome felt believable.

**Given** an unexplained contradiction, conservation error, duplicate effect, incorrect household day, unsupported recipe outcome, knowledge leak, or save/load failure
**When** the P5 gate is evaluated
**Then** the affected scenario fails and is corrected and repeated
**And** P6 remains unauthorized.

**Given** all P5 evidence passes
**When** Epic 7 closes
**Then** P5 is marked eligible for a separate P6 authorization decision
**And** affinity spells, recognition, quests, hidden bonuses, and combat remain absent until their stages are explicitly authorized.

## Epic 8: Earn a Distinctive Affinity Spell

Players can choose an affinity package, awaken a bounded Rest-concept spell, receive stable history-shaped presentation and distinct recognition, and optionally deepen the earned spell.

### Story 8.1: Choose an Affinity Package

As a player,
I want to choose one of two clearly described affinity packages,
So that my first magic reflects my choice without changing the character I already created.

**Acceptance Criteria:**

**Given** the P5 evidence gate has not passed, P6 has not been separately authorized, or no P6-specific UX contract is approved
**When** a P6 upgrade is requested
**Then** affinity selection and P6 spell state remain unavailable
**And** the existing P5 branch remains unchanged.

**Given** an eligible P5 branch is upgraded to P6
**When** migration runs
**Then** it validates the immediately preceding ruleset and content versions and records the P6 stage/version atomically
**And** all existing character, world, inventory, progression, commitment, and household state is preserved.

**Given** an upgraded character has not chosen a package
**When** the choice is displayed
**Then** exactly Ember + Fellowship and Vessel + Fellowship are offered with their skill bonuses, starting spells, Mana costs, and affinity-owned slot capacity explained
**And** neither option is preselected or committed by narration.

**Given** the player previews either package
**When** they inspect or cancel the preview
**Then** the choice changes no authoritative state, Mana, or fictional time
**And** they can still review the other package.

**Given** the player confirms Ember + Fellowship
**When** the choice commits
**Then** the character gains those two affinities, two slots belonging to each affinity, +1 Survival from the package, and Hearthspark in one Ember slot
**And** the other three slots remain unfilled.

**Given** the player confirms Vessel + Fellowship
**When** the choice commits
**Then** the character gains those two affinities, two slots belonging to each affinity, +1 Medicine from the package, and Steady Vessel in one Vessel slot
**And** the other three slots remain unfilled.

**Given** the character has an earned Survival or Medicine bonus before package selection
**When** the package bonus is applied
**Then** the +1 package source is recorded separately and adds to the existing applicable bonus
**And** confirming or recovering the same choice cannot stack the package bonus with itself.

**Given** a package is committed
**When** the character sheet is inspected
**Then** it identifies the chosen affinities, the owner and occupancy of every slot, the package skill-bonus source, and the starting spell’s fixed contract
**And** learning the starting spell consumes no Mana; Mana is paid only when a valid cast commits.

**Given** the player submits an unknown package, a stale world revision, or a second incompatible package choice
**When** validation runs
**Then** the request is rejected with a specific conflict or field error
**And** the confirmed package, slots, spell, bonuses, and prior world state are unchanged.

**Given** migration or package selection fails before commit
**When** recovery is offered
**Then** the prior readable branch and valid choice state remain intact
**And** no partial affinity, spell, skill bonus, or P6 version is exposed.

**Given** a committed migration or package choice is retried, interrupted, saved, or loaded
**When** its result is recovered
**Then** the same stage version, package, slots, spell, and bonus sources restore
**And** no second package, slot occupant, or bonus is created.

**Given** package selection is used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the player compares and confirms the packages
**Then** names, bonuses, spell terms, slot ownership, preview state, validation, and confirmation status have readable labels
**And** the choice requires no hover-only information, color-only meaning, or horizontal page scrolling.

**Given** Story 8.1 automated evidence
**When** integration and browser tests run
**Then** stage gating, adjacent-version migration, both package choices, four affinity-owned slots, exact bonuses and starting spells, nonstacking, invalid choices, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party migration, character, spell, and persistence behavior is not mocked.

### Story 8.2: Use a Starting Spell

As a player,
I want to cast the starting spell from my chosen affinity package,
So that my first magic has a useful, predictable effect in the world.

**Acceptance Criteria:**

**Given** the player inspects their starting spell
**When** its details are displayed
**Then** the fixed spell identity, owning affinity and slot, 8-Mana cost, range, duration, valid targets, and effect are stated
**And** the displayed terms match the committed spell definition rather than generated narration.

**Given** an Ember + Fellowship character has at least 8 Mana
**When** they validly cast Hearthspark on a target within 10 m
**Then** they can ignite, extinguish, or sustain one hand-sized nonmagical flame, or safely warm one held object, as selected
**And** its applicable effect lasts no longer than 10 minutes and deals no direct combat damage in P6.

**Given** a Vessel + Fellowship character has at least 8 Mana and a Minor Wound
**When** they validly cast Steady Vessel on themselves and select one Minor Wound
**Then** the action penalty from that wound is suppressed for 120 seconds
**And** the wound remains present, Health is not restored, and penalties from other wounds remain applicable.

**Given** a valid starting-spell cast commits
**When** its effect begins
**Then** exactly 8 Mana is spent in the same authoritative transaction as the effect and applicable action-clock change
**And** no Stamina is spent unless a separately declared effect requires it.

**Given** the character lacks 8 Mana, does not own the spell, selects an invalid target or effect, exceeds its range, or has no eligible wound for Steady Vessel
**When** the cast is validated
**Then** it is rejected with a specific reason before commitment
**And** Mana, fictional time, world state, and existing effects remain unchanged.

**Given** Hearthspark’s duration ends, its sustained flame is no longer eligible, or Steady Vessel’s 120 seconds expire
**When** the effect is evaluated
**Then** its temporary magical effect or penalty suppression ends according to its fixed contract
**And** it does not erase an underlying wound or create a lasting resource or combat benefit.

**Given** a cast is retried, interrupted, saved, loaded, or resumed across an effect-expiration boundary
**When** its state is recovered
**Then** Mana payment, chosen effect, target, start and expiry times, and any remaining wound penalty restore consistently
**And** neither the cast nor its expiration is applied twice.

**Given** the player casts or inspects a starting spell with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** target, effect choice, cost, validation, and result are displayed
**Then** each has a readable label and clear committed-or-rejected status
**And** no essential spell term is conveyed only by color, hover, or narration.

**Given** Story 8.2 automated evidence
**When** integration and browser tests run
**Then** both starting spells, their exact costs and effects, invalid casts, duration boundaries, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party spell, resource, effect, clock, and persistence behavior is not mocked.

### Story 8.3: Acquire and Inspect the Rest Stone

As a player,
I want to inspect the Rest stone before using it,
So that I understand its rarity, possible spells, and slot requirements before making an irreversible choice.

**Acceptance Criteria:**

**Given** the authorized P6 Rest-stone acquisition occurs
**When** acquisition commits
**Then** one stone is added to the character’s inventory with a stable identity and a rarity rolled once: standard at 80% or resonant at 20%
**And** that rarity is retained rather than rolled again on inspection or use.

**Given** the player inspects an unspent Rest stone after choosing Ember + Fellowship
**When** its possibilities are displayed
**Then** the two candidates are Banked Warmth in an Ember slot and Shared Vigil in a Fellowship slot
**And** each candidate’s cost, target, range, duration or rest requirement, effect, use limit, and rarity-dependent magnitude are stated.

**Given** the player inspects an unspent Rest stone after choosing Vessel + Fellowship
**When** its possibilities are displayed
**Then** the two candidates are Quiet Reservoir in a Vessel slot and Lend Strength in a Fellowship slot
**And** each candidate’s cost, target, range, duration or rest requirement, effect, use limit, and rarity-dependent magnitude are stated.

**Given** either package’s stone is inspected before use
**When** the choice is explained
**Then** the player is told that valid use selects uniformly between its two displayed candidates and permanently awards the selected spell
**And** both candidates’ owning affinities must have a free slot; previewing the choice does not consume the stone.

**Given** the stone has resonant rarity
**When** its candidates are inspected
**Then** Banked Warmth or Quiet Reservoir shows 40% rather than 25% restoration, Shared Vigil shows +2 rather than +1, or Lend Strength shows ally +3 rather than +2 with caster −2 unchanged, as applicable
**And** all other fixed spell terms remain those of the approved candidate.

**Given** a stone is inspected repeatedly, transferred under ordinary ownership rules, saved, loaded, or recovered after interruption
**When** its record is read again
**Then** its identity, ownership, and rolled rarity are unchanged
**And** no additional stone or rarity roll is created.

**Given** an acquisition request is duplicated or an invalid stone record is encountered
**When** validation runs
**Then** the request is rejected or reconciled without granting another P6 stone
**And** no rarity or candidate spell is silently altered.

**Given** stone inspection is used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** rarity, candidates, odds, slot requirements, and irreversible-use terms are displayed
**Then** those terms have readable labels and can be compared without hover-only or color-only information
**And** inspection does not commit a selection or advance fictional time.

**Given** Story 8.3 automated evidence
**When** integration and browser tests run
**Then** both rarity bands, the 80/20 acquisition rule, both packages’ candidate disclosures, retained rarity, duplicate acquisition, and save/load are verified against the real application and SQLite store
**And** the recorded random input reproduces the same acquisition result on mechanical replay without mocking first-party inventory or persistence behavior.

### Story 8.4: Awaken and Use an Ember Rest Spell

As an Ember + Fellowship player,
I want the Rest stone to grant one of my package’s two spells and let me use it,
So that the uncertain discovery produces a reliable, bounded capability.

**Acceptance Criteria:**

**Given** the player owns an unspent Rest stone and both the Ember and Fellowship affinities have a free slot
**When** they confirm its use
**Then** the rules select uniformly between Banked Warmth and Shared Vigil using one recorded random result
**And** the stone is consumed and only the selected spell is permanently placed in a slot owned by its affinity.

**Given** either candidate’s owning affinity has no free slot, the stone is not owned, or the request uses stale state
**When** use is validated
**Then** the request is rejected before selection
**And** the stone, slots, random state, Mana, and fictional time remain unchanged.

**Given** Banked Warmth is awarded from a standard stone
**When** its fixed contract is inspected
**Then** it costs 12 Mana and can target the caster or one target within 5 m, restoring 25% of the target’s Effective Maximum Health, rounded up, after 10 uninterrupted minutes of rest
**And** restoration is limited to once per target per day.

**Given** Banked Warmth is awarded from a resonant stone
**When** its fixed contract is inspected or used
**Then** its restoration is 40% of Effective Maximum Health, rounded up
**And** its cost, target range, rest requirement, and once-per-target-per-day limit are unchanged.

**Given** a valid Banked Warmth cast commits
**When** the target completes the required uninterrupted rest
**Then** the applicable Health is restored, capped at the target’s Effective Maximum
**And** an interrupted rest grants no restoration.

**Given** Shared Vigil is awarded from a standard stone
**When** it is validly cast on one willing ally within 10 m
**Then** 10 Mana is spent and, for up to 120 seconds, caster and ally each gain +1 to Perception and Insight while they remain within 10 m of each other
**And** the bonuses do not apply while that distance condition is unmet.

**Given** Shared Vigil is awarded from a resonant stone
**When** it is validly cast
**Then** the corresponding Perception and Insight bonuses are +2
**And** the 10-Mana cost, willing-ally target, 10 m range condition, and 120-second duration remain unchanged.

**Given** either awarded spell is cast with insufficient Mana, an invalid target, or an unmet prerequisite
**When** validation runs
**Then** the cast is rejected with a specific reason and no spell effect is created
**And** Mana and fictional time are unchanged.

**Given** an awakened spell is inspected, cast, retried, saved, or loaded
**When** its state is recovered
**Then** its stable mechanical identity, rarity-specific magnitude, owning slot, Mana payment, targets, durations, and use limits remain consistent
**And** awakening or casting cannot duplicate the spell, consume a second stone, or apply an effect twice.

**Given** the player reviews or uses the stone and spell with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the result, slot, cost, target, effect, remaining duration, or rejection is displayed
**Then** each has a readable label and clear committed-or-rejected status
**And** the outcome does not depend on color-only or hover-only information.

**Given** Story 8.4 automated evidence
**When** integration and browser tests run
**Then** both Ember results, both rarity bands, the uniform selection rule, both-slot precondition, permanent award, spell effects, interruptions, daily limit, invalid casts, idempotency, and save/load are verified against the real application and SQLite store
**And** recorded random inputs reproduce the same awakening result without mocking first-party rules or persistence behavior.

### Story 8.5: Awaken and Use a Vessel Rest Spell

As a Vessel + Fellowship player,
I want the Rest stone to grant one of my package’s two spells and let me use it,
So that the uncertain discovery produces a reliable, bounded capability.

**Acceptance Criteria:**

**Given** the player owns an unspent Rest stone and both the Vessel and Fellowship affinities have a free slot
**When** they confirm its use
**Then** the rules select uniformly between Quiet Reservoir and Lend Strength using one recorded random result
**And** the stone is consumed and only the selected spell is permanently placed in a slot owned by its affinity.

**Given** either candidate’s owning affinity has no free slot, the stone is not owned, or the request uses stale state
**When** use is validated
**Then** the request is rejected before selection
**And** the stone, slots, random state, Mana, and fictional time remain unchanged.

**Given** Quiet Reservoir is awarded from a standard stone
**When** its fixed contract is inspected
**Then** it costs 12 Mana, targets the caster, and restores 25% of the caster’s Effective Maximum Mana, rounded up, after 10 uninterrupted minutes of rest
**And** restoration is limited to once per day.

**Given** Quiet Reservoir is awarded from a resonant stone
**When** its fixed contract is inspected or used
**Then** its restoration is 40% of Effective Maximum Mana, rounded up
**And** its cost, self-only target, rest requirement, and once-per-day limit are unchanged.

**Given** a valid Quiet Reservoir cast commits
**When** the caster completes the required uninterrupted rest
**Then** the applicable Mana is restored, capped at the caster’s Effective Maximum
**And** an interrupted rest grants no restoration and does not refund the committed casting cost.

**Given** Lend Strength is awarded from a standard stone
**When** it is validly cast on one willing ally within 5 m
**Then** 12 Mana is spent and, for 120 seconds, the ally gains +2 on Body-based checks while the caster takes −2 on Body-based checks
**And** both modifiers expire together without changing either character’s raw Body score.

**Given** Lend Strength is awarded from a resonant stone
**When** it is validly cast
**Then** the ally’s Body-check bonus is +3 while the caster’s penalty remains −2
**And** the 12-Mana cost, willing-ally target, 5 m casting range, and 120-second duration remain unchanged.

**Given** either awarded spell is cast with insufficient Mana, an invalid target, an exhausted daily use, or another unmet prerequisite
**When** validation runs
**Then** the cast is rejected with a specific reason and no spell effect is created
**And** Mana and fictional time are unchanged.

**Given** an awakened spell is inspected, cast, retried, saved, or loaded
**When** its state is recovered
**Then** its stable mechanical identity, rarity-specific magnitude, owning slot, Mana payment, targets, durations, and use limits remain consistent
**And** awakening or casting cannot duplicate the spell, consume a second stone, restore Mana twice, or apply duplicate modifiers.

**Given** the player reviews or uses the stone and spell with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the result, slot, cost, target, effect, remaining duration, daily use, or rejection is displayed
**Then** each has a readable label and clear committed-or-rejected status
**And** the outcome does not depend on color-only or hover-only information.

**Given** Story 8.5 automated evidence
**When** integration and browser tests run
**Then** both Vessel results, both rarity bands, the uniform selection rule, both-slot precondition, permanent award, spell effects, interrupted rest, daily limit, invalid casts, idempotency, and save/load are verified against the real application and SQLite store
**And** recorded random inputs reproduce the same awakening result without mocking first-party rules or persistence behavior.

### Story 8.6: Give the Awakened Spell a History-Shaped Identity

As a player,
I want my awakened Rest spell’s presentation to reflect my character and history,
So that the spell feels personal while its rules remain dependable.

**Acceptance Criteria:**

**Given** the Rest stone selects a fixed spell result
**When** player-facing presentation is generated
**Then** the generation context may include the Rest concept, owning affinity, complete affinity set, Session 0 character concept, and committed character history
**And** it excludes uncommitted proposals, private NPC knowledge, and facts unavailable to the player.

**Given** presentation generation succeeds
**When** its output is validated
**Then** the awarded spell receives a player-facing name and exactly one sentence describing its manifestation
**And** both are stored separately from the stable mechanical definition and spell-instance identity.

**Given** a generated name or manifestation claims a different cost, owner, slot, target, range, duration, magnitude, limit, or effect
**When** validation compares it with the selected fixed definition
**Then** the conflicting presentation is rejected or replaced with safe bounded presentation
**And** the selected spell and all of its mechanics remain unchanged.

**Given** generated presentation is malformed, unsafe, unavailable, or times out
**When** the mechanical awakening has already committed
**Then** the awarded spell remains valid and usable through neutral fallback presentation or recoverable presentation generation
**And** the stone, random selection, spell award, and slot occupancy are not repeated or rolled back.

**Given** two characters receive the same fixed Rest-spell definition
**When** their generated presentations differ based on permitted character context
**Then** each may retain a distinct player-facing name and manifestation
**And** both spells still resolve from the same versioned mechanical definition.

**Given** the player inspects or casts an awakened spell
**When** its personalized presentation is shown
**Then** the generated name and manifestation accompany the authoritative cost, targeting, duration, limits, rarity effect, and owning slot
**And** flavor text cannot override or obscure those mechanical terms.

**Given** the spell is cast repeatedly, evolved later, transferred through a supported future operation, saved, loaded, replayed, or recovered after interruption
**When** its record is read
**Then** its committed player-facing name, manifestation, instance identity, and mechanical-definition reference remain stable
**And** narration does not silently rename the spell or mutate its mechanics.

**Given** spell presentation is inspected with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** personalized and mechanical details are displayed
**Then** the generated name and manifestation are distinguishable from the authoritative spell terms with readable labels
**And** the distinction requires no color-only, hover-only, or narration-only cue.

**Given** Story 8.6 automated evidence
**When** integration and browser tests run
**Then** all four fixed Rest-spell results, permitted context inputs, stable personalized presentation, invalid-generation recovery, mechanical isolation, and save/load are verified against the real application and SQLite store
**And** tests prove that generated output cannot alter the selected definition, rarity, slot ownership, or spell effect.

### Story 8.7: Earn the Brackenford’s Anchor Title

As a player,
I want Brackenford’s lasting stability to be recognized with a useful title,
So that the community outcome remains part of my character’s identity.

**Acceptance Criteria:**

**Given** a P6 character’s committed history proves that all four households completed G01’s three consecutive qualifying days
**When** recognition is evaluated
**Then** the character is awarded the nonstacking title Brackenford’s Anchor exactly once
**And** the award references the committed community-victory event rather than a quest flag or narrated claim.

**Given** G01 has not been completed or its evidence is incomplete
**When** recognition is evaluated
**Then** Brackenford’s Anchor is not awarded
**And** no household streak, resource, agreement, or historical result is changed to make the character eligible.

**Given** Brackenford’s Anchor was earned before P6 recognition records existed
**When** an eligible P5 branch is upgraded and its committed G01 evidence is reconciled
**Then** the title is awarded without replaying the victory or its rewards
**And** repeated migration or reconciliation cannot create a duplicate title.

**Given** the player has not used the title’s daily benefit
**When** they apply Brackenford’s Anchor to an eligible Persuasion check
**Then** that check receives exactly +1 before the roll
**And** the title’s benefit is marked used for the current simulated day whether the check succeeds or fails.

**Given** the title’s benefit has already been used during the current simulated day
**When** the player attempts to apply it again
**Then** no additional title bonus is added
**And** the check can proceed using its other applicable modifiers.

**Given** a new simulated day begins
**When** the title’s benefit state is evaluated
**Then** one use becomes available for that day
**And** skipped uses do not accumulate across days.

**Given** Brackenford’s Anchor is combined with other valid Persuasion modifiers
**When** the check is calculated
**Then** its single +1 is included as a separately identified source
**And** duplicate title records, retries, or narration cannot stack the title with itself.

**Given** the title is awarded or its daily benefit is used
**When** recognition records are inspected
**Then** the title, its G01 award source, and its daily-use state are stored independently of achievements, item prizes, spell instances, and spell-evolution records
**And** earning or using the title does not grant the Copper Sandglass or advance a Rest spell.

**Given** title award or benefit use is retried, interrupted, saved, or loaded
**When** state is recovered
**Then** title ownership, award provenance, simulated-day identity, and daily-use state restore consistently
**And** neither the award nor the +1 benefit can be applied twice.

**Given** the title is inspected or applied with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** its source, benefit, availability, or use result is displayed
**Then** each has a readable label and clear status
**And** availability is not conveyed only by color, hover, or narration.

**Given** Story 8.7 automated evidence
**When** integration and browser tests run
**Then** qualifying and nonqualifying G01 histories, migration reconciliation, exact-once award, daily Persuasion use, nonstacking, day rollover, record separation, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party recognition, check, clock, and persistence behavior is not mocked.

### Story 8.8: Record Consequential Rest-Spell Practice

As a player,
I want meaningful uses of my awakened Rest spell to leave reliable advancement evidence,
So that the spell can deepen through consequential play rather than empty repetition.

**Acceptance Criteria:**

**Given** the player uses their awarded Rest spell
**When** the resulting events commit
**Then** a use qualifies as consequential only when committed evidence links the spell’s actual effect to a material recovery, action, check, or resolved outcome
**And** casting the spell without an eligible effect or merely claiming that it mattered does not qualify.

**Given** a Rest-spell use qualifies as consequential
**When** its advancement evidence is recorded
**Then** the record identifies the spell instance and fixed definition, cast event, affected characters or effects, relevant resolved situation, committed consequence, and world revision
**And** generated narration cannot create or alter that evidence.

**Given** two qualifying uses arise from genuinely different resolved situations
**When** distinctness is evaluated
**Then** each can contribute one consequential-use record
**And** distinctness is based on authoritative event and consequence identities rather than different wording.

**Given** a request retries the same cast or repeats an identical already-resolved situation without a new consequence
**When** advancement evidence is evaluated
**Then** it contributes at most one qualifying use
**And** narration, reloads, or alternate descriptions cannot manufacture additional progress.

**Given** the first qualifying consequential use is recorded
**When** the result is presented
**Then** the player is shown exactly `Rest deepens when recovery protects a promise.`
**And** the clue is recorded as discovered without exposing the number of required uses, an advancement checklist, or the hidden achievement trigger.

**Given** the first-use event or clue presentation is retried or interrupted
**When** recovery runs
**Then** the consequential-use record and clue-discovery state each commit at most once
**And** a presentation failure cannot remove valid practice evidence or duplicate the underlying use.

**Given** a second or third distinct consequential use is recorded
**When** the player reviews the spell or its known clues
**Then** no progress counter, checklist, unrevealed prerequisite, or premature Deepened choice is exposed
**And** the exact first-use clue remains available without being announced as newly discovered again.

**Given** consequential-use evidence is saved, loaded, or mechanically replayed
**When** its state is recovered
**Then** qualifying records, causal references, distinctness decisions, and clue-discovery state remain consistent
**And** the same recorded inputs produce the same advancement evidence even if prose differs.

**Given** the clue or known spell history is inspected with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** its text and discovery status are displayed
**Then** they have readable labels and sensible focus and reading order
**And** no advancement meaning depends only on color, hover, or animation.

**Given** Story 8.8 automated evidence
**When** integration and browser tests run
**Then** qualifying and nonqualifying uses of all four Rest spells, distinct and repeated situations, the exact first-use clue, hidden progress, idempotency, replay, and save/load are verified against the real application and SQLite store
**And** first-party spell, event, progression, presentation, and persistence behavior is not mocked.

### Story 8.9: Earn the Rest Achievement and Copper Sandglass

As a player,
I want recovery that protects an accepted promise to receive lasting recognition,
So that a meaningful Rest-spell success earns a distinct achievement and useful prize.

**Acceptance Criteria:**

**Given** the player completes a timed, accepted commitment
**When** committed causal evidence shows that their awarded Rest spell materially enabled recovery during that attempt
**Then** the fixed internal achievement Rest Is Part of the Work is awarded exactly once
**And** the record references the accepted commitment, qualifying spell effect, recovery, and completion events.

**Given** a commitment was only proposed, was untimed, failed, expired, or was abandoned, or the Rest spell did not materially enable recovery during its attempt
**When** achievement eligibility is evaluated
**Then** the achievement is not awarded
**And** narration or player assertion cannot substitute for missing committed evidence.

**Given** the fixed achievement trigger is satisfied
**When** its player-facing presentation is generated
**Then** it receives a two-to-six-word name and one sentence tied only to the committed qualifying event
**And** the generated presentation is stored separately from the fixed internal identity and trigger evidence.

**Given** generated achievement presentation invents facts, uses unrelated history, violates its length or sentence limits, is unavailable, or times out
**When** validation or recovery runs
**Then** invalid output is rejected or replaced with neutral bounded presentation
**And** the achievement and its qualifying evidence remain intact without being awarded again.

**Given** the achievement is awarded
**When** its reward transaction commits
**Then** one Copper Sandglass with a stable identity and value of 5 gold is added to the player’s inventory
**And** the achievement record and item-prize record remain distinct from each other, Brackenford’s Anchor, and every spell-evolution record.

**Given** the player owns the Copper Sandglass and has not used it during the current simulated day
**When** they use it on one known active effect
**Then** it reveals that effect’s exact authoritative remaining time
**And** no hidden source, unrevealed effect, or unrelated private state is disclosed.

**Given** the player owns the Copper Sandglass and has not used it during the current simulated day
**When** they use it on one known active commitment
**Then** it reveals that commitment’s exact authoritative remaining time
**And** no hidden requirement, NPC plan, or fact beyond the known commitment is disclosed.

**Given** the target is unknown, unsupported, or no longer active, the player does not own the Sandglass, or its daily use is already spent
**When** use is validated
**Then** the request is rejected with a specific reason and no time is revealed
**And** no unrelated state or additional daily use is changed.

**Given** the Sandglass’s daily use has been spent
**When** a new simulated day begins
**Then** one use becomes available for the new day
**And** unused activations do not accumulate across days.

**Given** the Copper Sandglass is sold, transferred, consumed by a future supported effect, or otherwise lost
**When** the player’s recognition is inspected
**Then** Rest Is Part of the Work and its qualifying evidence remain recorded
**And** item ownership is not treated as achievement ownership or a prerequisite for retaining the achievement.

**Given** achievement award, prize delivery, or Sandglass use is retried, interrupted, saved, or loaded
**When** recovery runs
**Then** trigger evidence, presentation, achievement identity, item identity and ownership, daily-use state, and revealed result restore consistently
**And** neither the achievement, item, nor daily activation is duplicated.

**Given** the achievement or Sandglass is inspected or used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the trigger summary, presentation, prize, value, target, remaining time, or availability is displayed
**Then** each has a readable label and clear status
**And** no essential distinction or result depends only on color, hover, or animation.

**Given** Story 8.9 automated evidence
**When** integration and browser tests run
**Then** qualifying and nonqualifying commitments, generated presentation boundaries, exact-once award, separate prize delivery, both supported Sandglass targets, knowledge filtering, daily use, sale or loss, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party commitment, spell, recognition, inventory, clock, and persistence behavior is not mocked.

### Story 8.10: Choose and Use an Ember Deepened Spell

As an Ember + Fellowship player,
I want to review and explicitly choose my Rest spell’s Deepened form,
So that earned growth offers a clear tradeoff without changing my spell unexpectedly.

**Acceptance Criteria:**

**Given** the Ember Rest spell has fewer than three distinct consequential-use records or Rest Is Part of the Work has not been earned
**When** evolution eligibility is evaluated
**Then** no Deepened mechanics or replacement choice are revealed
**And** the first-use clue remains the only permitted advancement guidance.

**Given** the Ember Rest spell has three distinct consequential-use records and Rest Is Part of the Work is recorded
**When** evolution eligibility commits
**Then** the exact Deepened variant, Mana cost, changed benefit, tradeoff, and same-slot replacement consequence are revealed
**And** the player receives an explicit confirm-or-decline choice rather than an automatic replacement.

**Given** the player has eligible Banked Warmth
**When** its Deepened choice is displayed
**Then** it states that the spell will cost 16 Mana, restore 50% of Effective Maximum Health after 10 uninterrupted minutes of rest, and become self-only
**And** its rounding, once-per-day self limit, interruption behavior, and other unchanged terms are stated.

**Given** the player has eligible Shared Vigil
**When** its Deepened choice is displayed
**Then** it states that the spell will cost 14 Mana, last 240 seconds, and benefit Perception but no longer Insight
**And** its existing rarity-specific bonus, willing-ally targeting, 10 m casting range, and continuing proximity requirement remain unchanged.

**Given** the player previews or declines either Deepened variant
**When** the choice closes
**Then** the original spell remains unchanged and usable in its existing slot
**And** no Mana, fictional time, item, recognition, or evolution record is spent or created.

**Given** the player explicitly confirms the displayed Deepened variant against the current world revision
**When** replacement commits
**Then** the Deepened definition replaces the original spell in the same affinity-owned slot and an evolution record links both definitions to the confirmed choice
**And** the original version is no longer castable from that slot.

**Given** narration implies acceptance, the request lacks explicit confirmation, eligibility evidence is missing, or the world revision or offered definition is stale
**When** replacement is validated
**Then** the request is rejected with a specific reason
**And** the original spell, slot, Mana, history, and evolution state remain unchanged.

**Given** Deepened Banked Warmth is validly cast with at least 16 Mana
**When** its uninterrupted rest completes
**Then** it restores 50% of the caster’s Effective Maximum Health, rounded up and capped at that maximum
**And** interruption grants no restoration or refund of its committed Mana cost.

**Given** Deepened Shared Vigil is validly cast with at least 14 Mana on one willing ally within 10 m
**When** its effect commits
**Then** caster and ally receive the spell’s rarity-specific Perception bonus for up to 240 seconds while within 10 m of each other
**And** neither character receives an Insight bonus from the Deepened spell.

**Given** a Deepened cast lacks Mana, has an invalid target, exceeds range, violates its daily limit, or otherwise fails validation
**When** casting is attempted
**Then** no effect, Mana cost, or fictional time is committed
**And** the Deepened spell remains unchanged.

**Given** the offer, decline, confirmation, replacement, or Deepened cast is retried, interrupted, saved, or loaded
**When** recovery runs
**Then** eligibility evidence, choice state, slot ownership, active definition, Mana payment, effects, limits, and evolution provenance restore consistently
**And** neither the replacement nor any cast is applied twice.

**Given** the Deepened offer or spell is inspected and used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** prerequisites, original and replacement terms, tradeoffs, confirmation, or results are displayed
**Then** each has a readable label and clear status
**And** no acceptance or essential comparison depends only on color, hover, animation, or narration.

**Given** Story 8.10 automated evidence
**When** integration and browser tests run
**Then** both Ember evolutions, prerequisite orderings, exact reveal boundaries, decline, explicit confirmation, same-slot replacement, both rarity bands, evolved casts, invalid requests, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party progression, spell, effect, transaction, and persistence behavior is not mocked.

### Story 8.11: Choose and Use a Vessel Deepened Spell

As a Vessel + Fellowship player,
I want to review and explicitly choose my Rest spell’s Deepened form,
So that earned growth offers a clear tradeoff without changing my spell unexpectedly.

**Acceptance Criteria:**

**Given** the Vessel Rest spell has fewer than three distinct consequential-use records or Rest Is Part of the Work has not been earned
**When** evolution eligibility is evaluated
**Then** no Deepened mechanics or replacement choice are revealed
**And** the first-use clue remains the only permitted advancement guidance.

**Given** the Vessel Rest spell has three distinct consequential-use records and Rest Is Part of the Work is recorded
**When** evolution eligibility commits
**Then** the exact Deepened variant, Mana cost, changed benefit, tradeoff, and same-slot replacement consequence are revealed
**And** the player receives an explicit confirm-or-decline choice rather than an automatic replacement.

**Given** the player has eligible Quiet Reservoir
**When** its Deepened choice is displayed
**Then** it states that the spell will cost 16 Mana and restore 50% of Effective Maximum Mana after 10 uninterrupted minutes of rest
**And** its self-only target, rounding, once-per-day limit, interruption behavior, and other unchanged terms are stated.

**Given** the player has eligible Lend Strength
**When** its Deepened choice is displayed
**Then** it states that the spell will cost 16 Mana, grant the willing ally +4 on Body-based checks, and impose −3 on the caster’s Body-based checks for 120 seconds
**And** its 5 m casting range and other unchanged terms are stated.

**Given** either Vessel Deepened choice is displayed for a standard or resonant original spell
**When** its changed magnitude is compared
**Then** Quiet Reservoir’s 50% restoration or Lend Strength’s +4/−3 modifiers replace the original rarity-dependent values
**And** no unlisted rarity bonus is added to the Deepened definition.

**Given** the player previews or declines either Deepened variant
**When** the choice closes
**Then** the original spell remains unchanged and usable in its existing slot
**And** no Mana, fictional time, item, recognition, or evolution record is spent or created.

**Given** the player explicitly confirms the displayed Deepened variant against the current world revision
**When** replacement commits
**Then** the Deepened definition replaces the original spell in the same affinity-owned slot and an evolution record links both definitions to the confirmed choice
**And** the original version is no longer castable from that slot.

**Given** narration implies acceptance, the request lacks explicit confirmation, eligibility evidence is missing, or the world revision or offered definition is stale
**When** replacement is validated
**Then** the request is rejected with a specific reason
**And** the original spell, slot, Mana, history, and evolution state remain unchanged.

**Given** Deepened Quiet Reservoir is validly cast with at least 16 Mana
**When** its uninterrupted rest completes
**Then** it restores 50% of the caster’s Effective Maximum Mana, rounded up and capped at that maximum
**And** interruption grants no restoration or refund of its committed casting cost.

**Given** Deepened Lend Strength is validly cast with at least 16 Mana on one willing ally within 5 m
**When** its effect commits
**Then** the ally receives +4 and the caster receives −3 on Body-based checks for 120 seconds
**And** neither modifier changes a raw Body score or persists after expiration.

**Given** a Deepened cast lacks Mana, has an invalid target, exceeds range, violates its daily limit, or otherwise fails validation
**When** casting is attempted
**Then** no effect, Mana cost, or fictional time is committed
**And** the Deepened spell remains unchanged.

**Given** the offer, decline, confirmation, replacement, or Deepened cast is retried, interrupted, saved, or loaded
**When** recovery runs
**Then** eligibility evidence, choice state, slot ownership, active definition, Mana payment, effects, limits, and evolution provenance restore consistently
**And** neither the replacement nor any cast is applied twice.

**Given** the Deepened offer or spell is inspected and used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** prerequisites, original and replacement terms, tradeoffs, confirmation, or results are displayed
**Then** each has a readable label and clear status
**And** no acceptance or essential comparison depends only on color, hover, animation, or narration.

**Given** Story 8.11 automated evidence
**When** integration and browser tests run
**Then** both Vessel evolutions, prerequisite orderings, exact reveal boundaries, decline, explicit confirmation, same-slot replacement, both rarity bands, evolved casts, invalid requests, idempotency, and save/load are verified against the real application and SQLite store
**And** first-party progression, spell, effect, transaction, and persistence behavior is not mocked.

### Story 8.12: Verify the P6 Spells and Recognition Gate

As a playtester,
I want to exercise the complete P6 affinity, awakening, recognition, and evolution loop,
So that later quest systems build on magic and rewards that remain bounded, causal, and persistent.

**Acceptance Criteria:**

**Given** an authorized P6 build, its phase-specific UX contract, and controlled starting states
**When** P6 content and stage boundaries are validated
**Then** exactly the two approved affinity packages, their skill bonuses, starting spells, affinity-owned slots, four Rest-spell candidates, two rarity bands, recognition records, and four Deepened definitions are available
**And** P7 daily quests, hidden quest bonuses, combat content, and later affinity-discovery systems remain absent.

**Given** independent Ember + Fellowship and Vessel + Fellowship fixture branches
**When** package selection and starting-spell use are completed
**Then** each branch receives the correct +1 skill source, four affinity-owned slots, starting spell, fixed contract, and Mana-at-commitment behavior
**And** migration, selection retries, or save/load create no duplicate package, bonus, slot, spell, or resource payment.

**Given** controlled random inputs on both package branches
**When** Rest stones are acquired and awakened across the standard and resonant rarity boundaries
**Then** the 80/20 acquisition rule, retained rarity, both disclosed candidates, uniform candidate selection, both-affinity capacity check, valid-use consumption, and permanent same-owner slot award are demonstrated
**And** invalid use leaves the stone, slots, random state, Mana, and fictional time unchanged.

**Given** Banked Warmth, Shared Vigil, Quiet Reservoir, and Lend Strength in both applicable rarity bands
**When** every spell is inspected and exercised through valid and invalid uses
**Then** costs, targets, ranges, durations or rest intervals, magnitudes, proximity rules, daily limits, interruption behavior, modifiers, and pool caps match their approved definitions
**And** no narration, rarity roll, or generated presentation changes those mechanics.

**Given** controlled characters with different Session 0 concepts and committed histories
**When** player-facing Rest-spell names and manifestations are generated
**Then** permitted concept, affinity, and history inputs can shape the name and one-sentence manifestation while the selected mechanical identity remains fixed
**And** committed presentation remains stable across casting, retries, save/load, and replay.

**Given** qualifying and nonqualifying G01 histories and accepted timed commitments
**When** recognition is evaluated
**Then** Brackenford’s Anchor is awarded only from G01 completion, Rest Is Part of the Work only from its fixed recovery-and-commitment trigger, and the Copper Sandglass only as that achievement’s separate prize
**And** title, achievement, prize, spell instance, and evolution records retain distinct identities and provenance.

**Given** the Copper Sandglass is exercised against known effects and commitments
**When** daily use, day rollover, sale or loss, retries, and knowledge boundaries are tested
**Then** it reveals only the exact remaining time on one eligible known target per day and retains its 5-gold item value
**And** loss of the item does not erase the achievement or create another prize.

**Given** each of the four Rest spells receives qualifying and repeated practice
**When** advancement evidence is evaluated
**Then** only three distinct consequential uses count, the exact first-use clue is shown without a checklist, and duplicate situations create no additional progress
**And** no Deepened terms are revealed until both the three-use condition and Rest Is Part of the Work are recorded.

**Given** each Rest spell becomes eligible for its Deepened form
**When** decline and explicit-confirmation branches are exercised
**Then** declining preserves the original, while confirmation installs the exact approved Deepened definition in the same slot with its stated cost and tradeoff
**And** no title, item, narration, or implicit response can replace the spell automatically.

**Given** one failure or interruption is introduced during acquisition, awakening, presentation generation, recognition, prize delivery, evolution, and spell resolution
**When** recovery and safe retry are exercised
**Then** every committed boundary is identifiable and unfinished work can resume without rerolling or duplicating authoritative state
**And** no stone, spell, slot, Mana payment, effect, title, achievement, item, practice record, or evolution is lost or applied twice.

**Given** the same captured state, content versions, structured proposals, and recorded random inputs
**When** mechanical replay is run
**Then** package, rarity, awakening, costs, effects, recognition, advancement, and state hashes reproduce exactly
**And** newly generated prose may differ only before presentation is committed and can never alter mechanics.

**Given** one unplanned but supported use of P6 magic
**When** its intent is validated and resolved
**Then** it composes with existing places, access, resources, effects, needs, commitments, and time through ordinary authoritative rules
**And** unsupported portions receive factual limits rather than invented capabilities or success.

**Given** P6 player journeys are tested with keyboard, pointer, screen reader, 200% zoom, and 320-pixel reflow
**When** package comparison, spell inspection and targeting, stone disclosure, generated presentation, recognition, Sandglass use, clues, and Deepened confirmation are exercised
**Then** costs, ownership, odds, prerequisites, tradeoffs, validation, and committed status remain readable and operable
**And** no essential information or action depends only on color, hover, animation, horizontal scrolling, or narration.

**Given** P6 playtest sessions
**When** feedback is recorded
**Then** evidence separately captures what changed, why the magic or recognition felt earned, what felt unfair or unclear, and what the player wants next
**And** mechanical correctness is not treated as proof that affinity identity or advancement felt meaningful.

**Given** an unexplained mechanical contradiction, unauthorized generated change, knowledge leak, duplicate reward, incorrect rarity or slot result, premature reveal, implicit evolution, conservation error, or save/load failure
**When** the P6 gate is evaluated
**Then** the affected scenario fails and is corrected and repeated
**And** P7 remains unauthorized.

**Given** all P6 evidence passes
**When** Epic 8 closes
**Then** P6 is marked eligible for a separate P7 authorization decision
**And** daily System quests, hidden bonuses, and combat remain unavailable until their stages are explicitly authorized.

## Epic 9: Complete Daily Quests for Explicit Rewards

Players can receive three explicit System-assigned daily quests, complete them for one-time XP and item draws, and understand every objective and reward without compromising free play.

### Story 9.1: Receive Three Daily System Quests

As a player,
I want to receive three clearly defined daily quests,
So that I can decide whether to pursue explicit objectives without surrendering control of my day.

**Acceptance Criteria:**

**Given** the P6 evidence gate has not passed, P7 has not been separately authorized, or no P7-specific UX contract is approved
**When** a P7 upgrade is requested
**Then** daily quests, gacha draws, and P7 System notices remain unavailable
**And** the existing P6 branch remains unchanged.

**Given** an eligible P6 branch is upgraded to P7
**When** migration runs
**Then** it validates the immediately preceding ruleset and content versions and records the P7 stage and daily-refresh schedule atomically
**And** existing character, world, inventory, progression, spell, recognition, commitment, and clock state is preserved.

**Given** an authorized P7 branch reaches a scheduled 06:00 assignment boundary with eligible quest inputs
**When** the daily set commits
**Then** exactly three versioned quest instances occupy the three System slots: one crafting, one social, and one observation quest
**And** no combat quest, hidden bonus condition, preference weighting, streak, or multiplier is created.

**Given** the crafting quest is assigned
**When** its success contract is displayed
**Then** it identifies one named recipe already known by the player and requires production of one resulting item after assignment
**And** it states the named relevant skill, evaluating authority, next-06:00 expiry, 25 player XP, 25 relevant-skill XP, and one gacha draw.

**Given** the social quest is assigned
**When** its success contract is displayed
**Then** it identifies one currently accepted NPC commitment and requires actual fulfillment after assignment
**And** it states the named relevant skill, evaluating authority, next-06:00 expiry, 25 player XP, 25 relevant-skill XP, and one gacha draw.

**Given** the observation quest is assigned
**When** its success contract is displayed
**Then** it identifies one named location and the specific previously unknown condition the player must investigate and record after visiting
**And** it states the named relevant skill, evaluating authority, next-06:00 expiry, 25 player XP, 25 relevant-skill XP, and one gacha draw without revealing the undiscovered result.

**Given** any daily quest is inspected from assignment onward
**When** the player opens the journal
**Then** its System issuer, category, explicit success contract, named relevant skill, reward, assignment time, expiry time, and current G10 lifecycle state are visible
**And** it appears in a distinct System category without concealing any required success condition.

**Given** a proposed daily set references an unknown recipe, an unaccepted or resolved commitment, a condition already known at assignment, an invalid location, or an unsupported category
**When** the set is validated
**Then** the invalid proposal is rejected before any quest becomes visible
**And** no partial set, fictional fact, hidden objective, or reward entitlement is committed.

**Given** assignment fails before commit or presentation fails after commit
**When** recovery is offered
**Then** an uncommitted set can be safely retried while a committed set can be redisplayed from authoritative state
**And** the 06:00 clock event, quest instances, and assignments are not duplicated.

**Given** a daily-set operation is retried, interrupted, saved, loaded, or mechanically replayed
**When** its state is recovered
**Then** the same three quest identities, categories, contracts, skill names, rewards, assignment and expiry times, and content versions restore
**And** no slot is omitted, replaced independently, or assigned twice.

**Given** the daily journal is used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the player compares and inspects all three quests
**Then** issuer, category, conditions, skill, reward, state, and expiry have readable labels and sensible focus and reading order
**And** no objective depends on color-only, hover-only, animation-only, or horizontally scrolling presentation.

**Given** Story 9.1 automated evidence
**When** integration and browser tests run
**Then** P7 gating, adjacent-version migration, the exact three categories, explicit contracts, eligible-input validation, P8 and combat exclusion, atomic assignment, recovery, idempotency, replay, and save/load are verified against the real application and SQLite store
**And** first-party migration, scheduler, quest, journal, and persistence behavior is not mocked.

### Story 9.2: Complete a Crafting Daily Quest

As a player,
I want producing the daily quest’s named recipe to grant its stated reward,
So that completing a concrete crafting objective advances the promised tracks exactly once.

**Acceptance Criteria:**

**Given** an active, unexpired crafting daily quest
**When** the player inspects it
**Then** the named known recipe, qualifying output, relevant Alchemy or Brewing skill, expiry, and full reward are visible
**And** the success contract cannot change after assignment.

**Given** the player produces the named recipe after the quest’s assignment and before its expiry
**When** the valid crafting result commits
**Then** the resulting item is created under the ordinary crafting rules and the quest is fulfilled from that committed evidence
**And** declaration, narration, or possession of a copy produced before assignment cannot satisfy the quest.

**Given** the crafting quest is fulfilled for the first time
**When** its completion transaction commits
**Then** the quest enters its completed state, exactly 25 XP is added to the player track, exactly 25 XP is added to the quest’s named relevant-skill track, and exactly one gacha-draw entitlement is created
**And** the completion, XP awards, draw entitlement, reward claims, and notification commit atomically.

**Given** the quest XP crosses one or more existing progression thresholds
**When** the fixed rewards are applied
**Then** normal level advancement, carried excess XP, and any resulting unspent attribute points are processed under the existing progression rules
**And** each 25-XP quest award remains a separately identified source from any ordinary crafting-check XP.

**Given** the player gathers ingredients, begins but does not finish the craft, produces another recipe, or fails an uncertain attempt at the named recipe
**When** quest progress is evaluated
**Then** the quest remains incomplete and grants no quest XP or draw
**And** the underlying crafting action retains its normal committed costs, elapsed time, failure result, and any independently earned check XP.

**Given** the named recipe is successfully produced after the quest expires
**When** the craft commits
**Then** the ordinary item and crafting consequences still occur
**And** the expired quest grants no XP, draw, penalty, or retroactive completion.

**Given** the qualifying crafted item is later consumed, transferred, sold, or lost
**When** the quest record is inspected
**Then** its completed state and earned rewards remain intact
**And** later ownership changes neither revoke nor duplicate the completion.

**Given** the player produces the named recipe again or retries completion after the quest has resolved
**When** reward evaluation runs
**Then** no additional daily-quest XP or draw is granted
**And** the new crafting action remains valid under ordinary crafting rules.

**Given** completion fails before atomic commit or reward presentation fails after commit
**When** recovery runs
**Then** either no quest reward component committed or the complete authoritative reward can be redisplayed
**And** retrying cannot duplicate the item output, completion, either XP award, draw entitlement, or notification.

**Given** the craft, completion, or reward operation is interrupted, retried, saved, loaded, or replayed
**When** state is recovered
**Then** the quest identity and state, craft evidence, item output, XP sources, progression results, draw entitlement, and reward claims remain consistent
**And** the same committed action cannot satisfy more than one claim for that quest.

**Given** the crafting daily quest and its completion are used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** requirements, progress, expiry, result, and reward are displayed
**Then** each has a readable label and clear pending, completed, expired, or rejected status
**And** no essential information depends only on color, hover, animation, or horizontal scrolling.

**Given** Story 9.2 automated evidence
**When** integration and browser tests run
**Then** Alchemy and Brewing quest variants, qualifying and nonqualifying crafts, failed attempts, expiry, exact XP, level crossings, one draw entitlement, atomic rewards, duplicate claims, recovery, replay, and save/load are verified against the real application and SQLite store
**And** first-party crafting, quest, progression, reward, inventory, and persistence behavior is not mocked.

### Story 9.3: Complete a Social Daily Quest

As a player,
I want fulfilling the daily quest’s accepted NPC commitment to grant its stated reward,
So that the System recognizes completed promises rather than persuasive claims.

**Acceptance Criteria:**

**Given** an active, unexpired social daily quest
**When** the player inspects it
**Then** the referenced accepted commitment, required outcome, involved parties, evaluating authority, named relevant social skill, expiry, and full reward are visible
**And** the named skill is Deception, Intimidation, Performance, or Persuasion and the success contract cannot change after assignment.

**Given** the player actually fulfills the referenced commitment after the quest’s assignment and before its expiry
**When** the commitment’s required outcome commits
**Then** the commitment enters its fulfilled state and the daily quest is completed from the same authoritative evidence
**And** a successful conversation, stated intention, unrelated favor, or narration alone cannot satisfy it.

**Given** the social quest is fulfilled for the first time
**When** its completion transaction commits
**Then** exactly 25 XP is added to the player track, exactly 25 XP is added to the named social-skill track, and exactly one gacha-draw entitlement is created
**And** quest completion, XP awards, draw entitlement, reward claims, and notification commit atomically.

**Given** the fulfilled commitment has its own NPC-provided reward or consequence
**When** fulfillment resolves
**Then** its transfers, relationship changes, and other terms follow the accepted agreement and ordinary conservation rules
**And** those results remain separately sourced from the System’s fixed XP and draw reward.

**Given** the quest XP crosses one or more existing progression thresholds
**When** the fixed rewards are applied
**Then** normal level advancement, carried excess XP, and any resulting unspent attribute points are processed under the existing progression rules
**And** each 25-XP quest award remains distinguishable from XP earned by any check used during fulfillment.

**Given** the player makes partial progress, succeeds at a social check without fulfilling the commitment, or fulfills a different commitment
**When** quest progress is evaluated
**Then** the daily quest remains incomplete and grants no quest XP or draw
**And** all independently committed actions, checks, transfers, time, and consequences remain valid.

**Given** the referenced commitment is renegotiated after daily-quest assignment
**When** its terms change
**Then** the daily quest’s original success contract is not silently rewritten
**And** only fulfillment matching the displayed contract before expiry can earn its reward.

**Given** the referenced commitment is fulfilled after the daily quest expires
**When** fulfillment commits
**Then** the ordinary agreement resolves normally
**And** the expired daily quest grants no XP, draw, penalty, or retroactive completion.

**Given** the referenced commitment was fulfilled before assignment or its fulfillment is replayed after quest completion
**When** reward eligibility is evaluated
**Then** no new daily-quest reward is granted
**And** past or duplicated evidence cannot be reused as current fulfillment.

**Given** completion fails before atomic commit or reward presentation fails after commit
**When** recovery runs
**Then** either no System reward component committed or the complete authoritative reward can be redisplayed
**And** retrying cannot duplicate commitment consequences, quest completion, either XP award, draw entitlement, or notification.

**Given** fulfillment or reward processing is interrupted, retried, saved, loaded, or mechanically replayed
**When** state is recovered
**Then** commitment and quest identities, required outcome, evidence, XP sources, progression results, draw entitlement, and reward claims remain consistent
**And** the same fulfillment event cannot satisfy the quest more than once.

**Given** the social daily quest and its completion are used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** parties, requirements, progress, expiry, result, and rewards are displayed
**Then** each has a readable label and clear pending, completed, expired, renegotiated, or rejected status
**And** no essential information depends only on color, hover, animation, or horizontal scrolling.

**Given** Story 9.3 automated evidence
**When** integration and browser tests run
**Then** all four named social skills, qualifying fulfillment, partial and unrelated actions, renegotiation, expiry, exact XP, agreement-reward separation, one draw entitlement, duplicate claims, recovery, replay, and save/load are verified against the real application and SQLite store
**And** first-party commitment, quest, progression, reward, economy, and persistence behavior is not mocked.

### Story 9.4: Complete an Observation Daily Quest

As a player,
I want visiting the named location and recording the specified condition to grant the stated reward,
So that careful exploration is recognized from what I actually observe.

**Acceptance Criteria:**

**Given** an active, unexpired observation daily quest
**When** the player inspects it
**Then** the named location, condition to investigate, required observation record, named relevant skill, expiry, and full reward are visible
**And** the condition’s undiscovered value is not disclosed and the success contract cannot change after assignment.

**Given** the player travels to and enters the named location after assignment
**When** their presence commits
**Then** ordinary travel time, access, permission, key, lock, capacity, and consequence rules apply
**And** the daily quest neither teleports the player nor grants special access to the location.

**Given** the player is present at the named location and validly observes the specified condition before expiry
**When** an accurate observation record commits
**Then** the condition becomes player knowledge with its actual source, subject, place, and observation time recorded
**And** the daily quest is completed from the committed presence and observation evidence.

**Given** observing the condition requires a check
**When** the check resolves
**Then** only a successful observation that reveals the condition can complete the quest
**And** the roll, contextual difficulty, modifiers, stakes, elapsed time, and any ordinary success-only XP follow the existing check rules.

**Given** the observation quest is completed for the first time
**When** its completion transaction commits
**Then** exactly 25 XP is added to the player track, exactly 25 XP is added to the quest’s named relevant-skill track, and exactly one gacha-draw entitlement is created
**And** quest completion, knowledge, XP awards, draw entitlement, reward claims, and notification commit atomically.

**Given** the quest XP crosses one or more existing progression thresholds
**When** the fixed rewards are applied
**Then** normal level advancement, carried excess XP, and any resulting unspent attribute points are processed under the existing progression rules
**And** each 25-XP quest award remains distinguishable from XP earned by the observation check itself.

**Given** the player visits without recording the condition, records a guess remotely, observes another condition or location, fails a required check, or cites knowledge obtained before assignment
**When** quest progress is evaluated
**Then** the quest remains incomplete and grants no quest XP or draw
**And** any independently valid travel, access, check, time, and knowledge consequences remain committed.

**Given** the specified condition changes after an accurate qualifying observation is recorded
**When** the quest record is inspected
**Then** the completed quest retains the factual observation and timestamp that satisfied it
**And** later world changes neither revoke the reward nor rewrite the historical observation.

**Given** the condition is validly observed and recorded only after the quest expires
**When** the observation commits
**Then** the player gains the ordinarily available knowledge
**And** the expired quest grants no XP, draw, penalty, or retroactive completion.

**Given** the observation or completion is repeated after the quest has resolved
**When** reward eligibility is evaluated
**Then** no additional daily-quest XP or draw is granted
**And** later observations may update knowledge without duplicating the original reward.

**Given** completion fails before atomic commit or reward presentation fails after commit
**When** recovery runs
**Then** either no completion component committed or the complete authoritative observation and reward can be redisplayed
**And** retrying cannot duplicate knowledge evidence, quest completion, either XP award, draw entitlement, or notification.

**Given** travel, observation, completion, or reward processing is interrupted, retried, saved, loaded, or mechanically replayed
**When** state is recovered
**Then** location, presence, observed condition, knowledge provenance, quest state, XP sources, draw entitlement, and reward claims remain consistent
**And** the same observation event cannot satisfy the quest more than once.

**Given** the observation daily quest and its completion are used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** destination, investigation target, knowledge status, expiry, result, and rewards are displayed
**Then** each has a readable label and clear pending, completed, expired, or rejected status
**And** no undiscovered result leaks through color, hover, focus text, animation, or layout.

**Given** Story 9.4 automated evidence
**When** integration and browser tests run
**Then** routine and checked observations, access boundaries, qualifying and nonqualifying records, knowledge filtering and provenance, changing conditions, expiry, exact XP, one draw entitlement, duplicate claims, recovery, replay, and save/load are verified against the real application and SQLite store
**And** first-party place, access, knowledge, check, quest, reward, and persistence behavior is not mocked.

### Story 9.5: Expire and Refresh the Daily Quest Set

As a player,
I want the daily quests to refresh predictably without punishing unfinished objectives,
So that they remain optional opportunities rather than obligations.

**Acceptance Criteria:**

**Given** an active daily set before its next 06:00 boundary
**When** the player inspects any quest
**Then** its exact expiry time and current state are visible
**And** the interface does not imply a failure penalty, streak, multiplier, or obligation to complete it.

**Given** one or more quest-qualifying actions complete exactly at 06:00
**When** same-timestamp events resolve
**Then** completed actions and their eligible quest fulfillment are evaluated before the scheduled expiry and refresh
**And** the established deterministic event ordering is recorded for replay.

**Given** the world clock reaches 06:00 with eligible inputs for a new set
**When** the scheduled refresh commits
**Then** all three prior slots are replaced together by exactly one new crafting, one new social, and one new observation quest
**And** every new quest receives a stable identity, fixed success contract, named skill, reward, assignment time, and next-06:00 expiry.

**Given** a prior quest is still incomplete at refresh
**When** the old set is replaced
**Then** that quest enters the expired state and grants no player XP, skill XP, or draw
**And** expiry removes no XP, level, attribute, Health, Mana, Stamina, gold, item, relationship, knowledge, or other earned state.

**Given** a prior quest was completed before refresh
**When** its slot is replaced
**Then** its completed historical record, XP awards, and unused gacha-draw entitlement remain intact
**And** refresh neither repeats nor revokes any earned reward.

**Given** an expired quest had partial progress
**When** the new set becomes active
**Then** quest-specific progress does not carry into or satisfy a replacement quest
**And** independently committed crafts, items, travel, knowledge, checks, agreements, transfers, and world consequences remain unchanged.

**Given** a replacement quest resembles an expired quest
**When** its contract is evaluated
**Then** it remains a new quest instance requiring new post-assignment fulfillment
**And** evidence from the expired instance cannot be reused for its reward.

**Given** time advances across more than one 06:00 boundary
**When** scheduled events are processed
**Then** each intervening set expires and is replaced in chronological order, with the latest valid set occupying the three slots
**And** skipped sets generate no reward, penalty, streak, multiplier, or duplicate assignment.

**Given** a proposed replacement set contains an invalid or ineligible quest
**When** refresh validation runs
**Then** no partial replacement set commits and the failed refresh has a visible recoverable state
**And** expired quests cannot be restored as active or silently rewritten to conceal the failure.

**Given** refresh fails before commit or presentation fails after commit
**When** recovery runs
**Then** either the authoritative old-to-new transition remains uncommitted or the complete committed set can be redisplayed
**And** retrying does not advance the clock again, expire a quest twice, or duplicate a new set.

**Given** a branch is saved before, during, or after the 06:00 boundary and then loaded
**When** scheduled processing resumes
**Then** quest states, slot assignments, contracts, rewards, draw entitlements, clock position, and refresh evidence restore consistently
**And** no quest completion, expiry, or replacement event is skipped or repeated.

**Given** refresh and expiry are viewed with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** old and new quest states are presented
**Then** expiry time, expired status, preserved rewards, refresh status, and replacement contracts have readable labels and sensible focus order
**And** no penalty or continuity is implied through color, animation, hover, or layout alone.

**Given** Story 9.5 automated evidence
**When** integration and browser tests run
**Then** exact-boundary completion, atomic three-slot replacement, incomplete and completed quests, partial progress, similar replacements, multi-day advancement, invalid sets, recovery, replay, and save/load are verified against the real application and SQLite store
**And** first-party clock, scheduler, quest, reward, and persistence behavior is not mocked.

### Story 9.6: Draw from the Visible Gacha Pool

As a player,
I want to inspect the complete reward pool before spending an earned draw,
So that the odds are transparent even though the result remains uncertain.

**Acceptance Criteria:**

**Given** the player has one or more unused gacha-draw entitlements
**When** they inspect the draw interface
**Then** it displays the entitlement count, active pool version, Common 70%, Uncommon 25%, and Rare 5% tier chances
**And** no random result, selected tier, selected item, or future random evidence is revealed before commitment.

**Given** the active P7 pool is displayed
**When** the Common tier is inspected
**Then** its four uniformly selected entries are two basic ingredients worth 2 gold, Healing Draft worth 4 gold, Mana Draft worth 4 gold, and Common Ale worth 3 gold
**And** each crafted item links to its stable G19 effect rather than a generated or altered reward definition.

**Given** the active P7 pool is displayed
**When** the Uncommon tier is inspected
**Then** its three uniformly selected entries are two rare catalysts worth 8 gold, Restorative Elixir worth 10 gold, and Mana Elixir worth 10 gold
**And** each crafted item links to its stable G19 effect rather than a generated or altered reward definition.

**Given** the active P7 pool is displayed
**When** the Rare tier is inspected
**Then** its two uniformly selected entries are Perfect Catalyst worth 15 gold and System Token worth 15 gold
**And** their one-use substitution and reroll contracts are visible before drawing.

**Given** the player confirms a draw using an unused entitlement and the current pool version
**When** the draw resolves
**Then** the rules first select a tier using the approved 70/25/5 distribution and then select uniformly among that tier’s eligible entries
**And** the pool version, eligible entries, random evidence, selected tier, selected entry, source entitlement, and request identity are recorded.

**Given** a valid draw commits
**When** its result is awarded
**Then** exactly one entitlement is consumed and exactly one selected pool entry is added to inventory in the same transaction
**And** bundle entries add exactly two ingredient units while each other entry adds one stable item instance.

**Given** the committed result is presented
**When** the player inspects the award
**Then** its tier, item or bundle name, quantity, value, fixed effect or use contract, and inventory destination are stated
**And** award narration cannot substitute another item, change its mechanics, or conceal what was received.

**Given** the player owns multiple draw entitlements
**When** one valid draw commits
**Then** only its referenced entitlement is consumed
**And** remaining entitlements persist across quest refreshes, saves, and loads without expiring or merging their claim identities.

**Given** the player has no unused entitlement, submits a stale pool or world revision, or references an unknown pool entry
**When** draw validation runs
**Then** the request is rejected with a specific reason before random selection
**And** no entitlement, random state, inventory, fictional time, or prior reward changes.

**Given** a draw request is retried after its result committed
**When** idempotent recovery runs
**Then** the same tier, entry, random evidence, and awarded item are returned
**And** no second entitlement is consumed and no additional item is created.

**Given** draw processing fails before atomic commit or result presentation fails after commit
**When** recovery runs
**Then** either no entitlement or random result committed, or the complete authoritative result can be redisplayed
**And** retrying cannot reroll a committed result or duplicate its award.

**Given** a draw is interrupted, saved, loaded, or mechanically replayed
**When** its state is recovered
**Then** entitlement ownership, pool version, random evidence, tier, entry, inventory award, and request result remain consistent
**And** the same recorded inputs reproduce the same mechanical outcome.

**Given** the pool and draw result are used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** tiers, entries, odds, confirmation, operation status, and results are displayed
**Then** each has a readable label and sensible focus and reading order
**And** rarity, uncertainty, or award identity is not conveyed only by color, animation, hover, or horizontal scrolling.

**Given** Story 9.6 automated evidence
**When** integration and browser tests run
**Then** all nine entries, exact values and fixed effects, tier boundaries, uniform in-tier selection, bundle quantities, entitlement accounting, invalid draws, atomic awards, idempotency, replay, and save/load are verified against the real application and SQLite store
**And** first-party random, reward, inventory, item-definition, and persistence behavior is not mocked.

### Story 9.7: Craft with a Perfect Catalyst

As a player,
I want to substitute a Perfect Catalyst for a known recipe’s ingredients,
So that a rare draw can enable one valuable craft without bypassing the rest of its rules.

**Acceptance Criteria:**

**Given** the player owns a Perfect Catalyst
**When** they inspect it
**Then** it is shown as a one-use item worth 15 gold that substitutes for all ingredients in one execution of one known recipe
**And** it explicitly does not grant recipe knowledge or replace tools, facilities, work time, skill requirements, checks, targets, or other non-ingredient prerequisites.

**Given** the player selects a known recipe and previews Perfect Catalyst use
**When** the craft terms are displayed
**Then** the recipe version, output, normally required ingredients, ingredients to be replaced, required tools, work duration, relevant skill, and any check are visible
**And** previewing or cancelling consumes no item, ingredient, time, or resource.

**Given** the player validly confirms Perfect Catalyst use for one known recipe
**When** the crafting attempt commits
**Then** exactly one Perfect Catalyst is consumed in place of all ingredient units required for that attempt
**And** owned basic ingredients and rare catalysts that would otherwise satisfy the recipe remain unchanged.

**Given** a routine recipe is validly crafted with the Perfect Catalyst
**When** its work completes
**Then** the normal recipe output, elapsed time, successful-craft count, and other ordinary consequences commit
**And** the output’s identity, effect, quantity, and value are identical to the recipe’s non-Catalyst result.

**Given** an uncertain recipe attempt uses the Perfect Catalyst
**When** its check fails
**Then** the Catalyst is consumed and the declared work time and failure consequences commit without producing an item
**And** no successful-craft count, success-only XP, or ingredient refund is created.

**Given** a successful Catalyst craft matches an active crafting daily quest’s named recipe
**When** the output commits before that quest expires
**Then** the output can satisfy that quest through the same ordinary crafting evidence
**And** Catalyst use neither disqualifies the craft nor creates an additional daily-quest reward.

**Given** the player selects an unknown recipe, lacks a required tool or facility, chooses an invalid output or target, submits stale state, or attempts to cover more than one recipe execution
**When** validation runs
**Then** the request is rejected with a specific reason before commitment
**And** the Catalyst, other inventory, fictional time, random state, and crafting records remain unchanged.

**Given** the player sells, transfers, or loses the Perfect Catalyst before using it
**When** they later attempt a Catalyst craft
**Then** the request fails unless they currently own another valid Catalyst
**And** an ordinary sale values the transferred item at 15 gold without duplicating or consuming it twice.

**Given** Catalyst crafting fails before atomic commit or result presentation fails after commit
**When** recovery runs
**Then** either no Catalyst, time, output, count, or XP committed, or the complete authoritative crafting result can be redisplayed
**And** retrying cannot restore a spent Catalyst or duplicate an output.

**Given** a Catalyst craft is interrupted, retried, saved, loaded, or mechanically replayed
**When** state is recovered
**Then** Catalyst identity and ownership, recipe version, substituted inputs, elapsed work, roll evidence, output or failure, production count, and XP remain consistent
**And** the same Catalyst instance cannot fund more than one committed attempt.

**Given** Catalyst inspection and crafting are used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** recipe terms, substitutions, confirmation, validation, and results are displayed
**Then** each has a readable label and sensible focus and reading order
**And** ingredient replacement or item consumption is not conveyed only through color, hover, animation, or horizontal scrolling.

**Given** Story 9.7 automated evidence
**When** integration and browser tests run
**Then** base and upgraded known recipes, routine success, uncertain failure, ingredient preservation, non-ingredient prerequisites, daily-quest qualification, invalid requests, sale, atomicity, idempotency, replay, and save/load are verified against the real application and SQLite store
**And** first-party crafting, item, quest, progression, transaction, and persistence behavior is not mocked.

### Story 9.8: Reroll a Future Draw with a System Token

As a player,
I want to spend a System Token on a future gacha draw,
So that I can reroll once while accepting the uncertainty of the second result.

**Acceptance Criteria:**

**Given** the player owns a System Token
**When** they inspect it
**Then** it is shown as a one-use item worth 15 gold that rerolls one future gacha draw and requires acceptance of the second result
**And** it cannot alter tier odds, pool entries, item definitions, or any already awarded result.

**Given** the player owns a System Token and an unused draw entitlement
**When** they prepare a future draw
**Then** they can explicitly choose whether to reserve one Token for that draw before random selection begins
**And** previewing, declining, or cancelling before commitment consumes neither the Token nor the entitlement.

**Given** the player explicitly confirms a Token-backed draw
**When** it resolves
**Then** the rules perform one complete tier-and-entry selection followed by a second complete tier-and-entry selection from the same versioned 70/25/5 pool
**And** separate random evidence records the tier and uniform in-tier result for both selections.

**Given** the Token-backed draw commits
**When** its reward transaction completes
**Then** exactly one draw entitlement and one reserved System Token are consumed, the first result is recorded as replaced, and only the second result is added to inventory
**And** both selections, consumptions, accepted result, awarded item, and request result commit atomically.

**Given** the player confirms System Token use before the draw
**When** the first and second results are known
**Then** that confirmation constitutes advance acceptance of the second result
**And** the player cannot reclaim the first result, choose the better result, cancel the second, or perform another reroll on the same draw.

**Given** the first and second selections produce the same tier or item
**When** the result is presented
**Then** the second selection remains the accepted result and only one award is created
**And** matching outcomes do not refund the Token or entitlement.

**Given** the second result is another System Token
**When** it is awarded
**Then** the new Token enters inventory as the single accepted item
**And** it can apply only to a later draw, not to another reroll of the current draw.

**Given** a System Token was awarded by the current draw, was sold or lost, is already reserved or spent, or was not selected before random resolution began
**When** a reroll is requested
**Then** the request is rejected with a specific reason
**And** no committed draw is reopened and no entitlement, item, random state, or inventory award changes.

**Given** the player submits a stale pool or world revision, lacks an unused entitlement, or attempts to reserve more than one Token
**When** validation runs
**Then** the Token-backed draw is rejected before random selection
**And** all Tokens, entitlements, random state, inventory, and prior results remain unchanged.

**Given** a Token-backed draw fails before atomic commit or presentation fails after commit
**When** recovery runs
**Then** either neither selection nor consumption committed, or the complete two-result record and accepted award can be redisplayed
**And** retrying cannot generate new results, refund a spent Token, consume another entitlement, or duplicate the award.

**Given** a Token-backed draw is interrupted, retried, saved, loaded, or mechanically replayed
**When** state is recovered
**Then** Token and entitlement identities, pool version, both random records, replaced result, accepted result, and inventory award remain consistent
**And** the same recorded inputs reproduce the same two selections and final award.

**Given** Token selection and reroll results are used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the reservation, confirmation, both results, replacement status, and final award are displayed
**Then** each has a readable label and sensible focus and reading order
**And** replaced versus accepted results are not distinguished only by color, animation, hover, or horizontal layout.

**Given** Story 9.8 automated evidence
**When** integration and browser tests run
**Then** explicit reservation, both tier and in-tier rolls, mandatory second-result acceptance, matching results, a second-result Token, invalid timing and ownership, atomic consumption, idempotency, replay, and save/load are verified against the real application and SQLite store
**And** first-party random, reward, inventory, transaction, and persistence behavior is not mocked.

### Story 9.9: Distinguish System and Award Presentation

As a player,
I want daily-quest messages to be clearly attributable,
So that I can distinguish the fourth-wall-breaking System from the world, its characters, and authoritative mechanical results.

**Acceptance Criteria:**

**Given** a daily quest set is committed
**When** its assignment is presented
**Then** it uses the approved clean System-style treatment with an explicit `System` source label independent of color
**And** the narrator, Rowan, and NPCs are not presented as assigning or speaking the objectives.

**Given** a System quest is displayed in the journal or transcript
**When** its content is read
**Then** the objective, success contract, skill, reward, state, and expiry come from the authoritative quest instance
**And** System wording cannot add a hidden requirement, recommend a route, imply mandatory participation, or rewrite the fixed contract.

**Given** a player action contributes to a daily quest
**When** its result is presented
**Then** in-world narration, NPC speech, check details, mechanical consequences, quest-status changes, and award notices retain separate labeled presentation roles
**And** one role’s prose cannot be mistaken for or substitute for another role’s authoritative record.

**Given** a daily quest is only partially fulfilled
**When** System status is presented
**Then** it reports the quest’s actual unresolved state without announcing success or reward
**And** award narration does not claim XP, a draw, or an item that has not committed.

**Given** a daily quest completion commits
**When** the result is presented
**Then** the System may announce the completed objective while a separately labeled award notice states the committed 25 player XP, 25 named-skill XP, and one draw entitlement
**And** the mechanical result remains independently inspectable from both presentation layers.

**Given** a gacha draw or Token-backed reroll commits
**When** its result is presented
**Then** System presentation identifies the draw event while the separate award notice identifies the authoritative accepted item, tier, quantity, value, and effect
**And** replaced, pending, rejected, or uncommitted results are never narrated as awarded.

**Given** a daily quest expires at refresh
**When** the transition is presented
**Then** the System identifies the expired quest and newly assigned set without punitive language or fabricated consequences
**And** narration, NPC dialogue, and awards do not imply a penalty, streak loss, or in-world speaker responsible for the refresh.

**Given** Rowan is asked about known daily quests or rewards
**When** Rowan responds
**Then** Rowan may restate player-visible authoritative information with clear attribution to the System record
**And** Rowan cannot create a quest, certify fulfillment, grant a reward, reveal a draw result early, or speak as the System.

**Given** an NPC discusses the player’s actions
**When** dialogue is generated
**Then** the NPC speaks only from their own knowledge and observed world consequences
**And** private System state, draw odds, reward claims, or uncommunicated quest details are not placed into NPC knowledge.

**Given** an operation is pending, rejected, failed before commit, or interrupted
**When** status is presented
**Then** the interface uses the corresponding factual request state and offers the supported recovery path
**And** no System, award, narrator, Rowan, NPC, or mechanical channel implies that unfinished work succeeded.

**Given** mechanics commit but System or award presentation fails
**When** presentation recovery runs
**Then** the committed result can be safely regenerated or redisplayed from authoritative facts
**And** presentation recovery cannot rerun the quest action, XP award, draw, random selection, or inventory mutation.

**Given** attributed messages are retried, saved, loaded, or revisited
**When** their history is displayed
**Then** stable source labels, message roles, authoritative references, and delivery state remain consistent
**And** recovery does not append duplicate assignment, completion, expiry, or award claims.

**Given** System, award, mechanical, narrator, Rowan, and NPC content is used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** mixed-source results are displayed
**Then** every source has a programmatically determinable label, sensible reading order, visible focus, and no timed reading requirement
**And** attribution never depends only on color, typography, position, animation, or sound.

**Given** Story 9.9 automated evidence
**When** integration and browser tests run
**Then** assignment, partial progress, completion, expiry, base draws, Token rerolls, pending and failed operations, Rowan recall, NPC knowledge filtering, presentation recovery, attribution, and accessibility are verified against the real application and SQLite store
**And** tests prove that no presentation channel can create or misstate an uncommitted objective or reward.

### Story 9.10: Verify the P7 Daily-Quest and Gacha Gate

As a playtester,
I want to exercise the complete P7 daily-quest and reward loop,
So that hidden objectives are considered only after explicit quests remain optional, fair, and reproducible.

**Acceptance Criteria:**

**Given** an authorized P7 build, its phase-specific UX contract, and controlled starting states
**When** P7 content and stage boundaries are validated
**Then** exactly three daily quest slots, the crafting, social, and observation categories, and the versioned nine-entry gacha pool are available
**And** P8 hidden conditions, hidden rewards, combat quests, combat content, streaks, multipliers, and failure penalties remain absent.

**Given** an eligible P6 branch is upgraded and advanced to the first applicable 06:00 boundary
**When** migration and scheduled assignment run
**Then** all existing state is preserved and exactly one valid quest of each approved category is assigned with an explicit contract, named skill, reward, and expiry
**And** no partial migration, unsupported quest, or duplicate scheduled event is created.

**Given** controlled crafting, social, and observation quest fixtures
**When** each category is fulfilled through committed evidence before expiry
**Then** each quest awards exactly 25 player XP, 25 XP to its named relevant skill, and one distinct gacha-draw entitlement exactly once
**And** ordinary crafting, commitment, observation, knowledge, check, economy, and progression consequences remain separately sourced and conserved.

**Given** partial, incorrect, pre-assignment, post-expiry, repeated, and merely declared attempts in every category
**When** fulfillment is evaluated
**Then** no daily-quest XP or draw is awarded
**And** independently valid world actions and consequences remain committed without being rewritten as quest success.

**Given** incomplete, completed, and partially progressed quests at a 06:00 boundary
**When** refresh resolves
**Then** the prior three slots transition and are replaced together under deterministic same-timestamp ordering
**And** unfinished quests expire without penalty, completed rewards persist, and partial quest progress does not carry into the new instances.

**Given** controlled random inputs spanning every tier boundary and eligible in-tier result
**When** ordinary draws are resolved
**Then** Common, Uncommon, and Rare use the exact 70%, 25%, and 5% distribution and selection is uniform among the four, three, and two entries in the selected tier
**And** all nine pool outcomes produce the correct quantity, stable identity, effect or contract, and value from the visible pool version.

**Given** a Perfect Catalyst is awarded
**When** it is used in successful and failed controlled crafts
**Then** it replaces all ingredients for one known-recipe attempt while preserving every other crafting requirement and is consumed on the committed attempt
**And** success produces the ordinary output while failure produces none.

**Given** a System Token is awarded before a later draw
**When** it is explicitly reserved for that draw
**Then** two complete results are recorded from the same pool version, the first is replaced, the second is mandatory, and only the second is awarded
**And** the current draw, second result, matching outcome, or another Token cannot create an additional reroll.

**Given** System assignments, progress, completion, expiry, draws, rerolls, and awards are presented alongside in-world activity
**When** source attribution is inspected
**Then** System, award, mechanics, narrator, Rowan, and NPC roles remain visibly and programmatically distinct
**And** no channel claims an objective, fulfillment, XP award, draw result, or item before it commits.

**Given** one failure or interruption is introduced during migration, assignment, category fulfillment, refresh, reward claim, ordinary draw, Token reroll, and result presentation
**When** recovery and safe retry are exercised
**Then** every commit boundary is identifiable and unfinished work can resume without repeating committed mechanics
**And** no quest, elapsed time, XP, level, draw entitlement, random result, Token, Catalyst, or inventory award is lost or duplicated.

**Given** branches are saved before fulfillment, across 06:00 refresh, during recoverable operations, after draws, and after rare-item use
**When** each branch is loaded and continued
**Then** quests, contracts, clock events, evidence, XP, entitlements, pool versions, random records, items, uses, and presentation references restore exactly
**And** loading cannot complete, expire, reroll, or reward anything a second time.

**Given** the same captured state, content versions, structured proposals, and recorded random inputs
**When** mechanical replay is run
**Then** assignments, fulfillment decisions, refreshes, XP, tier and entry selections, rerolls, awards, and state hashes reproduce exactly
**And** regenerated prose cannot change any objective, evidence decision, probability, or reward.

**Given** a player completes one displayed daily contract through an unplanned but supported approach
**When** its committed evidence is evaluated
**Then** the quest can complete if the exact visible success contract is genuinely satisfied
**And** the System neither prescribes a tactic nor rejects valid fulfillment merely because it differs from the fixture route.

**Given** P7 journeys are tested with keyboard, pointer, screen reader, 200% zoom, and 320-pixel reflow
**When** assignment, journal inspection, completion, refresh, pool comparison, draws, rare-item use, mixed-source notices, and recovery are exercised
**Then** objectives, odds, expiry, states, confirmation, attribution, and rewards remain readable and operable
**And** no essential information or action depends only on color, hover, animation, sound, timed reading, or horizontal scrolling.

**Given** P7 playtest sessions
**When** feedback is recorded
**Then** evidence separately captures whether explicit contracts clarify goals, whether System presentation intrudes on free play, what felt unfair or unclear, and what the player wants next
**And** mechanical correctness is not treated as proof that the daily structure complements the game.

**Given** an unexplained contradiction, hidden P7 requirement, premature success claim, incorrect XP, duplicate reward, invalid pool outcome, reroll-choice violation, knowledge leak, attribution failure, conservation error, or save/load failure
**When** the P7 gate is evaluated
**Then** the affected scenario fails and is corrected and repeated
**And** P8 remains unauthorized.

**Given** all P7 evidence passes
**When** Epic 9 closes
**Then** P7 is marked eligible for a separate P8 authorization decision
**And** hidden bonus objectives and combat remain unavailable until their stages are explicitly authorized.

## Epic 10: Discover Hidden Quest Bonuses

Players can receive bounded surprise rewards when committed evidence satisfies a private unusual-approach condition without revealing the trigger or routinely over-awarding normal play.

### Story 10.1: Attach One Private Bonus Condition

As a player,
I want each new quest to have one bounded opportunity for surprising recognition,
So that an unusual supported approach can matter without changing the quest’s visible promise.

**Acceptance Criteria:**

**Given** the P7 evidence gate has not passed, P8 has not been separately authorized, or no P8-specific UX contract is approved
**When** a P8 upgrade is requested
**Then** hidden-condition records, hidden bonus evaluation, and hidden bonus notices remain unavailable
**And** the existing P7 branch remains unchanged.

**Given** an eligible P7 branch is upgraded to P8
**When** migration runs
**Then** it validates the immediately preceding ruleset and content versions and records the P8 stage atomically
**And** existing character, world, quest, reward, inventory, progression, clock, and random-evidence state is preserved.

**Given** active quests existed before the P8 upgrade
**When** migration completes
**Then** those quests retain their existing contracts and rewards without receiving retroactive hidden conditions
**And** only supported quest instances created after P8 authorization are eligible for P8 hidden bonuses.

**Given** a new daily System quest is created after P8 authorization
**When** its quest record commits
**Then** exactly one private hidden-condition child record is created in the same transaction
**And** the quest’s visible success contract, named skill, ordinary reward, lifecycle, and expiry remain unchanged.

**Given** an accepted NPC commitment becomes a supported organic quest after P8 authorization
**When** its quest record commits
**Then** exactly one private hidden-condition child record is created in the same transaction
**And** an unresolved situation, unaccepted proposal, or non-quest concern receives no hidden condition.

**Given** a hidden condition is created
**When** its private record is inspected through authorized diagnostics
**Then** it stores the unusual supported approach, qualifying-evidence contract, fixed evaluation point, evaluator version, quest identity, condition version, and one seeded reward
**And** none of those private fields are copied into player-visible quest, journal, transcript, narration, or model context that does not require them.

**Given** the reward is seeded at quest creation
**When** reward type is selected
**Then** XP, extra draw, and Common item are selected uniformly
**And** the seed, eligible reward types, selected type, and complete fixed reward definition are recorded for replay.

**Given** the seeded reward type is XP
**When** its fixed definition is created
**Then** an integer from 10 through 25 inclusive is seeded for both the player and the quest’s named relevant-skill tracks
**And** the amount cannot be changed later based on the player’s approach or evaluator judgment.

**Given** the seeded reward type is an extra draw
**When** its fixed definition is created
**Then** it specifies exactly one additional G20 draw entitlement
**And** it does not alter the ordinary quest reward, gacha pool, odds, or item result.

**Given** the seeded reward type is an item
**When** its fixed definition is created
**Then** one entry is selected uniformly from the four Common G20 entries and its stable quantity, item definition, and value of at most 5 gold are recorded
**And** no Uncommon, Rare, generated, or condition-shaped item can be substituted later.

**Given** a proposed hidden condition describes an impossible or unsupported action, the quest’s routine fulfillment path, evidence unavailable at its evaluation point, private knowledge the player cannot act upon, or an approach unrelated to the visible quest
**When** creation validation runs
**Then** the proposal is rejected before the P8 quest commits
**And** no partial condition, seed, reward, or player-visible hint is stored.

**Given** quest or hidden-condition creation fails before commit
**When** recovery is offered
**Then** no P8 quest is treated as valid without exactly one complete private condition record
**And** retrying cannot attach two conditions, reseed a committed reward, or change a visible quest contract.

**Given** a P8 quest is retried, saved, loaded, refreshed, or mechanically replayed
**When** its state is recovered
**Then** quest and condition identities, versions, evaluation point, evaluator version, reward seed, eligible set, and selected reward remain stable
**And** the private record remains absent from every ordinary player projection.

**Given** a player-visible P8 quest is inspected with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** its ordinary contract is displayed
**Then** it remains as readable and operable as the corresponding P7 or organic quest
**And** hidden-condition content does not leak through labels, counts, empty regions, focus order, accessibility text, network payloads, or layout changes.

**Given** Story 10.1 automated evidence
**When** integration and browser tests run
**Then** P8 gating, adjacent-version migration, non-retroactivity, System and organic quest creation, exactly-one private child, all reward-type and value boundaries, invalid conditions, idempotency, replay, save/load, and player-projection secrecy are verified against the real application and SQLite store
**And** first-party migration, quest, random, reward-definition, projection, and persistence behavior is not mocked.

### Story 10.2: Earn a Hidden XP Bonus

As a player,
I want an unusual qualifying approach to earn the quest’s fixed XP bonus,
So that creative play can receive bounded recognition without changing the visible objective.

**Acceptance Criteria:**

**Given** an active P8 System or organic quest has a private XP-type hidden condition
**When** its fixed evaluation point is reached
**Then** the evaluator receives only the versioned condition contract and relevant committed evidence available by that point
**And** uncommitted proposals, generated narration, later events, and unrelated private knowledge are excluded.

**Given** bounded LLM evaluation runs
**When** it returns a judgment proposal
**Then** the strict result identifies the quest, condition, evaluator version, satisfied-or-not decision, and cited committed evidence
**And** the evaluator cannot select, change, enlarge, or directly grant the seeded reward.

**Given** the evaluator proposes that the condition was satisfied
**When** deterministic validation runs
**Then** every cited event must exist, belong to the correct branch and quest attempt, occur by the evaluation point, and satisfy the fixed unusual-approach and evidence contract
**And** prose similarity, unsupported inference, player assertion, or fabricated evidence cannot qualify.

**Given** valid committed evidence satisfies the private condition
**When** quest resolution commits
**Then** the seeded integer from 10 through 25 is added once to the player XP track and once to the quest’s named relevant-skill XP track
**And** quest resolution, ordinary rewards, both hidden XP awards, the unique hidden-bonus claim, and its notification record commit atomically.

**Given** the quest also grants ordinary player or skill XP
**When** all rewards are applied
**Then** ordinary and hidden XP remain separately identified by quest, reward kind, amount, and source event
**And** the hidden amount supplements rather than replaces or modifies the visible reward.

**Given** either XP award crosses one or more progression thresholds
**When** progression resolves
**Then** normal level advancement, carried excess XP, and resulting unspent attribute points are processed
**And** retries cannot repeat a level, point, or hidden XP source.

**Given** the seeded hidden amount is 10 or 25
**When** the qualifying reward commits
**Then** that exact inclusive boundary amount is applied to both tracks
**And** no rounding, difficulty adjustment, evaluator confidence, or narrative emphasis changes it.

**Given** the evaluator response is malformed, mismatched to the quest or version, cites missing or post-evaluation evidence, or requests a reward outside the fixed definition
**When** validation runs
**Then** the proposal is rejected and the atomic quest-resolution boundary remains visibly recoverable
**And** no completion claim, ordinary reward, hidden XP, notification, or partial progression change commits from that invalid proposal.

**Given** evaluation or presentation is unavailable or interrupted
**When** recovery runs
**Then** uncommitted evaluation can be retried against the same condition and evidence while a committed result can be redisplayed
**And** recovery cannot alter the seeded amount, substitute evidence, or create a second claim.

**Given** a hidden XP claim has already committed
**When** evaluation, quest resolution, or notification delivery is retried
**Then** the prior decision and reward are returned
**And** neither XP track, progression result, ordinary reward, nor notification is duplicated.

**Given** a qualifying quest is saved, loaded, or mechanically replayed before or after evaluation
**When** its state is recovered
**Then** condition and evaluator versions, evidence references, private reasoning, seeded amount, claim identity, XP sources, and progression results remain consistent
**And** the same recorded inputs produce the same validated mechanical decision.

**Given** the hidden XP reward is presented with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the committed bonus notice and XP results are displayed
**Then** the two awarded tracks and exact amount have readable labels and clear status
**And** the hidden condition, evaluator reasoning, evidence contract, or missed alternatives are not exposed through visible or accessibility content.

**Given** Story 10.2 automated evidence
**When** integration and browser tests run
**Then** System and organic quests, 10 and 25 XP boundaries, valid and invalid evaluator proposals, evidence timing and provenance, ordinary-reward separation, level crossings, atomicity, duplicate claims, recovery, replay, save/load, and secrecy are verified against the real application and SQLite store
**And** first-party evaluation validation, quest, progression, reward, projection, and persistence behavior is not mocked.

### Story 10.3: Earn a Hidden Extra Draw

As a player,
I want an unusual qualifying approach to earn one additional item draw,
So that creative play can produce a bounded surprise without changing the published reward.

**Acceptance Criteria:**

**Given** an active P8 System or organic quest has a private extra-draw hidden condition
**When** its fixed evaluation point is reached
**Then** bounded evaluation uses the recorded evaluator version, private condition contract, and only relevant committed evidence available by that point
**And** the evaluator cannot modify the fixed reward, visible quest contract, G20 pool, odds, or entries.

**Given** the evaluator proposes that the hidden condition was satisfied
**When** deterministic validation runs
**Then** the cited evidence must belong to the correct quest attempt, occur by the evaluation point, and satisfy the recorded unusual approach
**And** malformed output, fabricated evidence, unsupported inference, or a merely routine completion path is rejected.

**Given** valid committed evidence satisfies the private condition
**When** quest resolution commits
**Then** exactly one additional G20 draw entitlement is created with a stable identity and hidden-bonus source
**And** quest resolution, ordinary rewards, the extra entitlement, unique hidden-bonus claim, and notification record commit atomically.

**Given** a daily System quest also awards its ordinary draw
**When** the qualifying completion commits
**Then** the ordinary and hidden entitlements remain two distinct claims with separate reward-kind identities
**And** neither entitlement replaces, merges with, or duplicates the other.

**Given** an organic quest has no ordinary gacha reward
**When** its extra-draw hidden condition is satisfied
**Then** exactly one hidden-bonus entitlement is created
**And** no ordinary draw or other undeclared reward is fabricated.

**Given** the extra entitlement is awarded
**When** the player inspects it before use
**Then** no tier, item, or random result has been selected
**And** its future draw must use the current supported G20 draw rules and a version validated at draw time.

**Given** the extra entitlement remains unused through a 06:00 refresh
**When** daily quests expire and are replaced
**Then** the entitlement remains owned and available
**And** refresh neither expires it nor creates another entitlement.

**Given** the player spends the extra entitlement on an ordinary or System-Token-backed draw
**When** the draw commits
**Then** the normal P7 pool, random, reroll, award, and idempotency rules apply
**And** the draw record retains the hidden-bonus entitlement as its source without revealing the condition.

**Given** evaluation returns an invalid version, missing or late evidence, or a request for more than one draw
**When** validation runs
**Then** the proposal is rejected and the atomic quest-resolution boundary remains recoverable
**And** no completion claim, ordinary reward, extra entitlement, notification, or partial reward state commits from that proposal.

**Given** a hidden extra-draw claim has already committed
**When** evaluation, resolution, notification, or entitlement delivery is retried
**Then** the prior decision and entitlement are returned
**And** no second bonus draw, ordinary reward, or notification is created.

**Given** evaluation or presentation fails before or after commitment
**When** recovery runs
**Then** unfinished evaluation can retry against the same private condition and evidence while a committed award can be redisplayed
**And** recovery cannot change the reward type, preselect a result, or consume the entitlement.

**Given** the quest or entitlement is saved, loaded, or mechanically replayed
**When** state is recovered
**Then** evaluator version, evidence references, private reasoning, claim identity, entitlement identity and source, and later draw linkage remain consistent
**And** the same recorded inputs produce the same validated award decision.

**Given** the hidden extra draw is presented with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the committed notice and entitlement are displayed
**Then** the additional draw and its unused or consumed state have readable labels and clear status
**And** the hidden condition, evaluator reasoning, evidence contract, and unselected result remain absent from visible and accessibility content.

**Given** Story 10.3 automated evidence
**When** integration and browser tests run
**Then** System and organic quests, ordinary-plus-extra entitlements, persistence through refresh, ordinary and Token-backed spending, invalid evaluator proposals, at-most-one claims, atomicity, recovery, replay, save/load, and secrecy are verified against the real application and SQLite store
**And** first-party evaluation validation, quest, reward, gacha, projection, and persistence behavior is not mocked.

### Story 10.4: Earn a Hidden Common Item

As a player,
I want an unusual qualifying approach to earn one bounded item prize,
So that creative play can produce a useful surprise without creating arbitrary loot.

**Acceptance Criteria:**

**Given** an active P8 System or organic quest has a private Common-item hidden condition
**When** its fixed evaluation point is reached
**Then** bounded evaluation uses the recorded evaluator version, private condition contract, and only relevant committed evidence available by that point
**And** the evaluator cannot select or change the item, quantity, value, effect, visible quest contract, or ordinary reward.

**Given** the evaluator proposes that the hidden condition was satisfied
**When** deterministic validation runs
**Then** the cited evidence must belong to the correct quest attempt, occur by the evaluation point, and satisfy the recorded unusual approach
**And** malformed output, fabricated evidence, unsupported inference, or routine fulfillment alone is rejected.

**Given** the fixed hidden reward is inspected through authorized diagnostics
**When** its Common-pool selection is validated
**Then** it is exactly one of two basic ingredients worth 2 gold, Healing Draft worth 4 gold, Mana Draft worth 4 gold, or Common Ale worth 3 gold
**And** the recorded selection came uniformly from those four entries at quest creation.

**Given** valid committed evidence satisfies the private condition
**When** quest resolution commits
**Then** the fixed Common entry is added to inventory, with a bundle award adding exactly two basic-ingredient units and any other entry adding one stable item instance
**And** quest resolution, ordinary rewards, inventory change, unique hidden-bonus claim, and notification record commit atomically.

**Given** Healing Draft, Mana Draft, or Common Ale is awarded
**When** the player inspects or uses it
**Then** it retains the corresponding stable G19 identity, effect, use rules, and value
**And** the hidden condition or evaluator cannot generate a variant or change its mechanics.

**Given** the hidden Common item is awarded
**When** random and entitlement records are inspected
**Then** no gacha-draw entitlement was consumed and no new tier or item selection occurred at evaluation
**And** the award uses the item fixed at quest creation rather than drawing again from the pool.

**Given** the quest also grants an ordinary item, XP, or draw reward
**When** all rewards commit
**Then** the ordinary and hidden rewards remain distinct claims with separate source and reward-kind identities
**And** neither replaces, enlarges, or duplicates the other.

**Given** the awarded item is later used, sold, transferred, or lost
**When** the resolved quest is inspected
**Then** the hidden-bonus claim and completed quest remain recorded
**And** later ownership changes do not revoke the bonus or create another item.

**Given** evaluation references an Uncommon, Rare, generated, over-5-gold, differently quantified, or post-creation item
**When** validation runs
**Then** the proposal is rejected and the atomic quest-resolution boundary remains recoverable
**And** no completion claim, ordinary reward, inventory item, notification, or partial reward state commits from that proposal.

**Given** a hidden Common-item claim has already committed
**When** evaluation, resolution, notification, or item delivery is retried
**Then** the prior decision and awarded item identity are returned
**And** no second bundle, item, ordinary reward, or notification is created.

**Given** evaluation or presentation fails before or after commitment
**When** recovery runs
**Then** unfinished evaluation can retry against the same private condition and evidence while a committed award can be redisplayed
**And** recovery cannot change the selected entry, quantity, item identity, effect, or value.

**Given** the quest or awarded item is saved, loaded, or mechanically replayed
**When** state is recovered
**Then** evaluator version, evidence references, private reasoning, claim identity, seeded selection, inventory identity or quantity, ownership, and use state remain consistent
**And** the same recorded inputs produce the same validated award decision.

**Given** the hidden item reward is presented with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the committed notice and item result are displayed
**Then** the item or bundle name, quantity, value, effect, and inventory destination have readable labels and clear status
**And** the hidden condition, evaluator reasoning, evidence contract, and other eligible entries remain absent from visible and accessibility content.

**Given** Story 10.4 automated evidence
**When** integration and browser tests run
**Then** System and organic quests, all four Common entries, uniform seeded selection, bundle quantity, fixed item mechanics, ordinary-reward separation, invalid item proposals, at-most-one claims, sale or use, atomicity, recovery, replay, save/load, and secrecy are verified against the real application and SQLite store
**And** first-party evaluation validation, quest, reward, inventory, item-definition, projection, and persistence behavior is not mocked.

### Story 10.5: Keep the Hidden Trigger Secret

As a player,
I want a hidden bonus to arrive as a genuine surprise without exposing its trigger,
So that unusual play remains discoverable through experimentation rather than a concealed checklist.

**Acceptance Criteria:**

**Given** a P8 quest exists before its hidden condition is evaluated
**When** the player inspects the quest, journal, transcript, rewards, or ordinary application data
**Then** its visible contract and presentation are indistinguishable from the corresponding P7 System quest or ordinary organic quest
**And** no condition text, evaluation point, evaluator version, reward preview, private identity, or hidden-record count is exposed.

**Given** a hidden condition is satisfied and its reward commits
**When** the System notification is presented
**Then** its first line is exactly `HIDDEN CONDITION SATISFIED — Bonus acquired.`
**And** the committed reward follows without an explanation, paraphrase, evidence summary, or condition name.

**Given** the committed hidden reward is XP
**When** its reward line is displayed
**Then** it states the exact player-XP amount and the same amount awarded to the named relevant skill
**And** it does not disclose why that amount or reward type was selected.

**Given** the committed hidden reward is an extra draw
**When** its reward line is displayed
**Then** it states that one additional G20 draw was acquired and shows its entitlement state
**And** it reveals no future tier, item, random result, or qualifying behavior.

**Given** the committed hidden reward is a Common item
**When** its reward line is displayed
**Then** it states the awarded item or bundle, quantity, value, fixed effect or use contract, and inventory destination
**And** it does not reveal the other eligible entries or why that item was selected.

**Given** a hidden bonus is earned from an organic quest
**When** its notification is delivered
**Then** the same exact System notification and bounded reward presentation are used
**And** the NPC, narrator, Rowan, or ordinary quest issuer is not presented as knowing or awarding the private condition.

**Given** a player asks Rowan, an NPC, narration, or the System what triggered or could have triggered a bonus
**When** a response is produced
**Then** no hidden condition, evaluator reasoning, evidence contract, or missed alternative is revealed, confirmed, or denied
**And** no generated response invents a hint, prerequisite, strategy, or checklist.

**Given** ordinary narration or dialogue context is assembled before or after evaluation
**When** model inputs are prepared
**Then** private condition content and evaluator reasoning are excluded unless the bounded evaluator specifically requires them
**And** the evaluator’s private context is not reused for narration, Rowan, NPC dialogue, or award prose.

**Given** player-facing APIs, browser state, accessibility trees, telemetry intended for ordinary play, or recoverable error details are inspected
**When** a quest has a triggered or untriggered hidden condition
**Then** no private condition or evaluator reasoning is serialized
**And** only capability-gated diagnostics can access the complete private record.

**Given** hidden evaluation is pending, malformed, rejected, failed, or interrupted
**When** operation status is presented
**Then** the player sees only the factual quest or request state and supported recovery path
**And** timing, error text, placeholders, or partial reward UI do not reveal whether a condition exists or nearly qualified.

**Given** mechanics commit but notification presentation fails
**When** presentation recovery runs
**Then** the exact approved line and committed reward can be safely redisplayed from authoritative records
**And** recovery cannot rerun evaluation, alter the reward, or expose private reasoning.

**Given** notification delivery is retried, saved, loaded, or revisited
**When** its history is displayed
**Then** the exact text, System attribution, reward details, source quest, and delivery state remain consistent
**And** no duplicate notification or reward is appended.

**Given** the hidden-bonus notification is used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the exact notice and reward are presented
**Then** System attribution, the approved line, and reward details have readable labels and sensible focus and reading order
**And** no private information leaks through hidden text, accessible descriptions, focus targets, color, animation, sound, or layout.

**Given** Story 10.5 automated evidence
**When** integration, serialization, security-boundary, and browser tests run
**Then** all three reward presentations, System and organic quests, the exact approved line, model-context separation, Rowan and NPC responses, API and accessibility redaction, failure recovery, duplicate delivery, and save/load are verified against the real application and SQLite store
**And** tests prove that conditions and evaluator reasoning never enter ordinary player projections or narration.

### Story 10.6: Complete a Quest Without a Hidden Bonus

As a player,
I want ordinary and nonqualifying quest outcomes to resolve without arbitrary extra rewards,
So that hidden bonuses remain meaningful rather than becoming routine payouts.

**Acceptance Criteria:**

**Given** a P8 quest is completed through its routine visible fulfillment path
**When** the private condition is evaluated at its fixed point
**Then** routine completion alone does not satisfy the unusual-approach requirement
**And** the quest grants only its ordinary declared rewards.

**Given** committed evidence does not satisfy the private condition
**When** bounded evaluation returns a valid not-satisfied decision
**Then** the private evaluation result commits with the ordinary quest resolution
**And** no hidden XP, extra draw, Common item, hidden-bonus claim, or bonus notification is created.

**Given** the evaluator incorrectly proposes satisfaction from routine, unrelated, fabricated, stale, cross-branch, or post-evaluation evidence
**When** deterministic validation runs
**Then** the false-positive proposal is rejected
**And** no hidden reward can commit until a valid evaluation result is available at the atomic resolution boundary.

**Given** the player performs some behavior described by the private condition but does not complete the quest’s visible success contract
**When** the quest remains partial, fails, is abandoned, or expires
**Then** no hidden bonus is paid
**And** ordinary committed actions and consequences remain intact without being rewritten as quest completion.

**Given** a daily quest expires without qualifying completion
**When** the 06:00 refresh commits
**Then** the quest receives neither its ordinary reward nor its hidden reward
**And** expiry imposes no penalty and provides no hint about the missed condition.

**Given** an organic quest fails, expires, is abandoned, or is renegotiated away from its fixed evaluated contract
**When** resolution occurs
**Then** no hidden bonus is paid for the unresolved original quest
**And** a new supported quest can receive only its own newly created private condition.

**Given** qualifying-looking evidence occurs after the recorded evaluation point
**When** the resolved quest is inspected or replayed
**Then** the prior evaluation is not reopened and no retroactive bonus is created
**And** later events remain eligible only for their own applicable quests and conditions.

**Given** an untriggered quest resolution is retried or reevaluated
**When** idempotent recovery runs
**Then** the prior validated not-satisfied result and ordinary reward state are returned
**And** no new evaluator version, evidence set, seed, reward type, or bonus claim is substituted.

**Given** the player asks whether an untriggered quest had a condition or what was missed
**When** System, Rowan, NPC, narrator, journal, or award presentation responds
**Then** it does not reveal, confirm, deny, or hint at the private condition or evaluator reasoning
**And** no absent-notification placeholder, near-miss message, progress indicator, or checklist is shown.

**Given** evaluation is malformed, unavailable, or interrupted before atomic quest resolution
**When** recovery is presented
**Then** the operation remains visibly pending or interrupted and can retry against the same private definition and committed evidence
**And** the system does not guess a result, silently skip required evaluation, partially grant ordinary rewards, or leak why evaluation failed.

**Given** presentation fails after a nonqualifying resolution commits
**When** recovery runs
**Then** the ordinary quest result and declared rewards can be redisplayed
**And** recovery does not add a bonus notice or reveal that a private evaluation occurred.

**Given** an untriggered quest is saved, loaded, or mechanically replayed
**When** its state is recovered
**Then** condition and evaluator versions, evaluation point, evidence references, private not-satisfied result, ordinary rewards, and absence of a bonus claim remain consistent
**And** the same recorded inputs reproduce the same non-award decision.

**Given** an untriggered or expired quest result is used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** its ordinary state and rewards are displayed
**Then** they remain readable and operable under the existing quest UX contract
**And** no private-condition clue leaks through text, accessibility metadata, focus order, spacing, color, animation, sound, or timing-dependent content.

**Given** Story 10.6 automated evidence
**When** integration and browser tests run
**Then** routine completion, unrelated and false-positive evidence, partial and expired System quests, failed and renegotiated organic quests, post-evaluation events, duplicate resolution, evaluator failure, recovery, replay, save/load, and projection secrecy are verified against the real application and SQLite store
**And** tests prove that ordinary paths never receive or imply an uncommitted hidden bonus.

### Story 10.7: Verify the P8 Hidden-Bonus Gate

As a playtester,
I want to exercise qualifying and nonqualifying hidden conditions across supported quests,
So that combat is considered only after surprise rewards are bounded, causal, and genuinely private.

**Acceptance Criteria:**

**Given** an authorized P8 build, its phase-specific UX contract, and controlled starting states
**When** P8 content and stage boundaries are validated
**Then** newly created supported System and organic quests each receive exactly one private hidden condition and one seeded bounded reward
**And** combat quests, combat content, multiple conditions per quest, visible bonus objectives, and retroactive conditions on pre-P8 quests remain absent.

**Given** controlled seeds spanning the hidden reward-type selection
**When** P8 quests are created
**Then** XP, extra draw, and Common item are selected uniformly, XP values cover the inclusive 10 and 25 boundaries, and item selection covers all four Common entries uniformly
**And** every selected reward, condition, evaluation point, evaluator version, eligible set, and random result remains stable for replay.

**Given** at least three qualifying quests split across System and organic sources
**When** one condition of each reward type is satisfied through committed unusual-approach evidence
**Then** the fixed XP, extra-draw, and Common-item rewards each commit exactly once with their ordinary quest resolution
**And** ordinary and hidden rewards remain separate, conserved, bounded claims.

**Given** the three triggered fixtures
**When** their reward records are inspected
**Then** XP applies the same seeded 10–25 amount to player and named-skill tracks, draw creates exactly one G20 entitlement, and item awards only its preselected Common entry worth at most 5 gold
**And** no evaluator confidence, prose, difficulty, or later event changes the fixed reward.

**Given** at least three non-triggering quests split across System and organic sources
**When** routine completion, partial or expired fulfillment, unrelated evidence, and failed or renegotiated outcomes are evaluated
**Then** no hidden XP, draw, item, claim, or bonus notification is created
**And** ordinary valid outcomes and declared rewards remain intact without penalty or retroactive reinterpretation.

**Given** valid, false-positive, malformed, stale-version, fabricated-evidence, cross-branch, and post-evaluation judgment proposals
**When** deterministic validation runs
**Then** only a proposal supported by the correct committed evidence and fixed condition can authorize its preselected reward
**And** invalid evaluation cannot partially complete the quest, alter ordinary rewards, substitute a reward, or leak private reasoning.

**Given** every triggered quest’s notification is inspected
**When** player-facing presentation is rendered
**Then** it begins exactly `HIDDEN CONDITION SATISFIED — Bonus acquired.` and is followed only by the committed reward
**And** condition text, evidence requirements, evaluator reasoning, confidence, alternative approaches, and missed conditions remain undisclosed.

**Given** triggered and untriggered quests are inspected before and after resolution
**When** journal, transcript, API, browser state, accessibility tree, narration context, Rowan context, NPC context, and ordinary telemetry are examined
**Then** private records and reasoning remain absent from every ordinary player projection and unrelated model context
**And** only capability-gated diagnostics can inspect them.

**Given** a player completes one hidden condition through an unplanned but supported approach
**When** the fixed evidence contract is evaluated
**Then** the approach can qualify when committed evidence genuinely satisfies it
**And** novelty alone, unsupported action, persuasive description, or difference from the fixture route cannot earn a bonus.

**Given** one failure or interruption is introduced during migration, condition creation, evaluation, ordinary resolution, each reward type, and notification presentation
**When** recovery and safe retry are exercised
**Then** every commit boundary remains identifiable and unfinished work can resume against the same versions, seed, condition, and evidence
**And** no quest, ordinary reward, hidden claim, XP, entitlement, item, evaluation, or notification is lost, changed, or duplicated.

**Given** branches are saved before creation, before evaluation, during recoverable evaluation, after qualifying resolution, and after nonqualifying resolution
**When** each branch is loaded and continued
**Then** private conditions, versions, seeds, evaluation points, evidence references, decisions, claims, rewards, and notification state restore exactly
**And** loading cannot reseed, reevaluate a resolved quest, reveal a condition, or pay a second bonus.

**Given** the same captured state, content versions, private definitions, evaluator proposals, and recorded random inputs
**When** mechanical replay is run
**Then** condition creation, reward selection, validation decisions, ordinary rewards, hidden rewards, and state hashes reproduce exactly
**And** regenerated prose cannot change eligibility, reasoning visibility, reward type, amount, or item.

**Given** P8 journeys are tested with keyboard, pointer, screen reader, 200% zoom, and 320-pixel reflow
**When** ordinary quests, qualifying rewards, nonqualifying outcomes, mixed-source notices, errors, and recovery are exercised
**Then** visible contracts, ordinary states, exact success notices, reward details, and operation status remain readable and operable
**And** no private information leaks through text, metadata, focus, spacing, color, animation, sound, timing, or horizontal scrolling.

**Given** P8 playtest sessions
**When** feedback is recorded
**Then** evidence separately captures whether triggered rewards felt earned or arbitrary, whether untriggered outcomes felt fair, whether secrecy encouraged experimentation or confusion, and what the player wants next
**And** mechanical correctness is not treated as proof that opaque rewards improve play.

**Given** a missing or duplicate private condition, routine over-award, unbounded reward, invalid evidence acceptance, duplicate claim, trigger disclosure, near-miss hint, context leak, conservation error, or save/load failure
**When** the P8 gate is evaluated
**Then** the affected scenario fails and is corrected and repeated
**And** P9 remains unauthorized.

**Given** all P8 evidence passes
**When** Epic 10 closes
**Then** P8 is marked eligible for a separate P9 authorization decision
**And** the bounded combat encounter remains unavailable until P9 is explicitly authorized.

## Epic 11: Resolve a Bounded Combat Encounter

Players can fight, flee, surrender, or accept surrender in one readable authored encounter while established resources, effects, positioning, items, time, death, rewards, and persistence remain authoritative.

### Story 11.1: Enter and Read the Road-Robber Encounter

As a player,
I want to enter the authored combat encounter and understand its state,
So that I can act through free text without needing a tactical map or hidden combat rules.

**Acceptance Criteria:**

**Given** the P8 evidence gate has not passed, P9 has not been separately authorized, or no P9-specific UX contract is approved
**When** a P9 upgrade or combat encounter is requested
**Then** P9 combat state, content, and interface remain unavailable
**And** the existing P8 branch remains unchanged.

**Given** an eligible P8 build is upgraded to P9
**When** migration runs
**Then** it validates the immediately preceding ruleset and content versions and records the P9 stage atomically
**And** existing campaign, quest, reward, inventory, progression, spell, effect, and clock state is preserved.

**Given** the controlled P9 fixture is created
**When** its branch is inspected
**Then** it is separate from the live campaign and cannot transfer fixture statistics, equipment, spells, resources, XP, or outcomes into that campaign
**And** creating, playing, resetting, or loading the fixture does not mutate the live branch.

**Given** the controlled player fixture is initialized
**When** its authoritative state is inspected
**Then** it has Body 12, Agility 13, Constitution 14, Mind 10, Presence 8; Health 168/168, Mana 120/120, Stamina 182/182; and Arcana, Melee, and Ranged +0
**And** it has no armor, owns a sword and bow, and has Ember + Fellowship with Hearthspark and Cinder Lance occupying the two Ember slots and no Rest-stone spell.

**Given** the authored road robber is initialized
**When** its authoritative state is inspected
**Then** it has Body 12, Agility 10, Constitution 10, Mind 8, Presence 10; Melee +1; Defense 10; Health 120, Mana 96, and Stamina 100
**And** it owns one sword with fixed 9-damage output and no undeclared armor, allies, abilities, loot, or resources.

**Given** the encounter begins
**When** both actors enter the authored encounter space
**Then** they start exactly 10 m apart with stable positions, legal known targets, and legal exits
**And** no procedural enemy, map, equipment set, or additional encounter content is generated.

**Given** combat initiative begins
**When** initiative is rolled
**Then** each actor rolls once using `d20 + Agility modifier`, with ties resolved first by higher raw Agility and then in favor of the player
**And** both rolls, modifiers, tie-break evidence, and final order are recorded without granting check XP.

**Given** initiative has committed
**When** combat starts or its state is revisited
**Then** the same initiative order remains in force for the encounter
**And** narration, retries, round transitions, or interface refreshes cannot reroll or reorder it.

**Given** the active combat state is displayed
**When** the player inspects it
**Then** the round, active actor, initiative order, positions and separation, current and Effective Maximum Health, Mana and Stamina, Defense, known active effects, legal targets, known exits, and committed prior results are readable
**And** the display identifies that each round represents six fictional seconds.

**Given** the player asks what is currently legal
**When** factual combat guidance is shown
**Then** it identifies applicable movement, attack, cast, item, defend, sprint, escape, and surrender categories with their known targets and costs
**And** it does not provide recommended tactics, action chips, generated reply choices, or claims that an unaffordable or out-of-range action is legal.

**Given** fixture creation, encounter entry, or initiative fails before commit
**When** recovery is offered
**Then** no partial actor, position, combat clock, initiative result, or P9 state is exposed
**And** the prior readable branch remains intact.

**Given** encounter entry or initiative is retried, interrupted, saved, loaded, or mechanically replayed
**When** state is recovered
**Then** actor identities, statistics, equipment, spells, starting positions, random evidence, initiative order, stage version, and encounter identity restore consistently
**And** no second opponent, item, roll, or combat instance is created.

**Given** combat status is inspected with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** initiative, actors, positions, pools, effects, actions, targets, and exits are displayed
**Then** each has a readable label, sensible reading order, and visible focus without requiring a tactical map
**And** no essential distinction depends only on color, hover, animation, sound, or horizontal scrolling.

**Given** Story 11.1 automated evidence
**When** integration and browser tests run
**Then** P9 gating, adjacent-version migration, live-fixture isolation, both exact actor fixtures, derived pools and Defense, 10 m start, initiative and both tie-breaks, stable order, readable state, invalid entry, idempotency, replay, and save/load are verified against the real application and SQLite store
**And** first-party migration, encounter, random, character, projection, and persistence behavior is not mocked.

### Story 11.2: Move, Sprint, and Defend in Combat

As a player,
I want movement and defensive turns to follow clear costs and limits,
So that positioning and protection remain tactical without becoming a separate rules system.

**Acceptance Criteria:**

**Given** an actor begins an active combat turn
**When** their available turn economy is inspected
**Then** they may take up to one ordinary movement component of no more than 8 m and one action
**And** unused movement or actions do not carry into a later turn.

**Given** an actor has at least 5 Stamina and chooses a legal ordinary move of up to 8 m
**When** movement commits
**Then** exactly 5 Stamina is spent and the actor’s position and separation from the opponent are updated atomically
**And** no additional action is consumed by that ordinary movement.

**Given** an actor has at least 10 Stamina and chooses sprint as their action
**When** the sprint commits
**Then** exactly 10 Stamina is spent and the actor moves no more than 34 m along a legal path
**And** sprint consumes the turn’s action while preserving only any separately unused ordinary movement allowed that turn.

**Given** an actor combines ordinary movement and sprint during one turn
**When** both components commit
**Then** each component obeys its own distance cap and the actor pays the full combined 15 Stamina
**And** the final position, traversed path, separation, movement evidence, and spent resources are recorded in turn order.

**Given** an actor has at least 5 Stamina and chooses defend as their action
**When** defend commits
**Then** exactly 5 Stamina is spent and the actor receives +2 Defense until the start of their next turn
**And** the modifier is stored as an ordinary timed combat effect without changing raw Agility or armor.

**Given** a defending actor is attacked before their next turn
**When** Defense is calculated
**Then** the temporary +2 is added to `10 + Agility modifier + armor bonus`
**And** all contributing sources and the resulting Defense are inspectable.

**Given** the defending actor’s next turn begins
**When** turn-start effects resolve
**Then** the prior defend modifier expires before new turn choices resolve
**And** defending again creates one fresh +2 effect rather than stacking with the expired or duplicate application.

**Given** an actor requests movement beyond 8 m, sprint beyond 34 m, movement through an illegal path, a second action, or an action outside their turn
**When** validation runs
**Then** the request is rejected with a specific reason
**And** position, separation, Stamina, action economy, effects, and fictional time remain unchanged.

**Given** an actor lacks the full 5 Stamina for movement or defend, or the full 10 Stamina for sprint
**When** the action is attempted
**Then** it is rejected before the actor moves or gains Defense
**And** no partial Stamina, action, position, effect, or fictional time is committed.

**Given** an actor reaches 0 Stamina
**When** further combat options are evaluated
**Then** movement and Stamina-costing actions are unavailable while applicable zero-Stamina options from the existing resource rules remain usable
**And** zero Stamina does not itself cause Health loss, unconsciousness, or death.

**Given** both actors complete their turns without a terminal outcome
**When** the round closes
**Then** the encounter clock advances exactly six fictional seconds and the next round begins with the established initiative order
**And** individual turn narration or retries do not add extra time.

**Given** the road robber moves, sprints, or defends
**When** the opponent turn resolves
**Then** the same distance limits, action economy, Stamina payments, Defense effect, and rejection rules apply
**And** NPC narration cannot bypass costs or positions.

**Given** movement or defense fails before atomic commit or presentation fails afterward
**When** recovery runs
**Then** either no position, Stamina, action, effect, or time committed, or the complete authoritative result can be redisplayed
**And** retrying cannot move, defend, spend resources, or close a round twice.

**Given** combat is saved, loaded, interrupted, retried, or mechanically replayed during movement or defense
**When** state is recovered
**Then** active actor, remaining turn economy, positions, separation, Stamina, defend duration, round, clock, and operation result restore consistently
**And** no movement component, action, effect expiry, or six-second interval is skipped or duplicated.

**Given** movement and defense are used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** costs, limits, positions, turn economy, Defense, validation, and results are displayed
**Then** each has a readable label and clear status without requiring a tactical map
**And** legal state or committed movement is not conveyed only through color, hover, animation, sound, or horizontal scrolling.

**Given** Story 11.2 automated evidence
**When** integration and browser tests run
**Then** player and robber movement, sprint, combined movement, defend, effect expiry, exact Stamina boundaries, invalid and out-of-turn actions, zero Stamina, six-second rounds, atomicity, idempotency, replay, and save/load are verified against the real application and SQLite store
**And** first-party encounter, resource, effect, scheduler, transaction, and persistence behavior is not mocked.

### Story 11.3: Make Mundane Combat Attacks

As a player,
I want unarmed, sword, and bow attacks to use familiar checks and resources,
So that combat outcomes remain understandable and consistent with ordinary uncertain actions.

**Acceptance Criteria:**

**Given** the controlled player inspects their mundane attacks
**When** the attack contracts are displayed
**Then** unarmed and sword attacks use `Body modifier + Melee`, bow attacks use `Agility modifier + Ranged`, and every attack costs 5 Stamina and the turn’s action
**And** the controlled player’s attack bonuses are +1 for each of the three attacks.

**Given** the controlled player’s damage is inspected
**When** fixed damage is calculated
**Then** unarmed deals 5, sword deals 9, and bow deals 9 Health damage on a hit
**And** those results come from the approved formulas with a minimum of 1 rather than generated narration.

**Given** the road robber makes a sword attack
**When** its contract is inspected or resolved
**Then** the attack uses `Body modifier + Melee` for a total +2 attack bonus, costs 5 Stamina, and deals exactly 9 Health damage on a hit
**And** the robber follows the same action, range, Defense, roll, payment, and transaction rules as the player.

**Given** an actor has at least 5 Stamina, owns or can use the selected attack, has an eligible target in its supported range, and has an unused action
**When** the attack commits
**Then** exactly 5 Stamina is spent and one d20 attack roll is resolved against `10 + target Agility modifier + target armor bonus` plus any active Defense effect
**And** the roll, modifiers, pre-roll success probability, target Defense, resource payment, and action use are recorded atomically.

**Given** an attack roll is a natural 20
**When** the result is evaluated
**Then** it succeeds at the admitted attack stakes
**And** it does not add undeclared critical damage, effects, movement, or loot.

**Given** an attack roll is a natural 1
**When** the result is evaluated
**Then** it fails without dealing damage
**And** it does not create an undeclared fumble effect, self-damage, dropped weapon, or extra action.

**Given** the final attack total meets or exceeds the target’s Defense without a natural-1 override
**When** the hit resolves
**Then** the attack’s fixed damage reduces current Health, capped at a minimum of 0
**And** armor and defend modify Defense only and do not reduce damage after a hit.

**Given** the attack misses
**When** the committed action resolves
**Then** no attack damage is applied while the 5 Stamina cost and action use remain spent
**And** fictional results cannot convert the miss into a hit or refund its cost.

**Given** the controlled player succeeds on a meaningful attack
**When** G18 progression resolves
**Then** XP calculated from the recorded pre-roll success probability is awarded once to the player track and the applicable Melee or Ranged track
**And** unarmed and sword attacks use Melee while bow uses Ranged.

**Given** the controlled player misses, succeeds at a 95% success probability, or replays an already resolved attack
**When** XP eligibility is evaluated
**Then** that result grants zero new attack XP
**And** combat creates no separate encounter-completion XP or retry-based XP opportunity.

**Given** the actor lacks 5 Stamina, does not own or support the selected weapon, targets an ineligible or out-of-range actor, acts outside their turn, has already spent their action, or targets a dead or absent actor
**When** validation runs
**Then** the attack is rejected before rolling
**And** Stamina, Health, position, action economy, random state, XP, and fictional time remain unchanged.

**Given** the player fires the authored bow
**When** its attack resolves
**Then** it uses the fixed bow contract and ordinary inventory ownership
**And** no undeclared ammunition count, reload action, range modifier, or generated weapon property is introduced.

**Given** attack resolution fails before atomic commit or presentation fails afterward
**When** recovery runs
**Then** either no Stamina, action, roll, damage, or XP committed, or the complete authoritative result can be redisplayed
**And** retrying cannot reroll, damage, spend, or award XP twice.

**Given** combat is saved, loaded, interrupted, retried, or mechanically replayed before or after an attack
**When** state is recovered
**Then** attacker, target, weapon, range state, Defense, Stamina, random evidence, damage, Health, action use, and XP source restore consistently
**And** the same resolved attack cannot change its roll or apply its consequences twice.

**Given** attacks are used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** attacker, target, range, cost, roll, Defense, hit or miss, damage, pools, and XP are displayed
**Then** each has a readable label and clear committed-or-rejected status without requiring a tactical map
**And** no essential result depends only on color, hover, animation, sound, or horizontal scrolling.

**Given** Story 11.3 automated evidence
**When** integration and browser tests run
**Then** player unarmed, sword, and bow attacks, robber sword attacks, exact bonuses and damage, Defense and defend, natural 1 and 20, hits and misses, Stamina rejection, range and ownership validation, G18 XP, atomicity, idempotency, replay, and save/load are verified against the real application and SQLite store
**And** first-party encounter, check, resource, Health, progression, transaction, and persistence behavior is not mocked.

### Story 11.4: Cast Cinder Lance and Utility Magic

As a player,
I want combat spells to retain their declared costs and effects,
So that entering combat does not secretly rewrite how my magic works.

**Acceptance Criteria:**

**Given** the controlled player inspects Cinder Lance
**When** its fixed contract is displayed
**Then** it is an Ember-slot spell costing 12 Mana with 10 m range and instantaneous duration, using `Mind modifier + Arcana` as a spell attack
**And** the controlled player has a +0 attack bonus and fixed 12-damage result on a hit.

**Given** the controlled player has at least 12 Mana, an unused action, and the road robber is within 10 m
**When** Cinder Lance commits
**Then** exactly 12 Mana and the turn’s action are spent and one spell attack is resolved against the robber’s current Defense
**And** no Stamina is spent unless a separate active effect explicitly modifies the spell’s cost.

**Given** Cinder Lance meets or exceeds the target’s Defense without a natural-1 override
**When** the hit resolves
**Then** the target loses exactly 12 Health, subject to the ordinary minimum-zero pool rule
**And** no undeclared burning, splash, critical, knockback, wound, or lingering effect is added.

**Given** Cinder Lance misses
**When** the committed cast resolves
**Then** no spell damage is applied while the 12 Mana cost and action remain spent
**And** narration, retries, or disappointment cannot refund Mana or turn the miss into a hit.

**Given** the Cinder Lance roll is a natural 20 or natural 1
**When** natural-roll rules are applied
**Then** natural 20 succeeds and natural 1 fails at the admitted attack stakes
**And** neither result changes the spell’s fixed damage, cost, range, or effect.

**Given** the controlled player succeeds on a meaningful Cinder Lance attack
**When** G18 progression resolves
**Then** XP calculated from the recorded pre-roll probability is awarded once to the player and Arcana tracks
**And** a miss, 95%-success result, or replayed cast grants zero new spell-check XP.

**Given** the caster lacks 12 Mana, the target exceeds 10 m, the target is invalid, the spell or slot is not owned, the action is already spent, or the request occurs outside the caster’s turn
**When** validation runs
**Then** the cast is rejected before rolling
**And** Mana, Health, action economy, random state, XP, positions, and fictional time remain unchanged.

**Given** the controlled player inspects Hearthspark during combat
**When** its contract is displayed
**Then** it retains its 8-Mana cost, 10 m range, 10-minute duration, eligible flame and held-object effects, and Ember-slot ownership
**And** it remains incapable of dealing direct combat damage.

**Given** the player validly casts Hearthspark during combat
**When** its selected effect commits
**Then** the applicable hand-sized nonmagical flame or held object changes according to the existing spell definition and the turn’s action is spent
**And** an attempt to damage the robber, ignite an ineligible target, or create an undeclared combat effect is rejected without cost.

**Given** an eligible P9 branch contains another previously awarded P6 utility spell
**When** that spell is inspected or cast in combat
**Then** its existing owner, slot, cost, target, range, duration, magnitude, daily limit, and effect rules remain authoritative
**And** combat does not add damage, increase rarity, waive prerequisites, or change a standard or Deepened definition.

**Given** a spell creates or maintains a timed utility effect during combat
**When** combat rounds advance
**Then** its duration is tracked by the shared clock and effect scheduler in six-second increments
**And** expiry, proximity, interruption, daily-use, and duplicate behavior remain those of the existing definition.

**Given** a spell has a generated name or manifestation
**When** its combat result is narrated
**Then** the committed presentation may accompany the cast
**And** it cannot change targeting, cost, attack evidence, damage, effect, duration, or slot ownership.

**Given** spell resolution fails before atomic commit or presentation fails afterward
**When** recovery runs
**Then** either no Mana, action, roll, damage, effect, or XP committed, or the complete authoritative result can be redisplayed
**And** retrying cannot reroll, recast, damage, spend Mana, apply an effect, or award XP twice.

**Given** combat is saved, loaded, interrupted, retried, or mechanically replayed before or after a spell
**When** state is recovered
**Then** spell identity, slot, target, range, Mana, action use, random evidence, damage, effects, duration, limits, XP, and result restore consistently
**And** the same cast cannot change its outcome or apply consequences twice.

**Given** combat magic is used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** spell terms, target, range, cost, roll, Defense, result, effect, duration, pools, and XP are displayed
**Then** each has a readable label and clear committed-or-rejected status without requiring a tactical map
**And** no essential result depends only on color, hover, animation, sound, or horizontal scrolling.

**Given** Story 11.4 automated evidence
**When** integration and browser tests run
**Then** Cinder Lance hits, misses, natural rolls, exact Mana and damage, range and ownership rejection, Arcana XP, Hearthspark’s valid uses and damage prohibition, inherited P6 utility spells, duration tracking, atomicity, idempotency, replay, and save/load are verified against the real application and SQLite store
**And** first-party encounter, spell, check, resource, effect, progression, transaction, and persistence behavior is not mocked.

### Story 11.5: Use Items and Resolve Combat Effects, Death, and Revival

As a player,
I want combat to reuse existing items, conditions, death, and recovery rules,
So that the encounter does not create exceptions to consequences already established in the world.

**Acceptance Criteria:**

**Given** an isolated combat subfixture supplies a previously established item, wound, or effect
**When** the fixture is created
**Then** the supplied record retains its stable definition, ownership, uses, duration, source, and mechanics
**And** it does not alter the authored combatants, live campaign, base encounter loot, or unrelated inventory.

**Given** an actor owns a suitable usable item and has an unused action
**When** item use commits during their turn
**Then** the turn’s action and the item’s declared quantity or use are spent atomically with its effect
**And** ordinary item use spends no Stamina unless the item or an active effect explicitly declares a cost.

**Given** a Healing Draft, Mana Draft, Restorative Elixir, or another supported recovery item is used in combat
**When** its effect resolves
**Then** it restores the declared percentage of the target’s current Effective Maximum, rounded as defined and capped at that maximum, and applies only its declared wound treatment
**And** combat does not increase healing, remove an undeclared wound, revive a dead target, or refund the item.

**Given** a poison is validly applied to a weapon during combat
**When** application commits
**Then** the item-use action, poison consumption, coating identity, trigger, duration, and weapon state follow the existing G19 and shared-effect rules
**And** the coating persists until its declared contact, cleaning, or expiry condition rather than disappearing at turn end.

**Given** a poisoned or otherwise effect-bearing attack makes qualifying contact
**When** the hit commits
**Then** weapon damage and the linked effect resolve through the ordinary damage and effect contracts in deterministic event order
**And** the same contact cannot consume a coating, apply a condition, tick damage, or award XP twice.

**Given** Sharpened, Bleeding, a wound penalty, or another supported effect is active during combat
**When** an applicable action, tick, treatment, or expiry occurs
**Then** magnitude, duration, charges, duplicate behavior, removal category, and player knowledge remain those of the stable effect definition
**And** six-second rounds use the shared scheduler and same-timestamp ordering rather than a combat-only timer.

**Given** simultaneous combat damage, healing, treatment, effect ticks, or expirations share a timestamp
**When** they resolve
**Then** completed actions resolve first, scheduled ticks follow in stable creation order, expirations follow, and pools and terminal states are recalculated last
**And** narration cannot reorder events to prevent or create damage, healing, removal, or death.

**Given** an actor’s current Health reaches 0
**When** terminal state is evaluated
**Then** the actor dies immediately and can no longer take combat turns or actions
**And** no Downed state, stabilization interval, automatic recovery, or undeclared death save is created.

**Given** the player dies in the controlled encounter
**When** defeat recovery is presented
**Then** a manual save can be selected and loaded under the existing branch rules
**And** the default mode does not forcibly delete the save or convert death into an uncommitted survival outcome.

**Given** an eligible actor administers a Draught of Revival within 120 seconds of a recorded death
**When** revival commits
**Then** the item is consumed and the dead target returns once for that death event at 25% of Effective Maximum Health
**And** Severe Wounds remain and no unrelated Health, Mana, Stamina, item, effect, XP, loot, or reward is restored.

**Given** Draught administration completes exactly at the 120-second boundary
**When** same-timestamp ordering resolves
**Then** the completed revival action is applied before the revival window expires
**And** the target returns under the fixed Draught contract.

**Given** revival is attempted after 120 seconds, without an eligible item or administrator, on a living target, or a second time for the same death event
**When** validation runs
**Then** the request is rejected before item consumption
**And** death state, inventory, pools, effects, encounter outcome, and fictional time remain unchanged.

**Given** an item or effect request uses an invalid target, unavailable item, exhausted use, incompatible removal category, stale state, or already spent action
**When** validation runs
**Then** it is rejected with a specific reason
**And** inventory, effects, wounds, pools, action economy, scheduler, and fictional time remain unchanged.

**Given** item, effect, death, or revival resolution fails before atomic commit or presentation fails afterward
**When** recovery runs
**Then** either no action, item, effect, pool, terminal state, or time committed, or the complete authoritative result can be redisplayed
**And** retrying cannot consume, apply, tick, kill, revive, heal, or reward twice.

**Given** combat is saved, loaded, interrupted, retried, or mechanically replayed around item use, effect timing, death, or revival
**When** state is recovered
**Then** ownership, quantities, actions, effect instances, charges, ticks, wounds, pools, death time, revival window, terminal state, and operation result restore consistently
**And** no scheduled or transactional consequence is skipped, rerolled, or duplicated.

**Given** combat items, effects, death, and revival are used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** ownership, targets, costs, effects, durations, wounds, pools, death, recovery, and validation are displayed
**Then** each has a readable label, exact status, and sensible reading order without requiring a tactical map
**And** no essential condition or timing boundary depends only on color, hover, animation, sound, or horizontal scrolling.

**Given** Story 11.5 automated evidence
**When** integration and browser tests run
**Then** recovery items, poison application and contact, Sharpened, Bleeding, wounds and treatments, shared scheduling, immediate death, manual-save recovery, revival before, at, and after 120 seconds, invalid uses, atomicity, idempotency, replay, and save/load are verified against the real application and SQLite store
**And** first-party encounter, inventory, item, effect, resource, scheduler, death, transaction, and persistence behavior is not mocked.

### Story 11.6: Escape the Road-Robber Encounter

As a player,
I want to create enough distance and flee,
So that survival is a valid outcome even when I do not defeat the robber.

**Acceptance Criteria:**

**Given** the encounter is active
**When** escape requirements are inspected
**Then** an actor must reach strictly more than 20 m separation, retain an unused action, and pay 10 Stamina to flee
**And** escape requires no attack roll, completion XP, purse transfer, or undeclared check.

**Given** the player begins their turn at more than 20 m separation with at least 10 Stamina
**When** they use their action to flee
**Then** exactly 10 Stamina and the action are spent and the encounter ends with the player-escape outcome
**And** the player receives no robber purse or separate encounter-completion XP.

**Given** the player begins within 20 m but can cross the threshold using legal ordinary movement
**When** they move to more than 20 m and then flee during the same turn
**Then** both the 5-Stamina movement and 10-Stamina escape costs commit with the final position and outcome
**And** the action is legal only if the player can pay the full combined cost and has not already spent it.

**Given** the player uses sprint to reach more than 20 m separation
**When** that sprint commits
**Then** the player reaches the recorded position but has spent the turn’s action
**And** they cannot flee until a later turn unless another rule explicitly grants an action.

**Given** the separation is exactly 20 m or less, the actor lacks 10 Stamina, the action is already spent, it is not their turn, or the encounter has ended
**When** flee is requested
**Then** the request is rejected with a specific reason
**And** Stamina, position, action economy, encounter outcome, rewards, and fictional time remain unchanged.

**Given** the player validly flees
**When** the terminal outcome commits
**Then** both actors’ final positions, current pools, inventory, equipment, wounds, effects, and elapsed combat time persist
**And** escape does not clear effects, heal damage, restore resources, invent pursuit damage, or transfer gold.

**Given** the player earned meaningful-check XP before escaping
**When** the encounter ends
**Then** that already committed XP remains recorded
**And** escape neither revokes it nor grants another XP award.

**Given** the road robber reaches more than 20 m separation and validly uses a flee action in a supported branch
**When** the action commits
**Then** the same 10-Stamina cost and escape rules apply
**And** narration cannot let the robber leave without paying the action and resource cost.

**Given** the escape outcome has committed
**When** another movement, attack, spell, item, surrender, or flee command targets that encounter
**Then** the request is rejected because combat is terminal
**And** no extra turn, round, cost, roll, damage, transfer, XP, or reward is created.

**Given** escape resolution fails before atomic commit or presentation fails afterward
**When** recovery runs
**Then** either no Stamina, action, position, outcome, or time committed, or the complete authoritative escape result can be redisplayed
**And** retrying cannot charge, move, terminate, or record the outcome twice.

**Given** combat is saved, loaded, interrupted, retried, or mechanically replayed before or after escape
**When** state is recovered
**Then** separation, positions, turn economy, Stamina, elapsed rounds, active effects, terminal outcome, absence of purse, and prior XP restore consistently
**And** loading cannot reopen the encounter, rerun escape, or create a reward.

**Given** escape is used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** separation, threshold, cost, action availability, rejection, and terminal outcome are displayed
**Then** each has a readable label and clear status without requiring a tactical map
**And** threshold or outcome is not conveyed only through color, hover, animation, sound, or horizontal scrolling.

**Given** Story 11.6 automated evidence
**When** integration and browser tests run
**Then** separation below, at, and above 20 m, move-then-flee, sprint action use, exact Stamina boundaries, player and robber escape, no-purse and no-completion-XP outcomes, terminal rejection, atomicity, idempotency, replay, and save/load are verified against the real application and SQLite store
**And** first-party encounter, movement, resource, outcome, reward, transaction, and persistence behavior is not mocked.

### Story 11.7: Surrender to the Road Robber

As a player,
I want to surrender and survive at a bounded cost,
So that ending the fight without victory remains a clear, consequential choice.

**Acceptance Criteria:**

**Given** the encounter is active and the player has an unused action
**When** surrender is interpreted before commitment
**Then** the player is shown that offering surrender spends the action, normally causes the robber to take up to 5 owned gold and leave, and awards no purse or completion XP
**And** previewing, clarifying, or cancelling changes no action, resource, ownership, outcome, or fictional time.

**Given** the controlled fixture contains no prior event that changes the robber’s behavior
**When** the player explicitly offers surrender on their turn
**Then** the robber accepts without a check and the offer consumes the player’s action
**And** no Stamina, Mana, attack roll, persuasion roll, or undeclared condition is required.

**Given** the player owns at least 5 gold when surrender is accepted
**When** the surrender transaction commits
**Then** exactly 5 gold transfers from the player to the road robber and the robber leaves
**And** the encounter ends with the player-surrender outcome.

**Given** the player owns between 1 and 4 gold when surrender is accepted
**When** the surrender transaction commits
**Then** all owned gold transfers to the road robber without creating a negative balance
**And** the encounter ends with no additional item or resource loss.

**Given** the player owns no gold when surrender is accepted
**When** the surrender transaction commits
**Then** the robber takes 0 gold and leaves
**And** surrender still ends the encounter without fabricating debt, gold, or another penalty.

**Given** surrender is accepted
**When** the terminal outcome is recorded
**Then** the player receives neither the robber’s 5-gold purse nor separate encounter-completion XP
**And** previously earned meaningful-check XP remains intact.

**Given** the player has equipment, consumables, ingredients, quest rewards, or other owned property
**When** surrender resolves
**Then** only up to 5 owned gold transfers under the authored surrender rule
**And** no weapon, item, spell, XP, attribute, relationship, or undeclared resource is confiscated.

**Given** a prior committed event establishes that the robber will not accept the player’s surrender
**When** the player offers surrender
**Then** the refusal follows that recorded fact, the surrender action remains spent, and combat continues
**And** narration alone cannot invent refusal or acceptance, transfer gold, or terminate the encounter.

**Given** accepted surrender commits
**When** post-combat state is inspected
**Then** final positions, Health, Mana, Stamina, wounds, effects, inventory, transferred gold, elapsed combat time, and outcome persist
**And** surrender does not heal, restore, clear effects, or reset either actor.

**Given** the player acts outside their turn, has spent their action, is dead or absent, or targets an already terminal encounter
**When** surrender is requested
**Then** the request is rejected with a specific reason
**And** no action, transfer, outcome, reward, or fictional time changes.

**Given** surrender resolution fails before atomic commit or presentation fails afterward
**When** recovery runs
**Then** either no action, gold transfer, outcome, or time committed, or the complete authoritative surrender result can be redisplayed
**And** retrying cannot spend the action, transfer gold, terminate combat, or record surrender twice.

**Given** combat is saved, loaded, interrupted, retried, or mechanically replayed before or after surrender
**When** state is recovered
**Then** acceptance basis, action use, pre-transfer balance, transferred amount, ownership, terminal outcome, absence of purse, and prior XP restore consistently
**And** loading cannot reopen combat, repeat the transfer, or create a reward.

**Given** surrender is used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** its stakes, confirmation, acceptance or refusal, transfer, and outcome are displayed
**Then** each has a readable label and clear committed-or-rejected status without requiring a tactical map
**And** the cost or outcome is not conveyed only through color, hover, animation, sound, or horizontal scrolling.

**Given** Story 11.7 automated evidence
**When** integration and browser tests run
**Then** preview and cancellation, controlled acceptance, prior-event refusal, balances above, below, and at 5 gold, zero gold, exact ownership transfer, unaffected property, no-purse and no-completion-XP outcomes, terminal rejection, atomicity, idempotency, replay, and save/load are verified against the real application and SQLite store
**And** first-party encounter, ownership, economy, outcome, reward, transaction, and persistence behavior is not mocked.

### Story 11.8: Resolve the Road Robber’s Surrender

As a player,
I want to accept or refuse the wounded robber’s surrender,
So that mercy and continued combat produce distinct, authoritative outcomes.

**Acceptance Criteria:**

**Given** the road robber is alive with Health above 25% of their current Effective Maximum
**When** surrender eligibility is evaluated
**Then** the authored threshold does not require a surrender offer
**And** narration cannot invent an offer, terminal outcome, or purse transfer.

**Given** the base road robber is alive at exactly 30 Health or below
**When** 25% of their 120 Effective Maximum Health is evaluated
**Then** the robber becomes eligible and committed to offer surrender on their next available action
**And** damage, healing, or Effective Maximum changes before that action are reflected by the current authoritative threshold state.

**Given** the road robber reaches 0 Health
**When** terminal state is evaluated
**Then** death resolves immediately rather than producing a surrender offer
**And** the encounter follows the defeat path.

**Given** the eligible road robber begins a turn with an unused action and remains at or below the threshold
**When** their authored behavior resolves
**Then** they spend the action to offer surrender without a check or Stamina cost
**And** the offer’s identity, terms, threshold evidence, action use, and pending player response are recorded.

**Given** a surrender offer is pending
**When** its terms are displayed
**Then** the player is told that accepting ends combat and awards the robber’s one-time 5-gold purse, while refusing continues combat without an immediate purse
**And** the interface does not recommend either response or invent additional loot, punishment, or relationship effects.

**Given** the player explicitly accepts the pending surrender
**When** acceptance commits
**Then** exactly 5 gold transfers from the road robber’s authored purse to the player and the encounter ends with the robber-surrender outcome
**And** the robber remains alive with their current pools, wounds, effects, equipment, and final position.

**Given** the player accepts the robber’s surrender
**When** rewards are evaluated
**Then** no separate encounter-completion XP is granted
**And** meaningful-check XP already earned during combat remains recorded.

**Given** surrender is accepted
**When** ownership is reconciled
**Then** only the authored 5-gold purse transfers unless another separately supported transfer is explicitly committed
**And** the robber’s sword, equipment, remaining property, and undeclared loot do not automatically become player-owned.

**Given** the player explicitly refuses the pending surrender
**When** refusal commits
**Then** no purse transfers, the offer is recorded as refused, and combat continues from the existing positions, pools, effects, round, and initiative order
**And** the robber’s spent surrender action is not restored.

**Given** the robber is healed above the threshold before making an eligible offer
**When** their next action is evaluated
**Then** the threshold-based offer is no longer required
**And** a stale pending eligibility marker cannot force surrender.

**Given** the player tries to accept or refuse without a pending offer, uses a stale offer revision, responds after another terminal outcome, or submits both responses
**When** validation runs
**Then** the request is rejected with a specific reason
**And** ownership, action economy, encounter state, rewards, and fictional time remain unchanged.

**Given** the surrender purse was already awarded or the acceptance request is retried
**When** reward evaluation runs
**Then** the prior terminal outcome and 5-gold transfer are returned
**And** no second purse, completion XP, or reward claim is created.

**Given** offer, acceptance, refusal, or reward resolution fails before atomic commit or presentation fails afterward
**When** recovery runs
**Then** either no action, response, transfer, outcome, or time committed, or the complete authoritative state can be redisplayed
**And** retrying cannot repeat the offer action, response, purse transfer, or terminal outcome.

**Given** combat is saved, loaded, interrupted, retried, or mechanically replayed before or after the surrender offer
**When** state is recovered
**Then** threshold evidence, pending eligibility, action use, offer identity, response state, positions, pools, effects, purse ownership, outcome, and prior XP restore consistently
**And** loading cannot erase a refusal, reopen an accepted surrender, or duplicate its reward.

**Given** robber surrender is used with a keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** threshold status, offer terms, responses, transfer, and outcome are displayed
**Then** each has a readable label and clear pending, accepted, refused, or rejected status without requiring a tactical map
**And** the decision or result is not conveyed only through color, hover, animation, sound, or horizontal scrolling.

**Given** Story 11.8 automated evidence
**When** integration and browser tests run
**Then** Health above, at, and below 30, Effective Maximum changes, death at 0, offer action use, acceptance, refusal, healing before offer, exact purse transfer, retained equipment, no completion XP, invalid and duplicate responses, atomicity, replay, and save/load are verified against the real application and SQLite store
**And** first-party encounter, health, behavior, action, ownership, reward, transaction, and persistence behavior is not mocked.

### Story 11.9: Defeat the Road Robber

As a player,
I want defeating the road robber to resolve combat and its rewards authoritatively,
So that victory remains causal, persistent, and impossible to claim twice.

**Acceptance Criteria:**

**Given** the road robber has Health above 0
**When** a valid attack, spell, item, or scheduled effect reduces their Health to 0
**Then** death resolves immediately and the encounter ends with the robber-defeated outcome
**And** the robber cannot take another turn, surrender, escape, or perform a post-death action.

**Given** an attack, spell, item, or effect deals the defeating damage
**When** the terminal outcome commits
**Then** its resource costs, roll result when applicable, damage, effects, elapsed time, death, and terminal encounter state are recorded together
**And** the final action cannot produce death or rewards without committing its required costs and consequences.

**Given** the road robber is defeated
**When** the authored purse is awarded
**Then** exactly 5 gold transfers from the robber to the player once
**And** the encounter records the transfer and reward claim as part of the defeat outcome.

**Given** the robber possesses a sword, equipment, remaining property, or undeclared belongings
**When** defeat rewards are reconciled
**Then** only the authored 5-gold purse transfers automatically
**And** the robber’s equipment and undeclared loot do not become player-owned.

**Given** the defeating action includes a meaningful check that qualifies under the established XP rules
**When** XP is resolved
**Then** that check can award its ordinary G18 XP exactly once
**And** XP earned from earlier meaningful combat checks remains intact.

**Given** the robber dies from an automatic or scheduled effect without a new meaningful check
**When** XP is resolved
**Then** death itself grants no check XP
**And** no encounter-completion XP is created.

**Given** the robber previously surrendered and their purse was awarded
**When** later state, replay, or revival is evaluated
**Then** defeating that robber cannot award another purse or replace the recorded terminal outcome
**And** reward ownership remains consistent with the prior committed result.

**Given** the robber is revived after a committed defeat
**When** their state becomes active outside the completed encounter
**Then** revival does not restore the spent purse, reopen the completed encounter, or create another defeat reward
**And** their restored Health and continuing state use the established revival rules.

**Given** the defeat outcome has committed
**When** either actor submits another combat action or outcome request
**Then** the request is rejected because the encounter is terminal
**And** no turn, position, pool, effect, time, XP, ownership, or reward state changes.

**Given** the final action, death, purse transfer, XP award, or terminal outcome fails before atomic commit
**When** recovery runs
**Then** none of those dependent consequences remain partially committed
**And** the encounter returns to its last complete authoritative state.

**Given** presentation fails after the defeat transaction commits
**When** the result is retried or redisplayed
**Then** the complete existing action, death, purse, XP, and terminal outcome are returned
**And** no roll, damage, transfer, XP award, or reward claim is repeated.

**Given** combat is saved, loaded, interrupted, retried, or mechanically replayed before or after the defeating action
**When** state is recovered
**Then** final action identity, roll when applicable, costs, damage, effects, death, positions, elapsed time, purse ownership, XP, and terminal outcome restore consistently
**And** loading cannot revive the encounter, reroll the final action, or duplicate its rewards.

**Given** defeat is presented through keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** the final action and outcome are displayed
**Then** death, encounter completion, purse transfer, XP results, and unavailable follow-up actions have readable labels and clear status without requiring a tactical map
**And** the result is not conveyed only through color, hover, animation, sound, or horizontal scrolling.

**Given** Story 11.9 automated evidence
**When** integration and browser tests run
**Then** defeat by attacks, spells, items, and scheduled effects; immediate death; stopped turns; exact purse transfer; retained equipment; qualifying and non-qualifying XP; terminal rejection; revival; atomicity; idempotency; replay; and save/load are verified against the real application and SQLite store
**And** first-party combat, health, death, ownership, reward, XP, transaction, revival, and persistence behavior is not mocked.

### Story 11.10: Save and Resume Mid-Combat

As a player,
I want to save and resume the road-robber encounter mid-combat,
So that continuing later preserves every committed consequence without rerolls or duplicate rewards.

**Acceptance Criteria:**

**Given** the road-robber encounter has started
**When** its first authoritative state is committed
**Then** the encounter receives a stable identity and persistence revision
**And** its fixture identities, initiative result, tie-break evidence, initiative order, starting positions, and starting pools are stored.

**Given** one or more combat turns have partially depleted resources or changed state
**When** a mid-combat save completes
**Then** current Health, Mana, Stamina, Effective Maximums, wounds, active effects, item quantities, equipment, ownership, and gold are stored
**And** restoring the save reproduces those values exactly.

**Given** actors have moved during combat
**When** their positions are saved and loaded
**Then** exact separation, each actor’s position, legal exits, and escape eligibility are restored
**And** loading does not reset either actor to the authored starting distance.

**Given** combat is saved between actions
**When** turn state is restored
**Then** round number, active actor, initiative order, movement used or remaining, action availability, defense status, and six-second round timing resume from the committed state
**And** loading grants no extra move, action, turn, or elapsed time.

**Given** attacks, spells, checks, or item uses have committed
**When** combat is saved and loaded
**Then** action identities, targets, rolls, modifiers, Defense values, costs, damage, healing, effect changes, XP awards, and resulting state remain recorded
**And** no committed roll is regenerated or resolved again.

**Given** a timed effect, wound, defend bonus, or other duration spans the save boundary
**When** combat resumes
**Then** its source, magnitude, remaining duration, next processing point, and prior ticks restore consistently
**And** loading neither skips nor repeats a scheduled consequence.

**Given** a surrender threshold, offer, refusal, or pending response exists
**When** combat is saved and resumed
**Then** the threshold evidence, eligibility, spent action, offer identity, terms, and response state are restored
**And** loading cannot erase a refusal, repeat an offer action, or fabricate a response.

**Given** meaningful combat checks have already awarded XP
**When** the encounter is loaded or replayed
**Then** each award retains its source check and idempotency identity
**And** no prior check awards XP again.

**Given** the robber’s purse has not transferred in the active encounter
**When** combat is saved and resumed
**Then** its ownership and unclaimed reward status remain unchanged
**And** loading alone grants no gold or reward claim.

**Given** escape, player surrender, robber surrender, or robber defeat has committed
**When** that terminal encounter state is saved and loaded
**Then** the exact outcome, final actor states, elapsed time, ownership transfers, XP history, and reward claims are restored
**And** the encounter cannot reopen, select another outcome, or issue another purse.

**Given** the player saves immediately before a random combat resolution
**When** the save is loaded and that unresolved action is later attempted
**Then** only the newly committed attempt receives an authoritative result under the established randomization contract
**And** no uncommitted preview is represented as a prior roll or consequence.

**Given** persistence is requested while a combat transaction is still committing
**When** the save boundary is established
**Then** only the last complete revision or the fully committed new revision is stored
**And** no partial action, cost, damage, effect, transfer, XP award, or outcome appears.

**Given** a stale client submits a combat command after another session has advanced the saved encounter
**When** revision validation runs
**Then** the stale command is rejected and the latest authoritative combat state is returned
**And** no roll, action, cost, time, reward, or state transition is duplicated.

**Given** the saved encounter is missing required state, has an unsupported version, or fails integrity validation
**When** loading is attempted
**Then** resume is rejected with a specific recoverable error rather than inventing defaults or resetting combat
**And** the last valid persisted revision remains unchanged.

**Given** the resumed encounter is presented through keyboard, pointer, screen reader, 200% zoom, or 320-pixel reflow
**When** its restored state is displayed
**Then** round, turn, positions, pools, effects, available actions, prior outcome when terminal, and save status have readable labels without requiring a tactical map
**And** restored or unavailable state is not conveyed only through color, hover, animation, sound, or horizontal scrolling.

**Given** Story 11.10 automated evidence
**When** integration and browser tests run
**Then** initiative, turns, action economy, positions, pools, attacks, rolls, effects, items, XP, purse ownership, surrender state, every terminal outcome, transaction boundaries, stale revisions, invalid saves, and repeated load cycles are verified against the real application and SQLite store
**And** first-party combat, randomization, transaction, reward, and persistence behavior is not mocked.

### Story 11.11: Verify the P9 Combat Gate

As a player,
I want the complete road-robber encounter verified as one coherent experience,
So that every combat outcome is readable, authoritative, and safe to resume.

**Acceptance Criteria:**

**Given** the controlled player and road-robber fixtures
**When** the P9 suite starts the authored encounter through the real application boundary
**Then** the actors begin 10 metres apart with the specified attributes, skills, pools, equipment, spells, Defense, damage, and purse
**And** the suite fails if undeclared fixture state affects the encounter.

**Given** combat begins repeatedly under controlled roll inputs
**When** initiative is resolved
**Then** `d20 + Agility modifier`, higher raw Agility, and finally player-priority tie-breaking are verified
**And** the committed initiative result remains unchanged through redisplay, retry, and save/load.

**Given** representative player and robber turns
**When** movement and action economy are exercised
**Then** 8-metre movement, one action per turn, 34-metre sprinting, legal exits, active actor, round advancement, and six-second round timing are verified
**And** invalid extra movement, actions, and out-of-turn commands are rejected without partial change.

**Given** normal movement, attacks, defending, sprinting, and escape attempts
**When** their Stamina rules are exercised at values below, equal to, and above each cost
**Then** 5-Stamina and 10-Stamina costs commit exactly once for affordable actions
**And** unaffordable actions reject without changing Stamina, position, action economy, or time.

**Given** unarmed, sword, bow, robber-sword, and targeted-spell attacks
**When** hits, misses, minimum damage, range, modifiers, and Defense are exercised
**Then** each action uses the established shared check and damage systems with the authored fixture values
**And** defend’s +2 Defense duration and Cinder Lance’s 12-Mana cost, 10-metre range, and miss cost are verified.

**Given** utility magic, consumable items, wounds, and timed effects are introduced during combat
**When** turns advance
**Then** the encounter delegates their costs, consequences, durations, and scheduled processing to the established systems
**And** combat does not implement a conflicting second version of those mechanics.

**Given** the player reaches 0 Health during representative encounter paths
**When** death and revival timing are exercised
**Then** death is immediate and revival uses the established state, cost, location, time, wound, and effect rules
**And** the dead player cannot act before valid revival completes.

**Given** each authored terminal path is exercised independently
**When** the player escapes, surrenders, accepts the robber’s surrender, or defeats the robber
**Then** all four outcomes produce their specified final states, transfers, and encounter closure
**And** escape grants no purse, player surrender transfers up to 5 owned gold, and robber surrender or defeat transfers the robber’s one-time 5-gold purse.

**Given** meaningful checks and terminal outcomes occur across all four paths
**When** XP and rewards are reconciled
**Then** qualifying checks use the established G18 XP rules and no encounter-completion XP is granted
**And** retries, replay, revival, and repeated loads cannot duplicate XP, gold, loot, transfers, or outcomes.

**Given** the encounter is saved at representative points before initiative, between turns, after movement, after attacks, during effects, during surrender handling, and after every terminal outcome
**When** each save is loaded and play continues
**Then** initiative, rolls, action history, pools, effects, positions, turns, elapsed time, XP, purse ownership, and outcome restore exactly
**And** no committed random result is rerolled and no action or reward is repeated.

**Given** any combat transaction fails before commit or presentation fails after commit
**When** recovery and retry are exercised
**Then** the state remains wholly pre-transaction or exposes the complete committed result
**And** partial costs, damage, effects, time, death, transfers, XP, and outcomes are never observable.

**Given** the full encounter is played without a tactical map
**When** the player reviews the current state and chooses an action
**Then** actor positions, separation, round, active turn, available movement and actions, pools, Defense, effects, surrender state, escape eligibility, and outcomes remain understandable in text and controls
**And** no required combat fact depends on interpreting an unstated spatial layout.

**Given** the P9 experience is operated with keyboard, pointer, and screen reader at default size, 200% zoom, and 320-pixel reflow
**When** every action, validation error, state change, pending decision, and terminal result is exercised
**Then** controls have accessible names, focus remains logical and visible, updates are announced appropriately, and content remains readable without horizontal scrolling
**And** no required distinction relies only on color, hover, animation, or sound.

**Given** P9 evidence is produced
**When** the gate report is assembled
**Then** it traces FR78–FR81 to automated integration and browser scenarios covering initiative, movement, costs, attacks, Defense, Mana, items, effects, death, revival, rewards, XP, six-second rounds, all four exits, and mid-combat persistence
**And** every result identifies its fixture, scenario, assertion, and reproducible test command.

**Given** any required P9 scenario is missing, skipped, flaky, mocked across a first-party boundary, or failing
**When** release readiness is evaluated
**Then** the P9 gate fails with the unmet requirement and evidence gap identified
**And** the encounter cannot be marked production-ready until the real application and SQLite-backed suite passes.
