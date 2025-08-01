# 사용 전 -> 빈 리스트가 필요하고, append가 필요함 -> 그래야 새로운 리스트가 만들어짐
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)


# 사용 후 -> 리스트 컴프리핸션을 빈 리스트도 필요 없고 for문의 append를 한 줄로 끝내버림 -> append를 안씀
numbers = [1, 2, 3, 4, 5]
squared_numbers = [num**2 for num in numbers]
#같은 코드드
squared_numbers = list(num**2 for num in numbers)


# List Comprehension 활용 예시 
# "2차원 배열 생성 시 (인접행렬 생성 시)"
data1 = [[0] * (5) for _ in range(5)]
#또는
data2 = [[0 for _ in range(5)] for _ in range(5)]

"""
[[0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0]]
"""
