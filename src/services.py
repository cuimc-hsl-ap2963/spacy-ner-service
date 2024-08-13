import spacy
from .models import Entity
from typing import List


class EntityService:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process(self, text: str) -> List[Entity]:
        doc = self.nlp(text)
        return [
            Entity(
                text=ent.text,
                label=ent.label_,
                start=ent.start_char,
                end=ent.end_char
            )
            for ent in doc.ents
        ]


entity_service = EntityService()
