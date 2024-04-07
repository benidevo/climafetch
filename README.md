# ClimaFetch

## Overview

ClimaFetch is a cloud-based solution designed to dynamically collect daily weather data from [OpenWeatherMap](https://openweathermap.org/), orchestrated by Google Cloud Pub/Sub and automated through Cloud Scheduler. The fetched data is processed and stored in a Google Cloud Platform (GCP)-managed Redis cluster, offering rapid access to applications that require up-to-date weather information. This project leverages Python 3.11, [Requests](https://requests.readthedocs.io/) for API calls, and [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation and settings management.

## Features

- **Data Collection**: Automated fetching of daily weather data from OpenWeatherMap.
- **Cloud-Native**: Utilizes GCP services including Cloud Functions, Cloud Pub/Sub, and Cloud Scheduler for scalable, serverless execution.
- **Data Storage**: Efficient storage in a managed Redis cluster for quick retrieval.
- **Real-Time Updates**: Ensures that consuming applications receive the most current weather data available.

## Prerequisites

- Google Cloud Platform account
- Python 3.11
- Access to OpenWeatherMap API

## Configurations

Create a .env file in the root directory of the project and add the environment variables in env.example

## Installation

Ensure you have Python 3.11 and Docker installed on your system. Clone the repository and run the app:

```sh
sh run.sh
```

## Deployment

- Deploy the Cloud Function:
- Navigate to the Google Cloud Console and deploy the ClimaFetch function to Cloud Functions.
- Set up Cloud Scheduler:
  - Create a Cloud Scheduler job to trigger the ClimaFetch function daily.
- Configure Cloud Pub/Sub:
  - Set up a Cloud Pub/Sub topic as the trigger for the ClimaFetch function.

## Usage

Once deployed, ClimaFetch will automatically execute at the scheduled time, fetching and storing weather data in Redis. Applications can access this data by querying the Redis cluster.
