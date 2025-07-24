number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1
    return number_of_people

def create_user(name, age, address):
    user_info = {'name' : name, 'age' : age, 'address' : address}
    print(f'{name}님 환영합니다!')
    increase_user()
    return user_info





name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

user = list(map(lambda i : create_user(name[i], age[i], address[i]), range(len(name))))
print(user)

#호출된 함수에 의해 return된 값은 map()함수에 의해 map()의 결과로 저장 된다.
#lambda는 익명 함수이다. 이름 없는 lambda라는 이름의 i 매개변수를 가진 함수