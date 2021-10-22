import requests
import json

URL='http://127.0.0.1:8000/studentapi/'

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    print(r)
    data=r.json()
    print(data)

# get_data()
def post_data():
    data={
        'name':'my name is jose',
        'roll':117,
        'city':'london',
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    print(r)
    data=r.json()
    print(data)

def update_data():
    data={
        'id':1,
        'name':'office',
        
        'city':'us',
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,headers=headers,data=json_data)
    print(r)
    data=r.json()
    print(data)
def delete_data():
    data={
        'id':7,
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,headers=headers,data=json_data)
    print(r)
    data=r.json()
    print(data)
get_data()
