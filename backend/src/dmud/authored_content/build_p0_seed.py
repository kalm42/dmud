import hashlib

from dmud.authored_content.canonical_seed import canonical_seed
from dmud.authored_content.content_registry import ContentRegistry
from dmud.authored_content.p0_starting_seed import (
    P0StartingSeed,
    SeedHandoverPerception,
    SeedNpc,
    SeedNpcGold,
    SeedObligation,
    SeedPouch,
    SeedStock,
)


def build_p0_seed(registry: ContentRegistry) -> P0StartingSeed:
    """Map validated content to the deterministic, immutable P0 pre-confirmation seed.

    Pure: it creates no campaign, branch, clock, database row, or player character.
    Collections are sorted by stable ID so the same registry always yields a
    byte-identical canonical seed and digest. Purchase, gift, and no-gift branches each
    start from their own copy. For example, build_p0_seed(loaded.registry).digest.
    """
    start = registry.starting_state
    handover = start.handover
    involved = {*handover.participant_npc_ids, *handover.witness_npc_ids}
    unhashed = P0StartingSeed(
        content_version=registry.version,
        fixture_origin_id=start.fixture_origin_id,
        location_ids=tuple(sorted(registry.locations)),
        npcs=tuple(
            SeedNpc(npc_id=p.npc_id, location_id=p.location_id)
            for p in sorted(start.npc_positions, key=lambda p: p.npc_id)
        ),
        item_stock=tuple(
            SeedStock(
                holder_npc_id=s.holder_npc_id,
                item_id=s.item_id,
                quantity=s.quantity,
                unit_price_gold=registry.items[s.item_id].price_gold,
            )
            for s in sorted(
                start.item_stock, key=lambda s: (s.holder_npc_id, s.item_id)
            )
        ),
        npc_gold=tuple(
            SeedNpcGold(npc_id=g.npc_id, gold=g.gold)
            for g in sorted(start.npc_gold, key=lambda g: g.npc_id)
        ),
        prepared_pouch=SeedPouch(
            pouch_id=start.prepared_pouch.id,
            gold=start.prepared_pouch.gold,
            funding_origin=start.prepared_pouch.funding_origin,
            fixture_origin_id=start.fixture_origin_id,
        ),
        obligations=tuple(
            SeedObligation(
                obligation_id=c.obligation.id,
                debtor_npc_id=c.obligation.debtor_npc_id,
                creditor_npc_id=c.obligation.creditor_npc_id,
                outstanding_gold=c.obligation.outstanding_gold,
                due_second=c.obligation.due_second,
            )
            for c in sorted(registry.conflicts.values(), key=lambda c: c.obligation.id)
        ),
        handover_perception=SeedHandoverPerception(
            location_id=handover.location_id,
            participant_npc_ids=tuple(sorted(handover.participant_npc_ids)),
            witness_npc_ids=tuple(sorted(handover.witness_npc_ids)),
            unaware_npc_ids=tuple(sorted(set(registry.npcs) - involved)),
        ),
        digest="",
    )
    digest = "sha256:" + hashlib.sha256(canonical_seed(unhashed)).hexdigest()
    return unhashed.model_copy(update={"digest": digest})
