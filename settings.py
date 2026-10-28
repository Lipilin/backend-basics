from fastapi import FastAPI
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    description: str
    version: str
    contact_name: str
    contact_email: str
    default_page_size: int
    max_page_size: int
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()


def get_settings() -> Settings:
    return settings


def create_app() -> FastAPI:
    return FastAPI(
        title=settings.app_name,
        description=settings.description,
        version=settings.version,
        contact={
            "name": settings.contact_name,
            "email": settings.contact_email,
        },
    )
