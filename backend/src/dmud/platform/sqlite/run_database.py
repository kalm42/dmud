import asyncio
from collections.abc import Callable


async def run_database[**P, T](
    call: Callable[P, T], *args: P.args, **kwargs: P.kwargs
) -> T:
    """Offload a complete adapter and drain it before cancellation; e.g. await run_database(get_operation, path, id)."""
    task = asyncio.create_task(asyncio.to_thread(call, *args, **kwargs))
    cancelled = False
    while True:
        try:
            result = await asyncio.shield(task)
        except asyncio.CancelledError:
            if task.cancelled():
                raise
            cancelled = True
            continue
        except Exception:
            if cancelled:
                raise asyncio.CancelledError from None
            raise
        if cancelled:
            raise asyncio.CancelledError
        return result
