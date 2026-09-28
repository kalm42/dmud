from contextlib import closing
from pathlib import Path
from typing import Literal

from dmud.operations.models import (
    Operation,
    OperationError,
    RecoveryCapability,
    RecoveryCommand,
)
from dmud.operations.payload_digest import payload_digest
from dmud.operations.read_operation import read_operation
from dmud.operations.write_event import write_event
from dmud.platform.sqlite.connect_database import connect_database


def recover_operation(
    path: Path,
    operation_id: str,
    command: RecoveryCommand,
    action: Literal["cancel", "retry"],
) -> Operation:
    """Serialize idempotent recovery against authoritative result; e.g. recover_operation(path, id, command, 'retry')."""
    digest = payload_digest(command, operation_id + action)
    with closing(connect_database(path)) as db, db:
        db.execute("BEGIN IMMEDIATE")
        existing = db.execute(
            "SELECT payload_digest, resource FROM recovery_commands WHERE request_id = ?",
            (command.request_id,),
        ).fetchone()
        if existing:
            if existing[0] != digest:
                raise OperationError("request_conflict")
            outcome = Operation.model_validate_json(existing[1])
            return read_operation(db, outcome.operation_id)
        operation = read_operation(db, operation_id)
        if operation.result is not None:
            updated = operation
            if action == "cancel" and operation.status == "committed":
                updated = operation.model_copy(
                    update={
                        "status": "complete",
                        "last_event_id": operation.last_event_id + 1,
                    }
                )
                write_event(db, updated)
        else:
            if (
                action == "retry"
                and db.execute(
                    "SELECT 1 FROM session_zero_drafts WHERE draft_id = ?",
                    (operation.subject.draft_id,),
                ).fetchone()
            ):
                raise OperationError("draft_already_committed", operation=operation)
            if operation.last_event_id != command.expected_last_event_id:
                raise OperationError("stale_event", operation=operation)
            eligible = (
                operation.recovery.retry
                if action == "retry"
                else operation.recovery.cancel
            )
            if not eligible:
                raise OperationError("recovery_not_supported", operation=operation)
            target = "accepted" if action == "retry" else "interrupted"
            updated = operation.model_copy(
                update={
                    "status": target,
                    "last_event_id": operation.last_event_id + 1,
                    "recovery": RecoveryCapability(
                        retry=target == "interrupted", cancel=target == "accepted"
                    ),
                }
            )
            write_event(db, updated)
        db.execute(
            "INSERT INTO recovery_commands VALUES (?, ?, ?, ?)",
            (
                command.request_id,
                operation_id,
                digest,
                updated.model_dump_json(by_alias=True),
            ),
        )
        return updated
