data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
for i in data_1:
    if i.isupper() == True or ' ' in i:
        print(i, end ='')

print()

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.

arr.append(data_2.find('내')) # data_2[i]
arr.append(data_2.find('힘')) # data_2[j]
arr.append(data_2.find('들')) # data_2[k]
arr.append(data_2.find('다')) # data_2[p]

print(arr)
arr.sort()
print(arr)
for j in arr:
    print(data_2[j], end = '')