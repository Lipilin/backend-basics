from fastapi import FastAPI
from db import coffee_shop_dict
from fastapi import HTTPException
import uuid
from models import (
    Order,
    OrderList, 
    OrderCreateRequest, 
    OrderPatchRequest, 
    OrderStatus
)

app = FastAPI(
    title = "Сервис по обработке заказов кофейни",
    description = "Сервис по обработке заказов кофейни",
    version = "1.0.0",
    contact = {
        "name": "Egor Lipilin",
        "email": "egor.lipilin@example.com"
    }
)

def ensure_order_exists(order_id: str):
    if order_id not in coffee_shop_dict:
        raise HTTPException(
            status_code=404, 
            detail=f'Заказ с ID {order_id} не найден'
        )

@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в сервис заказов кофейни!"}

@app.post("/orders", response_model=Order, status_code = 201)
def create_order(request: OrderCreateRequest):
    order_request_dict = request.model_dump()
    new_order = Order(id = uuid.uuid4(), **order_request_dict)
    coffee_shop_dict[new_order.id] = new_order
    return new_order

@app.get("/orders", response_model=OrderList, status_code = 200)
def get_orders(offset: int, limit: int):
    return OrderList(orders = list(coffee_shop_dict.values()))

@app.get("/orders/{order_id}", response_model=Order, status_code = 200)
def get_order_by_id(order_id: str):
    ensure_order_exists(order_id)
    return coffee_shop_dict[order_id]

@app.patch("/orders/{order_id}", response_model=Order, status_code = 200)
def patch_order(order_id: str, request: OrderPatchRequest):
    ensure_order_exists(order_id)

@app.delete("/orders/{order_id}", status_code = 204)
def delete_order(order_id: str):
    ensure_order_exists(order_id)
    coffee_shop_dict[order_id].status = OrderStatus.CANCELLED