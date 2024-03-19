from fastapi import APIRouter, HTTPException, Query
from datetime import datetime
from app.utils.data.sensors import sensors
from app.utils.data.rooms import rooms, rooms_by_collection, rooms_components
from app.utils.functions.fn_generate_sensor_data import fn_generate_sensor_data
from app.utils.functions.fn_generate_actuator_data import fn_generate_actuator_data 
from app.utils.functions.fn_get_collection_by_location import fn_get_collection_by_location
from app.utils.functions.fn_get_sensor_name import fn_get_sensor_name;
from app.models.rooms_model import RoomSchema
from ..config.database import (
    bathrooms_collection,
    bedrooms_collection,
    kitchens_collection,
    garages_collection,
    livingrooms_collection,
    collections,
)

generate_sensor_data_router = APIRouter(
    prefix="/data/sensor", tags=["sensors", "fake data", "generate", "random"]
)
generate_actuator_data_router = APIRouter(
    prefix="/data/actuator", tags=["actuators", "fake data", "generate", "random"]
)


@generate_sensor_data_router.get("/")
async def generate_sensor_data(
    sensorName: str = Query("Temperatura", description="Sensor type to generate data."),
    location: str = Query("Recámara 1", description="Location of sensor."),
    generateNum: int = Query(1, description="Number of documents to generate."),
):
    try:
        if sensorName not in sensors:
            raise HTTPException(
                status_code=404,
                detail=f"{sensorName} is not a valid Sensor to generate Data",
            )

        selected_collection = fn_get_collection_by_location(location);
       

        if selected_collection is None:
            raise HTTPException(
                status_code=404,
                detail=f"Location '{location}' is not found in any collection.",
            )

        sensor_data_list = fn_generate_sensor_data(
            location=location, sensor_name=sensorName, num_datas=generateNum
        )

        bedroom_schemas = [
            RoomSchema(**data, registeredDate=datetime.now().isoformat())
            for data in sensor_data_list
        ]

        # Insertar las instancias de RoomSchema en la base de datos
        result = await collections[selected_collection].insert_many(
            [room.model_dump() for room in bedroom_schemas]
        )
        inserted_count = len(result.inserted_ids)

        return {
            "msg": f"{inserted_count} documents of '{sensorName}' successfully inserted into collection '{selected_collection}' for '{location}'.",
            "inserted_count": inserted_count,
        }
    except HTTPException:
        raise
    except Exception as err:
        raise HTTPException(
            status_code=500, detail=f"Cannot generate data, server error: {err}"
        )

@generate_sensor_data_router.get("/random")
async def generate_random_sensor_data(
    location: str = Query("Recámara 1", description="Location of sensor."),
    generateNum: int = Query(1, description="Number of documents to generate."),
):
    try:
        generated_count = 0
        for _ in range(generateNum):
            sensorName = fn_get_sensor_name(fn_get_collection_by_location(location))
            await generate_sensor_data(sensorName, location, 1)
            generated_count += 1

        return {"msg": f"{generated_count} documents of '{sensorName}' successfully generated."}
    except HTTPException:
        raise
    except Exception as err:
        raise HTTPException(
            status_code=500, detail=f"Cannot generate data, server error: {err}"
        )

@generate_actuator_data_router.get("/")
async def generate_actuator_data(
    actuatorName: str = Query("Puerta", description="Actuator type to generate data."),
    location: str = Query("Recámara 1", description="Location of actuator."),
    generateNum: int = Query(1, description="Number of documents to generate."),
):
    try:
        actuator_data_list = fn_generate_actuator_data(
            location=location, actuator_name=actuatorName, num_datas=generateNum
        )

        room_schemas = [
            RoomSchema(**data, registeredDate=datetime.now().isoformat())
            for data in actuator_data_list
        ]

        selected_collection = fn_get_collection_by_location(location)

        if selected_collection is None:
            raise HTTPException(
                status_code=404,
                detail=f"Location '{location}' is not found in any collection.",
            )

        # Insertar las instancias de RoomSchema en la base de datos
        result = await collections[selected_collection].insert_many(
            [room.model_dump() for room in room_schemas]
        )
        inserted_count = len(result.inserted_ids)

        return {
            "msg": f"{inserted_count} documents of '{actuatorName}' successfully inserted into collection '{selected_collection}' for '{location}'.",
            "inserted_count": inserted_count,
        }
    except HTTPException:
        raise
    except Exception as err:
        raise HTTPException(
            status_code=500, detail=f"Cannot generate data, server error: {err}"
        )

@generate_actuator_data_router.get("/random")
async def generate_random_actuator_data(
    location: str = Query("Recámara 1", description="Location of actuator."),
    generateNum: int = Query(1, description="Number of documents to generate."),
):
    try:
        generated_count = 0
        for _ in range(generateNum):
            await generate_actuator_data("Puerta", location, 1)  # Cambiar el tipo de actuador si se desea
            generated_count += 1

        return {"msg": f"{generated_count} documents of successfully generated."}
    except HTTPException:
        raise
    except Exception as err:
        raise HTTPException(
            status_code=500, detail=f"Cannot generate data, server error: {err}"
        )