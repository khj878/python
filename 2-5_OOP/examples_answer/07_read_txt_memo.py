from pathlib import Path


data_dir = Path(__file__).parent / "data"
file_path = data_dir / "read_memo.txt"

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())
