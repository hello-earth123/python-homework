# # get
# person = {'name': 'Alice', 'age': 25}
# print(person.get('name'))
# print(person.get('country'))
# print(person.get('country', '해당 키는 존재하지 않습니다.'))
# # print(person['country'])  # KeyError: 'country'

# # keys
# person = {'name': 'Alice', 'age': 25}
# print(person.keys()) # dict_keys(['name', 'age']) -> 
# for key in person.keys():
#     print(key)
# #실시간으로 동기화되는 확인창 / 중요한건 key들을 뽑아낼 수 있다.

# # values
# person = {'name': 'Alice', 'age': 25}
# print(person.values())  # dict_values(['Alice', 25])


# # items
# person = {'name': 'Alice', 'age': 25}
# print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
# for key, value in person.items():
#     print(key, value)


# # pop
# person = {'name': 'Alice', 'age': 25}
# print(person.pop('age'))  # 25
# print(person)  # {'name': 'Alice'}
# print(person.pop('country', None))  # None -> default 설정
# # print(person.pop('country'))  # KeyError: 'country' #default 설정X

# # clear
# person = {'name': 'Alice', 'age': 25}
# person.clear()
# print(person)

# setdefault
person = {'name': 'Alice', 'age': 25}
print(person.setdefault('country', 'KOREA'))  # KOREA
print(person.setdefault('name', 'KOREA')) # 여기서 KOREA는 쓸 일이 없음 -> default값을 쓰려면 key가 없어야 하는데 'name'키가 있기 때문
print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}


# update
person = {'name': 'Alice', 'age': 25}
other_person = {'name': 'Jane', 'country': 'KOREA'}

person.update(other_person) 
print(person)  # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}

person.update(age=100, address='SEOUL')
print(
    person
)  # {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}
