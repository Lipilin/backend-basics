from src.clients.http import get
from src.config.api import COORDINATES_API_URL


def get_coordinates(city: str) -> tuple[float, float]:
    response = get(COORDINATES_API_URL, params={"name": city, "count": 1})
    results = response.get("results", [])[0]
    return (results["latitude"], results["longitude"])
