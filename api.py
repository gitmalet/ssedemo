from typing import Dict
from pathlib import Path

from fastapi import FastAPI

from crypto_util import *

app = FastAPI()


KEY: bytes = initialize_key(Path('./key.bin'))
items: Dict[int, bytes] = {}

@app.get("/data/")
def list():
    """
    List the ID of all stored items.
    Returns a list of all IDs.
    """
    return items.keys()

@app.get("/data/{item_id}")
def retrieve(item_id: int):
    """
    Retrieve an item from the store by ID.
    Returns the requested item.
    """
    if item_id in items:
        return decrypt(KEY, items[item_id])
    else:
        return {"error": f"Item with ID {item_id} not found"}

@app.post("/data/{item_id}")
def create(item_id: int, data: str):
    """
    Create an item with the given ID containing passed data.
    If an item with the same ID already exists, create it with a fresh id.
    Returns the ID under the item was created under
    """
    # If the item_id already exists use the next highest id instead
    if item_id in items.keys():
        item_id = max(items.keys()) + 1

    if data:
        items[item_id] = encrypt(KEY, data)
    else:
        return {"error": "Invalid data"}
    return item_id