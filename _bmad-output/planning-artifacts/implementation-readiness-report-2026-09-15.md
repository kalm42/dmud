---
stepsCompleted:
  - step-01-document-discovery
  - step-02-gdd-analysis
  - step-03-epic-coverage-validation
  - step-04-ux-alignment
  - step-05-epic-quality-review
  - step-06-final-assessment
overallStatus: NOT_READY
filesIncluded:
  gdd:
    - _bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/gdd.md
    - _bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/decision-log.md
    - _bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/epics.md
  architecture:
    - _bmad-output/game-architecture.md
  epics:
    - _bmad-output/planning-artifacts/epics.md
  ux:
    - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/DESIGN.md
    - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md
    - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/reconcile-brief.md
    - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/reconcile-gdd.md
    - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/review-rubric.md
    - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/validation-report.md
    - _bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/mockups/direction-dm-notebook.html
documentRoles:
  authoritativeEpics: _bmad-output/planning-artifacts/epics.md
  supportingChangeResolution: _bmad-output/planning-artifacts/gdds/gdd-dmud-2026-09-07/epics.md
---

# Implementation Readiness Assessment Report

**Date:** 2026-09-15
**Project:** dmud

## Document Inventory

### GDD

- Primary GDD: `gdds/gdd-dmud-2026-09-07/gdd.md` (97,581 bytes; modified 2026-09-15)
- Decision log: `gdds/gdd-dmud-2026-09-07/decision-log.md` (62,373 bytes; modified 2026-09-15)
- Supporting change-resolution artifact: `gdds/gdd-dmud-2026-09-07/epics.md` (16,772 bytes; modified 2026-09-15)

### Architecture

- `_bmad-output/game-architecture.md` (101,799 bytes; modified 2026-09-12). This valid architecture artifact is outside the configured planning-artifacts folder and was discovered through the authoritative epics document after the initial pattern-based search.

### Epics and Stories

- Authoritative implementation plan: `epics.md` (254,922 bytes; modified 2026-09-12)
- The similarly named GDD-local file is intentionally used for resolving changes and is not authoritative.

### UX Design

- `ux-designs/ux-dmud-2026-09-08/DESIGN.md` (12,012 bytes; modified 2026-09-08)
- `ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md` (24,418 bytes; modified 2026-09-08)
- Supporting reconciliation, review, validation, and mockup artifacts are included from the same versioned UX folder.

## GDD Analysis

Source analyzed completely: `gdds/gdd-dmud-2026-09-07/gdd.md`, version 0.6, updated 2026-09-15. The GDD is an approved staged design baseline: P0 is the initial implementation; P1–P9 are conditional stages and must not become P0 prerequisites.

### Functional Requirements

FR1 [P0]: The title screen shall present New Game and Continue.

FR2 [P0]: Continue shall open a three-slot save selector when saves exist; with no saves it shall remain visible but unavailable with an explanation; a save-index failure shall offer retry while New Game remains usable.

FR3 [P0]: New Game shall begin a zero-fictional-time Session 0 led by Rowan, covering the character's name, origin, cares, hates, especially cool ideas, and campaign hopes.

FR4 [P0]: Session 0 shall keep character authorship with the player, offer suggestions only when explicitly requested, distinguish character facts, agreed premises, preferences, and non-binding hopes, and permit corrections to the review and stat assignment until explicit confirmation.

FR5 [P0]: Confirmation shall atomically establish the character and initial world state and open at Market Square without predetermining an NPC decision, route, success, or campaign outcome. “James” is only a UX example; the player supplies the character name.

FR6 [P0]: Player input shall express an intention rather than directly edit authoritative state; routine feasible actions succeed without a roll, impossible or unsupported actions receive a factual explanation, and social success cannot override binding obligations or create obedience.

FR7 [P0]: Before a consequential action, the game shall expose reasonably knowable stakes, cost, and interpretation, clarify rare-resource spending or materially changed intent, fix difficulty before rolling, and validate contextual consequences before committing state.

FR8 [P0]: Rejected proposals shall change no state; retries shall not duplicate purchases, costs, time, or rolls; an unchanged failed approach shall not create unlimited new checks.

FR9 [P0]: Eligible uncertain checks shall use natural 1 automatic failure, natural 20 automatic success, and otherwise `d20 + attribute modifier + relevant basic-skill bonus >= difficulty`.

FR10 [P0]: The five attributes shall be Body, Agility, Constitution, Mind, and Presence; Session 0 shall assign each value in 8, 10, 12, 13, and 14 exactly once; modifiers shall equal `floor((score - 10) / 2)`.

FR11 [P0]: Confirmed starting-array assignments shall remain immutable while earned attribute points change current scores; attributes and skill bonuses shall have no design cap.

FR12 [P0]: Player levels shall grant allocatable attribute points, skill levels shall increase the corresponding skill bonus, and neither levels nor skills shall introduce classes or gate universal basic-skill access.

FR13 [P1]: Every character shall have integer current and Base Maximum resource pools where Health is Body × Constitution, Mana is Body × Mind, and Stamina is Agility × Constitution; new characters and P0 migrations shall initialize all three at maximum.

FR14 [P1]: The Mara, Oren, Tessa, and Ivo controlled fixtures shall use the G22/G24 standard-array assignments and derived maxima specified in the GDD.

FR15 [P1]: A permanent attribute increase shall recalculate affected Base Maxima and add the same positive difference to current pools; a decrease shall recalculate and clamp; temporary check modifiers shall not alter Base Maxima unless explicitly declared.

FR16 [P1]: Effective Maximum shall mean Base Maximum after active effects; percentage restoration, current-pool caps, and percentage thresholds shall use Effective Maximum unless a rule explicitly names Base Maximum; current pools shall remain between zero and Effective Maximum.

FR17 [P1]: Save/load shall restore current Health, Mana, and Stamina and verify Base Maxima against saved attributes.

FR18 [P1/P6/P9]: A spell shall spend Mana only when its effect commits; insufficient Mana shall reject the cast without effect, cost, or fictional-time mutation.

FR19 [P1]: Eight hours of adequate sleep shall restore all Mana and 25% of Effective Maximum Health rounded up; ten uninterrupted non-strenuous minutes shall restore 25% of Effective Maximum Stamina rounded up; time passage and eating alone restore none of these pools.

FR20 [P1/P9]: Stamina expenditure shall use Routine 0, Exerting 5, Strenuous 10, and Extreme 20; the full cost must be payable before an action begins and rejection shall spend neither time nor partial Stamina.

FR21 [P1]: At zero Stamina, a character shall be unable to move or perform Stamina-costing actions but may talk, inspect, eat, use suitable items, and attempt sleep; zero Stamina shall not itself be lethal.

FR22 [P1/P9]: Damage shall reduce Health; injuries may independently add Minor or Severe Wounds; zero Health shall cause death; revival shall require an explicitly supported effect within its declared window; player defeat shall offer recovery from a manual save without forced save deletion, while NPC death persists unless reversed by a supported effect.

FR23 [P1]: Conditions, buffs, debuffs, and item treatments shall share a configurable effect language whose definitions declare source, category, polarity, tier, magnitude, duration, removal, duplicate behavior, and player knowledge.

FR24 [P1]: The effect system shall support Health, Mana, Stamina, effective maxima, checks, Defense, movement, damage, healing, and spell/action-cost targets; unsupported or over-budget proposals shall be rejected or reduced before commitment; accepted definitions shall receive stable identities.

FR25 [P1]: Each effect definition shall select Stack, Refresh, or Replace behavior; different named effects may coexist; generated effects shall have one primary mechanical shape, while authored effects may combine separately balanced components.

FR26 [P1]: Ordinary modifiers shall resolve as `round(Base × (1 + sum percentage modifiers)) + sum flat modifiers`; percentages shall add rather than compound, opposing percentages shall cancel numerically without removing effects, flat modifiers shall apply afterward, affected values shall not fall below zero, and costs shall not fall below one unless explicitly allowed.

FR27 [P1]: Effect validation shall enforce the G24 Subtle, Standard, and Major source eligibility and flat, proportional, and periodic-damage limits.

FR28 [P1]: The fictional source shall fix maximum tier, eligible targets, and an explicit maximum duration, uses, or terminating condition before a check; difficulty shall determine success rather than magnitude; natural 20 shall not raise tier; natural 1 shall create no effect; repeated mundane actions shall not manufacture Major power.

FR29 [P1]: Every effect shall record one causal category and be removable only by its declared cause, a compatible category, or an exact remedy; numerical opposition shall not remove independently expiring effects.

FR30 [P1]: The controlled effect fixtures shall implement Sharpened, Bleeding, opposed ±25% modifiers, Star-metal Edge, and an exact-limit/over-limit tier-by-shape calibration matrix exactly as specified by G24.

FR31 [P1–P3]: Same-timestamp changes shall resolve in this order: completed actions and intervals in commitment order; scheduled effect ticks and unmet-need thresholds in creation order; effect expirations and environmental transitions; then Base/Effective recalculation, clamps, and terminal states. The GDD's exact-boundary meal, sleep, treatment, final-tick, and protection cases shall follow this ordering.

FR32 [P0]: Contextual difficulty shall be declared before rolling, include all bonuses and natural-roll overrides in its pre-roll probability, and remain unchanged after the result; impossible or unsupported actions shall be screened before a roll.

FR33 [P0]: The controlled payment-extension fixture shall use Presence 14 (+2), Persuasion +1, difficulty 12, and 60% success; success grants a one-day extension, failure leaves the deadline unchanged, and neither outcome reverses a prior gift.

FR34 [P0]: Difficulty shall reflect the attempted feat and circumstances and shall not rise for the same unchanged task merely to cancel earned competence; genuinely harder chosen feats may use higher targets.

FR35 [P0]: The shared action clock shall use seconds; travel, conversation, handling, and waiting shall advance time, while typing, reading, model latency, menus, known-information inspection, inventory, journal, and saving shall not; closing the game shall pause time.

FR36 [P0]: Travel shall use distance divided by a supported movement speed and round each completed segment up to a whole second; the controlled speeds and 7 m/140 m routes shall produce the exact G04 fixture durations.

FR37 [P0]: A completed dialogue exchange shall advance `15 × ceil(rendered spoken words / 30)` seconds, count player and NPC speech once, exclude narration and reasoning, and commit only completed speech/action segments when interrupted.

FR38 [P0]: Object handling shall use a validated contextual duration; the prepared 10,000-gold pouch transfer shall take five seconds, whereas counting 100 loose coins shall take at least 100 seconds; interrupted transfers may advance completed time without transferring the object until handover completes.

FR39 [P0]: The campaign epoch shall be day 1 at 00:00 and a newly confirmed campaign shall begin at 08:00; Session 0 shall advance no time; waits shall target explicit durations, clock targets, or actual event conditions without manufacturing requested events.

FR40 [P0]: Face-to-face silent waiting shall return control after 60 seconds; uneventful overnight waits shall not interrupt each minute; impossible or unscheduled event waits shall report their state rather than run indefinitely.

FR41 [P0]: Each named NPC shall have a need, competing desire, obligation, relationship, resources, current plan, and limited knowledge; NPC plans shall use rules for routine actions and LLM reasoning within recorded constraints for consequential replanning and dialogue.

FR42 [P0]: Authoritative events, observations/received beliefs, and player-facing presentation shall remain distinct; beliefs shall record source, time, uncertainty, and distortion; information shall require plausible observation or communication and shall not rewrite history or compel action.

FR43 [P0]: The controlled social scenario shall contain Mara, Oren, Tessa, and Ivo; Market Square, Mara's Stall, and the Common Room; the specified debt, desires, contact timing, 10,000 test gold, five-drink stock, one-gold purchase, gift/no-gift comparison, and separate distorted-rumor variant.

FR44 [P0]: Observation, contact, received claims, and resulting action shall be inspectable for testing while player presentation respects limited knowledge; memory shall be demonstrated through state-supported follow-up behavior rather than an internal flag alone.

FR45 [P2]: Resources shall be usable only where physically present and reachable; ownership shall neither grant remote access nor make unauthorized physical use impossible.

FR46 [P2]: Access shall support ownership, permission, relationship, compatible keys, unlocked entrances, lockpicking, and forced entry; doors shall record open, closed, locked, and broken states; beds shall record capacity and allow adequate sleep for permitted occupants within capacity.

FR47 [P2/P3]: Unauthorized eating or sleeping shall still satisfy physiological rules when the resource and environment qualify, while trespass, theft, damage, noise, observations, beliefs, and relationship consequences persist.

FR48 [P2]: Distinctive objects shall retain identity, possessor, legitimate claim, provenance, and recognizable marks; fungible goods shall track quantities and transfers but lose unique traceability after mixing while allowing equivalent restitution.

FR49 [P2]: Unseen removal shall create no knowledge; later inspection and remembered state may create a missing-item belief; thief identity shall remain a hypothesis until evidence supports it, and suspicion may be reasonable but wrong.

FR50 [P2]: Ivo's Home shall provide the G25 door, key, permission, bed-capacity, lockpicking, forced-entry, noise, fungible-theft, and distinctive-theft fixtures with their specified difficulties, durations, consumptions, Stamina costs, and state transitions.

FR51 [P2]: Save/load shall preserve access state, keys, permission, possession, event history, observations, and beliefs.

FR52 [P3]: Every character shall record the last completed meal and last completed adequate sleep; player needs shall remain information and consequences rather than forced intentions.

FR53 [P3]: Hunger priority shall follow the G26 time bands; at each 24 consecutive hours without eating, one Starved stack shall apply; Effective Maximum Health shall equal `round(Base Maximum Health × 0.75^stacks)` and clamp current Health without damage; a complete serving shall reset the timer and remove one stack without healing; a rounded maximum of zero shall cause death.

FR54 [P3]: Sleep priority shall follow the G26 time bands; at each 24 consecutive hours without adequate sleep, one Exhausted stack shall apply; Effective Maximum Stamina shall equal `round(Base Maximum Stamina × 0.75^stacks)` and clamp current Stamina without expenditure; eight adequate hours shall reset the timer, remove one stack, and restore Stamina to the new maximum.

FR55 [P3]: Adequate sleep shall require one continuous eight-hour interval with a usable bed and valid protection throughout; interruption, bed loss, leaving, or protection lapse shall make it inadequate; ordinary ten-minute-rest restoration, hunger, and timed effects shall still progress during sleep.

FR56 [P3/P5]: Exposed shall describe an unprotected sleeping place, block safe sleep and G01 qualification, deal no damage, and remove no food; valid protection or relocation shall prevent or remove it, while a missing bed remains a separate failure.

FR57 [P3]: One complete serving shall reset hunger and remove one Starved stack; food definitions shall support raw-edibility, ingredients, tools/facilities, preparation time, Stamina, yield, batch expiration, price, taste, preferences, and optional effects; taste shall influence choice and price rather than hunger.

FR58 [P3]: Food batches shall have one expiration timestamp unaffected by storage; crafted output expiry shall be based on completion plus recipe shelf life independently of ingredient age; expired food shall remain edible and satisfy hunger.

FR59 [P3]: Expired-food risk shall use the specified linear formula and nearest-achievable Constitution difficulty under the 5%–95% natural-roll bounds; failure shall apply a physiological food-poisoning effect of the specified overdue tier; success-only XP rules shall apply.

FR60 [P3]: The food system shall provide the six G26 fixtures—raw cabbage, cabbage stew, pound cake, sauerkraut, cooked meat, and cured meat—with their exact inputs, facilities, work, Stamina, yields, and shelf lives.

FR61 [P3]: Missing food inputs or facilities shall reject preparation before costs commit; routine known recipes shall succeed; substitutions and novel approaches shall use G03; unoccupied curing and fermentation shall advance on the shared clock and persist through save/load.

FR62 [P3]: Status shall show current/effective Health, Mana, and Stamina, known effects and their mechanics/sources/removal, time since meal/sleep, and exact time to the next Starved/Exhausted stack without recommending actions; unknown effects shall show symptoms until identified.

FR63 [P4]: Player and NPC characters shall share needs, pools, effects, and death rules; NPC wants shall be shaped by pressure, personality, obligations, knowledge, relationships, resources, risk, and time and shall choose among feasible known plans.

FR64 [P4]: NPC actions shall execute physically on the shared clock, spend the same resources whether observed or off-screen, and replan after failure without invented resources; persistent off-screen death shall require a complete causal chain, and player interruption shall require a reasonably perceivable event.

FR65 [P4]: Hunger plans may use accessible food, preparation, purchases, restaurants, hospitality, borrowing, trade, help, or work; urgent need may broaden socially costly options, but crime or violence shall become eligible only when the full character state supports it and shall never erase consequences.

FR66 [P4]: Sleep plans may use home, lodging, hospitality, bed sharing, repairs, protection, relocation, work, or trade, subject to the same access, time, budget, relationship, and replanning rules.

FR67 [P4]: Jobs shall be learned simulated plans rather than classes or passive income; completed work shall require opportunity, place, time, and inputs, use finite employer/customer budgets and demand, and transfer wages, expenses, goods, services, and ownership only through completed actions.

FR68 [P4]: The Ivo/Tessa proof shall begin with the exact G27 resources and need clocks and support the four-hour courier shift, wage transfer, cabbage purchase, cooking/raw choice, home/bed use, and declared failure-triggered replanning without creating a fifth NPC or unexplained money.

FR69 [P5]: Crafting shall accept an intention, ingredients, workspace, and recipe/approach; feasibility, inputs, tools, and Alchemy/Brewing skill shall determine routine versus uncertain resolution; successful output shall persist with explicit effects, failure shall consume inputs without output, and declared work time shall advance.

FR70 [P5]: Poison applied to a weapon or food shall alter that object's properties until triggered or cleaned, use the appropriate delivery trigger, and persist through save/load.

FR71 [P5]: Crafting shall provide separate healing/restorative, Mana-restoration, poison, and brewed-drink product categories and progression tracks.

FR72 [P5]: P5 shall start with a Field Alchemy Kit, Brewer's Crock, Healing Draft, Mana Draft, Weak Toxin, Common Ale, and Alchemy/Brewing bonuses of zero; tools shall be required by their recipe category.

FR73 [P5]: Exact known base recipes shall be routine; the bruised-duskroot Healing Draft substitution shall use Mind + Alchemy at difficulty 12; failed uncertain crafting shall consume inputs; ingredients, time, output, and XP shall commit atomically.

FR74 [P5]: Each product track shall provide the exact G19 Base, T1, and T2 recipes, inputs, work durations, effects, values, delivery rules, and revival restrictions for Healing, Mana Restoration, Poison, and Brewing.

FR75 [P5]: Each product track shall unlock T1 at 10 successful crafts and T2 at 25 total successful crafts; failed or replayed attempts shall not count; counters, known recipes, and offers shall persist; declining shall re-offer after the next success without replacing earlier recipes.

FR76 [P5]: The P5 economy shall start the player with 30 gold and exclude P0 test funds; the ingredient supplier shall charge the specified prices, cap stock at 20 basic and four rare units, and restock up to—not beyond—those limits at 06:00.

FR77 [P5]: NPC product demand shall be finite, need-driven, funded from owned resources, and use the Mara and Ivo baseline demand fixtures without automatic budget refill; gifts shall not count as sales.

FR78 [P5]: Community victory shall require all four one-resident households to complete three consecutive qualifying days with recorded meals, safe adequate sleep, and protection funded, supplied, earned, transferred, produced, or contractually guaranteed; only a failing household's streak shall reset.

FR79 [P5]: Ward repair shall cost 12 gold and two completed four-hour work actions and grant 30 days of protection; a settlement patrol shall cost 18 gold plus one gold for each of its first three days; relocation shall cost five gold per household and require acceptance by a named destination; causally equivalent supported solutions may qualify.

FR80 [P5]: P5 shall start with seven ward-protected days, show remaining duration on inspection, interrupt long waits at three-day and one-day warnings, and on expiry remove only protection without deleting food, dealing damage, or creating an irreversible lockout.

FR81 [P5]: Community success shall leave the world playable; Tessa, Ivo, and Mara shall retain their specified initial stakeholder pressures without fixed decisions, allowing later events, offers, relationships, and survival needs to change preferences.

FR82 [P5/P7]: The journal shall track concerns and explicit commitments through proposed, accepted, fulfilled, failed, expired, and abandoned states; renegotiation shall record changed terms; acceptance shall record outcome, parties, deadline, evaluator, and exact reward or absence of reward.

FR83 [P7]: The System shall assign three daily objectives in a distinct voice, display explicit success conditions, expose quests in the journal, refresh at 06:00, and award exactly 25 player XP, 25 relevant-skill XP, and one gacha draw only once on full completion; expiry and partial completion shall award nothing and impose no penalty.

FR84 [P7]: Every daily set shall contain one known-recipe crafting quest, one accepted-commitment social quest, and one specified-unknown-condition observation quest; the complete set shall be replaced at 06:00, and combat quests shall remain excluded through P9.

FR85 [P7]: Gacha shall select a tier using 70% Common, 25% Uncommon, and 5% Rare probabilities and then select uniformly within that tier from the visible nine-item G20 pool with the specified effects and values.

FR86 [P8]: Each supported quest shall receive exactly one stable private hidden condition at creation, recording unusual approach, qualifying evidence, evaluation point, and reward; the condition shall never be disclosed before or after resolution.

FR87 [P8]: Hidden reward type shall be chosen uniformly from XP, draw, or Common item; XP shall be 10–25 for both tracks, draw shall add one G20 draw, item shall be uniformly selected from Common items worth at most five gold; only one bonus may be paid and its notification shall use the exact G21 text without explaining the condition.

FR88 [P0]: Controls shall accept free-text intentions and show no suggested actions, recommended choices, dialogue replies, or action chips; linked exits, inventory, journal, save/load, and optional roll details may provide factual controls.

FR89 [P0]: Enter shall submit, Shift+Enter shall add a line, all controls shall be keyboard reachable, ambiguous names shall prompt neutral disambiguation, and unsupported verbs shall explain the limitation without consuming time or automatically suggesting alternatives.

FR90 [P0]: Clarifications shall preserve intent and identify missing information without recommending strategy; request state shall distinguish pending, resolved, and failed; a multi-action request shall expose order, stakes, and stopping conditions before consequential commitment and may require separate P0 submissions.

FR91 [P0+]: Natural-language synonyms shall map to supported intentions without promising an exhaustive verb parser or arbitrary mechanics.

FR92 [P0+]: Locations shall be authored and stable rather than procedurally generated; P0 shall use exactly the three G05 locations with readable exits, present people, and examinable context; later stages shall add only the authored fixture locations required by their proofs.

FR93 [P0+]: First-visit descriptions shall use 60–120 words, repeat visits 20–60 words emphasizing changes, and typical action results 40–120 words.

FR94 [P0+]: Inventory shall authoritatively track ownership, possession, quantity, location, transferability, and distinctive/fungible identity; scenery shall be examinable but not automatically takeable; prize sale or loss shall not erase an earned achievement record.

FR95 [P0+]: Journal summaries shall restate known promises and obstacles without revealing NPC secrets, recommending actions, or requiring an exact phrase to solve a challenge.

FR96 [P0+]: Narration shall use grounded NPC voices and distinguish narrator, NPC, System, award, and mechanics; award narration shall not decide NPC behavior, rewrite events, or recognize outcomes that did not occur.

FR97 [P0]: The opening campaign experience shall fit a 20–60-minute session including Session 0; returning sessions shall target the same duration; each later proof should leave an interesting unfinished concern.

FR98 [P0]: Three manual save slots shall restore the complete world situation specified by G08, including clock, ownership, inventory, relationships, commitments, beliefs, NPC plans, XP/levels, starting and current attributes, bonuses, and allocated/unspent points.

FR99 [P0]: Captured starting state, proposals, and seeded dice shall reproduce mechanical outcomes even if new LLM prose differs; no per-action undo is required; loading an older branch shall restore only that branch's progression and clock without cross-save reward carryover.

FR100 [P0+]: All characters shall be able to attempt the listed universal basic skills subject to feasibility, knowledge, tools, and context; P5 shall add universal Alchemy and Brewing; unsupported complex checks shall report an honest limit rather than require an affinity, title, achievement, stone, or class.

FR101 [P6]: P6 shall offer exactly the Ember + Fellowship and Vessel + Fellowship packages, each with the specified +1 basic-skill bonus, two spell slots per affinity, and the fully parameterized Hearthspark or Steady Vessel starting spell.

FR102 [P6]: A Rest-concept awakening stone shall retain an 80% standard/20% resonant rarity, disclose uniform selection between the two package-supported fixed candidates, require capacity for either outcome, remain unconsumed if invalid, and on valid use permanently award the selected spell into its owning affinity slot.

FR103 [P6]: Rules shall select the fixed spell mechanics while the LLM may generate only a stable player-facing name and one-sentence manifestation informed by concept, affinities, character concept, and committed history.

FR104 [P6]: After three distinct consequential Rest-spell uses and the internally recorded Rest Is Part of the Work trigger, the awarded spell shall become eligible for one optional Deepened replacement; repeating an identical resolved situation shall count once.

FR105 [P6]: The achievement shall use a generated 2–6-word name and one event-grounded sentence, retain a fixed internal ID and trigger, and award a Copper Sandglass worth five gold that reveals one known effect or commitment's exact remaining time once per day; loss or sale shall not erase the achievement.

FR106 [P6]: Meeting G01 shall award the nonstacking Brackenford's Anchor title granting +1 to one Persuasion check per simulated day; titles, achievements, and spell evolution shall remain distinct systems.

FR107 [P6]: Each Deepened choice shall use the exact G12 replacement effect, Mana cost, limitation, and tradeoff, replace the original in the same slot only after explicit confirmation, and leave the original unchanged when declined.

FR108 [P6]: After the first qualifying Rest-spell use, the game shall display the exact G13 clue without a checklist; after the third distinct use and achievement, it shall reveal the exact variant, cost, tradeoff, and replacement choice.

FR109 [P9]: Combat shall begin at 10 m, roll initiative once using d20 + Agility modifier with the specified tiebreakers, use six-second rounds, and on each turn allow movement up to 8 m plus one attack, cast, item use, defend, sprint, escape, or surrender action; sprint shall move up to 34 m.

FR110 [P9]: Attacks shall use G03 natural-roll rules against `10 + Agility modifier + armor bonus`; mappings shall be Body + Melee, Agility + Ranged, and Mind + Arcana; defend shall grant +2 Defense until the actor's next turn; the specified attacks, damage formulas, minimum damage, and Stamina costs shall apply atomically.

FR111 [P9]: The controlled player fixture shall use the exact G23 attributes, pools, skills, equipment, affinity package, and Cinder Lance parameters without altering the live campaign; misses shall spend committed Mana.

FR112 [P9]: The authored road robber shall use the exact G23 statistics, sword damage, surrender behavior, escape threshold, surrender consequences, and one-time purse outcomes.

FR113 [P9]: Meaningful combat checks shall use G18 XP without a separate encounter-completion award; replays or reloads shall not duplicate XP or purse transfer; combat position, order, pools, costs, conditions, and items shall persist through save/load.

FR114 [All stages]: Unsupported player proposals shall become recorded expansion candidates rather than invented successful consequences; source state and proposals shall be preserved for diagnosis.

FR115 [All stages]: Generated spells and reusable rulings shall retain stable identities and mechanics across sessions; intentional revisions shall be explicit and preserve which version governed earlier results.

FR116 [All stages]: Each stage shall enforce its stated content/asset budget and promotion gate; later-stage mechanics shall not become prerequisites of earlier stages.

Total FRs: 116

### Non-Functional Requirements

NFR1 [Platform]: The initial game shall run locally in a desktop browser and use an LLM connection required by the eventual model choice.

NFR2 [Usability]: Normal sessions shall target 20–60 minutes and support easy manual save/resume with no offline progression.

NFR3 [Accessibility]: Text size shall be adjustable from 16–24 px.

NFR4 [Accessibility]: Keyboard focus shall be visible and every control shall be keyboard reachable.

NFR5 [Accessibility]: Speaker attribution shall not depend on color, and reading shall never be timed.

NFR6 [Accessibility]: Every meaningful cue shall have a textual representation; music, audio, illustration, animation, portraits, and sprites shall not be required through P9.

NFR7 [Input performance]: Visible acknowledgement of player input shall occur within 100 ms.

NFR8 [Local performance]: Local menus shall respond within 200 ms.

NFR9 [Persistence performance]: Save and load shall complete within two seconds.

NFR10 [LLM performance]: At least 95% of completed LLM-mediated actions shall complete within ten seconds.

NFR11 [Recoverability]: An LLM-mediated interruption shall become visibly recoverable by 30 seconds; interrupted requests shall preserve committed progress and clearly identify pending work.

NFR12 [Memory]: After the initial scene loads, browser resident memory at the end of the 60-minute endurance run shall be no more than 100 MB above baseline and shall not grow monotonically per action.

NFR13 [Endurance]: The evaluation shall run for 60 wall-clock minutes with approximately 100 representative actions and four active NPCs, while separately recording simulated seconds.

NFR14 [Observability]: The game shall log action latency, model calls and tokens, actual session cost, rejected proposals, duplicate-action attempts, and contradiction repairs.

NFR15 [Reliability]: Rejected, replayed, retried, interrupted, saved, or loaded actions shall not duplicate committed time, resource, reward, item, transfer, or roll mutations.

NFR16 [Consistency]: Game rules shall own mechanical validation, random resolution, and authoritative state; the LLM shall interpret intentions, portray NPCs, judge bounded thematic fit, and narrate without bypassing rule validation.

NFR17 [Determinism]: Captured proposals, seeded dice, and captured starting state shall reproduce mechanical outcomes; identical regenerated prose is not required.

NFR18 [Persistence]: Saves shall durably preserve the complete causal state required by the active stage, including clocks, resources, identity, ownership, access, relationships, beliefs, plans, effects, progression, and versioned rulings.

NFR19 [Information integrity]: Player-facing information shall respect limited character knowledge while test instrumentation can inspect authoritative events, observations, claims, and downstream decisions.

NFR20 [Content consistency]: Authored geography shall remain stable and descriptions shall reflect committed state changes; locations shall never be procedurally generated.

NFR21 [Scope control]: No multiplayer, public-release, market, or scalability capability shall be inferred from the prototype or its endurance test; conditional co-op requires a later explicit design.

NFR22 [Compatibility]: Browser and test-machine specifications shall be recorded with evaluation results.

NFR23 [Cost]: Actual model cost shall be measured during play; acceptable spend and provider shall remain open until evidence and budget decisions exist.

NFR24 [Narrative integrity]: Narration shall agree with committed facts, preserve hidden information where appropriate, and never present uncommitted success as completed state.

NFR25 [Recovery]: Save-index errors and asynchronous/LLM failures shall offer a recoverable path without making New Game unavailable or losing committed progress.

Total NFRs: 25

### Additional Requirements

- Stage sequence is mandatory: E1 → E2 → P0 evidence gate → E3/P1 gate → E4/P2 gate → E5/P3 gate → E6/P4 gate → E7/P5 gate → E8/P6 gate → E9/P7 gate → E10/P8 gate → E11/P9 gate.
- P0 must run three controlled repetitions per gift/no-gift pair and at least one rumor variant with zero unexplained authoritative contradictions or conservation/save failures before promotion.
- Every later stage must exercise its controlled fixture, one failure/recovery path, save/load, and one unplanned but supported approach before promotion.
- The P0 evidence gate must verify conservation and motive-grounded plan changes, the controlled check and XP boundaries, contact-mediated rumor, complete save/load, and separate believability versus mechanical-consistency observations.
- Timing evidence must compare the specified travel modes, 2-word/31-word exchanges, prepared pouch/loose-coin handling, silent/clock/event waits, duplicate protection, and threshold-based progression fixtures.
- P1–P9 must execute the stage-specific evidence suites listed in the GDD Success Metrics, including all explicit success, failure, boundary, persistence, and recovery variants.
- Expansion must stop to investigate unexplained outcomes, irrelevant NPC memory, opaque progression, severe latency, conservation failures, or insufficient desire to return.
- P0 is limited to one settlement, three locations, four named NPCs, one social conflict, one drink item plus gold, one uncertain-check situation, player/Persuasion growth, and gift/no-gift plus rumor variants.
- P1–P9 are constrained by their stated fixture and content budgets. Broad catalogues, procedural geography, formal policing, parties, equipment progression, additional settlements/cast expansion, generated libraries, player-run businesses, and co-op remain excluded through those stages.
- Classes, class roadmaps, code validation of affinity–concept thematic compatibility, and place/domain/innkeeper powers are explicitly removed or deferred.
- P0–P9 use deliberately authored locations. Procedurally generated locations are permanently excluded.
- There is no public persistent multiplayer, public v1.0 commitment, post-launch roadmap, budget, delivery date, staffing commitment, implementation stack, storage technology, model, or provider decision in the GDD.
- Full event sourcing is not mandated. Architecture must select the implementation stack and define how authoritative state, atomicity, persistence, deterministic replay, LLM boundaries, and recovery are realized.
- P1–P9 design assumptions are resolved for staged planning, but measurements may motivate explicit later revisions and stage gates remain binding.

### GDD Completeness Assessment

The GDD is unusually detailed and internally explicit about mechanics, fixtures, boundary ordering, stage gates, persistence, recovery, performance targets, and out-of-scope areas. It is sufficiently complete to trace the authoritative epics against a staged P0–P9 design baseline.

An architecture artifact was later discovered outside the configured planning-artifacts folder. It selects the P0 stack and defines authoritative state, atomicity, persistence, replay, LLM boundaries, and recovery, but it is based on GDD 0.4 and must be reconciled to the 0.6 stage model and current four-epic plan. The GDD also leaves budget, schedule, public-release intent, alternate difficulty modes, and several later breadth decisions open; these are acceptable deferrals unless the implementation plan assumes them.

## Epic Coverage Validation

Authoritative implementation source analyzed completely: `_bmad-output/planning-artifacts/epics.md` (3,225 lines). Its current approved ownership model contains four P0 epics. Its frontmatter and overview identify the revision as `epic-1-draft-awaiting-review`, use GDD 0.4 as source authority, and explicitly exclude conditional P1, P2, and later scope. The current GDD is version 0.6 and defines P0–P9.

### Epic FR Coverage Extracted

The epics document uses its own 50-item delivery-FR namespace. At epic-ownership level it claims:

- Epic 1: entry, Session 0, natural-language lifecycle, player-safe information, saves, branch recovery, unsupported-action evidence, and campaign confirmation.
- Epic 2: checks, time, travel, transactions, growth, attribute allocation, and the P0 debt agreement.
- Epic 3: Mara's feasible-plan change and fact → observation → claim → belief propagation.
- Epic 4: integrated replay, diagnostics, P0 evidence, measurement, and human causal/believability evaluation.
- All 50 delivery FRs have a primary epic owner, but only Epic 1 currently has non-legacy story drafts. Epics 2–4 have approved epic-level ownership without current story decomposition.
- The retained legacy stories are explicitly non-authoritative and therefore are not counted as current story coverage.

### Coverage Matrix

| GDD FR | Requirement | Epic coverage | Status |
| --- | --- | --- | --- |
| FR1 | Title offers New Game and Continue | Epic 1 | ✓ Covered |
| FR2 | Save-aware three-slot Continue states and retry | Epic 1 | ✓ Covered |
| FR3 | Rowan-led zero-time Session 0 questions | Epic 1 | ✓ Covered |
| FR4 | Player authorship, categorized review, corrections | Epic 1 | ✓ Covered |
| FR5 | Atomic confirmation and Market Square opening | Epic 1 | ✓ Covered |
| FR6 | Intent is not authoritative state; routine/reject/social limits | Epic 1 | ✓ Covered |
| FR7 | Pre-commit interpretation, stakes, costs, validation | Epic 1; extended in Epic 2 | ✓ Covered |
| FR8 | Rejection/retry/unchanged-approach mutation protection | Epic 1; extended in Epic 2 | ✓ Covered |
| FR9 | Natural 1/20 and d20 check formula | Epic 2 | ✓ Covered |
| FR10 | Five attributes, fixed standard array, modifier | Epic 1 for array; Epic 2 for checks | ✓ Covered |
| FR11 | Immutable starting array and uncapped growth | Epics 1–2 | ✓ Covered |
| FR12 | Player/skill levels and allocatable growth | Epic 2 | ✓ Covered |
| FR13 | Derived Health, Mana, and Stamina pools | Not found; P1 excluded | Deferred / missing |
| FR14 | Four P1 NPC resource fixtures | Not found; P1 excluded | Deferred / missing |
| FR15 | Base Maximum recalculation and clamps | Not found; P1 excluded | Deferred / missing |
| FR16 | Effective Maximum semantics and bounds | Not found; P1 excluded | Deferred / missing |
| FR17 | Resource-pool save/load verification | Not found; P1 excluded | Deferred / missing |
| FR18 | Mana atomicity and insufficient-Mana rejection | Not found; P1/P6/P9 excluded | Deferred / missing |
| FR19 | Sleep/rest resource recovery | Not found; P1 excluded | Deferred / missing |
| FR20 | Stamina expenditure bands and atomic payment | Not found; P1/P9 excluded | Deferred / missing |
| FR21 | Zero-Stamina restrictions | Not found; P1 excluded | Deferred / missing |
| FR22 | Health, wounds, death, revival, defeat recovery | Not found; P1/P9 excluded | Deferred / missing |
| FR23 | Shared configurable effect schema | Not found; P1 excluded | Deferred / missing |
| FR24 | Effect targets, validation, stable identity | Not found; P1 excluded | Deferred / missing |
| FR25 | Stack/Refresh/Replace effect behavior | Not found; P1 excluded | Deferred / missing |
| FR26 | Effect arithmetic | Not found; P1 excluded | Deferred / missing |
| FR27 | Effect magnitude tiers and budgets | Not found; P1 excluded | Deferred / missing |
| FR28 | Source-bounded tier, target, and duration | Not found; P1 excluded | Deferred / missing |
| FR29 | Effect causal categories and removal | Not found; P1 excluded | Deferred / missing |
| FR30 | P1 effect fixtures and boundary matrix | Not found; P1 excluded | Deferred / missing |
| FR31 | Same-timestamp resolution order | Not found; P1–P3 excluded | Deferred / missing |
| FR32 | Contextual difficulty fixed before roll | Epic 2 | ✓ Covered |
| FR33 | Controlled payment-extension check | Epic 2 | ✓ Covered |
| FR34 | Mastery-preserving difficulty | Epic 2 | ✓ Covered |
| FR35 | Integer-second shared clock and pause rules | Epic 2 | ✓ Covered |
| FR36 | Distance/speed travel and fixture routes | Epic 2 | ✓ Covered |
| FR37 | Dialogue-time formula and completed speech | Epic 2 | ✓ Covered |
| FR38 | Handling estimates, pouch, loose coins | Epic 2 | ✓ Covered |
| FR39 | Campaign epoch and wait targets | Epic 1 for epoch; Epic 2 for waits | ✓ Covered |
| FR40 | Silent/event wait interruption behavior | Epic 2 | ✓ Covered |
| FR41 | Complete NPC constraints and plan inputs | Epic 1 definitions; Epic 3 behavior | ✓ Covered |
| FR42 | Separate facts, observations, claims, beliefs | Epic 3 | ✓ Covered |
| FR43 | Controlled social scenario and rumor variant | Epics 2–3 | ✓ Covered |
| FR44 | Inspectable causal records with player knowledge limits | Epic 3; integrated in Epic 4 | ✓ Covered |
| FR45 | Physical presence and reachability of resources | Not found; P2 excluded | Deferred / missing |
| FR46 | Access modes, door states, bed capacity | Not found; P2 excluded | Deferred / missing |
| FR47 | Unauthorized physiological benefit plus consequences | Not found; P2/P3 excluded | Deferred / missing |
| FR48 | Distinctive and fungible property identity | Not found; P2 excluded | Deferred / missing |
| FR49 | Missing-property belief and uncertain suspicion | Not found; P2 excluded | Deferred / missing |
| FR50 | Ivo's Home access/theft fixtures | Not found; P2 excluded | Deferred / missing |
| FR51 | Access/permission/evidence save-load | Not found; P2 excluded | Deferred / missing |
| FR52 | Meal and adequate-sleep clocks | Not found; P3 excluded | Deferred / missing |
| FR53 | Hunger bands and Starved stacks | Not found; P3 excluded | Deferred / missing |
| FR54 | Sleep bands and Exhausted stacks | Not found; P3 excluded | Deferred / missing |
| FR55 | Adequate/inadequate sleep behavior | Not found; P3 excluded | Deferred / missing |
| FR56 | Exposed behavior and removal | Not found; P3/P5 excluded | Deferred / missing |
| FR57 | Serving and food-definition semantics | Not found; P3 excluded | Deferred / missing |
| FR58 | Food batch expiration | Not found; P3 excluded | Deferred / missing |
| FR59 | Expired-food risk and poisoning | Not found; P3 excluded | Deferred / missing |
| FR60 | Six food fixtures | Not found; P3 excluded | Deferred / missing |
| FR61 | Food preparation validation and timed processing | Not found; P3 excluded | Deferred / missing |
| FR62 | Resource/effect/need status view | Not found; P3 excluded | Deferred / missing |
| FR63 | Shared player/NPC needs and wants-driven planning | Not found; P4 excluded | Deferred / missing |
| FR64 | Physical/off-screen execution and replanning | Not found; P4 excluded | Deferred / missing |
| FR65 | Hunger-plan options and crime constraints | Not found; P4 excluded | Deferred / missing |
| FR66 | Sleep-plan options and constraints | Not found; P4 excluded | Deferred / missing |
| FR67 | Finite job, wage, budget, and demand model | Not found; P4 excluded | Deferred / missing |
| FR68 | Ivo/Tessa autonomous-livelihood fixture | Not found; P4 excluded | Deferred / missing |
| FR69 | Alchemy/Brewing craft lifecycle | Not found; P5 excluded | Deferred / missing |
| FR70 | Persistent poison application and triggers | Not found; P5 excluded | Deferred / missing |
| FR71 | Four craft product tracks | Not found; P5 excluded | Deferred / missing |
| FR72 | P5 tools, recipes, and starting skills | Not found; P5 excluded | Deferred / missing |
| FR73 | Controlled uncertain craft and atomicity | Not found; P5 excluded | Deferred / missing |
| FR74 | Exact 12-recipe G19 catalogue | Not found; P5 excluded | Deferred / missing |
| FR75 | Per-track 10/25 unlock progression | Not found; P5 excluded | Deferred / missing |
| FR76 | P5 starting economy and finite restock | Not found; P5 excluded | Deferred / missing |
| FR77 | Finite need-driven NPC demand | Not found; P5 excluded | Deferred / missing |
| FR78 | Four-household lived-stability victory | Not found; P5 excluded | Deferred / missing |
| FR79 | Ward/patrol/relocation solution costs | Not found; P5 excluded | Deferred / missing |
| FR80 | Ward duration, warnings, expiry, recovery | Not found; P5 excluded | Deferred / missing |
| FR81 | Continued play and mutable stakeholder positions | Not found; P5 excluded | Deferred / missing |
| FR82 | Generic concern/commitment lifecycle | Explicitly deferred in root epics | Deferred / missing |
| FR83 | Three daily quests, refresh, reward, expiry | Not found; P7 excluded | Deferred / missing |
| FR84 | Daily category templates | Not found; P7 excluded | Deferred / missing |
| FR85 | Nine-item tiered gacha pool | Not found; P7 excluded | Deferred / missing |
| FR86 | One private hidden condition per quest | Not found; P8 excluded | Deferred / missing |
| FR87 | Bounded hidden rewards and exact notice | Not found; P8 excluded | Deferred / missing |
| FR88 | Free text without action suggestions | Epic 1; shared by later P0 epics | ✓ Covered |
| FR89 | Composer keys, keyboard access, neutral errors | Epic 1 | ✓ Covered |
| FR90 | Intent-preserving clarification and multi-action limits | Epic 1; extended in Epic 2 | ✓ Covered |
| FR91 | Synonym interpretation without arbitrary-mechanics promise | Epic 1 | ✓ Covered |
| FR92 | Authored stable locations across all stages | P0 locations in Epics 1–2; later additions absent | ◐ Partial |
| FR93 | Description-length rules across staged locations/actions | P0 behavior in Epics 1–2; later applications absent | ◐ Partial |
| FR94 | Inventory identity plus later prize/achievement persistence | P0 inventory in Epic 1; later reward behavior absent | ◐ Partial |
| FR95 | Known-information journal across staged concerns | P0 journal in Epic 1; later commitment/quest use absent | ◐ Partial |
| FR96 | Distinct narrator/NPC/System/award/mechanics voices | P0 voices in Epic 1; System/award explicitly excluded | ◐ Partial |
| FR97 | 20–60-minute session target | Epic 1 UX contract; Epic 4 measurement | ✓ Covered |
| FR98 | Complete three-slot manual persistence | Epic 1 | ✓ Covered |
| FR99 | Deterministic mechanical replay and branch isolation | Epic 4, with incremental evidence in Epics 1–3 | ✓ Covered |
| FR100 | Universal skills through P9 | P0 Persuasion/basic framework in Epics 1–2; later skill mappings absent | ◐ Partial |
| FR101 | Two P6 affinity packages | Not found; P6 excluded | Deferred / missing |
| FR102 | Rest-stone rarity, capacity, fixed selection | Not found; P6 excluded | Deferred / missing |
| FR103 | Stable generated spell presentation with fixed mechanics | Not found; P6 excluded | Deferred / missing |
| FR104 | Three-use Rest-spell evolution eligibility | Not found; P6 excluded | Deferred / missing |
| FR105 | Achievement and Copper Sandglass | Not found; P6 excluded | Deferred / missing |
| FR106 | Brackenford's Anchor title | Not found; P6 excluded | Deferred / missing |
| FR107 | Exact Deepened replacements and confirmation | Not found; P6 excluded | Deferred / missing |
| FR108 | Rest evolution clue and reveal | Not found; P6 excluded | Deferred / missing |
| FR109 | Combat initiative, turns, movement, actions | Not found; P9 excluded | Deferred / missing |
| FR110 | Combat attacks, Defense, damage, and Stamina | Not found; P9 excluded | Deferred / missing |
| FR111 | Controlled P9 player fixture and Cinder Lance | Not found; P9 excluded | Deferred / missing |
| FR112 | Authored robber, surrender, escape, purse | Not found; P9 excluded | Deferred / missing |
| FR113 | Combat XP, exact-once rewards, persistence | Not found; P9 excluded | Deferred / missing |
| FR114 | Expansion-candidate recording across all stages | P0 in Epic 1; later-stage application absent | ◐ Partial |
| FR115 | Stable versioned generated definitions/rulings | P0 content/proposal versioning in Epics 1 and 4; later generated systems absent | ◐ Partial |
| FR116 | Stage budgets and promotion gates | P0 exclusion guardrails exist; no P1–P9 implementation plan | ◐ Partial |

### Missing Requirements

#### Critical readiness gap: stale planning baseline

The authoritative epics document still declares GDD 0.4 as its source and describes G01–G02 and other later mechanics under an obsolete stage model. GDD 0.6 moves effects/resources, access/ownership, survival, and livelihoods into P1–P4 and community/alchemy through combat into P5–P9. Before any scope beyond P0 is authorized, the authoritative epics must be refreshed against GDD 0.6.

Impact: requirements can be assigned to the wrong gate, obsolete “proposed” dispositions can override approved 0.6 decisions, and cross-stage dependencies can be omitted.

Recommendation: retain the approved P0 ownership where still valid, reconcile every P0 statement against 0.6, and add phase-specific epics/stories only when each gate is promoted.

#### Deferred requirements not covered by the authoritative implementation plan

- P1: FR13–FR31 — derived resources, effects, recovery, Stamina, death, effect boundaries, and timestamp ordering.
- P2: FR45–FR51 — local access, doors, permission, ownership/evidence, theft, and persistence.
- P3: FR52–FR62 — hunger, sleep, shelter, food production/spoilage, conditions, and status presentation.
- P4: FR63–FR68 — wants-driven planning, off-screen execution, jobs, finite economies, and the Ivo/Tessa fixture.
- P5: FR69–FR82 — crafting/alchemy, community victory, ward/protection routes, finite demand, and commitment lifecycle.
- P6: FR101–FR108 — affinity packages, awakening, recognition, achievement/title separation, and Deepened spells.
- P7: FR83–FR85 — daily quest slots, categories, refresh/expiry, XP, and gacha.
- P8: FR86–FR87 — hidden condition records and bounded surprise rewards.
- P9: FR109–FR113 — the bounded combat proof.

These are not active P0 blockers because the epics explicitly scope implementation to P0 and the GDD forbids early implementation. They are blockers to claiming readiness for any later phase.

#### Partially covered cross-stage requirements

FR92–FR96, FR100, and FR114–FR116 have a valid P0 implementation path but require explicit extension when later stages are promoted. Their P0 portions count as covered for active-scope readiness; they do not establish full-roadmap coverage.

#### Epic-only requirements

The root epics include implementation details sourced from architecture and UX—30 AR requirements and 40 UX requirements—rather than unsupported gameplay scope. No clearly orphaned gameplay requirement was identified at epic-ownership level. Their correctness against architecture and UX is assessed in later workflow steps.

### Coverage Statistics

- Total GDD FRs: 116
- Fully covered across their complete stated stage range: 32
- Partially covered cross-stage FRs: 9
- Entirely deferred/not present in the authoritative implementation epics: 75
- Full-roadmap complete coverage: 27.6%
- Full-roadmap coverage including partial rows: 35.3%
- Active P0 FR groups with a planned epic path: 41 of 41 (100%)
- Current non-legacy story decomposition: Epic 1 only; Epics 2–4 remain at approved epic-ownership level

Epic-level P0 coverage is complete. This does not imply story completeness, test adequacy, source freshness, architecture alignment, or overall implementation readiness.

## UX Alignment Assessment

### UX Document Status

Found and read completely:

- `ux-designs/ux-dmud-2026-09-08/DESIGN.md` — final, P0 scope, 222 lines.
- `ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md` — final, P0 scope, 213 lines.
- Architecture support source: `_bmad-output/game-architecture.md` — version 1.1, complete, 1,840 lines.

The initial architecture warning is corrected: architecture exists, but it is stored directly under `_bmad-output/` rather than `_bmad-output/planning-artifacts/`.

### Confirmed P0 Alignment

- UX and GDD agree on a local desktop-browser, text-first, solo experience for 20–60-minute sessions.
- Title, Session 0, three-slot save selection, Main Notebook, Journal, Inventory, Character Sheet, and result details cover the P0 player journey.
- The one free-text composer, Enter/Shift+Enter behavior, no suggested actions, neutral clarification, factual linked exits, and zero-time reference surfaces match GDD input rules.
- UX consistently distinguishes player intention, Rowan, narration, NPC speech, mechanics, pending status, and failures, and prevents presentation from claiming uncommitted success.
- Player-knowledge boundaries, absence of an omniscient roster, exact submitted-intention echo, and fact-only journal behavior support the GDD's fact/observation/belief separation.
- Save/load, interruption, pre/post-commit recovery, no duplicated mutations, and missing/corrupt result evidence all have explicit UX states.
- DESIGN and EXPERIENCE provide a coherent notebook visual system, shared overlay behavior, responsive layout, reduced motion, keyboard operation, screen-reader semantics, contrast targets, 200% zoom, and 320 CSS px reflow.
- Architecture directly supports these P0 needs through React semantic UI, a generated validated API contract, subject-aware persisted operations, TanStack Query server state, presentation-only local state, player-safe projections, the shared dialog shell, status announcements, and real-browser accessibility verification.
- Architecture explicitly corrects the UX persona ambiguity by declaring that all normative views use the player-selected name.

### Alignment Issues

#### UX ↔ GDD

1. **Stale source and phase model — high.** Both UX files were finalized on 2026-09-08 and describe the older E1–E6/P0–P2 model. GDD 0.6 now defines P0–P9 with resources/effects, access/ownership, needs, livelihoods, community/alchemy, recognition, daily quests, hidden bonuses, and combat in distinct gated stages.

2. **Persona used normatively — medium.** DESIGN and EXPERIENCE repeatedly label persistent UI content as “James's” intentions/card/stats. GDD 0.6 states that James is only an example persona and the player supplies the character name. Architecture resolves the intended implementation, but the authoritative UX wording remains internally misleading.

3. **Resolved character rules still listed as open — high.** EXPERIENCE says the exact standard-array values and final attribute vocabulary remain open, and its `stat-assignment` contract repeats that statement. GDD 0.6 has approved Body, Agility, Constitution, Mind, Presence and the exact 8/10/12/13/14 array.

4. **Text adjustment requirement absent — high.** GDD G15 requires adjustable 16–24 px text. UX specifies fixed type tokens and relies on browser zoom, explicitly declining a Settings surface merely for zoom. Browser zoom supports accessibility but does not implement the GDD's adjustable 16–24 px preference.

5. **Performance status stale — medium.** EXPERIENCE calls latency numbers proposed targets. GDD 0.6 calls G16's responsiveness and recovery targets approved evaluation targets and adds an explicit memory ceiling/growth condition.

6. **Later-stage journeys absent by design — deferred.** P1–P9 status, effect inspection, access, survival, crafting, affinity/upgrade, daily quest/gacha, hidden reward, and combat flows have no current promoted UX contract. Deferred `system-notice` and `award-notice` treatments are useful guardrails but are insufficient for those full journeys.

#### UX ↔ Architecture

1. **Strong P0 support.** Every current P0 surface/component has an architecture owner, transport/query contract, authoritative-state boundary, persistence/recovery behavior, and accessibility verification approach.

2. **Framework selection wording is stale — low.** EXPERIENCE says no UI framework or storage technology has been selected; Architecture 1.1 selects React, FastAPI, SQLite, OpenAPI generation, TanStack Query, and Zod. This does not create a behavior conflict but should be reconciled to prevent implementer uncertainty.

3. **Text-size implementation is optional in architecture — high.** Architecture includes presentation preference storage and a `preferences/` feature, but explicitly calls a separate in-game text-size control optional. That does not guarantee the GDD's required adjustable 16–24 px behavior.

4. **Memory acceptance is missing — high.** Architecture says no memory ceiling is specified and only recommends measuring growth. GDD 0.6 now requires end-of-run resident memory no more than 100 MB above baseline and no monotonic per-action growth.

5. **Architecture stage map is obsolete — high for post-P0.** Architecture 1.1 maps community/alchemy/affinities/daily quests to P1 and hidden objectives to P2. It has no promoted design for the current P1 effects/resources, P2 access, P3 needs, P4 livelihoods, or P9 combat boundaries. Its conditional slice list therefore cannot support current GDD stage promotion without revision.

6. **Dependency versions require fresh verification — medium.** Architecture correctly warns that its September 2026 version checks were not repeated during the 1.1 reconciliation. Exact versions and compatibility must be verified at scaffolding; the readiness assessment does not treat historical version tables as executable proof.

### Warnings

- P0 UX is complete enough to plan once the stale-source conflicts are corrected, but only Epic 1 has current non-legacy story decomposition.
- No P1–P9 implementation should begin until a phase-specific UX update promotes that stage's end-to-end journeys, components, states, recovery, and accessibility behavior.
- Update UX and architecture source/version declarations to GDD 0.6 before treating their “final” or “complete” statuses as current readiness evidence.
- Replace normative “James” labels with player/player-character or an explicit runtime-selected-name token; retain James only in clearly marked examples.
- Make the 16–24 px text preference a required, persisted, accessible behavior or explicitly amend GDD G15.
- Add the GDD 0.6 memory requirement to architecture, measurement stories, and acceptance evidence.

## Epic Quality Review

Review scope: the current approved four-epic structure and the 15 non-legacy Epic 1 story drafts. The retained legacy five-epic/22-story section is explicitly non-authoritative and was not credited as current implementation planning.

### Epic Structure Validation

| Epic | User-value focus | Dependency direction | Current story readiness |
| --- | --- | --- | --- |
| Epic 1 — Create and Resume a Personal Campaign | Pass: a player can create, inspect, save, and resume a campaign | Pass: no prior epic required | 15 drafts; none approved |
| Epic 2 — Explore, Transact, and Grow in Brackenford | Pass: playable movement, transactions, checks, and progression | Pass: requires only Epic 1 | No current stories |
| Epic 3 — See Consequences Travel Through People | Pass: the player experiences grounded agency and rumor propagation | Pass: requires only Epics 1–2 | No current stories |
| Epic 4 — Evaluate the P0 World That Remembers | Pass: the prototype owner can make an evidence-backed scope decision | Pass: requires only Epics 1–3 | No current stories |

No technical-only epic, circular dependency, or forward epic dependency was found. Each epic describes an observable player or prototype-owner outcome, and each builds only on earlier delivery.

### Story Dependency Map

The explicit Epic 1 dependency graph is backward-only:

- 1.1: none
- 1.2: 1.1
- 1.3: 1.1, 1.2
- 1.4: 1.3
- 1.5: 1.4
- 1.6: 1.3
- 1.7: 1.2, 1.4, 1.6
- 1.8: 1.2, 1.4, 1.5, 1.7
- 1.9: 1.8
- 1.10: 1.4, 1.5, 1.8, 1.9
- 1.11: 1.7, 1.10
- 1.12: 1.9, 1.10, 1.11
- 1.13: 1.10, 1.11, 1.12
- 1.14: 1.4, 1.8, 1.9, 1.12, 1.13
- 1.15: 1.14

No explicit story depends on a higher-numbered future story. The document also states that schemas and migrations are introduced by the story that first uses them, avoiding speculative up-front domain modeling.

### 🔴 Critical Violations

#### Q1 — Current story decomposition is incomplete

Only Epic 1 has current story drafts. Epics 2–4 have epic-level ownership and completion boundaries but no current stories or acceptance criteria. The legacy stories cannot fill this gap because the document explicitly forbids using them as current implementation instructions.

Evidence: frontmatter reports `revisionStatus: epic-1-draft-awaiting-review`, `currentStoryEpic: 1`, `draftStoryCounts: {1: 15}`, and `storyEpicsApproved: []`.

Impact: most P0 gameplay—time, travel, transactions, checks, progression, causal NPC behavior, replay, diagnostics, and evaluation—has no approved, independently deliverable implementation path.

Remediation: review/approve or revise Epic 1, then decompose Epics 2–4 into current stories with backward-only dependencies, single-outcome boundaries, requirement ownership, and testable acceptance criteria.

#### Q2 — No story batch is approved

Even Epic 1 remains a draft awaiting review and the approved-story list is empty.

Impact: implementation would begin from unapproved story content despite the plan's own checkpoint rules.

Remediation: complete the explicit Epic 1 review checkpoint and record approval or revisions before development.

#### Q3 — Required ordinary starting gold is unresolved

The plan records `openContentDecisions: [ordinary-p0-starting-gold]`. Stories 1.2 and 1.8 state that normal-campaign content cannot be implementation-ready until the value is supplied, and correctly prohibit substituting the controlled 10,000-gold test fixture.

Impact: the authored P0 content package and atomic initial campaign state cannot be finalized; Story 1.3 also depends on 1.2, creating a broader delivery bottleneck.

Remediation: record the ordinary New Game starting gold in the authoritative GDD/content decision source, update the content package requirement, and remove the open decision from epics frontmatter.

#### Q4 — Architecture and current epic namespaces conflict

Architecture 1.1 repeatedly maps “current implementation Epics 1–5,” while the authoritative epics revision approves four epics and explicitly treats the five-epic section as legacy.

Impact: architecture verification references and ownership assignments point at obsolete epic/story IDs, weakening traceability and inviting work to be implemented under the wrong boundary.

Remediation: update architecture's requirement-to-verification map and all epic/story references to the authoritative four-epic structure after story decomposition stabilizes.

### 🟠 Major Issues

#### Q5 — Story 1.1 combines too many independent outcomes

It combines project scaffolding, runtime/SQLite compatibility, Title behavior, draft creation, API generation, semantic visual tokens, accessibility checks, and six independent CI gates.

Impact: failure and review ownership span unrelated concerns; the story is difficult to implement and verify in one developer context.

Remediation: keep one thin runnable Title/New Game slice, but separate repository/quality-baseline proof from durable draft creation if both cannot be reviewed together. Preserve the first usable browser outcome in the earliest slice.

#### Q6 — Story 1.3 is epic-sized

It includes the complete Session 0 questioning behavior, reusable persisted operation worker, provider contract validation, SSE/status transport, draft persistence, concurrency/idempotency, pre/post-commit failure handling, UI states, accessibility, and telemetry.

Impact: too many independent failure modes and architectural boundaries land together, making red-green iteration and acceptance ownership unwieldy.

Remediation: split the durable answer command/result from streamed progress/recovery presentation and from telemetry/accessibility integration, while ensuring each slice produces a usable player-visible result and no temporary alternate worker is introduced.

#### Q7 — Story 1.8 mixes campaign commit and post-commit opening presentation

Atomic origin/branch creation, concurrent confirmation, full initial-state instantiation, personalized opening narration, and pre/post-commit recovery are independently demonstrable outcomes.

Impact: a mechanically correct confirmation cannot be reviewed independently from provider-backed opening narration and its failure modes.

Remediation: separate atomic confirmation/initial branch creation from personalized opening presentation recovery, with the latter consuming only the earlier committed result.

#### Q8 — Story 1.9 bundles three distinct reference features

Character, Inventory, and Journal queries/states share one story alongside the reusable dialog shell and full accessibility behavior.

Impact: three independent projections and failure boundaries obscure ownership and increase review size.

Remediation: introduce the shared overlay with one reference view, then add the other projections as separate player-valued increments. Journal may remain a notebook surface rather than an overlay, as the UX contract specifies.

#### Q9 — Story 1.13 mixes player recovery with developer diagnostics

Honest unsupported-intention rejection is a player outcome; durable expansion-candidate classification and the capability-gated developer query serve a different user and security boundary.

Impact: the player-facing behavior depends on a development-only diagnostic facility and creates mixed-persona acceptance criteria.

Remediation: keep rejection plus durable candidate creation with the player action if atomicity requires it, but move developer inspection/query UI to the later diagnostics story; verify only persisted linkage and redaction here.

#### Q10 — Save/load stories are very broad

Stories 1.14 and 1.15 each combine slot UX, complete snapshots, revision conflicts, integrity/version validation, error recovery, idempotency, accessibility, measurement, and real-database/browser evidence; load additionally includes migrations, branch isolation, cache invalidation, and late SSE suppression.

Impact: each story has several independently failing completion outcomes and may exceed a single implementation/review context.

Remediation: preserve Save and Load as separate user outcomes, then split reusable snapshot/integrity infrastructure from slot interaction only if each slice remains end-to-end demonstrable. At minimum, extract historical migration support until a real prior schema exists; the current AC already warns against inventing one.

#### Q11 — Story 1.2 is primarily an enabling technical outcome

The prototype-owner story validates a complete content registry but delivers no direct player behavior until later confirmation.

Impact: it is close to a technical milestone and its unresolved starting-gold input blocks unrelated Session 0 conversation work through Story 1.3's dependency.

Remediation: frame its demonstrable outcome as “New Game refuses incoherent content and preserves existing data,” minimize the package to content needed by the next player slice, and reconsider whether Story 1.3 truly needs the complete world package rather than only versioned Session 0 definitions.

#### Q12 — Acceptance criteria are frequently compound

The Given/When/Then structure is consistently present and generally specific, but many ACs assert UI behavior, API semantics, persistence, accessibility, logging, concurrency, and testing strategy in one criterion, with D1–D6 adding further obligations.

Impact: one AC can fail for several unrelated reasons and cannot always map cleanly to one behavior-focused test or manual check.

Remediation: split ACs by observable behavior and assign shared Definition-of-Done clauses only where applicable. Keep infrastructure/test-method requirements in the evidence ledger rather than repeating them as part of a player behavior criterion.

### 🟡 Minor Concerns

- The story prose sometimes uses “safe,” “appropriate,” “coherent,” or “personally relevant” without a local definition. Most are later grounded by concrete clauses, but remaining uses should point to an explicit schema, source section, or observable rule.
- Story 1.1 defers populated Continue behavior to Story 1.15. Its no-save/error states still make 1.1 usable, but the story title and summary should avoid implying full Continue behavior before 1.15.
- Story 1.14 asks for performance measurement while the current epics/architecture still treat targets as provisional; GDD 0.6 now treats them as approved evaluation targets. Normalize the authority language during source refresh.
- Story and architecture references use multiple namespaces (GDD G IDs, report FR IDs, delivery FR IDs, current four epics, legacy five epics). The document explains this, but downstream artifacts should link by stable source ID plus current story ID to reduce mistakes.

### Best-Practices Compliance Checklist

| Check | Result | Notes |
| --- | --- | --- |
| Epics deliver player/user value | Pass | All four deliver a player or prototype-owner outcome |
| Epic dependency direction | Pass | Strict forward delivery order; no circular or future dependency |
| Stories appropriately sized | Fail | Several Epic 1 stories combine multiple independently reviewable outcomes |
| No forward story dependencies | Pass | All explicit `Requires` references point backward |
| Data structures created when first needed | Pass with caution | Explicit D3 rule is sound; Story 1.1/1.2 breadth should be reduced |
| Clear BDD acceptance criteria | Pass with concern | Consistent Given/When/Then, but often compound |
| Traceability maintained | Fail | Stale GDD 0.4 source and architecture's obsolete five-epic map |
| Starter requirement covered | Pass | Story 1.1 uses the selected create-vite/uv baseline and early quality gates |
| Greenfield pipeline established early | Pass | Environment, lockfiles, API generation, CI, integration, and browser gates start in 1.1 |
| Complete P0 story plan | Fail | Epics 2–4 have no current stories; no story batch is approved |

### Quality Review Recommendation

Do not begin implementation from the current plan. First resolve ordinary starting gold, refresh sources and epic references to GDD 0.6, finish and approve the current story decomposition for all four P0 epics, and resize the largest Epic 1 stories while preserving end-to-end user value and the existing backward-only dependency graph.

## Summary and Recommendations

### Overall Readiness Status

**NOT READY**

The P0 design foundation is strong: the current GDD is detailed, all active P0 requirement groups have an epic-level owner, the four epic boundaries deliver user value, explicit dependencies point backward, and the UX/architecture pair gives P0 a coherent interaction and technical model.

Those strengths do not yet constitute an implementable plan. The authoritative epics are a work-in-progress based on GDD 0.4; only Epic 1 has draft stories; no story batch is approved; an initial-state content decision is unresolved; Architecture 1.1 points to an obsolete five-epic map; and UX/architecture omit or contradict current 0.6 requirements. Starting implementation now would bypass the plan's own approval gates and create avoidable source-of-truth conflicts.

### Critical Issues Requiring Immediate Action

1. **Resolve ordinary P0 starting gold.** It blocks final authored content and atomic campaign creation. The 10,000-gold pouch remains a controlled test fixture and must not be used as the ordinary balance.
2. **Refresh all planning artifacts to GDD 0.6.** Epics, UX, and architecture still declare GDD 0.4 or the earlier E1–E6/P0–P2 stage model.
3. **Complete and approve P0 story decomposition.** Only Epic 1 has drafts, `storyEpicsApproved` is empty, and Epics 2–4 have no current stories.
4. **Synchronize architecture to the authoritative four-epic plan.** Remove obsolete “current Epics 1–5” mappings and rebuild the verification crosswalk after story IDs stabilize.
5. **Close current P0 UX/architecture contradictions.** Replace normative “James” labels, remove resolved attribute/array open items, require the 16–24 px text preference, and add GDD 0.6 memory acceptance criteria.
6. **Resize oversized Epic 1 stories.** Stories 1.1, 1.3, 1.8, 1.9, 1.13, 1.14, and 1.15 need smaller independently demonstrable boundaries or a documented proof that each fits one implementation/review context.

### Recommended Next Steps

1. Record the ordinary P0 starting-gold decision in the authoritative GDD decision log/content source and update Stories 1.2 and 1.8.
2. Reconcile the root epics requirements inventory and scope disposition against GDD 0.6, retaining P0-only implementation scope and marking P1–P9 as gated rather than using obsolete P1/P2 labels.
3. Revise and approve the 15 Epic 1 stories, splitting compound stories and ACs while preserving their real-browser, real-API, atomicity, persistence, and accessibility outcomes.
4. Create and approve current stories for Epics 2–4 with explicit backward-only `Requires`, stable requirement ownership, error/recovery criteria, and feature-owned persistence/replay evidence.
5. Update Architecture 1.1 to a new revision that references GDD 0.6 and the final four-epic/current-story map; add the required text-size and memory contracts and the current P1–P9 conditional slice boundaries.
6. Update DESIGN/EXPERIENCE to use the player-selected name normatively, remove resolved open items, adopt current stage labels, and promote only P0 flows. Keep P1–P9 UX deferred until each phase is explicitly promoted.
7. Rerun implementation readiness after those artifacts are internally consistent. Only then begin the first approved implementation story.

### Deferred Roadmap Guidance

The 75 entirely uncovered later-stage FRs and nine partially covered cross-stage FRs are not P0 blockers. They are intentional deferrals under the GDD's stage gates. Do not expand the current P0 stories to absorb them. Before promoting any later stage, create a phase-specific architecture, UX contract, epics/stories, and evidence plan for that stage.

### Final Note

This assessment documents 31 issue groups across epic coverage, UX/architecture alignment, and epic/story quality. The blocking findings are planning and source-alignment defects, not evidence that the core game concept is unsound. Address the critical items before implementation; proceeding as-is would knowingly accept incomplete story coverage and conflicting authoritative artifacts.

**Assessment date:** 2026-09-15  
**Assessor:** Codex, acting as Game Producer and Scrum Master for implementation-readiness review
