import os

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).removesuffix(
    os.path.join("src", "core")
)


class Settings(BaseSettings):
    ROOT_DIR: str = ROOT_DIR
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    DATABASE_URL: str = f"sqlite+aiosqlite:///{ROOT_DIR}/data/food_delivery.sqlite3"

    model_config = SettingsConfigDict(env_file=f"{ROOT_DIR}/../env")


settings = Settings()
