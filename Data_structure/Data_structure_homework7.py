# 아래 함수를 수정하시오.
def capitalize_words(string):   
    return string.title()


result = capitalize_words("hello, world!")
print(result)

# 파이썬에서 문자열은 변경 불가능하기 때문에 string.title()을 하면 원본이 바껴서 반환되는 것이 아니라 바꿔서 새로문 문자열을 반환한다.