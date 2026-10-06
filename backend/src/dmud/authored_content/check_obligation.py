from collections.abc import Mapping

from dmud.authored_content.approved_p0_content import (
    MARA,
    OBLIGATION_DUE_SECOND,
    OBLIGATION_GOLD,
    OREN,
    PAYMENT_EXTENSION_DIFFICULTY,
    PAYMENT_EXTENSION_SECONDS,
)
from dmud.authored_content.content_issue import ContentIssue
from dmud.authored_content.content_registry import ContentRegistry


def check_obligation(
    registry: ContentRegistry, sources: Mapping[str, str]
) -> tuple[ContentIssue, ...]:
    """Require the one Mara-to-Oren obligation, owned by its conflict and checked by ID.

    Both parties must be conflict participants, and the payment-extension check must
    target that same obligation so no later story invents a second debt record. For
    example, check_obligation(registry, sources) == () for the committed package.
    """
    issues: list[ContentIssue] = []
    for conflict in registry.conflicts.values():
        file = sources[conflict.id]
        obligation = conflict.obligation
        if obligation.debtor_npc_id != MARA:
            issues.append(
                ContentIssue(
                    code="obligation_mismatch",
                    file=file,
                    field="obligation.debtor_npc_id",
                )
            )
        if obligation.creditor_npc_id != OREN:
            issues.append(
                ContentIssue(
                    code="obligation_mismatch",
                    file=file,
                    field="obligation.creditor_npc_id",
                )
            )
        for field, actual, expected in (
            ("outstanding_gold", obligation.outstanding_gold, OBLIGATION_GOLD),
            ("due_second", obligation.due_second, OBLIGATION_DUE_SECOND),
        ):
            if actual != expected:
                issues.append(
                    ContentIssue(
                        code="obligation_mismatch",
                        file=file,
                        field=f"obligation.{field}",
                    )
                )
        parties = {obligation.debtor_npc_id, obligation.creditor_npc_id}
        if not parties <= set(conflict.participant_npc_ids):
            issues.append(
                ContentIssue(
                    code="obligation_mismatch", file=file, field="participant_npc_ids"
                )
            )
    for check in registry.checks.values():
        for field, actual, expected in (
            ("difficulty", check.difficulty, PAYMENT_EXTENSION_DIFFICULTY),
            (
                "on_success.extend_due_by_seconds",
                check.on_success.extend_due_by_seconds,
                PAYMENT_EXTENSION_SECONDS,
            ),
        ):
            if actual != expected:
                issues.append(
                    ContentIssue(
                        code="obligation_mismatch", file=sources[check.id], field=field
                    )
                )
    obligations = {c.obligation.id for c in registry.conflicts.values()}
    targeted = {check.obligation_id for check in registry.checks.values()}
    if targeted != obligations:
        for check in registry.checks.values():
            issues.append(
                ContentIssue(
                    code="obligation_mismatch",
                    file=sources[check.id],
                    field="obligation_id",
                )
            )
    return tuple(issues)
