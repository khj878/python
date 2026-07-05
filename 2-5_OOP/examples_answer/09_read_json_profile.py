from pathlib import Path
import json

data_dir = Path(__file__).parent / "data"
file_path = data_dir / "profile.json"

with open(file_path, "r", encoding="utf-8") as file:
    account = json.load(file)

cash = account["cash"]
total_stock_value = 0

print(f"계좌명: {account['account_name']}")
print(f"현금: {cash}원")
print()
print("보유 종목")

for stock in account["stocks"]:
    stock_value = stock["quantity"] * stock["current_price"]
    total_stock_value = total_stock_value + stock_value

    print(f"{stock['name']}: {stock['quantity']}주, 평가금액 {stock_value}원")

total_asset = cash + total_stock_value

print()
print(f"총 자산: {total_asset}원")
