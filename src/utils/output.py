import json


def print_summary(summary: dict, is_json: bool = False):
    if is_json:
        print(json.dumps(summary, indent=4))
        with open("summary.json", "w") as f:
            json.dump(summary, f, indent=4)
        return
    weather = summary.get("weather", {})
    rates = summary.get("rates", {})
    print(f"Город: {summary.get('city', '')}")
    print(f"Погода: {weather.get('temperature', 0)}{weather.get('unit', '°C')}")
    print(f"Тёплая одежда: {'Да' if weather.get('warm_clothes', False) else 'Нет'}")
    print(
        f"{rates.get('currency', '')}->{rates.get('target', '')}: {rates.get('rate', 0)}"
    )
    print(f"Дорогой курс: {'Да' if rates.get('expensive', False) else 'Нет'}")
