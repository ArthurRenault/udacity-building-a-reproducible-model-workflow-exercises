import json
from fastapi.testclient import TestClient
from main_fastapi import app


client = TestClient(app)


def test_api_locally_get_root():
    r = client.get("/")
    assert r.status_code == 200


def test_malformed_url():
    r = client.get('http://127.0.0.1:8000/mites/1')
    assert r.status_code == 404


def test_get():
    r = client.get('http://127.0.0.1:8000/items/1')
    print(r.json())
    assert r.status_code == 200
    assert r.json()["item_id"] == 1


def test_post():
    r = client.post('http://127.0.0.1:8000/items/1?item_name=foo')
    assert r.status_code == 200
    assert r.json()["item_id"] == 1
    assert r.json()["item_name"] == 'foo'


def test_post_data_dump():
    r = client.post("http://127.0.0.1:8000/items/1", json={"item_id": 1234})
    print(r.json())
    assert r.status_code == 200
    assert r.json()["item_id"] == 1234
    assert r.json()["item_name"] == 'na'
