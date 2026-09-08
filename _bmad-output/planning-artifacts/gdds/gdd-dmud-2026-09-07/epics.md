---
title: "dmud — GDD Development Epics"
created: 2026-09-07
updated: 2026-09-07
version: "0.3"
status: draft-for-correction
---

# dmud — Development Epics

Design breakdown accompanying [gdd.md](gdd.md). G IDs refer to its decision register, which distinguishes accepted corrections from unapproved tuning. No staffing, sprint lengths, estimates, engine choices, or implementation authorization are implied. Detailed technical stories belong to a later workflow.

## E1 — Act in a small persistent world

**Stage:** P0. **Pillars:** P-A, P-D. **Dependencies:** None. **Value:** Make an intention produce an explainable, durable consequence in the three-location world.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E1.1 — Discover the small world | Inspect three locations, four named people, exits, inventory, and known circumstances | Navigation and descriptions expose only appropriate knowledge; no extra world scope |
| E1.2 — Act and transact | Converse, move, give, purchase, and wait using free text without proactive action suggestions | Feasibility, consent, stock, and funds govern transactions; rejection leaves no partial transfer |
| E1.3 — Resolve uncertainty | Understand stakes and attempt the single meaningful Persuasion check | Pre-roll difficulty and actual success probability, natural 1 failure/natural 20 success, recorded modifiers/result, matching consequences; no unchanged-condition reroll loophole |
| E1.4 — Resume the same situation | Save and load without losing changes | Money, items, clock, relationships, commitments, beliefs, plans, XP/levels/bonuses and allocated/unspent points restored; repeated requests do not double-spend |
| E1.5 — Grow through a difficult check | Gain challenge-dependent XP, raise a skill bonus, and allocate player-level attribute points | No attribute/skill cap; zero XP for checks failing only on 1; threshold test saves avoid adding encounters; resolved check awards once |

**Scope:** G03–G08, G15–G16, and proposed G18 tuning as applicable to P0. No ward simulation, combat, affinity progression, dedicated training activities, or basic-skill unlock system. The action-driven clock uses seconds and pauses offline. Travel uses distance/speed; dialogue uses rendered speech; handling and waits use validated contextual estimates. Timed and event waits yield to actual events and attention-worthy silence. Keep one check situation, one player XP track, and one exercised skill.

**Exit evidence:** One inspect → move → purchase/converse → consequential check → save/load cycle, including a rejected operation, interrupted request/wait, natural-roll extremes, and near-threshold leveling save, preserves authoritative consistency. Verify room/travel distances and movement modes affect duration, speech/handling are counted once, and no proactive suggestions steer the player. E2 supplies the stronger NPC/social proof; E1 alone does not pass P0.

## E2 — Make consequences travel through people

**Stage:** P0. **Pillars:** P-A, P-B, P-C. **Dependency:** E1. **Value:** Observe people change plans and act on what they have learned.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E2.1 — Change someone's options | Give Mara transformative resources and observe a motivated decision | Gift/no-gift comparison changes feasible plans; behavior reflects need, competing desire, obligation, and affected relationship |
| E2.2 — Follow a report | See a witness later communicate through a real encounter | Observation and receipt separated; no NPC omniscience; source and timing inspectable in test evidence |
| E2.3 — Encounter imperfect belief | Experience a changed response to a distorted or doubted report | Belief affects a choice while original facts remain unchanged; no global reputation overwrite |
| E2.4 — Test persistence and credibility | Resume and ask about earlier events | Plans, commitments, and knowledge affect later actions after loading; captured proposals/rolls reproduce mechanical outcomes |

**Scope:** G04–G05, G08, G17. Exactly one social conflict across the existing four people and three locations. The 10,000-gold balance is controlled test funding, not an economy to balance. Keep the first gift witnessed and simple; anonymous gold delivery is a desired later test. The scheduled report encounter is 1,800 seconds after the gift opportunity, with actual travel/handling time respected.

**P0 exit gate:** All five GDD P0 evidence checks, with the G17 proposed repetition protocol. Record Kyle's explanation and believability assessment separately from consistency checks. Investigate failures before increasing scope. Passing P0 supports deciding whether to try P1; it does not prove the complete game enjoyable.

## E3 — Secure Brackenford's future through play

**Stage:** Conditional P1. **Pillars:** P-A, P-B, P-C. **Dependency:** P0 evidence gate and decision to expand. **Value:** Pursue a community future and livelihood without following a fixed plot.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E3.1 — Understand the community pressure | Inspect known safety/subsistence needs, warnings, and commitments | Viability thresholds and pressure are concrete and visible enough to plan; long waits interrupt for warnings |
| E3.2 — Negotiate a supported future | Choose among at least two plausible routes and fulfill the relevant agreements | Protection/repair/relocation outcomes use actual resources and commitments; an unplanned supported solution can meet the same conditions |
| E3.3 — Craft and apply alchemy | Purchase ingredients, craft potions or brewing products, and apply or distribute them | Declared ingredients present in inventory; G03 check determines success; successful craft produces a persistent item; failed craft consumes ingredients with no output |
| E3.4 — Apply a poison | Coat a weapon or food item and observe the effect on contact or consumption | Poison persists on item until triggered or cleaned; applied effect uses G03 modifiers; effect duration and magnitude match the declared recipe |
| E3.5 — Live with the result | Meet viability conditions or recover from setbacks, then continue | Success persists for the defined window; failure offers recovery; NPC adaptation and unresolved concerns survive save/load |

**Scope:** G01–G02, G07, G10, G19. Reuse the hub and cast; use purchased ingredients with no stall, lab, or production chain. Alchemy is personal crafting; NPC purchasing follows preference, affordability, and actual need. No building system, additional region, full economy, or forest-to-tavern production chain.

**Before implementation:** Define the four household populations/resources, protection-contract requirements and costs, warning/loss rules, and budget feasibility for each test route. Define G19 ingredient prices, NPC needs that crafted items can serve, and craft-type thresholds. The GDD proposes thresholds and effect values but does not claim those have been numerically balanced.

**Exit evidence:** Two plausible viable routes, one unplanned supported approach, and a crafting session that produces a used item. At least one successful craft and one failed craft observed. Measure understandable causality, response times, model usage/cost, and remaining motivation to play.

## E4 — Earn a distinctive affinity ability

**Stage:** Conditional P1. **Pillars:** P-D, P-A. **Dependency:** E3 provides consequential activity and history. **Value:** Choose a small build, obtain an uncertain but bounded awakening, and earn an optional evolution.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E4.1 — Choose an affinity package | Choose between two small packages without losing universal basic-skill access | Each affinity's bonus, ability ownership, and available slots are explicit; no classes |
| E4.2 — Awaken through a stone | Use the one concept stone with the whole affinity set affecting the result | Uncertain supported ability occupies one owning-affinity slot; rarity affects bounded quality; invalid outcome consumes nothing |
| E4.3 — Receive distinct recognition | Earn one title and one generated achievement | Title applies its buff; achievement creates its budgeted item prize; narration reflects actual history |
| E4.4 — Select an earned variant | Meet a meaningful-use and earned-record prerequisite, then choose an upgrade | Award alone does not upgrade; selling the prize does not remove the record; selected variant replaces existing ability within its slot |

**Scope:** G09, G11–G13. At most four awakening candidates total, two rarity bands, one ability variant, one title, and one achievement/prize. The LLM judges thematic fit; code validates mechanical constraints only. No full magic library, extra basic-skill gates, replacement/respec system, or magical business domain.

**Before implementation:** Specify both package kits, supported candidate effects/costs/ranges/durations, the rarity effect budget, title and item effects, the qualifying achievement, and the variant's tradeoff. Keep these inside the experiment's content budget.

**Exit evidence:** Exercise both packages and controlled rarity outcomes; demonstrate correct slot ownership, distinct rewards, and optional earned evolution. Ask whether powers feel history-shaped and worth their limited slots. Review G17's voluntary return-session signal before expanding.

## E5 — Daily quest system and gacha rewards

**Stage:** Conditional P1. **Pillars:** P-A, P-D. **Dependency:** E3 (alchemy system operational; crafting quests require it). **Value:** Complete system-assigned daily objectives for XP and gacha item draws; experience history-reflecting rewards through practice.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E5.1 — Receive daily quests | See three System-assigned quests appear at in-game dawn; read objectives, explicit success conditions, and reward information in the journal | Quests visible in distinct journal category in the System's fourth-wall-breaking voice; each has a stated objective, explicit success conditions, relevant skill, and reward preview; no quest requires a fixed solution path |
| E5.2 — Complete a quest and claim XP | Fulfill the stated objective (crafting, social, or observation) and receive XP reward | XP awarded to player XP track and stated skill; partial completion does not award; a retry of an already-resolved request does not award again |
| E5.3 — Draw from the gacha pool | Receive a gacha draw on quest completion; draw one item from the known pool | Pool contents visible before drawing; draw result uses RNG; item is created in inventory with explicit effects stated at draw time; selling or losing the item does not undo the draw record |
| E5.4 — Observe quest expiry and refresh | Let a quest expire without completing it; observe replacement at next dawn | Expired quest produces no reward, no penalty; three new quests replace the previous set; expired quests do not carry over |

**Scope:** G20. Daily quest categories: crafting (make N items of a given type using G19 crafting), social (fulfill an NPC concern or commitment), observation (visit a location and inspect a condition). No penalty mechanic, streak system, or player-configured quest preferences.

**Before implementation:** Define all three quest-category templates and sample objectives. Define the gacha pool: list every item at each rarity tier (common, uncommon, rare) with explicit effects and gold-value equivalents. Define the fictional System framing (status-window interface, narrator voice, attribution). These must be complete before implementation.

**Exit evidence:** Exercise all three quest categories across multiple in-game days. Verify correct XP awards, gacha draws from the declared pool, and clean expiry/refresh. Ask whether System quests feel like a meaningful addition or an intrusion on free-play intent. Record Kyle's answer as a signal before extending the quest pool.

## E6 — Hidden bonus objectives

**Stage:** Conditional P2. **Pillars:** P-A, P-D. **Dependency:** E5 (quests must exist before bonus objectives can extend them); P1 evidence gate. **Value:** Reward unusual, creative, and accidental play with surprise bonuses that make the player feel seen by the world.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E6.1 — Trigger a hidden bonus | Complete a quest in an unusual, creative, or accidental way and receive an unexpected additional reward | LLM-generated bonus condition was recorded at quest creation (hidden); player's approach satisfied it; bonus XP and/or additional item awarded |
| E6.2 — Verify LLM judgment and budget | Internal: hidden conditions generate cleanly; LLM judgment is consistent; bonus rewards stay within declared budget | Multiple triggered and non-triggered bonuses across different quest types; no bonus rewarded for a routine approach; no budget overflow |
| E6.3 — Evaluate player perception | Kyle reports that bonus felt like recognition of creativity, not random luck | Interview after first triggered bonus; record whether the player understood what they did to earn it (they should not have known in advance) |

**Scope:** G21. Hidden bonus conditions apply to all quest types: System daily quests and organic NPC quests. The LLM generates 1–3 bonus conditions per quest at creation time, each describing an unusual or creative approach (not the default successful path). The LLM evaluates whether the player's actual actions satisfied a bonus condition at quest completion or fulfillment. Rules validate that bonus rewards are within a declared budget (additional XP, one extra gacha draw, or a small named item). No bonus condition is surfaced to the player before or after it triggers — the reward arrives with a brief System notification but without revealing what the condition was.

**Before implementation:** Specify the bonus reward budget: XP amount range, item value ceiling, whether a gacha draw is available as a bonus. Define how bonus conditions are stored and retrieved at evaluation time. Define the System notification style for a triggered bonus — brief and distinct from regular quest completion messages.

**Exit evidence:** At least three triggered bonus objectives across different quest types and approaches. At least three non-triggered completions (to confirm the LLM does not over-award). Confirm no bonus fires on a routine approach that matches the primary success path. Record Kyle's description of what they thought triggered the bonus; this should not match the hidden condition (the surprise should hold).

## Sequence and deferred work

E1 → E2 → P0 evidence gate → E3 → E4 → E5 → P1 review → E6 → P2 review. E3–E6 remain conditional and may be revised after P0; their design dependencies do not justify implementing them early. E5 depends on E3's alchemy system being operational for crafting quest objectives. E6 depends on E5; bonus objectives extend the quest system and cannot exist without it.

All locations are authored; never introduce procedural geography. Hidden rooms, puzzles, traps, and anonymous gifts are later tests, not P0 additions.

Broader generative affinities, abilities, spells, items, traps, titles, and achievements remain vision ambitions. Full production/construction, another settlement, and co-op are not committed epics. Classes are removed; place/domain powers have no scheduled revisit. Public v1.0 and post-launch scope are unset.
