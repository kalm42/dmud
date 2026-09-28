from dmud.operations.models import OperationStatus

TRANSITIONS: dict[OperationStatus, frozenset[OperationStatus]] = {
    "accepted": frozenset({"validating", "interrupted", "failed"}),
    "validating": frozenset({"committed", "interrupted", "failed"}),
    "committed": frozenset({"complete"}),
    "complete": frozenset(),
    "failed": frozenset({"accepted"}),
    "interrupted": frozenset({"accepted"}),
}


def legal_transition(current: OperationStatus, target: OperationStatus) -> bool:
    """Decide lifecycle legality without side effects; e.g. legal_transition('accepted', 'validating')."""
    return target in TRANSITIONS[current]
