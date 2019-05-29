import json
from aiohttp import web

from routes.types import Route


async def treasure_handler(request: web.Request) -> web.Response:
    return web.Response(text=json.dumps(request.app["treasure"]))


route: Route = {"method": "get", "url": "/treasure", "handler": treasure_handler}
