from abc import ABC, abstractmethod


class CacheRepository(ABC):
    @abstractmethod
    def get(self, key):
        raise NotImplementedError

    @abstractmethod
    def set(self, key, value, exp=None):
        raise NotImplementedError
