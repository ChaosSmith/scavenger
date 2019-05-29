import json
from aiohttp import web

from routes.types import Route


async def move_handler(request: web.Request) -> web.Response:
    data = await request.json()
    request_keys = data.keys()
    if "direction" not in request_keys:
        return web.HTTPBadRequest(text="Need to provide a direction!")
    if "token" not in request_keys:
        return web.HTTPBadRequest(text="Need to provide a token!")

    player = next(
        (p for p in request.app["players"] if p["token"] == data["token"]), None
    )
    if not player:
        return web.HTTPBadRequest(text="Invalid Token!")

    i = request.app["players"].index(player)

    c_pos = request.app["players"][i]["position"]
    if data["direction"] == "right":
        new_position = (c_pos[0] + 1, c_pos[1])
    elif data["direction"] == "left":
        new_position = (c_pos[0] - 1, c_pos[1])
    elif data["direction"] == "down":
        new_position = (c_pos[0], c_pos[1] - 1)
    elif data["direction"] == "up":
        new_position = (c_pos[0], c_pos[1] + 1)
    else:
        return web.HTTPBadRequest(
            text="Invalid Direction! Should be one of left, right, up, down"
        )

    player["position"] = new_position

    treasure = next((t for t in request.app["treasure"] if t == new_position), None)

    if treasure:
        t_i = request.app["treasure"].index(treasure)
        request.app["treasure"].pop(t_i)
        player["score"] = player["score"] + 1

    request.app["players"][i] = player
    return web.Response(text=json.dumps(player))


route: Route = {"method": "post", "url": "/move", "handler": move_handler}
