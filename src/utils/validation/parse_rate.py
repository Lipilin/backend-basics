from src.exceptions import BadRequestError


def parse_rate(response: dict) -> float:
    rate = response.get("rate", None)
    if rate is None:
        raise BadRequestError("Не удалось получить курс валют")
    return rate
