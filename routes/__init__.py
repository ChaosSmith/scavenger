from typing import List

from routes import root, map, connect, player, players, move, treasure

from routes.types import Route

routes: List[Route] = [
    root.route,
    map.route,
    connect.route,
    player.route,
    players.route,
    move.route,
    treasure.route,
]
