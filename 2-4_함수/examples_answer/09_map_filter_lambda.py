trades = [
    {"name": "삼성전자", "type": "buy", "price": 73500, "quantity": 2},
    {"name": "카카오", "type": "sell", "price": 51000, "quantity": 3},
    {"name": "네이버", "type": "buy", "price": 182000, "quantity": 1},
    {"name": "LG에너지솔루션", "type": "sell", "price": 342000, "quantity": 1},
    {"name": "현대차", "type": "buy", "price": 85000, "quantity": 5},
]

fee = 300

buy_trades = filter(lambda trade: trade["type"] == "buy", trades)
buy_stock_names = list(map(lambda trade: trade["name"], buy_trades))
payment_amounts = list(
    map(lambda trade: trade["price"] * trade["quantity"] + fee, buy_trades)
)

print(f"매수 종목: {buy_stock_names}") # ['삼성전자', '네이버', '현대차']
print(f"매수 결제 금액: {payment_amounts}") # []
