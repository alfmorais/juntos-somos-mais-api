from typing import Dict

from pydantic import BaseModel
from shapely.geometry import Point, Polygon, box

FIRST_SPECIAL = {
    "minlon": -2.196998,
    "minlat": -46.361899,
    "maxlon": -15.411580,
    "maxlat": -34.276938,
}
SECOND_SPECIAL = {
    "minlon": -19.766959,
    "minlat": -52.997614,
    "maxlon": -23.966413,
    "maxlat": -44.428305,
}
NORMAL = {
    "minlon": -26.155681,
    "minlat": -54.777426,
    "maxlon": -34.016466,
    "maxlat": -46.603598,
}


class BoundingBoxParams(BaseModel):
    minlon: float
    minlat: float
    maxlon: float
    maxlat: float


class BoundingBox:
    def __init__(
        self,
        first_special: Dict = FIRST_SPECIAL,
        second_special: Dict = SECOND_SPECIAL,
        normal: Dict = NORMAL,
    ) -> None:
        self.first_special = BoundingBoxParams(**first_special)
        self.second_special = BoundingBoxParams(**second_special)
        self.normal = BoundingBoxParams(**normal)

    def polygon(
        self,
        minlon: float,
        minlat: float,
        maxlon: float,
        maxlat: float,
    ) -> Polygon:
        center_x = (minlon + maxlon) / 2
        center_y = (minlat + maxlat) / 2
        width = maxlon - minlon
        height = maxlat - minlat
        return box(center_x, center_y, width, height)

    def classify_consultants(self, latitude: float, longitude: float) -> str:
        point = Point(longitude, latitude)

        is_special = any(
            [
                self.polygon(
                    self.first_special.minlon,
                    self.first_special.minlat,
                    self.first_special.maxlon,
                    self.first_special.maxlat,
                ).contains(point),
                self.polygon(
                    self.second_special.minlon,
                    self.second_special.minlat,
                    self.second_special.maxlon,
                    self.second_special.maxlat,
                ).contains(point),
            ]
        )
        is_normal = self.polygon(
            self.normal.minlon,
            self.normal.minlat,
            self.normal.maxlon,
            self.normal.maxlat,
        ).contains(point)

        if is_special:
            return "special"
        elif is_normal:
            return "normal"
        else:
            return "laborious"
