import json
import pytest
from aiohttp import web

from app import create_app


@pytest.fixture
def client(loop, aiohttp_client):
    app = create_app()
    return loop.run_until_complete(aiohttp_client(app))


async def test_400_missing_name(client):
    resp = await client.post("/connect", json={"token": "test"})
    assert resp.status == 400


async def test_400_missing_token(client):
    resp = await client.post("/connect", json={"name": "test"})
    assert resp.status == 400


async def test_connect_player_1(client):
    resp = await client.post("/connect", json={"name": "test", "token": "test"})
    assert resp.status == 200
    assert json.loads(await resp.read()) == {
        "name": "test",
        "token": "test",
        "score": 0,
        "position": [0, 0],
    }


async def test_connect_player_2(client):
    resp = await client.post("/connect", json={"name": "test2", "token": "test2"})
    assert resp.status == 200
    assert json.loads(await resp.read()) == {
        "name": "test2",
        "token": "test2",
        "score": 0,
        "position": [0, 0],
    }


async def test_400_on_repeat_name(client):
    resp = await client.post("/connect", json={"name": "test", "token": "test"})
    assert resp.status == 200
    resp = await client.post("/connect", json={"name": "test", "token": "test"})
    assert resp.status == 400
