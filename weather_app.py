#weather app in python that fetches and displays current weather data of specifired location using weather API

import requests
import json
import os

api_key = os.getenv("weatherapp_api")
#api_key="721c549afe2421a27447e42874bc9cf9"
print(api_key)

#main
area = input("Enter the location:")
url = f"https://api.openweathermap.org/data/2.5/weather?&q={area}&units=metric&appid={api_key}"
weather_data = requests.get(url)
found=weather_data.status_code
print(found)
if found==200:
    weather=weather_data.json()["weather"][0]["main"]
    temp = round(weather_data.json()["main"]["temp"])
    humd = round(weather_data.json()["main"]["humidity"])
    print(f"The WEATHER in {area} is :{weather}")
    print(f"The TEMPERATURE in {area} is : {temp}°C")
    print(f"THE HUMIDITY in {area} is: {humd}%")
elif found==404:
    print("city is not found")
else:
    print("error occured! please retry")