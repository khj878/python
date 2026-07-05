from pathlib import Path

project_dir = Path(__file__).parent.parent
data_dir = project_dir / "data"
file_path = data_dir / "stock.txt"

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        print(line)

