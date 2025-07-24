#사용자가 갖고 있는 책 (대여한 책)
def rental_book(name, number):
    global number_of_book
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

number_of_book = 100

#도서관에 남은 책
def decrease_book(number):
    left = number_of_book-number
    print(f'남은 책의 수 : {left}')

rental_book('홍길동', 3)
rental_book('음준동', 7)