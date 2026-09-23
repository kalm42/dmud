import sqlite3

from fastapi import FastAPI

from dmud.get_status import get_status
from dmud.platform.require_sqlite import require_sqlite
from dmud.platform.settings import Settings
from dmud.status import StatusResponse


def create_app(sqlite_version: tuple[int, int, int] | None = None) -> FastAPI:
    """Construct the local API after validation; for example, create_app()."""
    version = (
        sqlite_version if sqlite_version is not None else sqlite3.sqlite_version_info
    )
    require_sqlite(version)
    Settings()
    app = FastAPI(title="dmud API", version="0.1.0", openapi_version="3.1.0")

    app.add_api_route(
        "/api/status",
        get_status,
        methods=["GET"],
        response_model=StatusResponse,
        operation_id="getStatus",
    )
    return app


app = create_app()
