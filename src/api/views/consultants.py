from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate
from src.api.cache import cache
from src.api.controllers.consultants import ConsultantsController
from src.api.schemas.consultants import Consultants, QueryParams

routers = APIRouter(
    prefix="/api/v1/consultants",
    tags=["Consultores"],
)


@routers.get("", description="Endpoint para listar consultores")
async def get_consultants(params: QueryParams = Depends()) -> Page[Consultants]:
    controller = ConsultantsController(cache["consultants"], params.region, params.type)
    response = controller.handle()
    return paginate(response)
