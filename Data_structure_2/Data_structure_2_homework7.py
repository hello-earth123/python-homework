# 아래 함수를 수정하시오.
def get_keys_from_dict(dictionary):
    return dictionary.items() 

def get_all_keys_from_dict(dictionary):
    dict_items = dictionary.items()
    lst = []
    for key, value in dict_items: # dict_items([('person', {'name': 'Alice', 'age': 25}), ('location', 'NY')])
        lst.append(key)
        if type(value) == dict:
            lst.extend(list(value.keys()))
    return lst

# my_dict = {'name': 'Alice', 'age': 25}
# result = get_keys_from_dict(my_dict)
# print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']


#재귀
