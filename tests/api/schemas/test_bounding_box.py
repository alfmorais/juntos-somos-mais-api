import pytest
from src.api.schemas.bounding_box import BoundingBox, BoundingBoxParams


@pytest.mark.parametrize(
    "latitude,longitude,expected_type",
    (
        (-76.3253, 137.9437, "laborious"),
        (20.9211, -0.2337, "laborious"),
        (-62.3232, 30.9146, "laborious"),
        (-14.6795, 178.2852, "laborious"),
        (-22.0270, -14.1291, "special"),
        (8.1519, -17.1622, "special"),
        (-18.8688, -14.2289, "special"),
        (-50.4568, -16.6951, "normal"),
        (7.7580, -18.9066, "special"),
        (-26.7856, -25.8708, "normal"),
        (-5.9019, -29.1696, "normal"),
        (-4.1651, -29.5626, "normal"),
    ),
)
def test_bounding_box_success(latitude, longitude, expected_type):
    bounding_box = BoundingBox()
    response = bounding_box.classify_consultants(
        latitude,
        longitude,
    )

    assert response == expected_type


@pytest.mark.parametrize(
    "minlon,minlat,maxlon,maxlat",
    (
        (
            -2.196998,
            -46.361899,
            -15.411580,
            -34.276938,
        ),
        (
            -19.766959,
            -52.997614,
            -23.966413,
            -44.428305,
        ),
        (
            -26.155681,
            -54.777426,
            -34.016466,
            -46.603598,
        ),
    ),
)
def test_bounding_box_params_success(minlon, minlat, maxlon, maxlat):
    bounding_box_params = BoundingBoxParams(
        minlon=minlon,
        minlat=minlat,
        maxlon=maxlon,
        maxlat=maxlat,
    )

    assert bounding_box_params.minlon == minlon
    assert bounding_box_params.minlat == minlat
    assert bounding_box_params.maxlon == maxlon
    assert bounding_box_params.maxlat == maxlat
