from fastapi import FastAPI

app = FastAPI(openapi_url="/api/v1/openapi.json", redoc_url=None)


@app.get("/items/{itemid}")
async def read_items(itemid: int):
    return [{"name": itemid}]
