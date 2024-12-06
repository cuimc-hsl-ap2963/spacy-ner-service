from pydantic import BaseModel
from typing import List


class RecognitionRequest(BaseModel):
    text: str


class RecognitionResponse(BaseModel):
    entities: List[str]
