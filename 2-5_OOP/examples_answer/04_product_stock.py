class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def get_details(self):
        return f"{self.name}: {self.price}원, 재고 {self.stock}개"

    def decrease_stock(self, amount):
        if self.stock < amount:
            return "재고가 부족합니다."

        self.stock -= amount
        return "판매 완료"


product = Product("모니터", 200000, 3)

print(f"판매 전: {product.get_details()}")
print(f"판매 결과: {product.decrease_stock(2)}")
print(f"판매 후: {product.get_details()}")
