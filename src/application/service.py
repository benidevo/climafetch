import logging
from typing import List, Optional, Union

from src.application.dto.weather import WeatherData
from src.application.interfaces.cache_repository import CacheRepository
from src.application.interfaces.weather_client import WeatherApiClient
from src.fixtures.cities import cites
from src.infrastructure.open_weather_map.client import OpenWeatherMapClient
from src.infrastructure.redis.repository import RedisCacheRepository

logger = logging.getLogger(__name__)


class WeatherForecastService:
    def __init__(self):
        self.client: WeatherApiClient = OpenWeatherMapClient()
        self.cache_repo: CacheRepository = RedisCacheRepository()
        self.forecast: List[WeatherData] = []

    def _get_forecast(
        self, lat: Union[float, int], lon: Union[float, int]
    ) -> Optional[WeatherData]:
        return self.client.get_weather(lat, lon)

    def run(self) -> None:
        city_count = 0
        logger.info("Retrieving weather forecasts")
        for city, coordinate in cites.items():
            city_count += 1
            lat = coordinate.get("lat")
            lon = coordinate.get("lon")
            if not lat or not lon:
                logger.error(f"Invalid coordinate for {city}")
                city_count -= 1
                continue

            weather: Optional[WeatherData] = self._get_forecast(lat, lon)
            if weather:
                self.forecast.append(weather)

        self._save_forecast()
        logger.info(f"Processed {city_count} cities")
        logger.info(f"Retrieved {len(self.forecast)} forecasts")

    def _save_forecast(self):
        self.cache_repo.save_forecast(self.forecast)
