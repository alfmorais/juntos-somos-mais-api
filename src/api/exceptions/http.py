class HttpException(Exception):
    def __init__(self, message: str) -> None:
        self.mensage = message

    def __str__(self) -> str:
        return f"Error: {self.mensage}"
