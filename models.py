from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from uuid import UUID


class OrderStatus(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class DrinkVolume(str, Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"
    EXTRA_LARGE = "EXTRA_LARGE"


class BaseOrder(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Название напитка",
        examples=["Cappuccino", "Latte"],
    )
    volume: DrinkVolume = Field(
        ...,
        description="Объём порции в литрах (допустимые значения из списка)",
        examples=[DrinkVolume.MEDIUM, DrinkVolume.LARGE],
    )
    quantity: int = Field(
        ...,
        ge=1,
        description="Количество порций",
        examples=[1, 2],
    )
    client: str | None = Field(
        default=None,
        min_length=3,
        max_length=100,
        description="Имя клиента",
        examples=["Egor Lipilin", "Anna Ivanova"],
    )


class Order(BaseOrder):
    id: UUID = Field(
        ...,
        description="Уникальный идентификатор заказа",
        examples=["550e8400-e29b-41d4-a716-446655440000"],
    )
    status: OrderStatus = Field(
        default=OrderStatus.PENDING,
        description="Текущий статус заказа",
        examples=[OrderStatus.PENDING, OrderStatus.IN_PROGRESS],
    )
    created_at: datetime = Field(
        default_factory=datetime.now,
        description="Дата и время создания заказа",
        examples=["2026-10-28T12:00:00"],
    )


class OrderCreateRequest(BaseOrder):
    pass


class OrderList(BaseModel):
    orders: list[Order] = Field(
        default_factory=list,
        description="Список заказов",
        examples=[
            [
                {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "name": "Cappuccino",
                    "volume": 0.35,
                    "quantity": 2,
                    "client": "Egor Lipilin",
                    "status": "PENDING",
                    "created_at": "2026-10-28T12:00:00",
                }
            ]
        ],
    )
    offset: int = Field(
        ...,
        ge=0,
        description="Смещение выборки",
        examples=[0, 10],
    )
    limit: int = Field(
        ...,
        ge=1,
        description="Размер страницы",
        examples=[10, 20],
    )


class OrderPatchRequest(BaseModel):
    status: OrderStatus | None = Field(
        default=None,
        description="Новый статус заказа",
        examples=[OrderStatus.IN_PROGRESS, OrderStatus.COMPLETED],
    )
    client: str | None = Field(
        default=None,
        min_length=3,
        max_length=100,
        description="Имя клиента",
        examples=["Egor Lipilin", "Anna Ivanova"],
    )
    quantity: int | None = Field(
        default=None,
        ge=1,
        description="Количество порций",
        examples=[1, 2],
    )
    volume: DrinkVolume | None = Field(
        default=None,
        description="Объём порции в литрах (допустимые значения из списка)",
        examples=[DrinkVolume.MEDIUM, DrinkVolume.LARGE],
    )
