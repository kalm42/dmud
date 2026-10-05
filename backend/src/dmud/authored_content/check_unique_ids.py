from collections.abc import Sequence

from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.declared_ids import declared_ids
from dmud.authored_content.models import SourcedDocument


def check_unique_ids(documents: Sequence[SourcedDocument]) -> tuple[ContentIssue, ...]:
    """Reject any stable ID declared more than once, across files and content kinds.

    Every repeat after the first is reported at its own file and field. For example,
    check_unique_ids(documents) == () for the committed package.
    """
    seen: set[str] = set()
    issues: list[ContentIssue] = []
    for source in documents:
        for content_id, field in declared_ids(source.document):
            if content_id in seen:
                issues.append(
                    ContentIssue(code="duplicate_id", file=source.path, field=field)
                )
            seen.add(content_id)
    return tuple(issues)
