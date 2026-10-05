from typing import cast

MAX_YAML_DEPTH = 64
MAX_YAML_NODES = 4096


def yaml_structure_valid(value: object) -> bool:
    """Reject cycles, excessive nesting and alias expansion before recursive validation.

    An iterative traversal bounds work independently of Python's recursion limit.
    For example, yaml_structure_valid({"ids": ["a"]}) is True.
    """
    pending: list[tuple[object, frozenset[int]]] = [(value, frozenset())]
    visited = 0
    while pending:
        node, ancestors = pending.pop()
        visited += 1
        if visited > MAX_YAML_NODES or len(ancestors) > MAX_YAML_DEPTH:
            return False
        identity = id(node)
        if not isinstance(node, (list, dict)):
            continue
        if identity in ancestors:
            return False
        parents = ancestors | {identity}
        if isinstance(node, list):
            children = cast(list[object], node)
        else:
            children = list(cast(dict[object, object], node).values())
        if len(children) + len(pending) + visited > MAX_YAML_NODES:
            return False
        pending.extend((child, parents) for child in children)
    return True
