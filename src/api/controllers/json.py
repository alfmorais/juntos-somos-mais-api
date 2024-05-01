from typing import Dict, List

from src.api.exceptions.http import HttpException
from src.api.integrations.client import JsonClient
from src.api.schemas.base import ConsultantsPreLoad
from src.api.schemas.bounding_box import BoundingBox


class ConsultantsJsonController:
    def __init__(self, client: JsonClient, schema: ConsultantsPreLoad) -> None:
        self.client = client
        self.schema = schema

    async def _include_bounding_box(self, response: List[Dict]) -> List[Dict]:
        bounding_box = BoundingBox()
        formated_response = [
            {
                **data,
                "type": bounding_box.classify_consultants(
                    float(data["location"]["coordinates"]["latitude"]),
                    float(data["location"]["coordinates"]["longitude"]),
                ),
            }
            for data in response
        ]
        return await self._format_response(formated_response)

    async def _format_response(self, response: List[Dict]) -> List[Dict]:
        return [
            ConsultantsPreLoad(**data).model_dump(warnings=False) for data in response
        ]

    async def request(self) -> List[Dict]:
        """
        TODO: Lançar excessao customizada.
        """
        api_response, status_code = await self.client.request()

        if status_code == 200:
            response = [data for data in api_response["results"]]

            return await self._include_bounding_box(response)
        raise HttpException("Error when collect data from api.")
