class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    # 인스턴스 메서드
    

# 클래스 호출 -> __init__ 실행
c1 = Counter()
c2 = Counter()

# 인스턴스 메서드 호출
c1.increment()
print(c1.count)
print(c2.count)