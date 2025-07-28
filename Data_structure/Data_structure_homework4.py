# 아래 함수를 수정하시오.
def reverse_string(string):
    return ''.join(reversed(string))    


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH

# 인자로 문자열도 받을 수 있다.
#''.join은 새로운 문자열을 반환할 때 쓰기 좋겠다.
# .join()안에 reversed() built in function을 사용하면 거꾸로 뒤집힌다.
