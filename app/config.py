from pydantic import BaseModel
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


class PaginationSettings(BaseModel):
    size: int
    max_size: int
