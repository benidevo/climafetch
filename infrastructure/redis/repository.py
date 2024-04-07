import json

from application.dto.weather import WeatherData
from application.interfaces.cache_repository import CacheRepository
from config import settings
from infrastructure.redis.client import get_redis_client


class RedisCacheRepository(CacheRepository):
    def __init__(self):
        self.client = get_redis_client()
        self.key = settings.WEATHER_CACHE_KEY

    def save_forecast(self, value, exp=None):
        if not value:
            return
        weather_forecast = []
        for weather_data in value:
            weather_data: WeatherData = weather_data.model_dump(mode="json")
            weather_forecast.append(weather_data)

        value = json.dumps(weather_forecast)
        self.client.set(self.key, value)
