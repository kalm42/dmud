from collections import Counter
from collections.abc import Sequence

from dmud.authored_content.approved_p0_content import (
    APPROVED_KIND_COUNTS,
    APPROVED_LOCATION_IDS,
    APPROVED_MOVEMENT_MODE_IDS,
    APPROVED_MOVEMENT_SPEEDS,
    APPROVED_NPC_IDS,
)
from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.models import (
    Location,
    MovementRules,
    Npc,
    SourcedDocument,
)


def check_approved_inventory(
    documents: Sequence[SourcedDocument],
) -> tuple[ContentIssue, ...]:
    """Accept exactly the approved P0 kinds, counts, locations, NPCs, and movement modes.

    Extra content (a fourth location, a fifth NPC, a second check) is unexpected_content
    at its file; absent content is missing_content. For example,
    check_approved_inventory(documents) == () for the committed package.
    """
    issues: list[ContentIssue] = []
    counts = Counter(source.document.kind for source in documents)
    for kind, expected in APPROVED_KIND_COUNTS.items():
        if counts[kind] < expected:
            issues.append(ContentIssue(code="missing_content", file="", field=kind))
    seen_kinds: Counter[str] = Counter()
    found_locations: set[str] = set()
    found_npcs: set[str] = set()
    for source in documents:
        document = source.document
        seen_kinds[document.kind] += 1
        if isinstance(document, Location):
            found_locations.add(document.id)
            if document.id not in APPROVED_LOCATION_IDS:
                issues.append(
                    ContentIssue(
                        code="unexpected_content", file=source.path, field="id"
                    )
                )
        elif isinstance(document, Npc):
            found_npcs.add(document.id)
            if document.id not in APPROVED_NPC_IDS:
                issues.append(
                    ContentIssue(
                        code="unexpected_content", file=source.path, field="id"
                    )
                )
        elif seen_kinds[document.kind] > APPROVED_KIND_COUNTS[document.kind]:
            issues.append(
                ContentIssue(code="unexpected_content", file=source.path, field="kind")
            )
        elif isinstance(document, MovementRules):
            mode_ids = frozenset(mode.id for mode in document.modes)
            speeds = {mode.id: mode.speed_mm_per_second for mode in document.modes}
            if (
                mode_ids != APPROVED_MOVEMENT_MODE_IDS
                or len(document.modes) != len(mode_ids)
                or speeds != dict(APPROVED_MOVEMENT_SPEEDS)
            ):
                issues.append(
                    ContentIssue(
                        code="unexpected_content", file=source.path, field="modes"
                    )
                )
    for missing in sorted(APPROVED_LOCATION_IDS - found_locations):
        issues.append(ContentIssue(code="missing_content", file="", field=missing))
    for missing in sorted(APPROVED_NPC_IDS - found_npcs):
        issues.append(ContentIssue(code="missing_content", file="", field=missing))
    return tuple(issues)
