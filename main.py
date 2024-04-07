from application.service import WeatherForecastService

import functions_framework

@functions_framework.http
def weather_forecast():
    service = WeatherForecastService()
    service.run()
    return "OK"
