class Person:
    # 생성자 메서드
    def __init__(self, name, age): #initialization의 약자 init /  __()__ -> 이런 형태는 매직 메서드라고 한다. 클래스로 뭔가를 생성할 때 사용
        #인스턴스 속성(변수) / 찍어내면 찍어낸 물건만의 독립된 속성(아이덴티티)
        self.name = name # 여기 name은 매직 메서드 안에 name이고 self.name과는 다름
        self.age = age

    def introduce(self):
        print(f'반갑습니다. 저는 {self.name}이고, 나이는 {self.age}살 입니다.') #그냥 name과 age가 아니다. self.name과 self.age이다. 애초에 쓸 수도 없음 함수 안에 없음


