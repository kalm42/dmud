---
name: dmud — The DM's Notebook
description: Experience contract for a persistent, text-first fantasy role-playing game.
status: final
implementation_scope: P0
sources:
  - ../../briefs/brief-dmud-2026-09-05/brief.md
  - ../../gdds/gdd-dmud-2026-09-07/gdd.md
updated: 2026-09-23
---

# dmud — Experience Spine

## Foundation

Initial form factor is a locally run desktop browser for solo, 20–60-minute sessions. Keyboard and mouse are baseline; screen-reader operation is equally required. Architecture 1.2 selects a React UI, FastAPI backend, SQLite storage, and loopback-only packaging for P0; this UX document does not own those technology choices. The LLM provider, public deployment model, and audio system remain unselected. [DESIGN.md](./DESIGN.md) owns visual identity; this file owns behavior.

The experience promise is tabletop agency: the player writes an ordinary or outrageous intention in their own words, and Rowan answers like a Dungeon Master adjudicating a persistent world—not like a verb parser. The rules own authoritative state and mechanics; presentation never claims success before a result is committed.

### Phase Scope

This spine pair is the downstream implementation contract for **P0**. E3–E11 and their conditional P1–P9 stages remain source context only until a later UX update promotes them; deferred notes below preserve already-captured direction without making those systems build requirements.

| Source work package | UX status in this pair |
| --- | --- |
| E1 — Enter and act in a small persistent world | P0 implementation scope; covered by a Key Flow and component/state contracts. |
| E2 — Make consequences travel through people | P0 implementation scope; covered by a Key Flow and information-boundary rules. |
| E3 — Make resources and effects authoritative | Deferred conditional P1; excluded from this P0 contract. |
| E4 — Make places physically accessible | Deferred conditional P2; excluded from this P0 contract. |
| E5 — Live with hunger and fatigue | Deferred conditional P3; excluded from this P0 contract. |
| E6 — Let needs become plans | Deferred conditional P4; excluded from this P0 contract. |
| E7 — Secure Brackenford's future through play | Deferred conditional P5; excluded from this P0 contract. |
| E8 — Earn a distinctive affinity spell | Deferred conditional P6; excluded from this P0 contract. Captured recognition principles are non-normative until promoted. |
| E9 — Daily quest system and gacha rewards | Deferred conditional P7; excluded from this P0 contract. |
| E10 — Hidden bonus objectives | Deferred conditional P8; excluded from this P0 contract. |
| E11 — Resolve a bounded combat encounter | Deferred conditional P9; excluded from this P0 contract. |

## Information Architecture

| Surface | Reached from | Purpose |
| --- | --- | --- |
| Title | App open | Choose **New Game** or **Continue** immediately. |
| Session 0 | New Game | Collaboratively define a character; assign 8, 10, 12, 13, and 14 exactly once across Body, Agility, Constitution, Mind, and Presence; record campaign hopes; and confirm Rowan's understanding. |
| Save selection | Continue; campaign controls | Choose among the three manual save slots and restore a branch. Uses `reference-overlay` with `save-slot` rows. |
| Main Notebook | Confirmed Session 0; loaded save | Read the current scene, talk with Rowan, act or speak in-world, and see request state. |
| Journal | Main Notebook navigation | Revisit legitimately known facts, concerns, and explicit commitments without action suggestions. |
| Inventory | Main Notebook | Inspect owned items without advancing fictional time. Uses `reference-overlay`. |
| Character sheet | Main Notebook; Session 0 | Inspect the current player character's stats and progression records; assign 8, 10, 12, 13, and 14 exactly once across Body, Agility, Constitution, Mind, and Presence during Session 0; and allocate earned attribute points during P0 play. Uses `reference-overlay` in play. |
| Roll details | Inline `mechanical-result` | Explain a specific rolled or no-roll resolution, including uncertainty, modifiers and sources, stakes/cost, and rationale. Uses `reference-overlay`. |

The [promoted Main Notebook mock](./mockups/direction-dm-notebook.html) illustrates the Main Notebook together with Inventory, Character sheet, and Roll details overlays. Title, Session 0, Save selection, and Journal remain spine-only.

Information hierarchy in the Main Notebook is: current transcript and scene context; `message-composer` plus truthful request status; the current player character's `character-card`; then factual navigation and reference controls. No Settings surface or in-game control is provided for text size; the browser owns the player's preferred text size. Post-P0 System and award presentation is outside the P0 IA.

## Voice and Tone

| Voice | Contract |
| --- | --- |
| Rowan | A personable tabletop Dungeon Master: warm, attentive, and direct. Infers intent from ordinary language and admits uncertainty. |
| Narration | Grounded and concrete; describes committed facts and perceptible consequences without pretending prose itself changed state. |
| NPC | Individually attributed, emotionally credible, and limited to that character's knowledge and motives. |
| Mechanics | Factual and transparent. States what was assessed and why without theatricalizing the rules. |
| Clarification | Neutral and intent-preserving. Asks for the missing distinction without proposing a tactic or preferred action. |
| Rowan waiting | Owned by `response-status`: warm, truthful, and allowed brief absurd backstage humor without implying measured progress or success. |
| LitRPG System (deferred P7–P8) | Owned by deferred `system-notice`: fourth-wall-breaking, mischievous, and opinionated; never narrates awards, rewrites events, or decides NPC behavior. Not a P0 implementation requirement. |
| Award narration (deferred P6–P8) | Owned by deferred `award-notice`: states a committed achievement, title, prize, or earned variant without speaking as the System or merging reward types. Not a P0 implementation requirement. |
| Failure | Plain, specific, and recoverable. Says what was and was not committed and what can safely be retried. |

Pending copy may use absurd backstage lines such as “Corralling the goblins,” but it must still say Rowan is working and expose the real pending/failed state. Brand voice lives in DESIGN.md; these are microcopy rules.

## Component Patterns

Behavioral rules below pair one-for-one with DESIGN.md Components.

Every pointer-operated interactive component must expose a target at least 24 by 24 CSS px or satisfy the WCAG 2.2 spacing exception. This target and spacing remain available when browser text is enlarged, at 200% page zoom, and in the 320 CSS px-equivalent reflow layout; inline mechanics and overlay close controls are explicit acceptance cases.

| Component | Behavioral contract |
| --- | --- |
| `action-button` | Activates on click or keyboard activation; never relies on an icon alone; disabled state includes a reason when not obvious. |
| `notebook-navigation` | Exposes Main Notebook destinations and factual campaign controls in a stable reading order. Current location is programmatically indicated. |
| `story-entry` | Appends only after its status is known; exposes speaker/message type before content and remains selectable. Do not collapse prior consequences silently. |
| `player-intention` | Echoes the exact submitted text and its status so the player can verify what Rowan interpreted. |
| `message-composer` | One input for Rowan questions, character actions, and in-world speech. Enter sends; Shift+Enter inserts a line. No mode, prefix, suggestion chips, or generated replies. |
| `response-status` | Acknowledges submission immediately, then transitions to clarification, resolved, interrupted, or failed. Updates are announced without moving focus. |
| `character-card` | Opens the current player character's sheet. Contains only that character's information; never derives a visible roster from omniscient simulation state. |
| `reference-overlay` | One overlay at a time. Has an accessible name/role, closes with its control or Escape, contains focus, and returns focus to its invoker. Opening it advances no fictional time. |
| `mechanical-result` | Belongs to one transcript result. Activating it opens its explanation; “no roll needed” is a supported, inspectable result. |
| `system-notice` | Deferred P7–P8 component for LitRPG System messages. It remains distinct from Rowan, award narration, and mechanics and cannot imply an uncommitted reward. Not required in P0. |
| `award-notice` | Deferred P6–P8 component that appears only after the underlying reward commits, identifies the reward type, and is announced once. Not required in P0. |
| `journal-entry` | Restates known information and recorded commitments. Never exposes hidden motives/state or recommends what the player should do next. |
| `stat-assignment` | Assigns 8, 10, 12, 13, and 14 exactly once across Body, Agility, Constitution, Mind, and Presence; reports duplicate or missing values and unassigned attributes inline; and locks ordinary editing only after confirmation. |
| `attribute-allocation` | In P0 play, shows earned, spent, and unspent attribute points; previews the chosen increase; requires explicit confirmation; rejects overspending; and reflects only persisted allocation. It never changes the starting-array record. |
| `save-slot` | Shows enough branch context to choose safely. Save/load progress is explicit; overwrite requires confirmation; a failed operation preserves the prior durable state. |

## State Patterns

| Surface / component | Required states and recovery |
| --- | --- |
| Title | Cold-loading saves; no saves (Continue unavailable with explanation); saves available; save-index failure with retry that leaves New Game available. |
| Session 0 | First question; incomplete concept; one or more of Body, Agility, Constitution, Mind, and Presence unassigned; duplicate, missing, or invalid use of 8, 10, 12, 13, and 14; all five assignments valid; Rowan pending; reflection awaiting correction/confirmation; response failure with all entered material preserved. |
| Main Notebook | Cold load; restored scene; composer ready; `response-status` pending/clarification/resolved/interrupted/failed; model unavailable; unsupported intention. Pending never masquerades as success. |
| Journal | Empty; known entries; loading; failed read. Empty and failure copy never invents concerns or hints. Post-P0 quest lifecycles are outside this contract. |
| Inventory overlay | Empty; populated; loading; failed read. Empty means no owned items, not unknown simulation content. |
| Character-sheet overlay | Session 0 editable assignment of 8, 10, 12, 13, and 14 across Body, Agility, Constitution, Mind, and Presence; duplicate/missing/valid assignment states; confirmed starting assignments locked; P0 progression summary; no unspent points; unspent points available; allocation preview; invalid overspend; confirmation pending; allocation persisted; loading/error. P6 titles and achievements are absent in P0. |
| Roll-details overlay | Routine/no roll; rolled resolution; missing/corrupt detail. A missing explanation is reported, never synthesized from guesses. |
| Save-selection overlay | Empty slots; occupied slots; saving/loading; overwrite confirmation; failed operation; recovered prior state. |

If a request fails after some state was legitimately committed, the response identifies that boundary and offers a safe resume. Retrying must not duplicate time, items, rolls, XP, or rewards.

## Interaction Primitives

- Click or keyboard activation opens navigation, inline mechanics, and overlays. Tab/Shift+Tab follow visible reading order; Escape dismisses the active overlay.
- Enter submits from `message-composer`; Shift+Enter adds a line. Submission echoes a `player-intention` and enters `response-status` immediately.
- Rowan classifies natural language from words and context. “What do I know about Mara's debt?” is a zero-time Dungeon Master question; “Walk to Mara's stall” is an in-world action; ordinary synonyms must not require MUD syntax.
- Ambiguity triggers clarification before commitment. “I'll talk to Mara about the debt” may prompt whether James wants to ask a general question or discuss a specific arrangement. Clarification commits no fictional time or world state and offers no strategy.
- Before a consequential action is committed, reasonably knowable interpretation, stakes, and costs are exposed. Rare-resource spending or materially changed intent requires clarification.
- Reading, typing, model latency, menus, inventory, known journal information, roll details, character sheet, and save actions advance no fictional time. In-world speech, movement, handling, waiting, and other actions may advance it according to the GDD.
- Factual linked exits are allowed; suggested actions, dialogue replies, recommendation chips, and steering are prohibited.

## Text UI & Information Boundaries

The notebook is a non-diegetic tabletop artifact shared with Rowan. Narration and NPC speech communicate the fiction; mechanics explain adjudication. In deferred P7–P8 work, the LitRPG System may deliberately break the fourth wall, while P6–P8 award narration remains a separate voice; neither is part of this P0 implementation contract. Every active voice is labeled in text and exposed semantically, not just styled differently.

Only information the current player character perceives or legitimately knows may enter the transcript, journal, overlays, or character reference. The UI must never expose hidden characters because they exist in simulation state, including characters who succeeded at stealth or concealment. Crowded scenes are handled through narration, not an always-on roster. Rowan may answer recall questions using known evidence, but never reveal secrets that character did not learn.

## Input Schemes

- **Keyboard:** complete operation without a pointer, including title choices, composer, navigation, overlays, starting-stat assignment, in-play attribute allocation, save slots, and inline mechanics.
- **Mouse / pointer:** click targets mirror keyboard actions; text remains selectable; hover never carries unique information.
- **Screen reader:** semantic reading order, landmarks, headings, explicit speaker/type labels, described controls, overlay focus behavior, and polite status announcements.
- **Not committed:** gamepad, touch-first mobile, voice input, custom key remapping, and platform-specific glyphs. These require a later form-factor decision rather than silent implementation.

## Game Feel & Juice

The main feedback arc is intention → immediate acknowledgement → playful anticipation → trustworthy consequence. While Rowan works, `response-status` cycles short absurd backstage messages and may use a small looping activity animation. Copy changes must not reset screen-reader speech or imply progress that is not measured. Under `prefers-reduced-motion`, replace looping movement with a static mark and changing or stable status text.

Resolution replaces the pending state in context without stealing focus. Inline mechanics make surprising outcomes inspectable. No audio, illustration, screen shake, confetti, or portrait asset is required. Inherit the approved G16 evaluation targets: visible input acknowledgement within 100 ms, local menus within 200 ms, save/load within 2 seconds, 95% of completed LLM-mediated actions within 10 seconds, and a recoverable interruption by 30 seconds. Architecture and testing own how those targets are achieved and measured.

## Inspiration & Anti-patterns

| Carry forward | Reject |
| --- | --- |
| A tabletop notebook as a shared record of a campaign. | A traditional MUD parser where one exact verb works and an ordinary synonym fails. |
| A real tabletop Dungeon Master's conversational adjudication and willingness to handle improvised actions. | Choice menus, suggested replies, or rail-bound outcomes that substitute for player agency. |
| Deferred LitRPG recognition with a funny, opinionated System voice distinct from award narration, without copying a source voice. | A generic chat-app shell that blurs narration, NPCs, Rowan, mechanics, the System, and awards. |
| Readable, skimmable long-form presentation. | Omniscient nearby-character lists, especially when actors are hidden or numerous. |
| Contextual overlays that preserve the current page. | New tabs for character, inventory, or roll details; persistent global roll logs as the routine path. |
| Honest waiting with small absurd humor. | A disabled composer with no status, deceptive progress, intrusive animation, or Comic Sans. |

## Accessibility Floor

WCAG 2.2 Level AA is the baseline for complete pages and responsive variations, including generated and dynamic content.

- Semantic HTML, landmarks, headings, control names/roles/states, and explicit speaker/message-type labels are required.
- All functionality operates by keyboard with visible, unobscured focus using `{colors.focus}`. Focus order follows visual and reading order.
- Normal text meets 4.5:1 contrast, large text 3:1, and essential focus/component boundaries 3:1; DESIGN.md defines load-bearing pair targets. Color never carries meaning alone.
- Typography uses relative `rem` units and inherits the browser's root text size; the application must not override that preference with a fixed-pixel root size or provide an in-game text-size control.
- Browser text/page zoom through at least 200% preserves content and functionality. At the WCAG reflow target equivalent to 320 CSS px, reading and operation require no two-dimensional page scrolling except intrinsically two-dimensional content.
- Pointer targets are at least 24 by 24 CSS px or satisfy the WCAG 2.2 spacing exception. The target area and spacing remain available under browser-root text enlargement, 200% page zoom, and narrow reflow; test inline `mechanical-result` controls and `reference-overlay` close controls explicitly.
- Pending, clarification, resolved, interrupted, failed, and attribute-allocation changes are announced programmatically without forcing focus. Avoid announcing every decorative waiting-copy rotation.
- `reference-overlay` provides an accessible dialog name, predictable Escape/close behavior, contained focus, and focus return. No stacked overlays.
- Honor `prefers-reduced-motion`; no timed reading, auto-dismissed narrative, or interaction timeout is required. Browser/OS controls are sufficient for zoom and motion preferences, but do not replace application responsibility.

The browser-owned sizing rule implements GDD v0.8 `G15`: users choose their preferred text size through browser settings, and dmud adds no separate text-size control.

## Responsive & Platform

- **Ordinary desktop:** navigation, dominant story page, and compact player-character reference may occupy three regions while transcript and composer remain central.
- **200% browser zoom and narrow/reflow layout:** regions collapse into one reading column; navigation becomes a labeled top region; the character reference becomes a compact block; controls remain fully available without horizontal page scrolling.
- **Overlays:** `reference-overlay` stays bounded by the visible viewport, scrolls internally when necessary, and never stacks. Opening, closing, and focus-return behavior does not change with width or zoom.
- **Interaction parity:** keyboard, pointer, and screen-reader semantics remain identical across responsive variations. The promoted mock's wide three-region branch is not an implementation minimum width.

## Deferred Post-P0 Experience

Each deferred E3–E11 stage requires a phase-specific UX update before implementation. Already-captured P6–P8 recognition direction remains: System voice and award narration stay distinct; achievements, titles, and earned variants remain separate reward types; eligibility and the underlying event commit before presentation; novelty is save/character-local unless a later online product explicitly defines identity, privacy, and arbitration.

Illustrative payoff, not a current Key Flow: after James creates a genuinely unusual committed outcome, a later `award-notice` may recognize his own history and record the reward on the character sheet. It must never claim cross-player “world first” status or silently apply an optional ability replacement.

## Open Items

- How player-authored facts, agreed premises, preferences, and non-binding hopes are stored is an architecture/content-model decision; the UI must keep their labels distinct.
- E3–E11 systems across conditional P1–P9 remain outside this P0 implementation contract and require phase-specific UX updates before development.
- Gamepad, mobile/touch, audio, public hosting, and additional Dungeon Master personalities are later scope.

## Key Flows

### Flow 1 — New Game / Session 0 (James creates a life he wants to inhabit)

1. James opens dmud and immediately sees **New Game** and **Continue**. He chooses **New Game**.
2. Rowan asks the character's name first. James names the character James.
3. Rowan asks where James came from, what he cares about, and what he hates. Rowan then asks what James thinks would be especially cool and what he hopes to experience in the campaign.
4. James proposes his own background and concept. If he explicitly asks for help, Rowan may suggest backgrounds; otherwise Rowan does not supply choices.
5. James opens the character sheet and assigns 8, 10, 12, 13, and 14 exactly once across Body, Agility, Constitution, Mind, and Presence. P6 title and achievement sections are absent from the P0 sheet.
6. Rowan reflects the character back, separating character facts, agreed campaign premises, James's preferences, and non-binding story hopes, then asks whether the understanding is correct.
7. James corrects anything wrong and confirms the character. Starting stats become read-only in ordinary character-sheet use.
8. **Climax:** Rowan opens on a personally relevant tension shaped by the confirmed concept and hopes. James feels the campaign was prepared for him, while neither outcomes nor NPC choices are predetermined.

Failure path: missing or duplicate stat assignments identify the exact problem and block confirmation without discarding answers. If Rowan's response fails, Session 0 preserves James's text and assignments and offers a safe retry; no campaign state begins before explicit confirmation.

### Flow 2 — E1: Enter and act in a small persistent world (James returns after a week)

1. James chooses **Continue**, opens save selection, and picks a slot using campaign, place, in-world time, and saved-at context.
2. The Main Notebook restores that branch's transcript and known state. No abandoned-branch reward or knowledge carries over.
3. James asks, “What do I know about Mara's debt?” in the single composer. Rowan recognizes a Dungeon Master question, answers only from James's legitimate knowledge, and advances no fictional time.
4. James follows a factual linked exit from Market Square to Mara's Stall. The chosen movement commits contextual travel time, and the notebook reports the new place and world time without requiring a command keyword.
5. James buys the baseline one-gold drink. Before commitment he can verify the known price and intended purchase; afterward, his funds, Mara's stock, his inventory, and the handling time reconcile exactly once.
6. In the supported P0 interaction, James asks Oren for a payment extension. Before the Persuasion check commits, he can inspect the declared difficulty/probability, modifiers, and stakes; afterward he can inspect the die, total, result, committed consequence, and XP awarded once.
7. When committed progression creates an unspent attribute point, the character sheet exposes `attribute-allocation`. James previews one allocation, sees earned/spent/unspent counts, and explicitly confirms it.
8. James saves, reloads the slot, and sees the same time, money, inventory, relationships, commitments, beliefs, plans, XP, levels, bonuses, and allocated/unspent points.
9. **Climax:** James returns to the same Persuasion task after growth and can see his persisted competence contribute to the later adjudication. The world feels as though it understood, remembered, and developed with him. The approved inherited contextual-difficulty rule reflects the attempted feat and circumstances and must not raise the same unchanged task merely to cancel earned mastery; architecture and testing own its implementation and evidence.

Failure path: an unsupported intention receives a factual limitation without time cost or unsolicited alternatives. Invalid allocation identifies the exact overspend and changes nothing. A processing interruption states what, if anything, committed and preserves a safe retry/resume path; retrying cannot duplicate state, cost, time, roll, XP, points, or reward.

### Flow 3 — E2: Make consequences travel through people (James tests whether the world carries news)

1. From the known starting state for the P0 gift branch, James gives Mara the prepared 10,000-gold known-value pouch. The submitted intention and truthful request state appear immediately.
2. The rules commit the transfer once: ownership and funds reconcile, and Mara perceives the gift. Rowan narrates only what James can observe.
3. Mara's feasible opportunities change because of the gift. Her selected plan and later behavior have a motive-based explanation rather than a required scripted outcome.
4. Tessa witnesses the event and later contacts Ivo. Before receiving that report, Ivo knows nothing about the gift; after receipt, the report may be distorted or doubted without changing the original event.
5. James later encounters an observable choice or consequence shaped by Ivo's received belief. He may ask Rowan what he legitimately knows, but the UI exposes neither hidden motives nor the simulation's omniscient chain.
6. **Climax:** James recognizes that one ordinary social act traveled through different minds and changed later behavior without the story railroading any NPC toward a fixed response.

Failure path: a failed or interrupted transfer reports whether ownership, funds, or perception committed and retrying cannot duplicate any mutation. A failed report delivery does not erase or rewrite the original gift. If James lacks evidence for part of the chain, Rowan says that he does not know rather than leaking the hidden state.
