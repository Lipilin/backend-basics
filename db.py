from models import Order
from uuid import UUID

coffee_shop_dict: dict[UUID, Order] = {}


def get_coffee_shop_dict() -> dict[UUID, Order]:
    return coffee_shop_dict
