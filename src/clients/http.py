from time import sleep

import requests
from requests.exceptions import ConnectionError, HTTPError, JSONDecodeError, Timeout

from src.config.network import DEFAULT_RETRIES, DEFAULT_RETRY_AFTER, DEFAULT_TIMEOUT
from src.exceptions import BadRequestError, NetworkError, ServerError


def retry_after(headers: dict) -> None:
    sleep(int(headers.get("Retry-After", DEFAULT_RETRY_AFTER)))

def raise_error(attempt: int, error: Exception) -> None:
    if attempt == DEFAULT_RETRIES - 1:
        raise error

def get(url: str, params: dict | None = None) -> dict:
    for attempt in range(DEFAULT_RETRIES):
        try:
            response = requests.get(url, params=params, timeout=DEFAULT_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except (Timeout, ConnectionError) as e:
            raise_error(attempt, NetworkError(f"Сервер не отвечает или не доступен: {e}"))
            retry_after({})
        except HTTPError as e:
            if e.response.status_code != 429 and e.response.status_code < 500:
                raise BadRequestError(f"Ошибка формирования запроса: {e}")
            raise_error(attempt, ServerError(f"Сервер не может корректно обработать запрос: {e}"))
            retry_after(e.response.headers)
        except JSONDecodeError:
            raise ValueError("Сервер вернул ответ не в JSON")
