from abc import ABC, abstractmethod
from typing import Union


class WeatherApiClient(ABC):
    @abstractmethod
    def get_weather(self, lat: Union[float, int], lon: Union[float, int]):
        raise NotImplementedError
