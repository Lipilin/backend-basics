import requests
from src.config.network import DEFAULT_TIMEOUT, DEFAULT_RETRIES
from src.exceptions import NetworkError, ServerError, BadRequestError
from requests.exceptions import HTTPError, ConnectionError, Timeout, JSONDecodeError
from time import sleep


def get(url: str, params: dict | None = None) -> dict:
    for _ in range(DEFAULT_RETRIES):
        try:
            response = requests.get(url, params=params)
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
            sleep(e.response.headers.get("Retry-After", DEFAULT_TIMEOUT))
        except JSONDecodeError as e:
            raise ValueError(f"Сервер вернул ответ не в JSON")
