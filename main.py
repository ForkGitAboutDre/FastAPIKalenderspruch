from enum import Enum
from fastapi import FastAPI, Query, Path, Body
from typing import Union
from pydantic import BaseModel

FastAPIKalenderspruch = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None





app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        item: Item,
        user: User,
        importance: int = Body(embed=False),
        q: Union[str, None] = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/{item_id}")
async def read_items(
        *,
        item_id: int = Path(title="The ID of the item to get", gt=0, le=1000),
        q: str,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results

@app.get("/items/")
async def read_items(
        q: str
           | None = Query(
            default=None,
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            regex="^fixedquery$",
            deprecated=True,
            include_in_schema=False
        )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


#@app.put("/items/{item_id}")
#async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
#    result = {"item_id": item_id, **item.dict()}
#    if q:
#        result.update({"q": q})
#    return result

@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict



class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


#@app.get("/items/{item_id}")
#async def read_user_item(
#        item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
#):
#    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


#@app.get("/items/{item_id}")
#async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
#    item = {"item_id": item_id}
#    if q:
#        item.update({"q": q})
#    if not short:
#        item.update(
#            {"description": "This is an amazing item that has a long description"}
#        )
#    return item


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#@app.get("/items/")
#async def read_item(skip: int = 0, limit: int = 5):
#    return fake_items_db[skip : skip + limit]

@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/")
async def root():
    return {"message": "Hello World"}

#@app.get("/items/{item_id}")
#async def read_item(item_id: int):
#    return {"item_id": item_id}