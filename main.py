from fastapi import FastAPI, Cookie, Header
from typing import Union, List

FastAPIKalenderspruch = FastAPI()



app = FastAPI()



@app.get("/items/")
async def read_items(x_token: Union[List[str], None] = Header(default=None)):
    return {"X-Token values": x_token}

@app.get("/")
async def root():
    return {"message": "Hello World"}
