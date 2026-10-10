import argparse

from src.config.api import DEFAULT_CURRENCY


def parse_args() -> dict:
    parser = argparse.ArgumentParser()
    parser.add_argument("--city", required=True)
    parser.add_argument("--currency", default=DEFAULT_CURRENCY)
    return parser.parse_args()
