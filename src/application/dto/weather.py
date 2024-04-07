from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Current(BaseModel):
    dt: Optional[datetime] = None
    sunrise: datetime
    sunset: datetime
    temp: float
    feels_like: float = Field(..., alias="feels_like")
    pressure: int
    humidity: int
    dew_point: float = Field(..., alias="dew_point")
    uvi: float
    clouds: int
    visibility: Optional[int] = None
    wind_speed: float
    wind_deg: int
    weather: List[Weather]


class Hourly(BaseModel):
    dt: Optional[datetime] = None
    temp: float
    feels_like: float = Field(..., alias="feels_like")
    pressure: int
    humidity: int
    dew_point: float = Field(..., alias="dew_point")
    uvi: float
    clouds: int
    visibility: Optional[int] = None
    wind_speed: float
    wind_deg: int
    weather: List[Weather]
    rain: Optional[dict] = None


class Alert(BaseModel):
    sender_name: str
    event: str
    start: datetime
    end: datetime
    description: str
    tags: List[str]


class WeatherData(BaseModel):
    lat: float
    lon: float
    timezone: str
    timezone_offset: int
    current: Current
    hourly: List[Hourly]
    alerts: Optional[List[Alert]] = None
