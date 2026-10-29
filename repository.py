import uuid
from typing import Any
from uuid import UUID

from repository_abstract import OrderRepositoryAbstract
from schemas import Order


class OrderRepository(OrderRepositoryAbstract):
    def __init__(self) -> None:
        self.__orders: dict[UUID, Order] = {}

    def get_all(self) -> dict[UUID, Order]:
        return self.__orders

    def get_by_id(self, id: UUID) -> Order | None:
        return self.__orders.get(id)

    def add(self, new_values: dict[str, Any]) -> Order:
        new_order = Order(id=uuid.uuid4(), **new_values)
        self.__orders[new_order.id] = new_order
        return new_order

    def update(self, id: UUID, new_values: dict[str, Any]) -> Order | None:
        if id not in self.__orders:
            return None
        self.__orders[id] = self.__orders[id].model_copy(update=new_values)
        return self.__orders[id]

    def delete(self, id: UUID) -> None:
        if id not in self.__orders:
            return
        del self.__orders[id]
