class BaseModel:
    PK = 1
    TYPE = 'Basic Model'

    def __init__(self, data_type, title, content, created_at, updated_at):
        self.PK = BaseModel.PK
        self.data_type = data_type 
        self.title = title 
        self.content = content 
        self.created_at = created_at 
        self.updated_at = updated_at
        BaseModel.PK += 1
    
    def save(self):
        print('데이터를 저장합니다.')

class Novel(BaseModel):
    def __init__(self, data_type, title, content, created_at, updated_at, author):
        super().__init__(data_type, title, content, created_at, updated_at)
        self.author = author
class Other(BaseModel):
    TYPE = 'Other Model'
    def __init__(self, data_type, title, content, created_at, updated_at):
        super().__init__(data_type, title, content, created_at, updated_at)
        
    

hong = Novel('소설', '홍길동', '고전 소설', 1618, 1692, '허균')
chun = Novel('소설', '춘향전', '고전 소설', 'unknown', 'unknown', '작자미상')
print('Novel 모델 인스턴스의 PK와 save 메서드')
print(hong.PK)
print(chun.PK)
hong.save()
chun.save()
print(hong.author)
print(chun.author)
print('---')

company = Other('회사', '회사명', '회사 설명', 2000, 2023)
print('Other 모델 인스턴스의 PK와 save 메서드')
print(company.PK)
company.save()

print('---')
print('모델 별 타입')
print(Novel.TYPE)
print(Other.TYPE)
# 속성을 오버라이딩을 하거나 아니면 인스턴스별로 타입이 달라야 한다면 self.type 이런식으로
# 여기서는 BaseModel의 TYPE이 self.TYPE으로 온 것이 아니기 때문에 self.TYPE을 해도 의미 없음