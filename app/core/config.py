# app/core/config.py
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "VaultPay"
    VERSION: str = "1.0.0"

    # Database URL → later we’ll use PostgreSQL, for now sqlite
    DATABASE_URL: str = "sqlite:///./vaultpay.db"

    class Config:
        env_file = ".env"  # allows overriding via .env file

# Singleton instance
settings = Settings()
