---
title: "dmud — Game Design Document"
game_type: text-based
secondary_genres: [rpg, simulation]
platforms: [desktop-browser]
created: 2026-09-07
updated: 2026-09-07
version: "0.3"
status: draft-for-correction
author: Kyle
sources:
  - ../../briefs/brief-dmud-2026-09-05/brief.md
  - ../../briefs/brief-dmud-2026-09-05/addendum.md
  - ../../briefs/brief-dmud-2026-09-05/.decision-log.md
---

# dmud — Game Design Document

**Review draft (0.3):** Accepted vision and working defaults are carried forward. The `G` decision register distinguishes accepted corrections from remaining assumptions. New tuning proposals retain explicit assumption tags; G05–G08 are accepted with the recorded corrections. Drafting does not approve those assumptions or authorize implementation. The initial prototype is P0 only; P1 is a conditional next slice. Version 0.3 replaces the competing drink stall with an alchemy crafting system (G19) and adds a daily quest system with gacha rewards (G20); G14 is superseded.

## Executive Summary

### Core concept

Live a self-directed fantasy life among people whose resources, obligations, knowledge, and relationships persist. Free-text intentions receive consistent consequences; history shapes limited special abilities and recognition. An LLM interprets intentions, portrays NPCs, judges thematic fit, and narrates. The game rules own mechanical validation, dice, and authoritative state.

Brackenford is a frontier settlement with a deteriorating protective ward. Repair, protection agreements, or relocation may secure its future. Residents disagree for legitimate reasons. The world continues after the central problem is resolved.

### Target platforms and audience

Desktop browser, initially running locally; solo personal prototype by one developer with AI assistance. Kyle and interested friends are the first audience. Adult tabletop roleplayers and LitRPG readers are the intended broader audience, with 20–60-minute sessions and easy save/resume. Small-party co-op is conditional on solo success. Public release depends on play evidence; no release date, revenue target, budget, or staffing commitment exists.

### Distinctive design combination

- Creative intentions become supported, persisted consequences rather than narration alone.
- NPCs pursue their own lives and act on limited, fallible knowledge.
- Player history shapes affinity abilities, title buffs, and achievement item prizes.

These are design goals to prove together, not claims of technical feasibility or market novelty.

## Goals and Context

### Project goals and scope gates

| Stage | Deliverable | Boundary / promotion condition |
| --- | --- | --- |
| P0: causal-world proof | A gift changes one NPC's feasible plans; a report travels through contact; one uncertain check resolves; consequences survive save/load | Exactly one settlement, three locations, four named NPCs, one social conflict. Pass P0 evidence checks before expanding |
| P1: first playable slice | A compact community problem, alchemy crafting (potions, poisons, and brewing) with narrow craft-progression upgrades, daily quest system with gacha item rewards, small affinity choice, one earned ability variant, generated achievement | Conditional on P0. Test sustained interest and understandable consequences before breadth |
| P2: extended quest depth | Hidden bonus objectives on all quest types; bonus rewards for unusual, creative, or accidental completion approaches | Conditional on P1. Test player creativity and surprise rewards before further expansion |
| Later vision | Production, construction, broader magic, additional settlements; possibly co-op | Separate scope decision after repeat play. No automatic promotion |

P0 tests causal credibility, not whether the complete game is fun. The 10,000-gold gift is controlled test funding, never the campaign's assumed starting balance.

### Background and references

Preserve tabletop flexibility and universal skills without importing all D&D rules; comic achievement personality without copying Dungeon Crawler Carl's voice or setting; affinity/awakening inspiration from He Who Fights With Monsters without adopting exact ranks or powers; earned opportunities inspired by Azarinth Healer without classes; grounded lives and consequential gifts inspired by Kingdom Come: Deliverance 2. Dwarf Fortress is an additional design reference for histories and social information, not a promised simulation scope. These references come from the supplied sources; this draft does not assert independently verified behavior in those works.

### Authority of inputs

The brief supplies vision and staged scope; the addendum expands mechanics and scenarios; the source decision log resolves chronology. Latest user corrections in this GDD decision log take precedence over original inputs and older draft proposals, including dice, progression, time, input, and authored-location rules. Earlier class, place-power, thematic-validator, and merged-reward overrides remain active. Explicit source proposals and provisional numbers remain proposals even where surrounding direction is accepted. See [decision log](decision-log.md) for the reconciliation register.

## Core Gameplay

### Game pillars

| ID | Pillar | Design consequence |
| --- | --- | --- |
| P-A | Creative actions have consistent consequences | State-supported results, declared stakes, reusable rulings; never narrate an uncommitted success |
| P-B | NPCs have lives beyond the player | Money changes feasible plans; obligations, preferences, relationships, and memory affect choices |
| P-C | Reputation travels through people | Reports require contact and motive; knowledge can distort or stop; beliefs never rewrite history |
| P-D | Limited powers reflect earned history | Uncapped attributes/skills reward long-term mastery; affinity slots limit the power repertoire, not growth; distinct rewards and optional evolution preserve accomplishment |

### Core gameplay loop

Discover a need, disagreement, or opportunity → inspect and plan → act or converse → resolve meaningful uncertainty → encounter changed resources, people, and information → gain opportunity, recognition, or ability development → choose the next concern. P0 exercises P-A through P-C plus basic earned growth from P-D; affinity powers and recognition enter P1 deliberately.

### Win/loss conditions

P0 ends when its evidence checklist is demonstrated; it has no campaign victory. Failure is a recoverable setback, not permadeath.

P1's central victory requires actual safety and livelihood conditions; an LLM declaration is insufficient. [ASSUMPTION: G01 — For the compact P1 scenario, every resident household must have a safe sleeping place, one food unit per resident per day, and an assigned credible protection or safe-relocation arrangement for three consecutive simulated days. All four named NPC households are explicitly represented. Repair, negotiated protection, and relocation can satisfy the same conditions through different recorded commitments.]

[ASSUMPTION: G02 — Start P1 with seven days of ward protection and communicate the remaining duration. Warn at three days and one day; deterioration interrupts long waits. After expiry, unresolved households face one visible supply loss per day, with no automatic deaths or irreversible campaign lockout. A recoverable failure interrupts the current plan and offers rebuilding or relocation.]

New supported solutions must meet the same conditions; the test duration and supply pressure need playtesting. Successful communities remain playable, including consequences of agreements, trade, and departures.

## Game Mechanics

### Intent, uncertainty, and outcome

The player enters an intention, not an authoritative state edit. Saying “I own this shop” does not transfer ownership. Routine feasible actions succeed without a roll; impossible or unsupported actions receive a factual explanation; offer alternatives only when the player asks for help. Social success cannot compel an NPC to abandon binding obligations or become obedient.

Before a consequential action, show reasonably knowable stakes, cost, and interpretation. Clarify rare-resource spending or materially changed intent. Fix difficulty before rolling and define mechanical success/failure consequences beforehand where practical; validate any contextual consequences proposed after resolution before committing them. Explain results using committed facts; hidden facts may remain hidden. A rejected proposal changes nothing. Retries of the same request cannot duplicate purchases, consume resources twice, or reroll a resolved action. Repeating an unchanged failed approach does not grant unlimited checks.

**G03 — accepted correction:** On an eligible uncertain check, a natural 1 automatically fails and a natural 20 automatically succeeds; other results use `d20 + attribute + relevant basic-skill bonus >= difficulty`. Attributes and skill bonuses have no design cap. Player levels award attribute points the player allocates; skill levels increase the corresponding bonus. Long-term play should allow godly competence and a feeling of being overpowered.

The LLM sets a contextual difficulty target before rolling and may raise it to establish an appropriate effective success probability. The rules calculate the actual probability from that target and all applicable bonuses, including natural-roll overrides. With one fair d20, count natural 20 plus successful faces 2–19, then divide by 20: rolled probabilities run from 5% to 95% in 5-point steps. Record the pre-roll target, modifiers, probability, and stakes; never change difficulty after seeing the result. Routine feasible actions still need no roll, and impossible or mechanically unsupported intentions are screened before rolling. A natural 20 succeeds at the admitted stakes, not at an otherwise impossible action or unlimited NPC obedience.

[ASSUMPTION: G03 — Keep Body, Finesse, Mind, and Presence as provisional attribute names, with P0 starting ratings 0–3 and starting basic-skill bonuses 0–2; these are initial fixture values, never caps. Retain the single Presence + Persuasion check at difficulty 12 with total bonus +3 (60% success). Success secures a one-day payment extension; failure leaves the deadline and costs the exchange's actual duration, without reversing a gift. Difficulty reflects the attempted feat and circumstances: do not raise the same unchanged task's target merely to cancel an increased bonus. Harder chosen feats can justify higher targets while familiar feats become easy.]

### P0 actions and time

**G04 — accepted correction:** The shared action clock uses seconds. There is no mandatory six-second turn and no flat five-minute action cost. Travel, conversation, handling items, and waiting advance fictional time; typing, reading, model latency, menus, and inspecting known information do not. Distant NPC plans advance on the same clock; closing the game pauses it. Durations proposed by the LLM must fit actual distance, movement, handling, speech, and events, and be validated before time advances.

| Action | Time basis | Preconditions and outcome |
| --- | --- | --- |
| Inspect / inventory / known journal / save | 0 seconds | Known information only; saving does not heal or restore items |
| Move | Distance divided by applicable speed | Use known route distance and chosen walking, jogging, sprinting, crawling, or another supported mode; stop for meaningful events |
| Converse / uncertain request | Rendered spoken words and thinking time | Trial formula below; never charge the whole narrative output as speech |
| Give / take / purchase | Contextual LLM estimate in seconds | One object can take seconds; counting 100 separate coins can take at least 100 seconds. Consent, ownership, stock, and funds still govern completion |
| Wait | Explicit duration, clock target, or event condition | LLM interprets intent and estimates; simulation determines actual elapsed time and whether the event occurs; interrupt for a response-worthy development |

Travel time is `distance / speed`, not `speed * distance`. Text descriptions can expose distance and travel mode without graphics. A next-room journey and a cross-town journey must not cost the same by default. NPC orders are decisions, not guaranteed timers: a waiting estimate must never manufacture the requested order.

[ASSUMPTION: G04 — Use metres and metres/second, rounding each completed travel segment up to a whole second. Initial ordinary-ground speeds: walk 1.4, jog 2.8, sprint 5.6, crawl 0.5; these are tunable character/context defaults, not permanent speed caps. Give the two P0 routes explicit distances of 7 m (Market Square to Mara's Stall) and 140 m (Market Square to Common Room): walking takes 5 s and 100 s. Unknown routes or movement modes require a supported distance/speed ruling before travel. No stamina subsystem is needed for these short fixture routes; long sustained sprints require later rules, not an assumption of limitless endurance.]

**G04 trial details (unapproved tuning):** For a completed dialogue exchange, total the rendered spoken words from the player and NPC, and use `15 * ceil(words / 30)` seconds: roughly two words per second rounded upward to a quarter minute for thinking time. Zero spoken words incur zero speech time; hesitation or silence is separately estimated. Thus 2 words take 15 s, 30 take 15 s, and 31 take 30 s. Count speech once across the exchange; exclude descriptive prose, player instructions, and model reasoning. This applies the user's proposed formula; the minimum 15-second spoken exchange remains a tuning choice. Exchanges interrupted by events commit only the speech/action segments actually completed; never charge unspoken future dialogue.

LLM handling estimates state whether coins are individually counted or transferred in an already counted container. For the P0 large-gift fixture, propose a 5-second transfer of a prepared, known-value pouch; its gold value is not a count of loose coins and it adds no container subsystem. In an interrupted transfer, completed time can elapse while funds/items remain untransferred until the agreed handover completes. Rejected interpretations and duplicate requests never double-charge time or resources. Purchases combine actual speech and handling time without counting either twice.

For “wait until morning,” resolve the next agreed morning time from the current world clock (trial: 06:00); 22:00 to 06:00 is 28,800 seconds. For “wait until the NPC orders,” advance through actual NPC decisions and stop when the order occurs. In a face-to-face wait, return control after 60 silent seconds with an observation that a minute passed, allowing the player to speak or continue. Do not interrupt an uneventful overnight wait every minute. If no event is scheduled or the target becomes impossible, report that state rather than waiting forever; the LLM's estimate is not an authoritative future fact. Rest, work, and crafting remain later activities.

### NPC agency and social information

Each named NPC has a need, competing desire, obligation, relationship, resources, current plan, and limited knowledge. A large gift changes the opportunity set; retirement, investment, debt payment, or refusal must follow that person's situation. Routine schedules and purchases proceed by rules; consequential replanning and dialogue use the LLM within recorded constraints.

Distinguish authoritative events, individual observations/received beliefs, and player-facing presentation. Beliefs retain source, time, uncertainty, and distortion. Gossip requires a plausible encounter and motive; non-witnesses do not learn events automatically. Truth need not be believed, and belief does not compel action. NPCs may lie or conceal motives consistently with what they know.

**G05 — accepted first-test scenario:** P0 uses this controlled social scenario: Mara, a stallholder owing 20 gold, wants to clear the debt but also visit her ill sister; Oren, the creditor, wants repayment and dependable trade; Tessa, a neighboring trader, observes the gift; Ivo, a courier and Tessa's friend, later meets her. Mara's decision affects Oren. Three locations are Market Square, Mara's Stall, and the Common Room. Market Square connects to each other location. Tessa meets Ivo in the Common Room 1,800 seconds after the gift opportunity, whether or not a gift occurs. The player starts the experiment with 10,000 test gold; a baseline purchase costs 1 gold from stock of 5 drinks. Compare gift/no-gift states with the same starting circumstances. A separate controlled rumor variant has Tessa suggest that the gift bought influence; Ivo's existing distrust makes him seek confirmation before favoring the player. This variant tests fallible belief, not automatic slander on every playthrough. Anonymous gifts, including sneaking gold to someone without revealing its source, are a desired later test; keep this first test witnessed and simple.

Observation, contact, received claim, and resulting action must be inspectable for testing. Player presentation must still respect limited knowledge. Follow-up dialogue and observed spending, changed schedules, or fulfilled obligations demonstrate memory; an internal “remembered” flag alone does not.

### Alchemy and crafting

The player can declare an intent to craft an item, providing ingredients, a workspace, and a stated recipe or approach. Feasibility, available ingredients, required tools, and the player's current Alchemy or Brewing skill level govern whether the attempt is routine or uncertain. Routine crafts with known recipes and mastered techniques succeed without a roll; uncertain crafts (novel recipes, scaling beyond current skill) use the G03 check system.

A successful craft produces a persistent item in inventory with explicitly stated effects. A failed craft consumes ingredients without output. Time advances by the declared work period using G04 rules. Applying a poison to a weapon or food item alters that object's properties until the coating is triggered or cleaned; the change persists across save and load.

Craft products fall into four categories, each with its own skill and upgrade track:

- **Healing and restorative potions** — consumable items that remove wound conditions from the recipient.
- **Mana-restoration potions** — consumable items that restore a spent affinity-ability use. [ASSUMPTION: G19 — This category requires a declared per-use affinity cost system. Without that system the track is deferred; healing and poison tracks are independent of it.]
- **Poisons** — applied to weapons (contact-on-hit) or food (effect-on-consume). Delivery method affects which targets are exposed and how the effect is triggered.
- **Brewed drinks** — beer, spirits, and artisan beverages. Consumed for immediate condition effects; higher-tier brews replace debuffs with buffs.

[ASSUMPTION: G19 — Alchemy and Brewing are universal basic skills; any player may attempt them subject to feasibility. Starting bonuses are 0. Ingredient prices, tool requirements, and base recipe knowledge are declared before a crafting attempt; no crafting attempt succeeds without declared inputs present in inventory. The LLM sets difficulty and validates feasibility; rules commit or reject the outcome.]

### Daily quest system

The System is a fourth-wall-breaking LitRPG-style interface that assigns daily objectives to the player. It speaks in a distinct voice — separate from the narrator, NPC speech, and award narration — and presents quests in a clean, system-style format with explicit success conditions visible from the moment a quest is assigned. The player always knows exactly what is required to complete each quest; the System does not hide objectives. This interface breaks the fourth wall deliberately and is consistent with the LitRPG genre conventions of the target audience.

Quests are visible in the journal, refreshed at a defined world-clock interval (draft: each in-game dawn), and tracked by the G10 journal mechanic (proposed → active → fulfilled or expired). Completing a daily quest rewards XP applied to both the player XP track and the most relevant skill used, and unlocks one gacha draw.

A gacha draw selects one item from a known pool with tiered rarity. The pool contents are visible before drawing; the draw result is not. Items are general-use: ingredients, rare crafting components, scrolls, or unique one-use objects. No daily quest failure incurs a penalty beyond the reward not being earned; the quest expires and a new one replaces it at the next refresh.

P2 extends daily quests with hidden bonus objectives (G21): see P2 scope and Development Epics E6.

[ASSUMPTION: G20 — Accepted direction: LitRPG fourth-wall-breaking System interface with a distinct voice; success conditions always visible. Remaining proposals: P1 tests three daily quest slots refreshed at in-game 06:00. Quest categories: crafting (make N items of a type), social (fulfill an NPC need or commitment), movement/observation (visit a location and inspect a condition). Gacha pool: three rarity tiers — common (70%: basic ingredients or minor consumables), uncommon (25%: rare ingredients, small item prizes), rare (5%: unique one-use items with explicit effects). Pool contents must be listed before P1 implementation.]

### Controls and input

**G06 — accepted with correction:** Use free-text intentions with no visible suggested actions, recommended choices, dialogue replies, or action chips. Do not steer the player's decisions. Retain linked exits, inventory, journal, save/load, and optional roll details as factual navigation/information controls. Enter submits; Shift+Enter adds a line; all controls are keyboard reachable. Ambiguous names prompt neutral disambiguation. Unsupported verbs explain the limitation without consuming time or automatically presenting alternative actions.

Clarifications preserve the player's intent and identify missing information without recommending a strategy. Show pending/resolved/failed request state and a recoverable failure path; never imply that uncertain processing succeeded.

## Text-Based Specific Design

### Input system

Natural-language interpretation without proactive action suggestions; no exhaustive verb parser or promise of arbitrary mechanics. Synonyms map to the same supported intent. A multi-action request must expose order, stakes, and stopping conditions before consequential commitment; P0 can ask the player to submit its actions individually (G06).

### Room/location structure

P0 has exactly the three locations in G05, readable exits, present people, and examinable context. No maze, fast travel, or hidden-room puzzle is required in P0. **G07 — accepted:** Location introductions use 60–120 words; repeat visits use 20–60 words emphasizing changes. Typical action results use 40–120 words. P1 reuses these three locations as its hub; protection and relocation can be represented as named destinations and commitments without adding explorable maps. Locations are never procedurally generated: authored geography and connections remain stable while descriptions reflect actual changes. Hidden rooms, puzzles, and traps may be added in later tests within authored locations; none is added to P0/P1 by this correction.

### Item and inventory system

Ownership, quantity, location, and transferability are authoritative. Scenery is examinable but not automatically takeable. P0 needs gold and one stocked drink item; no equipment grid, weight simulation, item combination puzzles, or loot tables. P1 adds the explicitly budgeted magic/reward and drink-production items below. Prize sale or loss does not erase the earned achievement record.

### Puzzle design

No authored puzzle chain in P0 or P1. Challenges arise from conflicting needs, constrained resources, information, and agreements. Inspecting known facts is free; journal summaries remind the player of promises and known obstacles without exposing NPC secrets. No required solution depends on guessing an exact phrase.

### Narrative and writing

Grounded, emotionally credible NPC voices; achievements may be mischievous and opinionated, while not every accomplishment requires a joke. The system's award voice cannot decide an NPC's behavior or rewrite an event. An award about retirement is eligible only if retirement actually occurred, not merely because the player mentioned it.

Use the fixed starting conflict to compare playthroughs, then permit outcomes to emerge. No mandatory villain, fixed quest order, full branching script, or campaign ending sequence. Dedicated narrative design is a later offered step for room copy, character voices, lore, and vocabulary; no separate narrative document is produced here.

### Game flow and pacing

P0 should fit inside a 20–60-minute session; P1 should leave a personally interesting unfinished concern for another session. Manual save/resume restores the whole current situation. No offline progression. **G08 — accepted:** Provide three manual save slots; loading restores the world clock, ownership, inventory, relationships, commitments, beliefs, NPC plans, player/skill XP and levels, allocated/unspent attribute points, and reward records. Replaying a captured starting state with captured proposals and seeded dice reproduces mechanical results; new LLM output may differ. There is no separate per-action undo. Reloading an older save is allowed for the personal prototype, specifically to compare diverging paths and repeat interactions. A loaded branch restores its own progression and clock; rewards from an abandoned branch do not carry across.

## RPG Specific Design

### Character system and basic skills

No classes, class unlocks, or class-evolution roadmap. Every character can attempt basic skills subject to feasibility, knowledge, tools, and context. The starting vocabulary is Athletics, Acrobatics, Sleight of Hand, Stealth, Arcana, History, Investigation, Nature, Religion, Animal Handling, Insight, Medicine, Perception, Survival, Deception, Intimidation, Performance, and Persuasion. P1 extends this with Alchemy (potion and poison crafting) and Brewing (fermented and distilled drinks); both are universal and subject to the same feasibility, knowledge, and tool requirements as all other basic skills. These categories do not import the full D&D ruleset or its six attributes.

P0 exercises only Persuasion (G03); other ordinary feasible actions are never locked behind affinity slots, titles, achievements, or stones. Unsupported complex checks receive an honest limit, not a claim that the character must unlock a basic skill. Unbounded growth, player levels, and skill levels are accepted; the provisional XP rules below exercise only this one skill in P0. Full attribute mappings, training activities, combat stats, and profession-specific crafting adjudication remain later design work.

### Inventory and equipment

P0 uses the ownership rules above, with no combat equipment. [ASSUMPTION: G09 — P1 has at most two chosen affinities, two special-ability slots per affinity, alongside the accepted player/skill leveling system. This deliberately tests fewer affinities than the source's provisional three. Offer two small starting packages: Ember + Fellowship or Vessel + Fellowship, each with one usable ability occupying one affinity's slot and a modest basic-skill bonus. Package details and all effect magnitudes must be listed before play; no passive ability is mechanically unlimited.]

The player chooses affinities among discoveries; substantially random rarity affects quality. Limited slots belong to each affinity, not a single global pool. A stone expresses its concept through one affinity into one available slot, with the entire affinity set influencing the result. Uncertainty concerns the acquired ability, not arbitrary unreliability whenever it is used. Awakening and earned evolution are separate systems.

### Quest system

Needs, conflicts, and negotiated agreements create quests; no fixed quest sequence is required. All quests — whether organic (from NPC needs and player commitments) or System-assigned daily objectives — display explicit success conditions when accepted. The player can inspect these at any time from the journal. Hidden information (NPC motives, available resources, what an NPC will actually do) remains hidden; the success *conditions* the player must meet are not. A quest that cannot state its success condition is not a quest — it is an unresolved situation to be tracked as an open concern.

[ASSUMPTION: G10 — The journal tracks known concerns and explicit commitments as proposed → accepted → fulfilled, failed, or abandoned, with renegotiation recorded as a changed agreement. When a commitment transitions to accepted, its success conditions are recorded in plain language: the specific outcome required, any involved parties, and the evaluating authority (NPC or System). Rewards require actual fulfillment and a payer's owned/promised resources. Victory is evaluated from community conditions (G01), not quest flags alone.]

Daily System quests (G20) are tracked in the same journal under a distinct category. They are assigned by the System rather than negotiated with an NPC, but their completion is evaluated by the same rules: actual fulfillment of the stated objective, not a declaration. System rewards (XP and gacha draw) are delivered by the System on confirmation of fulfillment; they cannot be claimed on partial completion or by exploiting retried requests.

### World, NPCs, dialogue, and combat

Brackenford is the hub; schedules and off-screen consequences share game time. Dialogue uses individual knowledge and commitments. NPC relationships are contextual, not a universal “gift enough money = obedience” meter. No companion party, merchant network, travel region, tactical combat, hit-point system, or combat ability kit is required in P0/P1. Risk is represented by the defined social/resource setbacks; combat is undecided later scope, not a silently implemented default.

## Progression and Balance

### Player and skill levels — G03 accepted direction

Attributes and skill bonuses have no design maximum. Player level-ups give allocatable attribute points; skill level-ups increase that skill's bonus. Levels do not introduce classes, gate universal basic-skill access, add affinity slots, or automatically evolve an affinity ability. Long-term mastery should let the player overpower familiar challenges; demanding new feats remain available.

XP depends on the actual pre-roll success probability: lower success probability gives greater XP, and a check that can fail only on natural 1 gives **zero XP**, on success or failure. A routine no-roll action also earns no check XP. Include all applicable bonuses when computing probability; do not compute rewards from nominal difficulty alone. Rejected actions, retries of an already resolved request, and repeated unchanged attempts do not create XP opportunities. Whether meaningful failures award reduced XP is an open tuning choice pending Kyle's answer.

[ASSUMPTION: G18 — Keep P0's scope to the existing check, one player XP track, one Persuasion XP track, and an attribute-allocation control. Proposed challenge award: `floor(100 * (0.95 - p) / 0.90)` for a successful meaningful check, with `p` calculated by counting successful d20 faces before the roll. Failures award zero XP. Award the challenge XP only on success; zero for both outcomes at p = 0.95. Start player and skill at level 1 with 0 XP. Reaching the next level costs `100 * current level` XP, consuming that threshold and carrying excess; repeat if multiple levels are crossed. Each player level grants one point to allocate as +1 to an attribute; each skill level grants +1 to that skill's bonus. No maximum level, attribute, or skill bonus is imposed.]

For the proposed curve, success at 95%, 60%, and 5% gives 0, 38, and 100 XP; failures always give 0. These success amounts are draft tuning, not approved progression pacing. P0 can start a separate controlled save near a threshold to test leveling without adding encounters or grinding. Save XP, levels, current bonuses, and unspent points; one resolved check awards only once. Player-chosen bonus suppression or deliberately contrived retries must not create an XP farm; the exact eligibility policy needs tuning without invalidating legitimate difficult approaches.

### Awakening experiment — conditional P1

[ASSUMPTION: G11 — To test the accepted progression direction without a full magic system, P1 adds one Rest-concept awakening stone and a tiny supported outcome pool: two candidates per starting affinity package, both composed for the player's chosen recipient affinity, each with an explicit owner, cost, duration, range, and slot requirement. Choose an affinity with a free slot before composing the two candidates, then select uniformly between them; this is a proposed choice among unresolved source procedures. At stone acquisition or controlled test setup, roll and record the stone's rarity in one of two prototype bands at 80%/20%; that retained stone rarity shapes its awakening pool. The higher stone band permits one stronger outcome parameter within a stated effect budget; it is not a new unlabelled output-rarity roll. Show the eligible ownership/slot/cost envelope before commitment. If no supported candidate fits, retain the stone and change nothing. Once validly awarded, the stone is consumed and the ability is fixed; save reload remains available. No respec/replacement system is required in this experiment.]

The LLM alone judges conceptual fit across stone, owning affinity, and whole affinity set. Rules validate ownership, capacity, explicit prerequisites, supported effects, costs, and limits; they must not certify thematic compatibility through code. A generated name never introduces an unsupported underlying effect. Compare the same concept across the two starting packages to test meaningful thematic variation without promising novel engine mechanics. Affinity-discovery rarity remains a separate accepted quality-linked concept; its distribution and experiment are deferred beyond this P1 stone test.

### Earned evolution and recognition

Meaningful practice, training, or consequential use supplies advancement evidence. Player attributes and basic-skill bonuses remain uncapped; affinity evolution still uses supported effects and explicit limits. Trivial unchanged repetition does not count as new advancement evidence. Improvements can specialize or trade one strength for another. Titles grant buffs; achievements award item prizes. Either earned record may independently be an explicit prerequisite for a future ability-upgrade option; neither automatically applies an upgrade or requires the other reward type.

[ASSUMPTION: G12 — P1 tests one earned variant after three distinct consequential uses of an existing ability plus one named earned achievement prerequisite. Show the revealed upgrade and tradeoff, then require the player's choice to replace the old version in its existing slot. Three repetitions of an identical resolved situation count once. The generated achievement awards one system-created utility item worth at most 5 gold; define its effect before award. Separately test one title granting +1 to a named basic-skill check once per simulated day, with no duplicate stacking and no automatic upgrade. Keep only one title and one achievement in this experiment.]

The prerequisite references the earned record, not continued possession of the prize. System-created rewards need explicit budgets; NPC rewards cannot conjure resources. Hidden advanced choices remain part of the vision. [ASSUMPTION: G13 — P1 uses one hinted upgrade: show a clue before qualification and exact requirements when revealed; record the condition before evaluating it. Full secret/hinted/visible tiers, rumor-based prerequisite advice, and discovery libraries are deferred.]

### Alchemy craft progression

Alchemy and Brewing skills level using the same XP and check system as all other basic skills (G03/G18). The additional mechanic specific to crafting is the **narrow upgrade track**: each distinct craft type maintains its own production count, and crossing a threshold unlocks a new *recipe* within that type — not a generic potency multiplier but a new capability with different effects. Unlocked recipes are offered to the player; declining re-offers at the next threshold crossing. Once adopted, the new recipe does not replace the base recipe; both remain available.

Upgrades expand *what can be crafted and what it does*, staying narrow to the product line. A player who crafts many health potions becomes capable of limb restoration — not generally better at all crafting.

**Healing track (Alchemy):**

| Tier | Recipe | Effect |
| --- | --- | --- |
| Base | Healing Draft | Removes one minor-wound condition impairing the recipient's actions |
| T1 unlock | Restorative Elixir | Removes a severe wound or crippling injury, including lost-limb conditions; cannot revive |
| T2 unlock | Draught of Revival | Administered to a deceased person within 120 seconds of their death; restores consciousness with critical injuries intact. One application per death event; additional doses on the same event have no effect |

**Mana-restoration track (Alchemy):**

Deferred pending a declared per-use affinity cost system. [ASSUMPTION: G19 — Base recipe would restore one exhausted affinity-ability use. Track design follows after cost system is specified.]

**Poison track (Alchemy):**

| Tier | Recipe | Effect |
| --- | --- | --- |
| Base | Weak Toxin | Applied to a weapon or food item; on contact or consumption, −2 to Perception and Athletics for 60 seconds. Persists on weapon until one contact event or 10 minutes; on food until consumed |
| T1 unlock | Potent Venom | −4 to Perception and Athletics, 120 seconds. Delivery mechanic identical to Weak Toxin |

Further tiers are not specified here; the track has no stated upper bound.

**Brewing track (Brewing):**

| Tier | Recipe | Effect |
| --- | --- | --- |
| Base | Common Ale | Drunk condition: −2 to Perception checks, +1 to a Presence check, duration 60 seconds |
| T1 unlock | Quality Ale | Reduced drunk condition: −1 to Perception, +1 to a Presence check, 60 seconds |
| T2 unlock | Artisan Brew | No drunk condition; grants a named social buff declared at recipe adoption: +2 to a chosen social skill for 120 seconds |

[ASSUMPTION: G19 — Proposed unlock thresholds: T1 = 10 successful craft events of that type; T2 = 25. Failed crafts do not count. Repeated identical attempts on an already-resolved craft (retry loop) do not count. These thresholds are proposals for tuning against session length and ingredient supply. All effect values above are draft proposals; all require correction before P1 implementation.]

### Difficulty curve and economy

P0 escalates from inspect/move → ordinary purchase/conversation → gift and plan change → uncertain request → report and downstream response. Increasing difficulty comes from competing constraints and uncertain information, not rising enemy levels.

[ASSUMPTION: G19 — P1 replaces the gift fixture with 30 starting gold and alchemy crafting as the player's primary economic activity (G14 superseded). Common alchemical ingredients are purchasable from an ingredient supplier at declared prices (draft: 1 gold per basic ingredient unit). One crafting attempt consumes a declared ingredient set and a work period; time advances by the work period using G04 rules. Successful crafts produce a persistent item in inventory; failed crafts consume ingredients with no output. Crafted items may be used personally, given to NPCs, or sold; NPC purchasing follows preference, affordability, and actual need — no guaranteed demand, no self-replenishing budgets. The ingredient supplier has a finite daily stock; restocking rules are deferred. External supplies and protection arrangements use explicitly bounded scenario contracts. The 10,000-gold test fixture never enters P1 economy.]

This tests crafting investment, ingredient economy, NPC need-driven demand, and personal use of crafted items at small scale. Upgrade thresholds, ingredient prices, NPC needs that crafted items can serve, and session-length assumptions are balance observations requiring P1 implementation specification.

## Simulation Specific Design

### Core simulation systems and management

Resources and obligations constrain NPC plans; executed plans create observations; encounters transmit claims; beliefs and relationships influence subsequent choices. Player transactions intervene in this cycle. Observe persisted changed behavior rather than assuming prose implies simulation.

Simulation advances only through game actions (G04). Routine schedules need no constant new narrative. Distant agents retain plans and consequences, but P0/P1 instantiate only four named NPCs. Controls support direct spending, agreements, and waiting; delegation and automated business management are later concerns.

### Building, economic loops, and unlocks

P0 supports ordinary purchases; P1 adds alchemy crafting using purchased ingredients with no stall, laboratory, or production chain (G19). The accepted long-term aspiration remains trees → timber → construction → brewing/distillation → bar operation → buyers and competitors with livelihoods. Brewing enters P1 as a personal crafting skill; the full production and distribution chain remains later vision. No construction, land-placement tool, factory chain, or magical business domain is included in P0/P1.

Progression combines player/skill levels, affinity/ability advancement, and opportunities; there is no city tech tree. Basic-skill access is universal. No passive offline income, infinite money source, or automatic daily budget refill is assumed.

### Emergence boundaries and end state

NPC decisions may surprise the player while respecting ownership, knowledge, obligations, and supported actions. Unsupported player proposals become recorded expansion candidates, not invented successful consequences. Preserve source state and proposals for diagnosis. Long-tail economy balance is unproven; measure resource creation/sinks and unmet needs across the compact scenario before expanding. This is one persistent scenario, with optional personal concerns and a central viability goal, not a procedural campaign or unrestricted creative sandbox. Victory does not reset the world.

## Level Design Framework

### Level types and progression

Use the G05 social triangle: public market for observation, stall for livelihoods/transactions, common room for contact and rumor. Each location serves a causal test; each NPC has a reason to move or remain. The player can follow people and revisit changed situations. P1 reuses the hub (G07); map expansion is not a prerequisite to multiple supported resolutions.

The first session exposes exits, one transaction, known needs, gift consequences, and the check's stakes before expecting the player to interpret social reports. Requested journal information restates known evidence without proactive action hints, a fixed order, or hidden motives. Record one unplanned supported player approach in P1 testing.

## Art and Audio Direction

### Art style

Readable text, dialogue, character sheet, journal, inventory, and optional roll log. Clear attribution distinguishes narrator, NPC speech, awards, and mechanical results. P0/P1 need no illustration, portraits, sprites, animation, or generated-image pipeline. [ASSUMPTION: G15 — Provide adjustable 16–24 px text, visible keyboard focus, speaker labels independent of color, and a quiet layout with no timed reading requirements.]

### Audio and music

No required music or audio assets. Every meaningful cue is textual; audio direction can be revisited if later scope warrants it. Achievement humor should not disrupt grounded consequences or mock the player's accessibility needs.

## Technical Specifications

### Platform and performance requirements

Local desktop-browser play with durable saves and an LLM connection as required by the eventual model choice. No engine, programming language, model, storage technology, server deployment, or provider is selected here. Architecture owns those choices and how authoritative state is implemented; full event sourcing is not a GDD requirement.

[ASSUMPTION: G16 — Evaluate a 60-minute, 100-action desktop session with four NPCs. Target visible input acknowledgement within 100 ms, local menus within 200 ms, save/load within 2 seconds, and 95% of completed LLM-mediated actions within 10 seconds; show a recoverable interruption by 30 seconds. Record browser and test-machine specifications. These are provisional usability targets, not measured results. Measure memory at session start/end for unexplained growth; defer a hard memory/FPS target because text interaction is the current workload.]

Log action latency, model calls/tokens, actual session cost, rejected proposals, duplicate-action attempts, and contradiction repairs. Acceptable dollar cost and provider choice remain open until measured play and Kyle's budget; do not invent a spending commitment. Preserve committed progress on interrupted requests and resume with clearly identified pending work.

### Content and asset budgets

Generated abilities and reusable rulings retain stable identities and recorded versions across sessions. Descriptions cannot silently change their mechanics; an intentional revision must be explicit and preserve which version governed earlier results. This does not prescribe a storage model.

P0: 3 location descriptions, 4 NPC profiles, 1 social conflict, 1 drink item plus gold, 1 uncertain-check situation, player/Persuasion XP and levels with attribute allocation, gift/no-gift and rumor test variants. P1 adds 2 affinity packages, 1 stone concept, at most 4 awakening candidates total, 2 rarity bands, 1 earned ability variant, 1 title, 1 generated achievement/prize, a set of alchemical base recipes and upgrade tracks, 3 daily quest slots, and 1 gacha pool with declared contents across 3 rarity tiers. Proposed P1 counts derive from G09/G11–G13/G19/G20. No generated catalogue or broad procedural content is necessary.

## Development Epics

Detailed high-level stories and evidence gates are in [epics.md](epics.md). These are design work packages, not scheduled implementation commitments.

| Epic | Title | Stage / pillars | Playable value |
| --- | --- | --- | --- |
| E1 | Act in a small persistent world | P0 / P-A, P-D | Navigate, transact, resolve the one check, gain XP, allocate points, save and resume |
| E2 | Make consequences travel through people | P0 / P-A, P-B, P-C | Gift changes a plan; contact spreads a fallible report |
| E3 | Secure Brackenford's future through play | Conditional P1 / P-A, P-B, P-C | Pursue two viable routes using alchemy crafting and community action |
| E4 | Earn a distinctive affinity ability | Conditional P1 / P-D, P-A | Choose, awaken, earn distinct rewards, and select an upgrade |
| E5 | Daily quest system and gacha rewards | Conditional P1 / P-A, P-D | Complete System-assigned daily objectives for XP and gacha item draws |
| E6 | Hidden bonus objectives | Conditional P2 / P-A, P-D | Trigger surprise bonus rewards by completing quests in unusual or creative ways |

Sequence E1 → E2 → P0 evidence gate → E3 → E4 → E5 → P1 review → E6 → P2 review. E5 depends on E3's alchemy system being operational; daily quests may include crafting objectives. E6 depends on E5 (quests must exist before bonus objectives can extend them). E3–E6 do not become P0 prerequisites.

## Success Metrics

### P0 evidence gate

1. Compare gift/no-gift from the same controlled initial state. Funds and ownership reconcile; Mara has a different feasible opportunity set. Her selected plan and observed behavior have a motive-based explanation, not a required retirement script.
2. Resolve the declared check at its declared difficulty. Record modifiers, die, total, pre-roll probability, XP, and committed consequence; verify natural 1 failure, natural 20 success, and zero XP for checks failing only on 1; narration agrees. Rejected/retried requests produce no duplicate mutation or new roll.
3. Verify Tessa's observation and later contact with Ivo. A non-witness knows nothing before receipt. Demonstrate a distorted or doubted claim changing a later choice without changing the original event.
4. Save/load preserves time in seconds, money, inventory, relationships, commitments, beliefs, plans, XP, levels, bonuses, and allocated/unspent points. Replaying captured proposals and rolls reproduces mechanical outcomes, without requiring identical new LLM prose.
5. Kyle can explain why the recipient changed plans and why the report recipient behaved differently. Record believability separately from mechanical consistency.

[ASSUMPTION: G17 — Run three controlled repetitions per P0 gift/no-gift pair and at least one rumor variant. Require zero unexplained authoritative contradictions or conservation/save failures before P1; correct and repeat the affected scenario on failure. These repetitions diagnose regressions, not statistical proof. For P1, exercise two plausible community routes and one unplanned supported approach; ask what changed, why people acted, what felt unfair, and what the player wants next. Use two voluntary return sessions by Kyle, plus friend feedback if available, as a signal for discussing expansion rather than an automatic release gate.]

### P0 timing, input, and growth evidence

On the same routes, distance/speed determines travel time and changing movement mode changes it; no flat adjacent-room cost remains. Compare a 2-word and 31-word exchange, a prepared gift and 100 individually counted coins, a one-minute silent wait and a clock-target overnight wait. Interrupt an event wait when an NPC actually orders or the silent-attention interval expires; loading/retrying never duplicates elapsed time. Verify no proactive action suggestions appear. Use fixed near-threshold saves to test XP award once, skill-bonus growth, allocatable attribute points, and old tasks becoming easy. A high-bonus fixture must exceed the old proposed attribute/skill caps without clamping; the 95% check yields zero XP. These are variations on existing actions, not additional P0 content.

### P1 progression and technical evidence

Verify an awakening occupies exactly one slot on one affinity; whole-set context changes the candidate description meaningfully; costs and results stay within supported limits. Compare ordinary/higher rarity through controlled trials, not by expecting rare outcomes in a few sessions. Title grants its buff; achievement grants its item; award alone never applies the upgrade; selling the prize preserves eligibility. A separately chosen, earned variant changes an ability without expanding its slot use.

Verify alchemy crafting: a declared attempt with correct ingredients and a passed check produces the stated item; a failed check consumes ingredients with no item; a poison applied to a weapon persists across save/load and triggers on the correct contact event. Verify craft-type threshold counts increment only on successful distinct events; reaching T1 reveals the next recipe; the player's choice to adopt or defer is recorded. Verify at least one healing tier and one brewing tier unlock through controlled play within a session of realistic length.

Verify daily quests: System assigns three quests at defined dawn interval with explicit success conditions displayed; fulfilled quests award correct XP to player and relevant skill; a gacha draw produces an item from the declared pool; partial completion or a retry of a resolved request does not award the reward again. Verify quests expire cleanly and are replaced at the next refresh. Verify that the System's voice is distinct from narrator and NPC voices. Verify that organic quest success conditions are equally visible in the journal. Ask whether visible success conditions feel clarifying or immersion-breaking; record Kyle's answer before expanding the quest pool.

Measure G16 targets and session cost during actual play. Stop expansion to investigate unexplained outcomes, irrelevant NPC memory, opaque progression, severe latency, or insufficient desire to return. No multiplayer, market, or scalability claim follows from these tests.

## Out of Scope

**P0 excludes:** magic/affinity implementation, titles, achievements, dedicated training activities beyond the existing-check XP/level test, community victory/ward pressure, businesses beyond one ordinary purchase, crafting, construction, combat, additional NPCs/locations, offline progression, and multiplayer. The ward may appear in setting text but creates no P0 subsystem.

**P1 excludes:** full affinity combinations/ranks, generated libraries of items/traps/spells, construction/production chains, the complete forest-to-tavern chain, additional settlements, broad social networks, tactical combat, and co-op. Alchemy-specific exclusions from P1: no alchemical laboratory or workspace construction; no ingredient harvesting or foraging system (ingredients are purchased); no recipe-discovery research system (only threshold-unlock progression); no multi-batch automated crafting; no player-run shop or stall for selling crafted items (direct NPC transactions only). Daily quest exclusions from P1: no penalty mechanic for expired quests; no quest streak or bonus multiplier; no player-configured quest preferences; no hidden bonus objectives (P2, G21). These are deferred ambitions or undecided systems, not hidden requirements for the slice.

**Explicitly removed or deferred by accepted decisions:** no class system or class roadmap; no code validation of affinity–concept thematic compatibility; place/domain/innkeeper powers deferred with no commitment to revisit. Ordinary business simulation remains part of the vision.

Procedurally generated locations are permanently excluded. Later hidden rooms, puzzles, traps, settlements, and the anonymous-gift test use deliberately authored places.

No public persistent multiplayer. A public v1.0 scope and post-launch roadmap are not established; neither should be inferred from the conditional later vision. Small co-op would first need explicit shared-time, concurrent-action, and conversation design after solo success.

## Decisions, Assumptions, and Dependencies

### G register

G IDs remain stable across corrections. Accepted rows are not assumptions. Mixed rows separate user-approved direction from inline provisional tuning. Every `[ASSUMPTION]` block maps to a row; associated G04 trial paragraphs are part of its provisional tuning.

| ID | Status | Current choice / remaining tuning |
| --- | --- | --- |
| G01 | Proposed | Household viability thresholds and three-day success window |
| G02 | Proposed | Seven-day ward pressure and recoverable supply losses |
| G03 | Accepted direction; tuning proposed | Natural 1/20; uncapped attributes/skills; player/skill levels; probability-based XP. Names, initial ratings/check fixture and anti-scaling policy remain provisional; XP curve in G18 |
| G04 | Accepted direction; tuning proposed | Seconds and contextual movement/speech/handling/event waits. Speeds, distances, exchange word-count aggregation/rounding, transfer fixture, 06:00 morning, and 60-second silence interval remain trial defaults |
| G05 | Accepted | Simple witnessed gift scenario; anonymous gift as later test |
| G06 | Accepted with correction | Free text; no visible action suggestions; factual navigation/information controls retained |
| G07 | Accepted with addition | Text lengths and small hub; never procedural locations; later hidden rooms/puzzles/traps |
| G08 | Accepted | Three saves, complete restoration, reload for branching tests; no cross-save progression carryover |
| G09 | Proposed; conflicting clause superseded | Two-affinity packages and two slots each; old no-XP clause removed |
| G10 | Proposed | Concern/commitment journal states |
| G11 | Proposed | Stone candidate pools, ownership choice, rarity odds and permanence |
| G12 | Proposed | Three uses + achievement gate, one variant/title/prize with bounded rewards |
| G13 | Proposed | One hinted affinity upgrade and reveal policy; no proactive action recommendations |
| G14 | Superseded by G19 | Drink-stall economy replaced; 30-gold start carried forward into G19 alchemy economy |
| G15 | Proposed | Text sizing and interaction accessibility |
| G16 | Proposed | Measured session and provisional responsiveness targets |
| G17 | Proposed | Controlled repetition and return-session evidence |
| G18 | Accepted direction (no failure XP); curve values proposed | Failures award zero XP; success awards `floor(100 * (0.95 - p) / 0.90)`; separate player/skill tracks; 100×level thresholds; one attribute point and one skill bonus per level; no caps |
| G19 | Proposed | Alchemy system: product categories (healing, mana-restoration, poison, brewing); narrow upgrade tracks with threshold-based recipe unlocks; T1/T2 thresholds, effect values, and ingredient economy; 30-gold P1 start; mana track deferred on affinity-cost system |
| G20 | Accepted direction (framing); details proposed | Daily quest system: fourth-wall-breaking LitRPG System interface with distinct voice; all success conditions visible; 3 daily slots, XP + gacha draw on completion, three rarity tiers (70/25/5%), no failure penalty; pool contents to be specified before P1 |
| G21 | Proposed (P2) | Hidden bonus objectives: LLM generates bonus conditions at quest creation (hidden from player); bonus rewards when player fulfills one via unusual, creative, or accidental approach; LLM judges qualification; rules validate bonus reward budget |

### Correction priorities and dependencies

G05–G08 no longer need the original correction pass. Review remaining G03/G04 tuning and G18 next, especially whether failures earn XP, progression pacing, contextual difficulty versus mastery, and the dialogue rounding minimum. The accepted uncapped-growth/level rules and seconds clock are not reopened by those tuning questions. P0 still has one check situation, three locations, four NPCs, and one social conflict; its growth test reuses that check and controlled saves.

All P1 assumptions can remain deferred while P0 is reviewed. Package effects, protection-contract costs, household inventory, rarity budgets, and reward behavior must be specified before their P1 implementation. G19 alchemy thresholds, effect values, ingredient prices, and NPC-need design must be specified before E3 implementation. G20 daily quest categories, gacha pool contents, and the fictional System framing must be specified before E5 implementation. Budget/acceptable session cost, weekly availability, delivery dates, model/provider, implementation stack, content boundaries, and public-release intent remain unset. Full skill mappings, training activities, combat, affinity replacement/respec, mature rarity distributions, and long-term unlock discovery await demonstrated need. The newly accepted player/skill leveling direction is not deferred away.

Draft 0.2 incorporates Kyle's corrections but remains a review draft with explicit tuning assumptions. Narrative detail and architecture are separate future workflows; no downstream work has been run.
