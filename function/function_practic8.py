number_of_people = 0
number_of_book = 100

def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people

def decrease_book(rent):
    global number_of_book
    number_of_book -= rent
    print(f'남은 책의 수 : {number_of_book}')
    return number_of_book

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(name, age, address):
    user_info = {'name' : name, 'age' : age, 'address' : address}
    increase_user()
    print(f'{name}님 환영합니다!')
    return user_info


many_user = list(map(lambda a,b,c: create_user(a,b,c), name, age, address))

#lambda는 인자에 대해 return값이 두 개가 될 수 없다. 따라서 튜플로 묶어줘야 한다.
info_dict = dict(map(lambda i: (i['name'], i['age']) , many_user))

def rental_book(info):
    decrease_book(int(info['age'] // 10))
    print(f"{info['name']}님이 {info['age'] // 10}권의 책을 대여하였습니다.")


list(map(lambda name: rental_book({'name': name, 'age': info_dict[name]}), info_dict))