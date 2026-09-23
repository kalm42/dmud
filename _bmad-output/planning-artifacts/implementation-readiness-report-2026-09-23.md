---
stepsCompleted:
  - step-01-document-discovery
  - step-02-gdd-analysis
  - step-03-epic-coverage-validation
  - step-04-ux-alignment
  - step-05-epic-quality-review
  - step-06-final-assessment
filesIncluded:
  gdd: _bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/gdd.md
  architecture: _bmad-output/game-architecture.md
  epics: _bmad-output/planning-artifacts/epics.md
  ux:
    - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/DESIGN.md
    - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md
  p0Plan: _bmad-output/planning-artifacts/p0-verification-and-exit-plan.md
---

# Implementation Readiness Assessment Report

**Date:** 2026-09-23
**Project:** dmud

## Document discovery

The assessment uses the GDD, the main game architecture, the planning epics, and both UX documents listed in the frontmatter. The P0 verification and exit plan defines the requested scope. The 23-byte planning architecture path is a symlink to the main architecture, not a second version. The GDD-folder epics file is supporting design context, not the authoritative implementation epics. Existing readiness reports dated September 12, 15, and 22 are historical context.

## GDD Analysis

The complete GDD version 0.8 was read. This assessment extracts the requirements effective for **P0**; G01–G02, G09–G14, and G19–G27 describe conditional later stages and are excluded from P0 coverage counts.

### Functional Requirements

| ID | P0 requirement extracted from the GDD |
| --- | --- |
| FR1 | The opening offers New Game and Continue. Continue opens a three-slot selector when saves exist; otherwise it stays visible but unavailable with an explanation. Save-index failure offers retry without blocking New Game. |
| FR2 | New Game starts a zero-fictional-time Session 0. Rowan asks for the player character's name, origin, cares, hates, especially cool ideas, and campaign hopes; suggestions are given only on request. |
| FR3 | Rowan's review distinguishes player-authored facts, agreed campaign premises, preferences, and non-binding hopes. The player may correct the review and the five-attribute assignment until explicit confirmation; confirmation atomically creates the character and initial world at Market Square without fixing an NPC choice or outcome. |
| FR4 | The five attributes are Body, Agility, Constitution, Mind, and Presence. Assign each of 8, 10, 12, 13, 14 exactly once; modifier is `floor((score - 10) / 2)`. Preserve confirmed starting assignments separately from later current-score increases. |
| FR5 | Accept free-text intentions as proposals, not state edits. Routine feasible actions succeed without a roll; impossible or unsupported actions receive a factual explanation. Unsupported verbs and rejected proposals consume no fictional time or resources. Ask neutral clarifications for ambiguity and suggest options only when explicitly requested. |
| FR6 | Show reasonably knowable stakes, cost, and interpretation before consequential commitment; clarify rare-resource spending or materially changed intent. Fix check difficulty and mechanical outcomes before rolling where practical, validate contextual consequences before commitment, and narrate only committed facts. |
| FR7 | Eligible uncertain checks use a fair d20: natural 1 fails, natural 20 succeeds, and other faces succeed when `die + attribute modifier + skill bonus >= difficulty`. Calculate and record pre-roll probability from all applicable bonuses; difficulty cannot change after the roll or rise on an unchanged task merely to erase growth. |
| FR8 | The controlled payment-extension check uses Presence 14 (+2), Persuasion +1, difficulty 12, and 60% success. Success grants one day; failure leaves the deadline unchanged and consumes only the exchange duration. The fixture assignment does not constrain ordinary Session 0 characters. |
| FR9 | Award check XP only for successful meaningful checks: `floor(100 * (0.95 - p) / 0.90)` to both player and relevant-skill tracks. Failed checks, routine actions, and 95%-success checks award zero. Each track begins at level 1/0 XP; the next level costs `100 * current level`, consumes that amount, and carries excess. |
| FR10 | Each player level grants one allocatable +1 attribute point; each skill level grants +1 to that skill bonus. Attribute and skill growth have no design cap. Resolved checks award once; unchanged retries, rejected actions, and artificial bonus suppression create no new XP opportunity. |
| FR11 | The authoritative shared clock stores seconds. Typing, reading, model latency, menus, inspection of known information, inventory, journal, and saving advance zero seconds. Completed travel, speech, handling, purchases, gifts, and waits advance only their validated actual duration. The game pauses when closed. |
| FR12 | Travel uses route distance divided by mode speed, rounded up per completed segment. P0 routes are Market Square–Mara's Stall 7 m and Market Square–Common Room 140 m; ordinary-ground speeds are walk 1.4, jog 2.8, sprint 5.6, crawl 0.5 m/s. Unknown routes or modes require a supported ruling. |
| FR13 | A completed dialogue exchange costs `15 * ceil(rendered spoken words / 30)` seconds, counting player and NPC speech once and excluding prose/instructions/reasoning; two and 30 words cost 15 seconds, 31 cost 30. Interrupted exchanges charge only completed segments. |
| FR14 | Item handling uses a contextual estimate: the prepared pouch handover takes five seconds, while counting 100 loose coins takes at least 100 seconds in an isolated timing fixture. Transfers occur only on completed handover; rejected or duplicate requests never charge twice. Purchases combine actual speech and handling once each. |
| FR15 | Campaign epoch is day 1 at 00:00; confirmation opens at second 28,800 (08:00). Waits may specify duration, clock target, or event. Next morning is 06:00; an NPC order occurs only if the NPC decides to order. Face-to-face silence returns control after 60 seconds; overnight waiting is not interrupted every minute. Impossible or unscheduled event targets do not wait forever. |
| FR16 | P0 has one settlement, three authored locations (Market Square, Mara's Stall, Common Room), four named NPCs (Mara, Oren, Tessa, Ivo), one social conflict, readable exits and context, one ordinary purchase, and one uncertain-check situation. No procedural location generation or required phrase/puzzle solution. |
| FR17 | The captured P0 starting state gives the player exactly one prepared test-fixture pouch containing 10,000 gold and no other gold; Mara stocks five 1-gold drinks. Purchase, full-pouch gift, and no-gift branches independently reload that same capture and never merge. The pouch is neither ordinary campaign starting wealth nor later-stage funding. |
| FR18 | Each named NPC has a need, competing desire, obligation, relationship, resources, current plan, and limited knowledge. A gift changes Mara's feasible opportunities; her choice and its effect on Oren follow recorded motives and state, with no required retirement script or obedience from social success. |
| FR19 | Tessa observes the gift and meets Ivo in the Common Room 1,800 seconds after the gift opportunity whether or not a gift occurs. Gossip requires actual contact and motive. Non-witnesses lack the event before receipt; a distorted or doubted claim may affect a later choice without rewriting the event. Beliefs retain source, time, uncertainty, and distortion. |
| FR20 | Authoritative events, individual observations and beliefs, and player-facing narration stay distinct. Follow-up dialogue, spending, schedules, or obligations demonstrate memory; an internal remembered flag alone is insufficient. Inspection for testing may expose the causal chain while player presentation respects limited knowledge. |
| FR21 | Free-text input has no proactive suggested actions, choices, replies, or action chips. Enter submits and Shift+Enter inserts a line. Linked exits, inventory, journal, save/load, and optional roll details are factual controls. Multi-action requests expose order/stakes/stopping conditions or ask for separate submissions. Pending/resolved/failed request state and recovery are visible. |
| FR22 | Three manual save slots restore the complete branch: seconds, ownership, money, inventory, relationships, commitments, beliefs, plans, confirmed starting attributes, current attributes, player/skill XP and levels, bonuses, and allocated/unspent points. Loading an older save restores its own clock and progression with no cross-branch carryover or separate per-action undo. |
| FR23 | Retried or replayed resolved requests cannot duplicate purchases, gifts, time, rolls, or XP. Captured proposals and seeded dice replay to the same mechanical result, though new LLM prose need not match. Interrupted requests preserve committed progress and identify pending work. |
| FR24 | The P0 gate captures three controlled gift/no-gift pairs and at least one rumor variant; checks funds, stock, ownership, plan and belief causes, the fixed roll and XP edge cases, timing variations, growth from near-threshold saves, save/load, and player-explained believability. Any unexplained authoritative contradiction or conservation/save failure is corrected and the affected scenario repeated before P1. |

**Total P0 functional requirements: 24.** These IDs are extraction handles for this assessment, not new GDD identifiers.

### Non-Functional Requirements

| ID | P0 non-functional requirement extracted from the GDD |
| --- | --- |
| NFR1 | Local desktop-browser, solo prototype with durable manual saves and an LLM connection. No engine, language, storage technology, server, model, or provider is selected by the GDD. |
| NFR2 | A new or returning session targets 20–60 minutes; a new session includes Session 0 and opening play. |
| NFR3 | Preserve browser preferred text sizing and zoom, including 200% page zoom and 320 CSS px reflow without two-dimensional page scrolling except intrinsically two-dimensional content. Use visible keyboard focus, non-color speaker labels, and no timed reading. |
| NFR4 | G07 text targets: 60–120 words for location introductions, 20–60 on repeat visits, and 40–120 for typical action results. Attribution distinguishes narrator, NPC speech, awards, and mechanics; every meaningful cue is textual. |
| NFR5 | G16 targets: input acknowledgement within 100 ms; local menus within 200 ms; save/load within 2 seconds; 95% of completed LLM actions within 10 seconds; recoverable interruption by 30 seconds. |
| NFR6 | Run a 60-minute wall-clock endurance evaluation of about 100 representative actions with four active NPCs; record simulated seconds separately. Browser resident memory may rise no more than 100 MB from the loaded-scene baseline and must not grow monotonically per action. |
| NFR7 | Log action latency, model calls/tokens, actual cost, rejected proposals, duplicate attempts, and contradiction repairs; record browser/test-machine specifications. No acceptable dollar limit or provider has yet been selected. |
| NFR8 | Results must be mechanically reproducible from captured proposals and dice, with zero unexplained authoritative contradictions or resource/save conservation failures across the controlled repetitions. Believability is recorded separately from mechanical consistency. |

**Total P0 non-functional requirements: 8.**

### Additional Requirements

P0 excludes magic, effects/resources, access/ownership expansion, survival, autonomous livelihood chains, community victory/ward pressure, businesses beyond one purchase, crafting, construction, combat, added cast/locations, offline progression, multiplayer, and procedural geography. The 100 loose coins are an isolated timing fixture and never enter the funded social branches. The broader GDD keeps P1–P9 conditional on prior evidence gates; budget, availability, dates, model/provider, and implementation stack remain separate decisions.

### GDD Completeness Assessment

The P0 baseline is unusually specific about fixture state, arithmetic, timing, branch isolation, failure paths, and acceptance evidence. Requirements are sufficiently explicit to test coverage against stories. The document intentionally leaves technical stack, provider, cost ceiling, and exact narrative copy to later decisions; their effect on implementation readiness must be checked against the architecture and exit plan.

## Epic Coverage Validation

The authoritative epics file uses its own FR1–FR84 numbering. The matrix below maps this report's **GDD extraction IDs** to story and exit-plan locations; the two FR number series must not be treated as identical.

### Coverage Matrix

| GDD extraction | Epic/story coverage | Status |
| --- | --- | --- |
| FR1 entry and saves | 1.2 | Covered |
| FR2 Rowan questions and zero-time draft | 1.3–1.4 | Covered |
| FR3 reflection and atomic confirmation | 1.5–1.8 | Covered |
| FR4 fixed attributes and immutable origin | 1.5, 1.7, 1.22–1.24 | Covered |
| FR5 free-text, feasibility, clarification | 1.10, 1.12, 1.14 | Covered |
| FR6 pre-commit stakes and truthful narration | 1.15–1.16 | Covered |
| FR7 d20, probability, contextual difficulty | 1.22 | Covered |
| FR8 controlled payment extension | 1.22 | Covered |
| FR9 XP formula and level thresholds | 1.23 | Covered |
| FR10 allocation, no caps, no duplicate XP | 1.23–1.24 | Covered |
| FR11 shared seconds clock and zero-time UI | 1.18 | Covered |
| FR12 route distances and modes | 1.17–1.18 | Covered |
| FR13 speech duration | 1.19 | Covered |
| FR14 pouch/loose-coin handling | 1.19–1.20 | Covered |
| FR15 epoch and waiting rules | 1.7, 1.21 | Covered |
| FR16 P0 authored content budget | 1.7, 1.17, 2.1 | Covered |
| FR17 isolated wealth/purchase/gift branches | 1.7, 1.19–1.20, 2.3–2.4 | Covered |
| FR18 grounded NPC state and gift replanning | 2.1–2.4 | Covered |
| FR19 witness, contact, rumor and doubt | 2.5–2.7 | Covered |
| FR20 truth/knowledge/presentation distinction | 1.25, 1.31, 2.5–2.8 | Covered |
| FR21 composer, controls and operation state | 1.9–1.14 | Covered |
| FR22 three-slot complete branch persistence | 1.28–1.30, 2.2–2.8 | Covered |
| FR23 idempotent retry and deterministic replay | 1.12–1.16, 1.30, 2.4–2.8 | Covered |
| FR24 full P0 evidence gate | [P0 Verification and Exit Plan](./p0-verification-and-exit-plan.md), Epic 1 and Epic 2 exit criteria | Covered |

### Missing Requirements

No P0 GDD functional requirement is missing from the revised Epics 1–2 and P0 Verification and Exit Plan. The exit plan holds stage-wide repetition, endurance, accessibility, contradiction, and believability checks; its separation from player feature stories is explicit.

The epics inventory also contains implementation requirements with no one-to-one GDD FR, notably durable operation states, typed API contracts, revision checks, diagnostics, and deployment/runtime choices (native FR31–FR34). Those are derived from architecture and UX rather than falsely presented as GDD mechanics. Epics 3–11 are conditional design backlog and do not expand P0 scope.

### Coverage Statistics

- P0 GDD FRs extracted: **24**
- Covered by revised P0 stories or P0 exit plan: **24**
- Missing: **0**
- Coverage: **100%**

## UX Alignment Assessment

### UX Document Status

Both P0 UX contracts are present and marked final: [DESIGN.md](./ux-designs/ux-dmud-2026-09-08/DESIGN.md) defines visual tokens and components; [EXPERIENCE.md](./ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md) defines behavior, states, accessibility, and the Session 0/E1/E2 flows. The illustrative notebook mockup yields to these documents if they differ. Both explicitly defer E3–E11.

### UX ↔ GDD Alignment

- Entry, Rowan-led Session 0, player-selected name, fixed five-score assignment, correctable reflection, and zero-time confirmation align with GDD G03 and the P0 entry contract.
- A single free-text composer, factual navigation, neutral clarification, known-information queries, explicit pre-commit stakes, truthful request states, and no suggested actions align with G06 and the intent/action rules.
- The E1 and E2 journeys preserve separate purchase and gift branches, authoritative transaction and check results, three-slot save/load, gift-driven Mara plans, contact-based Tessa-to-Ivo reports, and player knowledge limits.
- Browser-owned text size, keyboard and screen-reader parity, 200% zoom, 320 CSS px reflow, contrast, focus, target size, and reduced motion implement G15. G16 response targets are copied without changing their status as evaluation targets.
- Deferred System and award treatments remain design tokens only; P0 screens exclude P6–P8 mechanics and rewards as required by the staged GDD.

### UX ↔ Architecture Alignment

- Architecture 1.2 selects React/FastAPI/SQLite and maps the P0 UX contracts to typed queries/commands, durable Session 0 drafts, atomic confirmation, revisioned save slots, one composer, one accessible overlay shell, and operation state via SSE with polling recovery.
- Backend player-view projections filter knowledge before serialization and before Rowan recall; development diagnostics are separate and capability-gated. This supports the UX prohibition on hidden NPC knowledge leaking through transcript, journal, inventory, save labels, character sheet, and result details.
- The architecture translates DESIGN tokens in `frontend/src/app/styles.css`, assigns dialog/focus and status-announcement ownership, and lists browser accessibility journeys plus the 100 ms/200 ms/2 s/10 s/30 s response targets as verification gates.

### Alignment Issues and Warnings

No P0 document-level UX/GDD/architecture contradiction was found. The architecture expressly says its dependency compatibility and accessibility claims are document-level plans, not executable proof; Story 1.1 and the P0 exit plan require those checks during implementation. The UX Open Item about storage of player-authored facts and hopes is resolved by architecture's typed Session 0 draft and categorized statements.

## Epic Quality Review

### Epic structure and value

All eleven epic goals describe a player-observable capability. Epic 1 can be a useful entry/action foundation and Epic 2 adds the P0 social proof. Epics 3–11 have one-way stage dependencies and are explicitly conditional; they are design backlog, not P0 implementation commitments. No P0 story calls for a P1–P9 subsystem. Story 1.1 supplies the greenfield project setup required by Architecture 1.2 within a player-value epic; it is a setup story rather than a standalone technical epic.

### Critical structural defects

| Finding | Evidence and impact | Required repair |
| --- | --- | --- |
| Q1 — Session 0 stories depend on later operation stories | Stories 1.3–1.4 require durable Rowan operations, truthful pending/failure state, reconnect, and polling; 1.6–1.8 require recoverable reflection/confirmation. Stories 1.12–1.13 first define the common operation lifecycle, SSE/polling, cancellation, and restart recovery. Architecture ADR-006 says Session 0 uses that common worker from its first story. The early stories cannot meet their AC independently in the stated order. | Move a minimal durable operation vertical slice, including draft subject, status query and recovery, ahead of 1.3; keep branch-action-specific behavior in later stories. Update IDs and traceability. |
| Q2 — Campaign confirmation depends on later authored-world loading | Story 1.7 requires the confirmed campaign to contain the exact P0 locations, NPCs, pouch, conflict, and starting clock, while Story 1.17 first owns strict loading/validation of that content package. Story 1.7 either builds an unlisted provisional content path or waits for 1.17. | Move authored content loading/validation before confirmation, or explicitly make a minimal validated starting-world content slice part of an earlier story and have 1.17 extend it without replacement. |
| Q3 — Gift story depends on later observation model | Story 2.3 requires Mara's and Tessa's observations at gift commit and non-witness knowledge unchanged. Story 2.5 first owns typed historical facts, observations, claims, beliefs, and witness rules. Completing 2.3 before 2.5 would duplicate or defer its acceptance criteria. | Move typed fact/observation and witness capture before 2.3; leave scheduled contact and full claim/belief propagation for later stories. |

### Major sequencing and sizing issues

| Finding | Evidence and impact | Required repair |
| --- | --- | --- |
| Q4 — Title save selection reaches an unbuilt load boundary | Story 1.2 requires a compatible occupied slot to be selected, loaded, and reported as success/failure. The complete save and load behavior is in 1.28–1.29. The early story can implement cold/empty/error Title states, but cannot independently complete its occupied-save path as written. | Split 1.2 into early Title/New Game and later occupied-save selection/load integration, or move the save/load vertical slice earlier. |
| Q5 — Action submission claims later lifecycle behavior | Story 1.12 requires clarification, resolving, committed and narrating states before 1.14–1.16 implement interpretation, commit, and narration. Story 1.13 requires cancellation and restart reconciliation around the commit record later defined in 1.15. This makes 1.12–1.13 difficult to accept as independently done. | Establish the common operation state machine first; keep 1.12–1.13 criteria limited to states and recovery paths supported by their completed action slice, then add resolution and narration transitions with 1.14–1.16. |
| Q6 — Story 1.1 spans several delivery concerns | Its eight scenarios cover dependency locks, dev proxy, packaged production serving, SQLite migration, secrets, directory boundaries, and all baseline quality gates. The scope is broader than one demonstrable initial application slice even though the greenfield setup itself is required. Story 1.13 likewise combines stream replay, polling, cancellation, restart, idempotency, branch isolation, and timeout across nine scenarios. | Keep the minimal runnable, tested shell as the first story. Move packaging or other independently verifiable work into a small subsequent story; split operation recovery by distinct user-visible failure modes while preserving common lifecycle ownership. |

### Dependency and acceptance summary

The repaired P0 order should establish the local app, minimal durable operation contract, and validated authored fixture before Session 0 confirmation; then add action interpretation/commit/recovery and save/load; then deliver gift, witness observation, contact, belief, and downstream choice. Epic 2 needs only completed Epic 1 capabilities once Q1–Q5 are resolved. P0 acceptance criteria generally use concrete Given/When/Then/And scenarios and include invalid, interrupted, duplicate, save/load, and accessibility cases. The defects are **story order and scope**, not missing P0 requirements or vague ACs. The stage-wide P0 Verification and Exit Plan correctly holds repetitions and endurance outside player feature stories.

The conditional E3–E11 backlog is not sprint-ready by its own status; the existing backlog identifies oversized later-stage stories and requires each phase's UX update and decomposition at its own gate. Those known later-stage issues do not change the P0 verdict.

## Summary and Recommendations

### Overall Readiness Status

**NOT READY for P0 story-by-story implementation or sprint commitment in the current sequence.** The GDD, UX, architecture, and P0 requirement coverage align at the document level, but the first stories cannot each be completed against their own acceptance criteria without implementing behavior assigned to later stories. This is a planning defect; it is not a claim that P0 is technically infeasible or that implementation tests have failed.

### Critical Issues Requiring Immediate Action

1. **Q1:** Put the durable operation vertical slice before Rowan draft, reflection, and campaign-confirmation stories that already require it.
2. **Q2:** Put validated P0 authored-world content before the story that atomically confirms that world.
3. **Q3:** Put typed fact/observation and witness capture before the story that commits the witnessed gift.

### Recommended Next Steps

1. Re-sequence and, where necessary, split Stories 1.1–1.17 and 2.3–2.5 so every story's Given/When/Then criteria can pass using only completed prior work. Keep one owner for the common operation contract and one owner for authored-content validation.
2. Move or split Story 1.2's occupied-save path to follow save/load, and constrain Stories 1.12–1.13 to lifecycle transitions their completed action slice can actually exercise. Break the broad foundation and recovery work into independently demonstrable increments.
3. Update the P0 story-level FR traceability and architecture story references after renumbering; keep the P0 Verification and Exit Plan as the stage gate. Rerun a focused dependency/readiness review before sprint planning. During implementation, verify dependency compatibility, accessibility, performance, and causal evidence with the specified executable gates.

### Final Note

This P0 assessment found **six actionable story-quality issues** in two categories: three critical sequencing defects and three major sequencing/sizing issues. It found **zero missing P0 GDD functional requirements** among 24 extracted requirements and **zero P0 UX/architecture document contradictions**. P1–P9 remain conditional and outside this P0 readiness decision.

**Assessment date:** 2026-09-23  
**Assessor:** Codex, using the GDS Implementation Readiness workflow  
**Evidence type:** planning-document review; no implementation or runtime test result is implied.
