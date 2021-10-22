import requests

URL='http://localhost:8000/employees/6/'
data=requests.get(url=URL)
j_data=data.json()

print(j_data)