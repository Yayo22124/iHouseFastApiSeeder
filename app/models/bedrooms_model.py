from typing import List, Optional
from pydantic import BaseModel, Field


class Reading(BaseModel):
    name: str
    value: float
    measurementUnit: str


class Action(BaseModel):
    name: str
    value: float
    measurementUnit: str


class BedroomSchema(BaseModel):
    type: str
    name: str
    brand: str
    model: str
    specifications: List[dict]
    location: str
    status: str
    registeredDate: Optional[str] = Field(default_factory=str)
    owner: str
    readings: List[Reading]
    actions: List[Action]

    class Config:
        orm_mode = True
