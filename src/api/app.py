from contextlib import asynccontextmanager
from typing import AsyncIterable

from fastapi import FastAPI
from fastapi_pagination import add_pagination
from src.api.controllers.csv import ConsultantsCsvController
from src.api.controllers.json import ConsultantsJsonController
from src.api.integrations.client import CsvClient, JsonClient
from src.api.schemas.base import ConsultantsPreLoad
from src.api.views import consultants

from .cache import cache

BASE_URL = "https://storage.googleapis.com/juntossomosmais-code-challenge/"
CSV = "input-backend.csv"
JSON = "input-backend.json"


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterable:
    csv_client = CsvClient("{}{}".format(BASE_URL, CSV))
    json_client = JsonClient("{}{}".format(BASE_URL, JSON))

    format_consultants_csv = ConsultantsCsvController(
        csv_client,
        ConsultantsPreLoad,
    )
    format_consultants_json = ConsultantsJsonController(
        json_client,
        ConsultantsPreLoad,
    )

    response_csv = await format_consultants_csv.request()
    response_json = await format_consultants_json.request()

    cache["consultants"] = response_csv + response_json
    yield
    cache.clear()


app = FastAPI(
    title="Juntos Somos Mais API v1.0",
    lifespan=lifespan,
)
app.include_router(consultants.routers)
add_pagination(app)


@app.get("/", tags=["Juntos Somos Mais"], description="Juntos Somos Mais")
def juntos_somos_mais():
    return {"message": "Quero fazer parte do time!!!"}
