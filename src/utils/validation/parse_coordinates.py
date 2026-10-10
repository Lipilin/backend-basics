from src.exceptions import BadRequestError


def parse_coordinates(response: dict) -> tuple[float, float]:
    results = response.get("results", [])
    if not results:
        raise BadRequestError("Не удалось получить координаты")
    latitude = results[0].get("latitude", None)
    longitude = results[0].get("longitude", None)
    if latitude is None or longitude is None:
        raise BadRequestError("Не удалось получить координаты")
    return (latitude, longitude)
