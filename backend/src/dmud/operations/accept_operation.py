from contextlib import closing
from pathlib import Path
from uuid import uuid7

from dmud.operations.models import (
    Operation,
    OperationError,
    RecoveryCapability,
    Subject,
)
from dmud.operations.payload_digest import payload_digest
from dmud.operations.read_operation import read_operation
from dmud.operations.write_event import write_event
from dmud.platform.sqlite.connect_database import connect_database
from dmud.session_zero.models import CreateSessionZeroDraft


def accept_operation(path: Path, request: CreateSessionZeroDraft) -> Operation:
    """Durably accept one logical request before revealing its identity; e.g. accept_operation(path, request)."""
    digest = payload_digest(request)
    with closing(connect_database(path)) as db, db:
        db.execute("BEGIN IMMEDIATE")
        existing = db.execute(
            "SELECT operation_id, payload_digest FROM operations WHERE request_id = ?",
            (request.request_id,),
        ).fetchone()
        if existing:
            operation = read_operation(db, existing[0])
            if existing[1] != digest:
                raise OperationError("request_conflict", operation=operation)
            return operation
        operation_id = "op_" + str(uuid7())
        operation = Operation(
            operation_id=operation_id,
            request_id=request.request_id,
            subject=Subject(draft_id="draft_" + str(uuid7())),
            status="accepted",
            commit_boundary="none",
            committed_revision=None,
            last_event_id=1,
            recovery=RecoveryCapability(retry=False, cancel=True),
            result=None,
            status_url=f"/api/operations/{operation_id}",
            events_url=f"/api/operations/{operation_id}/events",
        )
        db.execute(
            "INSERT INTO operations VALUES (?, ?, ?, ?, ?, ?)",
            (
                operation.operation_id,
                request.request_id,
                operation.subject.draft_id,
                digest,
                request.model_dump_json(by_alias=True),
                operation.model_dump_json(by_alias=True),
            ),
        )
        write_event(db, operation)
        return operation
