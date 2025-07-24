import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()



dummy_data = []
for id in range(10):
    dict ={
        'company' : parsed_data[id]['company']['name'], #str
        'lat' : parsed_data[id]['address']['geo']['lat'], #dict
        'lng' : parsed_data[id]['address']['geo']['lng'], #dict
        'name' : parsed_data[id]['name'] #str 
        }

    if -80 < float(parsed_data[id]['address']['geo']['lat']) < 80 and -80 < float(parsed_data[id]['address']['geo']['lng']) < 80:
        dummy_data.append(dict)
    

print(dummy_data)
