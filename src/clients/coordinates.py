from src.clients.http import get
from src.config.api import COORDINATES_API_URL
from src.utils.validation.parse_coordinates import parse_coordinates


def get_coordinates(city: str) -> tuple[float, float]:
    response = get(COORDINATES_API_URL, params={"name": city, "count": 1})
    return parse_coordinates(response)
