import sqlite3

from fastapi import FastAPI

from dmud.get_status import get_status
from dmud.operations.execution_hooks import ExecutionHooks
from dmud.operations.register_operation_routes import register_operation_routes
from dmud.platform.application_lifespan import application_lifespan
from dmud.platform.require_sqlite import require_sqlite
from dmud.platform.settings import Settings
from dmud.saves.get_save_slots import get_save_slots
from dmud.saves.save_slots import SaveSlotsResponse
from dmud.status import StatusResponse


def create_app(
    sqlite_version: tuple[int, int, int] | None = None,
    settings: Settings | None = None,
    execution_hooks: ExecutionHooks | None = None,
) -> FastAPI:
    """Construct the local API after validation; for example, create_app()."""
    version = (
        sqlite_version if sqlite_version is not None else sqlite3.sqlite_version_info
    )
    require_sqlite(version)
    configuration = settings if settings is not None else Settings()
    app = FastAPI(
        title="dmud API",
        version="0.1.0",
        openapi_version="3.1.0",
        lifespan=application_lifespan,
    )
    app.state.settings = configuration
    app.state.execution_hooks = execution_hooks or ExecutionHooks()

    app.add_api_route(
        "/api/status",
        get_status,
        methods=["GET"],
        response_model=StatusResponse,
        operation_id="getStatus",
    )
    app.add_api_route(
        "/api/save-slots",
        get_save_slots,
        methods=["GET"],
        response_model=SaveSlotsResponse,
        operation_id="getSaveSlots",
    )
    register_operation_routes(app)
    return app


app = create_app()
