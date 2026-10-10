def parse_rate(response: dict) -> float:
    rate = response.get("rate", None)
    if rate is None:
        raise ValueError("Сервис курсов валют вернул неожиданный ответ")
    return rate
