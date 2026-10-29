from fastapi import FastAPI
from fastapi.responses import JSONResponse

from dependencies import RepositoryDependency, SettingsDependency, get_settings
from exceptions import (
    OrderAlreadyCompletedError,
    OrderNotFoundError,
    PageLimitExceededError,
)
from routers.orders import router as orders_router

app = FastAPI(
    title=get_settings().app_name,
    description=get_settings().description,
    version=get_settings().version,
    contact={
        "name": get_settings().contact_name,
        "email": get_settings().contact_email,
    },
)


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


@app.exception_handler(PageLimitExceededError)
def handle_page_limit_exceeded(_request, exc: PageLimitExceededError):
    return JSONResponse(
        status_code=422,
        content={"detail": str(exc)},
    )


@app.get("/", tags=["сервис"], summary="Приветствие")
def read_root():
    return {"message": "Добро пожаловать в сервис заказов кофейни!"}


@app.get("/info", status_code=200, tags=["сервис"], summary="Информация о сервисе")
def get_info(
    app_settings: SettingsDependency,
    repository: RepositoryDependency,
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


app.include_router(orders_router)
