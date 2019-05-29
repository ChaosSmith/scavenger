import json
from aiohttp import web

from routes.types import Route


async def player_handler(request: web.Request) -> web.Response:
    name = request.match_info["name"]
    if not name:
        return web.HTTPBadRequest(text="Must provide name of player")

    player = next((p for p in request.app["players"] if name == p["name"]), None)

    if not player:
        return web.HTTPBadRequest(text=f"No player of name {name} in this game!")

    return web.Response(text=json.dumps(player))


route: Route = {"method": "get", "url": "/player/{name}", "handler": player_handler}
