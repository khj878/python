from pathlib import Path
import csv


data_dir = Path(__file__).parent / "data"
file_path = data_dir / "inventory.csv"

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        stock = int(row["stock"])
        if stock <= 5:
            print(f"재고 확인: {row['name']} ({stock}개)")
