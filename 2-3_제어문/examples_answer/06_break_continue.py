orders = [
    "아메리카노",
    "품절",
    "카페라떼",
    "바닐라라떼",
    "마감",
    "딸기라떼",
]

for order in orders:
    if order == "품절":
        print("품절 주문은 건너뜁니다.")
        continue

    if order == "마감":
        print("주문 접수를 마감합니다.")
        break

    print(f"{order}")
