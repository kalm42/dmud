"""Strict, immutable models for authored YAML documents and the content version.

Every model forbids unknown fields and coercion. Sequences are tuples so a validated
document cannot be mutated after loading.
"""

from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, StringConstraints

_SEGMENT = r"[a-z0-9]+(?:-[a-z0-9]+)*"
_NAMESPACED = rf":{_SEGMENT}:{_SEGMENT}$"

LocationId = Annotated[str, StringConstraints(pattern="^location" + _NAMESPACED)]
NpcId = Annotated[str, StringConstraints(pattern="^npc" + _NAMESPACED)]
ItemId = Annotated[str, StringConstraints(pattern="^item" + _NAMESPACED)]
RouteId = Annotated[str, StringConstraints(pattern="^route" + _NAMESPACED)]
ObligationId = Annotated[str, StringConstraints(pattern="^obligation" + _NAMESPACED)]
ConflictId = Annotated[str, StringConstraints(pattern="^conflict" + _NAMESPACED)]
CheckId = Annotated[str, StringConstraints(pattern="^check" + _NAMESPACED)]
StartId = Annotated[str, StringConstraints(pattern="^start" + _NAMESPACED)]
FixtureId = Annotated[str, StringConstraints(pattern="^fixture" + _NAMESPACED)]
PouchId = Annotated[str, StringConstraints(pattern="^pouch" + _NAMESPACED)]
WorldId = Annotated[str, StringConstraints(pattern=rf"^world:{_SEGMENT}$")]
MovementModeId = Annotated[str, StringConstraints(pattern=rf"^movement:{_SEGMENT}$")]
RulesId = Annotated[str, StringConstraints(pattern=rf"^rules:{_SEGMENT}$")]
PackageId = Annotated[str, StringConstraints(pattern=rf"^package:{_SEGMENT}$")]
Name = Annotated[str, StringConstraints(min_length=1, max_length=80)]
Prose = Annotated[str, StringConstraints(min_length=1, max_length=2000)]
PositiveInt = Annotated[int, Field(gt=0)]
NonNegativeInt = Annotated[int, Field(ge=0)]


class ContentModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True, frozen=True)


class Manifest(ContentModel):
    kind: Literal["manifest"]
    content_schema_version: PositiveInt
    package_id: PackageId
    package_version: Annotated[
        str, StringConstraints(pattern=r"^[0-9]+\.[0-9]+\.[0-9]+$", max_length=80)
    ]


class MovementMode(ContentModel):
    id: MovementModeId
    name: Name
    speed_mm_per_second: PositiveInt


class MovementRules(ContentModel):
    kind: Literal["movement_rules"]
    id: RulesId
    travel_rounding: Literal["ceil_whole_second"]
    modes: tuple[MovementMode, ...]


class Route(ContentModel):
    id: RouteId
    endpoint_ids: tuple[LocationId, LocationId]
    length_mm: PositiveInt


class World(ContentModel):
    kind: Literal["world"]
    id: WorldId
    name: Name
    routes: tuple[Route, ...]


class Exit(ContentModel):
    route_id: RouteId
    to_location_id: LocationId
    label: Annotated[Name, StringConstraints(pattern=r"\S")]


class Location(ContentModel):
    kind: Literal["location"]
    id: LocationId
    name: Name
    introduction: Prose
    exits: tuple[Exit, ...]


class Npc(ContentModel):
    kind: Literal["npc"]
    id: NpcId
    name: Name
    role: Name


class Item(ContentModel):
    kind: Literal["item"]
    id: ItemId
    name: Name
    identity: Literal["fungible"]
    price_gold: PositiveInt


class PaymentObligation(ContentModel):
    id: ObligationId
    debtor_npc_id: NpcId
    creditor_npc_id: NpcId
    outstanding_gold: PositiveInt
    due_second: NonNegativeInt


class SocialConflict(ContentModel):
    kind: Literal["social_conflict"]
    id: ConflictId
    name: Name
    summary: Prose
    participant_npc_ids: tuple[NpcId, ...]
    obligation: PaymentObligation


class DeadlineExtension(ContentModel):
    extend_due_by_seconds: PositiveInt


class Check(ContentModel):
    kind: Literal["check"]
    id: CheckId
    name: Name
    attribute: Literal["presence"]
    skill: Literal["persuasion"]
    difficulty: PositiveInt
    obligation_id: ObligationId
    on_success: DeadlineExtension
    on_failure: Literal["leave_unchanged"]


class NpcPosition(ContentModel):
    npc_id: NpcId
    location_id: LocationId


class ItemStock(ContentModel):
    holder_npc_id: NpcId
    item_id: ItemId
    quantity: PositiveInt


class NpcGold(ContentModel):
    npc_id: NpcId
    gold: NonNegativeInt


class PreparedPouch(ContentModel):
    id: PouchId
    gold: PositiveInt
    funding_origin: Literal["p0_test_fixture"]


class Handover(ContentModel):
    location_id: LocationId
    participant_npc_ids: tuple[NpcId, ...]
    witness_npc_ids: tuple[NpcId, ...]


class StartingState(ContentModel):
    kind: Literal["starting_state"]
    id: StartId
    world_id: WorldId
    fixture_origin_id: FixtureId
    npc_positions: tuple[NpcPosition, ...]
    item_stock: tuple[ItemStock, ...]
    npc_gold: tuple[NpcGold, ...]
    prepared_pouch: PreparedPouch
    handover: Handover


ContentDocument = Annotated[
    Manifest
    | MovementRules
    | World
    | Location
    | Npc
    | Item
    | SocialConflict
    | Check
    | StartingState,
    Field(discriminator="kind"),
]


class SourcedDocument(ContentModel):
    """A validated document and the content-relative file it came from."""

    path: str
    document: ContentDocument


class ContentVersion(ContentModel):
    content_schema_version: PositiveInt
    package_id: PackageId
    package_version: str
