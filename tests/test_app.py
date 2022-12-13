import random

from fastapi.testclient import TestClient
from rp_fastapi.app import app

client = TestClient(app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_get_item_id_works():
    item_id = random.randint(1,10)
    print(item_id)
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id}

def test_get_item_id_fails():
    item_id = 'abc'
    print(item_id)
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 422
    # assert response.json() == {"item_id": item_id}
