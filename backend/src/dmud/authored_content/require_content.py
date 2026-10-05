from dmud.authored_content.content_registry import ContentRegistry
from dmud.authored_content.content_result import ContentLoaded, ContentResult
from dmud.operations.models import OperationError

CONTENT_UNAVAILABLE_DETAIL = (
    "The authored starting world failed validation, so nothing was started. "
    "Correct the game content and restart the application."
)


def require_content(content: ContentResult) -> ContentRegistry:
    """Return the validated registry or raise a content_unavailable problem before any mutation.

    Commands that need authored content (New Game now, confirmation in Story 1.9) call
    this before durable acceptance. For example, require_content(app.state.content).
    """
    if isinstance(content, ContentLoaded):
        return content.registry
    raise OperationError("content_unavailable", 503, detail=CONTENT_UNAVAILABLE_DETAIL)
