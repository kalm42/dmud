from collections.abc import Sequence

from dmud.authored_content.models import (
    Check,
    DeadlineExtension,
    Exit,
    Handover,
    Item,
    ItemStock,
    Location,
    Manifest,
    MovementMode,
    MovementRules,
    Npc,
    NpcGold,
    NpcPosition,
    PaymentObligation,
    PreparedPouch,
    Route,
    SocialConflict,
    StartingState,
    World,
)

_SCHEMA_FIELDS = frozenset(
    field
    for model in (
        Check,
        DeadlineExtension,
        Exit,
        Handover,
        Item,
        ItemStock,
        Location,
        Manifest,
        MovementMode,
        MovementRules,
        Npc,
        NpcGold,
        NpcPosition,
        PaymentObligation,
        PreparedPouch,
        Route,
        SocialConflict,
        StartingState,
        World,
    )
    for field in model.model_fields
)


def format_field_path(location: Sequence[int | str]) -> str:
    """Render a bounded schema field path without echoing arbitrary authored keys.

    For example, format_field_path(("exits", 0, "label")) == "exits[0].label".
    """
    path = ""
    for part in location:
        if isinstance(part, int):
            path += f"[{part}]"
        else:
            field = part if part in _SCHEMA_FIELDS else "<unknown>"
            path += f".{field}" if path else field
    return path[:256]
