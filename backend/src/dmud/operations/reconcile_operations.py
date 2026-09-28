from pathlib import Path

from dmud.operations.list_nonterminal import list_nonterminal
from dmud.operations.transition_operation import transition_operation


def reconcile_operations(path: Path) -> None:
    """Recover results first without rerunning uncommitted commands; e.g. reconcile_operations(path)."""
    for operation in list_nonterminal(path):
        target = "complete" if operation.result is not None else "interrupted"
        transition_operation(path, operation.operation_id, target)
