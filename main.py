from enum import Enum
from fastapi import FastAPI, Query, Path, Body
from typing import Union, Set, List, Dict
from pydantic import BaseModel, HttpUrl

FastAPIKalenderspruch = FastAPI()

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None

class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    image: Union[Image, None] = None


class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    items: List[Item]


app = FastAPI()

@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        item: Item = Body(
            examples={
                "normal": {
                    "summary": "A normal example",
                    "description": "A **normal** item works correctly.",
                    "value": {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    },
                },
                "converted": {
                    "summary": "An example with converted data",
                    "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                    "value": {
                        "name": "Bar",
                        "price": "35.4",
                    },
                },
                "invalid": {
                    "summary": "Invalid data is rejected with an error",
                    "value": {
                        "name": "Baz",
                        "price": "thirty five point four",
                    },
                },
            },
        ),
):
    results = {"item_id": item_id, "item": item}
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