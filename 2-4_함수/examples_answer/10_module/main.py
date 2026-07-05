from stock_utils import calculate_return_rate


stocks = [
    {"name": "삼성전자", "buy_price": 270000, "current_price": 330000},
    {"name": "현대차", "buy_price": 520000, "current_price": 480000},
]

for stock in stocks:
    return_rate = calculate_return_rate(
        stock["buy_price"],
        stock["current_price"],
    )

    print(f"종목명: {stock['name']}")
    print(f"매수가: {stock['buy_price']}원")
    print(f"현재가: {stock['current_price']}원")
    print(f"수익률: {return_rate}%")

    if stock != stocks[-1]:
        print()
