from fastapi import FastAPI

from models import Laptop, Keyboard, Mouse

app = FastAPI()

@app.get("/laptop")
async def get_laptop() -> list[Laptop]:
    return Laptop.values()

@app.post("/laptop")
async def add_laptop() -> None: