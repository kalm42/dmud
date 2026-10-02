import asyncio
import importlib
import sqlite3
import threading
from pathlib import Path

import httpx
import pytest

from dmud.main import create_app
from dmud.operations.accept_operation import accept_operation
from dmud.operations.get_operation import get_operation
from dmud.operations.get_request_operation import get_request_operation
from dmud.operations.transition_operation import transition_operation
from dmud.platform.settings import Settings
from dmud.platform.sqlite.connect_database import connect_database
from dmud.platform.sqlite.initialize_database import initialize_database
from dmud.session_zero.models import CreateSessionZeroDraft


@pytest.mark.parametrize("action", ["create", "retry"])
def test_cancelled_transport_drains_acceptance_and_wakes_the_worker(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, action: str
) -> None:
    path = initialize_database(tmp_path)
    request_id = "req_00000000-0000-4000-8000-000000000055"
    url = "/api/session-zero-drafts"
    payload: dict[str, str | int] = {"requestId": request_id}
    if action == "retry":
        operation = accept_operation(path, CreateSessionZeroDraft(requestId=request_id))
        interrupted = transition_operation(path, operation.operation_id, "interrupted")
        url = operation.status_url + "/retry"
        payload = {
            "requestId": "req_00000000-0000-4000-8000-000000000056",
            "expectedLastEventId": interrupted.last_event_id,
        }
    waiting = threading.Event()
    module_name = "accept_operation" if action == "create" else "recover_operation"
    module = importlib.import_module(f"dmud.operations.{module_name}")

    def traced_connection(database_path: Path) -> sqlite3.Connection:
        db = connect_database(database_path)
        db.set_trace_callback(
            lambda statement: waiting.set() if statement == "BEGIN IMMEDIATE" else None
        )
        return db

    # Gate a real ASGI request on a real second-connection SQLite lock.
    monkeypatch.setattr(module, "connect_database", traced_connection)
    app = create_app(settings=Settings(application_data_directory=tmp_path))

    async def scenario() -> None:
        async with (
            app.router.lifespan_context(app),
            httpx.AsyncClient(
                transport=httpx.ASGITransport(app=app), base_url="http://localhost"
            ) as client,
        ):
            with sqlite3.connect(path) as blocker:
                blocker.execute("BEGIN IMMEDIATE")
                submitting = asyncio.create_task(client.post(url, json=payload))
                try:
                    assert await asyncio.to_thread(waiting.wait, 2)
                    submitting.cancel()
                    await asyncio.sleep(0)
                    submitting.cancel()
                    await asyncio.sleep(0)
                    assert not submitting.done()
                finally:
                    blocker.rollback()
                with pytest.raises(asyncio.CancelledError):
                    await submitting
            recovered = get_request_operation(path, request_id)
            assert recovered is not None
            async with asyncio.timeout(3):
                while (
                    await asyncio.to_thread(get_operation, path, recovered.operation_id)
                ).status != "complete":
                    await asyncio.sleep(0.01)

    asyncio.run(scenario())
