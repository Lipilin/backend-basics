from src.clients import get_coordinates, get_rates, get_weather
from src.config.api import DEFAULT_CURRENCY, TARGET_CURRENCY
from src.processing.preprocessing import check_is_expensive, check_is_warm_clothes


def get_city_summary(city: str, currency: str = DEFAULT_CURRENCY) -> dict:
    latitude, longtitude = get_coordinates(city)
    weather = get_weather(latitude, longtitude)
    rate = get_rates(currency)
    summary = {
        "city": city,
        "rates": {
            "currency": currency,
            "target": TARGET_CURRENCY,
            "rate": rate,
            "expensive": check_is_expensive(rate),
        },
        "weather": {
            **weather,
            "warm_clothes": check_is_warm_clothes(weather["temperature"]),
        },
    }

    return summary
