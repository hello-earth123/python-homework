def restructure_word(word, arr):
    pass

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

arr.extend(original_word)
print(arr)

def restructure_word(word, arr):
    for x in word:
        if x.isdecimal() == True:
            for _ in range(int(x)):
                arr.pop()
        else:
            arr.remove(x)
    return arr

result = restructure_word(word, arr)
print(result)

print(''.join())