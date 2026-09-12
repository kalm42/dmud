---
stepsCompleted:
  - step-01-document-discovery
  - step-02-gdd-analysis
  - step-03-epic-coverage-validation
  - step-04-ux-alignment
  - step-05-epic-quality-review
  - step-06-final-assessment
filesIncluded:
  gdd:
    - gdds/gdd-dmud-2026-09-07/gdd.md
    - gdds/gdd-dmud-2026-09-07/decision-log.md
  architecture:
    - _bmad-output/game-architecture.md
  epics:
    - epics.md
  ux:
    - ux-designs/ux-dmud-2026-09-08/DESIGN.md
    - ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md
    - ux-designs/ux-dmud-2026-09-08/reconcile-brief.md
    - ux-designs/ux-dmud-2026-09-08/reconcile-gdd.md
    - ux-designs/ux-dmud-2026-09-08/review-rubric.md
    - ux-designs/ux-dmud-2026-09-08/validation-report.md
    - ux-designs/ux-dmud-2026-09-08/mockups/direction-dm-notebook.html
excludedDuplicates:
  - gdds/gdd-dmud-2026-09-07/epics.md
---

# Implementation Readiness Assessment Report

**Date:** 2026-09-12
**Project:** dmud

## Document Inventory

### GDD

- `gdds/gdd-dmud-2026-09-07/gdd.md` — primary GDD
- `gdds/gdd-dmud-2026-09-07/decision-log.md` — companion decision record

### Architecture

- No architecture document was found inside `planning_artifacts`; `_bmad-output/game-architecture.md` was located during UX alignment and included in the assessment.

### Epics and Stories

- `epics.md` — selected current epic and story source
- `gdds/gdd-dmud-2026-09-07/epics.md` — excluded as the older duplicate candidate

### UX Design

- `ux-designs/ux-dmud-2026-09-08/DESIGN.md`
- `ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md`
- Supporting reconciliation, validation, rubric, decision-log, and mockup artifacts

### Discovery Warnings

- Architecture was not discoverable under the configured planning-artifact search patterns because it is stored at `_bmad-output/game-architecture.md`; this location mismatch risks future workflow omissions.

## GDD Analysis

Source analyzed in full: `gdds/gdd-dmud-2026-09-07/gdd.md` (version 0.3, status `draft-for-correction`). Requirement wording below preserves whether the source marks a rule as accepted, proposed, assumed, conditional, deferred, or out of scope.

### Functional Requirements

FR1: The game shall accept free-text player intentions while treating the LLM as interpreter, NPC performer, thematic judge, and narrator; deterministic game rules shall remain authoritative for validation, dice, and committed state.

FR2: P0 shall contain exactly one settlement, three locations, four named NPCs, one social conflict, one uncertain check situation, one stocked drink item plus gold, and the defined gift/no-gift and rumor test variants.

FR3: P0 shall prove that a gift changes one NPC's feasible plans, a report travels through contact, an uncertain check resolves, and all resulting consequences survive save/load before P1 is considered.

FR4: P1 shall remain conditional on passing P0 and, if promoted, shall add the compact community problem, alchemy and brewing, daily quests with gacha item rewards, a small affinity choice, one earned ability variant, and generated recognition.

FR5: P2 shall remain conditional on P1 and, if promoted, shall add hidden bonus objectives and bonus rewards for unusual, creative, or accidental quest completion approaches.

FR6: Resolving Brackenford's central problem shall not end or reset the persistent world.

FR7: A player intention shall not directly edit authoritative state; ownership, success, and other state changes occur only when mechanically validated and committed.

FR8: Routine feasible actions shall succeed without a roll; impossible or unsupported actions shall receive a factual explanation without consuming time, and alternatives shall be offered only when the player requests help.

FR9: Social checks shall not compel an NPC to abandon binding obligations or become obedient.

FR10: Before a consequential action, the game shall expose reasonably knowable stakes, cost, and interpreted intent, and shall clarify rare-resource spending or materially changed intent.

FR11: The game shall set difficulty and, where practical, mechanical success and failure consequences before rolling; difficulty shall never be changed after the result is known.

FR12: Contextual consequences proposed after resolution shall be validated before state is committed; rejected proposals shall change nothing.

FR13: Retrying a resolved request shall not duplicate purchases, consume resources twice, reroll the action, duplicate elapsed time, or award XP again; an unchanged failed approach shall not create unlimited checks.

FR14: Eligible uncertain checks shall use `d20 + attribute + relevant basic-skill bonus >= difficulty`, with natural 1 always failing and natural 20 always succeeding at the admitted stakes.

FR15: The rules shall calculate pre-roll success probability from the fixed target and all applicable bonuses, including natural-roll overrides, and record target, modifiers, probability, stakes, die, total, consequence, and XP.

FR16: Attributes and skill bonuses shall have no design cap; player levels shall grant allocatable attribute points and skill levels shall increase the corresponding skill bonus.

FR17: The provisional P0 check fixture is Presence + Persuasion at difficulty 12 with total bonus +3: success grants a one-day payment extension; failure preserves the deadline and consumes only the exchange's actual duration without reversing a gift.

FR18: The authoritative action clock shall use seconds; travel, spoken conversation, item handling, and waiting advance time, while typing, reading, model latency, menus, known-information inspection, inventory viewing, journaling, and saving do not.

FR19: Travel time shall equal route distance divided by the applicable movement speed, with meaningful events interrupting movement and no flat adjacent-room travel cost.

FR20: The provisional movement fixture shall use metres and metres/second, whole-second ceiling per completed segment, ordinary speeds of walk 1.4, jog 2.8, sprint 5.6, and crawl 0.5, and route distances of 7 m and 140 m.

FR21: Completed dialogue time shall provisionally be `15 * ceil(rendered spoken words / 30)` seconds, count player and NPC speech once, exclude narration/instructions/reasoning, and commit only completed segments when interrupted.

FR22: Item transfers and purchases shall use validated contextual handling durations; the P0 gift fixture provisionally transfers a prepared known-value pouch in five seconds, while individually counting 100 coins takes at least 100 seconds.

FR23: Wait actions shall accept a duration, clock target, or event condition; simulation—not an LLM estimate—shall determine elapsed time and whether the requested event occurs.

FR24: A wait shall stop for a response-worthy development, an actual scheduled decision, a provisional 60-second face-to-face silence interval, or an impossible target; it shall not manufacture an NPC decision or wait forever.

FR25: Distant NPC plans shall advance on the shared action clock; closing the game shall pause simulation and there shall be no offline progression.

FR26: Each named NPC shall have a need, competing desire, obligation, relationship, resources, current plan, and limited knowledge that constrain decisions.

FR27: A gift shall alter an NPC's feasible opportunity set without forcing a scripted retirement, investment, debt payment, refusal, or obedience response.

FR28: Routine NPC schedules and purchases shall proceed by rules, while consequential replanning and dialogue may use the LLM only within recorded constraints.

FR29: The game shall distinguish authoritative events, observations, received beliefs, and player-facing presentation; beliefs shall retain source, time, uncertainty, and distortion and shall never rewrite historical fact.

FR30: Gossip shall require plausible contact and motive; non-witnesses shall not automatically learn events, and received claims may be doubted, distorted, concealed, or lied about consistently with an NPC's knowledge.

FR31: P0 shall use Mara, Oren, Tessa, and Ivo with the accepted G05 motives, obligations, relationships, and contact schedule across Market Square, Mara's Stall, and the Common Room.

FR32: The controlled G05 fixture shall start with 10,000 test gold, a one-gold drink with stock five, Tessa witnessing the gift opportunity, and Tessa meeting Ivo in the Common Room 1,800 seconds later whether or not the gift occurs.

FR33: The rumor variant shall allow Tessa to suggest that the gift bought influence and Ivo's existing distrust to cause him to seek confirmation before favoring the player; automatic slander and anonymous gifts are excluded from this first test.

FR34: Observation, contact, received claims, and resulting action shall be inspectable for testing, while the player presentation continues to respect limited knowledge.

FR35: A crafting attempt shall require a declared item intent, ingredients, workspace, recipe or approach, tools, and applicable Alchemy or Brewing competence; feasibility shall be validated before resolution.

FR36: A known mastered craft shall succeed routinely; an uncertain or novel craft shall use the G03 check system. Success shall create a persistent item with explicit effects; failure shall consume ingredients without output; both shall advance time by the declared work period.

FR37: P1 crafting shall support healing/restorative potions, conditionally mana-restoration potions, poisons, and brewed drinks, each with its own skill association and narrow upgrade track.

FR38: Poison applied to a weapon or food shall alter that object's persisted properties until triggered, consumed, expired under the stated recipe rule, or cleaned; delivery method shall govern exposure.

FR39: Alchemy and Brewing shall be universal basic skills, provisionally starting at bonus zero, and shall not permit a craft without declared inputs present in inventory.

FR40: Daily quests shall be assigned through a fourth-wall-breaking LitRPG System whose voice and presentation are distinct from the narrator, NPC dialogue, and award narration.

FR41: Every System quest shall display explicit success conditions from assignment, appear in the journal, refresh at a defined world-clock interval, and transition through the journal state model.

FR42: Actual completion of a daily quest—not declaration, partial completion, or retry—shall award both player XP and relevant-skill XP and unlock exactly one gacha draw.

FR43: A gacha draw shall select one item from a visible, declared pool while concealing the result until drawing; expired daily quests shall incur no penalty beyond the unearned reward and shall be replaced at the next refresh.

FR44: The provisional P1 daily-quest configuration shall provide three slots refreshing at 06:00, crafting/social/movement-observation categories, and common/uncommon/rare gacha tiers at 70%/25%/5%, with pool contents declared before implementation.

FR45: The primary input shall remain free text with no visible suggested actions, recommendations, dialogue replies, or action chips.

FR46: The interface shall retain factual linked exits, inventory, journal, save/load, and optional roll details; Enter submits, Shift+Enter inserts a line, and all controls shall be keyboard reachable.

FR47: Ambiguous names shall prompt neutral disambiguation; unsupported verbs shall explain the limitation without spending time or automatically suggesting alternatives; clarifications shall preserve intent without recommending strategy.

FR48: Request state shall visibly distinguish pending, resolved, and failed states and provide a recoverable failure path without implying that uncertain processing succeeded.

FR49: Multi-action input shall expose order, stakes, and stopping conditions before consequential commitment; P0 may require actions to be submitted individually.

FR50: P0 shall expose exactly the three accepted authored locations with readable exits, present people, and examinable context; geography and connections shall remain stable and shall never be procedurally generated.

FR51: Location introductions shall use 60–120 words, repeat visits 20–60 words emphasizing changes, and typical action results 40–120 words.

FR52: Inventory state shall authoritatively track ownership, quantity, location, and transferability; scenery may be examined but is not automatically takeable.

FR53: P0/P1 shall not require an authored puzzle chain, exact-phrase solution, maze, fast travel, hidden-room puzzle, equipment grid, weight simulation, item-combination puzzle, or loot table.

FR54: Narrative and award text shall agree with committed facts; the award voice shall not decide NPC behavior or rewrite an event, and an achievement shall be eligible only when its underlying event actually occurred.

FR55: The game shall provide three manual save slots, no separate per-action undo, and explicit permission to reload older saves for controlled branch comparison.

FR56: Loading shall restore world time, ownership, inventory, relationships, commitments, beliefs, NPC plans, player and skill XP/levels, bonuses, allocated and unspent points, and reward records; abandoned-branch rewards shall not carry across saves.

FR57: Replaying a captured initial state with captured proposals and seeded dice shall reproduce mechanical results even when newly generated prose differs.

FR58: All characters shall be able to attempt the listed universal basic skills subject to feasibility, knowledge, tools, and context; P0 shall exercise only Persuasion, and no class system shall exist.

FR59: All organic and System-assigned quests shall state explicit success conditions when accepted; situations without expressible conditions shall remain open concerns rather than quests.

FR60: The proposed journal shall track concerns and commitments through proposed, accepted, fulfilled, failed, or abandoned states, record renegotiation, parties, required outcome, evaluating authority, and the ownership or promise backing any reward.

FR61: Brackenford shall remain the hub; NPC schedules, dialogue, and off-screen consequences shall respect shared game time, individual knowledge, resources, and commitments, without a universal obedience reputation meter.

FR62: Successful meaningful checks shall award probability-based player and relevant-skill XP; routine actions, rejected actions, resolved retries, and checks that can fail only on natural 1 shall award no check XP.

FR63: The proposed G18 curve shall award `floor(100 * (0.95 - p) / 0.90)` XP only on success, use a `100 * current level` threshold with overflow, grant one attribute point per player level and +1 skill bonus per skill level, and impose no maximum.

FR64: Conditional P1 awakening shall use at most two chosen affinities with two ability slots per affinity and one small starting package; all package effects, ownership, costs, limits, duration, range, and slot use shall be declared before play.

FR65: A Rest-concept awakening stone shall provisionally choose a recipient affinity with a free slot, compose two supported candidates using whole-affinity context, select uniformly, retain its recorded 80%/20% prototype rarity band, and be consumed only after a valid award.

FR66: The LLM alone shall judge thematic fit for awakening, while rules validate ownership, capacity, prerequisites, supported effects, costs, and limits; a generated name shall not introduce an unsupported mechanic.

FR67: Conditional P1 shall allow one earned ability variant after three distinct consequential uses and one named achievement prerequisite, disclose its tradeoff, and require the player to choose whether it replaces the prior version in the same slot.

FR68: Titles shall grant explicit buffs and achievements shall award explicit item prizes; neither shall automatically apply an ability upgrade, the earned record shall survive sale or loss of its prize, and NPC rewards shall not conjure unowned resources.

FR69: The proposed recognition fixture shall include one title granting +1 to a named basic-skill check once per simulated day and one generated utility prize worth at most five gold, without duplicate stacking.

FR70: Each craft type shall maintain its own successful-distinct-event count; threshold crossing shall offer a new recipe within that type, declining shall defer the offer until the next crossing, and adopting shall preserve the base recipe.

FR71: The healing track shall include Healing Draft, Restorative Elixir, and Draught of Revival with the source-defined wound-removal, lost-limb, 120-second post-death, critical-injury, and one-application-per-death limitations.

FR72: The poison track shall include Weak Toxin and Potent Venom with the source-defined Perception/Athletics penalties, durations, weapon/food delivery, and persistence behavior.

FR73: The brewing track shall include Common Ale, Quality Ale, and Artisan Brew with the source-defined Perception penalties, Presence/social bonuses, durations, and recipe-adoption choice.

FR74: Craft thresholds are provisionally T1 at 10 and T2 at 25 successful distinct craft events; failures and retries of an already resolved craft shall not count.

FR75: Conditional P1 shall begin with 30 gold, use purchased finite-stock ingredients at declared prices and declared work periods, and permit crafted goods to be used, given, or sold only where an NPC has actual need, preference, and funds.

FR76: The simulation shall implement the causal cycle in which resources and obligations constrain NPC plans, executed plans create observations, encounters transmit claims, and beliefs and relationships influence later choices.

FR77: Unsupported proposals shall be rejected and recorded as expansion candidates rather than narrated as successful consequences; source state and proposals shall be retained for diagnosis.

FR78: P0 play shall expose exits, one transaction, known needs, gift consequences, and check stakes before expecting interpretation of social reports; journal views shall restate known evidence without revealing secrets, fixed ordering, or action hints.

FR79: P0 evidence shall compare gift/no-gift from identical initial state and reconcile funds and ownership while demonstrating a motive-grounded change in Mara's opportunity set and observed behavior.

FR80: P0 evidence shall verify declared-check resolution, natural 1/20 behavior, probability and XP records, narration consistency, and idempotency of rejected or retried requests.

FR81: P0 evidence shall verify Tessa's observation, later contact with Ivo, non-witness ignorance before receipt, and a distorted or doubted claim changing a later choice without changing the original event.

FR82: P0 evidence shall verify full save/load restoration and reproducible mechanical outcomes from captured proposals and rolls.

FR83: P0 evidence shall separately record mechanical consistency and Kyle's ability to explain why Mara changed plans and why Ivo behaved differently.

FR84: P0 timing and growth evidence shall compare movement speeds, short and long dialogue, prepared and individually counted coin transfers, silent and overnight waits, event interruption, absence of proactive suggestions, once-only XP, leveling, uncapped high-bonus fixtures, and zero XP at 95% success probability.

FR85: Conditional P1 evidence shall verify affinity slot use, context-sensitive candidates, rarity bounds, title and achievement effects, prize-sale eligibility, and a separately chosen earned variant.

FR86: Conditional P1 evidence shall verify crafting success/failure consumption, persistent poison delivery, distinct-event thresholds, recipe adoption/deferral, and at least one healing and brewing tier unlocked during controlled realistic-length play.

FR87: Conditional P1 evidence shall verify daily assignment and refresh, visible conditions, exact XP and gacha rewards, no duplicate reward, clean expiry, distinct System voice, equal visibility for organic quest conditions, and player feedback on whether explicit conditions harm immersion.

Total FRs: 87

### Non-Functional Requirements

NFR1: The initial product shall run locally in a desktop browser for solo play and use an LLM connection once a model/provider is selected.

NFR2: P0 should fit a 20–60-minute session; P1 should leave a personally interesting unfinished concern that supports an easy later return.

NFR3: Saves shall be durable and complete, preserve committed progress through interrupted requests, and resume with pending work clearly identified.

NFR4: The interface shall support adjustable 16–24 px text, visible keyboard focus, speaker identification independent of color, a quiet layout, and no timed reading requirements; these G15 accessibility targets remain proposed.

NFR5: Every meaningful cue shall have a textual representation; P0/P1 require no audio, music, illustration, portrait, sprite, animation, or generated-image pipeline.

NFR6: In the proposed G16 test profile of 60 minutes, 100 actions, and four NPCs, visible input acknowledgement should occur within 100 ms and local menus within 200 ms.

NFR7: Save/load should complete within two seconds under the proposed G16 profile.

NFR8: Under the proposed G16 profile, 95% of completed LLM-mediated actions should finish within 10 seconds and an action still incomplete at 30 seconds should expose a recoverable interruption.

NFR9: Session tests shall record browser and test-machine specifications and measure memory at start and end for unexplained growth; a hard memory or FPS target is intentionally deferred.

NFR10: The system shall log action latency, model calls and tokens, actual session cost, rejected proposals, duplicate-action attempts, and contradiction repairs.

NFR11: Generated abilities and reusable rulings shall retain stable identities and recorded versions across sessions; mechanics shall not change silently, and intentional revisions shall identify the version governing earlier results.

NFR12: Authoritative state shall remain internally consistent across narration, mechanical resolution, conservation of funds/items, event history, beliefs, and save/load.

NFR13: Interrupted operations shall be atomic with respect to uncompleted resource transfers while preserving any time or action segments already committed.

NFR14: Controlled replay shall be mechanically deterministic for captured state, proposals, and dice without requiring deterministic LLM prose.

NFR15: The game shall clearly distinguish narrator, NPC, System, award, and mechanical-result voices and shall never rely only on color to communicate attribution.

NFR16: The first evidence gate shall target zero unexplained authoritative contradictions and zero conservation or save failures before P1; any affected controlled scenario shall be corrected and repeated. This G17 threshold remains proposed.

NFR17: P1 expansion shall stop for investigation when play reveals unexplained outcomes, irrelevant NPC memory, opaque progression, severe latency, or insufficient desire to return.

NFR18: Actual model cost shall be measured before setting an acceptable dollar budget or selecting a provider; no unapproved spending commitment may be inferred.

Total NFRs: 18

### Additional Requirements

- **Authority and approval:** Accepted G05–G08 rules are authoritative. G03/G04/G18 combine accepted direction with unresolved tuning. G01–G02, G09–G13, G15–G17, G19, the detailed portion of G20, and G21 remain proposed. G14 is superseded by G19.
- **Stage gates:** Implementation scope is P0 only until its evidence checks pass. P1, P2, production, construction, broader magic, additional settlements, and possible co-op require separate promotion decisions.
- **P0 exclusions:** Magic/affinities, titles, achievements, new training activities, ward-pressure victory, crafting, construction, combat, extra NPCs or locations, offline progression, and multiplayer are excluded.
- **P1 exclusions:** Full affinity ranks/combinations, generated content libraries, construction/production chains, ingredient harvesting, recipe research, automated multi-batch crafting, player-run shops, new settlements, broad social networks, tactical combat, co-op, quest expiry penalties, streaks, configurable quest preferences, and hidden bonus objectives are excluded.
- **Permanent constraints:** Locations shall not be procedurally generated. There is no class system or class roadmap, no code validator for affinity/concept thematic compatibility, and no public persistent multiplayer commitment.
- **Unresolved design inputs before P0 implementation:** G03/G04 fixture tuning and G18 XP curve/pacing require review, including the dialogue minimum, contextual difficulty behavior, and final failure-XP policy; the document contains both an open-question sentence and G18's proposed zero-failure-XP rule.
- **Unresolved design inputs before P1 implementation:** Household viability, ward pressure, affinity packages/effects, protection costs, inventories, reward budgets, craft thresholds/effects/prices/needs, supplier restocking, mana-use costs, daily quest categories, gacha pool contents, and the fictional System framing require specification or approval.
- **Unresolved delivery inputs:** Architecture, engine/stack, storage approach, LLM model/provider, acceptable operating cost, delivery dates, weekly availability, content boundaries, public-release intent, and staffing/budget commitments are unset.
- **Evidence requirement:** G17 proposes three controlled repetitions per gift/no-gift pair, at least one rumor variant, two plausible P1 community routes, one unplanned supported approach, two voluntary return sessions, and optional friend feedback.

### GDD Completeness Assessment

The GDD provides a strong, unusually testable P0 concept, a tightly bounded fixture, explicit authoritative-state rules, and concrete evidence gates. Its separation of accepted direction, assumptions, deferred scope, and exclusions is generally clear. It is not implementation-ready as a final requirements authority, however: the file is explicitly marked `draft-for-correction`; several P0 tuning choices remain proposed; the failure-XP discussion is internally unsettled; and the existing architecture does not resolve newly introduced Session 0 and final UX requirements. P1 and P2 should be treated strictly as conditional planning because many mechanics, balance values, content pools, and dependencies remain unapproved or unspecified.

## Epic Coverage Validation

Source analyzed in full: `epics.md` (2,211 lines). The epic document explicitly limits implementation to P0 and excludes conditional P1, P2, and later scope. The matrix therefore distinguishes full coverage from deliberate phase deferral; a deferred item is not counted as covered, but it is not a P0 planning defect unless its prerequisite is needed now.

### Coverage Matrix

| FR | GDD requirement | Epic/story coverage | Status |
| --- | --- | --- | --- |
| FR1 | LLM interpretation with rules-owned authoritative state | Epics 2–5; especially Stories 2.2, 2.4 | ✓ Covered |
| FR2 | Exact P0 content boundary | Epic 3 and Story 5.5; cross-epic guardrails | ✓ Covered |
| FR3 | P0 causal-world promotion evidence | Story 5.5 | ✓ Covered |
| FR4 | Conditional P1 feature slice | Explicitly excluded from current epics | ◌ Deferred |
| FR5 | Conditional P2 hidden bonus objectives | Explicitly excluded from current epics | ◌ Deferred |
| FR6 | Persistent play after P1 central resolution | P1 end-state behavior is outside P0 | ◌ Deferred |
| FR7 | Intentions cannot directly edit state | Stories 2.2, 2.4 | ✓ Covered |
| FR8 | Routine success and factual unsupported-action rejection | Stories 2.2, 2.4 | ✓ Covered |
| FR9 | Social checks cannot compel obedience | Stories 3.4, 4.2 | ✓ Covered |
| FR10 | Expose knowable interpretation, stakes, and cost | Story 2.3 | ✓ Covered |
| FR11 | Pre-roll fixed target and stakes | Story 3.4 | ✓ Covered |
| FR12 | Validate proposed consequences before commit | Stories 2.4, 4.2 | ✓ Covered |
| FR13 | Retry and duplicate idempotency | Stories 2.4, 3.3–3.5, 5.1–5.3 | ✓ Covered |
| FR14 | Natural 1/20 d20 rule | Story 3.4 | ✓ Covered |
| FR15 | Probability and roll-evidence calculation | Story 3.4 | ✓ Covered |
| FR16 | Uncapped attributes/skills and level rewards | Story 3.5 | ✓ Covered |
| FR17 | Controlled Persuasion fixture | Story 3.4 | ✓ Covered |
| FR18 | Integer-seconds authoritative clock | Stories 3.1, 3.2 | ✓ Covered |
| FR19 | Distance/speed movement | Story 3.1 | ✓ Covered |
| FR20 | Provisional movement speeds and routes | Story 3.1 | ✓ Covered |
| FR21 | Provisional spoken-word time formula | Story 3.2 | ✓ Covered |
| FR22 | Handling and prepared/loose-coin durations | Story 3.3 | ✓ Covered |
| FR23 | Duration, target, and event waits | Story 3.2 | ✓ Covered |
| FR24 | Wait interruption and impossible-target behavior | Story 3.2 | ✓ Covered |
| FR25 | Shared clock, off-screen plans, no offline progress | Stories 3.2, 4.2 | ✓ Covered |
| FR26 | Complete grounded NPC state | Stories 3.1, 4.2 | ✓ Covered |
| FR27 | Gift changes feasible options without scripting | Story 4.2 | ✓ Covered |
| FR28 | Deterministic routine plans; bounded LLM replanning | Story 4.2 | ✓ Covered |
| FR29 | Facts, observations, claims, and beliefs separated | Stories 4.1, 4.3, 4.4 | ✓ Covered |
| FR30 | Contact-dependent, fallible information | Stories 4.3, 4.4 | ✓ Covered |
| FR31 | Accepted four-NPC social fixture | Stories 3.1, 4.1–4.4 | ✓ Covered |
| FR32 | Gift, stock, and 1,800-second contact fixture | Stories 3.3, 4.3 | ✓ Covered |
| FR33 | Controlled influence-rumor variant | Story 4.4 | ✓ Covered |
| FR34 | Inspectable social causal evidence | Stories 4.1, 5.4 | ✓ Covered |
| FR35 | Craft attempt prerequisites | Conditional P1 excluded | ◌ Deferred |
| FR36 | Craft success/failure and time | Conditional P1 excluded | ◌ Deferred |
| FR37 | Four crafting product tracks | Conditional P1 excluded | ◌ Deferred |
| FR38 | Persistent poison delivery | Conditional P1 excluded | ◌ Deferred |
| FR39 | Universal Alchemy and Brewing | Conditional P1 excluded | ◌ Deferred |
| FR40 | Distinct LitRPG System voice | Conditional P1 excluded | ◌ Deferred |
| FR41 | Visible daily quest conditions and refresh | Conditional P1 excluded | ◌ Deferred |
| FR42 | Daily quest XP and one gacha draw | Conditional P1 excluded | ◌ Deferred |
| FR43 | Visible gacha pool and no expiry penalty | Conditional P1 excluded | ◌ Deferred |
| FR44 | Proposed slots, categories, and rarity rates | Conditional P1 excluded | ◌ Deferred |
| FR45 | Free text without suggested actions | Epic 2; Stories 1.2, 2.1–2.4 | ✓ Covered |
| FR46 | Factual controls and keyboard composer | Stories 1.2, 2.1 and UX guardrails throughout | ✓ Covered |
| FR47 | Neutral clarification and unsupported verbs | Stories 2.3, 2.4 | ✓ Covered |
| FR48 | Truthful lifecycle and recovery state | Story 2.4 | ✓ Covered |
| FR49 | Multi-action order/stopping clarification | Story 2.3 | ✓ Covered |
| FR50 | Three stable authored locations | Story 3.1 | ✓ Covered |
| FR51 | Location and result text-length ranges | Story 3.1 plus UX requirements | ✓ Covered |
| FR52 | Authoritative inventory fields | Story 3.3 | ✓ Covered |
| FR53 | Explicit absence of P0/P1 puzzle/inventory extras | Scope guardrails and NFR1 | ✓ Covered |
| FR54 | Narration/award agreement with committed fact | Narration covered in Stories 2.2, 2.4, 3.4; achievement eligibility deferred | △ Partial |
| FR55 | Three manual slots and branch reload | Stories 5.1, 5.2 | ✓ Covered |
| FR56 | Complete branch restoration | Stories 5.1, 5.2 | ✓ Covered |
| FR57 | Deterministic mechanical replay | Story 5.3 | ✓ Covered |
| FR58 | Universal basic-skill access; P0 exercises Persuasion | P0 Persuasion and no-class boundary covered; broader skills deferred by scope | ✓ Covered |
| FR59 | Explicit conditions for organic and System quests | P0 concern distinction covered in Story 2.1; quest systems deferred | △ Partial |
| FR60 | Journal commitment states, renegotiation, evaluator, and funded rewards | Story 2.1 covers known entries and written status but not the complete G10 lifecycle or reward-backing rules | △ Partial |
| FR61 | Brackenford hub and knowledge-bounded NPC behavior | Stories 3.1 and 4.1–4.4 | ✓ Covered |
| FR62 | Probability-based XP eligibility | Story 3.5 | ✓ Covered |
| FR63 | Proposed XP curve and level thresholds | Story 3.5 | ✓ Covered |
| FR64 | P1 affinity packages and slot limits | Conditional P1 excluded | ◌ Deferred |
| FR65 | Rest-stone candidate and rarity procedure | Conditional P1 excluded | ◌ Deferred |
| FR66 | LLM thematic fit with rules validation | Conditional P1 excluded | ◌ Deferred |
| FR67 | Earned ability variant | Conditional P1 excluded | ◌ Deferred |
| FR68 | Titles, achievements, prizes, and prerequisites | Conditional P1 excluded | ◌ Deferred |
| FR69 | Proposed title and prize fixture | Conditional P1 excluded | ◌ Deferred |
| FR70 | Craft-type progression and adoption | Conditional P1 excluded | ◌ Deferred |
| FR71 | Healing recipes and effects | Conditional P1 excluded | ◌ Deferred |
| FR72 | Poison recipes and effects | Conditional P1 excluded | ◌ Deferred |
| FR73 | Brewing recipes and effects | Conditional P1 excluded | ◌ Deferred |
| FR74 | Proposed craft thresholds | Conditional P1 excluded | ◌ Deferred |
| FR75 | Proposed P1 crafting economy | Conditional P1 excluded | ◌ Deferred |
| FR76 | Resource→plan→observation→belief causal cycle | Epic 4 | ✓ Covered |
| FR77 | Reject unsupported proposals and record expansion candidates | Rejection and diagnostics are covered, but no acceptance criterion classifies the proposal as an expansion candidate | △ Partial |
| FR78 | Required first-session information exposure sequence | Features exist across Epics 2–4, but no story enforces the required exposure order before social-report interpretation | ❌ Missing |
| FR79 | Gift/no-gift conservation evidence | Story 5.5 | ✓ Covered |
| FR80 | Declared-check and idempotency evidence | Story 5.5 | ✓ Covered |
| FR81 | Tessa→Ivo provenance and distortion evidence | Story 5.5 | ✓ Covered |
| FR82 | Save/load and replay evidence | Story 5.5 | ✓ Covered |
| FR83 | Separate explainability and believability feedback | Story 5.5 | ✓ Covered |
| FR84 | Timing, input, and uncapped-growth variants | Story 5.5 | ✓ Covered |
| FR85 | P1 affinity and recognition evidence | Conditional P1 excluded | ◌ Deferred |
| FR86 | P1 crafting evidence | Conditional P1 excluded | ◌ Deferred |
| FR87 | P1 daily quest evidence | Conditional P1 excluded | ◌ Deferred |

### Missing Requirements

#### High-priority P0 gap

**FR78 — First-session exposure sequence**

- Impact: The individual capabilities are planned, but implementation could introduce the social-report reasoning test before the player has seen exits, a transaction, known needs, gift consequences, and declared check stakes. That would weaken the GDD's onboarding and evidence validity.
- Recommendation: Add an acceptance criterion to Epic 3 or Story 5.5 that exercises the first-session sequence and asserts that those facts are exposed before the player is expected to interpret a social report.

#### Partial P0 gaps

**FR60 — Journal commitment lifecycle**

- Impact: `proposed → accepted → fulfilled/failed/abandoned`, renegotiation history, evaluator identity, and resource-backed rewards are not all traceable to current acceptance criteria. This risks a journal that displays labels without enforcing commitment semantics.
- Recommendation: Extend Story 2.1 or add a bounded P0 commitment story covering state transitions, renegotiation, evaluating authority, and the rule that rewards must be owned or promised.

**FR77 — Expansion-candidate recording**

- Impact: Unsupported intentions are rejected and logged, but the GDD also requires them to become inspectable expansion candidates. Without classification, playtest demand cannot be separated cleanly from operational rejection telemetry.
- Recommendation: Add an acceptance criterion to Story 2.4 or 5.4 for a versioned, read-only expansion-candidate record linked to the rejected request, without implying implementation commitment.

#### Mixed or deliberately deferred partials

- FR54's fact-consistent narration is covered; its achievement-award eligibility clause belongs to excluded P1.
- FR59's P0 concern behavior is covered; organic quest workflow and System quests remain conditional future scope.

### Requirements Present in Epics but Not in the GDD Baseline

- Epic FR1–FR4 add a Title screen and a detailed Rowan-led Session 0 flow, including a fixed `8, 10, 12, 13, 14` array and five attributes. These requirements are not stated in GDD v0.3.
- The epics replace the GDD's provisional `Body, Finesse, Mind, Presence` vocabulary with `Body, Agility, Constitution, Mind, Presence` and treat the array/modifier details as confirmed.
- Architecture-derived requirements add exact runtime versions, monorepo structure, FastAPI/React/SQLite, SQLite STRICT migrations, SSE operation resources, OpenAPI generation, RFC 9457 errors, loopback security, provider isolation, structured logging, and detailed CI gates. These are not traceable to the GDD itself.
- UX-derived requirements add a complete visual token system, WCAG 2.2 AA, overlay behavior, responsive/reflow behavior, and many named component states beyond the GDD's smaller G15 accessibility proposal.

These additions may be validly sourced from architecture and UX artifacts, but the GDD alone does not authorize them. Their cross-document consistency is assessed in later workflow steps.

### Coverage Statistics

- Total GDD FRs: 87
- Fully covered in current P0 epics: 54
- Partially covered: 4
- Deliberately deferred with conditional P1/P2 scope: 28
- Missing from current stories: 1
- Strict full-GDD coverage: 62.1%
- Full coverage among non-deferred requirements: 91.5% (54 of 59)
- Non-deferred requirements with full or partial coverage: 98.3% (58 of 59)

## UX Alignment Assessment

### UX Document Status

**Found and analyzed in full:**

- `ux-designs/ux-dmud-2026-09-08/DESIGN.md` — final, P0 visual contract
- `ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md` — final, P0 behavioral contract

**Architecture also found and analyzed in full:** `_bmad-output/game-architecture.md` (complete, version 1.0). It was outside the configured `planning_artifacts` folder, so the initial pattern-based discovery reported it as missing. This assessment uses the actual architecture file referenced by `epics.md`.

### UX ↔ GDD Alignment

#### Strong alignment

- Both require ordinary free-text interaction without action chips, suggested dialogue, strategy steering, or MUD-style exact verbs.
- Both preserve the authority boundary: presentation reports committed facts and never claims success while work is pending.
- Both require factual exits, inventory, journal, save/load, and roll details to consume zero fictional time.
- Both require explicit attribution for narration, NPC speech, player intent, mechanics, and later System/award voices without relying only on color.
- Both require three manual save slots, branch isolation, complete restoration, safe retry, and exact-once state mutation.
- Both enforce player-knowledge boundaries and prohibit omniscient character rosters or hidden-state leakage.
- Both treat P1 alchemy, affinities, achievements, titles, daily quests, gacha, and P2 hidden objectives as deferred until a later phase-specific UX update.
- Both support text-first desktop-browser sessions, no required art/audio, adjustable/readable text, keyboard operation, and no timed reading.

#### Alignment issues

1. **Session 0 and Title flow lack GDD authorization.** The final UX contract adds Title, New Game/Continue, a Rowan-led Session 0, character-background questions, campaign hopes, reflection/correction, and explicit character confirmation. GDD v0.3 does not define this journey.
2. **Starting attributes conflict.** The GDD provisionally names four attributes—Body, Finesse, Mind, Presence—with P0 fixture ratings 0–3. EXPERIENCE.md says the fixed array and attribute names remain unresolved, while `epics.md` hard-codes five attributes—Body, Agility, Constitution, Mind, Presence—and the exact array `8, 10, 12, 13, 14` as confirmed.
3. **Player identity wording is ambiguous.** UX prose repeatedly names the player character “James,” while Session 0 allows the player to provide a name. Implementation must treat James as the design persona/example unless the product decision explicitly fixes the campaign character's name.
4. **GDD tuning status is not preserved consistently.** UX correctly describes contextual-difficulty tuning and latency values as provisional, but the epics call the action-duration, XP, attribute, and check tuning “confirmed.” GDD v0.3 still marks substantial parts of G03, G04, and G18 as proposed.

### UX ↔ Architecture Alignment

#### Strong alignment

- React DOM and semantic CSS are appropriate for the text-first notebook, selectable content, responsive layouts, and native keyboard interaction.
- The architecture keeps the browser presentational and the FastAPI domain authoritative, matching the UX's truthful status and committed-result rules.
- Persisted operations, typed SSE, polling recovery, cancellation, restart reconciliation, and exactly-once request handling directly support `response-status`, interruption, retry, and commit-boundary UX.
- TanStack Query for authoritative server views and React state for drafts, overlays, focus, and preferences supports the UX state split.
- A shared `Dialog`, `Button`, `StatusMessage`, and `VisuallyHidden` layer can support the documented overlay, focus, status, and accessible-label primitives.
- Architecture performance targets match the UX expectations for acknowledgement, menus, LLM completion, interruption, and save/load measurement.
- The project structure explicitly includes game-session, journal, inventory, saves, roll-details, diagnostics, and presentation-preference slices.
- CSS tokens are assigned to frontend application styles, providing an implementation home for the final DESIGN.md tokens.

#### Architectural gaps

1. **Session 0 domain and persistence are not designed.** The architecture has no explicit model, commands, queries, storage states, or validation boundary for Session 0 drafts; separation of character facts, agreed premises, preferences, and non-binding hopes; stat-array assignment; confirmation; or immutable starting-stat records.
2. **Title/save-index behavior is not mapped.** The architecture supports saves generally but does not define the UX-required cold save-index state, Continue availability, retry behavior, or transition into Session 0 versus save selection.
3. **Accessibility coverage is materially under-specified.** Architecture mentions keyboard reachability, color-independent speaker labels, and text size, but does not make WCAG 2.2 AA, semantic landmarks, screen-reader reading order, live regions, focus containment/return, 200% zoom, 320-CSS-pixel reflow, contrast thresholds, reduced motion, hover parity, or no-stacked-dialog behavior architectural quality gates.
4. **Character-sheet ownership is implicit.** The frontend structure has no explicit character/session-creation or progression presentation slice despite extensive UX states. It may live inside `game-session`, but that ownership and its API/read-model boundaries need to be explicit before stories are implemented independently.
5. **UX state contracts are not transport-mapped.** The operation lifecycle is well modeled, but empty/loading/error/corrupt states for Journal, Inventory, Character Sheet, Roll Details, Title, and Save Selection are not tied to explicit query or problem-response contracts in the architecture.
6. **The architecture predates the final UX status.** Its readiness boundary says the GDD and epics remain draft-for-correction and it contains no direct reference to DESIGN.md or EXPERIENCE.md, indicating that UX support was inferred rather than validated and incorporated.

### Warnings

- Do not implement the exact Session 0 stat model until the GDD/product authority resolves the four-versus-five attribute model, exact array values, and whether Session 0 is P0 scope.
- Add the primary UX pair and current root-level `epics.md` to the architecture's source-document register; it currently points to the older nested GDD `epics.md` and omits UX.
- Convert the UX accessibility floor into explicit architecture decisions and automated quality gates before frontend stories begin, especially focus management, announcements, contrast, zoom, reflow, and reduced motion.
- Keep deferred `system-notice` and `award-notice` definitions as design tokens only; current epics correctly prohibit rendering P1/P2 UI.

## Epic Quality Review

### Review Scope

All five epics and all 22 stories in `epics.md` were reviewed for player/prototype-owner value, sequential independence, forward dependencies, vertical slicing, data creation timing, BDD quality, testability, starter compliance, and traceability.

### Epic Compliance Summary

| Epic | User value | Sequential independence | Story sizing | No forward dependency | Data created when needed | Testable ACs | Traceability |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 — Create a Personal Campaign | ✓ | ❌ | ❌ | ❌ | △ | ✓ | △ |
| 2 — Speak and Act Through a Trustworthy Rowan | ✓ | ❌ | △ | ❌ | ✓ | ✓ | ✓ |
| 3 — Explore, Transact, and Grow in Brackenford | ✓ | ✓ | ❌ | ✓ | ✓ | ✓ | ✓ |
| 4 — See Consequences Travel Through People | ✓ | ✓ | △ | ✓ | ✓ | ✓ | ✓ |
| 5 — Preserve and Verify a World That Remembers | ✓ | ✓ | ❌ | ✓ | ✓ | △ | ✓ |

All epic titles and goals express player or prototype-owner outcomes rather than technical milestones. Epic 5's diagnostics and proof capabilities are valid prototype-owner value, although several of its stories are too broad.

### 🔴 Critical Violations

#### 1. Contradictory controlled-gift amount

Story 5.5 says the gift branch “deducts exactly 100 coins,” while the GDD, Epic FR24, Story 3.3, and the same epic's scenario define a prepared pouch worth 10,000 gold.

- Impact: The primary P0 conservation proof has two incompatible expected outcomes, so tests can pass only one authority.
- Remediation: Change Story 5.5 to deduct the complete 10,000-gold prepared-pouch value, or explicitly redefine the fixture in all source artifacts through an approved decision.

#### 2. Forward dependency from Epics 1–2 to Story 3.1

Story 1.4 requires stable authored Brackenford content and an opening Market Square scene. Story 2.2 requires authored current-location details. The concrete content registry, strict YAML validation, stable location IDs, and P0 world instantiation are first acceptance-tested in Story 3.1.

- Impact: Epic 1 cannot deliver its promised opening scene, and Epic 2 cannot deliver grounded inspection, using only completed earlier work. This violates epic independence and makes Story 3.1 a hidden prerequisite.
- Remediation: Move the minimal immutable content-registry and Market Square/NPC fixture capability into Story 1.1 or a new early Story 1.2, then make Story 3.1 extend it with movement and full location behavior. Do not duplicate a temporary content path.

#### 3. Unapproved stat model treated as confirmed implementation input

Epic FR3 and Stories 1.3–1.4 hard-code the array `8, 10, 12, 13, 14` across Body, Agility, Constitution, Mind, and Presence. GDD v0.3 instead has a provisional four-attribute vocabulary and 0–3 P0 fixture ratings; final EXPERIENCE.md explicitly says the array and attribute vocabulary remain open.

- Impact: Story 1.3 can be implemented and tested exactly as written while contradicting both the current GDD authority and UX open items.
- Remediation: Resolve the product decision, update GDD and UX, and only then lock the story. Until then, Story 1.3 is not ready for implementation.

### 🟠 Major Issues

#### Oversized stories

| Story | Why it is too large | Recommended split |
| --- | --- | --- |
| 1.1 | Combines repository scaffolding, exact dependency setup, SQLite validation/migrations, title/save index, New Game idempotency, responsive design tokens, accessibility, contracts, and all quality gates | Separate a runnable vertical starter/title slice from contract/quality baseline work, while keeping each resulting story independently runnable |
| 2.4 | Combines rejection semantics, the complete persisted operation FSM, SSE reconnection, polling, per-branch concurrency, idempotency, cancellation, crash recovery, RFC 9457 errors, focus preservation, and fault-injection testing | Split operation recovery/transport from rule rejection and truthful player recovery, ensuring the first slice still produces a real visible outcome |
| 3.1 | Combines full authored-content validation, NPC/world instantiation, location narration, all movement modes/routes, UI navigation, idempotency, accessibility, and browser tests | Establish content loading earlier; retain one focused authored-navigation story and separate fixture-validation evidence if needed |
| 3.2 | Defines conversation timing, several wait modes, deterministic scheduling, simultaneous ordering, interruption phases, loop detection, downtime, retry, UI, and full integration coverage | Split core clock/speech timing from event waits/interruption, with deterministic scheduler foundations introduced in the first slice |
| 5.3 | Requires replay for movement, waiting, transactions, checks, progression, allocation, reports, belief changes, NPC replanning, migrations, narration, diagnostics, privacy, and divergence detection | Build replay incrementally with each owning mechanic, leaving a smaller cross-mechanic replay-verification story |
| 5.4 | Combines player diagnostics, capability security, causal inspector, branch diff, provider telemetry, read-only enforcement, export/redaction, structured logging, accessibility, and all failure modes | Split player-safe evidence, gated causal inspection, and redacted export/observability into separate independently valuable stories |
| 5.5 | Combines the entire deterministic P0 proof, performance/endurance testing, qualitative playtest, accessibility, report generation, and optional real-provider evaluation | Separate deterministic acceptance proof, measured performance run, and human believability evaluation/report |

Stories 4.2–4.4 are large but remain cohesive around one causal behavior each; they should be estimated carefully rather than split automatically.

#### Incomplete source traceability

The epic document defines a new FR1–FR40 namespace and maps it internally, but it does not preserve source IDs or section links for GDD, architecture, and UX requirements. New Session 0 and technical requirements therefore appear alongside GDD-derived requirements without authoritative provenance.

- Remediation: Add a source column or stable IDs such as `GDD-G03`, `UX-DR19`, and architecture ADR/pattern references to each requirement and story. Keep local delivery IDs if useful, but do not replace source traceability with renumbering alone.

#### Undefined campaign start time

Story 1.4 requires the campaign to begin at its “defined starting game second,” but neither the story nor the current GDD/UX baseline specifies that value.

- Remediation: Name the exact epoch/starting second or reference a single authored-content field whose value is validated and testable.

#### Ambiguous endurance duration

Story 5.5 calls for “60 in-world or evaluation minutes,” while G16 specifies a 60-minute, 100-action desktop session. In-world time and wall-clock evaluation duration are different measures.

- Remediation: Require a 60-minute wall-clock evaluation session and separately record simulated seconds advanced, unless an approved decision says otherwise.

#### CI ownership is implicit

Story 1.1 requires all quality gates to pass but does not explicitly create or validate the architecture's `.github/workflows/quality.yml` pipeline.

- Remediation: Add an acceptance criterion identifying the versioned CI workflow, its separate failing gates, and the locally reproducible commands it runs.

#### NFR and UX traceability is not closed

The epics inventory contains 18 NFRs and 40 UX requirements, but only FR1–FR40 receive a formal coverage map. Cross-cutting ACs repeat many NFR/UX concerns without showing whether every source requirement has an owner.

- Remediation: Add NFR and UX coverage maps or annotate each story with the NFR/UX IDs it verifies.

### 🟡 Minor Concerns

- The UX and story prose repeatedly says “James” despite Session 0 allowing a player-selected name. Clarify that James is a test persona and use “the player character” in normative ACs unless the name is fixed.
- Story 5.5 says “Rowan attempts the controlled persuasion scenario,” while Story 3.4 assigns the request to the player speaking to Oren. Correct the actor for unambiguous test steps.
- Cross-cutting accessibility, idempotency, failure, and real-boundary test clauses are repeated in nearly every story. A shared Definition of Done plus story-specific observable criteria would reduce maintenance risk without weakening coverage.
- “Personally relevant” in Story 1.4 needs a deterministic test interpretation, such as referencing at least one confirmed character fact or preference while making no outcome promise.

### Dependency Analysis

```text
Epic 1
  1.1 → 1.2 → 1.3 → 1.4
                └──────── hidden dependency on 3.1 authored content

Epic 2
  2.1 → 2.2 → 2.3 → 2.4
          └────────────── hidden dependency on 3.1 authored location content

Epic 3
  3.1 → 3.2 → 3.3 → 3.4 → 3.5

Epic 4
  prior gift/content → 4.1 → 4.2
                           └→ 4.3 → 4.4

Epic 5
  prior complete causal state → 5.1 → 5.2 → 5.3 → 5.4 → 5.5
```

Apart from the authored-content dependency, later-epic ordering is sound: no Epic 3–5 story requires a capability first introduced in a later epic. Data structures are generally introduced by the story that first needs them, and cross-epic guardrails correctly discourage building all future schemas up front.

### Positive Quality Findings

- Every epic has a clear player or prototype-owner outcome.
- All stories use the user-story form and maintain explicit FR references.
- Acceptance criteria consistently use Given/When/Then, cover happy paths and failures, and are unusually specific and behavior-focused.
- The plan consistently enforces real FastAPI/SQLite/browser integration and confines deterministic substitution to the external LLM boundary.
- The create-vite and uv starter requirements, exact dependency capture, and committed lockfiles are correctly placed in Story 1.1.
- Conditional P1/P2 work is consistently excluded from P0 stories.
- Epic 4 correctly refuses narration-only proof and demands provenance-backed causal behavior.

## Summary and Recommendations

### Overall Readiness Status

**NOT READY**

The project has a strong causal-world design, a complete architecture, a final P0 UX pair, and unusually detailed behavior-driven stories. Nevertheless, P0 implementation should not begin from the current artifacts because developers would have to choose between incompatible requirements and work around a forbidden forward dependency. The blockers are document-authority and plan-correctness defects, not a lack of product thought.

### Critical Issues Requiring Immediate Action

1. **Resolve the P0 source of truth.** GDD v0.3 is still `draft-for-correction`; G03/G04/G18 tuning remains proposed; UX says the stat model is open; and epics treat those inputs as confirmed. Approve one P0 baseline and update every downstream artifact to match it.
2. **Correct the gift conservation criterion.** Story 5.5 requires a 100-coin deduction while all other current sources define the prepared pouch as 10,000 gold.
3. **Remove the forward authored-content dependency.** Stories 1.4 and 2.2 require stable Brackenford content whose first concrete delivery is Story 3.1. Move the minimal content registry and opening fixture into Epic 1, then extend it later.
4. **Architect the newly added P0 journey.** Title, save-index behavior, Session 0 drafts, fact/premise/preference/hope separation, stat assignment, confirmation, and immutable starting attributes need explicit domain, persistence, command/query, and transport decisions.
5. **Turn the final UX accessibility contract into architecture and quality gates.** WCAG 2.2 AA, focus management, announcements, contrast, zoom/reflow, reduced motion, pointer parity, and dialog behavior are required by UX but not adequately specified by architecture.

### Recommended Next Steps

1. Run a focused GDD correction pass that decides whether Title/Session 0 is P0, chooses the attribute vocabulary and standard array, approves or revises G03/G04/G18 tuning, resolves failure XP wording, and changes the GDD status from draft only when those decisions are accepted.
2. Correct Story 5.5's gift amount, change “Rowan attempts” to the player attempting the Persuasion check, define the campaign epoch/starting second, and distinguish 60 wall-clock evaluation minutes from simulated game time.
3. Re-sequence the epic plan so the immutable authored-content registry and minimum Market Square fixture are delivered before Stories 1.4 and 2.2.
4. Update architecture version 1.0 or issue a superseding addendum that references the current root `epics.md` and final UX pair, then defines Title/Session 0, character-sheet ownership, save-index queries, UX state/error contracts, and accessibility enforcement.
5. Add explicit acceptance coverage for FR78's first-session exposure order, FR60's commitment lifecycle and funded rewards, and FR77's expansion-candidate recording.
6. Add source-level traceability for GDD, architecture, NFR, and UX requirements rather than relying only on the epic document's local FR1–FR40 numbering.
7. Split Stories 1.1, 2.4, 3.1, 3.2, 5.3, 5.4, and 5.5 into smaller runnable vertical increments without creating infrastructure-only stories.
8. Make CI ownership explicit in the first delivery slice and ensure each resulting story retains independently executable format, lint, strict type, contract, integration, and browser gates appropriate to its scope.
9. Rerun implementation readiness after the revised GDD, architecture, UX, and epics agree. Begin P0 implementation only after the critical conflicts and forward dependency are gone.

### Final Note

This assessment consolidated **17 issues across five categories**: requirements authority, GDD-to-epic coverage, UX/architecture alignment, story correctness and dependencies, and story sizing/verification. Three are critical epic-quality violations, one non-deferred GDD requirement is entirely missing from story coverage, four are only partially covered, and seven stories need resizing. Conditional P1/P2 requirements are appropriately deferred and should remain outside the corrective P0 work.

**Assessment date:** 2026-09-12  
**Assessor:** Codex, using the GDS Implementation Readiness workflow
