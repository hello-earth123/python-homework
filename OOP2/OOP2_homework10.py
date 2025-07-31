# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}


    def get_user_info(self):
        try:
            name = input('이름을 입력하세요 : ')
            age = int(input('나이를 입력하세요 : '))
        except ValueError:
            print('나이는 숫자로 입력해야 합니다.')
        else: # except가 실행이 안되면 (에러가 안나면) 실행
            self.user_data['name'] = name
            self.user_data['age'] = age

    def display_user_info(self):
        if not self.user_data:
            print('사용자 정보가 입력되지 않았습니다.')
            return

        print('사용자 정보: ')
        print(f"이름 : {self.user_data['name']}")
        print(f"나이 : {self.user_data['age']}")


user = UserInfo()
user.get_user_info()
user.display_user_info()