import type * as React from 'react';

export type Attribute = 'Body' | 'Agility' | 'Constitution' | 'Mind' | 'Presence';
export type StartingValue = 8 | 10 | 12 | 13 | 14;
export type RequestState = 'pending' | 'clarification' | 'resolved' | 'interrupted' | 'failed';

export interface ActionButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  /** primary = forest fill (default); quiet = forest outline. */
  variant?: 'primary' | 'quiet';
  /** Shown under a disabled button and linked via aria-describedby. */
  disabledReason?: string;
}
export declare function ActionButton(props: ActionButtonProps): React.ReactElement;

export interface NavItem { id: string; label: string }
export interface NotebookNavigationProps {
  items: NavItem[];
  currentId?: string;
  onSelect?: (id: string) => void;
  /** Accessible name of the nav landmark. Default "Notebook". */
  label?: string;
  /** Visible heading, e.g. the campaign name. */
  title?: string;
  className?: string;
}
export declare function NotebookNavigation(props: NotebookNavigationProps): React.ReactElement;

export interface NotebookPageProps {
  children: React.ReactNode;
  /** Element to render. Default "main". */
  as?: 'main' | 'section' | 'div' | 'article';
  label?: string;
  /** Drop the gilt frame, stars and grain. */
  plain?: boolean;
  className?: string;
}
export declare function NotebookPage(props: NotebookPageProps): React.ReactElement;

export interface SceneHeadingProps {
  /** Place (and time if it matters): "Mill Lane, at dusk". */
  title: string;
  /** Italic caption under the rule, e.g. "Day 3". */
  detail?: string;
  /** Heading level. Default 2. */
  level?: 2 | 3 | 4;
  className?: string;
}
export declare function SceneHeading(props: SceneHeadingProps): React.ReactElement;

/** Decorative gilt flourish between scenes (aria-hidden). */
export declare function SceneDivider(props: { className?: string }): React.ReactElement;

export interface StoryTurnProps {
  /** A PlayerIntention, then its StoryEntry replies (and a ResponseStatus while pending). */
  children: React.ReactNode;
  /** In-world time/place the turn began, e.g. "Day 3 · dusk · Mill Lane". */
  time?: string;
  /** Accessible name for the turn's region. */
  label?: string;
  className?: string;
}
export declare function StoryTurn(props: StoryTurnProps): React.ReactElement;

export interface StoryEntryProps {
  kind?: 'narration' | 'npc' | 'rowan' | 'clarification' | 'failure';
  /** NPC name as the player knows it ("Oren", or "Stranger" before it is learned). kind = "npc". */
  speaker?: string;
  /** What the player knows them as: "moneylender", "grey coat, by the well". Player knowledge only. */
  epithet?: string;
  /** Opens "What you know about {speaker}" (ReferenceOverlay + KnownCharacter). Makes the name a button. */
  onIdentify?: () => void;
  /** Same voice as the entry before: hides the margin label visually and tightens the gap. */
  continued?: boolean;
  /** Illuminated initial on the first paragraph. Once per scene, on the first narration. */
  dropCap?: boolean;
  /** Override the margin label for non-NPC kinds. */
  label?: string;
  /** A MechanicalResult attached to this entry (put it on the last entry of a continued run). */
  mechanic?: React.ReactNode;
  children: React.ReactNode;
  className?: string;
}
export declare function StoryEntry(props: StoryEntryProps): React.ReactElement;

export interface KnownFact { text: string; /** Where the character learned it: "Tessa told you, Day 2". */ source?: string }
export interface KnownCharacterProps {
  epithet?: string;
  facts: KnownFact[];
  lastSeen?: string;
  /** The player's character, for the "Only what James has seen…" note. */
  characterName?: string;
  className?: string;
}
export declare function KnownCharacter(props: KnownCharacterProps): React.ReactElement;

export interface PlayerIntentionProps {
  /** The exact submitted text. */
  text: string;
  status?: 'sent' | RequestState;
  characterName?: string;
  className?: string;
}
export declare function PlayerIntention(props: PlayerIntentionProps): React.ReactElement;

export interface MessageComposerProps {
  value?: string;
  defaultValue?: string;
  onChange?: (value: string) => void;
  onSubmit?: (value: string) => void;
  disabled?: boolean;
  label?: string;
  placeholder?: string;
  submitLabel?: string;
  rows?: number;
  className?: string;
}
export declare function MessageComposer(props: MessageComposerProps): React.ReactElement;

export interface ResponseStatusProps {
  state: RequestState;
  /** Overrides the default truthful state text. */
  message?: string;
  /** Pending only: a short absurd backstage line. Not announced. */
  quip?: string;
  /** What was / was not committed, for failed or interrupted. */
  detail?: string;
  onRetry?: () => void;
  retryLabel?: string;
  className?: string;
}
export declare function ResponseStatus(props: ResponseStatusProps): React.ReactElement;

export interface CharacterCardProps {
  name: string;
  monogram?: string;
  descriptor?: string;
  facts?: { label: string; value: React.ReactNode }[];
  onOpen?: () => void;
  className?: string;
}
export declare function CharacterCard(props: CharacterCardProps): React.ReactElement;

export interface ReferenceOverlayProps {
  open: boolean;
  title: string;
  onClose: () => void;
  /** Position within the nearest positioned ancestor instead of the viewport (previews, docs). */
  contained?: boolean;
  autoFocus?: boolean;
  children: React.ReactNode;
  className?: string;
}
export declare function ReferenceOverlay(props: ReferenceOverlayProps): React.ReactElement | null;

export interface MechanicalResultProps {
  skill: string;
  /** false = "no roll needed". Default true. */
  rolled?: boolean;
  /** e.g. "14 + 3 = 17 vs 15" */
  roll?: string;
  result: string;
  /** Opens Roll details. The Details button is the only interactive part. */
  onDetails?: () => void;
  className?: string;
}
export declare function MechanicalResult(props: MechanicalResultProps): React.ReactElement;

export interface JournalEntryProps {
  title: string;
  /** Written status, e.g. "Known", "Commitment", "Kept". */
  status?: string;
  source?: string;
  children: React.ReactNode;
  className?: string;
}
export declare function JournalEntry(props: JournalEntryProps): React.ReactElement;

export type StatValues = Partial<Record<Attribute, StartingValue | null>>;
export interface StatAssignmentProps {
  value?: StatValues;
  defaultValue?: StatValues;
  onChange?: (value: StatValues) => void;
  onConfirm?: (value: StatValues) => void;
  locked?: boolean;
  className?: string;
}
export declare function StatAssignment(props: StatAssignmentProps): React.ReactElement;

export interface AttributeAllocationProps {
  attributes: Partial<Record<Attribute, number>>;
  earned: number;
  spent: number;
  state?: 'idle' | 'pending' | 'persisted';
  onConfirm?: (attribute: Attribute) => void;
  className?: string;
}
export declare function AttributeAllocation(props: AttributeAllocationProps): React.ReactElement;

export interface SaveSlotProps {
  slot: 1 | 2 | 3;
  empty?: boolean;
  campaign?: string;
  place?: string;
  worldTime?: string;
  savedAt?: string;
  selected?: boolean;
  onSelect?: () => void;
  className?: string;
}
export declare function SaveSlot(props: SaveSlotProps): React.ReactElement;

/** Deferred P7–P8. */
export interface SystemNoticeProps { label?: string; children: React.ReactNode; className?: string }
export declare function SystemNotice(props: SystemNoticeProps): React.ReactElement;

/** Deferred P6–P8. */
export interface AwardNoticeProps { type: 'achievement' | 'title' | 'prize' | 'variant'; name: string; children?: React.ReactNode; className?: string }
export declare function AwardNotice(props: AwardNoticeProps): React.ReactElement;

declare global {
  interface Window {
    Dmud: {
      ActionButton: typeof ActionButton; NotebookNavigation: typeof NotebookNavigation; NotebookPage: typeof NotebookPage; SceneHeading: typeof SceneHeading; SceneDivider: typeof SceneDivider; StoryTurn: typeof StoryTurn; StoryEntry: typeof StoryEntry; KnownCharacter: typeof KnownCharacter;
      PlayerIntention: typeof PlayerIntention; MessageComposer: typeof MessageComposer; ResponseStatus: typeof ResponseStatus;
      CharacterCard: typeof CharacterCard; ReferenceOverlay: typeof ReferenceOverlay; MechanicalResult: typeof MechanicalResult;
      JournalEntry: typeof JournalEntry; StatAssignment: typeof StatAssignment; AttributeAllocation: typeof AttributeAllocation;
      SaveSlot: typeof SaveSlot; SystemNotice: typeof SystemNotice; AwardNotice: typeof AwardNotice;
    };
  }
}
