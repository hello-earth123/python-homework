number_of_people = 0
number_of_book = 100

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people

def decrease_book(rent):
    global number_of_book
    left = number_of_book - (rent)
    print(f'남은 책의 수 : {left}') 
    # print(f'{name}님이 {rent}권의 책을 대여하였습니다.')
    return left


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']



def create_user(name, age, address):
    user_info = {'name' : name, 'age' : age, 'address' : address}
    print(f'{name}님 환영합니다!')
    increase_user()
    return user_info


many_user = list(map(lambda i : create_user(name[i], age[i], address[i]), range(len(name))))


#info인자는 딕셔너리

# 이름과 나이만 추출한 info_list 생성
info_list = list(map(lambda user: {'name': user['name'], 'age': user['age']}, many_user))

# rental_book 함수 정의
def rental_book(info):
    return list(map(lambda user: (
        print(f"{user['name']}님이 {user['age'] // 10}권의 책을 대여하였습니다."),
        decrease_book(user['age'] // 10)
    ), info))

# 대여 진행
rental_book(info_list)