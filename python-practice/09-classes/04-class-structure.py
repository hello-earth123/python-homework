class Circle:
    # 클래스 변수
    pi = 3.14 # 클래스 변수는 모든 인스턴스가 공유하는 속성(변수) # 클래스 내부에서 직접 정의

    # 생성자 메서드를 만들면서 클래스 시작 (initialization)
    def __init__(self, radius): # '인스턴스 생성시에' 자동 호출되는 특별한 메서드(매직 메서드) # 인스턴스 변수의 초기화를 담당
        self.radius = radius    # 각 인스턴스의 고유한 속성 # self.radius의 radius랑 = radius 는 맞출 필요는 없지만 맞추는게 좋다. (햇갈리니까)
    


# 인스턴스 생성 / 이 때 매직 메서드가 자동 호출
c1 = Circle(1)
c2 = Circle(2)

# 인스턴스 변수(속성) 접근
print(c1.radius)
print(c2.radius)

# 클래스 변수(공통 속성) 접근
print(c1.pi)
print(c1.pi)

