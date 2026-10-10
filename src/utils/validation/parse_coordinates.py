def parse_coordinates(response: dict) -> tuple[float, float]:
    results = response.get("results", [])
    if not results:
        raise ValueError("Сервис координат вернул неожиданный ответ")
    latitude = results[0].get("latitude", None)
    longitude = results[0].get("longitude", None)
    if latitude is None or longitude is None:
        raise ValueError("Сервис координат не предоставил координаты")
    return (latitude, longitude)
