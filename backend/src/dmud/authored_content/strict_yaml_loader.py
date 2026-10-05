from collections.abc import Hashable

import yaml
from yaml.constructor import ConstructorError
from yaml.nodes import MappingNode


class DuplicateYamlKey(ConstructorError):
    """A mapping repeats a key; carries only the key name, never the YAML body."""

    def __init__(self, key: str):
        super().__init__(problem="duplicate key")
        self.key = key


class StrictYamlLoader(yaml.SafeLoader):
    """SafeLoader that rejects duplicate mapping keys instead of keeping the last value.

    Plain yaml.safe_load silently accepts `id: a` followed by `id: b`. For example,
    yaml.load(text, Loader=StrictYamlLoader).
    """

    def construct_mapping(
        self, node: MappingNode, deep: bool = False
    ) -> dict[Hashable, object]:
        seen: set[Hashable] = set()
        for key_node, _ in node.value:
            key: object = self.construct_object(key_node, deep=deep)  # pyright: ignore[reportUnknownMemberType, reportUnknownVariableType]
            if not isinstance(key, Hashable):
                raise ConstructorError(problem="unhashable key")
            if key in seen:
                raise DuplicateYamlKey(str(key))
            seen.add(key)
        return super().construct_mapping(node, deep=deep)
