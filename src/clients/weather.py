from src.clients.http import get
from src.config.api import WEATHER_API_URL


def get_weather(latitude: float, longitude: float) -> dict:
    response = get(
        WEATHER_API_URL,
        params={
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,weather_code",
        },
    )
    return response
