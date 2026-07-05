menus = ["아메리카노", "카페라떼", "레몬에이드"]
quantities = [2, 1, 3]
prices = [3000, 4500, 4000]

total = 0

for menu, quantity, price in zip(menus, quantities, prices):
    subtotal = quantity * price
    total = total + subtotal

    print(f"{menu} {quantity}잔 x {price}원 = {subtotal}원")

print(f"총 결제 금액: {total}원")
