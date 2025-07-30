# 아래 클래스를 수정하시오.
class Shape:
    #생성자 메서드
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #인스턴스 메서드
    def calculate_area(self):
        return (self.width * self.height)

    #인스턴스 메서드2
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


shape1 = Shape(5, 3)
perimeter1 = shape1.calculate_perimeter()
print(perimeter1)
