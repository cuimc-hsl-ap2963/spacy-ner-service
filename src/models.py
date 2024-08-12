from pydantic import BaseModel
from typing import List


class Entity(BaseModel):
    text: str
    label: str
    start: int
    end: int


class RecognitionRequest(BaseModel):
    text: str


class RecognitionResponse(BaseModel):
    entities: List[Entity]


class HealthResponse(BaseModel):
    status: str
