from abc import ABC, abstractmethod


class CacheRepository(ABC):
    @abstractmethod
    def save_forecast(self, key: str, value: str) -> None:
        raise NotImplementedError
