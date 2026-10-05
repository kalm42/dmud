from collections.abc import Sequence

from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.content_result import MAX_REPORTED_ISSUES, ContentUnavailable


def content_unavailable(issues: Sequence[ContentIssue]) -> ContentUnavailable:
    """Bound reported issues while keeping the true total.

    For example, content_unavailable(issues).issue_count == len(issues).
    """
    return ContentUnavailable(
        issues=tuple(issues[:MAX_REPORTED_ISSUES]), issue_count=len(issues)
    )
