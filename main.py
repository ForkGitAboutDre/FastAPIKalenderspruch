from fastapi import FastAPI

app = FastAPI(openapi_url="/api/v1/openapi.json", docs_url=None, redoc_url=None)


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]
