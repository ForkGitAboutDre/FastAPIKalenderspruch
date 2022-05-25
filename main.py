from fastapi import FastAPI, Body
from typing import Union, Set, List
from pydantic import BaseModel, HttpUrl
from uuid import UUID
from datetime import datetime, time, timedelta

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

@app.put("/items/{item_id}")
async def read_items(
        item_id: UUID,
        start_datetime: Union[datetime, None] = Body(default=None),
        end_datetime: Union[datetime, None] = Body(default=None),
        repeat_at: Union[time, None] = Body(default=None),
        process_after: Union[timedelta, None] = Body(default=None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }


@app.get("/")
async def root():
    return {"message": "Hello World"}
