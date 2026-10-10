from src.clients.http import get
from src.config.api import CURRENCY_API_URL, TARGET_CURRENCY


def get_rates(currency: str) -> float:
    url = f"{CURRENCY_API_URL}/{currency}/{TARGET_CURRENCY}"
    response = get(url)
    return response.get("rate", 0.0)
