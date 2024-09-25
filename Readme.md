Weather App Backend
Hello Bernhard

Introduction
    This project provides the backend for the weather application that retrieves weather data using the OpenWeatherMap API. The backend is built with Django and Django REST Framework, providing a RESTful API to serve weather data to the frontend.

The backend includes several features:

1. Fetch weather data using city name or geographical coordinates (latitude/longitude).
2. Caching of weather data to reduce redundant API calls to OpenWeatherMap.
3. Environment variable configuration for API keys.
4. Simple setup with a virtual environment to manage Python dependencies.
Features
5. Fetch Weather Data: Get current weather data based on city name or geolocation (latitude and longitude).
Caching: Weather data is cached for 5 minutes to reduce the number of API requests made to the OpenWeatherMap service.
6.API Integration: Integration with OpenWeatherMap API for fetching weather information.
7.Django REST Framework: API for communication between the frontend and backend.
8.Environment Variables: Use .env files for storing sensitive information like the OpenWeatherMap API key.

Getting Started
1. Clone the Repository
First, you need to clone the backend repository to your local machine.

after you the the "git clone"
cd weather_backend

2. Set Up Virtual Environment
Before you start working on the project, create and activate a virtual environment.

Create a Virtual Environment
To create a virtual environment, run:

python -m venv venv
Activate Virtual Environment
On Windows:

venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

3. Install Dependencies
Once the virtual environment is activated, install all required dependencies listed in the requirements.txt file. Run the following command:

pip install -r requirements.txt

4. Environment Variables Setup
i put for you in github(the .env file) to use it in the project

5. Database Migrations
Django uses a database to store data, and the database schema must be migrated before running the project. To apply migrations, run:

python manage.py migrate

6. Run the Django Development Server
After setting up the environment and applying migrations, you can start the Django development server. Run the following command:

python manage.py runserver

API Endpoints
POST /api/weather/
This endpoint accepts a POST request containing the following fields:

city (string): City name.
latitude (float): Latitude coordinate (optional).
longitude (float): Longitude coordinate (optional).
useCurrentLocation (boolean): Whether to use the current location.
Example Request:

{
    "city": "London",
    "latitude": "",
    "longitude": "",
    "useCurrentLocation": false
}
Example Response:

{
    "name": "London",
    "sys": {
        "country": "GB"
    },
    "main": {
        "temp": 15.25,
        "humidity": 72
    },
    "weather": [
        {
            "description": "clear sky"
        }
    ],
    "wind": {
        "speed": 3.09
    }
}
Project Structure
Here is an overview of the key files and folders in the backend:

weather_backend/
│
├── weather/                 # Main app folder
│   ├── migrations/          # Database migrations
│   ├── __init__.py          # App initialization
│   ├── admin.py             # Django admin settings
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models (empty for this project)
│   ├── tests.py             # Unit tests
│   ├── urls.py              # App-level URL routing
│   └── views.py             # API views and logic
│
├── weather_backend/         # Main project folder
│   ├── settings.py          # Django settings (configured to read .env)
│   ├── urls.py              # Project-level URL routing
│   └── ...
│
├── manage.py                # Django command-line utility
├── requirements.txt         # Dependencies for the project
└── .env                     # Environment variables (not committed to git)
Caching Mechanism
To reduce the load on the OpenWeatherMap API and avoid redundant API requests, the backend caches weather data for 5 minutes. The cache is implemented using Django’s caching framework.

If weather data for a location has already been fetched in the last 5 minutes, it will be retrieved from the cache instead of making another API request.

Freezing Requirements
After installing any new dependencies, you should freeze the dependencies into the requirements.txt file. To do that, run:

pip freeze > requirements.txt
This will generate an updated requirements.txt file with all installed packages.

Conclusion
By following these steps, you can successfully run the backend of the weather app. The backend is responsible for fetching weather data from OpenWeatherMap, caching results, and serving data to the frontend via a REST API.


