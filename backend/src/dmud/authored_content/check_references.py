from collections.abc import Mapping

from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.content_registry import ContentRegistry


def check_references(
    registry: ContentRegistry, sources: Mapping[str, str]
) -> tuple[ContentIssue, ...]:
    """Require every cross-document reference to resolve to existing content.

    ID patterns already fix the referenced kind, so an NPC field can only name an NPC
    ID; this check proves that ID exists. For example,
    check_references(registry, sources) == () for the committed package.
    """
    locations = registry.locations
    npcs = registry.npcs
    routes = {route.id for route in registry.world.routes}
    obligations = {c.obligation.id for c in registry.conflicts.values()}
    checked: list[tuple[str, str, bool]] = []

    world_file = sources[registry.world.id]
    for i, route in enumerate(registry.world.routes):
        for j, endpoint in enumerate(route.endpoint_ids):
            checked.append(
                (world_file, f"routes[{i}].endpoint_ids[{j}]", endpoint in locations)
            )
    for location in locations.values():
        file = sources[location.id]
        for i, exit_ in enumerate(location.exits):
            checked.append((file, f"exits[{i}].route_id", exit_.route_id in routes))
            checked.append(
                (file, f"exits[{i}].to_location_id", exit_.to_location_id in locations)
            )
    for conflict in registry.conflicts.values():
        file = sources[conflict.id]
        for i, npc in enumerate(conflict.participant_npc_ids):
            checked.append((file, f"participant_npc_ids[{i}]", npc in npcs))
        obligation = conflict.obligation
        checked.append(
            (file, "obligation.debtor_npc_id", obligation.debtor_npc_id in npcs)
        )
        checked.append(
            (file, "obligation.creditor_npc_id", obligation.creditor_npc_id in npcs)
        )
    for check in registry.checks.values():
        checked.append(
            (sources[check.id], "obligation_id", check.obligation_id in obligations)
        )

    start = registry.starting_state
    file = sources[start.id]
    checked.append((file, "world_id", start.world_id == registry.world.id))
    for i, position in enumerate(start.npc_positions):
        checked.append((file, f"npc_positions[{i}].npc_id", position.npc_id in npcs))
        checked.append(
            (
                file,
                f"npc_positions[{i}].location_id",
                position.location_id in locations,
            )
        )
    for i, stock in enumerate(start.item_stock):
        checked.append(
            (file, f"item_stock[{i}].holder_npc_id", stock.holder_npc_id in npcs)
        )
        checked.append(
            (file, f"item_stock[{i}].item_id", stock.item_id in registry.items)
        )
    for i, holding in enumerate(start.npc_gold):
        checked.append((file, f"npc_gold[{i}].npc_id", holding.npc_id in npcs))
    handover = start.handover
    checked.append((file, "handover.location_id", handover.location_id in locations))
    for i, npc in enumerate(handover.participant_npc_ids):
        checked.append((file, f"handover.participant_npc_ids[{i}]", npc in npcs))
    for i, npc in enumerate(handover.witness_npc_ids):
        checked.append((file, f"handover.witness_npc_ids[{i}]", npc in npcs))

    return tuple(
        ContentIssue(code="unresolved_reference", file=file, field=field)
        for file, field, resolved in checked
        if not resolved
    )
