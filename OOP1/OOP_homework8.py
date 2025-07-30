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
    
    def print_info(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'Area: {self.calculate_area()}')
        print(f'Perimeter: {self.calculate_perimeter()}')

    def __str__(self):
        return f'Shape: width={self.width}, height={self.height}'


shape1 = Shape(5, 3)
print(shape1)
