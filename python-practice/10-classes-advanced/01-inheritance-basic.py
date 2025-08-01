#부모 클래스
class Animal:
    def eat(self):
        print('먹는 중')


#자식 클래스 -> Animal이라는 부모 클래스를 상속 받음
class Dog(Animal): 
    def bark(self):
        print('멍멍')


#인스턴스 생성
my_dog = Dog()
my_dog.bark()


#부모 클래스의 인스턴스 메서드 eat을 호출
my_dog.eat()