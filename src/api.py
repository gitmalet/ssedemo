from typing import Dict
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.crypto_util import *

app = FastAPI()


KEY: bytes = initialize_key(Path('./key.bin'))

class Item(BaseModel):
    id: int
    data: str

items: Dict[int, bytes] = {}


@app.get("/data")
def list():
    """
    List the ID of all stored items.
    Returns a list of all IDs.
    """
    return [k for k in items.keys()]

@app.get("/data/{item_id}", response_model=Item)
def retrieve(item_id: int):
    """
    Retrieve an item from the store by ID.
    Returns the requested item.
    """
    if item_id in items:
        return Item(id = item_id, data = decrypt(KEY, items[item_id]))
    else:
        raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")

@app.post("/data", response_model=Item)
def create(item: Item):
    """
    Create an item with the given ID containing passed data.
    If an item with the same ID already exists, create it with a fresh id.
    Returns the ID under the item was created under
    """
    # If the item_id already exists use the next highest id instead
    if item.id in items.keys():
        item.id = max(items.keys()) + 1

    if item.data:
        items[item.id] = encrypt(KEY, item.data)
    else:
        raise HTTPException(status_code=400, detail=f"Invalid or missing data")
    return item