from typing import List


class Region:
    def get(self, state: str) -> str:
        match state:
            case state if state in self.north:
                return "norte"
            case state if state in self.north_east:
                return "nordeste"
            case state if state in self.midwest:
                return "centro-oeste"
            case state if state in self.southeast:
                return "sudeste"
            case state if state in self.south:
                return "sul"
            case _:
                return "not_found"

    @property
    def north(self) -> List:
        return [
            "acre",
            "amapa",
            "amazonas",
            "para",
            "rondonia",
            "roraima",
            "tocantins",
        ]

    @property
    def north_east(self) -> List:
        return [
            "alagoas",
            "bahia",
            "ceara",
            "maranhao",
            "pernambuco",
            "paraiba",
            "piaui",
            "rio_grande_do_norte",
            "sergipe",
        ]

    @property
    def midwest(self) -> List:
        return [
            "distrito_federal",
            "goias",
            "mato_grosso",
            "mato_grosso_do_sul",
        ]

    @property
    def southeast(self) -> List:
        return [
            "minas_gerais",
            "espirito_santo",
            "rio_de_janeiro",
            "sao_paulo",
        ]

    @property
    def south(self) -> List:
        return [
            "rio_grande_do_sul",
            "parana",
            "santa_catarina",
        ]
