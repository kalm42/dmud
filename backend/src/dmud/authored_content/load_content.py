from pathlib import Path

from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.content_result import ContentResult
from dmud.authored_content.content_unavailable import content_unavailable
from dmud.authored_content.validate_content import validate_content

MAX_FILES = 64
MAX_FILE_BYTES = 64 * 1024


def load_content(directory: Path) -> ContentResult:
    """Read every *.yaml file under the content directory, then validate purely.

    This is the only authored-content function that touches the filesystem. It bounds
    file count and size, refuses files resolving outside the directory, and reports
    only content-relative paths. Call it off the event loop. For example,
    await asyncio.to_thread(load_content, settings.content_directory).
    """
    if not directory.is_dir():
        return content_unavailable(
            [ContentIssue(code="content_directory_missing", file="", field="")]
        )
    root = directory.resolve()
    paths = sorted(directory.rglob("*.yaml"))
    if len(paths) > MAX_FILES:
        return content_unavailable(
            [ContentIssue(code="too_many_files", file="", field="")]
        )
    files: dict[str, str] = {}
    issues: list[ContentIssue] = []
    for path in paths:
        relative = path.relative_to(directory).as_posix()
        try:
            if not path.resolve().is_relative_to(root) or not path.is_file():
                issues.append(
                    ContentIssue(code="unreadable_file", file=relative, field="")
                )
                continue
            if path.stat().st_size > MAX_FILE_BYTES:
                issues.append(
                    ContentIssue(code="file_too_large", file=relative, field="")
                )
                continue
            files[relative] = path.read_text(encoding="utf-8")
        except OSError, UnicodeDecodeError:
            issues.append(ContentIssue(code="unreadable_file", file=relative, field=""))
    if issues:
        return content_unavailable(issues)
    return validate_content(files)
