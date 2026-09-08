# dmud GDD Decision Log

## 2026-09-07 — Draft creation

- User requested a GDD from the approved brief, addendum, and decision log, preserving accepted decisions, keeping the initial prototype small, and drafting explicit assumptions for correction.
- Status: drafting; new design proposals are not user-approved decisions.
- Source workspace: `../../briefs/brief-dmud-2026-09-05/`. Original sources remain unchanged.

## Source precedence and accepted-decision audit

References are relative to the source workspace above. IDs C01–C15 are this GDD's reconciliation IDs, not invented source decision numbers. Source A1–A9 are accepted working defaults; exact provisional details and later proposals remain unapproved.

| ID | Accepted decision / source locator | Carried into draft |
| --- | --- | --- |
| C01 | Free intentions, engine authority, NPC agency, fallible knowledge, generative history; brief §§Vision/Pillars; source log lines 6, 32 | Executive Summary; pillars; intent, NPC, and progression rules |
| C02 | Solo personal prototype; friends; later conditional co-op/public release; log lines 16–18 | Audience; stage gates; Out of Scope |
| C03 | A1–A9 working defaults accepted; not final parameter approval; log lines 46–56; addendum lines 218–232 | Draft status; assumption index; no approval claim |
| C04 | Brackenford, viable community future with multiple supported solutions and continued play; addendum lines 57–65 | Core Gameplay; G01–G02 proposed thresholds; E3 |
| C05 | Browser/local, shared action clock, no offline progression, custom d20, recoverable defeat/manual saves; brief §§Rules/Scope; addendum lines 168–178 | Platform; G03–G04/G08 proposed details; E1 |
| C06 | Exactly three locations/four NPCs/one conflict; gift, contact, check, persistence proof; addendum lines 182–196; log line 51 | P0; G05 fixture; E1–E2; evidence checks |
| C07 | Conditional compact community/stall/magic/evolution/achievement slice; addendum lines 198–206 | P1; E3–E4; extra progression-test details remain G assumptions |
| C08 | Wealth-gift agency, full trees-to-bar economy, social rumor network, broad generated content preserved as vision; log lines 7, 21, 33; addendum lines 11–25 | NPC mechanics; Simulation; scope deferrals; epic deferred-work register |
| C09 | Choose discovered affinities; substantially random quality-linked rarity; meaningful limited powers; log lines 47–49 | RPG and progression; exact pools/odds remain G09/G11 proposals |
| C10 | Stone concept through one owning affinity; per-affinity capacity; whole-set context; uncertain outcome; awakening separate from evolution; log lines 60–68 | RPG; G11 experiment; E4 |
| C11 | NO CLASSES; supersedes prior class evolution/generated-class roadmap; log lines 72, 77, 81 | Character system; Out of Scope; E4 |
| C12 | Place/domain/innkeeper powers deferred, no automatic revisit; ordinary businesses retained; log lines 73, 78, 80 | Simulation; Out of Scope; E3 |
| C13 | LLM solely judges thematic fit; code validates mechanical constraints only; log lines 74, 79, 81 | Progression; E4; explicit exclusion of thematic code gates |
| C14 | Universal basic skills; different proficiency; 18-category starting vocabulary; no affinity/award access gates; log lines 75, 78, 80 | RPG basic skills; P0 only exercises one check |
| C15 | Titles give buffs, achievements give item prizes; either may independently gate optional future upgrade; award never auto-upgrades; log lines 85–90 | Progression; G12 experiment; E4 |

### Historical wording deliberately not revived

- Earlier class systems and professional-class evolution are superseded, not open design questions.
- The prior guaranteed Banked Flame → Shelter's Heart stone-upgrade example is rejected; awakening outcome remains uncertain and separate from evolution.
- Engine affinity–concept compatibility validators are rejected. Mechanical support checks cannot claim to certify theme.
- Generic merged title/achievement rewards are superseded by distinct buff/item roles.
- Historical “unaccepted” default statuses do not override the later acceptance of working defaults. Later `[PROPOSAL]` blocks are not covered retroactively by that acceptance.

## 2026-09-07 — Draft design choices, not accepted decisions

- Primary game type classified provisionally as canonical `text-based`, with `rpg` and `simulation` secondary genres. Free-text/MUD presentation leads; both secondary genre sections are included so important systems are not omitted by a low-complexity primary label.
- User requested explicit assumptions, so a complete express draft was created without another discovery/confirmation gate. This overrides the skill's default conversational assumption policy for this run.
- G01–G17 index every new design package. Priority for correction: P0 G03–G08; presentation/evaluation G15–G17; conditional P1 G01–G02/G09–G14 later.
- G09 proposes two affinities rather than the source's explicitly provisional three. This is a visible size proposal, not a change to an accepted fixed count.
- G11 selects player-chosen recipient affinity as a proposal; the source's joint affinity/ability roll remains a legitimate alternative, not a rejected design.
- P0 tests P-A/P-B/P-C only. P-D waits for P1, preserving the accepted staging.
- Genre guide flags dedicated narrative design; offer it after correction, without invoking it or writing a separate handoff artifact.

## Deferred details and phase implications

| Item | Current disposition |
| --- | --- |
| P0 check/time/scenario/interface/save assumptions | Explicit review targets; complete provisional defaults supplied, not approved |
| P1 victory populations, route costs, and protection contracts | Required before P1 implementation; not needed to draft or evaluate P0 |
| P1 package effects, candidate costs/ranges/durations, rarity budgets, variant/reward details | Required before E4 implementation; bounded experiment only |
| P1 alchemy thresholds, effect values, ingredient economy, NPC-need design | Required before E3/E5 implementation; G19 proposals are explicit, not approved |
| P1 daily quest categories, gacha pool contents | Required before E5 implementation; G20 proposals are explicit; System framing now accepted direction |
| P2 hidden bonus reward budget (XP range, item ceiling, gacha-draw eligibility), bonus storage/retrieval model, System notification style | Required before E6 implementation; G21 is proposed, not approved |
| Mana-restoration potion track | Deferred; requires declared affinity per-use cost system |
| Full attributes/training, replacement/respec, hidden unlock system, mature title stacking/rarity | Deferred until wider progression warrants them |
| Content boundaries, model/provider, cost ceiling, budget/time allocation | Unset; do not infer commitments; technical choices belong to architecture |
| Public v1.0/post-launch, construction breadth, additional settlement, co-op | Conditional future scoping; no scheduled epics |
| Place-based powers | Explicitly deferred without promise to revisit |

Original brief artifacts remain unchanged. This log captures the source audit for Kyle to correct asynchronously; it does not claim a user review or approval occurred.

## Source A1–A9 mapping

All rows are accepted working defaults from addendum lines 222–232, with later overrides applied. This table does not approve provisional values.

| Source ID | Working default | GDD location |
| --- | --- | --- |
| A1 | Adult tabletop/LitRPG audience; 20–60-minute sessions | Executive Summary; Game Flow |
| A2 | Desktop browser, local execution, one developer with AI help | Executive Summary; Technical Specifications |
| A3 | Action game time; offline pause | P0 Actions and Time |
| A4 | Brackenford, failing ward, several viable-community routes | Core Gameplay; E3 summary |
| A5 | Custom d20, four provisional attributes, recoverable defeat, manual saves | Intent/Uncertainty; G03/G08 |
| A6 | Engine validates and commits every persistent consequence | Intent/Uncertainty; NPC facts/beliefs |
| A7 | Limited affinity combinations, practice-shaped powers, universal skills; expanded rarity/stones/prerequisites; classes removed | RPG; Progression and Balance |
| A8 | Grounded NPCs, comic achievements, continued play after victory | Narrative and Writing; Win/Loss |
| A9 | Four-NPC causal proof before broader playable slice | Stage gates; E1–E4 |

## 2026-09-07 — Source reconciliation corrections

- Independent brief, addendum, and decision-log comparisons preserved accepted vision and the tiny P0 boundary.
- Clarified G11 so both candidates use the selected owning affinity; the draw remains uncertain within the four-candidate total budget.
- Clarified G11 rarity as the stone's recorded acquisition/setup rarity affecting awakening. Affinity-discovery rarity stays a distinct accepted concept, with its experiment deferred.
- Added stable generated-definition/ruling identities and explicit recorded revisions at design level, without prescribing architecture.
- Made pre-roll consequence definition explicit while retaining validated contextual consequences after resolution.

## 2026-09-07 — Draft 0.1 review status

- Version transition: skeleton/drafting → **0.1 draft-for-correction**. The requested draft is complete; accepted-design approval and production readiness are not claimed.
- Decision audit and three source reconciliation passes completed. Validator passed the 18 checklist items for this assumption-based draft after the awakening clarification; no separate validation report was created.
- P0 correction priorities and P1 implementation dependencies remain explicit in the GDD. No unresolved conflict requires stopping draft delivery.
- Mechanical document checks: all 17 inline assumptions match the index; artifact links resolve; template placeholders removed; epic IDs/titles/sequence agree.
- No external handoffs or completion hooks are configured. Original inputs were not edited and no downstream workflow was run.
- Next step from the installed help catalog: correct this draft first. Dedicated narrative design (`gds-create-narrative`, ND) is offered afterward for voices, room copy, and lore; Kyle has not selected it. Game architecture (`gds-game-architecture`, GA) follows when the intended P0 design is sufficiently settled, in a fresh context. Detailed stories follow architecture. Neither requires promoting P1 into the first implementation.
- Final parallel prose polish completed for GDD and epics without design changes; artifact checks repeated successfully afterward.

## 2026-09-07 — Kyle's G03–G08 corrections; draft 0.2

This entry supersedes conflicting 0.1 proposals/status statements above. Historical entries remain a record of what the earlier draft proposed, not current rules. The original brief/addendum are unchanged; the latest user corrections take precedence.

| ID | Accepted correction | Applied locations |
| --- | --- | --- |
| U01 / G03 | Natural 1 automatically fails; natural 20 automatically succeeds. No attribute or skill-bonus cap; extended play should feel godly/overpowered | GDD uncertainty, character/progression, evidence; E1 |
| U02 / G03 | LLM sets difficulty to control effective success probability; lower probability yields higher XP; a check failing only on 1 gives no XP | GDD uncertainty and Player/Skill Levels; E1.3/E1.5 |
| U03 / G03 | Player levels award allocatable attribute points; skill levels increase bonuses | GDD growth/save rules; E1.4/E1.5; removes G09 no-level/XP clause |
| U04 / G04 | Seconds as base time; free inspection/inventory/known journal/save; contextual movement speed/distance, rendered dialogue, handling and event/clock-based waiting | GDD P0 action rules/table/trial details; E1 |
| U05 / G05 | Keep the simple first gift test; anonymous/sneaked gold is desired in future tests | Accepted scenario, Out of Scope, E2/deferred tests |
| U06 / G06 | Accept input controls except visible suggestions; do not influence player choices | Controls/Input, neutral unsupported-action feedback, E1.2 |
| U07 / G07 | Accept text/hub proposal; hidden rooms, puzzles, traps later; never procedural locations | Location structure, Out of Scope, epic deferred work |
| U08 / G08 | Accept manual reload/save test points for branching paths/interactions | Save model extended to restore new growth state; E1.4 |

### Interpretation and remaining assumptions

- Travel arithmetic corrected to `time = distance / speed`. No external D&D timing rule is adopted or needed.
- Natural outcomes apply to admitted uncertain checks; impossible actions/ownership violations still fail feasibility validation without a roll. Actual rolled probabilities are 5%–95%, counted before the roll.
- LLM may raise contextual difficulty. G03 explicitly proposes avoiding automatic scaling of an unchanged task merely to cancel earned bonuses, preserving the requested feeling of overpowering familiar challenges. That anti-scaling detail remains open for correction.
- G04 retains the user's suggested dialogue formula as trial tuning, not silently final mechanics. Counting both speakers once per completed exchange, rounding to 15 seconds, 60-second face-to-face silence interruptions, route distances/speeds, prepared-pouch timing, and 06:00 morning are explicit provisional details. Overnight waiting does not stop every minute.
- G18: failures award zero XP (accepted). Success awards `floor(100 * (0.95 - p) / 0.90)`; XP curve amounts remain draft tuning proposals.
- The old permanent rating caps, rejection of natural extremes, fixed five-minute action costs, wait presets, visible suggestions, no-XP clause, and blanket P0 leveling exclusion are superseded.
- P0 gains only the requested rule behavior on its existing check plus progression accounting/allocation; its locations, NPC count, social conflict, and check-situation count do not increase. Near-threshold saves test level-ups without adding grind or encounters. Full affinity growth remains P1.
- G05–G08 now carry accepted status with corrections. G03/G04 separate accepted direction from tuning; G09's conflicting clause is removed. G01–G02/G09–G18 remain proposals where indicated. Draft 0.2 is not whole-document approval.

## 2026-09-07 — Kyle's P1 redesign: alchemy and daily quests; draft 0.3

Kyle replaced the competing drink stall with an alchemy crafting system and added a Solo Leveling-inspired daily quest system with gacha item rewards.

| ID | Change | Applied locations |
| --- | --- | --- |
| U09 / G14 | G14 drink-stall economy superseded; 30-gold P1 start carried into G19 | Stage gates, Difficulty/economy assumption block, Simulation economic loops, E3 scope, G register |
| U10 / G19 | Alchemy crafting added as P1 mechanic: potions (healing, mana-restoration pending affinity-cost system), poisons (weapon/food coating), brewed drinks; narrow upgrade tracks unlock new recipes at thresholds T1=10/T2=25 (proposals) | Game Mechanics (Alchemy and crafting), Progression (Alchemy craft progression), Basic skills, Out of Scope, G register; E3.3/E3.4 → E3.3/E3.4/E3.5 |
| U11 / G20 | Daily quest system added as P1 mechanic: System-assigned daily objectives (3 slots), XP + gacha draw on completion, three rarity tiers (70/25/5%), no failure penalty; fictional System framing open | Game Mechanics (Daily quest system), Quest system, Success Metrics, Out of Scope, G register; new E5 |

### Interpretation and design intent

- Alchemy replaces the stall as the P1 economic/crafting activity; community viability (G01–G02, ward pressure) is unchanged.
- Upgrade model is *recipe unlock*, not a stat multiplier: each craft type's track unlocks a new, named capability (e.g., Restorative Elixir, Draught of Revival, Artisan Brew). Declining an unlock re-offers it; base recipes remain available.
- Draught of Revival (T2 healing unlock) is the most consequential ability: player must administer it within 120 seconds of the target's death. This is a deliberate time-pressure restriction that keeps the ability rare and meaningful.
- Mana-restoration track is conditionally deferred: it requires the affinities to have a declared per-use cost. If affinities have no cost, the track simply does not exist in P1.
- Brewing is separated into its own skill (Brewing) alongside Alchemy; both are universal and subject to G03 checks.
- The daily quest system's fictional framing (LitRPG "System") is an open design question; the working default is a status-window interface consistent with LitRPG genre conventions (the stated target audience includes LitRPG readers). Kyle's Solo Leveling reference establishes the aesthetic intent.
- No failure penalty for daily quests: quests expire, not punish. This diverges from Solo Leveling's harsher mechanics by design.
- G14's specific drink-stall economy numbers (ingredient 1g/serving, 2 ingredients/2 drinks/30 minutes, 2g sell price, 4-serving stock) are superseded. G19 adopts the same economic philosophy (no infinite budgets, declared ingredient costs, NPC preference/affordability) with alchemy products instead.
- Epics: E3.3 "competing drink stall" → "craft and apply alchemy"; E3.4 "apply a poison" added; E3.5 "live with the result" (formerly E3.4). New E5 covers daily quest system. E4 unchanged.
- All G19/G20 values are proposals requiring correction before P1 implementation. Draft 0.3 is not implementation authorization.

## 2026-09-07 — G18 failure-XP accepted; P0 design complete

| ID | Change | Applied locations |
| --- | --- | --- |
| U15 / G18 | Failures award zero XP — accepted decision. 25% failure-award assumption removed. Success-only XP curve confirmed. G18 updated to "Accepted direction (no failure XP); curve values proposed" | Progression section (G18 assumption block and following paragraph), G register |

P0 design is now complete. All accepted corrections are locked (G03–G08, G18). Remaining open items are P1 tuning proposals (G01–G02, G09–G13, G19–G20) and P2 proposals (G21) — none block P0 architecture. Recommended next step: `gds-game-architecture` in a fresh context.

## 2026-09-07 — Kyle's quest-framing corrections; G20 direction accepted; P2 added

| ID | Change | Applied locations |
| --- | --- | --- |
| U12 / G20 | System framing confirmed as fourth-wall-breaking LitRPG interface, distinct voice, separate from narrator and NPC speech; this is accepted design direction (not open) | Daily quest system section, G20 register row updated to "Accepted direction (framing); details proposed" |
| U13 | All quests — System daily and organic NPC — must display explicit success conditions when accepted; player can inspect these at any time; hidden information (NPC motives, world facts) remains hidden; success conditions do not | Quest system section (added display rule); G10 extended to record success conditions at accepted state; Success Metrics P1 evidence |
| U14 / G21 | P2 stage added: hidden bonus objectives on all quest types; LLM generates 1–3 bonus conditions per quest at creation (hidden); LLM judges whether player's approach qualifies at evaluation; bonus rewards (XP, extra gacha draw, or small item) must stay within declared budget; no condition revealed to player before or after trigger | Goals/stage gates (P2 row), Daily quest system (P2 forward reference), Out of Scope P1 (exclusion explicit), G register (G21 added), Epic table (E6), epics.md (E6 full spec) |

### Interpretation

- "All quests should be like this" means the clarity standard — visible success conditions — applies to all quest types, not that all quests use the System's fourth-wall voice. Organic quests retain NPC voice for negotiation; the journal entry on acceptance shows the conditions in plain language.
- Hidden bonus conditions are generated by the LLM and are never surfaced to the player, even after triggering. The reward notification (brief System message) confirms something extra was earned without explaining why. This preserves the surprise and rewards attentiveness to creative play without turning it into a puzzle to solve.
- P2 is conditional on P1 success exactly as P1 is conditional on P0. No automatic promotion.
- G21 bonus reward budget is not yet specified; it must be declared before E6 implementation.
