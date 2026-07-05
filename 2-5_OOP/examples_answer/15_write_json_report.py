from pathlib import Path
import json


data_dir = Path(__file__).parent / "data"
data_dir.mkdir(exist_ok=True)
file_path = data_dir / "order_record.json"

stock_name = "삼성전자"
order_type = "buy"
quantity = 3
price = 70000
total_price = quantity * price

order_record = {
    "stock_name": stock_name,
    "order_type": order_type,
    "quantity": quantity,
    "price": price,
    "total_price": total_price,
    "status": "completed",
}

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(order_record, file, ensure_ascii=False, indent=4)

print("order_record.json 작성 완료")
