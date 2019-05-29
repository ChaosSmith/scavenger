import json
from aiohttp import web

from routes.types import Route


async def connect_handler(request: web.Request) -> web.Response:
    data = await request.json()
    request_keys = data.keys()
    if "name" not in request_keys:
        return web.HTTPBadRequest(text="Need to provide a name!")
    if "token" not in request_keys:
        return web.HTTPBadRequest(text="Need to provide a token!")
    if data["name"] in [player["name"] for player in request.app["players"]]:
        return web.HTTPBadRequest(text="Player of this name is already registered")

    player = {
        "name": data["name"],
        "token": data["token"],
        "score": 0,
        "position": (0, 0),
    }

    request.app["players"].append(player)
    return web.Response(text=json.dumps(player))


route: Route = {"method": "post", "url": "/connect", "handler": connect_handler}
