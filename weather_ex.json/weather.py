import requests

url = "https://api.openweathermap.org/data/2.5/weather"
access_key = "ec63e10e4c51fdc5f50c23a5f57c9f0a"

response = requests.get(url, params={"lat": 41.0082, "lon": 28.9784, "appid": access_key})
weather_data = response.json()

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


print("Şehir: ", weather_data["name"])
print("Hava Durumu: ", weather_data["weather"][0]["description"])
print("Sıcaklık: ", round(kelvin_to_celsius(weather_data["main"]["temp"]), 2), "°C")
print("Hissedilen Sıcaklık: ", round(kelvin_to_celsius(weather_data["main"]["feels_like"]), 2), "°C")
print("Minimum Sıcaklık: ", round(kelvin_to_celsius(weather_data["main"]["temp_min"]), 2), "°C")
print("Maksimum Sıcaklık: ", round(kelvin_to_celsius(weather_data["main"]["temp_max"]), 2), "°C")
print("Rüzgar Hızı: ", weather_data["wind"]["speed"], "m/s")
