# Design depth and options

Companion to the approved game vision in [brief.md](brief.md). Kyle accepted the original assumptions on 2026-09-05. Those choices are now working defaults; explicitly provisional numbers and open details remain provisional. New **[PROPOSAL]** sections distinguish further design suggestions from accepted direction. This is not a detailed implementation plan.

## Confirmed direction after discovery

Solo play comes first. A small cooperative campaign is a desirable later expansion if the concept works. This is initially a personal prototype, with interested friends as potential players and public release conditional on fun. Kyle requested a complete first vision with assumptions for correction and added **He Who Fights With Monsters**, especially its magic system, as an inspiration. Kyle subsequently confirmed affinity choice, substantially random rarity linked to quality, awakening stones whose rarity influences special abilities, and a limited spell/skill set. He added **Azarinth Healer** for achievement/title prerequisites that reveal stronger advancement options behind harder accomplishments; the current design applies this to ability upgrade options. Titles grant buffs; achievements award item prizes. Either can be a prerequisite for a future option, without automatically granting that upgrade. Classes have been removed, place-based powers deferred, and thematic judgment assigned to the LLM. Universal basic skills follow the D&D 5e skill-list model and are separate from awakened abilities. The desired feeling is earned distinction: the player feels accomplished and special.

## User-contributed scenarios

### The 10,000-gold test

The player gives an NPC enough money, in the user's example, to live on for the rest of their life. The interesting question is what that particular person does next. Wealth should affect their opportunities and decisions. Retirement is only one possibility; behavior must follow their wants, obligations, and circumstances. The motivating experience was a gift in Kingdom Come: Deliverance 2 after which the user observed no meaningful change.

### Building a competing bar

The player wants to cut trees, mill timber, construct a building, brew beer or distill liquor, and operate a bar. Materials and production connect to the world economy. NPC customers choose whether to buy; an established competitor can retain their loyalty. The player must find ways to attract customers. Existing bartenders also have reasons to work and use income to obtain stock.

### Fallible social knowledge

Witnesses tell friends, who pass the story to their own friends. News can spread, stall, or change along the way. An account arriving in the next town may be distorted, and some events never become known there. NPC dialogue must reflect what that speaker actually witnessed or learned.

### Generative game content

The LLM should have configuration mechanisms for affinities, abilities, spells, items, traps, achievements, titles, and other content. Frequently practiced skills can develop into better, individualized versions. Rewards should fit the player's history. NPC conflicts and the central world problem should create emergent quests without a fixed plot.

## Accepted system foundations

These working defaults preserve the requested LLM interpretation loop while keeping authoritative world changes under mechanical engine validation. The LLM alone judges thematic appropriateness; no code-based thematic restrictions are required. Detailed schemas and algorithms remain implementation choices.

### Rules and language boundary

Have the LLM propose an interpretation and a structured action using supported game operations. The engine validates prerequisites, stakes, costs, and the check before rolling. Where practical, define the mechanical consequences of success and failure before rolling. The LLM can propose contextual consequences afterward, but all world changes pass validation and commit through the engine before narration describes them as facts. This preserves the user's intended interpret → roll → interpret loop while protecting continuity.

Separate attempted actions from spoken claims: a player saying they own a building does not make them its owner. Failed validation should request a revised proposal or a clarification; it must not partially mutate the world. Retries must not spend resources or roll again unintentionally.

The content system could compose existing operations such as damage, movement, resource transfer, status application, item creation from materials, and changes to relationships. New combinations are generative; genuinely new mechanics still need an engine capability. This distinction bounds the promise of unrestricted intent without pretending to simulate every possible action.

### Three distinct records

- World facts: what actually happened, ownership, resources, positions, and other authoritative state.
- NPC beliefs: direct observations and received claims, including source, time, confidence, and distortions.
- Presentation: dialogue and narration drawn from the relevant facts and beliefs.

Rumor mutation changes beliefs, not historical truth. Gossip needs contact opportunities and motives to transmit, not an automatic broadcast to every NPC. Truthful information is not automatically believed, and a true belief does not automatically force a particular action.

### NPC agency without constant LLM calls

Represent needs, obligations, preferences, relationships, resources, and current plans explicitly. Routine schedules and purchases can run in code. Use LLM judgment for consequential replanning and dialogue. Memory retrieval supplies relevant observations and beliefs; memory must affect decisions, not only conversational recollection. NPCs may conceal motives or lie while remaining consistent with their own knowledge.

Abstract distant activity carefully. A distant NPC must not lose money, memories, or agency merely because the player cannot see them. For the solo prototype, advance their activity on the same game clock as the player's actions; pause that clock between sessions.

### Personalized progression

Treat mechanics and expressive language separately: track meaningful behavior in code, generate names and flavor from that history, and validate mechanical rewards within power limits. Proposed eligibility should distinguish meaningful practice from endlessly repeating a trivial action. Generated achievements can have their own comic voice while NPC lives retain emotional credibility.

## First campaign premise

Brackenford's protective ward is weakening. Maintaining it competes with immediate needs for food, shelter, and income. A shopkeeper wants safe trade, a craftsperson wants overdue wages, and someone with family elsewhere thinks relocation is the sensible option. None needs to be a villain for their interests to collide.

The campaign asks: **Can this community secure a viable future?** The engine should track concrete conditions for safety and subsistence; the game design document will define thresholds and the duration over which they must hold. Fixing the ward is one route. Recruiting capable protectors, negotiating a workable arrangement, or establishing a safer home may also qualify when represented by the rules. Narration alone cannot declare victory.

Pressure develops on game time and is communicated through observable events. A sudden deadline should not make building a business an obviously foolish way to play. Stabilizing supply, earning trust, or funding protection can contribute to the central problem. The world remains playable after success; the player sees how people adapt.

This original premise is the accepted starting scenario for testing open solutions. It does not prescribe a sequence of quests. A fixed starting situation supports comparison between runs; NPC plans and player interventions determine what follows.

## Universal basic skills

Everyone has access to the same basic skill categories, with different ratings or proficiency. These describe ordinary attempts and do not occupy affinity slots. Skills do not require an awakening stone, affinity, title, or achievement to become available. Access does not guarantee that an action is feasible or successful; circumstances, knowledge, equipment, training, and the rules still matter.

Use the D&D 5e skill list as the starting vocabulary: **Acrobatics, Animal Handling, Arcana, Athletics, Deception, History, Insight, Intimidation, Investigation, Medicine, Nature, Perception, Performance, Persuasion, Religion, Sleight of Hand, Stealth, and Survival.** The official rules also distinguish making a skill-related check from having proficiency in it. [D&D Free Rules — Skill Proficiencies](https://www.dndbeyond.com/sources/dnd/br-2024/playing-the-game#SkillProficiencies)

This adopts the model and reference categories, not the entire D&D ruleset. The earlier four provisional attributes are not silently replaced by D&D's six; mappings, starting ratings, training, and any additional crafting categories remain detailed-design decisions. The minimum prototype can exercise only the categories its actions need without introducing skill-unlock gates.

Use **basic skill** for universal capabilities and **affinity ability** for an awakened spell or special skill. Affinities can supply special abilities and bonuses, including mechanically defined modifiers to basic-skill checks. Exact bonus growth remains open. Everyone can attempt to sneak using Stealth; a supernatural concealment ability requires the relevant acquired power.

## Magic and character identity

The accepted magic direction combines deliberate affinity selection, uncertain discoveries, rarity linked to quality, awakening stones, a limited ability set, and practice-driven personalization. Azarinth Healer inspires achievement/title prerequisites for affinity and ability advancement; no class system remains. These are Kyle's desired design qualities; this document does not claim exact equivalence to either novel's mechanics. The following affinity example is original to dmud.

Characters discover and bind a limited set of **affinities**, provisionally three. Their combination suggests a unifying identity and a bounded family of abilities. Discovery offers meaningful build choices; practice, training, and consequential use influence later variants. Each affinity owns a limited set of slots for spells or special skills. Awakening fills an available slot on one affinity; the entire affinity combination influences the ability that emerges. Unlocking new powers and improving existing powers are distinct events. Universal basic skills remain available to everyone regardless of affinity choices and consume no affinity slots.

For example, **Ember + Vessel + Fellowship** could suggest **Hearth**. One player develops protection and recovery for companions around a campfire; another develops precise heating, preservation, and hospitality skills through running an inn. These outcomes share a theme but respond to different histories. They illustrate the accepted direction; exact effects, costs, targets, duration, and progression limits remain to be designed.

The engine records evidence for advancement. The LLM proposes a fitting evolution and explains how it follows from that evidence. Validate the evolution before offering or granting it. Repeating a trivial action indefinitely should not supply unlimited growth. A more powerful variant may add a tradeoff or specialization; advancement need not be a universal numerical increase.

For the first playable slice, retain one choice between two small affinity packages and one earned variant. Full combinations, numerous ranks, and a broader library of generated abilities come later. Affinity count, slot counts, rarity probabilities, awakening procedure, permanence of choices, and respecialization remain open. Rarity-linked quality, rarity-influenced awakening outcomes, limited abilities, and achievement/title prerequisites are confirmed requirements; exact novel rank names and counts are not.

## Progression through choice, discovery, and accomplishment

### Confirmed requirements

- **Affinity selection provides agency.** Players choose which discovered affinities to build around. Their rarity is substantially random and tied to quality.
- **Awakening stones express concepts.** A stone awakens a spell or special skill embodying its concept through one of the character's affinities. The full affinity set influences the result so it also fits the character concept. The exact ability is not guaranteed; rarity influences the possible outcomes.
- **Capacity belongs to each affinity.** Each affinity has a limited number of spell/special-skill slots. An awakened ability belongs to one affinity and occupies one of its available slots. Scarcity makes each acquisition and upgrade meaningful.
- **Titles grant buffs.** A title can also be a prerequisite for unlocking future ability upgrade options.
- **Achievements award item prizes.** An achievement can also be a prerequisite for unlocking future ability upgrade options. Harder accomplishments can reveal stronger hidden choices. Prerequisites are defined per upgrade; neither award type must unlock an option every time.
- **Progression should feel earned and distinctive.** The player should recognize that a special opportunity follows from something they actually accomplished.

These combine the user's selected qualities from He Who Fights With Monsters and Azarinth Healer. No exact rarity ladder, probability table, or ability count is adopted from either work. Affinities provide special abilities and bonuses without a separate class layer.

### How the parts could fit [PROPOSAL]

| Part | Decision or uncertainty | Proposed mechanical role |
| --- | --- | --- |
| Affinity | Choose among discovered themes and qualities | Owns limited ability slots; contributes its theme to the complete character concept |
| Affinity rarity/quality | Engine rolls from a source's configured distribution | Improves a defined quality budget or potential; exact advantage remains to be chosen |
| Awakening stone | Choose a concept and rarity; exact ability remains uncertain | Awakens its concept through one affinity with capacity, shaped by the entire affinity set |
| Title | Earn a title | Grants a mechanically defined buff; may satisfy a future ability-upgrade prerequisite |
| Achievement | Earn an achievement | Awards an item prize; may satisfy a future ability-upgrade prerequisite |
| Practice | Use abilities in meaningful situations | Improves mastery and contributes evidence toward personalized variants |

Keep the rarity roll in the engine, with a recorded result. A source's location, danger, or history could affect its distribution while preserving uncertainty. Higher rarity should have a defined quality benefit, honoring the desired connection, but compatibility and intended use can still make a lower-rarity option valuable. Rarity can influence eligible categories, quality, or probability, but does not guarantee a specific spell or special skill. The exact relationship remains to be designed.

For awakening, the LLM creates candidate abilities using the stone concept, entire affinity set, and character concept. Its judgment determines thematic fit. Assign each candidate to one affinity with an available slot; the engine validates only mechanical effects, capacity, costs, and explicit prerequisites, then rolls among mechanically eligible candidates. This proposed joint roll chooses an ability and its owning affinity together; whether the player instead selects an affinity first remains open. The LLM can compose candidates, but it should not make a failed prerequisite disappear because an ability sounds appropriate. Finding a rare stone and earning a hard achievement can unlock different dimensions of progression, so buying one resource need not bypass every accomplishment requirement. Exact prerequisite combinations remain open.

### Limited abilities, flexible actions [PROPOSAL]

Apply the confirmed per-affinity slots to awakened spells and special skills. Ordinary competence can still support attempts such as climbing, bargaining, or tending a fire. Everyone has the universal basic skills; training and ratings differentiate effectiveness. Basic skills are not unlocked by stones, affinity slots, or achievements. Advancement details remain for the game design document.

Define abilities by supported effects and constraints so players can apply them creatively. Heat control could support warming a shelter, maintaining a brewing temperature, or causing a distraction when its targets, range, output, and costs permit. A creative use does not automatically require learning a separate spell.

Favor upgrades that evolve or replace an existing ability over continually adding slots. Whether players can replace, retrain, or preview irreversible choices is open. Permanent foundational choices plus random awakening can otherwise make an unlucky discovery dominate a long campaign; address that tradeoff explicitly when defining the rules.

### Hidden advancement with consistent requirements [PROPOSAL]

Store achievement/title eligibility as validated conditions over recorded events and state. For mechanically consequential unlocks, register and version those conditions before evaluating eligibility. The engine determines whether the player met them; the LLM supplies fitting names, descriptions, and compatible reward proposals. Flavor narration can remain flexible, but an actual title has a buff and an actual achievement has an item prize; both require validated mechanical rewards.

Hide some options from the player while preserving their requirements in the engine. Decide which unlocks are entirely secret, which are hinted at by mentors or stories, and which expose progress. Once an option is earned, show how the accomplishment relates to it so the reward feels deserved. Do not require every hidden condition to be announced beforehand.

An NPC may know a rumored route to a rare affinity or ability upgrade and pass it on incompletely or incorrectly. This makes the existing information system useful to progression. NPC belief does not alter the underlying prerequisite. Practical experimentation or a reliable source can reveal which part of the rumor is wrong.

Different difficult accomplishments should support different identities: protection, exploration, diplomacy, craft, trade, and combat. The engine needs relevant evidence of challenge and outcome; a counter for repeated trivial actions is insufficient. An achievement always has an item prize, but need not unlock an ability upgrade. A title has a buff, but likewise need not unlock an upgrade. Not every major accomplishment needs a joke.

### Original example: earning an upgrade [PROPOSAL]

A character with Ember, Vessel, and Fellowship keeps companions safe through a dangerous storm while heat and provisions are scarce. Recorded danger, resource pressure, and outcomes establish the accomplishment. The achievement **Last Light** awards an item prize, such as a well-made lantern, and can also satisfy a prerequisite that reveals a stronger upgrade option for an existing ability. No class is awarded.

Separately, a **Rest** stone awakens a new ability into an available affinity slot. The LLM interprets Rest through the complete affinity set; the engine validates mechanical limits and rolls the result. Neither this stone nor the achievement promises a specific named awakening. Earned evolution and new awakening remain distinct progression events.

### One stone, several coherent possibilities [PROPOSAL]

For the Ember + Vessel + Fellowship character, a **Rest** stone might produce one of these original candidates. Every row uses the complete warmth-and-companionship character concept while assigning the resulting ability to a specific affinity.

| Owning affinity | Possible awakening | Fit with the stone and character |
| --- | --- | --- |
| Ember | Banked Warmth | Maintains warmth around sleeping companions, with fuel and output limits |
| Vessel | Held in Repose | A bounded recovery effect on a resting target, with explicit duration and costs |
| Fellowship | Ease the Weary | Influences a gathering's emotional state toward calm, with explicit strength and resistance rules |

These are possible outcomes, not a player-facing spell menu or guaranteed rewards. A different affinity combination should yield a different set or weighting of abilities from the same Rest stone. An affinity with no remaining slots cannot own the new result. What happens when no valid slot or candidate exists must be defined before a stone can be consumed; refusing the attempt without consumption is the proposed default.

The LLM judges how a candidate expresses the stone concept, owning affinity, and complete character concept. Code validates ownership, capacity, costs, effect types, numerical limits, and explicit mechanical prerequisites. It does not validate thematic compatibility, require affinity-to-effect mappings, or run a separate theme classifier. Character history can inform the LLM's interpretation. Playtest feedback can improve that interpretation without becoming a code-based thematic gate.

## Titles, achievements, and rewards

Titles and achievements have distinct direct rewards. Titles grant buffs; achievements award item prizes. Both may be referenced by future ability-upgrade prerequisites. Neither inherently grants the other, and neither automatically applies an unlocked upgrade. The prerequisite references the earned title or achievement rather than possession of the prize item.

**[PROPOSAL] Title example:** *Steady Hand* grants a bounded bonus on qualifying precision checks and may be a prerequisite for a future affinity-ability upgrade. Exact eligibility, bonus, duration, stacking, and whether buffs require an active title remain open.

If an NPC actually leaves an unwanted job after receiving the player's gift, a generated achievement might read:

> **Unscheduled Retirement**
> You gave someone enough money to quit. Their employer has classified you as a natural disaster.

The comment is comic exaggeration, not an authoritative claim that the employer has taken an action. A real reaction must follow the employer's knowledge and choices. The achievement's eligibility depends on the recorded gift and resignation, rather than being awarded merely because the player typed an intention. This achievement also awards an item prize, for example a durable traveling cloak. The item is an illustrative proposal, not a fixed reward. Title buffs and achievement items must have mechanically defined effects within their reward budgets. NPC-funded quest rewards come from resources they own or can credibly promise; system-granted rewards have explicit creation rules.

## Time, interaction, and rules

Use game time rather than real-world elapsed time. Actions with fictional duration advance a shared clock: travel, crafting, shopping, waiting, and rest. Reading menus and inspecting known information do not. Conversation advances time in coherent exchanges; the exact granularity is a design choice. Large time skips stop at events that reasonably require player attention. Plans and rumors continue during elapsed game time, including at places the player is not visiting.

Use a small custom d20 system first. Candidate attributes are Body, Finesse, Mind, and Presence, with a small skill list selected for the prototype's actual actions. They are placeholders, not a complete character sheet. Resolve genuinely uncertain, consequential attempts; do not require a roll for every sentence or routine purchase. Social success can change willingness or secure an agreement within an NPC's motives and constraints; it does not automatically compel obedience.

Before consequential action, communicate what the character can reasonably understand about the attempt and its risks. Exact hidden facts need not be exposed. Show rolls and modifiers in an optional inspection view. If an interpretation would spend a rare resource or take a materially different action, ask the player to clarify. A failed attempt cannot be retried without limit under unchanged circumstances unless the rules explicitly allow it.

When a plausible idea lacks a direct rule, try composing supported operations. If the missing capability changes stakes or persistent consequences, explain the limitation and offer the closest supported approach rather than narrating an unrecorded success. Record such ideas as candidates for expanding the engine. Stable, reusable rulings matter more than maximizing the number of bespoke checks.

Use manual saves and recoverable setbacks for initial testing. Permanent death and difficulty modes remain open. Failures can matter through injury, expense, lost time, distrust, or missed opportunities without destroying every experiment.

## Prototype sequence and evidence

### 1. Minimum proof: a world that reacts

One settlement, three locations, four named NPCs, one conflict, and support for conversation, movement, giving, purchasing, waiting, and a meaningful uncertain skill check. Provide a controlled starting state and enough test money for the wealth-gift experiment. Money used in this test is a setup fixture, not a proposed starting balance for the campaign.

Give the recipient a reason to need money, a competing desire, and a relationship affected by their decisions. The test is not that every recipient must retire. It is that money changes their feasible plans, they respond consistently with their motives, and any decision to delay has a grounded reason. Actual transactions move inventory and funds.

| Experiment | Evidence to inspect |
| --- | --- |
| Gift versus no gift from the same starting state | Changed affordable options and subsequent decisions; no universal scripted retirement response |
| A player attempts an uncertain action | Validated check, recorded roll and outcome, narration that agrees with the committed result |
| A witness tells another person | Recorded contact and received claim; an uninformed NPC does not know the event by default |
| The account is distorted or disbelieved | Recipient belief can differ from the event record and influence a later choice |
| Save, exit, and resume | Money, inventory, relationships, commitments, beliefs, and unresolved plans remain consistent |

Capture the initial state and LLM proposals when diagnosing a run. Seeded dice support repeatable mechanical resolution, but do not assume a new LLM call will produce identical prose or decisions. Mechanical consistency and subjective believability both need evaluation.

### 2. First playable slice: a reason to return

Add a compact version of the community problem, one competing drink stall, one choice between two small magic packages, an earned variant of an affinity ability, and a generated achievement. The stall starts with purchased inputs and an existing place to trade. NPC buyers have funds, preferences, and reasons for loyalty; reducing price alone need not attract everyone.

**[PROPOSAL] Progression experiment:** award an achievement item and a title buff in a controlled setup, then retain the earned variant to test optional prerequisites against those separate earned records. Verify the item is delivered and the buff affects qualifying resolution as defined, and that neither reward automatically applies an upgrade; separately test one concept-based awakening with a tiny candidate pool and two rarity outcomes in a controlled setup. Verify that an ineligible character cannot obtain the gated upgrade, that satisfying its prerequisite reveals an upgrade choice, and that the LLM receives the stone concept and complete affinity set when composing awakening candidates. Thematic fit is assessed through play feedback, not an engine validator. The awakened ability must belong to one affinity with capacity and consume its slot; a full affinity cannot receive another ability through this process. As a qualitative playtest, compare the same stone across two different complete affinity sets to assess how the LLM uses character context. Compare starting states directly; a playtester should not need to grind for a rare drop to test the system. Broader affinity progression remains later scope.

Give Kyle and friends a session with at least two plausible routes through the conflict and an opportunity to try an unplanned approach. Ask them to explain what changed, why an NPC acted as they did, whether an outcome felt unfair, and what they want to do next. A strong signal is voluntary return play accompanied by interest in unresolved people or plans. This is a test of the broader fantasy, not a revenue forecast.

Measure response latency, LLM calls and token use, session cost, invalid action proposals, and repairs needed for contradictory narration. Set acceptable thresholds from actual play before committing to a provider, hosting model, or public release.

### 3. Expand only where play earns it

Deepen magic combinations, add production and construction chains, extend the social network into another settlement, and increase world breadth. Ultimately support the complete forest-to-tavern scenario. Cooperative campaigns are a later design effort: shared time, separate conversations, and conflicting actions require explicit rules. Avoid making a multiplayer server a prerequisite for the solo experiment.

## Implementation direction

Begin with a local application, a durable save store, a text interface, and an adapter for the chosen LLM. Keep rule resolution independent of the model and presentation. Select the actual language, model, and storage system after specifying the minimum experiment; no framework, subscription, or infrastructure purchase is committed here.

Build behavior in small slices: one action from interpretation through resolution and persistence, one NPC responding to changed resources, then one contact transmitting a belief. Keep generated configuration as validated data using supported operations. Retain stable IDs and versions for abilities and rulings so descriptions and mechanics do not silently change between turns. Use an event record to explain consequential changes; a full event-sourced architecture is not required by this brief.

## Accepted working-default register

| ID | Accepted default | Rationale |
| --- | --- | --- |
| A1 | Adult tabletop/LitRPG audience; 20–60-minute sessions | Gives the first playtest a specific audience and manageable duration |
| A2 | Desktop browser, local execution, one developer with AI assistance | Keeps the text prototype small; weekly availability remains unknown |
| A3 | Game time advances through actions; offline time pauses | Supports persistence without requiring continuous attention |
| A4 | Brackenford and its failing ward; several routes to a viable community | Connects adventure, relationships, and livelihoods to one problem |
| A5 | Custom d20 checks, four provisional attributes, recoverable defeat, manual saves | Provides inspectable hard rules while testing creative adjudication |
| A6 | Engine validates and commits every persistent consequence | Keeps the LLM's interpretation accountable to stable state |
| A7 | Limited affinity combinations plus practice-shaped powers and universal basic skills | Confirmed magic direction, now expanded with rarity, awakening stones, limited abilities, and achievement/title prerequisites; classes removed |
| A8 | Grounded NPC tone, comic achievements, play continues after victory | Preserves emotional credibility and room to observe consequences |
| A9 | Four-NPC causal proof, followed by the broader playable slice | Tests the hardest promise before taking on the full world simulation |

All A1–A9 defaults were accepted on 2026-09-05. Budget, timeline, exact rules and victory thresholds, rarity distributions, ability counts, reveal and replacement rules, content boundaries, and acceptable cost/latency remain open. New sections marked [PROPOSAL] require further design rather than being silently included in that acceptance.

## Deferred reference

Kyle's Rise of the Living Forge innkeeper example is preserved as inspiration only: identifying protected visitors, influencing thoughts, accelerated healing during sleep, and buffs/debuffs based on operation and guest satisfaction. Place-based powers are deferred at Kyle's request because of implementation complexity. The earlier domain/class design is superseded and is not part of the active plan. Ordinary businesses and NPC customer choice remain active goals; there is no automatic commitment to restore magical domains later.

## Research grounding — 2026-09-05

- [Generative Agents, Park et al. (2023)](https://arxiv.org/abs/2304.03442): a research simulation of 25 agents used observations, memory retrieval, reflection, and planning; an invitation spread through conversations. This supports a small experiment in memory and social transmission. It does not establish long-running economic consistency, production multiplayer scalability, or the proposed distorted rumor model.
- [Voyager, Wang et al. (2023)](https://arxiv.org/abs/2305.16291): an LLM agent developed reusable executable Minecraft behaviors with environment feedback. This is relevant to structured actions and feedback, but its programmatic skills are not balanced RPG abilities and do not demonstrate unrestricted DM adjudication.
- [Dwarf Fortress official features](https://bay12games.com/dwarves/features.html) and [2016 developer log](https://www.bay12games.com/dwarves/dev_2016.html): persistent world histories, individual personalities, taverns, and rumor gathering/spreading provide a simulation comparison. The development account does not verify the complete telephone-distortion behavior requested here. Proposed inspiration is persistent causal history and social places as information routes; its full simulation breadth is not proposed as initial scope.

- [He Who Fights With Monsters author/narrator AMA (2021)](https://www.reddit.com/r/litrpg/comments/pjvrec/ama_author_and_audiobook_narrator_of_he_who/): Shirtaloon discusses a confluence arising from animal essences and the challenge of presenting numerous powers. This supports considering combinations and readable ability presentation. The dmud affinity example is an original design. Kyle subsequently clarified his own preferences, recorded above; those preferences are the design authority here.

These are precedents for constituent ideas, not evidence that their integration already solves this game's design challenges.
