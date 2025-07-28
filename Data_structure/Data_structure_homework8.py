# 아래 함수를 수정하시오.
def even_elements(list):
    even_list = []

    for i in range(len(list)):
        if list[i] % 2 != 0:
            list.pop(i)
            list.extend([1])
            if list[i] != 1:
                even_list.append(list[i])


    return even_list



my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)


# 아래 함수를 수정하시오. # 이 방법이 더 좋은듯
def even_elements(list):

    for _ in range(len(list)):
        if list[0] % 2 != 0:
            list.pop(0)

        else:
            list.extend(list[0])

    return list