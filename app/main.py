from typing import List
from fastapi import FastAPI, HTTPException
from bson import ObjectId

from app.routes.generate_data_routes import generate_actuator_data_router, generate_sensor_data_router;
from .routes.delete_data_routes import delete_router;
from app.models.rooms_model import RoomSchema
from app.config.database import bedrooms_collection

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello World"}

@app.get("/bedrooms/")
async def get_bedrooms() -> List[RoomSchema]:
    try:
        bedrooms = await bedrooms_collection.find({}).to_list(None)

        for bedroom in bedrooms:
            bedroom["_id"] = str(bedroom["_id"])
        
        return bedrooms
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/bedroom/")
async def get_bedroom() -> RoomSchema | dict:
    try:
        bedroom = await bedrooms_collection.find_one({})

        if bedroom:
            bedroom["_id"] = str(bedroom["_id"])
            return bedroom
        else:
            raise HTTPException(status_code=404, detail="Bedroom not found")
    except HTTPException:
        raise 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app.include_router(delete_router);
app.include_router(generate_sensor_data_router);
app.include_router(generate_actuator_data_router);