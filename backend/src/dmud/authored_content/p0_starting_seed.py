"""Typed, immutable pre-confirmation seed for the P0 starting world.

The seed is plain branch-ready state, not a campaign: it has no clock, branch, save,
player character, attributes, or inventory row. Story 1.9 instantiates it.
"""

from typing import Literal

from pydantic import BaseModel, ConfigDict

from dmud.authored_content.models import ContentVersion


class SeedModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)


class SeedNpc(SeedModel):
    npc_id: str
    location_id: str


class SeedStock(SeedModel):
    holder_npc_id: str
    item_id: str
    quantity: int
    unit_price_gold: int


class SeedNpcGold(SeedModel):
    npc_id: str
    gold: int


class SeedPouch(SeedModel):
    pouch_id: str
    holder: Literal["player"] = "player"
    gold: int
    funding_origin: Literal["p0_test_fixture"]
    fixture_origin_id: str


class SeedObligation(SeedModel):
    obligation_id: str
    debtor_npc_id: str
    creditor_npc_id: str
    outstanding_gold: int
    due_second: int


class SeedHandoverPerception(SeedModel):
    location_id: str
    participant_npc_ids: tuple[str, ...]
    witness_npc_ids: tuple[str, ...]
    unaware_npc_ids: tuple[str, ...]


class P0StartingSeed(SeedModel):
    content_version: ContentVersion
    fixture_origin_id: str
    location_ids: tuple[str, ...]
    npcs: tuple[SeedNpc, ...]
    item_stock: tuple[SeedStock, ...]
    npc_gold: tuple[SeedNpcGold, ...]
    prepared_pouch: SeedPouch
    obligations: tuple[SeedObligation, ...]
    handover_perception: SeedHandoverPerception
    digest: str
