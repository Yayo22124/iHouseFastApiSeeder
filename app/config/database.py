from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
import os

load_dotenv()
print(os.getenv("MONGODB_LOCAL"))

# Establecer la conexión con la base de datos
client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
database = client.get_database("bd_ihouse")


bedrooms_collection = database.get_collection("bedrooms")
livingrooms_collection = database.get_collection("livingrooms")
bathrooms_collection = database.get_collection("bathrooms")
garages_collection = database.get_collection("garages")
kitchens_collection = database.get_collection("kitchens")

collections = {
    "bedrooms": bedrooms_collection,
    "livingrooms": livingrooms_collection,
    "bathrooms": bathrooms_collection,
    "garages": garages_collection,
    "kitchens": kitchens_collection,
}

print("Conexión a la base de datos establecida correctamente")

