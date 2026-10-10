import sys

from src import get_city_summary, parse_args, print_summary
from src.exceptions import BadRequestError, NetworkError, ServerError


def main():
    try:
        args = parse_args()
        city = args.city
        currency = args.currency
        summary = get_city_summary(city, currency)
        print_summary(summary)
    except SystemExit:
        print("Введены некорректные аргументы")
        return 2
    except BadRequestError as e:
        print(e)
        return 3
    except (ServerError, NetworkError, ValueError) as e:
        print(e)
        return 4
    return 0


if __name__ == "__main__":
    sys.exit(main())
