data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
for dict in data:
    for key in key_list:
        if key in dict.keys():
            value = dict.get(key)
            print(f'{key} 은/는 {value}입니다.')

        else:
            value = dict.setdefault(key, 'unknown')
            print(f'{key} 은/는 {value}입니다.')
    print()