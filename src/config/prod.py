from src.config.base import BaseConfig


class ProdConfig(BaseConfig):
    ENV: str = "prod"
