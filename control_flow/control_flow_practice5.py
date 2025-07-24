import requests
from pprint import pprint as print

# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'

# API 요청
response = requests.get(API_URL)

# JSON → Python 리스트
parsed_data = response.json()

# 블랙리스트 기업
black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

# 🔹 블랙리스트 검사 함수
def censorship(company_name, user_name):
    if company_name in black_list:
        print(f'{company_name} 소속의 {user_name} 은/는 등록할 수 없습니다.')
        return False
    else:
        print('이상 없습니다.')
        return True

# 🔹 유저 등록 함수
def create_user(user_list):
    censored_user_list = {}

    for user in user_list:
        company = user['company']['name']
        name = user['name']

        if censorship(company, name):
            censored_user_list[company] = [name]

    return censored_user_list

# 실행
print(create_user(parsed_data))    
    



