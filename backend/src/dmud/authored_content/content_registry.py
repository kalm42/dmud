from collections.abc import Mapping
from dataclasses import dataclass

from dmud.authored_content.models import (
    Check,
    ContentVersion,
    Item,
    Location,
    MovementRules,
    Npc,
    SocialConflict,
    StartingState,
    World,
)


@dataclass(frozen=True, slots=True)
class ContentRegistry:
    """Immutable, validated P0 content keyed by stable ID.

    Mappings are read-only proxies and every value is a frozen model, so no caller can
    change loaded content. Production never hot-reloads it. For example,
    registry.locations["location:brackenford:market-square"].name.
    """

    version: ContentVersion
    movement: MovementRules
    world: World
    locations: Mapping[str, Location]
    npcs: Mapping[str, Npc]
    items: Mapping[str, Item]
    conflicts: Mapping[str, SocialConflict]
    checks: Mapping[str, Check]
    starting_state: StartingState
