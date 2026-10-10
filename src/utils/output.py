def print_summary(summary: dict):
    weather = summary.get('weather', {})
    rates = summary.get('rates', {})
    print(f"Город: {summary.get('city', '')}")
    print(f"Температура: {weather.get('temperature', 0)}{weather.get('unit', '°C')}")
    print(f"Тёплая одежда: {weather.get('warm_clothes', '')}")
    print(f"{rates.get('currency', '')}->{rates.get('target', '')}: {rates.get('rate', 0)}")
    print(f"Дорогой курас: {rates.get('expensive', False)}")
