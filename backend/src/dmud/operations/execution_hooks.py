from collections.abc import Awaitable, Callable
from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionHooks:
    """Inject controlled scheduling at composition in tests; release roots leave hooks absent."""

    before_commit: Callable[[str], Awaitable[None]] | None = None
    after_commit: Callable[[str], Awaitable[None]] | None = None
