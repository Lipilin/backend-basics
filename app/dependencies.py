from functools import lru_cache
from typing import Annotated

from fastapi import Depends, Query
from exceptions import PageLimitExceededError
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


def get_pagination_settings(
    settings: SettingsDependency, 
    limit: int | None = Query(default = None, ge = 1), 
    offset: int = Query(default = 0, ge = 0),
) -> PaginationSettings:
    if limit is None:
        limit = settings.default_page_size
    if limit > settings.max_page_size:
        raise PageLimitExceededError(settings.max_page_size)
    return PaginationSettings(
        limit = limit,
        offset = offset,
    )


PaginationSettingsDependency = Annotated[
    PaginationSettings, Depends(get_pagination_settings)
]
