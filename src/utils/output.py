def print_summary(summary: dict):
    weather = summary.get("weather", {})
    rates = summary.get("rates", {})
    print(f"Город: {summary.get('city', '')}")
    print(f"Погода: {weather.get('temperature', 0)}{weather.get('unit', '°C')}")
    print(f"Тёплая одежда: {'Да' if weather.get('warm_clothes', False) else 'Нет'}")
    print(
        f"{rates.get('currency', '')}->{rates.get('target', '')}: {rates.get('rate', 0)}"
    )
    print(f"Дорогой курс: {'Да' if rates.get('expensive', False) else 'Нет'}")
