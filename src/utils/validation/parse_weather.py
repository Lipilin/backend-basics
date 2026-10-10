def parse_weather(response: dict) -> dict:
    current = response.get("current", {})
    current_units = response.get("current_units", {})
    temperature = current.get("temperature_2m", None)
    weather_code = current.get("weather_code", None)
    unit = current_units.get("temperature_2m", None)
    if temperature is None or weather_code is None:
        raise ValueError("Сервис погоды вернул неожиданный ответ")
    return {"temperature": temperature, "weather_code": weather_code, "unit": unit}
