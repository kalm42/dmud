---
title: "dmud — Game Design Document"
game_type: text-based
secondary_genres: [rpg, simulation]
platforms: [desktop-browser]
created: 2026-09-07
updated: 2026-09-15
version: "0.8"
status: staged-design-baseline-approved
author: Kyle
sources:
  - ../../briefs/brief-dmud-2026-09-05/brief.md
  - ../../briefs/brief-dmud-2026-09-05/addendum.md
  - ../../briefs/brief-dmud-2026-09-05/.decision-log.md
  - ../../ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md
  - ../../ux-designs/ux-dmud-2026-09-08/.decision-log.md
  - ../../implementation-readiness-report-2026-09-12.md
---

# dmud — Game Design Document

**Approved staged design baseline (0.8):** P0 remains the approved initial implementation. P1–P4 separately prove effects/resources, access/ownership, survival needs, and autonomous livelihoods. The former community, alchemy, spell, quest, hidden-bonus, and combat work moves to P5–P9. Every later stage remains conditional on the preceding evidence gate; design approval does not authorize early implementation.

## Executive Summary

### Core concept

Live a self-directed fantasy life among people whose resources, obligations, knowledge, and relationships persist. Free-text intentions receive consistent consequences; history shapes a limited repertoire of affinity-awakened spells and recognition. An LLM interprets intentions, portrays NPCs, judges thematic fit, and narrates. The game rules own mechanical validation, dice, and authoritative state.

Brackenford is a frontier settlement with a deteriorating protective ward. Repair, protection agreements, or relocation may secure its future. Residents disagree for legitimate reasons. The world continues after the central problem is resolved.

### Target platforms and audience

Desktop browser, initially running locally; solo personal prototype by one developer with AI assistance. Kyle and interested friends are the first audience. Adult tabletop roleplayers and LitRPG readers are the intended broader audience, with 20–60-minute sessions and easy save/resume. Small-party co-op is conditional on solo success. Public release depends on play evidence; no release date, revenue target, budget, or staffing commitment exists.

### Distinctive design combination

- Creative intentions become supported, persisted consequences rather than narration alone.
- Needs become plans: NPCs pursue food, rest, safety, work, and relationships through physical actions, finite resources, and limited, fallible knowledge.
- Player history shapes affinity spells, title buffs, and achievement item prizes.
- Configurable, causally sourced effects let conditions, buffs, debuffs, and item treatments interact through shared rules.

These are design goals to prove together, not claims of technical feasibility or market novelty.

## Goals and Context

### Project goals and scope gates

| Stage | Deliverable | Boundary / promotion condition |
| --- | --- | --- |
| P0: causal-world proof | A gift changes one NPC's feasible plans; a report travels through contact; one uncertain check resolves; consequences survive save/load | Exactly one settlement, three locations, four named NPCs, one social conflict. Pass P0 evidence checks before expanding |
| P1: effects and resources | Derived Health, Mana, and Stamina plus configurable effects, magnitude budgets, stacking, removal, inspection, timing, and persistence | Conditional on P0. Prove one shared mechanical language before survival, crafting, spells, or combat depend on it |
| P2: places, access, and ownership | Local resources, doors, locks, keys, permission, shared beds, lockpicking, forced entry, theft, evidence, observations, and beliefs | Conditional on P1. Prove physical access and knowledge separation before needs-driven plans use private resources |
| P3: needs and shelter | Hunger, varied food crafting and spoilage, sleep pressure, beds/protection, `Exposed`, `Starved`, `Exhausted`, and deliberate player tradeoffs | Conditional on P2. Prove survival state and recovery without autonomous livelihood breadth |
| P4: autonomous livelihoods | Wants drive NPC plans through finite jobs, wages, shops, food preparation, lodging, relationships, and off-screen activity | Conditional on P3. Prove a complete need → plan → action → consequence → replan cycle |
| P5: community and alchemy | Brackenford's three-day lived-stability problem plus the approved alchemy system and multiple protection/relocation routes | Conditional on P4. Test sustained causal play and community outcomes before magic breadth |
| P6: spells and recognition | Approved affinity packages, awakening, spells, earned variant, title, and achievement | Conditional on P5. Test bounded history-shaped magic and recognition |
| P7: daily quests | Three System daily quests, visible success conditions, XP, and the nine-item gacha pool | Conditional on P6. Test whether explicit LitRPG structure complements free play |
| P8: hidden quest bonuses | One hidden bonus condition per supported quest and bounded surprise rewards | Conditional on P7. Test creativity recognition without opaque over-awarding |
| P9: combat proof | One authored one-on-one encounter using resources, effects, access rules, positioning, weapons, one combat spell, defeat, surrender/escape, rewards, and persistence | Conditional on P8. Prove readable deterministic combat before breadth |
| Later vision | Production, construction, broader magic and combat, additional settlements; possibly co-op | Separate scope decision after repeat play. No automatic promotion |

P0 tests causal credibility, not whether the complete game is fun. Its captured starting state gives the player one prepared pouch containing exactly 10,000 gold, provided only by the P0 test fixture. This is never an ordinary campaign starting balance or progression reward.

### Background and references

Preserve tabletop flexibility and universal skills without importing all D&D rules; comic achievement personality without copying Dungeon Crawler Carl's voice or setting; affinity/awakening inspiration from He Who Fights With Monsters without adopting exact ranks or powers; earned opportunities inspired by Azarinth Healer without classes; grounded lives and consequential gifts inspired by Kingdom Come: Deliverance 2. Dwarf Fortress is an additional design reference for histories and social information, not a promised simulation scope. These references come from the supplied sources; this draft does not assert independently verified behavior in those works.

### Authority of inputs

The brief supplies vision and staged scope; the addendum expands mechanics and scenarios; the source decision log resolves chronology. Latest user corrections in this GDD decision log take precedence over original inputs and older draft proposals, including dice, progression, time, input, and authored-location rules. Earlier class, place-power, thematic-validator, and merged-reward overrides remain active. Explicit source proposals and provisional numbers remain proposals even where surrounding direction is accepted. See [decision log](decision-log.md) for the reconciliation register.

## Core Gameplay

### Game pillars

| ID | Pillar | Design consequence |
| --- | --- | --- |
| P-A | Creative actions have consistent consequences | State-supported results, declared stakes, reusable rulings; never narrate an uncommitted success |
| P-B | Needs become plans | Physiological needs, personality, obligations, knowledge, and circumstances create wants; NPCs pursue them through concrete actions, finite resources, and real relationships, then replan from failure |
| P-C | Reputation travels through people | Reports require contact and motive; knowledge can distort or stop; beliefs never rewrite history |
| P-D | Limited powers reflect earned history | Uncapped attributes/skills reward long-term mastery; affinity slots limit the spell repertoire, not growth; distinct rewards and optional evolution preserve accomplishment |

### Core gameplay loop

Need, desire, or opportunity → inspect knowledge and resources → choose or form a feasible plan → act, travel, work, craft, converse, or transact over time → validate costs, uncertainty, and effects → commit changed resources, conditions, relationships, and world state → observe → continue or replan. NPC wants and personality choose among feasible plans. The player receives pressures and information but keeps control: skipping food or sleep may be worth the accepted consequences. P0 exercises P-A through P-C plus basic growth from P-D; later stages add the systems incrementally.

### P0 entry and Session 0

Opening dmud presents **New Game** and **Continue**. Continue opens the three-slot save selector when saves exist; when none exist, it remains visible but unavailable with an explanation. A save-index failure offers retry while New Game remains available.

New Game begins a zero-fictional-time Session 0 with Rowan. Rowan asks for the character's name, origin, cares, hates, especially cool ideas, and campaign hopes. The player authors the concept; Rowan suggests options only when explicitly asked for help. Rowan's review separates player-authored character facts, agreed campaign premises, preferences, and non-binding story hopes. The player can correct the review and stat assignment until explicit confirmation. Confirmation atomically establishes the character and initial world state, then opens at Market Square without predetermining an NPC decision, route, success, or campaign outcome.

“James” is the UX journey persona and example character name, not a fixed campaign protagonist. The player supplies the character's name in Session 0.

### Win/loss conditions

P0 ends when its evidence checklist is demonstrated; it has no campaign victory. Failure is a recoverable setback, not permadeath.

**G01 — approved P5 design:** P5 represents four one-resident households: Mara, Oren, Tessa, and Ivo. Each household has a concrete home location, local resources, a bed, and a protection state. Victory requires every household to complete three consecutive simulated days of lived stability: every resident eats through a recorded action before the next `Starved` threshold, completes adequate sleep using a bed in a protected place, and remains in a household that is not `Exposed`. Food, lodging, and protection must be funded or supplied by existing resources and commitments; promised income or food counts only after it is earned, transferred, produced, or contractually guaranteed. A failed day resets only that household's streak and causes no arbitrary loss. A ward repair costs 12 gold in materials and two completed four-hour work actions and provides 30 days of protection. A settlement-wide patrol contract costs 18 gold plus 1 gold for each of its first three days. Relocation costs 5 gold per household and succeeds only when a named destination accepts that resident. Stockpiles, farming, work, restaurants, hospitality, mixed solutions, and other supported plans qualify when they causally meet the same conditions.

**G02 — approved P5 design:** P5 starts with seven days of ward protection and exposes the remaining duration when inspected. Warnings at three days and one day interrupt long waits. Ward expiry removes that protection but never deletes food or deals automatic damage. A household's sleeping place is **Exposed** when it lacks valid protection: the state blocks G01 and prevents sleep there from qualifying as safe, but causes no direct character effect or inventory loss. Ward repair, a valid protection agreement, safe relocation, or another recorded equivalent removes the cause. Food leaves inventory only through a recorded event such as eating, transfer, theft, spoilage use, or destruction. Expiry causes no irreversible lockout; affected characters respond through the ordinary need-and-plan rules.

New supported solutions must meet the same conditions. Successful communities remain playable, including consequences of agreements, trade, and departures.

P5 preserves the original stakeholder disagreement within the four-person cast: Tessa's shopkeeping interest favors safe, dependable trade; Ivo is also a working craftsperson seeking overdue pay for prior work; and Mara sees relocation as a credible way to live nearer her ill sister. These pressures create starting positions rather than fixed decisions. Later events, offers, relationships, and survival needs may change any person's preferred route.

## Game Mechanics

### Intent, uncertainty, and outcome

The player enters an intention, not an authoritative state edit. Saying “I own this shop” does not transfer ownership. Routine feasible actions succeed without a roll; impossible or unsupported actions receive a factual explanation; offer alternatives only when the player asks for help. Social success cannot compel an NPC to abandon binding obligations or become obedient.

Before a consequential action, show reasonably knowable stakes, cost, and interpretation. Clarify rare-resource spending or materially changed intent. Fix difficulty before rolling and define mechanical success/failure consequences beforehand where practical; validate any contextual consequences proposed after resolution before committing them. Explain results using committed facts; hidden facts may remain hidden. A rejected proposal changes nothing. Retries of the same request cannot duplicate purchases, consume resources twice, or reroll a resolved action. Repeating an unchanged failed approach does not grant unlimited checks.

**G03 — approved P0 baseline:** On an eligible uncertain check, a natural 1 automatically fails and a natural 20 automatically succeeds; other results use `d20 + attribute modifier + relevant basic-skill bonus >= difficulty`. The five attributes are **Body, Agility, Constitution, Mind, and Presence**. Session 0 assigns the fixed standard array **8, 10, 12, 13, 14**, using every value exactly once. An attribute's modifier is `floor((score - 10) / 2)`. Confirmed starting-array assignments remain an immutable record; later earned attribute points increase current scores without rewriting that record. Attributes and skill bonuses have no design cap. Player levels award attribute points the player allocates; skill levels increase the corresponding bonus. Long-term play should allow godly competence and a feeling of being overpowered.

### Derived Health, Mana, and Stamina

**G22/G24 — approved P1 design:** Every character has integer current and Base Maximum resource pools derived from current raw attribute scores:

- `Maximum Health = Body × Constitution`
- `Maximum Mana = Body × Mind`
- `Maximum Stamina = Agility × Constitution`

New characters begin at all three maxima; existing P0 characters initialize all three pools to maximum when P1 begins. The four P1 NPC fixtures use the same standard array:

| Character | Body | Agility | Constitution | Mind | Presence | Max Health | Max Mana | Max Stamina |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Mara | 10 | 12 | 8 | 13 | 14 | 80 | 130 | 96 |
| Oren | 13 | 8 | 14 | 10 | 12 | 182 | 130 | 112 |
| Tessa | 8 | 13 | 10 | 14 | 12 | 80 | 112 | 130 |
| Ivo | 12 | 14 | 13 | 10 | 8 | 156 | 120 | 182 |

A permanent increase to Body, Agility, Constitution, or Mind recalculates each affected Base Maximum immediately and adds the same positive difference to the current pool, preserving damage or spent resources as an absolute deficit. A decrease recalculates the Base Maximum and clamps the current value to its Effective Maximum. Temporary check modifiers do not change a Base Maximum unless an effect explicitly says they do. **Effective Maximum** means the Base Maximum after active effects. Unless a rule explicitly says Base Maximum, every percentage restoration, current-pool cap, and percentage-of-maximum threshold uses the current Effective Maximum. Current values cannot fall below 0 or exceed their Effective Maxima; save/load restores every current value and verifies Base Maxima against saved attributes.

Spells spend the listed Mana when their effect commits. A character with insufficient Mana cannot cast: no effect, Mana cost, or fictional time is committed. Eight hours of adequate sleep as defined by G26 restores all Mana and 25% of Effective Maximum Health, rounded up. Ten uninterrupted minutes of non-strenuous rest restores 25% of Effective Maximum Stamina, rounded up. Time passage and eating alone restore none of the pools; consumables may declare restoration effects.

Stamina expenditure uses four bands: Routine 0, Exerting 5, Strenuous 10, and Extreme 20. Routine includes normal walking, conversation, inspection, and ordinary item use. Exerting includes combat movement up to 8 m, attacks, and defending. Strenuous includes sprinting up to 34 m, an escape attempt, and sustained heavy work. Extreme is reserved for exceptional validated feats. Casting normally spends Mana rather than Stamina unless a spell or effect declares otherwise. A character must pay the full cost before an action begins; rejection spends no time or partial Stamina. At 0 Stamina, the character cannot move or perform Stamina-costing actions but may talk, inspect, eat, use suitable items, and attempt sleep; this restriction overrides normally free walking. Zero Stamina is not lethal.

Health loss and wounds are related but distinct. Damage reduces current Health; a declared injury may also add a Minor or Severe Wound with its own penalty. Reaching 0 Health causes death. The former Downed/stabilization interval is superseded; revival remains available only through an explicitly supported effect within its declared window. Player defeat always offers recovery from a manual save; the default mode has no forced permanent-death deletion. NPC death persists unless a supported effect reverses it.

### Shared effects, conditions, buffs, and debuffs

**G24 — approved P1 design:** Conditions, buffs, debuffs, and item treatments use one configurable effect language. Within the budget and eligible targets established by the fictional source, the LLM may propose the effect's validated shape, target, name, description, duration, magnitude, and causally appropriate presentation. Every mechanical definition must declare source, source category, polarity, tier, magnitude, duration, removal, duplicate behavior, and player knowledge. Supported targets include Health, Mana, Stamina, effective maxima, checks, Defense, movement, damage, healing, and spell/action costs. Unsupported targets or over-budget values are rejected or reduced before commitment. Once accepted, the complete definition receives a stable identity and remains consistent.

Different named effects coexist. Each definition chooses one duplicate behavior: **Stack** applies every instance independently; **Refresh** retains magnitude and resets duration or uses; **Replace** keeps the stronger application. Generated effects receive one primary mechanical shape; explicitly authored effects may combine components when separately balanced. Ordinary modifiers resolve as `round(Base × (1 + sum of percentage modifiers)) + sum of flat modifiers`. Opposing percentages cancel, percentage stacks add rather than compound, and flat modifiers apply afterward. Health, Mana, Stamina, damage, and healing cannot fall below 0. Spell/action costs cannot fall below 1 unless an authored effect explicitly permits zero.

| Tier | Eligible source | Flat limit | Proportional limit | Total periodic-damage limit |
| --- | --- | ---: | ---: | ---: |
| Subtle | Ordinary maintenance, common materials, minor environments, plausible improvisation | ±1 | ±10% | 10 |
| Standard | Trained techniques, established recipes/spells, specialized tools/materials, serious hazards | ±4 | ±25% | 30 |
| Major | Rare materials/artifacts, major achievements/sacrifices, extreme hazards | ±20 | ±50% | 100 |

The fictional source fixes the maximum tier and eligible targets before a check. It also supplies an explicit maximum duration, number of uses, or terminating condition separate from the magnitude tier; if it supplies none, a generated effect is rejected rather than made indefinite. The LLM may propose any shorter duration within that source limit. Difficulty determines success, not effect magnitude; natural 20 does not raise the tier, natural 1 creates no effect, and repeated mundane actions cannot manufacture Major power. Every effect records a causal category—physiological, wound, poison, disease, magical, environmental, social, or item treatment—and can be removed only by its declared cause, a compatible category, or an exact-effect remedy. Food removes `Starved`; adequate sleep removes `Exhausted`; wound treatment removes linked `Bleeding`; antidotes remove compatible poison effects; dispels affect magical effects but never physiological or wound effects; and an item treatment ends through its declared physical removal or use limit. Numerically opposing effects remain present and expire independently even when their modifiers cancel.

P1's controlled fixtures are: `Sharpened`, requiring a whetstone, 10 minutes, and 5 Stamina for +1 weapon damage on the next 10 successful hits with Refresh; `Bleeding`, dealing 2 Health every 6 seconds for five ticks, with separate wounds stacking and treatment removing one linked instance; simultaneous +25%/−25% modifiers that cancel numerically while remaining distinct; and diagnostic-only `Star-metal Edge`, sourced from rare artifact-grade honing oil, which grants +20 weapon damage to the next successful hit within 10 minutes with Replace. A calibration matrix proposes every tier/shape combination at its exact limit and one unit or percentage point above it; exact-limit proposals validate and over-limit proposals are rejected or reduced before commitment. P1 proves all tier limits, generation validation, inspection, ordering, and save/load without hunger, sleep, autonomous livelihoods, alchemy, spells, or combat.

When multiple changes share a timestamp, resolve them in this order: (1) completed actions and continuous intervals in recorded commitment order, including meals, adequate sleep, healing, and treatments; (2) scheduled effect ticks and unmet need thresholds in stable creation order; (3) effect expirations and environmental transitions; then (4) recalculate Base/Effective values, clamp current pools, and apply terminal states such as death. An action completed exactly at the 24-hour hunger threshold prevents that `Starved` stack; adequate sleep completed exactly at the sleep threshold prevents that `Exhausted` stack; a treatment completed exactly on a Bleeding tick removes the linked effect before that tick; a final scheduled tick resolves before ordinary duration expiry. Protection that ends exactly when an eight-hour sleep interval completes was valid for that completed interval. No narration or later proposal may reorder committed events at the same timestamp.

The LLM sets a contextual difficulty target before rolling and may raise it to establish an appropriate effective success probability. The rules calculate the actual probability from that target and all applicable bonuses, including natural-roll overrides. With one fair d20, count natural 20 plus successful faces 2–19, then divide by 20: rolled probabilities run from 5% to 95% in 5-point steps. Record the pre-roll target, modifiers, probability, and stakes; never change difficulty after seeing the result. Routine feasible actions still need no roll, and impossible or mechanically unsupported intentions are screened before rolling. A natural 20 succeeds at the admitted stakes, not at an otherwise impossible action or unlimited NPC obedience.

P0 retains one controlled payment-extension check. Its evidence fixture assigns Presence 14 (+2) and Persuasion +1 against difficulty 12, for a total bonus of +3 and a 60% success probability. Ordinary Session 0 play may assign 14 to another attribute; the fixed mapping and +1 Persuasion bonus belong to the controlled evidence fixture, not a restriction on every player-authored character. Success secures a one-day payment extension; failure leaves the deadline unchanged and consumes only the exchange's actual duration, without reversing a gift. Difficulty reflects the attempted feat and circumstances. It must not increase for the same unchanged task merely to cancel an earned bonus; genuinely harder chosen feats may justify higher targets while familiar feats become easier through growth. Full mappings for skills not exercised by P0 remain later design work.

### P0 actions and time

**G04 — approved P0 baseline:** The shared action clock uses seconds. There is no mandatory six-second turn and no flat five-minute action cost. Travel, conversation, handling items, and waiting advance fictional time; typing, reading, model latency, menus, and inspecting known information do not. Distant NPC plans advance on the same clock; closing the game pauses it. Durations proposed by the LLM must fit actual distance, movement, handling, speech, and events, and be validated before time advances.

| Action | Time basis | Preconditions and outcome |
| --- | --- | --- |
| Inspect / inventory / known journal / save | 0 seconds | Known information only; saving does not heal or restore items |
| Move | Distance divided by applicable speed | Use known route distance and chosen walking, jogging, sprinting, crawling, or another supported mode; stop for meaningful events |
| Converse / uncertain request | Rendered spoken words and thinking time | Approved P0 formula below; never charge the whole narrative output as speech |
| Give / take / purchase | Contextual LLM estimate in seconds | One object can take seconds; counting 100 separate coins can take at least 100 seconds. Consent, ownership, stock, and funds still govern completion |
| Wait | Explicit duration, clock target, or event condition | LLM interprets intent and estimates; simulation determines actual elapsed time and whether the event occurs; interrupt for a response-worthy development |

Travel time is `distance / speed`, not `speed * distance`. Text descriptions can expose distance and travel mode without graphics. A next-room journey and a cross-town journey must not cost the same by default. NPC orders are decisions, not guaranteed timers: a waiting estimate must never manufacture the requested order.

**G04 — approved P0 fixture values:** Use metres and metres/second, rounding each completed travel segment up to a whole second. Ordinary-ground speeds are walk 1.4, jog 2.8, sprint 5.6, and crawl 0.5. The P0 routes are 7 m from Market Square to Mara's Stall and 140 m from Market Square to the Common Room; walking takes 5 s and 100 s. These values are authoritative for the controlled P0 content, not permanent speed caps for later worlds. Unknown routes or movement modes require a supported distance/speed ruling before travel. No stamina subsystem is needed for these short fixture routes; long sustained sprints require later rules.

For a completed dialogue exchange, total the rendered spoken words from the player and NPC and use `15 * ceil(words / 30)` seconds: roughly two words per second rounded upward to a quarter minute for thinking time. Any nonempty completed spoken exchange therefore has a 15-second minimum. Zero spoken words incur zero speech time; hesitation or silence is separately estimated. Thus 2 words take 15 s, 30 take 15 s, and 31 take 30 s. Count speech once across the exchange; exclude descriptive prose, player instructions, and model reasoning. Exchanges interrupted by events commit only the speech/action segments actually completed; never charge unspoken future dialogue.

LLM handling estimates state whether coins are individually counted or transferred in an already counted container. The P0 large-gift fixture uses a 5-second transfer of the player's prepared P0 test-fixture pouch, which contains exactly 10,000 gold; its gold value is not a count of loose coins and it adds no container subsystem. The purchase timing test and the gift/no-gift comparison are isolated fixture branches, each restored from the same captured P0 starting state. Spending 1 gold in the purchase branch therefore never reduces the pouch available at the start of the gift branch. In an interrupted transfer, completed time can elapse while funds/items remain untransferred until the agreed handover completes. Rejected interpretations and duplicate requests never double-charge time or resources. Purchases combine actual speech and handling time without counting either twice.

The campaign epoch is day 1 at 00:00, and a newly confirmed P0 campaign begins at second 28,800 (day 1 at 08:00); Session 0 advances zero seconds. For “wait until morning,” resolve the next 06:00 from the current world clock; 22:00 to 06:00 is 28,800 seconds. For “wait until the NPC orders,” advance through actual NPC decisions and stop when the order occurs. In a face-to-face wait, return control after 60 silent seconds with an observation that a minute passed, allowing the player to speak or continue. Do not interrupt an uneventful overnight wait every minute. If no event is scheduled or the target becomes impossible, report that state rather than waiting forever; the LLM's estimate is not an authoritative future fact. Rest, work, and crafting remain later activities.

### NPC agency and social information

Each named NPC has a need, competing desire, obligation, relationship, resources, current plan, and limited knowledge. A large gift changes the opportunity set; retirement, investment, debt payment, or refusal must follow that person's situation. Routine schedules and purchases proceed by rules; consequential replanning and dialogue use the LLM within recorded constraints.

Distinguish authoritative events, individual observations/received beliefs, and player-facing presentation. Beliefs retain source, time, uncertainty, and distortion. Gossip requires a plausible encounter and motive; non-witnesses do not learn events automatically. Truth need not be believed, and belief does not compel action. NPCs may lie or conceal motives consistently with what they know.

**G05 — accepted first-test scenario:** P0 uses this controlled social scenario: Mara, a stallholder owing 20 gold, wants to clear the debt but also visit her ill sister; Oren, the creditor, wants repayment and dependable trade; Tessa, a neighboring trader, observes the gift; Ivo, a courier and Tessa's friend, later meets her. Mara's decision affects Oren. Three locations are Market Square, Mara's Stall, and the Common Room. Market Square connects to each other location. Tessa meets Ivo in the Common Room 1,800 seconds after the gift opportunity, whether or not a gift occurs. The captured P0 starting state gives the player one prepared P0 test-fixture pouch containing exactly 10,000 gold and no other starting gold. Mara's stall holds 5 drinks priced at 1 gold each. The purchase test runs from its own reset of the captured state and may spend 1 gold. The large-gift and no-gift branches each reload the same captured state separately, so the gift branch begins with the untouched P0 test-fixture pouch and branch outcomes never merge. This funding exists only for P0 fixture evidence; it is not the campaign's assumed starting balance, a progression reward, or funding for any later-stage economy. A separate controlled rumor variant has Tessa suggest that the gift bought influence; Ivo's existing distrust makes him seek confirmation before favoring the player. This variant tests fallible belief, not automatic slander on every playthrough. Anonymous gifts, including sneaking gold to someone without revealing its source, are a desired later test; keep this first test witnessed and simple.

Observation, contact, received claim, and resulting action must be inspectable for testing. Player presentation must still respect limited knowledge. Follow-up dialogue and observed spending, changed schedules, or fulfilled obligations demonstrate memory; an internal “remembered” flag alone does not.

### Places, access, ownership, and evidence

**G25 — approved P2 design:** Resources are usable only where they physically exist and when the acting character can reach them. Ownership alone gives no remote access; lack of ownership does not make physical use impossible. Access may follow ownership, permission, relationship, a compatible key, an unlocked entrance, successful lockpicking, or forced entry. Doors and entrances record open, closed, locked, and broken states. Beds record capacity; every permitted occupant within capacity may receive adequate sleep. Unauthorized eating or sleeping still satisfies physiological rules when the resource and environment qualify, while trespass, theft, damage, noise, observations, beliefs, and relationship consequences persist.

Authoritative property state never grants NPC knowledge. Distinctive objects retain individual identity, possessor, legitimate claim, provenance, and recognizable marks. Fungible goods track quantities and causal transfer events but cannot be recognized as the stolen instance after mixing; equivalent restitution is possible. An unseen removal creates no knowledge. Later inspection can establish that an expected item is absent; comparison with remembered state can create a belief that something is missing. Theft and thief identity remain hypotheses until observations or inference support them. Witnessed access, damage, tampering, opportunity, motive, a newly possessed distinctive object, and inconsistent statements may produce suspicion, including mistaken accusations.

P2's controlled fixture is Ivo's Home. Its door has difficulty 12 and supports the four door states. Ivo and permitted guest Mara have matching keys; unlocking/opening takes 5 seconds without a roll. Lockpicking requires a pick, takes 60 seconds, and uses `Agility + Sleight of Hand` at difficulty 12. Failure consumes the pick; another pick permits another attempt. Forced entry takes 30 seconds and 10 Stamina and uses `Body + Athletics` at difficulty 14. Every attempt is loud; success leaves the door broken and open; another fully paid attempt is allowed. The bed has capacity two. Theft tests one fungible food serving and one distinctive marked object. Save/load preserves access state, keys, permission, possession, event history, observations, and beliefs. Formal guards, arrest, courts, and universal crime reputation are outside P0–P9.

### Needs, food, sleep, and survival conditions

**G26 — approved P3 design:** Every character records the last completed meal and last completed adequate sleep. The player receives needs as information and consequences, never forced intentions. NPC needs become planning pressure in P4.

Hunger priority is 0–8 hours satisfied; 8–16 low; 16–20 competing with ordinary work/leisure; 20–24 urgent enough to interrupt noncritical plans; and critical after 24, beneath only an immediate threat. At 24 consecutive hours without eating, apply one `Starved` stack and another after every additional 24 hours. `Effective Maximum Health = round(Base Maximum Health × 0.75^stacks)`. Applying a stack immediately clamps current Health without counting as damage. Eating one complete serving resets the timer and removes one stack; restored maximum does not heal current Health. If effective Maximum Health rounds to 0, Health reaches 0 and the character dies.

Sleep priority is 0–12 hours rested; 12–16 low priority to secure a bed and safe place; at 16 hours high priority to begin adequate sleep; and 20–24 critical enough to interrupt nonessential activity. At 24 consecutive hours without completing adequate sleep, apply one `Exhausted` stack and another after every additional 24 hours. `Effective Maximum Stamina = round(Base Maximum Stamina × 0.75^stacks)`. Applying a stack clamps current Stamina without counting as expenditure. Eight adequate hours reset the timer, remove one stack, and restore Stamina to the newly available maximum. `Starved` and `Exhausted` are authored multiplicative exceptions to ordinary percentage stacking.

Adequate sleep requires one continuous eight-hour interval with a usable bed and valid protection for the entire interval. Leaving the bed, a disruptive event, bed loss, or protection lapse makes the sleep inadequate. Inadequate sleep still restores ordinary Stamina per completed 10-minute rest interval but neither resets the timer nor removes `Exhausted`. Hunger and timed effects continue during sleep; thresholds apply without waking the character unless the effect/event explicitly wakes them. **Exposed** describes a sleeping place without valid protection. It blocks safe sleep and G01, deals no damage, and removes no food. A ward, protection agreement, safe relocation, or another supported equivalent prevents or removes it. A missing bed independently prevents adequate sleep without making a protected household Exposed.

One complete serving always resets hunger and removes one `Starved` stack. Food definitions vary in raw-edibility, ingredients, tools/facilities, preparation time, Stamina cost, yield, expiration duration, price, taste, preferences, and optional effects. Taste affects choice and willingness to pay, not the hunger timer. Calories, nutrients, and dietary-balance penalties are outside the current stages. Food uses one expiration timestamp per batch; storage does not alter it. A crafted batch receives `craft completion + recipe shelf life` regardless of ingredient age. Expired food remains edible and counts as a serving.

Unexpired food has no food-poisoning check. For expired food, calculate `risk = min(100%, 5% + 95% × time past expiration / declared shelf life)`, rounded to the nearest whole percent. A Constitution check uses the difficulty whose achievable failure chance is nearest that risk for the eater; natural 1/20 bounds actual failure probability to 5%–95%. Failure applies a generated physiological food-poisoning effect: Subtle through 25% of shelf life overdue, Standard above 25% through 75%, and Major above 75%. Success and failure use the ordinary success-only G18 XP curve; near-certain success yields negligible or zero XP.

| P3 food fixture | Inputs / tools / work | Yield | Shelf life from creation |
| --- | --- | ---: | ---: |
| Raw cabbage | Raw-edible; 10 minutes to eat | 1 serving | 7 days |
| Cabbage stew | Cabbage + water; hearth and pot; 30 minutes, 5 Stamina | 2 | 2 days |
| Pound cake | Flour + sugar + butter; oven; 60 minutes, 10 Stamina | 4 | 5 days |
| Sauerkraut | Cabbage + salt; crock; 15 minutes, 5 Stamina setup + 72 hours unoccupied fermentation | 4 | 30 days |
| Cooked meat | Raw meat; hearth and pan; 20 minutes, 5 Stamina | 2 | 2 days |
| Cured meat | Raw meat + salt; curing rack; 30 minutes, 5 Stamina setup + 48 hours unoccupied curing | 2 | 14 days |

Missing inputs or facilities reject preparation before costs commit. Routine known recipes succeed; substitutions and novel approaches use G03. Unoccupied curing/fermentation advances on the shared clock and persists through save/load.

The status view shows current/effective maximum Health, Mana, and Stamina; known effects with stacks, mechanics, sources, and removal; time since meal/sleep; and exact time to the next `Starved`/`Exhausted` stack. Messages state facts without recommending actions. Unknown effects expose symptoms until identified. Exact duration appears only when known or revealed by an ability such as Copper Sandglass.

### Autonomous livelihoods and wants-driven action

**G27 — approved P4 design:** Player and NPC characters use the same needs, pools, effects, and death rules. NPC wants are shaped by physiological pressure, personality, obligations, knowledge, relationships, resources, risk, and time. NPCs choose among feasible known plans using those factors; duration and resource cost matter but do not override personality, taste, relationships, or obligations. They execute every step physically on the shared clock and replan after failure rather than receiving invented resources. Off-screen action advances only with game time and spends the same inventory, gold, access, Stamina, and work time. Persistent off-screen death requires a complete causal chain. The player is interrupted only by reasonably perceivable events and otherwise discovers outcomes through later observation, absence, conversation, or rumor.

Hunger plans may eat accessible prepared food; prepare raw ingredients; buy ingredients or meals; visit a restaurant; ask for hospitality; borrow, trade, sell, or seek help; or obtain gold through work. Normal hunger favors owned and lawful options. Urgent hunger broadens socially costly alternatives. `Starved` or near-death states may make trespass, theft, lockpicking, or forced entry eligible only when personality, knowledge, fear, relationships, risks, and remaining alternatives support them. Need never automatically makes every NPC criminal or violent, and preventing starvation never erases consequences.

Sleep plans may return home, rent lodging, request hospitality, obtain or share a bed, repair shelter, secure protection, relocate, or first obtain the required resources through work or trade. They obey the same access, time, budget, relationship, and failure-replanning rules as hunger plans.

Jobs and professions are learned roles and simulated economic plans, not class restrictions or passive income. Work requires a known opportunity, place, time, and tools/inputs; goods, services, wages, expenses, and ownership change only through completed actions. Employers/customers have finite budgets and demand. Missed work, failed production, unavailable inputs, closure, or absent demand may prevent payment. Characters may change employers, take contracts, trade, borrow, seek help, or pursue illicit alternatives when supported by their state.

P4's controlled proof uses Ivo and Tessa. Ivo begins with 0 discretionary gold, 12 hours since food, and 12 hours since adequate sleep. Tessa's business has 12 gold and six 1-gold cabbages. A declared four-hour courier shift transfers 3 gold from Tessa to Ivo only on completion. Ivo can buy a cabbage, transferring 1 gold back, then prefers stew when time and his protected home's hearth/pot remain available but may eat it raw. His home also has a bed. Unavailable work, insufficient employer funds, sold-out stock, an unusable hearth, or lost protection triggers replanning. After eating, he pursues adequate sleep. This supersedes Ivo's unexplained 3-gold discretionary budget and adds no fifth named NPC.

### Alchemy and crafting

The player can declare an intent to craft an item, providing ingredients, a workspace, and a stated recipe or approach. Feasibility, available ingredients, required tools, and the player's current Alchemy or Brewing skill level govern whether the attempt is routine or uncertain. Routine crafts with known recipes and mastered techniques succeed without a roll; uncertain crafts use G03.

A successful craft produces a persistent item in inventory with explicitly stated effects. A failed craft consumes ingredients without output. Time advances by the declared work period using G04 rules. Applying a poison to a weapon or food item alters that object's properties until the coating is triggered or cleaned; the change persists across save and load.

Craft products fall into four categories, each with its own skill and upgrade track:

- **Healing and restorative potions** — consumable items that restore Health and, where stated, remove wound conditions.
- **Mana-restoration potions** — consumable items that restore Mana up to the recipient's maximum.
- **Poisons** — applied to weapons (contact-on-hit) or food (effect-on-consume). Delivery method affects which targets are exposed and how the effect is triggered.
- **Brewed drinks** — beer, spirits, and artisan beverages. Consumed for immediate condition effects; higher-tier brews replace debuffs with buffs.

**G19 — approved P5 design:** Alchemy and Brewing are universal basic skills with starting bonuses of 0. P5 begins with a Field Alchemy Kit, a Brewer's Crock, and knowledge of Healing Draft, Mana Draft, Weak Toxin, and Common Ale. Alchemy recipes require the kit; Brewing recipes require the crock. Known base recipes with exact inputs are routine. The controlled uncertain fixture substitutes one bruised duskroot for one basic ingredient in a Healing Draft and checks `d20 + Mind modifier + Alchemy` against difficulty 12; success creates the normal draft, failure consumes both ingredients with no output. Other substitutions or novel methods receive a declared contextual difficulty before commitment. Rules commit ingredients, time, item output, and XP atomically. The exact recipes, progression thresholds, economy, and NPC needs are defined below.

### Daily quest system

The System is a fourth-wall-breaking LitRPG-style interface that assigns daily objectives to the player. It speaks in a distinct voice — separate from the narrator, NPC speech, and award narration — and presents quests in a clean, system-style format with explicit success conditions visible from the moment a quest is assigned. The player always knows exactly what is required to complete each quest; the System does not hide objectives. This interface breaks the fourth wall deliberately and is consistent with the LitRPG genre conventions of the target audience.

Quests are visible in the journal, refresh at 06:00, and use the G10 states. Completing a daily quest awards 25 XP to the player track and 25 XP to the named relevant skill, then unlocks one gacha draw. Partial completion awards nothing; a resolved quest can reward only once.

A gacha draw selects one item from a known pool with tiered rarity. The pool contents are visible before drawing; the draw result is not. Items are general-use: ingredients, rare crafting components, scrolls, or unique one-use objects. No daily quest failure incurs a penalty beyond the reward not being earned; the quest expires and a new one replaces it at the next refresh.

P8 extends daily and organic quests with hidden bonus objectives (G21): see P8 scope and Development Epic E10.

**G20 — approved P7 design:** The System maintains three slots and replaces the entire set at 06:00. Each set contains one crafting quest (produce one named known recipe), one social quest (fulfill one accepted NPC commitment), and one observation quest (visit a named location and record one specified, previously unknown condition). Each quest expires at the next refresh without penalty. Combat quests remain outside the pool through the P9 proof and require a later design decision.

A gacha draw first selects a tier, then selects uniformly within that tier. The visible P7 pool is:

| Tier | Chance | Items and explicit value/effect |
| --- | ---: | --- |
| Common | 70% | Two basic ingredients (2 gold); Healing Draft (restore 25% Effective Maximum Health, 4 gold); Mana Draft (restore 25% Effective Maximum Mana, 4 gold); Common Ale (G19 effect, 3 gold) |
| Uncommon | 25% | Two rare catalysts (8 gold); Restorative Elixir (G19 effect, 10 gold); Mana Elixir (restore 50% Effective Maximum Mana, 10 gold) |
| Rare | 5% | Perfect Catalyst (substitutes for all ingredients in one known recipe, 15 gold); System Token (reroll one future gacha draw and accept the second result, 15 gold) |

**G21 — approved P8 design:** Each P8 quest receives exactly one hidden bonus condition at creation. Its stable private record names the unusual approach, qualifying evidence, evaluation point, and reward. The condition is never shown before or after resolution. Seeded rules choose the reward type uniformly at creation: XP, draw, or item. XP is a seeded integer from 10 through 25 awarded to both player and relevant-skill tracks; draw grants one extra G20 draw; item selects uniformly from the Common G20 items, all worth at most 5 gold. At the evaluation point, the LLM judges the committed evidence and rules reject or pay the fixed reward. Only one bonus can be paid per quest. The System notification is exactly `HIDDEN CONDITION SATISFIED — Bonus acquired.` followed by the reward, without an explanation of the condition.

### Controls and input

**G06 — accepted with correction:** Use free-text intentions with no visible suggested actions, recommended choices, dialogue replies, or action chips. Do not steer the player's decisions. Retain linked exits, inventory, journal, save/load, and optional roll details as factual navigation/information controls. Enter submits; Shift+Enter adds a line; all controls are keyboard reachable. Ambiguous names prompt neutral disambiguation. Unsupported verbs explain the limitation without consuming time or automatically presenting alternative actions.

Clarifications preserve the player's intent and identify missing information without recommending a strategy. Show pending/resolved/failed request state and a recoverable failure path; never imply that uncertain processing succeeded.

## Text-Based Specific Design

### Input system

Natural-language interpretation without proactive action suggestions; no exhaustive verb parser or promise of arbitrary mechanics. Synonyms map to the same supported intent. A multi-action request must expose order, stakes, and stopping conditions before consequential commitment; P0 can ask the player to submit its actions individually (G06).

### Room/location structure

P0 has exactly the three locations in G05, readable exits, present people, and examinable context. No maze, fast travel, or hidden-room puzzle is required in P0. **G07 — accepted:** Location introductions use 60–120 words; repeat visits use 20–60 words emphasizing changes. Typical action results use 40–120 words. P2 adds Ivo's Home as the access fixture; P3–P5 add the remaining authored household and livelihood locations required by their proofs. Locations are never procedurally generated: authored geography and connections remain stable while descriptions reflect actual changes. Hidden rooms, puzzles, and traps may be added in later tests within authored locations; none is added to P0.

### Item and inventory system

Ownership, possession, quantity, location, transferability, and the distinctive/fungible identity rules are authoritative. Scenery is examinable but not automatically takeable. P0 needs the player's single prepared P0 test-fixture pouch containing exactly 10,000 gold and Mara's five stocked drink items; no other starting gold, equipment grid, weight simulation, item-combination puzzle, or loot table is required. P1 adds effect fixtures; P2 adds keys, lockpicks, and local household property; P3 adds the food chain; later stages add the explicitly budgeted alchemy, magic, and reward items. Prize sale or loss does not erase the earned achievement record.

### Puzzle design

No authored puzzle chain in P0–P3. Challenges arise from conflicting needs, constrained resources, information, and agreements. Inspecting known facts is free; journal summaries remind the player of promises and known obstacles without exposing NPC secrets. No required solution depends on guessing an exact phrase.

### Narrative and writing

Grounded, emotionally credible NPC voices; achievements may be mischievous and opinionated, while not every accomplishment requires a joke. The system's award voice cannot decide an NPC's behavior or rewrite an event. An award about retirement is eligible only if retirement actually occurred, not merely because the player mentioned it.

Use the fixed starting conflict to compare playthroughs, then permit outcomes to emerge. No mandatory villain, fixed quest order, full branching script, or campaign ending sequence. Dedicated narrative design is a later offered step for room copy, character voices, lore, and vocabulary; no separate narrative document is produced here.

### Game flow and pacing

P0 should fit inside a 20–60-minute play session. For a new campaign, that budget includes Session 0 and the opening playable scene; returning sessions use the same target without Session 0. Each later proof should leave a personally interesting unfinished concern for another session. Manual save/resume restores the whole current situation. No offline progression. **G08 — accepted:** Provide three manual save slots; loading restores the world clock, ownership, inventory, relationships, commitments, beliefs, NPC plans, player/skill XP and levels, starting-array assignments, current attributes, and allocated/unspent attribute points. Replaying a captured starting state with captured proposals and seeded dice reproduces mechanical results; new LLM output may differ. There is no separate per-action undo. Reloading an older save is allowed for the personal prototype, specifically to compare diverging paths and repeat interactions. A loaded branch restores its own progression and clock; rewards from an abandoned branch do not carry across.

## RPG Specific Design

### Character system and basic skills

No classes, class unlocks, or class-evolution roadmap. Every character can attempt basic skills subject to feasibility, knowledge, tools, and context. P0 uses Body, Agility, Constitution, Mind, and Presence with the fixed 8, 10, 12, 13, 14 Session 0 array and the modifier rule in G03. The starting skill vocabulary is Athletics, Acrobatics, Sleight of Hand, Stealth, Arcana, History, Investigation, Nature, Religion, Animal Handling, Insight, Medicine, Perception, Survival, Deception, Intimidation, Performance, and Persuasion. P5 extends this with Alchemy (potion and poison crafting) and Brewing (fermented and distilled drinks); both are universal and subject to the same feasibility, knowledge, and tool requirements as all other basic skills. These categories do not import the full D&D ruleset or its six attributes.

P0 exercises only Presence + Persuasion (G03); other ordinary feasible actions are never locked behind affinity slots, titles, achievements, or stones. Unsupported complex checks receive an honest limit, not a claim that the character must unlock a basic skill. Unbounded growth, player levels, skill levels, and the P0 XP curve below are accepted. P2 first exercises Agility + Sleight of Hand and Body + Athletics; P3 exercises Constitution resistance; P9 adds the first combat-skill mappings; broader mappings, dedicated training activities, and profession-specific crafting adjudication remain later design work.

### Inventory and equipment

P0 uses the ownership rules above, with no combat equipment. **G09 — approved P6 design:** P6 offers exactly two starting packages. Each grants two affinities with two spell slots per affinity, one basic-skill bonus, and one starting spell:

| Package | Skill bonus | Starting spell |
| --- | --- | --- |
| Ember + Fellowship | +1 Survival | **Hearthspark** (Ember slot): 8 Mana, 10 m, 10 minutes; ignite, extinguish, or sustain one hand-sized nonmagical flame or safely warm one held object; no direct combat damage in P6 |
| Vessel + Fellowship | +1 Medicine | **Steady Vessel** (Vessel slot): 8 Mana, self, 120 seconds; suppress the action penalty from one Minor Wound without removing the wound or restoring Health |

Bonuses do not stack with themselves. Spells always state owner, slot, Mana cost, range, duration, targets, and effect.

The player chooses affinities among discoveries; substantially random rarity affects quality. Limited slots belong to each affinity, not a single global pool. A stone expresses its concept through one affinity into one available slot, with the entire affinity set influencing the result. Uncertainty concerns the acquired spell, not arbitrary unreliability whenever it is cast. Awakening and earned evolution are separate systems.

### Quest system

Needs, conflicts, and negotiated agreements create quests; no fixed quest sequence is required. All quests — whether organic (from NPC needs and player commitments) or System-assigned daily objectives — display explicit success conditions when accepted. The player can inspect these at any time from the journal. Hidden information (NPC motives, available resources, what an NPC will actually do) remains hidden; the success *conditions* the player must meet are not. A quest that cannot state its success condition is not a quest — it is an unresolved situation to be tracked as an open concern.

**G10 — approved P5/P7 design:** The journal tracks known concerns and explicit commitments as proposed → accepted → fulfilled, failed, expired, or abandoned, with renegotiation recorded as a changed agreement. Acceptance records the required outcome, involved parties, deadline if any, evaluating authority, and exact reward or lack of reward in plain language. NPC rewards require actual fulfillment and owned or already promised resources; System rewards follow G20. Community victory is evaluated from G01 conditions rather than quest flags.

Daily System quests (G20) are tracked in the same journal under a distinct category. They are assigned by the System rather than negotiated with an NPC, but their completion is evaluated by the same rules: actual fulfillment of the stated objective, not a declaration. System rewards (XP and gacha draw) are delivered by the System on confirmation of fulfillment; they cannot be claimed on partial completion or by exploiting retried requests.

### World, NPCs, dialogue, and combat

Brackenford is the hub; schedules and off-screen consequences share game time. Dialogue uses individual knowledge and commitments. NPC relationships are contextual, not a universal “gift enough money = obedience” meter. P0 requires no companion party, merchant network, travel region, tactical encounter, weapon kit, or enemy roster. P1 introduces resources/effects; P2–P5 add local places, livelihood trade, and community play without an enemy roster. P9 adds the first bounded combat encounter under G23.

### Combat proof — conditional P9

**G23 — approved P9 design:** P9 contains one authored one-on-one encounter that begins with the opponents 10 m apart. Roll initiative once as `d20 + Agility modifier`; ties go to the higher Agility score, then to the player. A combat round represents six fictional seconds. On a turn, an actor may move up to 8 m and take one action: attack, cast, use an item, defend, sprint, attempt escape, or offer surrender. Sprint uses the action to move up to 34 m. Outside combat, G04's contextual clock remains unchanged.

Attacks use G03 natural-roll rules against `Defense = 10 + Agility modifier + armor bonus`. Melee uses `Body modifier + Melee`, ranged weapons use `Agility modifier + Ranged`, and targeted combat spells use `Mind modifier + Arcana`. Melee and Ranged are universal P9 basic skills starting at +0. Defend grants +2 Defense until the actor's next turn. Armor changes Defense only. Prototype damage is unarmed `4 + Body modifier`, sword `8 + Body modifier`, and bow `8 + Agility modifier`, each with a minimum of 1. Moving, attacking, and defending each cost 5 Stamina; sprinting and escape attempts cost 10. Insufficient Stamina rejects the action without partial commitment.

The controlled player fixture is separate from the live campaign. It uses Body 12, Agility 13, Constitution 14, Mind 10, Presence 8; Health 168/168; Mana 120/120; Stamina 182/182; Arcana, Melee, and Ranged +0; no armor; a sword and bow; and the Ember + Fellowship package with Hearthspark occupying the first Ember slot. The second Ember slot holds **Cinder Lance**: 12 Mana, 10 m, instantaneous; make a `Mind modifier + Arcana` spell attack and deal `12 + Mind modifier` Health damage on success, minimum 1. A miss spends the Mana because the cast committed. The fixture has no Rest-stone spell and does not alter the live character. Other P6 spells retain their listed utility effects. Costs, damage, current pools, positions, action order, conditions, and item use commit atomically and survive save/load.

The authored opponent is a lone road robber with Body 12, Agility 10, Constitution 10, Mind 8, Presence 10, Melee +1, Defense 10, Health 120, Mana 96, Stamina 100, and a sword dealing 9 damage. The robber offers surrender at or below 25% Effective Maximum Health and accepts the player's surrender unless a prior recorded event establishes otherwise. An actor escapes after reaching more than 20 m separation and spending an action to flee. Defeat or robber surrender awards the one-time 5-gold purse. Escape awards no purse. On player surrender, the robber takes up to 5 owned gold and leaves; no purse is awarded. Meaningful combat checks use G18 XP when they resolve and are never revoked, but there is no separate encounter-completion XP. Replaying or reloading the same resolved threat cannot award XP or transfer the purse again. At 0 Health the character dies; revival, potions, wounds, effects, Stamina, and rest use G19/G22/G24/G26.

## Progression and Balance

### Player and skill levels — G03 accepted direction

Attributes and skill bonuses have no design maximum. Player level-ups give allocatable attribute points; skill level-ups increase that skill's bonus. Levels do not introduce classes, gate universal basic-skill access, add affinity slots, or automatically evolve an affinity spell. Long-term mastery should let the player overpower familiar challenges; demanding new feats remain available.

XP depends on the actual pre-roll success probability: lower success probability gives greater XP on success. **All failed checks award zero XP.** A check that can fail only on natural 1 also gives zero XP on success, and a routine no-roll action earns no check XP. Include all applicable bonuses when computing probability; do not compute rewards from nominal difficulty alone. Rejected actions, retries of an already resolved request, and repeated unchanged attempts do not create XP opportunities.

**G18 — approved P0 baseline:** Keep P0's scope to the existing check, one player XP track, one Persuasion XP track, and an attribute-allocation control. A successful meaningful check awards `floor(100 * (0.95 - p) / 0.90)` XP to both applicable tracks, with `p` calculated by counting successful d20 faces before the roll. Failures award zero XP. A 95%-success check awards zero XP on either outcome. Player and skill tracks start at level 1 with 0 XP. Reaching the next level costs `100 * current level` XP, consumes that threshold, and carries excess; repeat if multiple levels are crossed. Each player level grants one point to allocate as +1 to an attribute; each skill level grants +1 to that skill's bonus. No maximum level, attribute, or skill bonus is imposed.

Success at 95%, 60%, and 5% gives 0, 38, and 100 XP; failures always give 0. P0 can start a separate controlled save near a threshold to test leveling without adding encounters or grinding. Save XP, levels, current bonuses, and unspent points; one resolved check awards only once. Player-chosen bonus suppression or deliberately contrived retries do not create a new XP opportunity when the fictional approach and circumstances are unchanged.

### Awakening experiment — conditional P6

**G11 — approved P6 design:** P6 contains one Rest-concept awakening stone. When acquired, its rarity is rolled and retained: standard 80%, resonant 20%. Before use, show that the stone will choose uniformly between the two candidates supported by the character's package. Each candidate has a fixed owning affinity and requires one free slot in it; if either result cannot fit, the stone cannot be used and remains in inventory. A valid use consumes the stone and awards the selected spell permanently. P6 has no respec or replacement outside the earned G12 evolution.

| Package / owner | Standard spell | Resonant improvement |
| --- | --- | --- |
| Ember + Fellowship / Ember | **Banked Warmth:** 12 Mana, self or one target within 5 m; after 10 uninterrupted minutes of rest, restore 25% Effective Maximum Health, rounded up; once per target per day | Restore 40% Effective Maximum Health |
| Ember + Fellowship / Fellowship | **Shared Vigil:** 10 Mana, one willing ally within 10 m, 120 seconds; caster and ally each gain +1 to Perception and Insight while they remain within 10 m | Bonus becomes +2 |
| Vessel + Fellowship / Vessel | **Quiet Reservoir:** 12 Mana, self; after 10 uninterrupted minutes of rest, restore 25% Effective Maximum Mana, rounded up; once per day | Restore 40% Effective Maximum Mana |
| Vessel + Fellowship / Fellowship | **Lend Strength:** 12 Mana, one willing ally within 5 m, 120 seconds; ally gains +2 on Body-based checks while caster takes −2 on Body-based checks | Ally bonus becomes +3; caster penalty remains −2 |

The rules select the fixed result; the LLM generates its player-facing spell name and one-sentence manifestation from the Rest concept, owning affinity, full affinity set, Session 0 character concept, and committed history. Those generated details may change presentation but never the table's effect. Rules validate ownership, capacity, prerequisites, effects, costs, and limits. The stone's retained rarity is the only P6 magic-rarity roll; mature affinity-discovery rarity remains later scope.

### Earned evolution and recognition

Meaningful practice, training, or consequential use supplies advancement evidence. Player attributes and basic-skill bonuses remain uncapped; spell evolution uses supported effects and explicit limits. Repetition of an identical resolved situation counts once. Titles grant buffs; achievements award item prizes; neither automatically changes a spell. Later spell upgrades may name either an earned title or an achievement as a prerequisite; P6 tests the achievement path only.

**G12 — approved P6 design:** The awarded Rest spell gains one optional **Deepened** variant after three distinct consequential uses and the internally recorded **Rest Is Part of the Work** achievement. That achievement requires completing a timed accepted commitment after the Rest spell materially enabled recovery during the attempt. The LLM generates a 2–6-word player-facing achievement name and one sentence tied only to the committed event; rules retain the internal ID and fixed trigger. It awards a **Copper Sandglass**, worth 5 gold, which once per day reveals the exact remaining time on one known effect or commitment. Selling or losing it does not erase the achievement. Meeting G01 earns the nonstacking title **Brackenford's Anchor**, which grants +1 to one Persuasion check per simulated day.

Deepened replaces the original spell in the same slot only after explicit confirmation: Banked Warmth costs 16 Mana and restores 50% Effective Maximum Health but becomes self-only; Shared Vigil costs 14 Mana and doubles its duration but can affect only Perception; Quiet Reservoir costs 16 Mana and restores 50% Effective Maximum Mana; Lend Strength costs 16 Mana and gives +4 to the ally while imposing −3 on the caster. The original remains unchanged if the player declines.

**G13 — approved P6 design:** After the first qualifying consequential use, show the clue, `Rest deepens when recovery protects a promise.` Do not expose a checklist. Once the third distinct use and the achievement are recorded, reveal the exact Deepened variant, cost, tradeoff, and replacement choice. Secret upgrade libraries, rumor-based prerequisite advice, and other reveal modes remain later scope.

### Alchemy craft progression

Alchemy and Brewing skills level using the same XP and check system as all other basic skills (G03/G18). The additional mechanic specific to crafting is the **narrow upgrade track**: each distinct craft type maintains its own production count, and crossing a threshold unlocks a new *recipe* within that type — not a generic potency multiplier but a new capability with different effects. Unlocked recipes are offered to the player; declining re-offers at the next threshold crossing. Once adopted, the new recipe does not replace the base recipe; both remain available.

Upgrades expand *what can be crafted and what it does*, staying narrow to the product line. A player who crafts many health potions becomes capable of limb restoration — not generally better at all crafting.

**Healing track (Alchemy):**

| Tier | Recipe / inputs / work | Effect / value |
| --- | --- | --- |
| Base | Healing Draft; 2 basic ingredients; 30 minutes | Restore 25% Effective Maximum Health, rounded up, and remove one Minor Wound; 4 gold |
| T1 | Restorative Elixir; 2 basic + 1 rare catalyst; 60 minutes | Restore 50% Effective Maximum Health and remove one Severe Wound or crippling injury, including a lost-limb condition; cannot revive; 10 gold |
| T2 | Draught of Revival; 3 basic + 2 rare catalysts; 120 minutes | Administer within 120 seconds of death; return at 25% Effective Maximum Health with Severe Wounds intact; once per death event; 24 gold |

**Mana-restoration track (Alchemy):**

| Tier | Recipe / inputs / work | Effect / value |
| --- | --- | --- |
| Base | Mana Draft; 2 basic ingredients; 30 minutes | Restore 25% Effective Maximum Mana, rounded up; 4 gold |
| T1 | Mana Elixir; 2 basic + 1 rare catalyst; 60 minutes | Restore 50% Effective Maximum Mana, rounded up; 10 gold |
| T2 | Deepwell Tonic; 3 basic + 2 rare catalysts; 120 minutes | Restore to Effective Maximum Mana; 18 gold |

**Poison track (Alchemy):**

| Tier | Recipe / inputs / work | Effect / value |
| --- | --- | --- |
| Base | Weak Toxin; 2 basic ingredients; 30 minutes | Weapon contact or consumption deals 10 Health damage and gives −2 to Perception and Athletics for 60 seconds; one contact or 10 minutes on a weapon; persists on food until consumed; 4 gold |
| T1 | Potent Venom; 2 basic + 1 rare catalyst; 60 minutes | Deals 20 Health damage and gives −4 to Perception and Athletics for 120 seconds; same delivery rules; 10 gold |
| T2 | Lingering Bane; 3 basic + 2 rare catalysts; 120 minutes | Deals 10 Health damage immediately and after each of the next two 60-second intervals; gives −4 to Perception and Athletics for 180 seconds; same delivery rules; 18 gold |

**Brewing track (Brewing):**

| Tier | Recipe / inputs / work | Effect / value |
| --- | --- | --- |
| Base | Common Ale; 1 basic ingredient; 60 minutes | −2 Perception and +1 to one Presence-based check for 60 seconds; 3 gold |
| T1 | Quality Ale; 2 basic ingredients; 120 minutes | −1 Perception and +1 to all Presence-based checks for 120 seconds; 6 gold |
| T2 | Artisan Brew; 2 basic + 1 rare catalyst; 240 minutes | No Perception penalty; +2 to one social skill selected when this recipe is adopted, for 120 seconds; 12 gold |

Each product track unlocks T1 at 10 successful crafts and T2 at 25 total successful crafts in that track. Failed attempts and replayed requests for an already resolved attempt do not count. The counters, known recipes, and accepted or declined unlock offers persist. A declined unlock is offered again after the next successful craft in that track.

### Difficulty curve and economy

P0 escalates from inspect/move → ordinary purchase/conversation → gift and plan change → uncertain request → report and downstream response. Increasing difficulty comes from competing constraints and uncertain information, not rising enemy levels.

P5 starts from an independent controlled state with 30 gold; the P0 test-fixture pouch and every P0 branch outcome are discarded before this economy begins. The ingredient supplier charges 1 gold per basic ingredient and 4 gold per rare catalyst, holds at most 20 basic and 4 rare units, and restocks up to those limits at 06:00 rather than adding stock without limit. Food uses the P3 recipe/serving system and P4 finite sellers rather than an abstract daily food-unit stock. Purchases, crafting inputs, work time, outputs, and failures follow the atomicity and time rules above.

Demand is need-driven and finite. Mara begins P5 with one Minor Wound and 4 gold reserved for at most one Healing Draft. Ivo may consider one Common Ale only after a completed courier shift leaves him with the required owned funds; no unexplained discretionary balance is created. Other characters buy a crafted item only after a recorded event creates a compatible need and only from owned funds; no NPC budget refills automatically. The player may use or give any product, but a gift is not a sale.

This tests crafting investment, ingredient economy, NPC need-driven demand, and personal use at small scale. The values above are the P5 baseline to measure and revise after its evidence gate.

## Simulation Specific Design

### Core simulation systems and management

Needs, desires, and opportunities create priorities; knowledge, personality, relationships, access, resources, risk, and time constrain feasible plans. Executed actions change physical state and create only the observations they plausibly expose. Encounters transmit fallible claims; outcomes create new wants or replanning. Player actions intervene in the same cycle. Observe persisted behavior and resource flow rather than assuming prose implies simulation.

Simulation advances only through game actions (G04); closing the game pauses it. Routine schedules need no constant narration. Distant agents retain plans and consequences, and all current stages keep the same four named NPCs. Off-screen plans spend real time/resources and can end in conditions, immobility, or death, but the player learns only through plausible observation/contact. Controls support direct spending, agreements, and waiting; player-delegated automated business management remains later scope.

### Building, economic loops, and unlocks

P0 supports one ordinary purchase. P3 adds the bounded food-production chain; P4 adds finite work, wages, shops, and restaurant/lodging alternatives; P5 adds personal alchemy using purchased ingredients with no laboratory or automated batch system (G19). The long-term aspiration remains trees → timber → construction → brewing/distillation → bar operation → buyers and competitors with livelihoods. No construction, land-placement tool, factory chain, or magical business domain is included through P5.

Progression combines player/skill levels, affinity-spell advancement, and opportunities; there is no city tech tree. Basic-skill access is universal. No passive offline income, infinite money source, or automatic daily budget refill is assumed.

### Emergence boundaries and end state

NPC decisions may surprise the player while respecting ownership, knowledge, obligations, and supported actions. Unsupported player proposals become recorded expansion candidates, not invented successful consequences. Preserve source state and proposals for diagnosis. Long-tail economy balance is unproven; measure resource creation/sinks and unmet needs across the compact scenario before expanding. This is one persistent scenario, with optional personal concerns and a central viability goal, not a procedural campaign or unrestricted creative sandbox. Victory does not reset the world.

## Level Design Framework

### Level types and progression

Use the G05 social triangle: public market for observation, stall for livelihoods/transactions, common room for contact and rumor. P2 adds Ivo's Home; P3–P5 add only the authored homes, workplaces, food facilities, and protection destinations required by their proofs. Each location stores its actual occupants, resources, entrances, access, and facilities. The player can follow people and revisit changed situations; no procedural map expansion is allowed.

The first session exposes exits, one transaction, known needs, gift consequences, and the check's stakes before expecting the player to interpret social reports. Requested journal information restates known evidence without proactive action hints, a fixed order, or hidden motives. Record one unplanned supported player approach at each later evidence gate.

## Art and Audio Direction

### Art style

Readable text, dialogue, character sheet, journal, inventory, effect list, and optional roll log. Clear attribution distinguishes narrator, NPC speech, awards, and mechanical results. None of P0–P9 requires illustration, portraits, sprites, animation, or a generated-image pipeline. **G15 — approved presentation target:** defer preferred text sizing to the browser rather than provide an in-game text-size control. Preserve the user's browser text-size and zoom choices without loss of content or functionality, including 200% page zoom and reflow at the equivalent of 320 CSS px without two-dimensional page scrolling except for intrinsically two-dimensional content. Provide visible keyboard focus, speaker labels independent of color, and a quiet layout with no timed reading requirements.

### Audio and music

No required music or audio assets. Every meaningful cue is textual; audio direction can be revisited if later scope warrants it. Achievement humor should not disrupt grounded consequences or mock the player's accessibility needs.

## Technical Specifications

### Platform and performance requirements

Local desktop-browser play with durable saves and an LLM connection as required by the eventual model choice. No engine, programming language, model, storage technology, server deployment, or provider is selected here. Architecture owns those choices and how authoritative state is implemented; full event sourcing is not a GDD requirement.

**G16 accepted duration:** The endurance evaluation runs for 60 minutes of wall-clock time, targets approximately 100 representative actions with four active NPCs, and records simulated seconds advanced as a separate result.

**G16 — approved evaluation targets:** visible input acknowledgement within 100 ms, local menus within 200 ms, save/load within 2 seconds, and 95% of completed LLM-mediated actions within 10 seconds; show a recoverable interruption by 30 seconds. Record browser and test-machine specifications. After the initial scene has loaded, the browser process's resident memory at the end of the 60-minute run may be no more than 100 MB above that baseline and must not show monotonic per-action growth. The text workload has no separate FPS target.

Log action latency, model calls/tokens, actual session cost, rejected proposals, duplicate-action attempts, and contradiction repairs. Acceptable dollar cost and provider choice remain open until measured play and Kyle's budget; do not invent a spending commitment. Preserve committed progress on interrupted requests and resume with clearly identified pending work.

### Content and asset budgets

Generated spells and reusable rulings retain stable identities and recorded versions across sessions. Descriptions cannot silently change their mechanics; an intentional revision must be explicit and preserve which version governed earlier results. This does not prescribe a storage model.

P0 contains 3 location descriptions, 4 NPC profiles, 1 social conflict, 5 stocked copies of 1 drink item, the player's single prepared P0 test-fixture pouch containing exactly 10,000 gold, 1 uncertain-check situation, player/Persuasion growth, and isolated purchase, gift/no-gift, and rumor branches. P1 adds three resource pools, one configurable effect schema, three duplicate policies, eight source categories, three magnitude tiers, the Sharpened/Bleeding/opposed-modifier/Star-metal Edge fixtures, and one tier-by-shape boundary matrix. P2 adds Ivo's Home, one door and lock, two keys, one capacity-two bed, lockpick and forced-entry actions, one fungible theft item, and one distinctive theft item. P3 adds hunger/sleep clocks, Starved/Exhausted/Exposed, six food fixtures, and spoilage checks. P4 adds one courier job and Ivo's bounded eat/cook/sleep plan through Tessa's finite business. P5 adds four concrete households, lived-stability tracking, protection routes, 12 alchemical recipes across 4 tracks, and the bounded ingredient economy. P6 adds 2 affinity packages, 1 stone concept, 4 awakening candidates, 2 rarity bands, 1 earned spell variant, 1 title, and 1 generated achievement presentation with a fixed trigger/prize. P7 adds 3 daily quest slots and 1 nine-item gacha pool. P8 adds one hidden condition per quest and three bounded reward forms. P9 adds 1 authored opponent, 3 mundane attacks, 1 combat spell, and 1 encounter space. No generated catalogue or broad procedural geography is required.

## Development Epics

Detailed high-level stories and evidence gates are in [epics.md](epics.md). These are design work packages, not scheduled implementation commitments.

| Epic | Title | Stage / pillars | Playable value |
| --- | --- | --- | --- |
| E1 | Enter and act in a small persistent world | P0 / P-A, P-D | Start or continue, confirm a character, navigate, transact, resolve the one check, gain XP, allocate points, save and resume |
| E2 | Make consequences travel through people | P0 / P-A, P-B, P-C | Gift changes a plan; contact spreads a fallible report |
| E3 | Make resources and effects authoritative | Conditional P1 / P-A, P-D | Spend and recover Stamina; apply, stack, inspect, remove, and persist bounded effects |
| E4 | Make places physically accessible | Conditional P2 / P-A, P-B | Use permission, keys, locks, force, and evidence to access local resources |
| E5 | Live with hunger and fatigue | Conditional P3 / P-A, P-B | Eat, cook, sleep, accept deprivation, and experience causal conditions |
| E6 | Let needs become plans | Conditional P4 / P-B, P-C | Watch Ivo work, buy, prepare, eat, sleep, and replan using finite resources |
| E7 | Secure Brackenford's future through play | Conditional P5 / P-A, P-B, P-C | Sustain four households through community action and personal alchemy |
| E8 | Earn a distinctive affinity spell | Conditional P6 / P-D, P-A | Choose, awaken, earn distinct rewards, and select an upgrade |
| E9 | Daily quest system and gacha rewards | Conditional P7 / P-A, P-D | Complete System-assigned daily objectives for XP and item draws |
| E10 | Hidden bonus objectives | Conditional P8 / P-A, P-D | Trigger surprise bonuses by completing quests unusually or creatively |
| E11 | Resolve a bounded combat encounter | Conditional P9 / P-A, P-D | Fight, flee, or surrender while pools, effects, costs, and death remain authoritative |

Sequence E1 → E2 → P0 gate → E3/P1 gate → E4/P2 gate → E5/P3 gate → E6/P4 gate → E7/P5 gate → E8/P6 gate → E9/P7 gate → E10/P8 gate → E11/P9 gate. Every stage consumes the proven rules below it; none becomes a P0 prerequisite.

## Success Metrics

### P0 evidence gate

1. Capture a starting state in which the player owns one prepared P0 test-fixture pouch containing exactly 10,000 gold and no other gold. Reload that state independently for the purchase, full-pouch gift, and no-gift branches; never merge their outcomes. Funds, stock, and ownership reconcile within every branch; Mara has a different feasible opportunity set after the gift. Her selected plan and observed behavior have a motive-based explanation, not a required retirement script.
2. Resolve the controlled Presence 14 (+2) + Persuasion 1 check at difficulty 12 and 60% success. Record modifiers, die, total, pre-roll probability, XP, and committed consequence; verify natural 1 failure, natural 20 success, zero XP for every failed check, and zero XP for a successful check that can fail only on 1; narration agrees. Rejected/retried requests produce no duplicate mutation or new roll.
3. Verify Tessa's observation and later contact with Ivo. A non-witness knows nothing before receipt. Demonstrate a distorted or doubted claim changing a later choice without changing the original event.
4. Save/load preserves time in seconds, money, inventory, relationships, commitments, beliefs, plans, confirmed starting attributes, current attributes, XP, levels, bonuses, and allocated/unspent points. Replaying captured proposals and rolls reproduces mechanical outcomes, without requiring identical new LLM prose.
5. Kyle can explain why the recipient changed plans and why the report recipient behaved differently. Record believability separately from mechanical consistency.

**G17 — approved evidence protocol:** run three controlled repetitions per P0 gift/no-gift pair and at least one rumor variant. Require zero unexplained authoritative contradictions or conservation/save failures before P1; correct and repeat the affected scenario on failure. At each later stage, exercise its controlled fixture, one failure/recovery path, save/load, and one unplanned but supported approach. Ask what changed, why people acted, what felt unfair, and what the player wants next. Two voluntary return sessions by Kyle, plus friend feedback if available, inform expansion without acting as an automatic release gate.

### P0 timing, input, and growth evidence

On the same routes, distance/speed determines travel time and changing movement mode changes it; no flat adjacent-room cost remains. Compare a 2-word and 31-word exchange, the P0 test-fixture pouch's 5-second handover and a separate count of 100 loose coins, a one-minute silent wait and a clock-target overnight wait. The 100 loose coins exist only in an isolated handling-time fixture; they are not added to the player's P0 wealth and never enter the purchase or gift branches. Interrupt an event wait when an NPC actually orders or the silent-attention interval expires; loading/retrying never duplicates elapsed time. Verify no proactive action suggestions appear. Use fixed near-threshold saves to test XP award once, skill-bonus growth, allocatable attribute points, and old tasks becoming easy. A high-bonus fixture must exceed the old proposed attribute/skill caps without clamping; the 95% check yields zero XP. These are variations on existing actions, not additional P0 content.

### P1–P4 foundation evidence

**P1 — effects and resources:** verify all three resource formulas across the standard array and later attribute growth. Spent points remain absolute deficits when maxima rise; effective-max reductions clamp current values without firing damage triggers. Exercise every effect tier and duplicate policy, opposing percentage modifiers, Sharpened charges, separate Bleeding wounds, matching-cause removal, 0-Stamina restrictions, recovery, rejection of unaffordable actions, inspection, expiry, and save/load. Starved and Exhausted use their explicit multiplicative exception.

**P2 — places and access:** at Ivo's Home, exercise permitted entry, shared-bed capacity, locked and broken door states, matching keys, failed lockpicking with pick consumption, retry with another pick, forced entry and its noise/Stamina cost, and use of local resources. Steal the fungible serving and distinctive object in witnessed and unwitnessed variants. Verify that ownership truth persists, knowledge arises only from observation or communication, fungible identity is not magically traceable after mixing, and suspicion can be reasonable yet wrong.

**P3 — needs and shelter:** cross each hunger and sleep threshold; stack and remove Starved/Exhausted one instance at a time; verify current-pool clamps, recovery, 0 Stamina, Exposed, and adequate versus interrupted sleep. Craft and consume every food fixture, including raw cabbage. Verify recipe-specific work/cost/yield, batch expiration, fresh output expiry independent of ingredient age, expired food still satisfying hunger, the declared spoilage probability, nearest-achievable Constitution difficulty, success-only XP, and tiered food-poisoning effect.

**P4 — autonomous livelihoods:** from identical saves, let Ivo obtain food through his feasible work/buy/cook/eat plan and force each declared failure branch. Every wage, purchase, ingredient, action duration, Stamina cost, access check, meal, and sleep period must reconcile. Verify hunger changes priority rather than guaranteeing crime; where personality and knowledge support it, prove trespass/theft/force become eligible and still obey access/evidence rules. Off-screen execution must produce the same causal state as observed execution.

### P5–P9 expansion evidence

**P5 — community and alchemy:** complete two plausible lived-stability routes and one unplanned supported route. Every household must earn three consecutive qualifying days from actual meals, safe adequate sleep, and protection; only the failing household's streak resets. Exercise routine and uncertain alchemy, failure consumption, item application, poison contact, recipe-track counts, and finite need-driven demand.

**P6 — spells and recognition:** verify both affinity packages and rarity bands, slot ownership, Mana costs, stable generated presentation, title/achievement separation, and Deepened replacement. Session 0 concept, committed history, and the affinity set may shape names and manifestations but never mechanics.

**P7 — daily quests:** exercise all three categories through refresh and expiry. Verify explicit success conditions, one-time player/skill XP, declared-pool draws, distinct System voice, and no reward for partial completion or duplicate resolution. Record whether the structure clarifies or intrudes on free play.

**P8 — hidden bonuses:** exercise at least three triggered and three non-triggered conditions across System and organic quests. Confirm one private condition and at most one bounded reward per quest, no routine-path over-award, and no disclosure of the trigger.

**P9 — combat:** resolve the authored encounter by victory, escape, robber surrender, and player surrender. Verify initiative, movement, Stamina costs, attacks, Defense, spell Mana, effects, items, immediate death at 0 Health, supported revival timing, one-time rewards/XP, six-second rounds, and mid-combat save/load. Text must make positions, current/effective maxima, legal targets, committed costs, damage, and exits understandable without a tactical map.

Run the accepted G16 endurance duration and measure actual model cost during play. Stop expansion to investigate unexplained outcomes, irrelevant NPC memory, opaque progression, severe latency, or insufficient desire to return. No multiplayer, market, or scalability claim follows from these tests.

## Out of Scope

**P0 excludes:** magic/affinity implementation, titles, achievements, dedicated training activities beyond the existing-check XP/level test, community victory/ward pressure, businesses beyond one ordinary purchase, crafting, construction, combat, additional NPCs/locations, offline progression, and multiplayer. The ward may appear in setting text but creates no P0 subsystem.

**P1–P4 exclude:** broad effect catalogues; nutrition/macronutrients; storage-quality modifiers; ingredient-age inheritance; advanced cooking simulation; procedural recipes; construction; player-run businesses; additional settlements or cast expansion. NPCs may work and transact, but P4 proves only the bounded Ivo/Tessa chain.

**P5–P9 exclude:** full affinity combinations/ranks, generated libraries of items/traps/spells, the complete forest-to-tavern construction chain, additional settlements, broad social networks, formal guards/arrest/courts or universal crime reputation, tactical maps, parties, equipment progression, and co-op. Alchemy has no laboratory construction, ingredient harvesting, recipe research, automated batches, or player-run shop. Daily quests have no expiry penalty, streak, multiplier, player preferences, or combat category through P9. Formal policing remains an unscheduled later possibility; only direct evidence, belief, relationship, access, and resource consequences operate in P0–P9.

**Explicitly removed or deferred by accepted decisions:** no class system or class roadmap; no code validation of affinity–concept thematic compatibility; place/domain/innkeeper powers deferred with no commitment to revisit. The preserved *Rise of the Living Forge* inspiration concerns an innkeeper-like domain recognizing protected visitors, influencing thought, healing through lodging, and granting operation-dependent buffs or debuffs; it is reference context only, not a scheduled feature. Broader configurable/generated affinities, abilities, spells, items, traps, titles, achievements, and skill-practice-shaped variants remain long-term ambitions rather than current content budgets. Ordinary business simulation remains part of the vision.

Procedurally generated locations are permanently excluded. Later hidden rooms, puzzles, traps, settlements, and the anonymous-gift test use deliberately authored places.

No public persistent multiplayer. A public v1.0 scope and post-launch roadmap are not established; neither should be inferred from the conditional later vision. Small co-op would first need explicit shared-time, concurrent-action, and conversation design after solo success. Alternate difficulty modes, including any mode that changes save recovery or character-death persistence, remain unselected and require a later explicit design; the current rules describe only the default mode.

## Decisions, Assumptions, and Dependencies

### G register

G IDs remain stable across corrections. Version 0.7 adds the approved P0 fixture-funding and isolated-branch rule while retaining the survival, effects, access, ownership, food, and autonomous-livelihood decisions and their separate proof stages. Stage gates still control implementation order and provide opportunities to revise measured values.

| ID | Status | Current choice / remaining tuning |
| --- | --- | --- |
| G01 | Approved P5 design | Four one-resident households; three consecutive lived-stability days from actual meals, safe adequate sleep, and protection; only the failing household resets |
| G02 | Approved P5 design | Seven-day ward and warnings; expiry removes protection and can cause Exposed but never deletes food or deals automatic damage |
| G03 | Approved P0 baseline | Natural 1/20; Body, Agility, Constitution, Mind, Presence; standard array 8/10/12/13/14; standard modifier; uncapped attributes/skills; player/skill levels; fixed Presence + Persuasion fixture; mastery-preserving contextual difficulty |
| G04 | Approved P0 baseline | Seconds and contextual movement/speech/handling/event waits; fixture speeds/distances; 15-second dialogue rounding; 5-second pouch transfer; day-1 08:00 start; 06:00 morning; 60-second silence interval |
| G05 | Accepted with fixture correction | One prepared P0 test-fixture pouch containing exactly 10,000 gold as the only starting funding; purchase and gift/no-gift tests reload isolated copies of the captured state; simple witnessed gift scenario; anonymous gift as later test |
| G06 | Accepted with correction | Free text; no visible action suggestions; factual navigation/information controls retained |
| G07 | Accepted with addition | Text lengths and small hub; never procedural locations; later hidden rooms/puzzles/traps |
| G08 | Accepted | Three saves, complete restoration, reload for branching tests; no cross-save progression carryover |
| G09 | Approved P6 design | Two named affinity packages, two spell slots per affinity, skill bonuses, and starting spells |
| G10 | Approved P5/P7 design | Exact concern/commitment states, recorded success contract, evaluator, and reward authority |
| G11 | Approved P6 design | Four Rest-stone candidates, uniform package selection, 80/20 rarity, explicit spell parameters, permanence |
| G12 | Approved P6 design | Three distinct uses + fixed achievement trigger/generated presentation; Copper Sandglass; Brackenford's Anchor; four Deepened tradeoffs |
| G13 | Approved P6 design | One exact hint and reveal point for the Deepened spell choice |
| G14 | Superseded by G19 | Drink-stall economy replaced; 30-gold start carried forward into G19 alchemy economy |
| G15 | Approved presentation target | Browser-owned preferred text size; no in-game text-size control; 200% zoom and 320 CSS px reflow; visible focus; non-color speaker labels; no timed reading |
| G16 | Approved evaluation targets | 60 wall-clock minutes, about 100 actions, four NPCs, explicit latency/recovery/memory observations |
| G17 | Approved evidence protocol | Controlled repetitions, contradiction/conservation gates, failure/save/unplanned coverage at each stage, voluntary return-session signal |
| G18 | Approved P0 baseline | Failures award zero XP; successful meaningful checks award `floor(100 * (0.95 - p) / 0.90)` to player and relevant-skill tracks; 100×level thresholds; one attribute point and one skill bonus per applicable level; no caps |
| G19 | Approved P5 design | Starting tools/base recipes; difficulty-12 substitution fixture; twelve recipes; 10/25 thresholds; prices, stock, work, value, and bounded demand |
| G20 | Approved P7 design | Three 06:00 daily slots, exact category templates and XP, 70/25/5 nine-item gacha pool, no failure penalty |
| G21 | Approved P8 design | One private condition per quest; exact storage/evaluation contract; one bounded XP/draw/item reward; fixed notification |
| G22 | Approved P1/P9 design | Health, Mana, and Stamina formulas; current/max growth and clamps; death at 0 Health; revival only through a supported timed effect |
| G23 | Approved P9 design | One-on-one combat proof with initiative, rounds, Stamina, movement, attacks, damage, spell, effects, opponent, exits, rewards, and persistence |
| G24 | Approved P1 design | Configurable effects; source-bounded targets/shapes/duration; Subtle/Standard/Major magnitude budgets; Stack/Refresh/Replace; timestamp order, arithmetic, cause-matched removal, and UI knowledge rules |
| G25 | Approved P2 design | Local access, doors, locks, keys, permission, bed capacity, lockpick consumption/retry, force/noise, theft, evidence, and separate truth/knowledge |
| G26 | Approved P3 design | Hunger and sleep thresholds; Starved/Exhausted stacks; Exposed; adequate sleep; food recipes, batch expiry, spoilage checks, and sickness tiers |
| G27 | Approved P4 design | Wants-driven plans, finite jobs and budgets, physical/off-screen execution, failure replanning, risky options, and the Ivo/Tessa proof |

### Correction priorities and dependencies

The P0 source-of-truth pass is complete. Title/New Game/Continue, Rowan-led Session 0, player-authored character naming, five-attribute standard-array assignment, the controlled check, contextual-difficulty policy, action timings, campaign epoch/start second, and the success-only XP curve are approved. P0 still has one check situation, three locations, four NPCs, and one social conflict; Session 0 adds no fictional time or world-content breadth, and the growth test reuses the existing check and controlled saves.

P1–P9 design assumptions are resolved enough for staged implementation planning. Each stage remains conditional on evidence from the one before it. Measurements may motivate later corrections but are not blanks for implementers to fill. Budget, weekly availability, delivery dates, model/provider, implementation stack, public-release intent, alternate difficulty modes, broad skill mappings, dedicated training, affinity respec, mature rarity distributions, and long-term discovery libraries remain separate later decisions.

Version 0.7 is the staged design baseline. It explicitly supersedes any implication that P0 begins with loose or ordinary campaign gold, that the purchase must precede the full-pouch gift in one continuous branch, or that P0 fixture outcomes fund later stages. It also retains the 0.6 corrections superseding automatic food loss, passive NPC sustenance, and the former Downed/stabilization model. Narrative detail and downstream architecture, UX, and implementation planning remain separate workflows; their current contradictions do not override this GDD.
