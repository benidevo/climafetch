from application.service import WeatherForecastService

import functions_framework

@functions_framework.http
def main():
    service = WeatherForecastService()
    service.run()
    return "OK"
