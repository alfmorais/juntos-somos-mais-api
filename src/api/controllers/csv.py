import csv
from io import StringIO
from typing import Dict, List

from src.api.exceptions.http import HttpException
from src.api.integrations.client import CsvClient
from src.api.schemas.base import ConsultantsPreLoad
from src.api.schemas.bounding_box import BoundingBox


class ConsultantsCsvController:
    def __init__(self, client: CsvClient, schema: ConsultantsPreLoad) -> None:
        self.client = client
        self.schema = schema

    async def _format_response(self, response: List[Dict]) -> List[Dict]:
        bounding_box = BoundingBox()
        formated_response = [
            {
                "type": bounding_box.classify_consultants(
                    float(data["location__coordinates__latitude"]),
                    float(data["location__coordinates__longitude"]),
                ),
                "gender": data["gender"],
                "name": {
                    "title": data["name__title"],
                    "first": data["name__first"],
                    "last": data["name__last"],
                },
                "location": {
                    "street": data["location__street"],
                    "city": data["location__city"],
                    "state": data["location__state"],
                    "postcode": data["location__postcode"],
                    "coordinates": {
                        "latitude": data["location__coordinates__latitude"],
                        "longitude": data["location__coordinates__longitude"],
                    },
                    "timezone": {
                        "offset": data["location__timezone__offset"],
                        "description": data["location__timezone__description"],
                    },
                },
                "email": data["email"],
                "dob": {
                    "date": data["dob__date"],
                    "age": data["dob__age"],
                },
                "registered": {
                    "date": data["registered__date"],
                    "age": data["registered__age"],
                },
                "phone": data["phone"],
                "cell": data["cell"],
                "picture": {
                    "large": data["picture__large"],
                    "medium": data["picture__medium"],
                    "thumbnail": data["picture__thumbnail"],
                },
            }
            for data in response
        ]

        return [
            ConsultantsPreLoad(**data).model_dump(warnings=False)
            for data in formated_response
        ]

    async def request(self) -> List[Dict]:
        api_response, status_code = await self.client.request()

        if status_code == 200:
            content = StringIO(api_response)
            headers = next(csv.reader(content, delimiter=","))

            response = [
                {column: value for column, value in zip(headers, row)}
                for row in csv.reader(content, delimiter=",")
            ]

            return await self._format_response(response)
        raise HttpException("Error when collect data from api.")
