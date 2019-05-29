import json
from aiohttp import web

from routes.types import Route


async def players_handler(request: web.Request) -> web.Response:
    return web.Response(text=json.dumps(request.app["players"]))


route: Route = {"method": "get", "url": "/players", "handler": players_handler}
