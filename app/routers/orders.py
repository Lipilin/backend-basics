from uuid import UUID

from fastapi import APIRouter, Query

from dependencies import (
    PaginationSettingsDependency,
    ServiceDependency,
    SettingsDependency,
)

from schemas import (
    Order,
    OrderCreateRequest,
    OrderList,
    OrderPatchRequest,
    OrderStatus,
)
router = APIRouter(prefix="/orders")


@router.post(
    "",
    response_model=Order,
    status_code=201,
    tags=["редактирование"],
    summary="Создание заказа",
)
def create_order(
    request: OrderCreateRequest,
    order_service: ServiceDependency,
):
    return order_service.create_order(request.model_dump())


@router.get(
    "",
    response_model=OrderList,
    status_code=200,
    tags=["получение заказов"],
    summary="Список заказов",
)
def get_orders(
    order_service: ServiceDependency,
    pagination_settings: PaginationSettingsDependency,
    orderFilter: OrderStatus | None = Query(default=None),
):
    return order_service.list_orders(
        pagination_settings.offset,
        pagination_settings.limit,
        orderFilter,
    )


@router.get(
    "/{order_id}",
    response_model=Order,
    status_code=200,
    tags=["получение заказов"],
    summary="Заказ по идентификатору",
)
def get_order_by_id(
    order_id: UUID,
    order_service: ServiceDependency,
):
    return order_service.get_order(order_id)


@router.patch(
    "/{order_id}",
    response_model=Order,
    status_code=200,
    tags=["редактирование"],
    summary="Частичное обновление заказа",
)
def patch_order(
    order_id: UUID,
    request: OrderPatchRequest,
    order_service: ServiceDependency,
):
    updates = request.model_dump(exclude_unset=True)
    return order_service.patch_order(order_id, updates)


@router.delete(
    "/{order_id}",
    status_code=204,
    tags=["редактирование"],
    summary="Отмена заказа",
)
def delete_order(
    order_id: UUID,
    order_service: ServiceDependency,
):
    order_service.delete_order(order_id)
