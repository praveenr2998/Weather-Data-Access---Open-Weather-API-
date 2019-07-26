import requests
import json
 
from pprint import pprint
 
API_key = "b6264876af30a491aa320e16bf3f296b"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
city_name = input("Enter a city Name : ")
Final_url = base_url + "appid=" + API_key + "&q=" + city_name
 
weather_data = requests.get(Final_url).json()
 
print("\nCurrent Weather Data Of " + city_name +":\n")
pprint(weather_data)
