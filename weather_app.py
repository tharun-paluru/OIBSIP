#weather app in python that fetches and displays current weather data of specifired location using weather API

import requests
import json
import os

api_key = os.getenv("weatherapp_api")  #hiding the openweatherapp's APIkey from coders using system varibles


#main program
area = input(" Pleasle! Enter the location:")
url = f"https://api.openweathermap.org/data/2.5/weather?&q={area}&units=metric&appid={api_key}" #url of the openweathermap app to get the real time live data
weather_data = requests.get(url)
found=weather_data.status_code   #to find out weather the entered location is present

if (found==200):                 #Printing the weather conditions in simple form if location is found 
    weather=weather_data.json()["weather"][0]["main"]
    temp = round(weather_data.json()["main"]["temp"])
    humd = round(weather_data.json()["main"]["humidity"])
    print(f"The WEATHER in {area} is :{weather}")
    print(f"The TEMPERATURE in {area} is : {temp}°C")
    print(f"THE HUMIDITY in {area} is: {humd}%")
elif (found==404):
    print("city is not found")
else:
    print("error occured! please retry")
