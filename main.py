from uuid import UUID

from fastapi import Depends, Query
from fastapi.responses import JSONResponse

from db import get_order_repository, get_order_service
from exceptions import OrderAlreadyCompletedError, OrderNotFoundError
from repository import OrderRepository
from schemas import (
    Order,
    OrderCreateRequest,
    OrderList,
    OrderPatchRequest,
    OrderStatus,
)
from service import OrderService
from settings import Settings, create_app, get_settings

app = create_app()


@app.exception_handler(OrderNotFoundError)
def handle_order_not_found(_request, exc: OrderNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"detail": str(exc)},
    )


@app.exception_handler(OrderAlreadyCompletedError)
def handle_order_already_completed(_request, exc: OrderAlreadyCompletedError):
    return JSONResponse(
        status_code=409,
        content={"detail": str(exc)},
    )


@app.get("/", tags=["сервис"], summary="Приветствие")
def read_root():
    return {"message": "Добро пожаловать в сервис заказов кофейни!"}


@app.get("/info", status_code=200, tags=["сервис"], summary="Информация о сервисе")
def get_info(
    app_settings: Settings = Depends(get_settings),
    repository: OrderRepository = Depends(get_order_repository),
):
    return {
        "app_name": app_settings.app_name,
        "description": app_settings.description,
        "version": app_settings.version,
        "contact": {
            "name": app_settings.contact_name,
            "email": app_settings.contact_email,
        },
        "orders_count": len(repository.get_all()),
    }


@app.post(
    "/orders",
    response_model=Order,
    status_code=201,
    tags=["редактирование"],
    summary="Создание заказа",
)
def create_order(
    request: OrderCreateRequest,
    order_service: OrderService = Depends(get_order_service),
):
    return order_service.create_order(request.model_dump())


@app.get(
    "/orders",
    response_model=OrderList,
    status_code=200,
    tags=["получение заказов"],
    summary="Список заказов",
)
def get_orders(
    app_settings: Settings = Depends(get_settings),
    order_service: OrderService = Depends(get_order_service),
    offset: int = Query(default=0, ge=0),
    limit: int | None = Query(default=None, ge=1),
    filter: OrderStatus | None = Query(default=None),
):
    return order_service.list_orders(app_settings, offset, limit, filter)


@app.get(
    "/orders/{order_id}",
    response_model=Order,
    status_code=200,
    tags=["получение заказов"],
    summary="Заказ по идентификатору",
)
def get_order_by_id(
    order_id: UUID,
    order_service: OrderService = Depends(get_order_service),
):
    return order_service.get_order(order_id)


@app.patch(
    "/orders/{order_id}",
    response_model=Order,
    status_code=200,
    tags=["редактирование"],
    summary="Частичное обновление заказа",
)
def patch_order(
    order_id: UUID,
    request: OrderPatchRequest,
    order_service: OrderService = Depends(get_order_service),
):
    updates = request.model_dump(exclude_unset=True)
    return order_service.patch_order(order_id, updates)


@app.delete(
    "/orders/{order_id}",
    status_code=204,
    tags=["редактирование"],
    summary="Отмена заказа",
)
def delete_order(
    order_id: UUID,
    order_service: OrderService = Depends(get_order_service),
):
    order_service.delete_order(order_id)
