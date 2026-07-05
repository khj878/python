from pathlib import Path
import json


data_dir = Path(__file__).parent / "data"

file_names = [
    "trade_001.json",
    "trade_004.json",
    "trade_002.json",
    "trade_005.json",
    "trade_003.json",
]

for file_name in file_names:
    file_path = data_dir / file_name

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            trade = json.load(file)

        total_price = trade["price"] * trade["quantity"]

        print(
            f"{trade['trade_id']} {trade['stock_name']} "
            f"{trade['order_type']} {trade['quantity']}주"
        )
        print(f"거래 금액: {total_price}원")

    except FileNotFoundError:
        print(f"{file_name}: 파일을 찾을 수 없습니다.")
