import json
import requests
data= """{"Phone_Number":"8239192507",
        "Name":"chetan","College_Name":"poornima","Branch":"CE"
        }"""

#data = json.loads(data)
#print(data)
data = json.loads(data)
print(data)
url ="http://13.127.155.43/api_v0.1/sending"

response = requests.post(url,data)
print(str(response.status_code))

reponse_get =requests.get("http://13.127.155.43/api_v0.1/receiving?Phone_Number=987654310")

print(reponse_get.text)