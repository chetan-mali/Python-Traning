#code challenge 2 
"""
Currency Converter Convert  from USD to INR
You need to fetch the current conversion prices from the JSON  using REST API
"""
import json
import requests

url = "http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y"
response = requests.get(url)
jsondata = response.json()
print(jsondata)

value = jsondata['USD_INR']['val']

while(True):
    try:
        user_input =  float(input("Enter Amount in INR :"))
    except Exception:
        print("Invalid Input !!")
    else:
        break
print("Value of Amount in USD:",user_input/value)