from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum
from uuid import UUID

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class BaseOrder(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        examples=["Cappuccino", "Latte"],
    )
    volume: float = Field(..., ge=0.1, examples=[0.35, 0.5])
    quantity: int = Field(..., ge=1, examples=[1, 2])
    client: str = Field(
        min_length=3,
        max_length=100,
        examples=["Egor Lipilin"],
    )

class Order(BaseOrder):
    id: UUID = Field(
        ...,
        examples=["550e8400-e29b-41d4-a716-446655440000"],
    )
    status: OrderStatus = Field(
        default=OrderStatus.PENDING,
        examples=[OrderStatus.PENDING, OrderStatus.IN_PROGRESS],
    )
    created_at: datetime = Field(
        default_factory=datetime.now,
        examples=["2026-10-28T12:00:00"],
    )

class OrderCreateRequest(BaseOrder):
    pass

class OrderList(BaseModel):
    orders: list[Order] = Field(
        default_factory=list,
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

class OrderPatchRequest(BaseModel):
    pass
