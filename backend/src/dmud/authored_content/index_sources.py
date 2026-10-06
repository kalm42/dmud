from collections.abc import Mapping, Sequence
from types import MappingProxyType

from dmud.authored_content.declared_ids import declared_ids
from dmud.authored_content.models import SourcedDocument


def index_sources(documents: Sequence[SourcedDocument]) -> Mapping[str, str]:
    """Map each declared stable ID to its content-relative file, for issue reporting.

    For example, index_sources(documents)["npc:brackenford:mara"] == "worlds/brackenford/npcs/mara.yaml".
    """
    return MappingProxyType(
        {
            content_id: source.path
            for source in documents
            for content_id, _ in declared_ids(source.document)
        }
    )
