from collections.abc import Mapping

from dmud.authored_content.approved_p0_content import (
    INTRODUCTION_MAX_WORDS,
    INTRODUCTION_MIN_WORDS,
)
from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.content_registry import ContentRegistry


def check_introductions(
    registry: ContentRegistry, sources: Mapping[str, str]
) -> tuple[ContentIssue, ...]:
    """Require each location introduction to be 60–120 words (GDD G07).

    Words are whitespace-separated tokens. For example,
    check_introductions(registry, sources) == () for the committed package.
    """
    return tuple(
        ContentIssue(
            code="introduction_length",
            file=sources[location.id],
            field="introduction",
        )
        for location in registry.locations.values()
        if not (
            INTRODUCTION_MIN_WORDS
            <= len(location.introduction.split())
            <= INTRODUCTION_MAX_WORDS
        )
    )
