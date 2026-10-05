from collections.abc import Mapping

from dmud.authored_content.build_registry import build_registry
from dmud.authored_content.check_approved_inventory import check_approved_inventory
from dmud.authored_content.check_fixture_funding import check_fixture_funding
from dmud.authored_content.check_handover_perception import check_handover_perception
from dmud.authored_content.check_introductions import check_introductions
from dmud.authored_content.check_manifest import check_manifest
from dmud.authored_content.check_obligation import check_obligation
from dmud.authored_content.check_references import check_references
from dmud.authored_content.check_routes_and_exits import check_routes_and_exits
from dmud.authored_content.check_unique_ids import check_unique_ids
from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.content_result import ContentLoaded, ContentResult
from dmud.authored_content.content_unavailable import content_unavailable
from dmud.authored_content.index_sources import index_sources
from dmud.authored_content.models import SourcedDocument
from dmud.authored_content.parse_content_document import parse_content_document
from dmud.authored_content.parse_yaml_document import parse_yaml_document


def validate_content(files: Mapping[str, str]) -> ContentResult:
    """Validate a complete content package, given as relative path to text, purely.

    Stages run in order and stop at the first stage with issues, because later checks
    rely on earlier guarantees: parse and schema, then manifest, unique IDs, and the
    approved inventory, then references, then topology, text, obligation, funding, and
    perception. For example, validate_content({"manifest.yaml": "...", ...}).
    """
    issues: list[ContentIssue] = []
    documents: list[SourcedDocument] = []
    for path in sorted(files):
        data = parse_yaml_document(path, files[path])
        if isinstance(data, ContentIssue):
            issues.append(data)
            continue
        parsed = parse_content_document(path, data)
        if isinstance(parsed, SourcedDocument):
            documents.append(parsed)
        else:
            issues.extend(parsed)
    if issues:
        return content_unavailable(issues)

    issues.extend(check_manifest(documents))
    issues.extend(check_unique_ids(documents))
    issues.extend(check_approved_inventory(documents))
    if issues:
        return content_unavailable(issues)

    registry = build_registry(documents)
    sources = index_sources(documents)
    issues.extend(check_references(registry, sources))
    if issues:
        return content_unavailable(issues)

    for check in (
        check_routes_and_exits,
        check_introductions,
        check_obligation,
        check_fixture_funding,
        check_handover_perception,
    ):
        issues.extend(check(registry, sources))
    if issues:
        return content_unavailable(issues)
    return ContentLoaded(registry=registry)
