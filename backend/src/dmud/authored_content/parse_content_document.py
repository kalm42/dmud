from typing import cast

from pydantic import TypeAdapter, ValidationError

from dmud.authored_content.content_issue import ContentIssue, IssueCode
from dmud.authored_content.format_field_path import format_field_path
from dmud.authored_content.freeze_sequences import freeze_sequences
from dmud.authored_content.models import ContentDocument, SourcedDocument
from dmud.authored_content.yaml_structure_valid import yaml_structure_valid

_DOCUMENT = TypeAdapter[ContentDocument](ContentDocument)
_CODES: dict[str, IssueCode] = {
    "extra_forbidden": "unknown_field",
    "missing": "missing_field",
    "union_tag_invalid": "unknown_kind",
    "union_tag_not_found": "unknown_kind",
}


def parse_content_document(
    path: str, data: object
) -> SourcedDocument | tuple[ContentIssue, ...]:
    """Validate parsed YAML strictly against the document model chosen by its `kind`.

    Unknown fields, wrong types such as "20" for 20, and unknown kinds become issues
    with a field path; values are never echoed. For example,
    parse_content_document("npcs/mara.yaml", {"kind": "npc", ...}).
    """
    if not yaml_structure_valid(data):
        return (ContentIssue(code="invalid_yaml", file=path, field=""),)
    frozen = freeze_sequences(data)
    kind = (
        cast(dict[object, object], data).get("kind") if isinstance(data, dict) else None
    )
    try:
        document = _DOCUMENT.validate_python(frozen)
    except ValidationError as error:
        issues: list[ContentIssue] = []
        for detail in error.errors(include_input=False, include_url=False):
            location = list(detail["loc"])
            if location and location[0] == kind:
                location = location[1:]
            code = _CODES.get(detail["type"], "invalid_value")
            field = "kind" if code == "unknown_kind" else format_field_path(location)
            issues.append(ContentIssue(code=code, file=path, field=field))
        return tuple(issues)
    return SourcedDocument(path=path, document=document)
