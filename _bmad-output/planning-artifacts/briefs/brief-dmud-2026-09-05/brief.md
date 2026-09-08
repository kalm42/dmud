---
title: "dmud — A World That Remembers"
status: approved
approved_scope: game vision and working defaults
created: 2026-09-05
updated: 2026-09-05
---

# dmud — A World That Remembers

Kyle approved the first vision and its working defaults on 2026-09-05. This revision incorporates his progression preferences. Detailed examples, accepted defaults, and explicitly marked new proposals live in [addendum.md](addendum.md). Exact mechanics remain for detailed design.

## Vision and purpose

**Live a self-directed fantasy life in a world where your actions have lasting, rule-governed consequences, people pursue their own goals, and your abilities grow into a reflection of your history.**

dmud is a solo, text-based RPG with the freedom of a tabletop campaign, the progression of LitRPG, and a persistent simulated world. An LLM acts as dungeon master: interpreting intentions, playing NPCs, proposing consequences, and narrating results. Code runs the rules, rolls dice, and maintains world state. NPCs remember, make choices, and spread fallible accounts of events. Their conflicts create quests around a central problem with multiple possible solutions.

This begins as Kyle's personal prototype. Friends are the first potential playtesters; public release depends on whether it proves fun. Small-party cooperative campaigns are a later ambition, contingent on solo success.

## Player experience and pillars

1. **Creative actions have consistent consequences.** Describe what you want to attempt. Skills, circumstances, resources, and dice determine what happens; established facts persist.
2. **People have lives beyond you.** NPCs have motives, obligations, relationships, and limited knowledge. Giving someone a fortune changes their choices and can change their life.
3. **Reputation travels through people.** Witnesses tell others, stories change, and some news never reaches the next settlement. Beliefs influence behavior without rewriting reality.
4. **Your history shapes your power.** Chosen affinities, rare discoveries, and meaningful practice personalize a limited ability set. Titles grant buffs; achievements award item prizes. Either can be a prerequisite for future ability upgrade options; harder accomplishments can reveal hidden choices. Progression should make the player feel accomplished and special. Achievements retain a funny, opinionated voice.

**Core loop:** discover a situation → form a plan → act or converse → resolve uncertainty → encounter changed people and circumstances → develop abilities and choose what matters next.

**Audience:** adult tabletop roleplayers and LitRPG readers who enjoy experimenting, building a character, and following consequences through dialogue. Aim for satisfying 20–60-minute sessions with easy save/resume. Player curiosity drives the experience; simulation should yield understandable choices and surprises.

## World and direction

Begin in Brackenford, a frontier settlement whose protective ward is deteriorating. Its residents disagree about repair, control, and whether to leave. The campaign's central problem is securing a viable future for the community. Repair, negotiated protection, organized relocation, or another engine-supported solution can succeed when it meets explicit safety and livelihood conditions. The detailed victory conditions belong in the game design document.

The world continues after victory. NPCs remain emotionally credible; achievement announcements supply mischievous commentary. Presentation is readable text, dialogue, character sheets, and an optional roll log; graphics and audio are unnecessary for the prototype.

## Rules, magic, and emergence

Everyone has universal basic skills, using D&D 5e's skill categories as a reference, with differing proficiency. These skills do not consume affinity slots. Use a small original dice system, initially a d20 plus attribute and relevant skill against a difficulty set before rolling. Roll when uncertainty and stakes justify it. Routine feasible actions succeed; impossible actions receive an explanation. Failure can consume time, resources, or opportunity and change relationships. Start with recoverable defeat and manual saves.

The LLM maps intent to mechanics, judges thematic fit, and interprets results. The engine enforces mechanical constraints, rolls dice, commits changes, then supplies facts for narration. Thematic consistency belongs to the LLM; code does not validate affinity-to-concept compatibility. Generated configurations combine supported effects with explicit costs and limits; new underlying mechanics require engine work.

Players choose discovered affinities and their combinations. Their rarity is substantially random and linked to quality. Each affinity has a limited number of spell/special-skill slots. An awakening stone expresses its concept through one affinity, awakening an ability into an available slot, with chance influencing which ability emerges. The full affinity set shapes that ability to fit the character concept as well as the stone's concept; rarity influences possible outcomes. Practice and earned evolution develop existing abilities separately.

Affinities supply special abilities and bonuses without a separate class system. Titles provide buffs, while achievements provide item prizes. Either can be required to unlock future ability upgrade options, including stronger hidden choices; unlocking an option does not automatically grant the upgrade. A craftsperson or proprietor can earn distinctive utility powers alongside combat paths. Exact rarity curves, slot counts, and unlock rules remain open.

Quests arise from unmet needs, conflicts, and agreements. Player businesses participate in material supply and customer choice. The full ambition includes harvesting, construction, production, competition, and NPC livelihoods.

## Inspirations and boundaries

These references inform the vision; all except Dwarf Fortress were supplied by Kyle. Place-based powers are deferred; the reference is preserved in the addendum.

| Reference | Direction to carry forward | Outside this first vision |
| --- | --- | --- |
| Tabletop RPGs / D&D 5e | Creative adjudication, dice, universal basic skill categories | Adopting the entire ruleset or a fixed adventure path |
| Dungeon Crawler Carl | Achievement personality and comic recognition | Its setting, plot, or exact narrator voice |
| He Who Fights With Monsters | Stone concepts influence which abilities awaken through an affinity; the whole build shapes results; slots are limited per affinity | Assuming exact novel rules must be reproduced |
| Azarinth Healer | Hard accomplishments reveal stronger advancement options; apply this to affinities and abilities | A class system or copied unlock conditions |
| Kingdom Come: Deliverance 2 | Kyle's wish for grounded NPC lives and consequential gifts | Graphics or claims that its NPC simulation already meets this vision |
| Dwarf Fortress | Additional comparison for persistent histories and social information | Its full simulation breadth as prototype scope |

## Minimum proof and staged scope

Build for a desktop browser, initially run locally, with one developer and AI assistance. Use an action-based game clock: travel, work, rest, and consequential interactions advance time; offline time does not. Budget, availability, and delivery dates remain unknown.

**Minimum proof:** one settlement, three locations, four named NPCs, one social conflict, and a small set of engine-supported actions: conversation, movement, giving, purchasing, waiting, and one uncertain skill check. Prove that a large gift changes an NPC's feasible plans and observable behavior, that a witness's report travels through an actual encounter, and that the effects survive save/load. This experiment proves the causal-world foundation; it does not establish the entire game is fun.

**Next playable slice:** add one resolvable community problem, a competing drink stall, a small magic choice, one earned affinity-ability evolution, and a generated achievement. Use the slice's progression content to test an achievement prerequisite and an awakening outcome; detailed scope is in the addendum. Test with Kyle and interested friends. Expand to construction chains and wider regions only after this slice earns repeat play. Consider cooperative campaigns after solo play works.

## Risks and decisions to revisit

The central risks are inconsistent adjudication, NPCs that only pretend to remember, unlimited content becoming unbalanced, simulation obscuring useful feedback, and LLM latency or cost interrupting play. Evaluate these through persistent consequences, repeated rule checks, observed NPC choices, understandable cause and effect, and measured session cost and response time.

The setting, core magic direction, dice model, time model, failure policy, and staged prototype are accepted working defaults. Exact victory conditions, rarity probabilities, ability limits, achievement prerequisites, acceptable latency/cost, and a realistic schedule remain open. No implementation stack or release commitment has been selected.
