from repository import OrderRepository
from service import OrderService

_repository = OrderRepository()
_order_service = OrderService(_repository)


def get_order_service() -> OrderService:
    return _order_service


def get_order_repository() -> OrderRepository:
    return _repository
