from fastapi import Depends, Query
from db import get_coffee_shop_dict
from fastapi import HTTPException
from settings import Settings, create_app, get_settings
import uuid
from uuid import UUID
from models import (
    Order,
    OrderList,
    OrderCreateRequest,
    OrderPatchRequest,
    OrderStatus,
)

app = create_app()


def ensure_order_exists(order_id: UUID, orders: dict[UUID, Order]):
    if order_id not in orders:
        raise HTTPException(
            status_code=404,
            detail=f"Заказ с ID {order_id} не найден",
        )


@app.get("/", tags=["сервис"], summary="Приветствие")
def read_root():
    return {"message": "Добро пожаловать в сервис заказов кофейни!"}


@app.get("/info", status_code=200, tags=["сервис"], summary="Информация о сервисе")
def get_info(
    app_settings: Settings = Depends(get_settings),
    orders=Depends(get_coffee_shop_dict),
):
    return {
        "app_name": app_settings.app_name,
        "description": app_settings.description,
        "version": app_settings.version,
        "contact": {
            "name": app_settings.contact_name,
            "email": app_settings.contact_email,
        },
        "orders_count": len(orders),
    }


@app.post("/orders", response_model=Order, status_code=201, tags=["редактирование"], summary="Создание заказа")
def create_order(
    request: OrderCreateRequest,
    orders=Depends(get_coffee_shop_dict),
):
    order_request_dict = request.model_dump()
    new_order = Order(id=uuid.uuid4(), **order_request_dict)
    orders[new_order.id] = new_order
    return new_order


@app.get("/orders", response_model=OrderList, status_code=200, tags=["получение заказов"], summary="Список заказов")
def get_orders(
    app_settings: Settings = Depends(get_settings),
    orders=Depends(get_coffee_shop_dict),
    offset: int = Query(default=0, ge=0),
    limit: int | None = Query(default=None, ge=1),
    filter: OrderStatus | None = Query(default=None),
):
    if limit is None:
        limit = app_settings.default_page_size
    if limit > app_settings.max_page_size:
        raise HTTPException(
            status_code=422,
            detail=f"limit не может быть больше {app_settings.max_page_size}",
        )
    result = list(orders.values())
    if filter is not None:
        result = [order for order in result if order.status == filter]
    result = result[offset:offset + limit]
    return OrderList(orders=result, offset=offset, limit=limit)


@app.get("/orders/{order_id}", response_model=Order, status_code=200, tags=["получение заказов"], summary="Заказ по идентификатору")
def get_order_by_id(
    order_id: UUID,
    orders=Depends(get_coffee_shop_dict),
):
    ensure_order_exists(order_id, orders)
    return orders[order_id]


@app.patch("/orders/{order_id}", response_model=Order, status_code=200, tags=["редактирование"], summary="Частичное обновление заказа")
def patch_order(
    order_id: UUID,
    request: OrderPatchRequest,
    orders=Depends(get_coffee_shop_dict),
):
    ensure_order_exists(order_id, orders)
    order = orders[order_id]
    updates = {
        key: value
        for key, value in request.model_dump(exclude_unset=True).items()
    }
    if updates:
        order = order.model_copy(update=updates)
        orders[order_id] = order
    return order


@app.delete("/orders/{order_id}", status_code=204, tags=["редактирование"], summary="Отмена заказа")
def delete_order(
    order_id: UUID,
    orders=Depends(get_coffee_shop_dict),
):
    ensure_order_exists(order_id, orders)
    del orders[order_id]
