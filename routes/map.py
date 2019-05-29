import json
from aiohttp import web

from routes.types import Route


async def map_handler(request: web.Request) -> web.Response:
    parsed_grid = json.dumps(request.app["grid"])
    return web.Response(text=parsed_grid)


route: Route = {"method": "get", "url": "/map", "handler": map_handler}
