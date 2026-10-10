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
    temperature = response.get("current", {}).get("temperature_2m")
    weather_code = response.get("current", {}).get("weather_code")
    unit = response.get("current_units", {}).get("temperature_2m")
    return {
        "temperature": temperature,
        "weather_code": weather_code,
        "unit": unit,
    }
