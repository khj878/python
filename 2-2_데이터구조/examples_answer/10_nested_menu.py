menu_board = {
    "drinks": ["아메리카노", "카페라떼"],
    "desserts": ["쿠키", "치즈케이크"],
}

first_drink = menu_board["drinks"][0]
last_dessert = menu_board["desserts"][-1]
menu_board["drinks"].append("레몬에이드")

print(f"첫 번째 음료: {first_drink}")
print(f"마지막 디저트: {last_dessert}")
print(f"수정된 음료 목록: {menu_board['drinks']}")
