class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        try:
            if price >= 0:
                self.price = price # price 값 확인 (0 이상)
            else:
                self.price = f'잘못된 가격'
        except ValueError:
            self.price = f'잘못된 가격'  # 잘못된 가격 처리

    def discount_price(self, rate):
        try:
            if rate > 0 and rate < 1:
                self.price = self.price * (1 - rate)
                return self.price
            else: 
                return f'잘못된 할인율'  # 할인율 확인 (0 ~ 1)
        except ValueError:
            return f'잘못된 할인율'  # 잘못된 할인율 처리

    def __str__(self):
        return f'제목: {self.title}, 작가: {self.author}, 가격: {self.price}'  # 출력 문자열 반환

# ===== 테스트 코드 =====
book1 = Book("Python Basics", "Alice", 25000)
book2 = Book("Data Science", "Bob", -5000)

print(book1)
print("Discounted Price (10%):", book1.discount_price(0.1))
print("Discounted Price (150%):", book1.discount_price(1.5))

print(book2)