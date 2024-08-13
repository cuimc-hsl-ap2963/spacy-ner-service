from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from .models import RecognitionRequest, RecognitionResponse
from .services import entity_service

app = FastAPI()


@app.post("/ner", response_model=RecognitionResponse)
async def extract_entities(request: RecognitionRequest):
    entities = entity_service.process(request.text)
    return RecognitionResponse(entities=entities)


def openapi_spec():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="spaCy NER API",
        version="1.0.0",
        description="Detects and extracts named entities from text",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = openapi_spec
