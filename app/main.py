from typing import List
from fastapi import FastAPI;

from app.models.bedrooms_model import BedroomSchema;
from app.config.database import database, bedrooms_collection;

app = FastAPI();

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

@app.get("/bedrooms/", response_model=List[BedroomSchema])
async def get_bedrooms() -> dict:
    bedrooms = await bedrooms_collection.find({});
    if bedrooms:
        return bedrooms

    return {"msg": "Error"}