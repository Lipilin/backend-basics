from uuid import UUID


class OrderNotFoundError(Exception):
    def __init__(self, order_id: UUID) -> None:
        self.order_id = order_id
        super().__init__(f"Заказ с ID {order_id} не найден")

class OrderAlreadyCompletedError(Exception):

    def __init__(self, order_id: UUID) -> None:
        self.order_id = order_id
        super().__init__(f"Заказ с ID {order_id} уже завершен")