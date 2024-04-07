import logging
from typing import Optional, Union

import requests
from pydantic.types import Json

from application.dto.weather import WeatherData
from application.interfaces.weather_client import WeatherApiClient
from config import settings

logger = logging.getLogger(__name__)


class OpenWeatherMapClient(WeatherApiClient):
    def __init__(self):
        self.api_key: str = settings.OPEN_WEATHER_MAP_API_KEY
        self.base_url: str = settings.OPEN_WEATHER_MAP_BASE_URL
        self.excluded_forecasts: str = settings.OPEN_WEATHER_MAP_EXCLUDED_FORECASTS
        self.weather_data: Optional[WeatherData] = None

    def get_weather(self, lat: Union[float, int], lon: Union[float, int]):
        url = f"{self.base_url}?lat={lat}&lon={lon}&exclude={self.excluded_forecasts}&appid={self.api_key}&units=metric"
        response: Optional[requests.Response] = self._make_request(url)
        self._validate_response(response)
        return self.weather_data

    def _make_request(self, url: str) -> Optional[requests.Response]:
        logger.info("Making OpenWeatherMap API call")
        try:
            response: requests.Response = requests.get(url)
        except (requests.ConnectionError, requests.Timeout) as e:
            logger.error(f"Error while connecting to OpenWeatherMap API: {e}")
            return None
        if response.status_code != 200:
            logging.warn(
                f"Unexpected response from OpenWeatherMap API: {response.status_code}"
            )
            return None
        logging.info("OpenWeatherMap API call successful")
        return response.json()

    def _validate_response(self, response: Optional[Json]) -> None:
        if not response:
            logging.warn("Invalid response from OpenWeatherMap API", response)
            return
        try:
            validated_response = WeatherData(**response)

        except Exception as e:
            logging.warn(f"Invalid response from OpenWeatherMap API: {e}")
            return
        self.weather_data = validated_response
