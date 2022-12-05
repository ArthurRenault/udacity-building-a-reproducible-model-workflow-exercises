from fastapi import FastAPI
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
    return {"item_id": item.item_id, "item_name": item.item_name}
