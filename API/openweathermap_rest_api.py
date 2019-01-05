#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:05:13 2018

@author: dev
"""

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"
url = url1 + url2 + url3

import json
import requests
response = requests.get(url)
print (response.text)


print (("Status code: " + str(response.status_code)))

print (response.headers)

jsondata = response.json()



print (jsondata)

print (type(jsondata))

print (jsondata.keys())

print (jsondata.values())

 

for key, value in jsondata.items():

    print (key, ":" ,value , "\n")



# response has the original JSON String 

# jsondata has the convert string in the python data type

with open("weather_file.json", "w") as write_file:
    json.dump(jsondata, write_file)

