from pathlib import Path
import csv


data_dir = Path(__file__).parent / "data"
file_path = data_dir / "scores.csv"

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        score = int(row["score"])
        result = "합격" if score >= 60 else "불합격"
        print(f"{row['name']}: {result}")
