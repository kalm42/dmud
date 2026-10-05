from dmud.authored_content.models import Check, PaymentObligation


def extended_due_second(
    obligation: PaymentObligation, check: Check, succeeded: bool
) -> int:
    """The obligation's due second after a payment-extension check outcome.

    Success adds the check's authored extension; failure leaves the deadline unchanged.
    Story 1.24 commits the result against the same obligation record. For example,
    extended_due_second(obligation, check, succeeded=True) == 201_600.
    """
    if succeeded:
        return obligation.due_second + check.on_success.extend_due_by_seconds
    return obligation.due_second
