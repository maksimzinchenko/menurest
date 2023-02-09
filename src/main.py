from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class MenuItem(BaseModel):
    id: str = uuid.uuid4()
    name: str = 'Meal name'
    description: str = ''
    image: str = 'none.jpg'
    price: float = 0.0
    is_active: Union[bool, None] = None
    order: int = 0


menu_items: List[MenuItem] = [
    {'id': '59a46597-e48d-4dc1-b014-fd3908649c6d', 'name': 'Meal 1', 'price': 2.5, 'is_active': True, 'order': 1},
    {'id': 'e81d9cdb-71e3-440d-9bfb-d9b97d89f957', 'name': 'Meal 2', 'price': 3, 'is_active': True, 'order': 1},
    {'id': 'ed1c6231-ccb3-4527-b8a2-0bf6851676d7', 'name': 'Meal 3', 'price': 26, 'is_active': True, 'order': 1},
    {'id': 'a2ac5f5b-3463-4c42-b0fc-020ecc3be819', 'name': 'Meal 4', 'price': 21, 'is_active': True, 'order': 1},
    {'id': '5abc49cd-f1e3-470e-8d0f-670b09d16cac', 'name': 'Meal 5', 'price': 5, 'is_active': True, 'order': 1},
    {'id': '4472f08c-9c9a-4902-83aa-1247188c7eb8', 'name': 'Meal 6', 'price': 15, 'is_active': True, 'order': 1},
    {'id': 'dc74415a-38b0-418e-bd0d-af95a4c02004', 'name': 'Meal 7', 'price': 0.5, 'is_active': True, 'order': 1},
]


@app.get("/")
async def read_root():
    return {"Hello": "World"}



@app.get("/menu_items/")
async def read_items(skip: int = 0, limit: int = 3):
    return menu_items[skip: limit]


@app.get("/menu_items/{id}")
async def read_item(id: str):
    returned_item: MenuItem = list(filter(lambda item: (id == item['id']), menu_items))
    return returned_item

@app.post("/menu_items/")
async def post_item(item: MenuItem):
    menu_items.append(item)
    return item


@app.delete("/menu_items/{id}")
async def delete_item(id: str):
    global menu_items
    menu_items = list(filter(lambda item: (id != item['id']), menu_items))
    return {'result': 'Deletion query proccessed'}



@app.put("/menu_items/{id}")
async def update_item(id: str, menu_item: MenuItem):
    for item in menu_items:
        if item['id'] == id:
            item[id] = menu_item
            return {"item_updated": menu_item, "result": 'success'}
    return {'result': 'Item not found'}