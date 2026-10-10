from src.clients import get_coordinates, get_rates, get_weather
from src.config.api import DEFAULT_CURRENCY, TARGET_CURRENCY


def get_city_summary(city: str, currency: str = DEFAULT_CURRENCY) -> dict:
    latitude, longtitude = get_coordinates(city)
    weather = get_weather(latitude, longtitude)
    rate = get_rates(currency)
    temperature = weather["current"]["temperature_2m"]
    weather_code = weather["current"]["weather_code"]
    unit = weather["current_units"]["temperature_2m"]

    return {
        "city": city,
        "location": {
            "latitude": latitude,
            "longitude": longtitude,
        },
        "weather": {
            "temperature": temperature,
            "unit": unit,
            "weather_code": weather_code,
        },
        "rates": {
            "currency": currency,
            "target": TARGET_CURRENCY,
            "rate": rate,
        },
    }
