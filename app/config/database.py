from dotenv import load_dotenv;
from motor.motor_asyncio import AsyncIOMotorClient;
import os;
load_dotenv();

client = AsyncIOMotorClient(os.getenv("MONGODB_URL"));
database = client.get_database("bd_ihouse");

bedrooms_collection = database.get_collection("bedrooms");