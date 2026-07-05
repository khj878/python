cart = ["키보드", "마우스"]

cart.append("모니터")
cart.remove("마우스")
popped_item = cart.pop(0)

print(f"현재 장바구니: {cart}")
print(f"꺼낸 상품: {popped_item}")
print(f"상품 개수: {len(cart)}")
