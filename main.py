from fastapi import FastAPI, status, Form

FastAPIKalenderspruch = FastAPI()



app = FastAPI()


@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}