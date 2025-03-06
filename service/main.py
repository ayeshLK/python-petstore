from fastapi import FastAPI
from api import pets

app = FastAPI()

app.include_router(pets.router)


@app.get("/")
async def root():
    return "Hello, World..!"
