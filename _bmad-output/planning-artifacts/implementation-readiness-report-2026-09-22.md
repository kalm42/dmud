---
stepsCompleted:
  - step-01-document-discovery
  - step-02-gdd-analysis
  - step-03-epic-coverage-validation
  - step-04-ux-alignment
  - step-05-epic-quality-review
  - step-06-final-assessment
readinessStatus: NEEDS_WORK
filesIncluded:
  gdd:
    - _bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/gdd.md
  architecture:
    - _bmad-output/game-architecture.md
  epics:
    - _bmad-output/planning-artifacts/epics.md
  ux:
    - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/DESIGN.md
    - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md
---

# Implementation Readiness Assessment Report

**Date:** 2026-09-22
**Project:** dmud

## Document Inventory

### GDD

- Selected: `gdds/gdd-dmud-2026-09-07/gdd.md` (100,033 bytes; modified 2026-09-15 14:52:06 MST)
- Related but not selected as the governing epics artifact: `gdds/gdd-dmud-2026-09-07/epics.md`
- The GDD folder has no `index.md`; `gdd.md` is treated as the whole GDD.

### Architecture

- Selected after its citation was discovered in the governing epics: `_bmad-output/game-architecture.md` (129,740 bytes; modified 2026-09-15 16:03:02 MST).
- The architecture is stored at the `_bmad-output/` root rather than under the configured `planning-artifacts` directory, so the prescribed discovery glob did not initially find it.

### Epics and Stories

- Selected: `epics.md` (489,223 bytes; modified 2026-09-22 21:09:17 MST)
- Duplicate candidate excluded: `gdds/gdd-dmud-2026-09-07/epics.md` (17,493 bytes; modified 2026-09-15 14:52:06 MST)

### UX Design

- Selected: `ux-designs/ux-dmud-2026-09-08/DESIGN.md`
- Selected: `ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md`
- Supporting files in the UX folder include the decision log, reconciliation notes, review reports, and validation report.
- The UX folder has no `index.md`; `DESIGN.md` and `EXPERIENCE.md` are treated as the governing UX document set.

### Discovery Issues

- Warning: the architecture document is outside the configured planning-artifact directory, creating a discoverability and inventory consistency problem.
- The root `epics.md` was confirmed as the governing epics/story artifact; the older GDD-folder copy is excluded.

## GDD Analysis

### Functional Requirements

FR1: The title flow shall present **New Game** and **Continue**. Continue shall open a three-slot manual-save selector when saves exist; when none exist it shall remain visible but unavailable with an explanation. A save-index failure shall offer retry without blocking New Game.

FR2: New Game shall begin a zero-fictional-time Session 0 led by Rowan. Rowan shall ask for the character's name, origin, cares, hates, especially cool ideas, and campaign hopes; offer suggestions only when explicitly asked; distinguish player-authored facts, agreed premises, preferences, and non-binding hopes; permit correction of the review and fixed-array assignment until explicit confirmation; and then atomically establish the character and initial world state at Market Square without predetermining an NPC decision, route, check result, or campaign outcome.

FR3: Player input shall express an intention rather than directly edit authoritative state. The rules shall classify an intention as routine and feasible, uncertain, impossible, or unsupported; reject impossible/unsupported state changes factually; preserve state on rejected proposals; and offer alternatives only when the player asks for help. Social success shall not compel an NPC to violate binding obligations or become obedient.

FR4: Before committing a consequential action, the game shall expose reasonably knowable interpretation, stakes, and cost; clarify materially changed intent or rare-resource use; fix difficulty before a roll; define mechanical success and failure where practical; validate contextual consequences before commitment; preserve hidden facts; and make action cost, state change, narration, and outcome agree atomically. Replayed or duplicate requests shall not repeat purchases, costs, rolls, rewards, or other mutations.

FR5 (G03): Eligible uncertain checks shall use a fair d20: natural 1 automatically fails, natural 20 automatically succeeds, and all other results succeed when `d20 + attribute modifier + relevant basic-skill bonus >= difficulty`. The five attributes shall be Body, Agility, Constitution, Mind, and Presence; Session 0 shall assign 8, 10, 12, 13, and 14 exactly once; modifiers shall equal `floor((score - 10) / 2)`; confirmed starting assignments shall remain immutable; earned points may increase current scores; attributes and skill bonuses shall have no cap; and contextual difficulty shall not rise merely to cancel earned mastery.

FR6 (G04): A shared clock measured in seconds shall advance for travel, completed speech, item handling, work, crafting, and waits, but not for typing, reading, model latency, menus, known-information inspection, or saving. Movement shall use `ceil(distance / applicable speed)` per completed segment; ordinary-ground fixture speeds shall be walk 1.4, jog 2.8, sprint 5.6, and crawl 0.5 metres/second; the Market Square–Mara's Stall and Market Square–Common Room routes shall be 7 m and 140 m. Dialogue time shall equal `15 * ceil(rendered spoken words / 30)` seconds per completed exchange, excluding prose and reasoning. The campaign shall begin at day 1 08:00 (second 28,800), with 06:00 as morning.

FR7 (G04/G05): Item-transfer time shall reflect actual handling. The prepared 10,000-gold P0 pouch shall transfer in five seconds as a counted container, while counting 100 loose coins shall take at least 100 seconds. Interrupted transfers may consume completed time but shall not transfer funds/items before handover completes. The ordinary-purchase, gift, no-gift, and loose-coin fixtures shall use isolated reloads and shall never merge balances or outcomes.

FR8 (G04): Waiting shall accept an explicit duration, clock target, or event condition. Event waits shall advance through actual simulated decisions rather than manufacture the requested event; face-to-face silence shall return control after 60 seconds; uneventful overnight waits shall not interrupt every minute; and an impossible or unscheduled target shall be reported instead of waiting forever.

FR9 (G05): P0 shall implement Mara, Oren, Tessa, and Ivo across Market Square, Mara's Stall, and the Common Room. Mara shall owe Oren 20 gold while wanting both repayment and a visit to her ill sister; Tessa shall be able to witness the gift; Ivo shall later meet Tessa in the Common Room 1,800 seconds after the gift opportunity in both gift and no-gift branches; and a controlled rumor variant shall allow Tessa's influence claim plus Ivo's distrust to cause confirmation-seeking without rewriting the original event.

FR10: NPC decisions shall be constrained by each NPC's needs, desires, obligations, relationships, resources, current plan, personality, and limited knowledge. Consequential replanning and dialogue may use the LLM only within recorded constraints. Observation, received claims, belief source, time, uncertainty, distortion, contact, motive, and resulting action shall be distinct and inspectable; non-witnesses shall not learn events automatically; beliefs shall not rewrite authoritative history; and NPCs may lie or conceal motives only consistently with their knowledge.

FR11 (G06): The primary command interface shall accept free-text intentions and shall show no suggested actions, recommended choices, dialogue replies, or action chips. It shall retain factual linked exits, inventory, journal, save/load, and optional roll-detail controls; support Enter to submit and Shift+Enter for a newline; keep all controls keyboard reachable; neutrally disambiguate ambiguous names; explain unsupported verbs without consuming time; preserve player intent during clarification; expose pending/resolved/failed processing state; and provide a recoverable failure path.

FR12 (G07): P0 shall have exactly three authored, stable locations with readable exits and examinable context. Initial location descriptions shall be 60–120 words, repeat descriptions 20–60 words emphasizing actual changes, and typical action results 40–120 words. P2–P5 may add only the authored household, access, food, work, and protection locations required by their stage fixtures. Locations shall never be procedurally generated.

FR13 (G08): The game shall provide three manual save slots. Save/load shall restore the complete branch state, including world seconds, ownership, possession, quantities, relationships, commitments, beliefs, observations, NPC plans, access state, effects, current pools, starting and current attributes, player and skill XP/levels/bonuses, and allocated/unspent points. Loading an older save shall restore only that branch; abandoned-branch rewards shall not carry across. Replaying captured state with captured proposals and seeded dice shall reproduce mechanical outcomes even if fresh LLM prose differs.

FR14 (G22): Every character shall have integer current and Base Maximum pools where `Maximum Health = Body × Constitution`, `Maximum Mana = Body × Mind`, and `Maximum Stamina = Agility × Constitution`. New characters and P1-migrated P0 characters shall begin at all maxima. Permanent attribute increases shall add the Base Maximum delta to the current pool so existing damage/spend remains an absolute deficit; decreases shall recalculate and clamp; temporary check modifiers shall not alter Base Maximum unless explicit; percentages, thresholds, restoration, and caps shall use Effective Maximum unless Base Maximum is explicitly named; and current values shall remain between zero and Effective Maximum.

FR15 (G22): Spells shall spend listed Mana only when their effect commits; insufficient Mana shall reject the cast without effect, cost, or fictional time. Eight hours of adequate sleep shall restore all Mana and 25% of Effective Maximum Health, rounded up. Ten uninterrupted minutes of non-strenuous rest shall restore 25% of Effective Maximum Stamina, rounded up. Eating and time passage alone shall restore none of these pools unless a consumable explicitly declares restoration.

FR16 (G22): Stamina costs shall use Routine 0, Exerting 5, Strenuous 10, and Extreme 20 bands. Full cost shall be affordable before an action starts; rejected actions shall spend no partial Stamina or time. At zero Stamina, a character shall be unable to move or take Stamina-costing actions but may talk, inspect, eat, use suitable items, or attempt sleep. Damage shall reduce Health separately from wound effects; zero Health shall cause immediate death; revival shall require a supported effect within its declared window; player defeat shall offer manual-save recovery without forced save deletion; and NPC death shall persist unless reversed by a supported effect.

FR17 (G24): Conditions, buffs, debuffs, and item treatments shall share one configurable effect language. Every definition shall record source, source category, polarity, tier, magnitude, duration or terminating condition, removal rule, duplicate behavior, player knowledge, stable identity, and eligible target. Supported targets shall include Health, Mana, Stamina, effective maxima, checks, Defense, movement, damage, healing, and spell/action cost. Unsupported or over-budget definitions shall be rejected or reduced before commitment, and generated effects without an explicit duration/use/termination bound shall be rejected.

FR18 (G24): Named effects may coexist, while each definition shall choose Stack, Refresh, or Replace behavior. Generated effects shall use one primary mechanical shape unless an authored effect separately balances combined components. Ordinary modifiers shall resolve as `round(Base × (1 + sum percentage modifiers)) + sum flat modifiers`; percentages shall add rather than compound; opposing modifiers shall remain independently active even when numerically canceling; Health, Mana, Stamina, damage, and healing shall not fall below zero; and costs shall not fall below one unless an authored exception explicitly permits zero.

FR19 (G24): Effect validation shall enforce source-bounded tiers: Subtle permits ±1 flat, ±10%, and total periodic damage 10; Standard permits ±4, ±25%, and 30; Major permits ±20, ±50%, and 100. Difficulty shall determine success rather than magnitude; a natural 20 shall not raise the allowed tier; a natural 1 shall create no effect; repeated mundane actions shall not manufacture Major power; and removal shall require the declared cause, a compatible causal category, or an exact-effect remedy.

FR20 (G24): P1 shall implement and test Sharpened (+1 weapon damage on the next ten successful hits, Refresh), independently stacking Bleeding wounds (2 Health every six seconds for five ticks, one linked instance removed per treatment), simultaneous +25%/−25% modifiers, diagnostic Star-metal Edge (+20 weapon damage to the next successful hit within ten minutes, Replace), and an exact-limit/one-unit-over calibration matrix for every tier/shape combination.

FR21 (G24): Changes sharing a timestamp shall resolve in this order: completed actions and intervals in commitment order; scheduled effect ticks and unmet-need thresholds in stable creation order; effect expirations and environmental transitions; then Base/Effective recalculation, clamping, and terminal states. A meal or adequate sleep completing exactly at a threshold shall prevent the corresponding stack; linked treatment completing exactly on a Bleeding tick shall remove it before that tick; final scheduled ticks shall occur before ordinary expiration; and protection valid through a completed sleep interval shall qualify that interval.

FR22 (G25): Resources shall be usable only where they physically exist and when the actor can reach them. Access may derive from ownership, permission, relationship, compatible key, unlocked entrance, successful lockpicking, or forced entry. Doors shall record open, closed, locked, and broken states; beds shall record capacity; qualifying unauthorized use may satisfy physiological needs while preserving trespass, theft, damage, noise, observation, belief, and relationship consequences.

FR23 (G25): Authoritative ownership shall remain separate from NPC knowledge. Distinctive objects shall retain identity, possessor, claim, provenance, and recognizable marks; fungible goods shall retain quantities and causal transfers but lose instance-level traceability after mixing. Unseen removal shall create no knowledge; later inspection and remembered state may create a missing-item belief; and witness evidence, damage, tampering, opportunity, motive, possession, and statements may support correct or mistaken suspicion without making belief authoritative truth.

FR24 (G25): P2 shall implement Ivo's Home with a difficulty-12 four-state door; matching keys for Ivo and permitted guest Mara; five-second no-roll unlocking/opening; 60-second `Agility + Sleight of Hand` difficulty-12 lockpicking that consumes a pick on failure and permits retry with another; loud 30-second, 10-Stamina `Body + Athletics` difficulty-14 forced entry that leaves the door broken/open on success; a capacity-two bed; one fungible food serving; and one distinctive marked object. Save/load shall preserve all access, possession, event, observation, and belief state.

FR25 (G26): Every character shall track the last completed meal and adequate sleep. Hunger priority shall progress through satisfied (0–8 h), low (8–16 h), competing (16–20 h), urgent (20–24 h), and critical (24+ h). At each 24 consecutive hours without eating, one Starved stack shall apply and set `Effective Maximum Health = round(Base Maximum Health × 0.75^stacks)` with immediate non-damage clamping. One complete serving shall reset the timer and remove one stack without healing; an effective maximum rounded to zero shall cause death.

FR26 (G26): Sleep priority shall progress through rested (0–12 h), low (12–16 h), high (16–20 h), and critical (20–24 h). At each 24 consecutive hours without completing adequate sleep, one Exhausted stack shall apply and set `Effective Maximum Stamina = round(Base Maximum Stamina × 0.75^stacks)` with non-expenditure clamping. Eight adequate hours shall reset the timer, remove one stack, and restore Stamina to the newly available maximum. Starved and Exhausted shall be multiplicative authored exceptions to ordinary percentage stacking.

FR27 (G26): Adequate sleep shall require one continuous eight-hour interval using a usable bed with valid protection for the entire interval. Leaving, disruption, bed loss, or protection lapse shall make the sleep inadequate. Inadequate sleep shall still earn ordinary ten-minute Stamina-rest recovery but shall not reset sleep time or remove Exhausted. Hunger and timed effects shall continue during sleep. Exposed shall describe an unprotected sleeping place, block safe sleep and G01 qualification, deal no direct damage, and remove no food; a missing bed shall independently block adequate sleep without making a protected household Exposed.

FR28 (G26): One complete food serving shall reset hunger regardless of taste or expiration. Food definitions shall declare raw-edibility, inputs, facilities/tools, work time, Stamina, yield, shelf life, price, taste/preferences, and optional effects. Batches shall use one expiration timestamp based on craft completion rather than ingredient age; storage shall not alter expiry; expired food shall remain edible. Expired-food risk shall equal `min(100%, 5% + 95% × time overdue / declared shelf life)`, rounded to the nearest percent; the Constitution difficulty shall approximate that failure risk within natural-1/20 bounds; and failure shall apply a physiological food-poisoning effect of Subtle through 25% overdue, Standard above 25% through 75%, or Major above 75%.

FR29 (G26): P3 shall implement raw cabbage (one serving, ten-minute eating, seven-day life), cabbage stew (cabbage/water/hearth/pot, 30 minutes, 5 Stamina, two servings, two days), pound cake (flour/sugar/butter/oven, 60 minutes, 10 Stamina, four servings, five days), sauerkraut (cabbage/salt/crock, 15 minutes and 5 Stamina plus 72 unattended hours, four servings, 30 days), cooked meat (raw meat/hearth/pan, 20 minutes, 5 Stamina, two servings, two days), and cured meat (raw meat/salt/rack, 30 minutes and 5 Stamina plus 48 unattended hours, two servings, 14 days). Missing inputs/facilities shall reject before cost; known exact recipes shall be routine; substitution/novel methods shall use G03; and unattended processing shall persist through save/load.

FR30: The status view shall show current and Effective Maximum Health, Mana, and Stamina; known effects with stack count, mechanics, source, and removal; time since meal and adequate sleep; and exact time to the next Starved/Exhausted stack. It shall state facts without recommending actions. Unknown effects shall expose symptoms until identified, and exact durations shall appear only when known or revealed by an ability.

FR31 (G27): Player and NPC characters shall use the same needs, pools, effects, death, access, cost, and time rules. NPC wants shall be shaped by need pressure, personality, obligations, knowledge, relationships, resources, risk, and time. NPCs shall choose among feasible known plans, physically execute every step on the shared clock, spend actual inventories/gold/Stamina/work time, and replan after failure rather than receiving invented resources. Off-screen execution shall match observed causal state and shall advance only with game time; persistent off-screen death shall require a complete causal chain; the player shall be interrupted only by reasonably perceivable events.

FR32 (G27): Hunger and sleep planning may use owned food, preparation, purchase, restaurants/lodging, hospitality, borrowing, trade, sale, help, work, shelter repair, shared beds, protection, or relocation when known and feasible. Urgent deprivation may broaden socially costly alternatives, but trespass, theft, lockpicking, or force shall become eligible only when personality, knowledge, relationships, remaining alternatives, and risk support them; physiological need shall not automatically make an NPC criminal or erase consequences.

FR33 (G27): Jobs shall be learned, simulated plans rather than class restrictions or passive income. Work shall require a known opportunity, place, time, and tools/inputs; wages, goods, services, expenses, and ownership shall change only through completed actions; employers/customers shall have finite budgets and demand; missed work, failed production, unavailable inputs, closure, or absent demand may prevent payment; and characters may replan into other work, contracts, trade, borrowing, help, or supported illicit alternatives.

FR34 (G27): P4 shall start Ivo with zero discretionary gold, 12 hours since food, and 12 hours since adequate sleep; Tessa's business with 12 gold and six one-gold cabbages; and a four-hour courier shift that transfers three gold from Tessa to Ivo only on completion. Ivo may buy a cabbage, prefers stew when his protected home's hearth/pot remain usable, may eat it raw, and after eating shall pursue adequate sleep. Unavailable work, insufficient employer funds, sold-out stock, unusable hearth, or lost protection shall trigger replanning without inventing funds or a fifth NPC.

FR35 (G01/G02): P5 shall model four one-resident households—Mara, Oren, Tessa, and Ivo—each with a concrete home, local resources, a bed, and protection state. Each household shall independently earn three consecutive lived-stability days by recording a meal before the next Starved threshold, adequate sleep in a protected bed, and absence of Exposed; only the failing household's streak shall reset. Funding/supply shall come from existing resources, completed transfers/production, or guaranteed contracts. Supported protection routes shall include a 12-gold/two-four-hour-action ward repair lasting 30 days, an 18-gold plus one gold for each of three days patrol contract, five-gold accepted relocation per household, and causally equivalent supported plans.

FR36 (G02): P5 shall begin with seven days of ward protection, expose remaining duration on inspection, and interrupt long waits with three-day and one-day warnings. Ward expiry shall remove protection and may make households Exposed but shall not delete food, damage characters, or create irreversible lockout. Food shall leave inventory only through recorded eating, transfer, theft, spoilage use, or destruction. Later offers, relationships, survival pressure, and events may change each resident's starting preference.

FR37 (G19): Crafting shall accept a stated item intent, ingredients, workspace, recipe/approach, and relevant Alchemy or Brewing capability; validate feasibility/tools before commitment; resolve mastered known recipes routinely and uncertain substitutions/novel methods through G03; atomically commit ingredients, time, output, and XP; consume ingredients without output on failed attempts; persist created items and item coatings through save/load; and support restorative potions, Mana potions, weapon/food poisons, and brewed drinks with their declared delivery semantics.

FR38 (G19): P5 shall begin with Alchemy 0, Brewing 0, a Field Alchemy Kit, a Brewer's Crock, and knowledge of Healing Draft, Mana Draft, Weak Toxin, and Common Ale. The bruised-duskroot Healing Draft substitution shall use `Mind modifier + Alchemy` at difficulty 12. Four independent production-count tracks shall unlock optional T1 recipes at ten successful crafts and T2 recipes at 25 total successful crafts; failed or replayed attempts shall not count; accepted/declined unlock offers and counters shall persist; and a declined offer shall recur after the next qualifying craft.

FR39 (G19): The 12 alchemy/brewing recipes shall retain the GDD's exact inputs, work durations, restoration/damage/modifier values, durations, delivery limits, gold values, wound/removal behavior, 120-second revival window, and once-per-death constraint. P5 shall use an independent 30-gold start; discard all P0 fixture wealth/outcomes; sell basic ingredients for one gold and rare catalysts for four; cap supplier stock at 20 basic and four rare; restock up to rather than above those caps at 06:00; and make NPC demand finite, need-driven, and payable only from owned funds.

FR40 (G09): P6 shall offer exactly two starting affinity packages. Ember + Fellowship shall grant +1 Survival and Hearthspark (8 Mana, 10 m, ten minutes, manipulate one hand-sized nonmagical flame or warm one held object, no direct P6 combat damage). Vessel + Fellowship shall grant +1 Medicine and Steady Vessel (8 Mana, self, 120 seconds, suppress one Minor Wound action penalty without removing the wound or restoring Health). Each affinity shall own two slots; bonuses shall not self-stack; and spells shall always declare owner, slot, Mana, range, duration, targets, and effect.

FR41 (G11): P6 shall provide one Rest-concept stone whose retained rarity is Standard 80% or Resonant 20%. Before use, the game shall show uniform selection between the two package-supported candidates; require a free slot for either possible result; leave the stone unconsumed if capacity is invalid; and otherwise consume it and permanently award the rules-selected fixed effect. The LLM may generate only the player-facing name and one-sentence manifestation from concept, owning affinity, affinity set, Session 0 concept, and committed history; presentation shall not alter mechanics.

FR42 (G12/G13): After three distinct consequential uses of the awarded Rest spell plus the internally recorded Rest Is Part of the Work achievement—earned when the spell materially enables recovery during a timed accepted commitment—the game shall offer the exact authored Deepened replacement and tradeoff in the same slot after explicit confirmation. The first qualifying use shall reveal `Rest deepens when recovery protects a promise.` without a checklist. The achievement shall generate only a 2–6-word name and one event-grounded sentence, award a five-gold Copper Sandglass that reveals one known effect/commitment's exact remaining time once per day, and persist independently of the item. G01 completion shall award the nonstacking Brackenford's Anchor title for +1 to one Persuasion check per simulated day.

FR43 (G10): The journal shall track known concerns and commitments as proposed, accepted, fulfilled, failed, expired, or abandoned, recording renegotiation as a changed agreement. Acceptance shall record required outcome, parties, deadline if any, evaluating authority, and exact reward or lack of reward. NPC rewards shall require actual fulfillment and owned/promised resources. All accepted organic and System quests shall expose exact success conditions; hidden NPC facts may remain hidden, but an unstated success condition shall remain an open concern rather than a quest.

FR44 (G20): At each 06:00 refresh, the System shall replace all three daily slots with one crafting quest for a named known recipe, one social quest for an accepted NPC commitment, and one observation quest for a named location and specified previously unknown condition. Each quest shall visibly state success conditions, expire at the next refresh without penalty, award 25 player XP plus 25 relevant-skill XP and one gacha draw exactly once on full completion, and award nothing for partial completion or duplicate resolution. The System voice shall remain distinct from narrator, NPC, and award voices.

FR45 (G20): A gacha draw shall first select Common 70%, Uncommon 25%, or Rare 5%, then uniformly select within the visible tier pool. The pool shall contain exactly the nine authored item entries and their GDD-defined quantities, effects, and values, including Perfect Catalyst's one-recipe substitution and System Token's one future reroll whose second result must be accepted. Combat quests shall remain excluded through P9.

FR46 (G21): Each P8 daily or organic quest shall receive exactly one stable private hidden condition recording unusual approach, qualifying evidence, evaluation point, and reward. The condition shall never be disclosed before or after resolution. At creation, seeded rules shall uniformly select XP, extra draw, or Common item; XP shall be a seeded 10–25 for both applicable tracks, the draw shall use G20, and the item shall be uniformly selected from Common items worth at most five gold. At the evaluation point the LLM may judge only committed evidence; rules shall reject or pay the fixed reward at most once; and success shall display exactly `HIDDEN CONDITION SATISFIED — Bonus acquired.` followed by the reward without explaining the condition.

FR47 (G23): P9 shall implement one authored one-on-one encounter starting at ten metres. Initiative shall be `d20 + Agility modifier`, with ties broken by higher Agility then the player. Each six-second turn shall permit movement up to eight metres plus one action: attack, cast, item, defend, sprint, escape attempt, or surrender offer. Sprint shall use the action to move up to 34 m. Moving, attacking, and defending shall each cost five Stamina; sprint and escape shall cost ten; unaffordable actions shall reject without partial commitment.

FR48 (G23): Combat attacks shall use G03 against `Defense = 10 + Agility modifier + armor bonus`; melee shall use Body modifier + Melee, ranged Agility modifier + Ranged, and targeted spells Mind modifier + Arcana; Defend shall grant +2 Defense until the next turn; armor shall affect Defense only; and minimum-one damage shall be unarmed `4 + Body modifier`, sword `8 + Body modifier`, or bow `8 + Agility modifier`. Combat cost, damage, pools, positions, order, effects, and item changes shall commit atomically and persist through save/load.

FR49 (G23): The separate P9 player fixture and road-robber fixture shall use exactly the GDD-authored attributes, pools, skills, inventory, Hearthspark/Cinder Lance spell parameters, Defense, damage, and resources. The robber shall offer surrender at or below 25% Effective Maximum Health and normally accept player surrender; escape shall require more than 20 m separation plus a flee action; defeat/robber surrender shall award the one-time five-gold purse; escape shall award none; player surrender shall transfer up to five owned gold; combat checks may award G18 XP once; no encounter-completion XP shall exist; and reload/replay shall not duplicate XP or purse transfer.

FR50 (G18): Successful meaningful checks shall award `floor(100 * (0.95 - p) / 0.90)` XP to both player and relevant-skill tracks, where `p` is the pre-roll probability from all bonuses and natural-roll overrides; failed checks, routine no-roll actions, rejected actions, duplicate resolutions, unchanged retries, and 95%-success checks shall award zero. Player and skill tracks shall start at level 1/0 XP; the next level shall cost `100 * current level`, consume the threshold, carry excess, and repeat across multiple levels; each player level shall grant one allocatable +1 attribute point and each skill level +1 skill bonus; and all XP, levels, bonuses, and unspent points shall persist.

FR51: Authoritative inventory shall track ownership, possession, quantity, physical location, transferability, and distinctive/fungible identity. Scenery may be examined without being takeable. P0 shall contain only the prepared fixture pouch and Mara's five one-gold drinks as required inventory; later stages shall add only their explicitly budgeted keys, lockpicks, household goods, food, effects, alchemy, affinity, reward, and combat items. Selling or losing an award item shall not erase its earned achievement.

FR52: The simulation shall advance only through committed game actions and shall pause when the application is closed. Distant agents shall retain plans and causal consequences without constant narration. Unsupported proposals shall become expansion candidates rather than invented successes. Victory shall not reset the world, and successful communities shall remain playable with continuing consequences of agreements, trade, and departures.

Total FRs: 52

### Non-Functional Requirements

NFR1: The initial product shall run locally in a desktop browser as a solo personal prototype and shall support durable saves plus an LLM connection selected later; the GDD intentionally leaves engine, language, model, storage, server deployment, and provider to architecture.

NFR2: New and returning play sessions shall target 20–60 minutes, with Session 0 included only in a new campaign's budget, easy save/resume, and no offline progression.

NFR3 (G15): The interface shall respect browser text-size and zoom settings without loss of content or functionality, support 200% page zoom and reflow at the equivalent of 320 CSS pixels without two-dimensional page scrolling except for intrinsically two-dimensional content, expose visible keyboard focus, label speakers without relying on color, and impose no timed reading requirement.

NFR4: All controls shall be keyboard reachable; Enter and Shift+Enter behavior shall be consistent; factual navigation and information controls shall remain available without steering player choices.

NFR5 (G16): Visible input acknowledgement shall occur within 100 ms; local menus within 200 ms; save/load within two seconds; and at least 95% of completed LLM-mediated actions within ten seconds. A request still interrupted at 30 seconds shall show a recoverable interruption state.

NFR6 (G16): A 60-minute endurance run of approximately 100 representative actions with four active NPCs shall record simulated seconds separately. After the initial scene loads, browser resident memory at run end shall be no more than 100 MB over baseline and shall show no monotonic per-action growth. The text workload has no separate FPS target.

NFR7: The system shall log action latency, model calls/tokens, measured monetary cost, rejected proposals, duplicate-action attempts, and contradiction repairs, while leaving acceptable provider and dollar budget open until measured play.

NFR8: Interrupted processing shall preserve already committed progress, identify pending work clearly, and provide a recoverable retry/resume path without implying success or duplicating state changes.

NFR9: Rules—not LLM prose—shall own validation, dice, authoritative state, conservation, and commitment. Narration shall never assert an uncommitted success, and generated/contextual consequences shall be validated before mutation.

NFR10: Seeded/captured proposals and rolls shall reproduce mechanical results across reloads without requiring identical fresh prose. Stable generated spells, effects, rulings, and identities shall retain recorded versions across sessions; intentional revisions shall be explicit and preserve which version governed earlier outcomes.

NFR11: State integrity shall prevent negative current resources, values above Effective Maximum, overspending, stock creation, duplicate rewards, rerolled resolved actions, cross-branch progression leakage, and uncaused NPC knowledge or resources.

NFR12: P0 evidence shall tolerate zero unexplained authoritative contradictions, conservation failures, or save failures across three controlled gift/no-gift repetitions and at least one rumor variant; any such failure shall be corrected and the affected scenario repeated before promotion.

NFR13: Every later stage shall exercise its controlled fixture, one failure/recovery path, save/load, and one unplanned but supported approach before promotion; expansion shall stop to investigate unexplained outcomes, irrelevant NPC memory, opaque progression, severe latency, or insufficient desire to return.

NFR14: Every meaningful cue shall have a textual representation; P0–P9 shall not require illustration, portraits, sprites, animation, music, audio assets, a tactical map, or generated imagery.

NFR15: Location geography shall be authored and stable rather than procedural. Generated descriptions may reflect committed changes but shall not silently alter mechanics, connections, access, or history.

NFR16: The implementation shall remain within the stage-specific content and asset budgets enumerated by the GDD, avoiding generated catalogues, broad geography, additional cast, or feature breadth not authorized by the active stage.

Total NFRs: 16

### Additional Requirements

- **Mandatory stage gating:** Implement and validate P0 first, then P1 through P9 in order. Each stage consumes the proven rules below it and remains conditional on the preceding evidence gate; design approval for a later stage does not authorize early implementation.
- **P0 evidence scope:** Use the exact isolated purchase, gift, no-gift, rumor, timing, dialogue-length, coin-handling, wait, uncertainty, save/load, progression, and high-bonus fixtures. Record mechanical consistency separately from subjective believability.
- **Later-stage evidence:** Exercise every authored formula, boundary, duplicate policy, access state, need threshold, food fixture, livelihood failure branch, community route, affinity package/rarity, quest category, hidden-condition outcome, and combat resolution listed in the GDD.
- **Explicit exclusions:** No classes, procedural locations, public persistent multiplayer, co-op through P9, offline progress, tactical map, formal guards/courts/universal crime reputation, construction, broad generated catalogues, player-run alchemy shop, full spell/item libraries, or automatic roadmap beyond P9.
- **Open architecture/product decisions:** Implementation stack, storage, provider/model, server deployment, acceptable dollar budget, weekly availability, delivery dates, public-release intent, alternate difficulty modes, and possible later co-op remain unresolved and must not be invented by implementation.
- **Authority and change control:** The current GDD and its latest decision log override older brief/addendum implications. Measurements may motivate explicit later correction, but implementers shall not silently fill open decisions or reinterpret superseded rules.

### GDD Completeness Assessment

The GDD is unusually complete at the behavioral and evidence-fixture level: it defines the staged scope, authoritative mechanics, exact numeric fixtures, failure semantics, persistence expectations, content budgets, exclusions, and promotion evidence for P0–P9. Its strongest implementation assets are the stable G-register, explicit correction history, and tightly bounded stage gates.

The GDD is complete enough to delegate engine, language, model/provider, storage, event/state representation, deployment, and authoritative-state implementation to downstream architecture. Architecture 1.2 was subsequently found at `_bmad-output/game-architecture.md`, outside the configured planning-artifact search location, and supplies those decisions. The remaining traceability risk is that GDD requirements are embedded across prose and the G-register rather than maintained as a native FR/NFR catalogue; the normalized list above is therefore required for epic coverage and should become a controlled traceability baseline.

## Epic Coverage Validation

### Epic FR Coverage Extracted

The governing epics document contains its own 84-item functional-requirements inventory and an explicit coverage map:

- Native FR1–FR21, FR27–FR35, and FR82–FR84: Epic 1
- Native FR22–FR26: Epic 2
- Native FR36–FR42: Epic 3
- Native FR43–FR47: Epic 4
- Native FR48–FR53: Epic 5
- Native FR54–FR57: Epic 6
- Native FR58–FR65: Epic 7
- Native FR66–FR70: Epic 8
- Native FR71–FR74: Epic 9
- Native FR75–FR77: Epic 10
- Native FR78–FR81: Epic 11

The epics document decomposes several compound GDD requirements into smaller native FRs. The matrix below maps the 52 normalized GDD FRs from this assessment to the actual stories that supply an implementation path.

### Coverage Matrix

| FR | GDD requirement | Epic/story coverage | Status |
| --- | --- | --- | --- |
| FR1 | Title and save entry | E1 S1.2 | ✓ Covered |
| FR2 | Rowan-led Session 0 and atomic confirmation | E1 S1.3–S1.5 | ✓ Covered |
| FR3 | Intention classification and factual rejection | E1 S1.8 | ✓ Covered |
| FR4 | Consequential lifecycle, stakes, atomicity, idempotency | E1 S1.7–S1.10 | ✓ Covered |
| FR5 | d20 checks, attributes, fixed array, uncapped mastery | E1 S1.4, S1.10 | ✓ Covered |
| FR6 | Seconds-based clock, movement, dialogue, epoch | E1 S1.9 | ✓ Covered |
| FR7 | Handling time and isolated fixture branches | E1 S1.9; E2 S2.2 | ✓ Covered |
| FR8 | Duration/clock/event waits and interruption | E1 S1.9 | ✓ Covered |
| FR9 | Four-NPC P0 social fixture | E2 S2.1–S2.3 | ✓ Covered |
| FR10 | NPC state and fallible social information | E2 S2.1, S2.3–S2.4 | ✓ Covered |
| FR11 | Free-text, neutral clarification, controls, lifecycle states | E1 S1.6–S1.8 | ✓ Covered |
| FR12 | Authored locations and description bounds | E1 S1.6, S1.9; E4 S4.1 | ✓ Covered |
| FR13 | Three complete, isolated save branches | E1 S1.12 | ✓ Covered |
| FR14 | Derived pools, growth deltas, Effective Maximum clamps | E3 S3.1–S3.2 | ✓ Covered |
| FR15 | Mana/Stamina recovery and affordability | E3 S3.2 | ✓ Covered |
| FR16 | Stamina bands, zero restriction, wounds/death/revival | E3 S3.2; E11 S11.5 | ✓ Covered |
| FR17 | Shared effect definition/instance contract | E3 S3.3 | ✓ Covered |
| FR18 | Duplicate policies and modifier arithmetic | E3 S3.4 | ✓ Covered |
| FR19 | Tier budgets, duration bounds, causal removal | E3 S3.3–S3.4 | ✓ Covered |
| FR20 | P1 effect fixtures and boundary matrix | E3 S3.3–S3.6 | ✓ Covered |
| FR21 | Deterministic same-second resolution | E3 S3.5 | ✓ Covered |
| FR22 | Physical reach, access, doors, beds | E4 S4.1–S4.3 | ✓ Covered |
| FR23 | Ownership/knowledge separation and item identity | E4 S4.4–S4.5 | ✓ Covered |
| FR24 | Ivo's Home access fixture and persistence | E4 S4.2–S4.3, S4.6 | ✓ Covered |
| FR25 | Hunger bands and Starved | E5 S5.1–S5.2 | ✓ Covered |
| FR26 | Sleep bands and Exhausted | E5 S5.1, S5.3 | ✓ Covered |
| FR27 | Adequate sleep and Exposed | E5 S5.3 | ✓ Covered |
| FR28 | Food batches, expiry, and poisoning formula | E5 S5.4–S5.5 | ✓ Covered |
| FR29 | Six authored food fixtures and processing | E5 S5.1, S5.4–S5.6 | ✓ Covered |
| FR30 | Status/effect/need inspection | E1 S1.11; E3 S3.6; E5 S5.6 | ✓ Covered |
| FR31 | Same-rule NPC planning and off-screen equivalence | E6 S6.1, S6.6 | ✓ Covered |
| FR32 | Feasible hunger/shelter and risky alternatives | E6 S6.2, S6.5 | ✓ Covered |
| FR33 | Finite jobs, wages, demand, and replanning | E6 S6.3–S6.4 | ✓ Covered |
| FR34 | Ivo/Tessa controlled livelihood fixture | E6 S6.3–S6.6 | ✓ Covered |
| FR35 | Four-household stability and protection solutions | E7 S7.1–S7.4 | ✓ Covered |
| FR36 | Ward warnings, expiry, causality, continued play | E7 S7.1–S7.4 | ✓ Covered |
| FR37 | Alchemy/Brewing lifecycle and product categories | E7 S7.7–S7.10 | ✓ Covered |
| FR38 | Tools, uncertain substitution, recipe-track progression | E7 S7.1, S7.7–S7.8, S7.11–S7.17 | ✓ Covered |
| FR39 | Exact recipes and finite P5 economy/demand | E7 S7.6–S7.18 | ✓ Covered |
| FR40 | Two affinity packages, slots, and starting spells | E8 S8.1–S8.2 | ✓ Covered |
| FR41 | Rest-stone rarity, capacity, awakening, presentation | E8 S8.3–S8.6 | ✓ Covered |
| FR42 | Recognition, Sandglass, title, clue, Deepened variant | E8 S8.7–S8.11 | ✓ Covered |
| FR43 | Concern and commitment lifecycle | E7 S7.5; E9 S9.1–S9.5 | ✓ Covered |
| FR44 | Daily quest categories, refresh, rewards, expiry | E9 S9.1–S9.5 | ✓ Covered |
| FR45 | Visible gacha pool, Catalyst, and Token | E9 S9.6–S9.8 | ✓ Covered |
| FR46 | Private hidden condition and bounded reward | E10 S10.1–S10.7 | ✓ Covered |
| FR47 | Combat initiative, actions, movement, escape/surrender | E11 S11.1–S11.2, S11.6–S11.8 | ✓ Covered |
| FR48 | Combat attacks, costs, damage, and atomicity | E11 S11.2–S11.5 | ✓ Covered |
| FR49 | Player/robber fixtures, outcomes, XP, purse | E11 S11.1, S11.3–S11.9 | ✓ Covered |
| FR50 | Probability-based XP and uncapped progression | E1 S1.10 | ✓ Covered |
| FR51 | Authoritative inventory and staged item budgets | E1 S1.11; E4 S4.4; E7 S7.7–S7.18 | ✓ Covered |
| FR52 | Action-driven simulation, pause, expansion handling, persistence | E1 S1.13; E2 S2.5; E3–E11 gate-verification stories | ✓ Covered |

### Missing Requirements

No normalized GDD functional requirement is missing from the epics and stories document.

The epics document also contains finer-grained downstream requirements that are not separate requirements in the GDD: Main Notebook presentation, durable-operation lifecycle and recovery, read-only diagnostics, technical migration behavior, architecture constraints, and UX component/state requirements. These refine the GDD rather than contradict it, but their source traceability depends on the architecture and UX documents remaining authoritative.

### Coverage Statistics

- Total normalized GDD FRs: 52
- GDD FRs covered in epics/stories: 52
- Missing GDD FRs: 0
- GDD FR coverage: 100%
- Native epics FR inventory: 84
- Native epics FRs assigned to an epic: 84 (100%)

### Coverage Caveat

The epic document's frontmatter names `_bmad-output/game-architecture.md` as an input even though Step 1 found no architecture artifact under the configured `planning-artifacts` directory. This is a document-location/inventory inconsistency, not an FR coverage gap; it must be resolved during the overall readiness assessment so the architecture-derived requirements can be validated against their actual source.

## UX Alignment Assessment

### UX Document Status

**Found and reviewed:**

- `_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/DESIGN.md` — final, implementation scope P0
- `_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md` — final, implementation scope P0

**Architecture source reviewed:**

- `_bmad-output/game-architecture.md` — Architecture 1.2, complete, reconciled to GDD 0.8 and the final UX spines

### UX ↔ GDD Alignment

The UX contract is strongly aligned with the authorized P0 GDD scope:

- Title, New Game, Continue, three save slots, safe save-index failure, and branch restoration match the GDD.
- Rowan-led Session 0, exact player-authored fields, fixed-array assignment, review/correction, explicit confirmation, zero fictional time, and player-selected naming match the GDD.
- The single free-text composer, Enter/Shift+Enter behavior, neutral clarification, factual controls, exact intention echo, and prohibition on suggested actions match G06 and the intent lifecycle.
- Transcript, journal, inventory, character sheet, and roll details preserve the GDD's fact/observation/belief and player-knowledge boundaries.
- Time-free reading/UI operations and time-consuming speech, movement, handling, and waiting match G04.
- Browser-owned sizing, 200% zoom, 320 CSS px reflow, visible focus, non-color speaker labeling, reduced motion, and no timed reading match and elaborate G15.
- Separate deferred System and award voices match the GDD's P6–P8 distinctions without introducing them into P0.
- The three P0 key flows faithfully cover Session 0, the E1 persistent-world loop, and E2 social-causality flow, including their failure paths and idempotency expectations.

UX requirements that extend beyond explicit GDD wording—WCAG 2.2 AA, contrast ratios, minimum pointer targets/spacing exception, semantic landmarks, focus containment/return, polite status announcements, and detailed component states—are compatible downstream constraints rather than scope conflicts.

### UX ↔ Architecture Alignment

Architecture 1.2 provides direct support for the P0 UX contract:

- React DOM and CSS support the semantic text-first notebook rather than requiring a canvas or game-engine renderer.
- The generated OpenAPI client, Zod validation, TanStack Query server state, and presentation-only local React state preserve backend authority and truthful UI state.
- Durable operation resources, typed SSE events, polling recovery, idempotent request IDs, revision checks, and commit-boundary metadata support pending, clarification, committed-but-narrating, interrupted, failed, and recovered states.
- Purpose-built journal, inventory, character, result-detail, save-index, Session 0, and save/load projections support the documented surfaces and distinguish empty, loading, failure, and corrupt evidence.
- Backend knowledge filtering before serialization supports the no-hidden-state UX boundary.
- The shared dialog shell, one-overlay rule, focus containment/return, explicit labels, keyboard operation, contrast gates, zoom/reflow checks, and reduced-motion behavior are named architecture acceptance gates.
- The architecture inherits the G16 responsiveness targets and supplies browser/component/integration testing through Vitest, Testing Library, Playwright, FastAPI, and real SQLite.

### Alignment Issues

1. **P1–P9 UX is deliberately not implementation-ready.** Both UX documents are scoped to P0. `EXPERIENCE.md` requires a phase-specific UX update before implementing each of E3–E11, and the epics/architecture repeat that gate. Architecture provides projection boundaries for later systems, but not a complete later-stage player-experience contract. This is aligned planning, but it restricts the current readiness decision to P0.

2. **Stale technology-selection sentence in `EXPERIENCE.md`.** Its Foundation section says no engine, UI framework, LLM provider, storage technology, public deployment model, or audio system has been selected. Architecture 1.2 has selected React/FastAPI/SQLite and a loopback packaging model, while still deferring the LLM provider, public deployment, and audio. The UX sentence should be revised to say that UX does not own those selections or to reflect the architecture's current choices.

3. **Typography unit ambiguity in Architecture 1.2.** `DESIGN.md` specifies story text as `1.125rem` and forbids replacing browser root sizing with a fixed-pixel root. The architecture correctly preserves browser sizing elsewhere, but its visual gate describes a “specified 18px baseline.” Implementation should use the `rem` token (which commonly computes to 18 px at a default root) and must not hard-code a root or story size in pixels.

4. **Architecture discoverability mismatch.** The architecture is valid and cited by downstream artifacts but lives outside the configured `planning-artifacts` directory, so the prescribed readiness discovery patterns initially reported it missing. Either move/copy it into the configured artifact location or update project/workflow configuration so future readiness runs discover the authoritative file consistently.

### Warnings

- Architecture validation is documentary only: it explicitly reports that no runtime, performance, migration, or accessibility-conformance validation has been executed.
- Architecture's technology compatibility check is historical (2026-09-08 in the document) and must be refreshed at scaffolding; this does not block document-level P0 alignment but is a pre-implementation action.
- The promoted mockup is illustrative; DESIGN and EXPERIENCE remain authoritative wherever it conflicts.

### UX Alignment Conclusion

P0 UX, GDD, and Architecture are substantively aligned, with no player-flow or authority-boundary contradiction that prevents P0 planning. Readiness must remain **P0-only** until later stages receive their required phase-specific UX updates. The stale framework/storage sentence, `rem`/18px wording, and architecture location should be corrected to eliminate avoidable implementation ambiguity.

## Epic Quality Review

### Review Scope and Counts

- Epics reviewed: 11
- Stories reviewed: 101
- BDD scenarios reviewed structurally: 1,303
- Stories with 0–9 scenarios: 5
- Stories with 10–14 scenarios: 79
- Stories with 15–17 scenarios: 17
- Stories missing an `As a/an … / I want … / So that …` statement: 0
- Stories with mismatched Given/When/Then/And counts: 0
- Explicit forward story references found: 0

### Epic Structure

All 11 epics express player-visible value rather than technical milestones. Epic 1 establishes a playable persistent campaign; Epic 2 completes P0 social causality using only Epic 1; and Epics 3–11 follow the approved evidence-gated P1–P9 order without requiring a later epic. No circular or forward epic dependency was found.

Epic 1 Story 1.1 is implementation-foundation work, but it is the correct exception: Architecture explicitly requires create-vite plus a uv-managed FastAPI application as the starter approach, and the story includes initialization, dependency/lockfile, SQLite, local packaging, security boundary, quality-baseline, and no-speculative-module criteria.

### Dependency and Data-Timing Assessment

- Story order is consistently backward-dependent: later stories reuse capabilities introduced earlier in the same epic or in a proven earlier epic.
- Explicit `Story X.Y automated evidence` references point to the current or an earlier story; none points forward.
- Each conditional stage begins with an explicit migration/upgrade story and rejects skipped or unauthorized stages.
- P0 setup explicitly prohibits speculative P1–P9 modules, state, migrations, and UI.
- Later data structures are introduced by the first owning stage rather than created wholesale in Story 1.1.
- Combat is correctly defined as coordination over previously delivered systems rather than a parallel future-dependent rules engine.

### Acceptance-Criteria Quality

Acceptance criteria are unusually specific and consistently use BDD structure. Across 101 stories, the document contains equal counts of Given, When, Then, and And clauses. Happy paths, validation failures, insufficient resources, rollback/commit boundaries, idempotency, save/load, branch isolation, accessibility, and real-application verification are broadly covered. Vague statements such as “player can move” were not found as substitutes for measurable behavior.

The acceptance detail is therefore a strength, but its volume creates the principal quality defect below.

### 🔴 Critical Violations

#### 1. Systemic epic-sized story scope

Ninety-six of 101 stories contain at least ten independent BDD scenarios; 17 contain 15–17. Several stories combine multiple separately implementable and independently testable capabilities:

- **Story 1.9** combines movement, dialogue timing, item handling, transactions, several wait modes, interruption, and fixture isolation.
- **Story 1.10** combines check resolution, natural-roll behavior, probability, XP, multi-level progression, skill growth, attribute-point preview/confirmation, and persistence.
- **Story 3.2** combines three resource pools, affordability, recovery, maximum recalculation, wounds, zero-Stamina behavior, death, and revival boundaries.
- **Story 3.4** combines all duplicate policies, modifier arithmetic, cancellation, removal categories, use consumption, and persistence.
- **Story 5.3** combines fatigue bands, Exhausted stacking, recovery, continuous sleep, bed/capacity/protection interruption, and Exposed interaction.
- **Story 5.4** combines six food definitions, facility/tool validation, occupied and unattended processing, batch expiry, atomicity, and persistence.
- **Story 11.5** combines item use, poison delivery, effects, zero Health, death, timed revival, wounds, recovery, save/load, and accessibility.
- Gate stories **8.12, 9.10, 10.7, and 11.11** each span an entire stage with 15–17 scenarios and are release-test plans rather than sprint-sized stories.

**Impact:** These stories cannot be estimated, implemented, reviewed, or rolled back as small vertical increments. A partially complete story may contain working player value but still appear wholly unfinished, obscuring delivery state and increasing merge/test risk.

**Required remediation:** Split the named stories—and review the remaining 79 ten-to-fourteen-scenario stories—into smaller vertical slices with one cohesive player outcome each. Move stage-wide evidence matrices into an epic Definition of Done or dedicated test-plan artifact. Preserve every existing acceptance scenario by reallocating it; do not delete coverage.

### 🟠 Major Issues

#### 2. Cross-cutting acceptance boilerplate obscures story-local scope

Accessibility, idempotency, save/load, real-SQLite verification, and first-party no-mocking criteria are repeated in most stories. These are valid requirements, but repeated cross-cutting clauses inflate stories and make it harder to see what behavior is unique to each story.

**Impact:** Maintenance drift becomes likely when a shared policy changes, and developers may treat repeated boilerplate as the story's primary scope rather than its player outcome.

**Recommendation:** Keep story-specific boundary cases in the story, but place universal quality rules in a referenced Definition of Done/NFR matrix. Retain targeted story clauses only where a cross-cutting rule has unique behavior—for example mid-combat persistence or hidden-condition secrecy.

#### 3. Verification-gate work is mixed with feature-story structure

Stories 1.13, 2.5, 3.6, 4.6, 5.6, 6.6, 7.19, 8.12, 9.10, 10.7, and 11.11 combine player/playtester inspection features, automated verification, play evidence, and stage promotion decisions. Some deliver useful inspection capability; others primarily restate an epic-wide quality gate.

**Impact:** Completion depends on all prior stage work and operational evidence, so these items are not independently completable feature stories and can become oversized release containers.

**Recommendation:** Separate any player-visible inspection capability into feature stories, and model the remaining verification work as explicit epic acceptance/exit criteria or bounded QA stories with named fixtures and commands.

#### 4. Architecture-to-story references are stale

Architecture 1.2's requirement-to-verification table still references the earlier five-epic numbering—for example, G18 points to Story 3.5 and G04 to Stories 3.1–3.2—while the current epics place those concerns in Stories 1.10 and 1.9. The architecture acknowledges that this is historical and marks implementation-epic mapping pending, but the table itself is not clearly separated from the current mapping.

**Impact:** An implementer following the architecture table can open the wrong story, and automated traceability cannot reliably distinguish legacy from current identifiers.

**Required remediation:** Update Architecture 1.2's requirement-to-verification map to the current 11-epic/101-story identifiers, mark Implementation Epic Mapping as PASS only after review, and remove or explicitly label the legacy table as historical.

#### 5. Conditional stages lack current UX contracts

Epics 3–11 contain detailed UI/accessibility acceptance criteria, yet the authoritative UX pair explicitly excludes P1–P9 and requires a phase-specific UX update before each stage. Upgrade stories correctly block activation when that contract is missing, so this is not a forward-code dependency, but it prevents those stories from being implementation-ready today.

**Impact:** Later-stage player surfaces could be implemented from inferred story text rather than an approved experience model.

**Required remediation:** Before authorizing each later epic, produce and reconcile its phase-specific UX update, then revise the affected story criteria if necessary.

### 🟡 Minor Concerns

#### 6. Source-document and location hygiene

- The architecture lives outside the configured planning-artifacts directory.
- The epics frontmatter includes an older readiness report as an input even though Architecture states prior readiness reports are not proof of current alignment.
- `EXPERIENCE.md` has a stale sentence about the framework/storage stack being unselected.

These do not invalidate story behavior, but they weaken source-of-truth clarity and repeatability of future readiness runs.

#### 7. Verification personas are inconsistent

Most stage-gate stories use “As a playtester,” while Story 11.11 uses “As a player” despite being principally a complete-stage verification gate. This is minor but reinforces the mixed feature/QA purpose.

### Best-Practices Compliance Summary

| Area | Result | Notes |
| --- | --- | --- |
| Epic player value | Pass | All epic titles and goals describe playable outcomes |
| Epic independence | Pass | No epic depends on a future epic |
| Story value | Partial | Most are player-centered; several gate stories are primarily QA/release work |
| Story sizing | Fail | Systemic oversizing; 96/101 have at least ten scenarios |
| Forward dependencies | Pass | None found |
| Data/entity timing | Pass | Stage-owned migrations and no speculative later-stage models |
| BDD format | Pass | 1,303 complete Given/When/Then/And scenario groups |
| Testability/specificity | Pass | Strong numeric, failure, atomicity, and persistence criteria |
| Error/recovery coverage | Pass | Broad and explicit |
| FR traceability | Pass | 52/52 normalized GDD FRs and 84/84 native epic FRs mapped |
| Starter-template compliance | Pass | Story 1.1 matches Architecture's required scaffold |
| Current UX authorization | P0 only | P1–P9 remain gated on phase-specific UX |

### Epic Quality Conclusion

The epic structure, sequencing, traceability, and acceptance specificity are strong. The plan nevertheless fails strict story-sizing best practice and requires decomposition before it can serve as a reliable sprint backlog. P0 has fewer external-document blockers than later stages, but its Stories 1.9, 1.10, and 1.13 still require splitting or explicit treatment as multi-story work packages.

## Summary and Recommendations

### Overall Readiness Status

**NEEDS WORK**

The planning set has complete GDD-to-epic functional coverage, a coherent architecture, strong P0 UX alignment, sequential evidence gates, and highly testable acceptance criteria. It is not yet a reliable implementation backlog because story scope is systematically oversized. The current decision is therefore:

- **P0:** Document-aligned but not backlog-ready until its oversized stories are decomposed and the current architecture/story traceability is refreshed.
- **P1–P9:** **Not ready for implementation.** Each remains conditional on preceding evidence and on the phase-specific UX update explicitly required by the authoritative UX documents and stage-upgrade stories.

### Critical Issues Requiring Immediate Action

1. **Decompose epic-sized stories before implementation.** Ninety-six of 101 stories have at least ten BDD scenarios, including 17 with 15–17. Begin with P0 Stories 1.9, 1.10, and 1.13; they combine multiple independently implementable behaviors and block a trustworthy sprint plan.
2. **Do not authorize P1–P9 from the current UX set.** DESIGN and EXPERIENCE are P0-only and explicitly require phase-specific UX updates for E3–E11.

### Other Material Issues

- Architecture's requirement-to-verification table uses legacy story identifiers and still marks implementation-epic alignment pending.
- Cross-cutting NFR/test boilerplate is repeated across most stories rather than managed through a shared Definition of Done or verification matrix.
- Stage-gate evidence is often packaged as an oversized feature story instead of bounded QA/exit criteria.
- The architecture file's nonstandard location prevents the configured discovery pattern from finding it.
- `EXPERIENCE.md` has stale framework/storage-selection wording, and Architecture's “18px baseline” wording should explicitly defer to DESIGN's `1.125rem` token.
- Architecture's dependency/version compatibility evidence is historical and must be refreshed when scaffolding.

### Recommended Next Steps

1. **Refactor the P0 backlog first.** Split Stories 1.9 and 1.10 into cohesive vertical slices; separate Story 1.13's player-visible diagnostics from P0 evidence/exit criteria. Preserve all existing acceptance scenarios and remap native FR coverage.
2. **Create one shared delivery-quality contract.** Move universal accessibility, atomicity/idempotency, real-SQLite, no-first-party-mocking, save/load, and evidence-command rules into a referenced Definition of Done/NFR verification matrix; keep only behavior-specific exceptions in each story.
3. **Refresh Architecture 1.2 traceability.** Replace legacy five-epic story references with the current 11-epic mapping, set Implementation Epic Mapping to its reviewed result, and cite this readiness report or an equivalent controlled mapping.
4. **Fix source hygiene.** Put the authoritative architecture where the planning-artifact configuration discovers it or update the configuration; remove or clearly demote obsolete readiness reports as planning inputs; revise the stale UX stack sentence and typography wording.
5. **Re-run readiness for P0 after decomposition.** Confirm no FR or AC was lost, every new story is independently completable, and the current architecture mapping is accurate.
6. **Gate later stages individually.** After P0 evidence passes, create the P1 UX update, reconcile GDD/architecture/epics, and repeat for each subsequent stage rather than treating the complete P1–P9 story catalogue as currently authorized work.
7. **At scaffolding, revalidate the toolchain.** Confirm current compatibility and availability of the pinned React, FastAPI, Python, TypeScript, SQLite, and test-tool versions before creating lockfiles.

### Consolidated Issue Count

This assessment identified **7 consolidated issues across 4 categories**:

- Backlog sizing and story independence: 1 critical issue
- Cross-cutting quality and gate-story structure: 2 major issues
- Architecture/UX traceability and stage authorization: 2 major issues
- Artifact hygiene and persona consistency: 2 minor concerns

### Final Note

There are no missing GDD functional requirements in the epic plan and no forward or circular epic dependencies. The blocker is execution shape, not product intent: the documents describe what to build well, but the current stories bundle too much work to serve as dependable implementation units. Address the critical P0 decomposition and traceability corrections before production implementation; retain P1–P9 as explicitly conditional future stages.

**Assessment date:** 2026-09-22  
**Assessor:** Codex, following the `gds-check-implementation-readiness` workflow
