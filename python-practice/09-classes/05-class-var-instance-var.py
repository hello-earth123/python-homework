#클래스 변수 vs 인스턴스 변수

class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius


c1 = Circle(5)
c2 = Circle(10)

print(c1.radius)  # 5
print(c2.radius)  # 10

#c1 본인 인스턴스 변수 pi를 생성
c1.pi = 100
print(c1.pi) # 100 
# 본인이 생성한 인스턴스 변수가 클래스 변수와 충돌이 나면 클래스 변수에 접근하지 않고 본인이 생성한 인스턴스 변수로 접근함
#LEGB 룰 처럼 본인의 공간에서 먼저 찾고 나중에 찾으러 밖으러 나감
print(Circle.pi) # 3.14 본인 클래스 변수에서 먼저 찾음
print(c2.pi) # 3.14 -> 본인 인스턴스 변수 pi가 없기 때문에 pi를 찾으러 나감 

# 객체는 속성과 메서드로 이루어짐