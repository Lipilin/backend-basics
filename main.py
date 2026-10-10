from src import get_city_summary
from src.utils.parse_args import parse_args


def main():
    args = parse_args()
    city = args.city
    currency = args.currency
    summary = get_city_summary(city, currency)
    print(summary)
    return 0


if __name__ == "__main__":
    main()
