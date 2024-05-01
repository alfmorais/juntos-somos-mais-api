import pytest
from src.api.schemas.region import Region


@pytest.mark.parametrize(
    "state,expected_region",
    [
        ["acre", "norte"],
        ["alagoas", "nordeste"],
        ["amapa", "norte"],
        ["amazonas", "norte"],
        ["bahia", "nordeste"],
        ["ceara", "nordeste"],
        ["distrito_federal", "centro-oeste"],
        ["espirito_santo", "sudeste"],
        ["goias", "centro-oeste"],
        ["maranhao", "nordeste"],
        ["mato_grosso", "centro-oeste"],
        ["mato_grosso_do_sul", "centro-oeste"],
        ["minas_gerais", "sudeste"],
        ["para", "norte"],
        ["paraiba", "nordeste"],
        ["parana", "sul"],
        ["pernambuco", "nordeste"],
        ["piaui", "nordeste"],
        ["rio_de_janeiro", "sudeste"],
        ["rio_grande_do_norte", "nordeste"],
        ["rio_grande_do_sul", "sul"],
        ["rondonia", "norte"],
        ["roraima", "norte"],
        ["santa_catarina", "sul"],
        ["sao_paulo", "sudeste"],
        ["sergipe", "nordeste"],
        ["tocantins", "norte"],
    ],
)
def test_utils_found_region_success(state, expected_region):
    region = Region().get(state)

    assert region == expected_region


def test_utils_not_found_result():
    region = Region().get("Califórnia")

    assert region == "not_found"
