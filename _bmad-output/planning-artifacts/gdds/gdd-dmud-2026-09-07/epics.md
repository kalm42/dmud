---
title: "dmud — GDD Development Epics"
created: 2026-09-07
updated: 2026-09-15
version: "0.8"
status: staged-design-baseline-approved
---

# dmud — Development Epics

Design breakdown accompanying [gdd.md](gdd.md). G IDs refer to its decision register. P0 remains the initial implementation. P1–P9 are individually evidence-gated; approving their designs does not authorize implementing them early. These are design work packages, not estimates, sprint commitments, or technical stories.

## E1 — Enter and act in a small persistent world

**Stage:** P0. **Pillars:** P-A, P-D. **Dependencies:** None. **Value:** Establish a player-authored character, then make an intention produce an explainable, durable consequence in the three-location world.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E1.0 — Begin or continue | Choose New Game or Continue and complete Rowan-led Session 0 | Three save slots behave correctly; categorized inputs and the 8/10/12/13/14 array persist; confirmation starts day 1 at 08:00 without charging Session 0 time and captures the P0 fixture state |
| E1.1 — Discover the small world | Inspect three locations, four named people, exits, inventory, and known circumstances | The player owns one prepared P0 test-fixture pouch containing exactly 10,000 gold and no other gold; descriptions expose only appropriate knowledge and add no world scope |
| E1.2 — Act and transact | Converse, move, give, purchase, and wait through free text | Feasibility, consent, stock, time, and funds govern atomic outcomes; the 1-gold purchase branch and full-pouch gift branch each reload the captured state and never merge; no proactive action suggestions |
| E1.3 — Resolve uncertainty | Understand stakes and attempt the controlled Persuasion check | Presence 14 (+2) + Persuasion 1 against difficulty 12 is 60%; natural 1/20 and no-reroll rules hold |
| E1.4 — Resume and grow | Save/load, gain challenge-dependent XP, level a skill, and allocate an attribute point | Complete restoration, one-time awards, no caps, zero XP on failure and 95%-success checks |

**Exit evidence:** Complete the inspect → move → transact/converse → consequential check → save/load loop, including rejection, interruption, timing variants, natural-roll extremes, and near-threshold growth. E2 supplies the stronger causal-social proof.

## E2 — Make consequences travel through people

**Stage:** P0. **Pillars:** P-A, P-B, P-C. **Dependency:** E1. **Value:** Observe people change plans and act on what they have learned.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E2.1 — Change someone's options | Give Mara the prepared P0 test-fixture pouch containing exactly 10,000 gold and observe a motivated decision | Gift/no-gift comparison reloads the same untouched fixture state, changes feasible plans, and does not prescribe retirement |
| E2.2 — Follow a report | See Tessa later communicate through a real encounter with Ivo | Observation and receipt are separate; no non-witness omniscience |
| E2.3 — Encounter imperfect belief | Experience a changed response to a distorted or doubted report | Belief affects choice while the original event remains unchanged |
| E2.4 — Preserve causality | Resume and ask about earlier events | Plans, commitments, knowledge, and resources survive loading without duplication inside a branch; isolated fixture branches never merge state |

**P0 gate:** Capture one starting state with the player's single prepared P0 test-fixture pouch containing exactly 10,000 gold and no other gold. Reload it independently for the purchase, full-pouch gift, no-gift, and rumor branches; never merge their outcomes. Run three controlled gift/no-gift pairs and at least one rumor variant. Require zero unexplained contradictions or conservation/save failures, then record causal comprehension and believability separately. The P0 fixture and all branch outcomes are discarded before later-stage economy tests.

## E3 — Make resources and effects authoritative

**Stage:** Conditional P1. **Pillars:** P-A, P-D. **Dependency:** P0 gate. **Value:** Establish the shared mechanical language used by deprivation, crafting, spells, items, and combat.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E3.1 — Have three resource pools | See current/base/effective maximum Health, Mana, and Stamina | Formulas, growth, absolute deficits, clamps, save/load, and death at 0 Health match G22 |
| E3.2 — Exert and recover | Pay Stamina for strenuous actions and recover through rest | 0/5/10/20 bands, full-cost rejection, 0-Stamina restrictions, and 10-minute recovery are exact |
| E3.3 — Receive a bounded effect | Gain an authored or generated buff/debuff whose mechanics remain stable | The LLM may propose target, shape, duration, magnitude, and presentation within the source budget; validation and stable identity match G24 |
| E3.4 — Stack and remove effects | Experience Stack, Refresh, Replace, opposing modifiers, and causal treatment | Arithmetic order, minimums, linked removal, expiration, and persistence remain correct |
| E3.5 — Understand known effects | Inspect known mechanics and observe symptoms of unknown effects | UI reveals only justified source, stack, duration, mechanics, and removal knowledge |

**Controlled fixtures:** Sharpened, Bleeding, simultaneous +25%/−25%, diagnostic-only Star-metal Edge (+20 damage on the next successful hit within 10 minutes from rare artifact-grade oil), every tier/shape ceiling, and one-above-limit invalid proposals. Verify the declared same-timestamp order for completion, ticks/thresholds, expirations/transitions, recalculation/clamps, and death. P1 excludes hunger, sleep, access, autonomous livelihood, alchemy, spells, and combat.

## E4 — Make places physically accessible

**Stage:** Conditional P2. **Pillars:** P-A, P-B. **Dependency:** P1 gate. **Value:** Make possession, permission, locality, intrusion, and evidence causal rather than abstract.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E4.1 — Enter by right | Use permission or a matching key and share a capacity-two bed | Ownership gives no remote use; physical access and capacity govern use |
| E4.2 — Pick a lock | Attempt a 60-second Agility + Sleight check at difficulty 12 | Failure consumes one pick; another owned pick allows another fully resolved attempt |
| E4.3 — Force entry | Spend 30 seconds and 10 Stamina on Body + Athletics difficulty 14 | Every attempt is loud; success leaves the door broken/open; paid retries remain possible |
| E4.4 — Take local property | Remove one fungible serving and one distinctive marked object | Physiological/physical use succeeds despite ownership while property truth persists |
| E4.5 — Learn through evidence | Observe absence, compare memory, form a hypothesis, and possibly accuse | Unseen theft grants no knowledge; suspicion needs a cause and may be wrong |

**Controlled fixture:** Ivo's Home, its four door states, Ivo and permitted guest Mara's keys, one bed, one food serving, and one marked object. Save/load preserves possession, access, permission, event history, observations, and beliefs. Formal policing is excluded through P9.

## E5 — Live with hunger and fatigue

**Stage:** Conditional P3. **Pillars:** P-A, P-B. **Dependency:** P2 gate. **Value:** Let food, sleep, shelter, and deliberate neglect matter through transparent causal consequences.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E5.1 — Become Starved | Go 24 hours without a completed serving and accrue further daily stacks | Each stack multiplies effective max Health by 0.75, rounds, clamps current without damage triggers, and persists |
| E5.2 — Eat and recover capacity | Eat any complete serving, including expired food | Hunger timer resets and one Starved stack is removed; restored maximum does not heal current Health |
| E5.3 — Become Exhausted | Go 24 hours without adequate sleep and accrue further daily stacks | Effective max Stamina, clamp, and removal mirror Starved; 0 Stamina is restrictive but not lethal |
| E5.4 — Sleep adequately | Complete uninterrupted eight-hour sleep in a usable bed and protected place | Timer resets, one stack is removed, and Stamina fills to the new effective maximum; interrupted/unsafe sleep fails qualification |
| E5.5 — Prepare varied food | Eat raw cabbage or use recipe-specific tools, time, Stamina, and ingredients | Six fixture recipes produce exact yields and fresh batch expiration timestamps |
| E5.6 — Risk spoiled food | Consume expired food and resolve a Constitution check | Hunger is satisfied regardless; overdue fraction determines probability, nearest-achievable difficulty, XP, and sickness tier |

**Scope:** G26. Hunger and effect timers continue during sleep; inadequate sleep still receives ordinary short-rest Stamina recovery. P3 does not force player action and includes no nutrition/macronutrients, storage modifiers, or ingredient-age inheritance.

## E6 — Let needs become plans

**Stage:** Conditional P4. **Pillars:** P-B, P-C. **Dependency:** P3 gate. **Value:** Observe an NPC satisfy needs through work, money, access, preparation, and recovery instead of resource abstraction.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E6.1 — Watch priorities change | See Ivo's hunger/sleep pressures compete with obligations and immediate threats | Thresholds change priority; after Starved, only an immediate threat outranks food while personality, knowledge, resources, and risk still select the plan |
| E6.2 — Earn rather than receive money | Ivo completes Tessa's four-hour courier shift for 3 gold | Payment transfers only at completion and only from Tessa's finite 12-gold business budget |
| E6.3 — Obtain and prepare food | Ivo buys a 1-gold cabbage, prefers feasible stew, or eats it raw | Stock, gold, location, access, tools, time, Stamina, and ingredients all reconcile |
| E6.4 — Sleep after eating | Ivo reaches his bed and completes adequate protected sleep | The plan physically traverses every required step and satisfies P3 rather than clearing needs abstractly |
| E6.5 — Replan after failure | Work, funds, stock, hearth, protection, or access becomes unavailable | Ivo chooses another feasible known plan; risky trespass/theft/force is eligible only when character and circumstances support it |
| E6.6 — Continue off screen | Let game time advance while Ivo is elsewhere | Identical inputs yield the same resource/time/consequence chain; the player learns only through plausible contact or observation |

**P4 gate:** Begin Ivo at 0 discretionary gold and 12 hours since meal/sleep. Prove the successful loop plus every declared failure branch without inventing stock, money, access, or outcomes and without adding a fifth NPC.

## E7 — Secure Brackenford's future through play

**Stage:** Conditional P5. **Pillars:** P-A, P-B, P-C. **Dependency:** P4 gate. **Value:** Sustain four households and develop personal alchemy through ordinary causal activity.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E7.1 — Understand community pressure | Inspect protection, meals, sleep, household streaks, and commitments | Known facts are concrete; warnings interrupt waits at three and one ward-days remaining |
| E7.2 — Sustain households | Fulfill three consecutive lived-stability days by mixed supported means | Every resident actually eats, sleeps safely, and avoids Exposed; only a failing household resets |
| E7.3 — Protect or relocate | Repair the ward, fund patrol, relocate, host, or support another valid plan | Actual resources, labor, acceptance, local access, and commitments govern success |
| E7.4 — Craft and apply alchemy | Use known recipes and the bruised-duskroot uncertainty fixture | Inputs, tools, time, checks, outputs, failures, item effects, and XP commit atomically |
| E7.5 — Progress a craft track | Reach a production threshold and adopt or defer a revealed recipe | Only successful distinct crafts count; adoption adds rather than replaces recipes |

**P5 gate:** Complete two plausible community routes and one unplanned supported route, plus successful and failed crafts and one applied product. Automatic daily food loss is forbidden; ward expiry changes protection only.

## E8 — Earn a distinctive affinity spell

**Stage:** Conditional P6. **Pillars:** P-D, P-A. **Dependency:** P5 gate. **Value:** Choose a small build, receive a bounded history-shaped awakening, and earn an optional evolution.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E8.1 — Choose an affinity package | Choose Ember + Fellowship or Vessel + Fellowship | Listed skills, starting spells, Mana costs, and two slots per affinity apply; basic skills stay universal |
| E8.2 — Awaken through a stone | Receive one uniformly selected package candidate from a retained 80/20 rarity | Slot ownership and mechanics are fixed; generated name/manifestation reflects history without changing them |
| E8.3 — Receive recognition | Earn Brackenford's Anchor and Rest Is Part of the Work/Copper Sandglass | Title buff and achievement prize remain distinct and persist independently of item possession |
| E8.4 — Select an earned variant | Meet three-use and achievement prerequisites and choose Deepened | Exact tradeoff is revealed before confirmation; replacement consumes no extra slot |

## E9 — Daily quest system and gacha rewards

**Stage:** Conditional P7. **Pillars:** P-A, P-D. **Dependency:** P6 gate and operational alchemy. **Value:** Test whether explicit LitRPG objectives complement free play.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E9.1 — Receive daily quests | See crafting, social, and observation quests at 06:00 | Exactly three slots show explicit success conditions, relevant skill, and reward |
| E9.2 — Complete once | Fulfill a quest for 25 player XP, 25 skill XP, and one draw | Partial or repeated resolution cannot pay twice |
| E9.3 — Draw from the known pool | Receive one item using 70/25/5 tier odds and uniform in-tier selection | Pool is visible beforehand; result/effect is explicit and persists |
| E9.4 — Expire and refresh | Leave a quest incomplete until the next 06:00 | Replacement is clean and carries no penalty, streak, or multiplier |

## E10 — Hidden bonus objectives

**Stage:** Conditional P8. **Pillars:** P-A, P-D. **Dependency:** P7 gate. **Value:** Reward unusual or creative play without revealing a checklist.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E10.1 — Trigger a hidden bonus | Complete a supported quest unusually and receive an unexpected bounded reward | One private stable condition existed at creation; committed evidence satisfies it; it pays once |
| E10.2 — Avoid arbitrary rewards | Complete quests through routine or nonqualifying methods | No over-award, budget overflow, or retroactive trigger invention occurs |
| E10.3 — Interpret the surprise | See the fixed notification and reward, not the condition | Player inference is recorded without confirmation or denial |

## E11 — Resolve a bounded combat encounter

**Stage:** Conditional P9. **Pillars:** P-A, P-D. **Dependencies:** P1 resources/effects, P2 access, P5 items, P6 spells, and P8 gate. **Value:** Fight, flee, or surrender while every cost and consequence remains understandable and durable.

| Story | Player outcome | Evidence |
| --- | --- | --- |
| E11.1 — Enter and read combat | Encounter the road robber at 10 m and understand order, positions, pools, and actions | Initiative uses Agility; six-second rounds and current/effective maximum pools are visible |
| E11.2 — Move, attack, defend, and cast | Use melee, ranged, defend, movement, and Cinder Lance | Stamina/Mana costs, range, Defense, damage, misses, and atomic commitment match G23 |
| E11.3 — Use effects and items | Bleed, sharpen, recover, or apply another supported effect | Shared P1 rules govern magnitude, stacking, duration, removal, and persistence |
| E11.4 — Die or revive | Reach 0 Health or use a supported revival within its declared window | Death is immediate at 0; there is no Downed/stabilization interval; save recovery remains available |
| E11.5 — Choose an exit | Defeat, escape, accept surrender, or surrender | Time, transfer, one-time rewards, XP, and post-combat state reconcile and persist |

**P9 gate:** Complete every exit plus insufficient-resource, miss, effect, death/revival, and mid-combat save/load cases from controlled saves. No tactical map, party, enemy generation, equipment progression, or combat quest is added.

## Sequence and deferred work

E1 → E2 → P0 gate → E3/P1 → E4/P2 → E5/P3 → E6/P4 → E7/P5 → E8/P6 → E9/P7 → E10/P8 → E11/P9. Every stage includes its controlled fixture, a failure/recovery route, save/load, and one unplanned supported approach before expansion.

All locations are authored. Broader configurable/generated effects, affinities, spells, items, traps, titles, achievements, skill-practice-shaped variants, enemies, equipment, and encounters remain later ambitions. Detailed food storage, nutrition, formal policing, full production/construction, another settlement, difficulty modes, co-op, public-v1.0 scope, and a post-launch roadmap are not committed epics. Classes are removed; place/domain powers have no scheduled revisit.
