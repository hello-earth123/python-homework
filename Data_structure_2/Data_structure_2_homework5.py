# 아래 함수를 수정하시오.
def get_value_from_dict(dictionary, key):
    if key in my_dict.keys():
        return dictionary.get(key)
    else:
        return dictionary.setdefault(key, 'Unknown')

my_dict = {'name': 'Alice', 'age': 25}
result = get_value_from_dict(my_dict, 'name')
print(result)  # Alice

result = get_value_from_dict(my_dict, 'gender')
print(result)  # Unknown
