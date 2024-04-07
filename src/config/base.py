from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str

    OPEN_WEATHER_MAP_API_KEY: str
    OPEN_WEATHER_MAP_BASE_URL: str = "https://api.openweathermap.org/data/3.0/onecall"
    OPEN_WEATHER_MAP_EXCLUDED_FORECASTS: str = "daily,minutely"
    WEATHER_CACHE_KEY: str = "weather_forecast"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
