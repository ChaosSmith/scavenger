from aiohttp import web

from routes.types import Route


async def root_handler(request: web.Request) -> web.Response:
    return web.Response(text="Project Route")


route: Route = {"method": "get", "url": "/", "handler": root_handler}
