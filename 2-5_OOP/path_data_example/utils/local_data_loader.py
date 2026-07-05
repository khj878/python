from pathlib import Path

data_dir = Path("data")
file_path = data_dir / "stock.txt"

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        print(line)