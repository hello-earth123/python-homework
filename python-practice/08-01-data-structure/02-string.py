# find  .find(x) -> 찾고자하는 x의 첫 번째 위치(인덱스값)르 반환
text = 'banana'
print(text.find('a'))  # 1
print(text.find('z'))  # -1

# index  .index(x) -> .find랑 똑같은데 없으면 -1 반환이 아니고 ValueError를 일으킨다.
print(text.index('a'))  # 1
# print(text.index('z'))  # ValueError: substring not found

# isupper .isupper(문자열) -> 모든 문자열이 대문자로 이루어져있는가? (하나라도 아니면 False)
string1 = 'HELLO'
string2 = 'Hello'
print(string1.isupper())  # True
print(string2.isupper())  # False

# islower .islower() -> 모든 문자열이 소문자로 이루어져있는가? (하나라도 아니면 False)
print(string1.islower())  # False
print(string2.islower())  # False

# isalpha .isalpha() -> 모든 문자열이 영어로 이루어져있는가? (하나라도 아니면 False)
string1 = 'Hello'
string2 = '123heis98576ssh'
print(string1.isalpha())  # True
print(string2.isalpha())  # False

# replace
text = 'Hello, world! world world'
new_text1 = text
new_text2 = text
print(new_text1.replace('world', 'Python'))  # Hello, Python! Python Python
print(new_text2.replace('world', 'Python', 1))  # Hello, Python! world world

# strip
text = '  Hello, world!  '
new_text = text
print(new_text.strip())  # Hello, world!

# split
text = 'Hello, world!'
words1 = text
words2 = text
print(words1.split(','))  # ['Hello', ' world!']
print(words2.split())  # ['Hello,', 'world!']

# join -> 다른 메서드와는 달리 구분자가 먼저 나오고, iterable의 문자열을 연결한 문자열을 반환
# 요소(반복 가능한 객체)를 구분자로 연결해서 다 문자열로 바꿈
words = ['Hello', 'world!']
new_text = '-'.join(words)
print(new_text)  # Hello-world!

# capitalize
text = 'heLLo, woRld!'
new_text1 = text.capitalize()
print(new_text1)  # Hello, world!

# title
new_text2 = text.title()
print(new_text2)  # Hello, World!

# upper
new_text3 = text.upper()
print(new_text3)  # HELLO, WORLD!

# lower
new_text4 = text.lower()
print(new_text4)  # hello, world!

# swapcase
new_text5 = text.swapcase()
print(new_text5)  # HEllO, WOrLD!

