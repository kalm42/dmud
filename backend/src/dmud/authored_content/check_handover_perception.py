from collections import Counter
from collections.abc import Mapping

from dmud.authored_content.approved_p0_content import MARA, MARAS_STALL, TESSA
from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.content_registry import ContentRegistry


def check_handover_perception(
    registry: ContentRegistry, sources: Mapping[str, str]
) -> tuple[ContentIssue, ...]:
    """Require authored positions that make the stall handover perceptible to Tessa only.

    Every NPC has exactly one starting position. The NPCs at the handover location are
    exactly its participants (Mara) plus its witnesses (Tessa), so Oren and Ivo are
    elsewhere and cannot perceive it. For example,
    check_handover_perception(registry, sources) == () for the committed package.
    """
    issues: list[ContentIssue] = []
    start = registry.starting_state
    file = sources[start.id]
    positioned = Counter(position.npc_id for position in start.npc_positions)
    if set(positioned) != set(registry.npcs) or any(
        count != 1 for count in positioned.values()
    ):
        issues.append(
            ContentIssue(code="perception_mismatch", file=file, field="npc_positions")
        )
    handover = start.handover
    participants = set(handover.participant_npc_ids)
    witnesses = set(handover.witness_npc_ids)
    present = {
        position.npc_id
        for position in start.npc_positions
        if position.location_id == handover.location_id
    }
    if (
        handover.location_id != MARAS_STALL
        or participants != {MARA}
        or witnesses != {TESSA}
        or len(handover.participant_npc_ids) != 1
        or len(handover.witness_npc_ids) != 1
        or present != participants | witnesses
    ):
        issues.append(
            ContentIssue(code="perception_mismatch", file=file, field="handover")
        )
    return tuple(issues)
