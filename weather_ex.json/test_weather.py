import requests
import pytest

url = "https://api.openweathermap.org/data/2.5/weather"
access_key = "ec63e10e4c51fdc5f50c23a5f57c9f0a"

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def test_kelvin_to_celsius():
    kelvin_temp = 300
    expected_celsius_temp = 26.85
    result = kelvin_to_celsius(kelvin_temp)
    assert abs(result - expected_celsius_temp) < 0.01


def test_weather_api_integration():
    lat = 41.0082
    lon = 28.9784
    response = requests.get(url, params={"lat": lat, "lon": lon, "appid": access_key})
    weather_data = response.json()
    assert response.status_code == 200
    assert "name" in weather_data
    assert "weather" in weather_data
    assert "main" in weather_data
    assert "wind" in weather_data
