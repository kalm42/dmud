from dataclasses import dataclass

from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.content_registry import ContentRegistry

MAX_REPORTED_ISSUES = 32


@dataclass(frozen=True, slots=True)
class ContentLoaded:
    """Validated content is available; for example, ContentLoaded(registry)."""

    registry: ContentRegistry


@dataclass(frozen=True, slots=True)
class ContentUnavailable:
    """Validation failed; at most MAX_REPORTED_ISSUES issues plus the true total.

    Expected failures are data, not exceptions. For example,
    ContentUnavailable(issues=(issue,), issue_count=1).
    """

    issues: tuple[ContentIssue, ...]
    issue_count: int


ContentResult = ContentLoaded | ContentUnavailable
