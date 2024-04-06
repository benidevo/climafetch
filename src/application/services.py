from application.interfaces.weather_client import WeatherApiClient
from infrastructure.open_weather_map.client import OpenWeatherMapClient


class WeatherForecastService:
    def __init__(self):
        self.client: WeatherApiClient = OpenWeatherMapClient()

    def get_weather(self, lat: int, lon: int):
        return self.client.get_weather(lat, lon)
