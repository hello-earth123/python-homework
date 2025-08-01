class Animal:
    def eat(self):
        print('Animal이 먹는 중')


class Dog(Animal):#Dog 입장에서는 부모 클래스까지 올라가서 찾기 전에 본인 클래스의 메서드에서 찾음
                  #파라미터 구조를 동일하게 유지하자 -> 오류는 아니지만 객체 지향 프로그래밍의 핵심 개념인 다형성을 위반함
    # 오버라이딩 (부모 클래스 Animal의 eat 메서드를 재정의)
    def eat(self):
        print(f'Dog가먹는중')

my_dog = Dog()
my_dog.eat()

# 오버로딩 (파이썬 미지원)
# class Example:
#     def do_something(self, x):
#         print('첫 번째 do_something 메서드:', x)

#     # 파이썬에서는 메서드가 "이름"이 같으면 앞선 정의를 덮어써버림
#     def do_something(self, x, y):
#         print('두 번째 do_something 메서드:', x, y)


# example = Example()
# # TypeError: do_something() missing 1 required positional argument: 'y'
# example.do_something(10)
