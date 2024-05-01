from typing import List

from src.api.schemas.consultants import Consultants


class ConsultantsController:
    def __init__(self, consultants: List, region: str, type: str) -> None:
        self.consultants = consultants
        self.region = region
        self.type = type

    def __filter_by_region(self, region: str) -> List[Consultants]:
        return list(
            filter(
                lambda consultant: consultant["location"]["region"] == region,
                self.consultants,
            )
        )

    def __filter_by_type(
        self, type: str, consultants: dict
    ) -> List[Consultants]:  # noqa E501
        return list(
            filter(
                lambda consultant: consultant["type"] == type,
                consultants,
            )
        )

    def handle(self) -> List[Consultants]:
        consultants_filtered_by_region = self.__filter_by_region(
            self.region,
        )
        data_filter_by_type = self.__filter_by_type(
            self.type,
            consultants_filtered_by_region,
        )
        return data_filter_by_type
