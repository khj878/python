from pathlib import Path
import csv


data_dir = Path(__file__).parent / "data"
data_dir.mkdir(exist_ok=True)
file_path = data_dir / "student_results.csv"

students = [
    {"name": "철수", "score": 90},
    {"name": "영희", "score": 55},
    {"name": "민수", "score": 75},
]

with open(file_path, "w", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score", "result"])
    writer.writeheader()

    for student in students:
        score = student["score"]
        result = "합격" if score >= 60 else "불합격"
        writer.writerow({
            "name": student["name"],
            "score": score,
            "result": result,
        })

print("student_results.csv 작성 완료")
