def ordered_difference_sets(set1, set2):
    dif_set = set1.difference(set2) 
    dif_set_2 = set2.difference(set1)
    if len(dif_set) <= len(dif_set_2):
        return dif_set, dif_set_2
    else: 
        len(dif_set) > len(dif_set_2)
        return dif_set_2, dif_set

# 예시 실행
result = ordered_difference_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print("결과:", result)  # 출력: ({1, 2}, {5, 6})

result = ordered_difference_sets({1, 2, 3, 4}, {1, 2, 3})
print("결과:", result)  # 출력: (set(), {4})
