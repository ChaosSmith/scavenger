from mypy_extensions import TypedDict
from typing import Callable, Coroutine, Any

from aiohttp import web


Route = TypedDict(
    "Route",
    {
        "method": str,
        "url": str,
        "handler": Callable[[web.Request], Coroutine[Any, Any, web.Response]],
    },
)
