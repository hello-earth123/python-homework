# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    return set1.union(set2)

def union_multiple_sets(*sets):
    s = set()
    for st in sets:
        if len(sets) < 2 :
            print('최소 두 개의 셋이 필요합니다.')
        else:
           s = s.union(st) # union함수는 반환까지 해주므로 할당을 해줘야 저장이됨
    return s


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# 출력 : 최소 두 개의 셋이 필요합니다
