from enum import Enum
import os
from pydantic import PostgresDsn, RedisDsn
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class EnvironmentType(str, Enum):
    PROJECT_ENVIRONMENT = os.environ.get("PROJECT_ENVIRONMENT")
    DATABASE_HOSTNAME = os.environ.get("DATABASE_HOSTNAME")
    DATABASE_PORT = os.environ.get("DATABASE_PORT")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORTHM = os.environ.get("ALGORTHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")
    VERSION = os.environ.get("VERSION", "v1")


class BaseConfig(BaseSettings):

    class Config:
        case_sensitive = True


class Config(BaseConfig):
    DEBUG: int = 0
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: str = EnvironmentType.PROJECT_ENVIRONMENT
    POSTGRES_URL: str = "postgresql+asyncpg://postgresuser:root@localhost:5432/fastapi"
    # REDIS_URL: RedisDsn = "redis://localhost:6379"
    RELEASE_VERSION: str = "0.1"
    # SHOW_SQL_ALCHEMY_QUERIES: int = 0
    SECRET_KEY: str = "super-secret-key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24
    # CELERY_BROKER_URL: str = "amqp://rabbit:password@localhost:5672"
    # CELERY_BACKEND_URL: str = "redis://localhost:6379/0"


config: Config = Config()
