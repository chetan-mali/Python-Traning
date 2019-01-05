# code challenge 1
"""
Get me the other details about the city from the openweathermap.org
    Latitude and Longitude 
    Weather Condition 
    Wind Speed
    Sunset Rise and Set timing 
"""

city =input("Enter your city name :")

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+city
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
url = url1 + url2 + url3

import json
import requests
response = requests.get(url)
if response.status_code==200:
    jsondata = response.json()
    print("\nWeather Details of :"+city)
    print("\tLatitude         :",jsondata['coord']['lon'])
    print("\tLongitude        :",jsondata['coord']['lat'])
    print("\tWeather Condition:",jsondata['weather'][0]['main'])
    print("\tWeather Condition:",jsondata['wind']['speed'])
    print("\tSunRise          :",jsondata['sys']['sunrise'])
    print("\tSunSet           :",jsondata['sys']['sunset'])
else :
    print("Invalid city name !!!")