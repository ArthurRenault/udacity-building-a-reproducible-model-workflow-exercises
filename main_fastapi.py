from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    item_id: int
    item_name: str = 'na'
    count: int = 1


@app.get('/')
def hello_world():
    return {'hello': 'world'}


@app.get('/items/{item_id}')
def get_item(item_id: int, item_name: str = 'na', count: int = 1) -> dict:
    return {"item_id": item_id, "item_name": item_name, "count": count, "foo": "bar"}


@app.post('/items/')
def set_item(item: Item):
    if item.item_id <= 0:
        raise HTTPException(status_code=422, detail="item_id must be strictly greater than 0.")
    if len(item.item_name) > 100:
        raise HTTPException(status_code=422, detail="item_name must have less than 100 chars.")
    return {"item_id": item.item_id, "item_name": item.item_name}
