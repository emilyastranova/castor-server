import enum
from pathlib import Path
from tempfile import gettempdir
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

from castor_lib.core.database import DatabaseConfig, CastorDatabase

TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "0.0.0.0"
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False

    # Database
    db_host: str = "127.0.0.1"
    db_port: int = 27017
    db_user: str = "root"
    db_password: str = "changeme"

    # Current environment
    environment: str = "dev"

    log_level: LogLevel = LogLevel.INFO

    # This variable is used to define
    # multiproc_dir. It's required for [uvi|guni]corn projects.
    prometheus_dir: Path = TEMP_DIR / "prom"

    # Grpc endpoint for opentelemetry.
    # E.G. http://localhost:4317
    opentelemetry_endpoint: Optional[str] = None
    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="CASTOR_SERVER_",
        env_file_encoding="utf-8",
    )


settings = Settings()
database_config = DatabaseConfig(
    host=settings.db_host,
    port=settings.db_port,
    username=settings.db_user,
    password=settings.db_password,
)
database = CastorDatabase(database_config)
