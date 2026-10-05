from dmud.authored_content.models import (
    ContentDocument,
    Manifest,
    MovementRules,
    SocialConflict,
    StartingState,
    World,
)


def declared_ids(document: ContentDocument) -> tuple[tuple[str, str], ...]:
    """List every stable ID a document declares, with the field path that declares it.

    Nested definitions (routes, movement modes, the obligation, the pouch, the fixture
    origin) share one ID space with top-level documents. For example,
    declared_ids(world) == (("world:brackenford", "id"), ("route:...", "routes[0].id"), ...).
    """
    if isinstance(document, Manifest):
        return ((document.package_id, "package_id"),)
    ids = [(document.id, "id")]
    if isinstance(document, World):
        ids += [
            (route.id, f"routes[{i}].id") for i, route in enumerate(document.routes)
        ]
    elif isinstance(document, MovementRules):
        ids += [(mode.id, f"modes[{i}].id") for i, mode in enumerate(document.modes)]
    elif isinstance(document, SocialConflict):
        ids.append((document.obligation.id, "obligation.id"))
    elif isinstance(document, StartingState):
        ids.append((document.fixture_origin_id, "fixture_origin_id"))
        ids.append((document.prepared_pouch.id, "prepared_pouch.id"))
    return tuple(ids)
