from collections import Counter
from collections.abc import Mapping

from dmud.authored_content.approved_p0_content import (
    DRINK,
    DRINK_PRICE_GOLD,
    DRINK_STOCK,
    MARA,
    PREPARED_POUCH_GOLD,
)
from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.content_registry import ContentRegistry


def check_fixture_funding(
    registry: ContentRegistry, sources: Mapping[str, str]
) -> tuple[ContentIssue, ...]:
    """Require the exact P0 economy: one 10,000-gold pouch, Mara's explicit funds, 5 one-gold drinks.

    The pouch is the player's only gold by construction (the starting state has no other
    player-gold field). Every NPC gold holding is explicit and listed at most once. For
    example, check_fixture_funding(registry, sources) == () for the committed package.
    """
    issues: list[ContentIssue] = []
    start = registry.starting_state
    file = sources[start.id]
    if start.prepared_pouch.gold != PREPARED_POUCH_GOLD:
        issues.append(
            ContentIssue(
                code="fixture_funding_mismatch",
                file=file,
                field="prepared_pouch.gold",
            )
        )
    holders = Counter(holding.npc_id for holding in start.npc_gold)
    if holders[MARA] != 1 or any(count > 1 for count in holders.values()):
        issues.append(
            ContentIssue(code="fixture_funding_mismatch", file=file, field="npc_gold")
        )
    stock = [(s.holder_npc_id, s.item_id, s.quantity) for s in start.item_stock]
    if stock != [(MARA, DRINK, DRINK_STOCK)]:
        issues.append(
            ContentIssue(code="fixture_funding_mismatch", file=file, field="item_stock")
        )
    drink = registry.items.get(DRINK)
    if drink is None or drink.price_gold != DRINK_PRICE_GOLD:
        issues.append(
            ContentIssue(
                code="fixture_funding_mismatch",
                file=sources.get(DRINK, ""),
                field="price_gold",
            )
        )
    return tuple(issues)
