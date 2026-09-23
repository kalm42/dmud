def require_sqlite(version: tuple[int, int, int]) -> None:
    """Reject unsupported SQLite before data access; for example, require_sqlite(sqlite3.sqlite_version_info)."""
    if version < (3, 37, 0):
        raise RuntimeError("SQLite 3.37.0 or newer is required")
