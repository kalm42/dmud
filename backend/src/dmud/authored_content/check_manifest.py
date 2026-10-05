from collections.abc import Sequence

from dmud.authored_content.approved_p0_content import (
    SUPPORTED_CONTENT_SCHEMA_VERSION,
    SUPPORTED_PACKAGE_ID,
    SUPPORTED_PACKAGE_MAJOR_VERSION,
)
from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.models import Manifest, SourcedDocument

MANIFEST_PATH = "manifest.yaml"


def check_manifest(documents: Sequence[SourcedDocument]) -> tuple[ContentIssue, ...]:
    """Require the root manifest and a content schema and package this release supports.

    For example, check_manifest(documents) reports unsupported_content_version for
    content_schema_version: 2 or package_version: "2.0.0".
    """
    manifest = next(
        (
            source.document
            for source in documents
            if source.path == MANIFEST_PATH and isinstance(source.document, Manifest)
        ),
        None,
    )
    if manifest is None:
        return (ContentIssue(code="manifest_missing", file=MANIFEST_PATH, field=""),)
    issues: list[ContentIssue] = []
    if manifest.content_schema_version != SUPPORTED_CONTENT_SCHEMA_VERSION:
        issues.append(
            ContentIssue(
                code="unsupported_content_version",
                file=MANIFEST_PATH,
                field="content_schema_version",
            )
        )
    if manifest.package_id != SUPPORTED_PACKAGE_ID:
        issues.append(
            ContentIssue(
                code="unsupported_content_version",
                file=MANIFEST_PATH,
                field="package_id",
            )
        )
    major = manifest.package_version.split(".")[0].lstrip("0") or "0"
    if major != str(SUPPORTED_PACKAGE_MAJOR_VERSION):
        issues.append(
            ContentIssue(
                code="unsupported_content_version",
                file=MANIFEST_PATH,
                field="package_version",
            )
        )
    return tuple(issues)
