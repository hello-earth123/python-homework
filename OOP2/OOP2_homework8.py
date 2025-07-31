class Dog:
    sound = '멍멍'
    def __init__(self):
        pass

    def __str__(self):
        return f'강아지는 {self.sound} 소리를 냅니다.'
class Cat:
    sound = '야옹'
    def __init__(self):
        pass

    def __str__(self):
        return f'고양이는 {self.sound} 소리를 냅니다.'

class Pet1(Dog, Cat):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.'  

class Pet2(Cat, Dog):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'애완동물은 {self.sound} 소리를 냅니다.' 


dog = Pet1()
cat = Pet2()
print(dog)
print(cat)

print(Pet1.__mro__)
print(Pet2.__mro__)