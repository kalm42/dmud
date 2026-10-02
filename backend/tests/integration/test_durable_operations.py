from pathlib import Path

from dmud.operations.accept_operation import accept_operation
from dmud.operations.commit_draft import commit_draft
from dmud.operations.get_operation import get_operation
from dmud.operations.reconcile_operations import reconcile_operations
from dmud.operations.transition_operation import transition_operation
from dmud.platform.sqlite.initialize_database import initialize_database
from dmud.session_zero.models import CreateSessionZeroDraft

REQUEST = CreateSessionZeroDraft(requestId="req_00000000-0000-4000-8000-000000000001")


def test_acceptance_is_durable_without_committed_draft(tmp_path: Path) -> None:
    path = initialize_database(tmp_path)
    operation = accept_operation(path, REQUEST)
    assert get_operation(path, operation.operation_id) == operation
    assert operation.commit_boundary == "none"
    assert operation.last_event_id == 1


def test_same_request_recovers_original_identity(tmp_path: Path) -> None:
    path = initialize_database(tmp_path)
    first = accept_operation(path, REQUEST)
    second = accept_operation(path, REQUEST)
    assert second == first


def test_restart_interrupts_uncommitted_work(tmp_path: Path) -> None:
    path = initialize_database(tmp_path)
    operation = accept_operation(path, REQUEST)
    reconcile_operations(path)
    recovered = get_operation(path, operation.operation_id)
    assert recovered.status == "interrupted"
    assert recovered.recovery.retry is True


def test_restart_preserves_committed_result(tmp_path: Path) -> None:
    path = initialize_database(tmp_path)
    operation = accept_operation(path, REQUEST)
    transition_operation(path, operation.operation_id, "validating")
    committed = commit_draft(path, operation.operation_id)
    reconcile_operations(path)
    recovered = get_operation(path, operation.operation_id)
    assert recovered.status == "complete"
    assert recovered.result == committed.result
    assert recovered.committed_revision == 1


def test_concurrent_acceptance_has_one_identity(tmp_path: Path) -> None:
    from concurrent.futures import ThreadPoolExecutor

    path = initialize_database(tmp_path)
    with ThreadPoolExecutor(max_workers=8) as executor:
        operations = list(
            executor.map(lambda _: accept_operation(path, REQUEST), range(16))
        )
    assert len({op.operation_id for op in operations}) == 1
    assert len({op.subject.draft_id for op in operations}) == 1


def test_commit_failure_rolls_back_all_authoritative_artifacts(tmp_path: Path) -> None:
    import sqlite3

    import pytest

    path = initialize_database(tmp_path)
    operation = accept_operation(path, REQUEST)
    transition_operation(path, operation.operation_id, "validating")
    with sqlite3.connect(path) as db:
        db.execute(
            "CREATE TRIGGER inject_failure BEFORE INSERT ON request_results BEGIN SELECT RAISE(ABORT, 'controlled write failure'); END"
        )
    with pytest.raises(sqlite3.IntegrityError):
        commit_draft(path, operation.operation_id)
    with sqlite3.connect(path) as db:
        for table in ("session_zero_drafts", "draft_commits", "request_results"):
            assert db.execute(f"SELECT count(*) FROM {table}").fetchone()[0] == 0
    assert get_operation(path, operation.operation_id).commit_boundary == "none"


def test_changed_payload_digest_conflicts_with_original_identity(
    tmp_path: Path,
) -> None:
    import sqlite3

    import pytest

    from dmud.operations.models import OperationError

    path = initialize_database(tmp_path)
    accept_operation(path, REQUEST)
    # Creation has no optional material: corrupting the stored identity simulates a changed canonical envelope.
    with sqlite3.connect(path) as db:
        db.execute("UPDATE operations SET payload_digest = 'different'")
    with pytest.raises(OperationError, match="request_conflict"):
        accept_operation(path, REQUEST)


def test_retry_reuses_original_subject(tmp_path: Path) -> None:
    from dmud.operations.models import RecoveryCommand
    from dmud.operations.recover_operation import recover_operation

    path = initialize_database(tmp_path)
    original = accept_operation(path, REQUEST)
    interrupted = transition_operation(path, original.operation_id, "interrupted")
    command = RecoveryCommand(
        requestId="req_00000000-0000-4000-8000-000000000009",
        expectedLastEventId=interrupted.last_event_id,
    )
    retried = recover_operation(path, original.operation_id, command, "retry")
    duplicate = recover_operation(path, original.operation_id, command, "retry")
    assert retried == duplicate
    assert retried.subject == original.subject
    assert retried.request_id == original.request_id


def test_committed_retry_returns_original_result(tmp_path: Path) -> None:
    from dmud.operations.models import RecoveryCommand
    from dmud.operations.recover_operation import recover_operation

    path = initialize_database(tmp_path)
    original = accept_operation(path, REQUEST)
    transition_operation(path, original.operation_id, "validating")
    committed = commit_draft(path, original.operation_id)
    command = RecoveryCommand(
        requestId="req_00000000-0000-4000-8000-000000000009", expectedLastEventId=1
    )
    assert (
        recover_operation(path, original.operation_id, command, "retry").result
        == committed.result
    )


def test_concurrent_claims_have_one_executing_attempt(tmp_path: Path) -> None:
    from concurrent.futures import ThreadPoolExecutor

    from dmud.operations.claim_operation import claim_operation

    path = initialize_database(tmp_path)
    operation = accept_operation(path, REQUEST)
    with ThreadPoolExecutor(max_workers=8) as executor:
        claims = list(
            executor.map(
                lambda _: claim_operation(path, operation.operation_id), range(8)
            )
        )
    assert sum(claim is not None for claim in claims) == 1


def test_simultaneous_retries_open_only_one_attempt(tmp_path: Path) -> None:
    from concurrent.futures import ThreadPoolExecutor

    from dmud.operations.models import RecoveryCommand
    from dmud.operations.recover_operation import recover_operation

    path = initialize_database(tmp_path)
    original = accept_operation(path, REQUEST)
    interrupted = transition_operation(path, original.operation_id, "interrupted")
    command = RecoveryCommand(
        requestId="req_00000000-0000-4000-8000-000000000009",
        expectedLastEventId=interrupted.last_event_id,
    )
    with ThreadPoolExecutor(max_workers=8) as executor:
        retries = list(
            executor.map(
                lambda _: recover_operation(
                    path, original.operation_id, command, "retry"
                ),
                range(8),
            )
        )
    assert all(retry == retries[0] for retry in retries)
    assert (
        get_operation(path, original.operation_id).last_event_id
        == interrupted.last_event_id + 1
    )
