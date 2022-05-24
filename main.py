from enum import Enum
from fastapi import FastAPI

FastAPIKalenderspruch = FastAPI()

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@FastAPIKalenderspruch.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

@FastAPIKalenderspruch.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@FastAPIKalenderspruch.get("/")
async def root():
    return {"message": "Hello World"}

@FastAPIKalenderspruch.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}