from time import sleep

import requests
from requests.exceptions import ConnectionError, HTTPError, JSONDecodeError, Timeout

from src.config.network import DEFAULT_RETRIES, DEFAULT_TIMEOUT, DEFAULT_RETRY_AFTER
from src.exceptions import BadRequestError, NetworkError, ServerError


def get(url: str, params: dict | None = None) -> dict:
    for _ in range(DEFAULT_RETRIES):
        try:
            response = requests.get(url, params=params, timeout=DEFAULT_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except (Timeout, ConnectionError) as e:
            if _ == DEFAULT_RETRIES - 1:
                raise NetworkError(f"Сервер не отвечает или не доступен: {e}")
        except HTTPError as e:
            if _ == DEFAULT_RETRIES - 1:
                raise ServerError(f"Сервер не может корректно обработать запрос: {e}")
            if e.response.status_code != 429 and e.response.status_code < 500:
                raise BadRequestError(f"Ошибка формирования запроса: {e}")
            sleep(int(e.response.headers.get("Retry-After", DEFAULT_RETRY_AFTER)))
        except JSONDecodeError:
            raise ValueError("Сервер вернул ответ не в JSON")
