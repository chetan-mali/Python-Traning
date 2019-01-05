#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 12:24:00 2018

@author: dev
"""

import json

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""

print (type(json_string))

# Converts  JSON Data types to Python Data Types

my_data = json.loads(json_string)


print (type(my_data) )  # its a python dictionary  , it uses the table to convert 

print (my_data) 

print (my_data['researcher'])

print (my_data['researcher']['relatives'])

print (my_data['researcher']['relatives'][0])

print (my_data['researcher']['relatives'][0]['name'])

# Converts Python Data types to JSON Data Types
new_json_string = json.dumps(my_data)

print (type(new_json_string) )



#Writing/Storing the JSON data in a File 


# Writing/Storing the JSON data in a File 
with open("data_file.json", "w") as write_file:
    json.dump(json_string, write_file)
    # json.dump(json_string, write_file, indent=2   )

print (type(new_json_string)) 


new_json_string = json.dumps(my_data, indent=1 )

print (new_json_string) 


#Reading from a JSON file

with open("data_file.json", "r") as write_file:
    jsondata=json.load(write_file)
    print(jsondata)
 
    # JSON in python data structure 
    my_data = json.loads(jsondata)
    print ( my_data)

new_json_string = json.dumps(my_data, indent=2, sort_keys=True)

print (new_json_string) 