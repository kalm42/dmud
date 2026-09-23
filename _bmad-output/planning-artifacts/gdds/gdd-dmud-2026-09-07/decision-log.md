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

## 2026-09-12 — P0 source-of-truth resolution; baseline 0.4

Kyle requested resolution of the P0 source-of-truth decisions identified by the implementation-readiness review. This entry supersedes the P0 tuning and status language in draft 0.3. It does not approve conditional P1/P2 assumptions.

| ID | Approved P0 decision | Applied locations |
| --- | --- | --- |
| U16 | P0 opens on a Title surface with New Game and Continue; Continue uses the existing three-slot save selector | GDD P0 entry/Session 0; GDD and companion epic E1 |
| U17 | New Game runs a Rowan-led, zero-fictional-time Session 0; the player authors the character concept and name; Rowan distinguishes facts, premises, preferences, and non-binding hopes; explicit confirmation begins play | GDD P0 entry/Session 0; companion epic E1.0 |
| U18 / G03 | James is an example UX persona, not a fixed protagonist. P0 uses Body, Agility, Constitution, Mind, and Presence with the fixed array 8, 10, 12, 13, 14 assigned exactly once; modifiers use `floor((score - 10) / 2)`; confirmed starting assignments remain immutable while later earned increases change current scores | GDD entry, uncertainty, character, persistence, G register; companion epic E1.0 |
| U19 / G03 | The controlled evidence fixture uses Presence 14 (+2) + Persuasion 1 at difficulty 12 and 60% success; ordinary Session 0 characters may assign the standard array differently. Difficulty follows feat and circumstances and does not scale an unchanged task merely to erase earned mastery | GDD uncertainty, progression, G register |
| U20 / G04 | Existing P0 timing values are approved as bounded fixture rules: 1.4/2.8/5.6/0.5 m/s movement, 7 m and 140 m routes, `15 * ceil(words / 30)` dialogue with a 15-second nonempty minimum, 5-second prepared-pouch transfer, 06:00 morning, and 60-second face-to-face silence | GDD actions/time and G register |
| U21 / G04 | Campaign epoch is day 1 at 00:00; confirmed P0 play begins at second 28,800 (day 1 at 08:00); Session 0 advances zero seconds | GDD actions/time, P0 entry, G register; companion epic E1.0 |
| U22 / G18 | P0 uses success-only XP: failures award zero; successful meaningful checks award `floor(100 * (0.95 - p) / 0.90)` to player and relevant-skill tracks; both start at level 1/0 XP; next-level cost is `100 * current level` with carryover; rewards are one attribute point or +1 relevant skill bonus per applicable level; no caps | GDD progression and G register |
| U23 / G16 | The endurance evaluation's 60 minutes are wall-clock time; simulated seconds advanced are recorded separately. Other G16 targets remain provisional until measured | GDD technical specifications |
| U24 | GDD and companion design epics advance to version 0.4 with status `p0-baseline-approved`; conditional P1/P2 assumptions remain unapproved | Frontmatter, opening status note, correction priorities |
| U25 | The 20–60-minute P0 session target includes Session 0 and the opening playable scene for a new campaign | GDD game flow and pacing |

### Resolution notes

- The five-attribute standard array is the approved low-rework baseline already encoded in the detailed P0 epics; the earlier four-attribute 0–3 proposal is superseded.
- The prepared P0 gift remains the established 10,000-gold known-value pouch. The root implementation epic's isolated 100-coin conservation criterion is a downstream defect, not a competing GDD decision.
- Session 0 changes entry and character setup, not the controlled world's content budget: P0 still has three locations, four named NPCs, one conflict, and one uncertain-check situation.
- P1/P2 proposals and G15–G17 statuses are not promoted by this pass, except that G16's endurance duration is disambiguated as wall-clock time.
- Architecture, final UX open-item wording, and the root implementation epics remain downstream artifacts to reconcile in their own workflows. The GDD now owns the approved P0 design baseline they must follow.

### Finalization audit

- Audited U16–U25 against `gdd.md` and the companion `epics.md`; every decision is captured.
- Reconciled the original brief, addendum, and source decision log. No accepted P0 intent was dropped. The 20–60-minute first-session budget now explicitly includes Session 0 and the opening scene.
- Ran the GDD validation checklist against the text-based primary type and the documented RPG/simulation concerns. No failures or critical issues remained.
- Resolved validator continuity warnings by carrying all Title recovery states into E1.0 and adding the missing inline G21 assumption marker.
- Remaining low-severity incompleteness is intentionally confined to gated P1/P2 values and the proposed G15/G16/G17 items; none blocks the approved P0 design baseline.
- No document-polish standards, external handoffs, or completion hooks are configured for this workflow.

## 2026-09-13 — Resource pools, spell terminology, P1/P2 resolution, and P3 combat; baseline 0.5

Kyle identified missing combat and resource-pool design, established **spells** as the name for powers gained from awakened affinities, proposed attribute-derived Health and Mana, requested a combat stage, and asked that all P1/P2 assumptions be resolved. This entry supersedes earlier statements that G01–G02, G09–G13, G15–G17, and G19–G21 remain proposed or incomplete. Historical entries remain accurate records of their earlier states.

| ID | Approved design decision | Applied locations |
| --- | --- | --- |
| U26 | Affinity-awakened powers are **spells**; ordinary universal proficiencies remain **skills**. Affinity spell slots limit repertoire and are distinct from Mana | GDD concept, pillars, mechanics, RPG design, progression, assets, epics; E4 |
| U27 / G22 | `Maximum Health = Body × Constitution`; `Maximum Mana = Body × Mind`, using current raw scores. Current/max growth, clamping, save/load, safe-rest recovery, spell spending, insufficient-Mana rejection, Downed, stabilization, death, and recoverable player defeat are explicit | GDD Derived Health and Mana; P1/P3 evidence; E3/E4/E7 |
| U28 / G01–G02 | Four one-resident households, food consumption/inventory, three-day victory, repair/protection/relocation costs, seven-day ward, warnings, daily loss, and Exposed recovery are fixed | GDD win/loss, G register; E3 |
| U29 / G09–G11 | P1 has two exact affinity packages, two spell slots per affinity, starting spells, four Rest-stone outcomes, an 80/20 retained rarity roll, uniform package outcome, fixed Mana/effect parameters, and permanence | GDD inventory/equipment and Awakening; E4 |
| U30 / G12–G13 | P1 uses three distinct consequential spell uses plus the fixed Rest Is Part of the Work trigger; the LLM generates its player-facing name/description from the event; Copper Sandglass and Brackenford's Anchor are fixed rewards; four Deepened replacements, the clue, and reveal point are explicit | GDD Earned Evolution; E4 |
| U31 / G10 | Journal states, accepted-success contract, evaluating authority, reward ownership, and G01 victory authority are fixed | GDD Quest System; E3/E5 |
| U32 / G19 | Starting tools/base recipes, a reproducible difficulty-12 substitution fixture, twelve Health/Mana/poison/brewing recipes, effects, inputs, work times, values, T1/T2 thresholds, supplier prices/stock/restock, 30-gold start, and bounded Mara/Ivo demand are fixed | GDD Alchemy and economy; E3 |
| U33 / G20 | Three daily slots refresh at 06:00 with one crafting, social, and observation quest; each awards 25 player and skill XP plus a draw; the 70/25/5 nine-item pool is fixed; no combat quest through the P3 proof | GDD Daily Quest System; E5 |
| U34 / G21 | P2 records one hidden condition per quest and one fixed reward; XP is 10–25, item ceiling is 5 gold, one extra draw is allowed, the storage/evaluation contract is explicit, and the notification never exposes the condition | GDD Daily Quest System; E6 |
| U35 / G15–G17 | Accessibility, responsiveness/recovery/memory observations, repetition, conservation, route coverage, and return-session signals are approved evaluation targets | GDD Art, Technical Specifications, Success Metrics; E1–E5 gates |
| U36 / G23 | P3 follows P2 and proves one authored one-on-one combat encounter: initiative, six-second rounds, movement/actions, attack mappings, Defense, damage, Cinder Lance, opponent stats, surrender/escape, XP/loot uniqueness, and persistence | GDD stage table and Combat Proof; new E7 |
| U37 | GDD and companion design epics advance to version 0.5 with status `staged-design-baseline-approved`. P0 remains the initial implementation; P1/P2/P3 design approval does not bypass evidence gates | Frontmatter, opening status, sequence, correction/dependency text |

### Reconciliation notes

- Numeric Mana replaces the earlier exhausted-use model and unblocks the G19 mana-restoration track. Every P1 spell has a Mana cost.
- Health damage and wound conditions are distinct: potions can restore Health and remove the wound type they name. Draught of Revival retains the earlier 120-second restriction and now returns the target at 25% maximum Health.
- P1 still excludes combat encounters. Its resource pools, spell costs, poisons, wounds, and potions establish the mechanical foundation; P3 applies them to combat after P2.
- P2 hidden bonuses apply to quest types currently supported at P2. Combat quests remain outside the pool through the P3 proof and require a later explicit content addition.
- The two affinity packages intentionally test utility spells. Fixed spell mechanics retain generated names/manifestations shaped by the character and history. Cinder Lance is confined to an independent controlled P3 fixture with a free Ember slot, not approval for a generated combat-spell library or a mutation to the live character.
- No P0 content or implementation scope is expanded by version 0.5.

### Finalization audit

- Audited U26–U37 against `gdd.md` and `epics.md`; every decision is represented in the canonical G register, stage table, mechanics, evidence, or companion epic.
- Reconciled the final 0.5 draft against the brief, addendum, and source decision log. Restored character/history-shaped spell presentation, generated achievement presentation with fixed mechanics, title-or-achievement future upgrade eligibility, and explicit affinity-slot ownership.
- Resolved all live `[ASSUMPTION]` and `[NOTE FOR DESIGNER]` markers. Historical log text remains unchanged and is superseded by this entry.
- Ran the GDD validation checklist for the text-based primary type and RPG/simulation secondary concerns. The final pass found no remaining critical, high, or medium issue; its last low count mismatch was corrected from three exits to four controlled combat outcomes.
- No document-polish standards, external handoffs, or completion hooks are configured.
- The text-based genre guide marks narrative design as critical. `gds-create-narrative` is the immediate optional handoff offered to Kyle. Because the existing architecture, root epics, and readiness report predate GDD 0.5, the next required technical chain is an updated `gds-game-architecture`, then `gds-create-epics-and-stories`, then `gds-check-implementation-readiness`, each in a fresh context.

## 2026-09-13–14 — Survival, conditions, Stamina, and causal access; baseline 0.6

Kyle opened a facilitative design pass for physiological needs and a shared status-effect foundation, then extended it through food production, autonomous livelihoods, physical access, ownership, and evidence. The completed decisions below are applied to `gdd.md` and `epics.md` as baseline 0.6.

| ID | Accepted design direction | Status |
| --- | --- | --- |
| U38 | A character gains `Starved` after 24 consecutive in-game hours without eating and another stack after each additional 24 hours. `Effective Maximum Health = round(Base Maximum Health × 0.75^stacks)`. Applying a stack immediately clamps current Health to that maximum without counting as damage. If the effective maximum rounds to 0, the character dies at 0 Health. Eating one complete serving resets the timer and removes one stack; restored maximum Health does not heal current Health | Accepted; serving language finalized by U67 |
| U39 | A character gains one `Exhausted` stack after 24 consecutive in-game hours without completing eight uninterrupted hours of adequate sleep and another after each additional 24 hours. `Effective Maximum Stamina = round(Base Maximum Stamina × 0.75^stacks)`. Applying a stack immediately clamps current Stamina without counting as expenditure. Eight hours of adequate sleep resets the timer, removes one stack, and restores current Stamina to the newly available maximum. A physical bed is required for adequate sleep. A ward is one way—not the only way—to make rest safe; equivalent protection or safe relocation remains valid | Accepted |
| U40 | Add a dedicated design/delivery stage for character statuses, buffs/debuffs, stacking, survival needs, and their interactions. Unlike effects may coexist; repeated `Starved` instances stack multiplicatively | Accepted; placement finalized by U78 |
| U41 | Add a distinct `Stamina` resource pool separate from Mana. `Exhausted` multiplicatively constrains its recoverable maximum. At 0 Stamina, a character cannot move or perform Stamina-costing actions but may talk, inspect, eat, use suitable items, and attempt sleep. Exhaustion alone is nonlethal | Accepted; formula, costs, and recovery finalized by U49–U51 |
| U42 | Death occurs at 0 Health. A `Starved` stack that rounds effective maximum Health to 0 therefore kills the character; 0 Stamina does not | Accepted |
| U43 | Conditions, buffs, debuffs, and item treatments use a configurable shared effect language so the LLM can invent new effects. Generated presentation may vary, but mechanical effects must use declared, validated effect shapes and specify target, magnitude, duration, stacking, and removal. Supported design examples include maximum-resource changes, fixed damage over time, spell-cost changes, damage changes, and a sharpened weapon's subtle damage increase | Accepted; budgets finalized by U46–U48 and sources/removal by U59/U71 |
| U44 | Differently named effects coexist. Every effect definition declares duplicate-application behavior as `Stack`, `Refresh`, or `Replace`: stacked instances apply independently, refreshed instances retain magnitude and reset duration, and replacement keeps the stronger application. Each definition also records its logical cause, target, magnitude, duration, and removal rule | Accepted |
| U45 | A generated effect's validated source—such as a crafting outcome, spell, item quality, injury, environment, or survival threshold—provides its mechanical effect budget and eligible targets. The LLM may choose an allowed effect shape, target, name, description, duration, and magnitude within that budget; out-of-budget proposals are rejected or reduced. The complete accepted definition is recorded and remains mechanically consistent on later references | Accepted |
| U46 | The generated-effect `Major` tier must remain consequential under uncapped end-game progression. Its per-effect limits are a ±20 flat modifier where the target uses flat values, a ±50% proportional modifier, or 100 total periodic damage. These are alternative primary effect shapes rather than values bundled into one generated effect | Accepted |
| U47 | Generated-effect magnitude uses three tiers. `Subtle` permits a ±1 flat modifier, ±10% proportional modifier, or 10 total periodic damage. `Standard` permits ±4, ±25%, or 30 total periodic damage. `Major` permits ±20, ±50%, or 100 total periodic damage. A generated effect receives one primary effect shape; explicitly authored effects may combine components when separately balanced | Accepted |
| U48 | Ordinary modifiers resolve as `round(Base value × (1 + the sum of percentage modifiers)) + the sum of flat modifiers`. Opposing percentages cancel, percentage stacks grow additively rather than exponentially, and flats apply after percentages. Health, Stamina, Mana, damage, and healing cannot fall below 0. Spell and action costs cannot fall below 1 unless an authored effect explicitly makes them free. `Starved` and `Exhausted` retain their explicit multiplicative same-condition formulas | Accepted |
| U49 | `Maximum Stamina = Agility × Constitution`, using current raw scores. Current/maximum tracking, recalculation after attribute growth, clamping, persistence, and save/load follow the same pool rules as Health and Mana | Accepted |
| U50 | Ten uninterrupted minutes of non-strenuous rest restores 25% of effective Maximum Stamina, rounded up. Eight hours of adequate sleep removes one `Exhausted` stack and then restores current Stamina to the newly available maximum. Passive clock advance and eating alone do not restore Stamina, although declared consumable effects may. Short rest never removes `Exhausted`; when effective Maximum Stamina is 0, adequate sleep is required before movement can resume | Accepted |
| U51 | Stamina expenditure uses four bands: Routine 0, Exerting 5, Strenuous 10, and Extreme 20. Routine includes normal walking, conversation, inspection, and ordinary item use; Exerting includes combat movement up to 8 m, attacks, and defending; Strenuous includes a sprint up to 34 m, an escape attempt, and sustained heavy work; Extreme is reserved for exceptional validated feats. Casting normally costs Mana rather than Stamina unless a spell or effect says otherwise. The full cost must be payable before an action begins; rejection spends no time or partial Stamina. The 0-Stamina immobility rule overrides free normal walking | Accepted |
| U52 | Automatic extra food loss caused merely by ward expiry or an `Exposed` state is rejected as noncausal and supersedes that part of U28/G02. Food leaves inventory only through a recorded event with an intelligible cause, such as consumption, transfer, theft, spoilage, or destruction | Accepted correction |
| U53 | `Exposed` is a household/environmental state: the household's current sleeping place lacks valid protection. It causes no damage and removes no food, but blocks the G01 safety requirement and prevents sleep there from qualifying as safe sleep. A repaired ward, valid protection agreement, safe relocation, or another validated equivalent removes the cause. A missing bed independently prevents adequate sleep without making a protected household `Exposed` | Accepted |
| U54 | Fixed clock-boundary food deduction is rejected. Hunger creates a character want that drives an NPC plan and concrete actions: eat accessible prepared food; prepare ingredients and eat; buy ingredients or a prepared meal; visit a restaurant; or first obtain gold through work, profession, trade, or another valid action. Cooking, purchases, work, travel, and eating consume fictional time and commit observable inventory, gold, and state changes. Wants lead to actions on the shared clock, including for off-screen NPCs | Accepted; priorities and success finalized by U55/U62/U67 |
| U55 | Hunger is an internal planning pressure rather than another visible debuff. At 0–8 hours since eating, food does not influence planning; at 8–16 hours it is a low-priority want; at 16–20 hours it competes with ordinary work and leisure; at 20–24 hours it interrupts noncritical plans; at 24 hours the character gains `Starved` and food remains critical beneath only immediate threats. NPCs select the shortest feasible causal plan from what they know and can access, considering prepared food, ingredients, cooking access, money, relationships, work, risk, and travel; failure triggers replanning rather than invented resources. The player receives hunger feedback but retains control | Accepted |
| U56 | Sleep is an internal planning pressure. At 0–12 hours since adequate sleep it does not influence planning; at 12–16 hours securing a bed and safe place becomes a low-priority want; at 16 hours beginning adequate sleep becomes high priority; at 20–24 hours it interrupts nonessential activity; at 24 hours without completing adequate sleep the character gains `Exhausted`. NPC plans may return home, rent lodging, request hospitality, obtain a bed, repair shelter, secure protection, relocate, or obtain required resources through work/trade. Inadequate sleep passes time and may restore ordinary current Stamina but does not reset the sleep timer or remove `Exhausted` | Accepted |
| U57 | Jobs and professions are simulated economic plans, not passive income or character-class restrictions. Work requires a known opportunity, location, fictional time, and any required tools or inputs; the NPC travels and performs it on the shared clock. Goods, services, wages, expenses, and ownership change only through recorded actions. Employers and customers have finite budgets and demand. Missed work, failed production, unavailable inputs, closure, or absent demand may prevent payment and trigger replanning. NPCs may change employers, take contracts, sell or trade, borrow, seek help, or pursue illicit alternatives when supported by knowledge and personality | Accepted |
| U58 | Player and NPC characters use the same hunger, sleep, Stamina, Health, condition, and death rules. Off-screen NPCs pursue plans only when game time advances and spend the same time and resources. Failed plans may leave an NPC `Starved`, `Exhausted`, immobile, or dead; persistent off-screen death requires a complete recorded causal chain. The player is interrupted only by consequences they can reasonably perceive and otherwise learns through later observation, absence, conversation, or rumor | Accepted; death-at-0 correction in U42 governs |
| U59 | Every effect records a causal source category such as physiological, wound, poison, disease, magical, environmental, social, or item treatment. Removal must name the matching cause, a compatible category, or the exact effect: food removes `Starved`, adequate sleep removes `Exhausted`, wound treatment removes `Bleeding`, antidotes remove compatible poison effects, dispels affect magical effects rather than physiological/wound states, and an item treatment ends through its declared physical removal or use limit. Numerically opposing effects remain present and expire independently even when their current modifiers cancel | Accepted |
| U60 | A single new P1 containing effects, resource pools, survival needs, autonomous planning, and the livelihood economy is rejected as disproportionately large. The new work must be divided into smaller stages with independently playable evidence gates | Accepted correction; replacement sequence finalized by U78 |
| U61 | The staged sequence is rebalanced as P0 existing causal-world proof; P1 Effects and Resources; P2 Needs and Shelter; P3 Autonomous Livelihoods; P4 Community and Alchemy; P5 Spells and Recognition; P6 Daily Quests; P7 Hidden Quest Bonuses; and P8 Combat. P1 proves Health/Mana/Stamina plus the shared generated-effect rules; P2 proves hunger, food/preparation, sleep, beds/protection, `Exposed`, `Starved`, and `Exhausted`; P3 proves wants-driven multi-step plans through jobs, finite gold, shops/restaurants, preparation, lodging, and off-screen activity. Former P1 epics become P4–P6; former P2 becomes P7; former P3 becomes P8. P0 remains unchanged and every later stage retains a conditional evidence gate | Accepted |
| U62 | Brackenford community success replaces the static three-day food-stock requirement with three consecutive simulated days of lived stability for every household. Each resident must eat through recorded causal actions before the next `Starved` threshold, complete adequate sleep using a bed in a protected place, and remain in a household that is not `Exposed`. Food, lodging, and protection must be funded or supplied by resources and commitments that exist; future income or food counts only after it is earned, transferred, produced, or contractually guaranteed. Each household's failed day resets only its own streak and causes no arbitrary resource loss. Stockpiles, farming, work, restaurants, hospitality, patrols, ward repair, and relocation may all satisfy the same simulation | Accepted; placed in P5 by U78 |
| U63 | Food uses a crafting-chain model rather than uniform food units. Recipes transform declared raw materials through required tools/facilities and recipe-specific time and Stamina into products with their own servings, taste, effects, and shelf life; values are not globally fixed at 30 minutes or 5 Stamina. Raw-edible ingredients such as cabbage may be eaten directly, while cooking, baking, curing, pickling, or fermenting can improve taste, effects, value, or preservation. Examples include flour, sugar, and butter becoming pound cake; cabbage and water becoming stew; and cabbage becoming slaw or sauerkraut. Foods expire and remain edible and hunger-satisfying, but carry an increasing chance of a causal negative food-poisoning effect as they age beyond expiration. Cured and preserved products may outlast cooked products according to their declared recipe and storage | Accepted; storage and fixtures finalized by U66/U73 |
| U64 | Expired food uses `risk = min(100%, 5% + 95% × time past expiration / declared shelf life)`, rounded to the nearest whole percent; unexpired food has 0% spoilage risk. Eating it still supplies a serving, resets hunger, and removes one `Starved` stack. Consumption triggers a Constitution check whose difficulty produces the nearest achievable failure probability to the calculated risk for that character; the natural-1 failure and natural-20 success rules bound actual d20 risk to 5%–95%. On failure, food up to 25% of its shelf life overdue grants a Subtle food-poisoning effect budget, more than 25% through 75% grants Standard, and more than 75% grants Major | Accepted; XP and fixtures finalized by U65/U73 |
| U65 | Food-poisoning Constitution checks and other reactive resistance checks follow the ordinary success-only XP curve rather than a no-XP exception. A nearly certain success yields negligible or zero XP; a difficult resistance check awards more XP only on success, while failure awards zero under G18 | Accepted |
| U66 | Food spoilage uses a single expiration timestamp per batch; storage conditions do not alter aging in the current scope. Raw food receives its timestamp from its item definition when created/acquired. A crafted output receives a new expiration timestamp equal to craft completion plus that recipe's shelf-life duration; ingredient age and expiration have no effect on the output's expiration. The food-poisoning check applies only if the consumed item is past its own timestamp. More detailed storage, inherited spoilage, and temperature simulation are deferred | Accepted correction |
| U67 | One complete food serving has a common physiological result: it resets the hunger timer and removes one `Starved` stack. Foods vary independently in ingredients, tools/facilities, preparation time, Stamina cost, yield, expiration duration, price, taste, preference, and optional effects. Taste and preference affect NPC choice and willingness to pay but not the starvation timer; raw-edible ingredients may provide servings directly. Calories, macronutrients, vitamins, and dietary-balance penalties are out of scope for the current stages | Accepted |
| U68 | The former broad NPC-resources pillar is replaced by **Needs become plans**: every character has wants shaped by physiological needs, personality, obligations, knowledge, and circumstances. NPCs pursue those wants through concrete actions on the shared clock using finite resources and real relationships. Success changes world state; failure produces new needs and replanning rather than abstract penalties or invented resources. The player receives information and constraints but retains control of the player character | Accepted |
| U69 | The shared core loop becomes: need, desire, or opportunity → inspect knowledge/resources → choose or form a feasible plan → act, travel, work, craft, converse, or transact over time → validate costs, uncertainty, and effects → commit changed resources, conditions, relationships, and world state → observe → continue or replan. NPC wants/personality choose among feasible plans; the player chooses priorities. Player physiological needs create tradeoffs rather than forced actions: the player may deliberately skip sleep or food and accept `Exhausted` or `Starved` consequences when another goal is worth the cost | Accepted |
| U70 | The inspectable player-status view shows current and effective maximum Health, Mana, and Stamina; each known effect's name, stacks, mechanical impact, source, and removal condition; time since the last meal and adequate sleep; and exact time until the next `Starved` or `Exhausted` stack. Threshold messages state facts without suggesting actions. Unknown effects expose only observed symptoms until identified. Exact remaining duration is shown only when known to the character or revealed by an ability such as Copper Sandglass | Accepted |
| U71 | Generated-effect tier follows the fictional source and is declared before any uncertain check. Subtle covers ordinary maintenance, common materials, minor environments, and plausible improvisation; Standard covers trained techniques, established recipes/spells, specialized tools/materials, and serious hazards; Major requires rare materials/artifacts, major achievements or sacrifices, or extreme hazards with proportionate access/risk. Difficulty determines success rather than magnitude. Natural 20 succeeds without raising the tier; natural 1 fails without creating the effect. Repetition of mundane actions cannot promote their source to Major | Accepted |
| U72 | P1 Effects and Resources uses three controlled effect fixtures. `Sharpened` requires a whetstone, 10 minutes, and 5 Stamina and gives one weapon +1 damage for its next 10 successful hits; duplicate applications Refresh. `Bleeding` deals 2 Health every 6 seconds for five ticks (10 total); separate wounds Stack and treating one wound removes its linked instance. A modifier-interaction fixture applies +25% and -25% to the same value so both remain while the effective value returns to base and each expires independently. P1 also proves derived Health/Mana/Stamina, expenditure/recovery, all tier limits, source validation, LLM-generated presentation, inspection, threshold ordering, and save/load. Hunger, sleep, autonomy, alchemy, spells, and combat are excluded | Accepted |
| U73 | P3's controlled food set contains six varied products. Raw cabbage needs no preparation, takes 10 minutes to eat, yields one serving, and expires seven days after creation. Cabbage stew uses cabbage plus water at a hearth with a pot, takes 30 minutes and 5 Stamina, yields two servings, and expires after two days. Pound cake uses flour, sugar, and butter in an oven, takes 60 minutes and 10 Stamina, yields four servings, and expires after five days. Sauerkraut uses cabbage, salt, and a crock, takes 15 minutes and 5 Stamina of setup plus 72 hours of unoccupied fermentation, yields four servings, and expires after 30 days. Cooked meat uses raw meat with a hearth and pan, takes 20 minutes and 5 Stamina, yields two servings, and expires after two days. Cured meat uses raw meat, salt, and a curing rack, takes 30 minutes and 5 Stamina of setup plus 48 hours of unoccupied curing, yields two servings, and expires after 14 days. Completed batches receive fresh expiration timestamps | Accepted; stage corrected by U78 |
| U74 | Adequate sleep requires one continuous eight-hour interval with a usable bed and valid protection for the entire interval. Leaving the bed, a disruptive event, loss of the bed, or protection lapse before completion makes the sleep inadequate. Inadequate sleep still restores 25% of effective Maximum Stamina per completed 10-minute rest interval but does not reset the sleep timer or remove `Exhausted`. Hunger and other timed effects continue during sleep; crossing a status/effect threshold applies it without waking the character unless that effect or event explicitly causes waking. Adequacy is committed only after all eight hours complete | Accepted |
| U75 | P4 Autonomous Livelihoods uses Ivo and Tessa without adding a fifth named NPC. Ivo begins with 0 discretionary gold, 12 hours since his last meal, and 12 hours since adequate sleep. Tessa's business begins with 12 gold and six cabbages priced at 1 gold each. A declared four-hour courier shift pays Ivo 3 gold only on completion, transferring it from Tessa; Ivo may then buy a cabbage, transferring 1 gold back. Ivo's protected home has a hearth, pot, and bed. His preference favors cooking stew when feasible but allows raw cabbage when time/facilities require; failed work, insufficient employer funds, sold-out food, unusable hearth, or lost protection triggers replanning. After eating, he pursues adequate sleep. This replaces Ivo's unexplained 3 discretionary gold with earned funds and preserves finite money/stock | Accepted; stage corrected by U78 |
| U76 | Household resources are physically local rather than remotely usable or owner-exclusive. A present character may access a bed, food, tool, container, or room through ownership, permission, relationship, a compatible key, an unlocked entrance, successful lockpicking, or forced entry. Beds declare sleeping capacity; consensual sharing within capacity can provide adequate sleep to every occupant. Unauthorized eating or sleeping still satisfies the physiological rule when the resource and conditions are valid, but trespass, theft, damage, noise, witnesses, evidence, relationship changes, and legal responses remain causal consequences. Discovery or another disruptive event may interrupt sleep. Doors/entrances can be locked; keys open matching locks; lockpicking and breaking an entrance require their declared tools, time, uncertainty/costs, and consequences | Accepted; placement and fixture finalized by U78/U82 |
| U77 | Survival pressure changes goal priority and can broaden acceptable risk without erasing NPC personality. Normal hunger favors owned food, purchases, cooking, work, and planned hospitality; urgent hunger may admit requests for help, borrowing, selling possessions, unfavorable work, or reliance on relationships; `Starved` or near-death states may make trespass, theft, lockpicking, or forced entry eligible only when supported by personality, knowledge, relationships, fear, risks, and remaining alternatives. No threshold automatically makes every NPC criminal or violent. The selected plan still requires physical travel, access resolution, time, Stamina, tools, and checks, and its consequences persist even when it prevents starvation | Accepted |
| U78 | Physical access becomes a separate P2 Places, Access, and Ownership stage before survival needs. The sequence is P0 causal-world proof; P1 Effects and Resources; P2 Places, Access, and Ownership; P3 Needs and Shelter; P4 Autonomous Livelihoods; P5 Community and Alchemy; P6 Spells and Recognition; P7 Daily Quests; P8 Hidden Quest Bonuses; and P9 Combat. P2 proves local resources, doors, locks, matching keys, permission, bed capacity/sharing, lockpicking, forced entry, theft, evidence, consequences, and save/load. Later stages use these already-proven rules and retain conditional evidence gates | Accepted; fixture finalized by U82 |
| U79 | Property truth and character knowledge are separate. The engine records possession changes and the causal theft event, but NPCs learn only through observations, testimony, evidence, and inference. An unwitnessed removal creates no knowledge. An owner must later observe that an expected item is absent and compare that observation with remembered inventory before believing something is missing; theft and thief identity remain hypotheses. Unmarked fungible/common goods do not carry an observable identity proving they are the stolen instance. Suspicion and accusation require a cause such as witnessed access, observed absence, damage/tampering, known opportunity or motive, prior knowledge that a suspect lacked the item, possession of a distinctive object, or inconsistent statements; beliefs may still be mistaken. On a failed lockpicking check, one lockpick breaks and is consumed. A character with another lockpick may attempt again, paying full time and tool cost; without another pick, the attempt is infeasible | Accepted |
| U80 | Property uses two identity models. Distinctive items retain individual identity, current possessor, legitimate ownership claim, provenance, and recognizable marks when present. Fungible items track quantities and causal transfer/theft events but have no observable instance identity after mixing; restitution may return an equivalent item. Authoritative records preserve conservation and causality but never grant NPC knowledge or legal proof by themselves. Repeated finite-cost attempts are allowed: each failed 60-second lockpick attempt consumes one pick, and another pick permits another roll while time and circumstances continue to change | Accepted |
| U81 | State changes never create character knowledge merely because they affect owned property. The knowledge chain for unseen loss is explicit: later inspection/search → observation that an expected item is absent → comparison with remembered state → belief that it is missing → optional hypotheses or suspicions from further evidence. Until an observation occurs, the owner does not know about the loss | Accepted correction |
| U82 | P2's controlled fixture is Ivo's Home. Its front door supports open/closed/locked/broken states and a difficulty-12 lock. Ivo and permitted guest Mara have matching keys; unlocking/opening takes 5 seconds without a roll. Lockpicking requires a pick, takes 60 seconds, and uses Agility + Sleight of Hand at difficulty 12; failure consumes the pick and another pick permits another attempt. Forced entry takes 30 seconds and 10 Stamina with Body + Athletics at difficulty 14; each attempt is loud, success leaves the door broken/open, and another fully paid attempt is allowed. The bed has capacity two and proves consensual sharing. Theft tests one fungible serving and one distinctive marked object; both change possession, but only the distinctive object can be recognized directly. An unwitnessed removal creates no knowledge until later observation of absence. Save/load preserves access states, keys, permissions, possession, event history, observations, and beliefs. Formal guards, arrest, courts, and universal crime reputation remain outside P2; relationship and belief consequences remain active | Accepted |

### 0.6 reconciliation and completion

- `Exposed` is an environmental sleeping-place state; `Starved`, `Exhausted`, and `Bleeding` affect characters. Their causes and removal rules remain distinct.
- U59 resolves opposing-effect and cleansing behavior. U78 resolves the stage sequence; U82 resolves the access fixture. U65, U66, U67, U73, and U74 resolve the food and sleep questions. No facilitation item from this pass remains open.
- The 0.6 GDD and companion epics now use P0–P9 consistently. G24–G27 collect the new foundation decisions without renumbering earlier G IDs.
- U42 and the 0.6 G22 rule supersede every earlier reference to a Downed/stabilization interval: death occurs at 0 Health, while supported revival may operate only within its declared window.
- U52/U54 supersede fixed clock-boundary or ward-triggered food deductions. Food changes only through recorded causal events, and hunger pressures characters toward physical plans.

### 0.6 finalization audit — 2026-09-15

- Independently reconciled `gdd.md` and `epics.md` against the original brief, addendum, and source decision log. No unsuperseded high-severity intent loss remains.
- Restored four source details that had survived only in decision history: the LLM may propose bounded mechanical effect definitions; antidote/dispel/item-treatment category boundaries are explicit; the original P5 stakeholder disagreement is instantiated within the four-person cast; and the deferred *Rise of the Living Forge* innkeeper/domain reference is preserved without scheduling it.
- Preserved the broader long-term ambition for configurable/generated affinities, abilities, spells, items, traps, titles, achievements, and skill-practice-shaped variants. Alternate difficulty modes remain an explicit later decision.
- Resolved deterministic specification gaps needed by downstream architecture: Base versus Effective Maximum terminology; source-bounded generated-effect duration/uses; action/tick/threshold/expiry/death order at one timestamp; a diagnostic Major `Star-metal Edge` fixture; exact-limit and over-limit calibration; and a measurable 100 MB endurance-test memory ceiling.
- Corrected the interim “shortest feasible plan” wording. NPCs weigh time and cost alongside need priority, personality, taste, obligations, relationships, knowledge, and risk; this preserves Ivo's preference for stew when it is feasible.
- Ran the full GDD validation checklist using the canonical text-based game type and the high-complexity RPG/simulation secondary-genre requirements. After corrections, all applicable checks pass; the final epic/content-budget continuity warning was corrected by adding `Star-metal Edge` and the tier/shape matrix to P1's budget.
- Mechanical artifact checks confirm no template tokens, `[ASSUMPTION]`, or `[NOTE FOR DESIGNER]` markers; E1–E11 titles/stages/sequence agree between both files; source links resolve; and `git diff --check` reports no whitespace errors.
- No document-polish standards, external handoffs, or completion hooks are configured. The text-based genre guide marks dedicated narrative design as critical; `gds-create-narrative` remains the immediate optional handoff.

## 2026-09-15 — Version 0.7 P0 fixture-funding correction

| ID | Decision | Status |
| --- | --- | --- |
| U83 | The captured P0 starting state gives the player one prepared, known-value pouch containing exactly 10,000 gold and no other starting gold. This is test-fixture funding only: it is not an ordinary campaign starting balance, a progression reward, or funding for later-stage economies. The 1-gold purchase test and the full-pouch gift/no-gift comparison run as isolated branches, each reloading the same captured starting state; their outcomes never merge. The separate 100-loose-coin timing fixture is not player wealth and does not enter either branch. | Accepted correction; supersedes the unresolved implication that the purchase and full-pouch gift occur sequentially in one branch |
| U84 | GDD and companion design epics advance to version 0.7 with status `staged-design-baseline-approved`. P0 remains the initial implementation, and all later evidence gates remain unchanged. | Accepted |

### 0.7 reconciliation note

- G05, P0 inventory/content budgets, evidence criteria, and E1–E2 now share one exact opening ledger and branch-isolation rule.
- P5 retains its independent 30-gold controlled start; no P0 fixture balance or branch outcome carries into P4, P5, or later economies.
- This correction resolves the earliest P0 implementation blocker without expanding player-facing content or adding a container subsystem.

### 0.7 finalization audit — 2026-09-15

- Audited U83 against `gdd.md` and `epics.md`: the exact opening ledger, isolated fixture branches, loose-coin timing isolation, and later-economy boundary are present in both artifacts where applicable.
- Reconciled the correction against the original brief, addendum, and source decision log. The change preserves the transformative, motive-dependent gift; the same-state gift/no-gift comparison; transaction conservation; persistence; and the simple witnessed first test.
- Ran the full GDD validation checklist against the canonical text-based type and high-complexity RPG/simulation requirements. The two terminology/version findings were corrected; the targeted re-check found no remaining non-pass items.
- Confirmed no live `[ASSUMPTION]`, `[NOTE FOR DESIGNER]`, open-question, or template-token blocker. No document-polish standards, external handoffs, or completion hooks are configured.

## 2026-09-15 — Version 0.8 browser-owned text sizing correction

| ID | Decision | Status |
| --- | --- | --- |
| U85 | Preferred text size is owned by the browser. dmud provides no in-game text-size control and must preserve the user's browser text-size and zoom choices without content or functional loss, including 200% page zoom and reflow at the equivalent of 320 CSS px without two-dimensional page scrolling except for intrinsically two-dimensional content. Visible focus, non-color speaker labels, a quiet layout, and no timed reading remain required. | Accepted correction; supersedes U35/G15 only where it required an adjustable 16–24 px in-game control |
| U86 | GDD and companion design epics advance to version 0.8 with status `staged-design-baseline-approved`. No stage, mechanic, content budget, or implementation authorization changes. | Accepted |

### 0.8 reconciliation and completion

- Updated G15 in the Art and Audio Direction and canonical decision register; the browser-owned sizing requirement now agrees with the finalized UX spine.
- Preserved the existing WCAG-oriented 200% zoom, 320 CSS px reflow, keyboard-focus, non-color attribution, and no-timed-reading requirements.
- No new settings surface, preference persistence, game mechanic, or implementation technology is introduced.
- Targeted checks confirm no live GDD or companion-epic reference still requires a 16–24 px in-game text control; version metadata agrees at 0.8.
- No document-polish standards, external handoffs, or completion hooks are configured.
