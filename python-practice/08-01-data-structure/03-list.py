# append
my_list = [1, 2, 3]
my_list
print(my_list.append(4))  # [1, 2, 3, 4]
# append는 None을 반환합니다.
print(my_list)  # None

# extend
my_list = [1, 2, 3]
my_list
print(my_list.extend([4, 5, 6]))  # [1, 2, 3, 4, 5, 6]

# extend와 append의 비교
my_list.append([5, 6, 7])
print(my_list)  # [1, 2, 3, 4, 5, 6, [5, 6, 7]]

# my_list.extend(100)  # TypeError: 'int' object is not iterable

# insert
my_list = [1, 2, 3]
my_list
print(my_list.insert(1, 5))  # [1, 5, 2, 3]

# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list
print(my_list.remove(2))  # [1, 3, 2, 2, 2]

# pop
my_list = [1, 2, 3, 4, 5]
item1 = my_list
item2 = my_list

print(item1.pop())  # 5
print(item2.pop(0))  # 1
print(my_list)  # [2, 3, 4]


# clear
my_list = [1, 2, 3]
my_list
print(my_list.clear())  # []

# index
my_list = [1, 2, 3]
index = my_list
print(index)  # 1

# count
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list
print(counting_number)  # 3

# reverse
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
# reverse는 None을 반환합니다.
# print(my_list.reverse())  # None -> 이거 주석처리 안하면 .reverse()가 두 번 처리되어 다시 원상복구됨
# reverse는 원본 리스트를 변경합니다.
print(my_list)  # [9, 1, 8, 2, 3, 1]

# sort
my_list = [3, 2, 100, 1]
my_list.sort()
# sort는 None을 반환합니다.
# print(my_list.sort())  # None
# sort는 원본 리스트를 변경합니다.
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True) #키워드 인자를 넣어주면 (reverse = True) 내림차순 / 기본 인자 값이 reverse = False라는 것을 알 수 있음
print(my_list)  # [100, 3, 2, 1]
