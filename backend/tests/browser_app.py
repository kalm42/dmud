"""Real browser-test composition with per-request scheduling barriers, never release routes."""

import asyncio
from pathlib import Path

from fastapi import Request

from dmud.main import create_app
from dmud.operations.execution_hooks import ExecutionHooks
from dmud.operations.get_operation import get_operation

barriers: dict[str, asyncio.Event] = {}
reached: set[str] = set()
failures: set[str] = set()


async def pause(operation_id: str) -> None:
    path: Path = app.state.database_path
    operation = get_operation(path, operation_id)
    request_id = operation.request_id
    gate = barriers.get(request_id)
    if gate is not None:
        reached.add(request_id)
        await gate.wait()
    if request_id in failures:
        failures.remove(request_id)
        raise OSError("Controlled infrastructure failure")


app = create_app(execution_hooks=ExecutionHooks(before_commit=pause))


@app.post("/__test__/barriers/{request_id}")
async def arm(request_id: str, fail: bool = False) -> dict[str, bool]:
    barriers[request_id] = asyncio.Event()
    if fail:
        failures.add(request_id)
    return {"armed": True}


@app.get("/__test__/barriers/{request_id}")
async def status(request_id: str) -> dict[str, bool]:
    return {"reached": request_id in reached}


@app.post("/__test__/barriers/{request_id}/release")
async def release(request_id: str, request: Request) -> dict[str, bool]:
    barriers[request_id].set()
    return {"released": True}
