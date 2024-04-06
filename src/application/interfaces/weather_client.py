from abc import ABC, abstractmethod


class WeatherApiClient(ABC):
    @abstractmethod
    def get_weather(self, lat: int, lon: int):
        raise NotImplementedError
