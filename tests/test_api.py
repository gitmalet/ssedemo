from fastapi.testclient import TestClient

from src.api import app
from src.api import Item

client = TestClient(app)

def test_empty_list():
    r = client.get("/data")
    assert r.status_code == 200
    assert r.json() == []

def test_create():
    """
    Creating a single object and retrieving it
    """
    item = Item(id=1, data="TestString")

    r = client.post("/data", json=item.dict())
    assert r.status_code == 200
    assert r.json() == item

    r = client.get("/data")
    assert r.status_code == 200
    assert item.id in r.json()

    r = client.get("/data/1")
    assert r.status_code == 200
    assert r.json() == item


def test_create_multiple_id():
    """
    Creating the same object multiple times and retrieving both
    Checks ID collision detection
    """
    item = Item(id=2, data="TestString")

    r = client.post("/data", json=item.dict())
    r = client.post("/data", json=item.dict())

    # Check whether content is the same 
    assert r.status_code == 200
    assert r.json()['data'] == item.data

    # Retrieve fresh ID
    new_id = r.json()['id']
    assert new_id != item.id

    # Check whether two objects were created
    r = client.get("/data")
    assert r.status_code == 200
    assert len(r.json()) >= 2
    
    # Retrieve object under new id
    item.id=new_id
    r = client.get(f"/data/{new_id}")
    assert r.status_code == 200
    assert r.json() == item