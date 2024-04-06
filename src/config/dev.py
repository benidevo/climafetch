from config.base import BaseConfig


class DevConfig(BaseConfig):
    ENV: str = "dev"
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = "dev_pass"
