import spacy
from typing import List


class EntityService:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_trf")

    def process(self, text: str) -> List[str]:
        doc = self.nlp(text)
        return [ent.text for ent in doc.ents if ent.label_ == "ORG"]


entity_service = EntityService()
