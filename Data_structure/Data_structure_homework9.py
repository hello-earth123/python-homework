# 아래 함수를 수정하시오.
def count_character(string, target):
    count = 0
    for text in string:
        if target == text:
            count += 1

    return count

result = count_character("Hello, World!", "o")
print(result)  # 2
