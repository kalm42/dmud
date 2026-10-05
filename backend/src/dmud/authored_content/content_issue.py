from typing import Literal

from pydantic import BaseModel, ConfigDict

IssueCode = Literal[
    "content_directory_missing",
    "too_many_files",
    "file_too_large",
    "unreadable_file",
    "invalid_yaml",
    "duplicate_key",
    "unknown_kind",
    "unknown_field",
    "missing_field",
    "invalid_value",
    "manifest_missing",
    "unsupported_content_version",
    "duplicate_id",
    "unexpected_content",
    "missing_content",
    "unresolved_reference",
    "route_mismatch",
    "exit_mismatch",
    "introduction_length",
    "obligation_mismatch",
    "fixture_funding_mismatch",
    "perception_mismatch",
]


class ContentIssue(BaseModel):
    """One bounded validation finding: a code, a content-relative file, and a field path.

    Issues never carry absolute paths, raw YAML, or stack traces, so they are safe to
    count and log. For example, ContentIssue(code="duplicate_id", file="npcs/ivo.yaml", field="id").
    """

    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)
    code: IssueCode
    file: str
    field: str
