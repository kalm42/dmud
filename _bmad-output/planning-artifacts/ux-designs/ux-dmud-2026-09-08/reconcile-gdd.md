# GDD Reconciliation

Sources reconciled:

- `../../gdds/gdd-dmud-2026-09-07/gdd.md` — version 0.8, `staged-design-baseline-approved`
- `.decision-log.md` — canonical UX discovery decisions
- `mockups/direction-dm-notebook.html` — promoted first-pass visual reference

`DESIGN.md` and `EXPERIENCE.md` remain authoritative over the mockup. This reconciliation does not promote any GDD proposal or assumption to accepted status.

## GDD Requirements Preserved in UX

- The desktop-browser, text-first experience centers on one free-text intention composer. It accepts natural phrasing and synonyms without an exhaustive MUD-style verb syntax.
- No suggested actions, dialogue replies, recommendation chips, fixed solution order, or proactive strategy hints are introduced. Neutral clarification preserves intent without steering; factual exits, journal, inventory, character, save/load, and mechanical-detail controls remain allowed.
- Every submitted intention must expose pending, resolved, interrupted, or failed status and a recoverable failure path. Playful waiting copy is presentation for pending work, never evidence that an action succeeded.
- Routine feasible actions may resolve without a roll. Mechanical details remain inspectable, including uncertainty, pre-roll difficulty/probability when applicable, modifiers and their sources, stakes/cost, roll/result, and committed rationale. Impossible or unsupported actions receive a factual explanation without state mutation.
- Reading, typing, model latency, menus, save, inventory, character reference, known journal information, and other inspections of already-known facts advance no fictional time. In-world action, speech, travel, handling, and waiting may advance it under G04.
- Player-facing information respects limited character knowledge. NPC observations, beliefs, motives, plans, concealed characters, and other simulation state are not exposed merely because the engine knows them.
- Narration, NPC speech, player intention, mechanics, awards, and the fourth-wall-breaking LitRPG System remain perceptibly distinct. The System cannot decide NPC behavior or rewrite unresolved events.
- The journal remains the factual surface for known concerns, commitments, quests, and their explicit success conditions, subject to G10/G20 status. It must not reveal hidden motives or become a source of recommended actions.
- Manual save/resume remains branch-local and restores authoritative state under accepted G08. The single save shown in the mockup is an example, not a reduction of the accepted three-slot requirement.
- The character model remains classless. Universal basic skills are not visually presented as locked behind titles, achievements, affinities, or special abilities.
- Easy reading and skimming, clear attribution independent of color, keyboard reachability, and no timed reading remain required. No audio is needed to understand a meaningful cue.

## New UX Decisions

- The approved visual metaphor is **the DM's Notebook**: a restrained, readable, accumulating tabletop artifact. Comic Sans is prohibited.
- Rowan is a personable Dungeon Master conveyed through writing and responsive status copy, not through privileged persistent portrait space. The interaction should feel like talking with a tabletop DM among friends.
- Waiting should create playful anticipation through absurd backstage messages and optional motion, such as “Corralling the goblins,” while retaining truthful processing state.
- The persistent side reference is limited to the player's character in the first pass. There is no persistent “On this page” or nearby-character roster.
- Inventory and the character sheet open as temporary overlays. Mechanical details open from the relevant inline result; there is no global roll-details tab. Opening or closing these overlays is zero-time inspection.
- One composer handles questions to Rowan, character actions, and in-world speech. Rowan infers message type from ordinary language and context; no prefix or mode switch is required. Ambiguity triggers a neutral, zero-time clarification before commitment.
- Continue-game recall is conversational: the player may ask Rowan anything, and Rowan answers only with information the character legitimately knows.
- New Game includes a collaborative Session 0. Rowan asks for the character's name, origin, cares, hates, what the player thinks would be cool, and hopes for play. Rowan first invites the player to author the concept and offers background ideas only when asked.
- The player directly assigns the fixed `8, 10, 12, 13, 14` array across Body, Agility, Constitution, Mind, and Presence on the character sheet. Stats remain editable until confirmation, then read-only in ordinary character-sheet use.
- Before play, Rowan reflects the character and campaign understanding back for confirmation. Session 0 ends with a personally relevant opening situation, while establishing opportunities and tensions without predetermining outcomes or overriding NPC agency.
- The character sheet owns stats, titles, and achievements. New characters begin with no titles or achievements. Personalized titles, achievements, and ability upgrades arise from subsequent play and remain distinct reward types.
- First-pass novelty recognition is save/character-local. Cross-player “world first” recognition is deferred to a possible online indie release.
- WCAG 2.2 Level AA is the accepted accessibility floor for complete pages and responsive variations, including generated and dynamic content. This includes semantic structure, screen-reader attribution and announcements, full keyboard operation, visible unobscured focus, accessible overlay names/roles and focus return, contrast, 200% browser zoom, target reflow, and reduced-motion handling.

## Deferred or Intentionally Omitted

- No in-game text-size control is provided: browser preferences and zoom own text sizing. A convenience control for reduced motion may remain optional, but it does not weaken the required operating-system preference support.
- No persistent DM portrait, NPC portrait rail, nearby-character list, or omniscient presence summary is included. Other characters appear only through perceived or legitimately known story information.
- No separate full-page destinations are required for inventory, character reference, or routine roll inspection.
- Session 0 validates one use of each approved array value across the five approved attributes and allows correction until atomic character confirmation. Storage for player preferences versus binding character/campaign facts remains an architecture/content-model decision.
- Cross-player achievement comparison, identity matching across generated wording, shared account/registry scope, privacy, consent, and world-first arbitration are later online-product decisions.
- The current mockup does not define dedicated UI for the conditional P1–P9 systems: effects/resources, access/ownership, survival needs, autonomous livelihoods, community/alchemy, affinity awakening and recognition, daily quests/gacha, hidden bonuses, or combat. Their GDD stage gates remain unchanged and each requires a later phase-specific UX update before implementation.
- The GDD requires no illustration, portrait, animation, generated-image pipeline, music, or audio asset for P0–P9. The mockup's lightweight player avatar and CSS waiting motion demonstrate presentation only and do not create an asset-pipeline requirement.
- Multiple Dungeon Masters with different personalities remain a possible future idea, not accepted first-pass scope.

## Conflicts and Clarifications

- GDD references to “present people” do not authorize an omniscient roster. In player-facing UX, “present” means currently perceived or legitimately known; successful stealth, concealment, and unknown presence must not leak.
- **Resolved — G15 text sizing:** GDD v0.8 and the UX spines assign preferred text size to browser settings, provide no in-game text-size control, and retain browser zoom/reflow requirements. DESIGN.md expresses that decision through relative `rem` typography without a fixed root size.
- The updated mock keeps the wide desktop composition as one branch and adds fluid/narrow reflow for enlarged browser text. The final implementation must still verify the WCAG AA reflow target and 200% zoom behavior rather than treating the reference as test evidence.
- The mockup's “Ward holds for 5 days” is illustrative scene content. It neither approves nor changes proposed G02's seven-day starting pressure, and it must not introduce a ward subsystem into P0, where ward pressure is explicitly excluded.
- The mockup shows one save card, while accepted G08 requires three manual save slots. The card demonstrates presentation for one slot only.
- Session 0 background suggestions are permitted only when the player requests creative help. This is a bounded pre-play exception and does not weaken the accepted prohibition on unsolicited in-play action suggestions.
- Titles, achievements, and earned ability variants may have character-sheet homes without entering P0. They remain excluded from P0 and conditionally budgeted for P6.
- Rowan's personality is visible through language and feedback, resolving the earlier portrait asymmetry without removing the explicit Dungeon Master relationship.

## Qualitative Ideas at Risk of Being Dropped

- The emotional target is escapism with meaningful agency: James should feel able to attempt ordinary, strange, or socially disruptive actions and receive credible, persisted consequences rather than encounter a railcart of pre-programmed outcomes.
- The trust test is semantic freedom: “go north” and “walk north” should be equivalent, and improvised actions such as pouring beer over someone's head should be treated as real intentions within world rules.
- The notebook should feel shared and accumulated, like notes kept at a tabletop campaign, while still being easy to scan during long text-heavy sessions.
- Rowan's humor belongs mainly in waiting and recognition. It should make latency enjoyable without undermining grounded NPC consequences, accessibility, or the truth of what has resolved.
- The simulation/story balance is intentional: Session 0 may plant conflicts, opportunities, and room for character growth, but neither the player nor NPCs are railroaded toward predetermined outcomes.
- Returning after time away should not require a conventional recap screen to restore confidence; asking Rowan what the character knows is itself a primary recall interaction.
- A later personalized ability name or genuinely unusual achievement is an important aspirational payoff, but it must emerge from actual history rather than be granted during Session 0.
