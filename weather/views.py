"""
Views:
    Explanation:
        in Django, views are the functions that take a web request and return a web response.
    Equivalent in Node.js To:
        Express.js controllers
"""
from django.shortcuts import render
import json

# Create your views here.
import requests
from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from decouple import config


@api_view(['POST'])
def get_weather(request):
    city = request.data.get('city')
    latitude = request.data.get('latitude')
    longitude = request.data.get('longitude')
    use_current_location = request.data.get('useCurrentLocation')

    api_key = '4d8b13b2dc6b8b1c157b83bad078d92d'

    if use_current_location and latitude and longitude:
        location_key = f"{latitude},{longitude}"
        cache_key = f"weather_{location_key}"
    else:
        cache_key = f"weather_{city}"

    # Check cache first
    cached_data = cache.get(cache_key)
    if cached_data:
        return Response(cached_data)

    # If not cached, make a request to the weather API
    if use_current_location and latitude and longitude:
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
        print("url", url)
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        print("url", url)

    response = requests.get(url)
    if response.status_code == 200:
        weather_data = response.json()
        cache.set(cache_key, weather_data, timeout=300)  # Cache for 5 minutes
        # print in a human-readable format
        # print("weather_data", json.dumps(weather_data, indent=4))
        # print("weather_data", weather_data)
        return Response(weather_data)
    else:
        return Response({'error': 'Could not fetch weather data'}, status=response.status_code)
