from functools import lru_cache
from typing import Annotated

from fastapi import Depends

from config import PaginationSettings, Settings
from repository import OrderRepository
from repository_abstract import OrderRepositoryAbstract
from service import OrderService


@lru_cache
def get_settings() -> Settings:
    return Settings()


SettingsDependency = Annotated[Settings, Depends(get_settings)]


@lru_cache
def get_order_repository() -> OrderRepositoryAbstract:
    return OrderRepository()


RepositoryDependency = Annotated[OrderRepositoryAbstract, Depends(get_order_repository)]


@lru_cache
def get_order_service(repository: RepositoryDependency) -> OrderService:
    return OrderService(repository)


ServiceDependency = Annotated[OrderService, Depends(get_order_service)]


def get_pagination_settings(settings: SettingsDependency) -> PaginationSettings:
    if settings.default_page_size is None:
        raise ValueError("В приложении не установлен размер страницы по умолчанию")
    if settings.max_page_size is None:
        raise ValueError("В приложении не установлен максимальный размер страницы")
    return PaginationSettings(
        size=settings.default_page_size,
        max_size=settings.max_page_size,
    )

PaginationSettingsDependency = Annotated[PaginationSettings, Depends(get_pagination_settings)]