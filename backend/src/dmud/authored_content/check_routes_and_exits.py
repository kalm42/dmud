from collections.abc import Mapping

from dmud.authored_content.approved_p0_content import (
    APPROVED_ROUTE_ENDPOINTS,
    APPROVED_ROUTE_LENGTHS,
)
from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.content_registry import ContentRegistry


def check_routes_and_exits(
    registry: ContentRegistry, sources: Mapping[str, str]
) -> tuple[ContentIssue, ...]:
    """Require the approved route topology and exits that mirror it exactly.

    Market Square connects to each other location and nothing else connects. Each
    location has one exit per route touching it, leading to that route's other end.
    For example, check_routes_and_exits(registry, sources) == () for the committed package.
    """
    issues: list[ContentIssue] = []
    world_file = sources[registry.world.id]
    pairs = [frozenset(route.endpoint_ids) for route in registry.world.routes]
    for i, pair in enumerate(pairs):
        if len(pair) != 2 or pairs.index(pair) != i:
            issues.append(
                ContentIssue(
                    code="route_mismatch", file=world_file, field=f"routes[{i}]"
                )
            )
    if frozenset(pairs) != APPROVED_ROUTE_ENDPOINTS:
        issues.append(
            ContentIssue(code="route_mismatch", file=world_file, field="routes")
        )

    lengths = dict(APPROVED_ROUTE_LENGTHS)
    for i, route in enumerate(registry.world.routes):
        if route.length_mm != lengths.get(frozenset(route.endpoint_ids)):
            issues.append(
                ContentIssue(
                    code="route_mismatch",
                    file=world_file,
                    field=f"routes[{i}].length_mm",
                )
            )

    for location in registry.locations.values():
        expected = {
            (route.id, other)
            for route in registry.world.routes
            if location.id in route.endpoint_ids
            for other in route.endpoint_ids
            if other != location.id
        }
        actual = [(e.route_id, e.to_location_id) for e in location.exits]
        if len(actual) != len(set(actual)) or set(actual) != expected:
            issues.append(
                ContentIssue(
                    code="exit_mismatch", file=sources[location.id], field="exits"
                )
            )
    return tuple(issues)
