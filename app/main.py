from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

"test"

app = FastAPI(title="FastAPI Demo",
              description="A demo FastAPI app for deployment",
              version="1.0.0")

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

items_db = []

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Demo"}

@app.get("/items/", response_model=List[Item])
def read_items():
    return items_db

@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items_db.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    if item_id >= len(items_db):
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]