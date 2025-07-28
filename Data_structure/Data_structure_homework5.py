# 아래 함수를 수정하시오.
def remove_duplicates(list):
    new_lst = []

    for i in list:
        if i not in new_lst:
            new_lst.append(i)
        else:
            continue           
    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)

# set으로 중복을 지울 수도 있지만
# 새로운 리스트에 만약 없다면 추가, 이미 있다면(중복이라면) continue를 통해 중복 없는 리스트를 작성 가능