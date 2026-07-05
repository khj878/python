class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


product = Product("키보드", 30000, 5)

print(f"상품명: {product.name}")
print(f"가격: {product.price}원")
print(f"재고: {product.stock}개")
