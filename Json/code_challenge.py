import json

jsondata ="""{
	"faculty1": {
		"firstname": "chetan",
		"lastname": "mali",
		"photo": "abc",
		"department": "CE",
		"RA": "cloud",
		"contactD": {"phone":8236945, "email":"abc@gmail.com"}
	},
	"faculty2": {
		"firstname": "avi",
		"lastname": "ag",
		"photo": "xyz",
		"department": "CEG",
		"RA": "hardware",
		"contactD": {"phone":83434345, "email":"xyz@gmail.com"}
	}
}
    """
my_data = json.loads(jsondata)
print(my_data)
print(my_data["faculty1"]["contactD"]["phone"])

new_jsondata =json.dumps(my_data)
print(new_jsondata)
print(type(new_jsondata))

with open("data_file.json", "w") as write_file:
    json.dump(jsondata, write_file)
    #json.dump(jsondata, write_file, indent=2   )

x =json.dumps(my_data , indent = 2)