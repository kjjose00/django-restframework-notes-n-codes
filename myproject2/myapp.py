import requests
import json

URL='http://127.0.0.1:8000/stucreate/'

data={
    'name':'jose', #python dictionary
    'roll':101,
    'city':'Delhi',
}

json_data=json.dumps(data) #converts to json data from python dictionary
r=requests.post(url=URL,data=json_data)

data=r.json()
print(data)



