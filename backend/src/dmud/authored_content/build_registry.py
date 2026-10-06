from collections.abc import Sequence
from types import MappingProxyType

from dmud.authored_content.content_registry import ContentRegistry
from dmud.authored_content.models import (
    Check,
    ContentVersion,
    Item,
    Location,
    Manifest,
    MovementRules,
    Npc,
    SocialConflict,
    SourcedDocument,
    StartingState,
    World,
)


def build_registry(documents: Sequence[SourcedDocument]) -> ContentRegistry:
    """Index structurally valid documents by stable ID into an immutable registry.

    Callers run check_approved_inventory first, so each singleton kind is present exactly
    once. For example, build_registry(documents).npcs["npc:brackenford:mara"].
    """
    parsed = [source.document for source in documents]
    manifest = next(d for d in parsed if isinstance(d, Manifest))
    return ContentRegistry(
        version=ContentVersion(
            content_schema_version=manifest.content_schema_version,
            package_id=manifest.package_id,
            package_version=manifest.package_version,
        ),
        movement=next(d for d in parsed if isinstance(d, MovementRules)),
        world=next(d for d in parsed if isinstance(d, World)),
        locations=MappingProxyType(
            {d.id: d for d in parsed if isinstance(d, Location)}
        ),
        npcs=MappingProxyType({d.id: d for d in parsed if isinstance(d, Npc)}),
        items=MappingProxyType({d.id: d for d in parsed if isinstance(d, Item)}),
        conflicts=MappingProxyType(
            {d.id: d for d in parsed if isinstance(d, SocialConflict)}
        ),
        checks=MappingProxyType({d.id: d for d in parsed if isinstance(d, Check)}),
        starting_state=next(d for d in parsed if isinstance(d, StartingState)),
    )
