import os

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)).removesuffix(
    os.path.join("src", "core")
)


class Settings(BaseSettings):
    ROOT_DIR: str = ROOT_DIR

    model_config = SettingsConfigDict(env_file=f"{ROOT_DIR}/../env")


settings = Settings()
