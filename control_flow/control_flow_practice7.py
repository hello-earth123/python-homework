#보유 중인 도서
list_of_book = [
    '장화홍련전', #
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전', #
    '만복자서포기', #
    '수성지', #
    '백호집', #
    '원생몽유록', #
    '홍길동전', #
    '장생전', #
    '도문대작',
    '옥루몽',
    '옥련몽',
]

# 대여 예정 도서
rental_list = [
    '장생전', 
    '원생몽유록',
    '이생규장전',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

# for list in rental_list:
#     if list not in list_of_book:
#         print(f'{list} 은/는 보유하고 있지 않습니다.')
#         continue
#     else:
#         print('모든 도서가 대여 가능한 상태입니다.')

# while - else

# for -else
# break문만 관련이 있음
    # break문 만났다? => else 실행 안함
    # break문 안만났다면 => else 실행함.
# continue가 있건 없건 정상 종료(break를 안만났다면)만 되었다면 else문 실행

for list in rental_list:
    if list not in list_of_book:
        print(f'{list} 은/는 보유하고 있지 않습니다.')
        break # break를 하면 for문을 벗어난다
else: # 만약 for문을 돌면서 break를 만나지 않았다면(모든 반복이 완료되어 정상종료되었다면)
    print('모든 도서가 대여 가능한 상태입니다.')