import asyncio
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager, suppress

from fastapi import FastAPI

from dmud.operations.execution_hooks import ExecutionHooks
from dmud.operations.reconcile_operations import reconcile_operations
from dmud.operations.run_worker import run_worker
from dmud.platform.settings import Settings
from dmud.platform.sqlite.initialize_database import initialize_database
from dmud.platform.sqlite.run_database import run_database


@asynccontextmanager
async def application_lifespan(app: FastAPI) -> AsyncGenerator[None]:
    """Own application data only while serving; e.g. FastAPI(lifespan=application_lifespan)."""
    settings: Settings = app.state.settings
    app.state.database_path = await run_database(
        initialize_database, settings.application_data_directory
    )
    await run_database(reconcile_operations, app.state.database_path)
    app.state.wake = asyncio.Event()
    hooks: ExecutionHooks = app.state.execution_hooks
    worker = asyncio.create_task(
        run_worker(app.state.database_path, app.state.wake, hooks)
    )
    try:
        yield
    finally:
        worker.cancel()
        with suppress(asyncio.CancelledError):
            await worker
        await run_database(reconcile_operations, app.state.database_path)
