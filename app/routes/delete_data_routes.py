from fastapi import APIRouter, HTTPException, Query
from ..config.database import (
    bathrooms_collection,
    bedrooms_collection,
    livingrooms_collection,
    garages_collection,
    kitchens_collection,
    collections
)

delete_router = APIRouter(prefix="/data", tags=["rooms", "delete data", "random"])


@delete_router.delete("/", description="Delete all data in each collection of database")
async def delete_all():
    try:
        result_bedrooms = await bedrooms_collection.delete_many({})
        result_bathrooms = await bathrooms_collection.delete_many({})
        result_livingrooms = await livingrooms_collection.delete_many({})
        result_garages = await garages_collection.delete_many({})
        result_kitchens = await kitchens_collection.delete_many({})

        return {
            "msg": {
                "bedrooms": f"{result_bedrooms.deleted_count} documents deleted successfully",
                "bathrooms": f"{result_bathrooms.deleted_count} documents deleted successfully",
                "livingrooms": f"{result_livingrooms.deleted_count} documents deleted successfully",
                "garages": f"{result_garages.deleted_count} documents deleted successfully",
                "kitchens": f"{result_kitchens.deleted_count} documents deleted successfully",
            }
        }
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


@delete_router.delete(
    "/{collection}", description="Delete all data in a specific collection and specific location."
)
async def delete_by_collection(collection: str, location: str = Query(None, description="Optional location filter to delete in collection.")):
    try:
        if collection not in collections:
            raise HTTPException(
                status_code=404, detail=f"Collection: {collection}, not found."
            )
        else :
        
            if location is not None :
                result = await collections[collection].delete_many({"location": location}) # Delete in collection (previus validated of exist) and filter by location.
                return {
                    "msg": f"{str(result)} documents deleted successfully from collection '{collection}' and by '{location}'"
                }
            else :
                result = await collections[collection].delete_many({})
                
            return {
                "msg": f"{str(result)} documents deleted successfully from collection '{collection}'"
            }
    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Cannot delete, server error: {err}.")
