class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def show_info(self):
        print(f"{self.name}는 {self.category} 상품이며, 가격은 {self.price}원입니다.")


product = Product("무선 마우스", 25000, "컴퓨터 주변기기")
product.show_info()
