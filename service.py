from typing import Any
from uuid import UUID

from exceptions import OrderAlreadyCompletedError, OrderNotFoundError
from repository_abstract import OrderRepositoryAbstract
from schemas import Order, OrderList, OrderStatus
from settings import Settings


class OrderService:
    def __init__(self, repository: OrderRepositoryAbstract) -> None:
        self._repository = repository

    def create_order(self, new_values: dict[Any, Any]) -> Order:
        return self._repository.add(new_values)

    def list_orders(
        self,
        settings: Settings,
        offset: int,
        limit: int | None,
        status_filter: OrderStatus | None,
    ) -> OrderList:
        if limit is None:
            limit = settings.default_page_size
        if limit > settings.max_page_size:
            # TODO: добавить доменную ошибку при превышении settings.max_page_size (422)
            pass

        result = list(self._repository.get_all().values())
        if status_filter is not None:
            result = [order for order in result if order.status == status_filter]
        result = result[offset : offset + limit]
        return OrderList(orders=result, offset=offset, limit=limit)

    def get_order(self, order_id: UUID) -> Order:
        order = self._repository.get_by_id(order_id)
        if order is None:
            raise OrderNotFoundError(order_id)
        return order

    def patch_order(self, order_id: UUID, updates: dict[Any, Any]) -> Order:
        order = self._repository.get_by_id(order_id)
        if order is None:
            raise OrderNotFoundError(order_id)
        if order.status == OrderStatus.COMPLETED:
            raise OrderAlreadyCompletedError(order_id)

        updated = self._repository.update(order_id, updates)
        return updated

    def delete_order(self, order_id: UUID) -> None:
        order = self._repository.get_by_id(order_id)
        if order is None:
            raise OrderNotFoundError(order_id)
        if order.status == OrderStatus.COMPLETED:
            raise OrderAlreadyCompletedError(order_id)
        self._repository.delete(order_id)
