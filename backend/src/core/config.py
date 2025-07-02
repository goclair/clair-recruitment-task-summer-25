import os

from dotenv import load_dotenv


def _require_env_var(name: str, default: str | None = None) -> str:
    value = os.getenv(name)
    if value is None:
        if default is None:
            raise EnvironmentError(f"Missing required environment variable: {name}")
        return default
    return value


load_dotenv()

DB_HOST = _require_env_var("DB_HOST")
DB_NAME = _require_env_var("DB_NAME")
DB_USER = _require_env_var("DB_USER")
DB_PASSWORD = _require_env_var("DB_PASSWORD")
