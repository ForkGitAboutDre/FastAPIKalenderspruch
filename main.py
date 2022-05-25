from fastapi import FastAPI, status

FastAPIKalenderspruch = FastAPI()



app = FastAPI()

@app.post("/items/", status_code=status.HTTP_402_PAYMENT_REQUIRED)
async def create_item(name: str):
    return {"name": name}