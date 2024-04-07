import logging
from functools import lru_cache
from typing import Optional

import redis

from config import settings

logger = logging.getLogger(__name__)


class RedisClient:
    def __init__(self):
        self.host: str = settings.REDIS_HOST
        self.port: str = settings.REDIS_PORT
        self.password: str = settings.REDIS_PASSWORD
        self.client: Optional[redis.Redis] = None
        try:
            logger.info("Connecting to Redis")
            self.client = redis.Redis(
                host=self.host, port=self.port, password=self.password
            )
        except Exception as e:
            logger.error(f"Error while connecting to Redis: {e}")
            raise e

    def shutdown(self):
        if self.client is not None:
            logger.info("Shutting down Redis")
            self.client.close()

    def set(self, key: str, value: str, exp=None):
        self.client.set(key, value)  # type: ignore


@lru_cache(maxsize=1)
def get_redis_client():
    return RedisClient()
