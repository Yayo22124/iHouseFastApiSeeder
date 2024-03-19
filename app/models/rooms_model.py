from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime


class RoomSchema(BaseModel):
    arduinoIp: str
    type: str
    name: str
    brand: str
    model: str
    specifications: List[dict]
    location: str
    status: str
    registeredDate: Optional[datetime] = Field(default_factory=datetime.now)
    owner: str
    readings: Optional[List[dict]] = []
    actions: Optional[List[dict]] = []
