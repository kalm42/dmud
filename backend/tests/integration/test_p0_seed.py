import pytest
from pydantic import ValidationError

from dmud.authored_content.build_p0_seed import build_p0_seed
from dmud.authored_content.canonical_seed import canonical_seed
from dmud.authored_content.content_registry import ContentRegistry
from dmud.authored_content.content_result import ContentLoaded
from dmud.authored_content.load_content import load_content
from dmud.authored_content.p0_starting_seed import P0StartingSeed
from dmud.platform.settings import REPOSITORY_CONTENT_DIRECTORY

MARA = "npc:brackenford:mara"
OREN = "npc:brackenford:oren"
TESSA = "npc:brackenford:tessa"
IVO = "npc:brackenford:ivo"


def registry() -> ContentRegistry:
    result = load_content(REPOSITORY_CONTENT_DIRECTORY)
    assert isinstance(result, ContentLoaded)
    return result.registry


def seed() -> P0StartingSeed:
    return build_p0_seed(registry())


class TestBuildP0Seed:
    def test_provides_the_three_locations(self) -> None:
        assert seed().location_ids == (
            "location:brackenford:common-room",
            "location:brackenford:maras-stall",
            "location:brackenford:market-square",
        )

    def test_positions_each_npc_once(self) -> None:
        positions = {npc.npc_id: npc.location_id for npc in seed().npcs}
        assert positions == {
            MARA: "location:brackenford:maras-stall",
            TESSA: "location:brackenford:maras-stall",
            OREN: "location:brackenford:common-room",
            IVO: "location:brackenford:common-room",
        }

    def test_stocks_mara_with_five_one_gold_drinks(self) -> None:
        stock = [
            (s.holder_npc_id, s.item_id, s.quantity, s.unit_price_gold)
            for s in seed().item_stock
        ]
        assert stock == [(MARA, "item:brackenford:drink", 5, 1)]

    def test_states_maras_transaction_funds_explicitly(self) -> None:
        assert [(g.npc_id, g.gold) for g in seed().npc_gold] == [(MARA, 0)]

    def test_gives_the_player_one_fixture_funded_pouch_of_ten_thousand_gold(
        self,
    ) -> None:
        pouch = seed().prepared_pouch
        assert (pouch.holder, pouch.gold, pouch.funding_origin) == (
            "player",
            10_000,
            "p0_test_fixture",
        )

    def test_pouch_carries_the_immutable_fixture_origin(self) -> None:
        built = seed()
        assert built.prepared_pouch.fixture_origin_id == built.fixture_origin_id
        assert built.fixture_origin_id == "fixture:brackenford:p0-start"

    def test_holds_no_other_player_gold(self) -> None:
        document = seed().model_dump(exclude={"prepared_pouch"})
        holders = {g["npc_id"] for g in document["npc_gold"]}
        assert holders <= {MARA, OREN, TESSA, IVO}
        assert "player" not in str(document)

    def test_has_no_campaign_clock_or_character_state(self) -> None:
        assert set(P0StartingSeed.model_fields) == {
            "content_version",
            "fixture_origin_id",
            "location_ids",
            "npcs",
            "item_stock",
            "npc_gold",
            "prepared_pouch",
            "obligations",
            "handover_perception",
            "digest",
        }

    def test_handover_is_perceptible_to_tessa(self) -> None:
        assert seed().handover_perception.witness_npc_ids == (TESSA,)

    def test_handover_is_not_perceptible_to_oren_or_ivo(self) -> None:
        assert seed().handover_perception.unaware_npc_ids == (IVO, OREN)

    def test_records_the_content_version(self) -> None:
        version = seed().content_version
        assert (version.package_id, version.package_version) == (
            "package:brackenford-p0",
            "1.0.0",
        )

    def test_same_registry_yields_byte_identical_canonical_seed(self) -> None:
        loaded = registry()
        assert canonical_seed(build_p0_seed(loaded)) == canonical_seed(
            build_p0_seed(loaded)
        )

    def test_same_content_yields_the_same_digest(self) -> None:
        assert seed().digest == seed().digest

    def test_digest_covers_the_canonical_seed(self) -> None:
        built = seed()
        changed = built.model_copy(
            update={"fixture_origin_id": "fixture:brackenford:other"}
        )
        assert canonical_seed(changed) != canonical_seed(built)
        assert built.digest.startswith("sha256:")

    def test_seed_rejects_mutation(self) -> None:
        built = seed()
        with pytest.raises(ValidationError):
            built.fixture_origin_id = "fixture:brackenford:other"

    def test_changing_a_seed_copy_leaves_the_registry_unchanged(self) -> None:
        loaded = registry()
        original = build_p0_seed(loaded)
        original.model_copy(update={"location_ids": ()})
        assert build_p0_seed(loaded).digest == original.digest
