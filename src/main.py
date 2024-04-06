from application.services import WeatherForecastService


def main():
    service = WeatherForecastService()
    lat, lon = 48.8566, 2.3522
    weather = service.get_weather(lat, lon)
    return weather


if __name__ == "__main__":
    print(main())
