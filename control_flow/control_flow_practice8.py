#보유 중인 도서
list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

#대여 예정 도서
rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

missing_book = []
for list in rental_book:
  
    if list not in list_of_book:
        missing_book.append(list)
        continue
else:
    print('모든 도서가 대여 가능한 상태입니다.')
    
for book_name in missing_book:
    print(f'{book_name} 을/를 보충하여야 합니다.')
    
