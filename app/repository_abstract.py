from abc import ABC, abstractmethod
from typing import Any
from uuid import UUID

from schemas import Order


class OrderRepositoryAbstract(ABC):
    @abstractmethod
    def get_all(self) -> dict[UUID, Order]:
        pass

    @abstractmethod
    def get_by_id(self, id: UUID) -> Order | None:
        pass

    @abstractmethod
    def add(self, new_values: dict[str, Any]) -> Order:
        pass

    @abstractmethod
    def update(self, id: UUID, new_values: dict[str, Any]) -> Order | None:
        pass

    @abstractmethod
    def delete(self, id: UUID) -> None:
        pass
